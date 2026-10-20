"""Tests for the capture verification in ops/wayback_worker.py. Run: python3 -m unittest discover -s ops/tests"""
import hashlib
import json
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


if __name__ == "__main__":
    unittest.main()
