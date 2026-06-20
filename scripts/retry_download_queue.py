#!/usr/bin/env python
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
RETRY_PATH = ROOT / "state/daily_retry_candidates.json"
PROCESSED_PATH = ROOT / "state/processed_articles.json"
DOWNLOADER = ROOT / "scripts/safe_pdf_download.py"


def norm_title(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s]", " ", s)
    s = re.sub(r"\s+", " ", s)
    return s


def guess_source_family(url: str, doi: str | None = None, journal: str | None = None) -> str:
    url = (url or "").lower()
    doi = (doi or "").lower()
    journal = (journal or "").lower()
    if "cambridge.org" in url:
        return "cambridge"
    if "nature.com" in url:
        return "nature"
    if "sciencedirect.com" in url or "elsevier" in url:
        return "elsevier"
    if "iop" in url or "iopscience" in url or doi.startswith("10.1088/") or "new journal of physics" in journal:
        return "iop"
    return "other"


def load_json(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return json.loads(path.read_text() or "[]")


def upsert_processed(rows: list[dict[str, Any]], item: dict[str, Any], pdf_path: str) -> None:
    doi = (item.get("doi") or "").lower()
    title_key = norm_title(item["title"])
    for row in rows:
        if doi and (row.get("doi") or "").lower() == doi:
            row["pdf_path"] = pdf_path
            row.setdefault("note_path", None)
            row["processed_date"] = datetime.now().date().isoformat()
            return
        if row.get("normalized_title") == title_key:
            row["pdf_path"] = pdf_path
            row.setdefault("note_path", None)
            row["processed_date"] = datetime.now().date().isoformat()
            return
    rows.append(
        {
            "title": item["title"],
            "normalized_title": title_key,
            "doi": item.get("doi"),
            "source_url": item.get("source_url"),
            "journal": item.get("journal"),
            "publication_date": item.get("publication_date"),
            "processed_date": datetime.now().date().isoformat(),
            "pdf_path": pdf_path,
            "note_path": None,
        }
    )


def build_cmd(item: dict[str, Any], report_path: str) -> list[str]:
    cmd = [sys.executable, str(DOWNLOADER)]
    pdf_hint = item.get("pdf_hint_url")
    if pdf_hint:
        cmd += ["--url", pdf_hint]
    if item.get("source_url"):
        cmd += ["--url", item["source_url"]]
    if item.get("doi"):
        cmd += ["--doi", item["doi"]]
    cmd += ["--output", str(ROOT / item["output_pdf"]), "--report-json", report_path]
    return cmd


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--source-family", choices=["cambridge", "nature", "elsevier", "iop", "other", "all"], default="all")
    ap.add_argument("--limit", type=int, default=0)
    args = ap.parse_args()

    retry_rows = load_json(RETRY_PATH)
    processed_rows = load_json(PROCESSED_PATH)

    remaining: list[dict[str, Any]] = []
    successes: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    handled = 0

    for item in retry_rows:
        family = guess_source_family(item.get("source_url", ""), item.get("doi"), item.get("journal"))
        if args.source_family != "all" and family != args.source_family:
            remaining.append(item)
            continue
        if args.limit and handled >= args.limit:
            remaining.append(item)
            continue
        handled += 1

        with tempfile.TemporaryDirectory() as tmpdir:
            report_path = str(Path(tmpdir) / "report.json")
            cmd = build_cmd(item, report_path)
            proc = subprocess.run(cmd, cwd=str(ROOT), capture_output=True, text=True)
            report = json.loads(Path(report_path).read_text()) if Path(report_path).exists() else {}

        item["last_retry_at"] = datetime.now().astimezone().isoformat(timespec="seconds")
        item["retry_count"] = int(item.get("retry_count") or item.get("failure_count") or 0) + 1
        item["attempt_cmd"] = " ".join(subprocess.list2cmdline([part]) if (" " in part or "(" in part or ")" in part) else part for part in cmd)
        item["stdout"] = proc.stdout
        item["stderr"] = proc.stderr
        item["last_failure_class"] = report.get("failure_class")
        item["source_family"] = family

        if proc.returncode == 0 and report.get("ok"):
            upsert_processed(processed_rows, item, item["output_pdf"])
            successes.append(
                {
                    "title": item["title"],
                    "doi": item.get("doi"),
                    "output_pdf": item["output_pdf"],
                    "source_family": family,
                }
            )
            continue

        item["failure_count"] = item["retry_count"]
        failures.append(
            {
                "title": item["title"],
                "doi": item.get("doi"),
                "failure_class": item.get("last_failure_class"),
                "source_family": family,
            }
        )
        remaining.append(item)

    RETRY_PATH.write_text(json.dumps(remaining, ensure_ascii=False, indent=2) + "\n")
    PROCESSED_PATH.write_text(json.dumps(processed_rows, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({
        "handled": handled,
        "successes": successes,
        "failures": failures,
        "remaining_retry_count": len(remaining),
        "processed_count": len(processed_rows),
    }, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
