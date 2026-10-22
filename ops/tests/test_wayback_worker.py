"""Tests for the capture verification in ops/wayback_worker.py. Run: python3 -m unittest discover -s ops/tests"""
import hashlib
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_worker as W  # noqa: E402

CAP = "https://web.archive.org/web/20261020174512/https://res.starwarsccg.org/legacyblocks/VirtualBlock7_1.pdf"
PDF = b"%PDF-1.4 fake pdf bytes " * 100
PAGE = (b"<!DOCTYPE html><html><head><title>Ultimate Power Rules Questions</title><script>var x=1;</script></head>"
        b"<body><h1>Ultimate Power Rules Questions</h1><p>Post your rules questions about Virtual Block 7.1 "
        b"Ultimate Power here. The set came out on 18 June 2010.</p></body></html>")


def resp(body, ctype="application/pdf", status=200):
    return {"status": status, "ctype": ctype, "sha256": hashlib.sha256(body).hexdigest(), "size": len(body), "body": body}


def fake_get(table):
    def get(url):
        if url not in table:
            raise AssertionError(f"unexpected fetch {url}")
        r = table[url]
        if isinstance(r, Exception):
            raise r
        return r
    return get


class IdUrl(unittest.TestCase):
    def test_id_url(self):
        self.assertEqual(W.id_url(CAP), "https://web.archive.org/web/20261020174512id_/https://res.starwarsccg.org/legacyblocks/VirtualBlock7_1.pdf")
        self.assertEqual(W.id_url("https://web.archive.org/web/20261020174512if_/https://x.org/"),
                         "https://web.archive.org/web/20261020174512id_/https://x.org/")


class Verify(unittest.TestCase):
    src = "https://res.starwarsccg.org/legacyblocks/VirtualBlock7_1.pdf"

    def test_file_sha256_match(self):
        st, info = W.verify(self.src, CAP, fake_get({W.id_url(CAP): resp(PDF), self.src: resp(PDF)}))
        self.assertEqual(st, "verified")
        self.assertEqual(info["method"], "sha256")
        self.assertEqual(info["sha256"], hashlib.sha256(PDF).hexdigest())

    def test_file_sha256_mismatch(self):
        st, info = W.verify(self.src, CAP, fake_get({W.id_url(CAP): resp(PDF + b"x"), self.src: resp(PDF)}))
        self.assertEqual(st, "unverified")
        self.assertIn("differs", info["reason"])

    def test_html_text_match_ignores_scripts_and_markup(self):
        url = "https://www.decktech.net/x/"
        cap = "https://web.archive.org/web/20261020174512/" + url
        live = PAGE.replace(b"var x=1;", b"var x=2; tracking()").replace(b"<h1>", b"<h1 class='big'>")
        st, info = W.verify(url, cap, fake_get({W.id_url(cap): resp(PAGE, "text/html; charset=utf-8"),
                                                url: resp(live, "text/html; charset=utf-8")}))
        self.assertEqual(st, "verified")
        self.assertEqual(info["method"], "text")
        self.assertGreaterEqual(info["text_match"], 0.99)

    def test_html_text_differs(self):
        url = "https://example.org/p"
        cap = "https://web.archive.org/web/20261020174512/" + url
        other = b"<html><body><p>Completely different content about something else entirely.</p></body></html>"
        st, info = W.verify(url, cap, fake_get({W.id_url(cap): resp(other, "text/html"), url: resp(PAGE, "text/html")}))
        self.assertEqual(st, "unverified")
        self.assertLess(info["text_match"], W.TEXT_MATCH)

    def test_cloudflare_capture_is_unverified(self):
        url = "https://swccg.com/snapshots/forum/t1.html"
        cap = "https://web.archive.org/web/20261020174512/" + url
        cf = b"<html><head><title>Just a moment...</title></head><body>cf-chl- challenge</body></html>"
        st, info = W.verify(url, cap, fake_get({W.id_url(cap): resp(cf, "text/html"), url: resp(PAGE, "text/html")}))
        self.assertEqual(st, "unverified")
        self.assertIn("Cloudflare", info["reason"])

    def test_source_unreachable_retries_then_gives_up(self):
        e = {"capture": CAP, "status": "ok", "last": "2026-10-20T00:00:00Z"}
        get = fake_get({W.id_url(CAP): resp(PDF), self.src: W.VerifyRetry("URLError: timed out")})
        for i in range(W.VERIFY_TRIES):
            self.assertTrue(W.verify_entry(self.src, e, get))
            self.assertEqual(e["status"], "ok" if i < W.VERIFY_TRIES - 1 else "unverified")
        self.assertIn("could not fetch", e["verify"]["reason"])

    def test_capture_403_counts_against_the_entry(self):
        e = {"capture": CAP, "status": "ok", "last": "2026-10-20T00:00:00Z"}
        get = fake_get({W.id_url(CAP): resp(b"", status=403)})
        for _ in range(W.VERIFY_TRIES):
            self.assertTrue(W.verify_entry(self.src, e, get))  # no raise: the backlog goes on
        self.assertEqual(e["status"], "unverified")
        self.assertIn("403", e["verify"]["error"])

    def test_capture_http_error_is_transient(self):
        get = fake_get({W.id_url(CAP): resp(b"", status=503)})
        with self.assertRaises(W.VerifyRetry):
            W.verify(self.src, CAP, get)


