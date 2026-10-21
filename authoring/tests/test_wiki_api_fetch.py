"""wiki_api_fetch: retries transient errors (429/502/503/504) and keeps 404 behaviour for missing pages.

Runs against a local HTTP server, never the live wiki.
"""
import json
import sys
import threading
import unittest
import urllib.error
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
from unittest import mock

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import wiki_api_fetch as W  # noqa: E402

PAGE = {"query": {"pages": [{"title": "Main Page", "revisions": [{"slots": {"main": {"content": "hello"}}}]}]}}
MISSING = {"query": {"normalized": [{"from": "Zz_missing", "to": "Zz missing"}],
                     "pages": [{"title": "Zz missing", "missing": True}]}}


class _Handler(BaseHTTPRequestHandler):
    script: list = []  # (status, body) per request; the last entry repeats
    seen: list = []

    def do_GET(self):  # noqa: N802
        type(self).seen.append((self.path, self.headers.get("User-Agent")))
        i = min(len(type(self).seen) - 1, len(type(self).script) - 1)
        status, body = type(self).script[i]
        data = json.dumps(body).encode() if body is not None else b"error"
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, *a):
        pass


class WikiApiFetchTest(unittest.TestCase):
    def setUp(self):
        self.srv = HTTPServer(("127.0.0.1", 0), _Handler)
        threading.Thread(target=self.srv.serve_forever, daemon=True).start()
        _Handler.seen = []
        self.patches = [
            mock.patch.object(W, "API", f"http://127.0.0.1:{self.srv.server_port}/api.php"),
            mock.patch.object(W, "MIN_INTERVAL", 0),
            mock.patch.object(W.time, "sleep", lambda s: None),
        ]
        for p in self.patches:
            p.start()

    def tearDown(self):
        for p in self.patches:
            p.stop()
        self.srv.shutdown()
        self.srv.server_close()

    def test_retries_502_504_then_succeeds(self):
        _Handler.script = [(502, None), (504, None), (200, PAGE)]
        self.assertEqual(W.fetch_raw("Main Page"), "hello")
        self.assertEqual(len(_Handler.seen), 3)
        self.assertTrue(_Handler.seen[0][1].startswith("SWCCGWikiTools/"))

    def test_retries_429_503(self):
        _Handler.script = [(429, None), (503, None), (200, PAGE)]
        self.assertEqual(W.fetch_raw_many(["Main Page"]), {"Main Page": "hello"})
        self.assertEqual(len(_Handler.seen), 3)

    def test_gives_up_after_tries(self):
        _Handler.script = [(504, None)]
        with self.assertRaises(urllib.error.HTTPError) as cm:
            W.fetch_raw("Main Page")
        self.assertEqual(cm.exception.code, 504)
        self.assertEqual(len(_Handler.seen), 7)

    def test_other_errors_not_retried(self):
        _Handler.script = [(500, None), (200, PAGE)]
        with self.assertRaises(urllib.error.HTTPError) as cm:
            W.fetch_raw("Main Page")
        self.assertEqual(cm.exception.code, 500)
        self.assertEqual(len(_Handler.seen), 1)

    def test_missing_page_404_unchanged(self):
        _Handler.script = [(200, MISSING)]
        self.assertEqual(W.fetch_raw_many(["Zz_missing"]), {"Zz_missing": None})
        with self.assertRaises(urllib.error.HTTPError) as cm:
            W.fetch_raw("Zz_missing")
        self.assertEqual(cm.exception.code, 404)
        self.assertEqual(str(cm.exception), "HTTP Error 404: Not Found")


if __name__ == "__main__":
    unittest.main()
