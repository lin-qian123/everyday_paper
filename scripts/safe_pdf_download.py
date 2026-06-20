#!/usr/bin/env python
"""Robust PDF downloader for automation runs.

Features:
- Retries with current env proxies first, then direct (proxy bypass)
- Accepts multiple candidate URLs and optional DOI fallback
- Validates content as PDF (header/content-type)
- Uses Python stdlib only (no third-party dependencies)
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Iterable, Optional

PDF_MAGIC = b"%PDF-"
TIMEOUT = 45
PROXY_ENV_KEYS = (
    "http_proxy",
    "https_proxy",
    "all_proxy",
    "HTTP_PROXY",
    "HTTPS_PROXY",
    "ALL_PROXY",
)


def normalize_doi(doi: str) -> str:
    return doi.strip().removeprefix("https://doi.org/").removeprefix("http://doi.org/")


def _build_opener(trust_env: bool) -> urllib.request.OpenerDirector:
    if trust_env:
        return urllib.request.build_opener()
    return urllib.request.build_opener(urllib.request.ProxyHandler({}))


def _fetch_url(url: str, accept: str, trust_env: bool, timeout: int = TIMEOUT) -> tuple[Optional[bytes], dict[str, str], Optional[str], Optional[str]]:
    opener = _build_opener(trust_env)
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "everyday-paper-bot/1.0 (+local automation)",
            "Accept": accept,
        },
    )
    try:
        with opener.open(req, timeout=timeout) as resp:
            content = resp.read()
            headers = {k.lower(): v for k, v in resp.headers.items()}
            final_url = resp.geturl()
            return content, headers, final_url, None
    except urllib.error.HTTPError as e:
        return None, {}, None, f"HTTP {e.code}"
    except Exception as e:  # noqa: BLE001
        data, headers, final_url, curl_err = _fetch_url_with_curl(
            url=url,
            accept=accept,
            trust_env=trust_env,
            timeout=timeout,
        )
        if data is not None or curl_err:
            return data, headers, final_url, curl_err
        return None, {}, None, f"{type(e).__name__}: {e}"


def _fetch_url_with_curl(url: str, accept: str, trust_env: bool, timeout: int = TIMEOUT) -> tuple[Optional[bytes], dict[str, str], Optional[str], Optional[str]]:
    curl_bin = os.getenv("EVERYDAY_PAPER_CURL_BIN", "curl")
    with tempfile.NamedTemporaryFile() as header_file:
        cmd = [
            curl_bin,
            "-L",
            "-sS",
            "-D",
            header_file.name,
            "-A",
            "everyday-paper-bot/1.0 (+local automation)",
            "-H",
            f"Accept: {accept}",
            "--max-time",
            str(timeout),
            "--connect-timeout",
            str(min(timeout, 15)),
            url,
        ]
        env = os.environ.copy()
        if not trust_env:
            for key in PROXY_ENV_KEYS:
                env.pop(key, None)
        try:
            proc = subprocess.run(cmd, capture_output=True, env=env, check=False)
        except Exception as e:  # noqa: BLE001
            return None, {}, None, f"{type(e).__name__}: {e}"

        header_text = Path(header_file.name).read_text(errors="replace")
        headers, status_code, final_url = _parse_curl_headers(header_text, url)
        if proc.returncode == 0:
            return proc.stdout, headers, final_url, None
        if status_code is not None:
            return None, headers, final_url, f"HTTP {status_code}"
        stderr = proc.stderr.decode("utf-8", errors="replace").strip()
        if stderr:
            return None, headers, final_url, f"curl: {stderr}"
        return None, headers, final_url, f"curl exit {proc.returncode}"


def _parse_curl_headers(header_text: str, fallback_url: str) -> tuple[dict[str, str], Optional[int], Optional[str]]:
    blocks = [b.strip() for b in header_text.split("\r\n\r\n") if b.strip()]
    if not blocks:
        return {}, None, fallback_url
    last = blocks[-1]
    lines = [line.strip() for line in last.splitlines() if line.strip()]
    if not lines:
        return {}, None, fallback_url
    status = None
    status_match = re.match(r"HTTP/\S+\s+(\d{3})", lines[0])
    if status_match:
        status = int(status_match.group(1))
    headers: dict[str, str] = {}
    for line in lines[1:]:
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        headers[key.lower().strip()] = value.strip()
    final_url = headers.get("location") or fallback_url
    return headers, status, final_url


def _extract_pdf_candidates_from_html(html: str, base_url: str) -> list[str]:
    out: list[str] = []
    seen = set()

    def add(url: Optional[str]) -> None:
        if not url:
            return
        abs_url = urllib.parse.urljoin(base_url, url.strip())
        if not abs_url or abs_url in seen:
            return
        seen.add(abs_url)
        out.append(abs_url)

    for match in re.findall(r'citation_pdf_url[^>]*content="([^"]+)"', html):
        add(match)
    for match in re.findall(r'https://[^"\']+\.pdf[^"\']*', html):
        add(match)
    for match in re.findall(r'/core/services/aop-cambridge-core/content/view/[^"\']+\.pdf[^"\']*', html):
        add(match)
    return out


def fetch_json(url: str, timeout: int = 30) -> Optional[dict]:
    for trust_env in (True, False):
        data, _headers, _final, err = _fetch_url(
            url=url,
            accept="application/json,*/*;q=0.8",
            trust_env=trust_env,
            timeout=timeout,
        )
        if data is None:
            continue
        try:
            parsed = json.loads(data.decode("utf-8", errors="replace"))
        except Exception:
            continue
        if isinstance(parsed, dict):
            return parsed
    return None


def unpaywall_pdf_candidates(doi: str) -> list[str]:
    email = os.getenv("UNPAYWALL_EMAIL", "open-access@example.com")
    doi_norm = normalize_doi(doi)
    doi_enc = urllib.parse.quote(doi_norm, safe="")
    email_enc = urllib.parse.quote(email, safe="@._+-")
    url = f"https://api.unpaywall.org/v2/{doi_enc}?email={email_enc}"
    data = fetch_json(url)
    if not isinstance(data, dict):
        return []

    out: list[str] = []
    seen = set()

    def add(u: Optional[str]) -> None:
        if not u:
            return
        u = u.strip()
        if not u or u in seen:
            return
        seen.add(u)
        out.append(u)

    best = data.get("best_oa_location") or {}
    if isinstance(best, dict):
        add(best.get("url_for_pdf"))
        add(best.get("url"))

    for loc in data.get("oa_locations") or []:
        if not isinstance(loc, dict):
            continue
        add(loc.get("url_for_pdf"))
        add(loc.get("url"))

    return out


def crossref_landing_candidates(doi: str) -> list[str]:
    doi_norm = normalize_doi(doi)
    doi_enc = urllib.parse.quote(doi_norm, safe="")
    data = fetch_json(f"https://api.crossref.org/works/{doi_enc}")
    if not isinstance(data, dict):
        return []
    msg = data.get("message")
    if not isinstance(msg, dict):
        return []
    url = msg.get("URL")
    if isinstance(url, str) and url.strip():
        return [url.strip()]
    return []


def doi_redirect_landing(doi: str, timeout: int = 30) -> Optional[str]:
    doi_url = f"https://doi.org/{normalize_doi(doi)}"
    for trust_env in (True, False):
        _data, _headers, final_url, err = _fetch_url(
            url=doi_url,
            accept="text/html,*/*;q=0.8",
            trust_env=trust_env,
            timeout=timeout,
        )
        if err:
            continue
        landing = (final_url or "").strip()
        if landing and landing != doi_url:
            return landing
    return None


def normalize_candidates(urls: Iterable[str], doi: Optional[str]) -> list[str]:
    out: list[str] = []
    seen = set()

    def add(u: str) -> None:
        u = u.strip()
        if not u or u in seen:
            return
        seen.add(u)
        out.append(u)

        m = re.match(r"https?://www\\.nature\\.com/articles/([^/?#]+)$", u)
        if m:
            pdf_u = f"https://www.nature.com/articles/{m.group(1)}.pdf"
            if pdf_u not in seen:
                seen.add(pdf_u)
                out.append(pdf_u)

    for u in urls:
        add(u)

    if doi:
        doi_norm = normalize_doi(doi)
        for u in crossref_landing_candidates(doi_norm):
            add(u)
        landing = doi_redirect_landing(doi_norm)
        if landing:
            add(landing)
        add(f"https://doi.org/{doi_norm}")
        for u in unpaywall_pdf_candidates(doi_norm):
            add(u)

    return out


def is_pdf(content: bytes, headers: dict[str, str]) -> bool:
    ctype = (headers.get("content-type") or "").lower()
    if "application/pdf" in ctype:
        return True
    return content[:5] == PDF_MAGIC


def classify_failures(errors: list[str]) -> str:
    joined = "\n".join(errors).lower()
    if not joined:
        return "unknown"
    if "validate.perfdrive.com" in joined or "botmanager" in joined or "radware" in joined:
        return "publisher_bot_wall"
    if (
        "operation not permitted" in joined
        or "failed to establish a new connection" in joined
        or "failed to connect to 127.0.0.1" in joined
        or "couldn't connect to server" in joined
    ):
        return "runtime_proxy_blocked"
    if (
        "nodename nor servname provided" in joined
        or "failed to resolve" in joined
        or "could not resolve host" in joined
    ):
        return "runtime_dns_failure"
    if "http 403" in joined:
        return "publisher_http_403"
    if "cookies_not_supported" in joined:
        return "publisher_cookie_wall"
    if "not pdf" in joined and "text/html" in joined:
        return "html_instead_of_pdf"
    if "http 401" in joined or "http 429" in joined:
        return "publisher_access_limited"
    return "unknown"


def fetch_pdf(url: str, trust_env: bool, timeout: int = TIMEOUT) -> tuple[Optional[bytes], Optional[str], list[str]]:
    data, headers, final_url, err = _fetch_url(
        url=url,
        accept="application/pdf,application/octet-stream;q=0.9,*/*;q=0.5",
        trust_env=trust_env,
        timeout=timeout,
    )
    if data is None:
        return None, err, []
    if not is_pdf(data, headers):
        html = data.decode("utf-8", errors="replace")
        extra = _extract_pdf_candidates_from_html(html, final_url or url)
        return None, f"not pdf (content-type={headers.get('content-type', '')})", extra
    return data, None, []


def main() -> int:
    p = argparse.ArgumentParser(description="Safely download PDF with proxy and OA fallback")
    p.add_argument("--url", action="append", default=[], help="Candidate URL (repeatable)")
    p.add_argument("--doi", default=None, help="Optional DOI for fallback resolution")
    p.add_argument("--output", required=True, help="Output PDF path")
    p.add_argument("--report-json", default=None, help="Optional JSON report path")
    args = p.parse_args()

    candidates = normalize_candidates(args.url, args.doi)
    if not candidates:
        print("No candidate URLs provided", file=sys.stderr)
        return 2

    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)

    last_errors: list[str] = []
    queued = list(candidates)
    seen = set(queued)
    while queued:
        url = queued.pop(0)
        for trust_env in (True, False):
            payload, err, extra_candidates = fetch_pdf(url=url, trust_env=trust_env)
            mode = "env-proxy" if trust_env else "direct"
            if payload is None:
                for extra in extra_candidates:
                    if extra not in seen:
                        seen.add(extra)
                        queued.append(extra)
                last_errors.append(f"[{mode}] {url} -> {err}")
                continue
            output.write_bytes(payload)
            print(f"Downloaded: {output} ({len(payload)} bytes) from {url} via {mode}")
            if args.report_json:
                Path(args.report_json).write_text(json.dumps({
                    "ok": True,
                    "output": str(output),
                    "source_url": url,
                    "mode": mode,
                    "attempts": last_errors,
                }, ensure_ascii=False, indent=2) + "\n")
            return 0

    print("Failed to download PDF. Attempts:", file=sys.stderr)
    for e in last_errors:
        print(f"- {e}", file=sys.stderr)
    if args.report_json:
        Path(args.report_json).write_text(json.dumps({
            "ok": False,
            "output": str(output),
            "attempts": last_errors,
            "failure_class": classify_failures(last_errors),
        }, ensure_ascii=False, indent=2) + "\n")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