class RunLoop(unittest.TestCase):
    """run() end to end with archive.org and git stubbed out."""

    def setUp(self):
        self.saved = {k: getattr(W, k) for k in ("reset_to_origin", "commit_and_push", "spn2_submit", "spn2_status",
                                                  "capture_ok", "fetch", "AUTH", "GAP_S")}
        self.sleep = W.time.sleep
        W.time.sleep = lambda s: None
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        (self.repo / "ops/wayback").mkdir(parents=True)
        self.src = "https://res.starwarsccg.org/legacyblocks/VirtualBlock7_1.pdf"
        self.old = "https://res.starwarsccg.org/legacyblocks/VirtualBlock4.pdf"
        (self.repo / W.QUEUE).write_text(self.src + "\n" + self.old + "\n")
        old_cap = "https://web.archive.org/web/20261019000000/" + self.old
        (self.repo / W.DONE).write_text(json.dumps({self.old: {"capture": old_cap, "status": "ok", "tries": 1,
                                                                "last": "2026-10-19T00:00:00Z"}}))
        self.pushed = []
        W.reset_to_origin = lambda repo: None
        W.commit_and_push = lambda repo, paths, msg, redo: self.pushed.append(msg) or True
        W.AUTH = "LOW test:test"
        W.GAP_S = 0
        W.spn2_submit = lambda url: {"job_id": "spn2-test"}
        W.spn2_status = lambda job: {"status": "success", "timestamp": "20261020193000", "original_url": self.src}
        W.capture_ok = lambda cap: True
        new_cap = "https://web.archive.org/web/20261020193000/" + self.src
        W.fetch = fake_get({W.id_url(new_cap): resp(PDF), self.src: resp(PDF),
                            W.id_url(old_cap): resp(b"old pdf"), self.old: resp(b"old pdf")})

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(W, k, v)
        W.time.sleep = self.sleep
        self.tmp.cleanup()

    def test_new_url_and_backlog_end_verified(self):
        W.run(self.repo, minutes=5)
        done = json.loads((self.repo / W.DONE).read_text())
        self.assertEqual(done[self.src]["status"], "verified")
        self.assertEqual(done[self.src]["capture"], "https://web.archive.org/web/20261020193000/" + self.src)
        self.assertEqual(done[self.src]["verify"]["method"], "sha256")
        self.assertEqual(done[self.old]["status"], "verified")
        self.assertTrue(self.pushed and self.pushed[0].startswith("wayback: 2 verified"))

    def test_verified_urls_are_not_resubmitted(self):
        W.run(self.repo, minutes=5)
        W.spn2_submit = lambda url: self.fail("resubmitted " + url)
        self.pushed.clear()
        W.run(self.repo, minutes=5)
        self.assertEqual(self.pushed, [])


class Fetch(unittest.TestCase):
    """fetch() decodes the Content-Encoding Wayback replays (gzip) before hashing."""

    def serve(self, body, headers):
        import http.server
        import threading

        class H(http.server.BaseHTTPRequestHandler):
            def do_GET(self):
                self.send_response(200)
                for k, v in headers.items():
                    self.send_header(k, v)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def log_message(self, *a):
                pass

        srv = http.server.HTTPServer(("127.0.0.1", 0), H)
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        self.addCleanup(srv.shutdown)
        return f"http://127.0.0.1:{srv.server_address[1]}/x.pdf"

    def test_gzip_capture_hashes_like_source(self):
        import gzip
        url = self.serve(gzip.compress(PDF), {"Content-Type": "application/pdf", "Content-Encoding": "gzip"})
        r = W.fetch(url)
        self.assertEqual(r["sha256"], hashlib.sha256(PDF).hexdigest())
        self.assertEqual(r["size"], len(PDF))

    def test_plain_body(self):
        url = self.serve(PAGE, {"Content-Type": "text/html"})
        r = W.fetch(url)
        self.assertEqual(r["body"], PAGE)
        self.assertTrue(W.is_html(r))


