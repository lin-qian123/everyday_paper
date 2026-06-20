import importlib.util
import json
import tempfile
import unittest
from unittest import mock
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "scripts" / "safe_pdf_download.py"
SPEC = importlib.util.spec_from_file_location("safe_pdf_download", MODULE_PATH)
MODULE = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
SPEC.loader.exec_module(MODULE)


class SafePdfDownloadTests(unittest.TestCase):
    def test_classify_failures(self) -> None:
        self.assertEqual(
            MODULE.classify_failures(["[env-proxy] x -> URLError: <urlopen error [Errno 1] Operation not permitted>"]),
            "runtime_proxy_blocked",
        )
        self.assertEqual(
            MODULE.classify_failures(["[env-proxy] x -> curl: curl: (7) Failed to connect to 127.0.0.1 port 1087 after 0 ms: Couldn't connect to server"]),
            "runtime_proxy_blocked",
        )
        self.assertEqual(
            MODULE.classify_failures(["[direct] x -> curl: curl: (6) Could not resolve host: www.cambridge.org"]),
            "runtime_dns_failure",
        )
        self.assertEqual(
            MODULE.classify_failures(["[direct] x -> HTTP 403"]),
            "publisher_http_403",
        )
        self.assertEqual(
            MODULE.classify_failures(["[direct] x -> not pdf (content-type=text/html; charset=UTF-8) https://www.nature.com/articles/foo?error=cookies_not_supported"]),
            "publisher_cookie_wall",
        )
        self.assertEqual(
            MODULE.classify_failures(["[direct] x -> not pdf (content-type=text/html) https://validate.perfdrive.com/abc?ssk=botmanager_support@radware.com"]),
            "publisher_bot_wall",
        )

    def test_extracts_cambridge_pdf_candidates_from_html(self) -> None:
        html = """
        <html>
          <head>
            <meta name="citation_pdf_url" content="https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7455A103DE0717CC117130D01914BF65/S209547192610139Xa.pdf/div-class-title-dual-picosecond-laser-driven-generation-of-mv-m-giant-electromagnetic-pulses-div.pdf">
          </head>
          <body>
            <a href="/core/services/aop-cambridge-core/content/view/7455A103DE0717CC117130D01914BF65/S209547192610139Xa.pdf/dual-picosecond-laser-driven-generation-of-mvm-giant-electromagnetic-pulses.pdf">PDF</a>
          </body>
        </html>
        """
        candidates = MODULE._extract_pdf_candidates_from_html(
            html,
            "https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/dualpicosecondlaserdriven-generation-of-mvm-giant-electromagnetic-pulses/7455A103DE0717CC117130D01914BF65",
        )
        self.assertIn(
            "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7455A103DE0717CC117130D01914BF65/S209547192610139Xa.pdf/div-class-title-dual-picosecond-laser-driven-generation-of-mv-m-giant-electromagnetic-pulses-div.pdf",
            candidates,
        )
        self.assertIn(
            "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/7455A103DE0717CC117130D01914BF65/S209547192610139Xa.pdf/dual-picosecond-laser-driven-generation-of-mvm-giant-electromagnetic-pulses.pdf",
            candidates,
        )

    def test_fetch_pdf_returns_extracted_candidates_for_html_landing_page(self) -> None:
        article_url = "https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/example/ABC123"
        pdf_url = "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/ABC123/S209547192610139Xa.pdf/example.pdf"
        html = f"""
        <html>
          <head>
            <meta name="citation_pdf_url" content="{pdf_url}">
          </head>
        </html>
        """.encode()

        with mock.patch.object(
            MODULE,
            "_fetch_url",
            return_value=(html, {"content-type": "text/html; charset=utf-8"}, article_url, None),
        ):
            payload, err, extra = MODULE.fetch_pdf(article_url, trust_env=True)

        self.assertIsNone(payload)
        self.assertIn("not pdf", err)
        self.assertIn(pdf_url, extra)

    def test_main_follows_extracted_pdf_candidate_from_html_landing_page(self) -> None:
        article_url = "https://www.cambridge.org/core/journals/high-power-laser-science-and-engineering/article/example/ABC123"
        pdf_url = "https://www.cambridge.org/core/services/aop-cambridge-core/content/view/ABC123/S209547192610139Xa.pdf/example.pdf"
        html = f"""
        <html>
          <head>
            <meta name="citation_pdf_url" content="{pdf_url}">
          </head>
        </html>
        """.encode()
        pdf_bytes = b"%PDF-1.7 test payload"

        def fake_fetch(url: str, accept: str, trust_env: bool, timeout: int = MODULE.TIMEOUT):
            if url == article_url:
                return html, {"content-type": "text/html; charset=utf-8"}, article_url, None
            if url == pdf_url:
                return pdf_bytes, {"content-type": "application/pdf"}, pdf_url, None
            raise AssertionError(f"unexpected url {url}")

        with tempfile.TemporaryDirectory() as tmpdir, \
             mock.patch.object(MODULE, "_fetch_url", side_effect=fake_fetch), \
             mock.patch("sys.argv", ["safe_pdf_download.py", "--url", article_url, "--output", f"{tmpdir}/out.pdf"]):
            rc = MODULE.main()
            output = Path(tmpdir) / "out.pdf"
            written = output.read_bytes()

        self.assertEqual(rc, 0)
        self.assertEqual(written, pdf_bytes)

    def test_report_json_written_on_failure(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir, \
             mock.patch.object(MODULE, "_fetch_url", return_value=(None, {}, None, "HTTP 403")), \
             mock.patch("sys.argv", [
                 "safe_pdf_download.py",
                 "--url",
                 "https://example.com/file.pdf",
                 "--output",
                 f"{tmpdir}/out.pdf",
                 "--report-json",
                 f"{tmpdir}/report.json",
             ]):
            rc = MODULE.main()
            report = json.loads((Path(tmpdir) / "report.json").read_text())

        self.assertEqual(rc, 1)
        self.assertFalse(report["ok"])
        self.assertEqual(report["failure_class"], "publisher_http_403")


if __name__ == "__main__":
    unittest.main()