class CaptureSideErrors(unittest.TestCase):
    def test_capture_side_error_does_not_use_up_tries(self):
        e = {"capture": CAP, "status": "ok", "last": "2026-10-20T00:00:00Z"}
        get = fake_get({W.id_url(CAP): W.VerifyRetry("URLError: Connection refused")})
        with self.assertRaises(W.VerifyRetry):
            W.verify_entry("https://res.starwarsccg.org/legacyblocks/VirtualBlock7_1.pdf", e, get)
        self.assertEqual(e["status"], "ok")
        self.assertNotIn("verify_tries", e)


class SnapshotDelete(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name) / "snapshots"
        self.root.mkdir()
        self.log = self.root / "DELETED-after-wayback.log"
        (self.root / "pc").mkdir()
        self.fp = self.root / "pc" / "wrap.html"
        self.fp.write_bytes(b"<html>ok</html>")
        self.url = "https://swccg.com/snapshots/pc/wrap.html"
        self.e = {
            "capture": "https://web.archive.org/web/20261022114128/" + self.url,
            "status": "verified",
            "verify": {"method": "sha256"},
        }

    def tearDown(self):
        self.tmp.cleanup()

    def test_relpath_accepts_swccg_snapshot(self):
        self.assertEqual(W.snapshot_relpath(self.url), "pc/wrap.html")
        self.assertEqual(W.snapshot_relpath("https://www.swccg.com/snapshots/forum/t1.html"), "forum/t1.html")

    def test_relpath_rejects_other_hosts_and_traversal(self):
        self.assertIsNone(W.snapshot_relpath("https://www.decktech.net/starwarsccg/deck/14504"))
        self.assertIsNone(W.snapshot_relpath("https://swccg.com/preserved/x.html"))
        self.assertIsNone(W.snapshot_relpath("https://swccg.com/snapshots/../etc/passwd"))
        self.assertIsNone(W.snapshot_relpath("https://swccg.com/snapshots/"))

    def test_verified_snapshot_is_deleted_and_logged(self):
        self.assertTrue(W.delete_verified_snapshot(self.url, self.e, self.root, self.log))
        self.assertFalse(self.fp.exists())
        log = self.log.read_text(encoding="utf-8")
        self.assertIn("\tdelete\tpc/wrap.html\t20261022114128\tverified (sha256) by wayback_worker", log)

    def test_unverified_or_ok_is_kept(self):
        self.e["status"] = "ok"
        self.assertFalse(W.delete_verified_snapshot(self.url, self.e, self.root, self.log))
        self.assertTrue(self.fp.exists())
        self.e["status"] = "unverified"
        self.assertFalse(W.delete_verified_snapshot(self.url, self.e, self.root, self.log))
        self.assertTrue(self.fp.exists())

    def test_missing_file_is_not_an_error(self):
        self.fp.unlink()
        self.assertFalse(W.delete_verified_snapshot(self.url, self.e, self.root, self.log))

    def test_run_prunes_already_verified_without_a_done_json_push(self):
        saved = {k: getattr(W, k) for k in ("reset_to_origin", "commit_and_push", "AUTH", "GAP_S")}
        sleep = W.time.sleep
        W.time.sleep = lambda s: None
        repo = Path(self.tmp.name) / "repo"
        (repo / "ops/wayback").mkdir(parents=True)
        (repo / W.QUEUE).write_text(self.url + "\n")
        (repo / W.DONE).write_text(json.dumps({self.url: self.e}))
        pushed = []
        W.reset_to_origin = lambda repo: None
        W.commit_and_push = lambda repo, paths, msg, redo: pushed.append(msg) or True
        W.AUTH = "LOW test:test"
        W.GAP_S = 0
        os.environ["SWCCG_SNAPSHOT_ROOT"] = str(self.root)
        os.environ["SWCCG_SNAPSHOT_LOG"] = str(self.log)
        try:
            W.run(repo, minutes=1)
        finally:
            for k, v in saved.items():
                setattr(W, k, v)
            W.time.sleep = sleep
            os.environ.pop("SWCCG_SNAPSHOT_ROOT", None)
            os.environ.pop("SWCCG_SNAPSHOT_LOG", None)
        self.assertFalse(self.fp.exists())
        self.assertEqual(pushed, [])
        self.assertIn("pc/wrap.html", self.log.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
