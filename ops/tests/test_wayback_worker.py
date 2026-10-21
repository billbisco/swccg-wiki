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


class Timestamps(unittest.TestCase):
    """parse() reads every timestamp shape found in done.json (all "...Z" today) and the ones a
    reconciliation may write; the result is always an aware UTC datetime."""

    def test_formats(self):
        want = W.datetime(2026, 10, 20, 22, 2, 22, tzinfo=W.timezone.utc)
        for s in ("2026-10-20T22:02:22Z", "2026-10-20T22:02:22z", "2026-10-20T22:02:22+00:00",
                  "2026-10-20T18:02:22-04:00", "2026-10-21T00:02:22+02:00", "2026-10-20T22:02:22.123456Z",
                  "2026-10-20 22:02:22", "2026-10-20T22:02:22", "20261020220222", want.timestamp()):
            self.assertEqual(W.parse(s), want, s)

    def test_every_stamp_in_the_repo_done_json(self):
        done = json.loads((Path(__file__).resolve().parents[1] / "wayback/done.json").read_text())
        for url, e in done.items():
            for s in (e.get("last"), (e.get("verify") or {}).get("at"), (e.get("pending_timeout") or {}).get("at")):
                if s is not None:
                    self.assertGreater(W.parse(s), W.EPOCH, (url, s))

    def test_missing_or_garbage_is_very_old(self):
        for s in (None, "", "yesterday", "2026-13-45T99:00:00Z"):
            self.assertEqual(W.parse(s), W.EPOCH)


class Cdx(unittest.TestCase):
    def test_parse_cdx_newest_first_skips_header(self):
        body = json.dumps([["timestamp", "original", "statuscode"], ["20261019000000", "https://x.org/a", "200"],
                           ["20261020000000", "https://x.org/a", "200"], ["bad", "https://x.org/a", "200"]])
        self.assertEqual(W.parse_cdx(body), ["https://web.archive.org/web/20261020000000/https://x.org/a",
                                             "https://web.archive.org/web/20261019000000/https://x.org/a"])
        self.assertEqual(W.parse_cdx(""), [])
        self.assertEqual(W.parse_cdx("[]"), [])

    def test_cdx_query_is_exact_url(self):
        seen = []

        class R:
            def __init__(self, body): self.body = body
            def read(self): return self.body
            def __enter__(self): return self
            def __exit__(self, *a): return False

        orig = W.urllib.request.urlopen
        W.urllib.request.urlopen = lambda req, timeout=0: seen.append(req.full_url) or R(b'[["timestamp","original","statuscode"]]')
        try:
            self.assertEqual(W.cdx_captures("https://swccg.com/snapshots/pc/home.html"), [])
        finally:
            W.urllib.request.urlopen = orig
        q = W.urllib.parse.parse_qs(W.urllib.parse.urlsplit(seen[0]).query)
        self.assertTrue(seen[0].startswith("https://web.archive.org/cdx/search/cdx?"))
        self.assertEqual(q["url"], ["https://swccg.com/snapshots/pc/home.html"])
        self.assertEqual(q["matchType"], ["exact"])
        self.assertEqual(q["filter"], ["statuscode:200"])

    def test_cdx_connection_refused_is_capture_side(self):
        orig = W.urllib.request.urlopen
        def refuse(req, timeout=0):
            raise W.urllib.error.URLError(ConnectionRefusedError(111, "Connection refused"))
        W.urllib.request.urlopen = refuse
        try:
            with self.assertRaises(W.VerifyRetry) as cm:
                W.cdx_captures("https://x.org/a")
        finally:
            W.urllib.request.urlopen = orig
        self.assertEqual(cm.exception.side, "capture")


class PendingTimeout(unittest.TestCase):
    """Chief, 2026-10-20: pending entries older than PENDING_TIMEOUT get an exact-URL CDX lookup and a
    capture check; verified, or back to retry, or failed after PENDING_MAX_CYCLES. CDX, SPN2 and HTTP
    are all stubbed: no network."""
    NOW = W.datetime(2026, 10, 21, 2, 0, 0, tzinfo=W.timezone.utc)
    SRC = "https://res.starwarsccg.org/legacyblocks/VirtualBlock7_1.pdf"
    SNAP = "https://swccg.com/snapshots/pc/home.html"
    SCOMP = "https://swccg.com/snapshots/scomp/card-287.html"

    def setUp(self):
        names = ("reset_to_origin", "commit_and_push", "spn2_submit", "spn2_status", "capture_ok", "fetch", "AUTH",
                 "GAP_S", "now", "cdx_captures", "PENDING_TIMEOUT", "PENDING_MAX_CYCLES")
        self.saved = {k: getattr(W, k) for k in names}
        self.sleep, self.mono = W.time.sleep, W.time.monotonic
        self.clock = [0.0]                       # fake clock: sleeps advance it, so poll loops end
        W.time.monotonic = lambda: self.clock[0]
        W.time.sleep = lambda s: self.clock.__setitem__(0, self.clock[0] + max(s, 0.01))
        self.tmp = tempfile.TemporaryDirectory()
        self.repo = Path(self.tmp.name)
        (self.repo / "ops/wayback").mkdir(parents=True)
        (self.repo / W.QUEUE).write_text("")
        self.pushed, self.cdx_calls, self.submits = [], [], []
        W.reset_to_origin = lambda repo: None
        W.commit_and_push = lambda repo, paths, msg, redo: self.pushed.append(msg) or True
        W.AUTH = "LOW test:test"
        W.GAP_S = 0
        W.now = lambda: self.NOW
        W.PENDING_TIMEOUT = W.timedelta(hours=6)
        W.PENDING_MAX_CYCLES = 3
        W.spn2_status = lambda job: {"status": "pending"}           # SPN2 never finishes: the stuck case
        W.spn2_submit = lambda url: self.submits.append(url) or {"job_id": "spn2-new"}
        W.capture_ok = lambda cap: True
        self.cdx = {}
        W.cdx_captures = lambda url: self.cdx_calls.append(url) or list(self.cdx.get(url, []))
        self.http = {}
        W.fetch = fake_get(self.http)

    def tearDown(self):
        for k, v in self.saved.items():
            setattr(W, k, v)
        W.time.sleep, W.time.monotonic = self.sleep, self.mono
        self.tmp.cleanup()

    def stamp(self, hours_ago):
        return W.iso(self.NOW - W.timedelta(hours=hours_ago))

    def pending(self, hours_ago, **kw):
        return {"capture": "", "job_id": "spn2-stuck", "last": self.stamp(hours_ago), "status": "pending", "tries": 1, **kw}

    def write(self, done):
        (self.repo / W.DONE).write_text(json.dumps(done))

    def read(self):
        return json.loads((self.repo / W.DONE).read_text())

    def test_pending_under_timeout_is_untouched(self):
        e = self.pending(5.9)
        self.write({self.SRC: e})
        W.run(self.repo, minutes=5)
        self.assertEqual(self.cdx_calls, [])
        self.assertEqual(self.submits, [])
        self.assertEqual(self.read()[self.SRC], e)
        self.assertEqual(self.pushed, [])

    def test_over_timeout_verified_from_cdx(self):
        cap = "https://web.archive.org/web/20261020193000/" + self.SRC
        self.cdx[self.SRC] = [cap]
        self.http.update({W.id_url(cap): resp(PDF), self.SRC: resp(PDF)})
        self.write({self.SRC: self.pending(6.5, capture="https://web.archive.org/web/20261019000000/" + self.SRC)})
        W.run(self.repo, minutes=5)
        e = self.read()[self.SRC]
        self.assertEqual(e["status"], "verified")
        self.assertEqual(e["capture"], cap)
        self.assertEqual(e["verify"]["method"], "sha256")
        self.assertEqual(e["pending_timeout"]["result"], "verified")
        self.assertEqual(e["pending_timeout"]["cdx_timestamp"], "20261020193000")
        self.assertEqual(e["pending_timeouts"], 1)
        self.assertNotIn("job_id", e)
        self.assertEqual(e["last"], W.iso(self.NOW))
        self.assertEqual(self.submits, [])
        self.assertTrue(self.pushed[0].startswith("wayback: 1 verified"))

    def test_deleted_snapshot_verified_by_header(self):
        cap = "https://web.archive.org/web/20261020234753/" + self.SNAP
        page = b"<!-- snapshot-of: https://www.starwarsccg.org/ captured: 2026-10-20T22:58:06Z -->\n" + PAGE
        self.cdx[self.SNAP] = [cap]
        self.http.update({W.id_url(cap): resp(page, "text/html"), self.SNAP: resp(b"", "text/html", status=404)})
        e = self.pending(7)
        self.assertEqual(W.resolve_timed_out(self.SNAP, e), "verified")
        self.assertEqual(e["verify"]["method"], "snapshot-header")
        self.assertEqual(e["verify"]["snapshot_of"], "https://www.starwarsccg.org/")

    def test_over_timeout_not_verified_is_requeued_and_resaved(self):
        cap = "https://web.archive.org/web/20261020193000/" + self.SRC
        self.cdx[self.SRC] = [cap]
        self.http.update({W.id_url(cap): resp(PDF + b"x"), self.SRC: resp(PDF)})   # different bytes
        self.write({self.SRC: self.pending(8)})                                      # not in queue.txt
        W.run(self.repo, minutes=5)
        e = self.read()[self.SRC]
        self.assertEqual(e["status"], "retry")
        self.assertEqual(e["pending_timeouts"], 1)
        self.assertEqual(e["pending_timeout"]["result"], "resave")
        self.assertIn("differs", e["pending_timeout"]["reason"])
        self.assertEqual(e["stale_job_id"], "spn2-stuck")
        self.assertNotIn("job_id", e)
        self.assertEqual(self.submits, [])            # RETRY_AFTER has not passed yet
        # next run, RETRY_AFTER later: re-saved, and the cycle count survives the re-save
        self.NOW = self.NOW + W.RETRY_AFTER
        W.run(self.repo, minutes=5)
        e = self.read()[self.SRC]
        self.assertEqual(self.submits, [self.SRC])
        self.assertEqual((e["status"], e["job_id"], e["tries"], e["pending_timeouts"]), ("pending", "spn2-new", 2, 1))

    def test_no_capture_in_cdx_is_requeued(self):
        e = self.pending(7)
        self.assertEqual(W.resolve_timed_out(self.SRC, e), "retry")
        self.assertEqual(e["pending_timeout"]["reason"], "no capture in CDX")
        self.assertEqual(e["pending_timeout"]["cdx_captures"], 0)

    def test_retry_cap_reached_is_failed(self):
        e = self.pending(7)
        for cycle in range(1, W.PENDING_MAX_CYCLES + 1):
            st = W.resolve_timed_out(self.SRC, e)
            self.assertEqual(st, "retry" if cycle < W.PENDING_MAX_CYCLES else "failed")
            self.assertEqual(e["pending_timeouts"], cycle)
            e.update(status="pending", job_id="spn2-again")   # the re-save that would follow
        self.assertEqual(e["pending_timeout"]["result"], "failed")
        self.assertIn(f"{W.PENDING_MAX_CYCLES}/{W.PENDING_MAX_CYCLES}", e["error"])
        # failed is terminal: run() neither re-checks nor re-saves it
        e.update(status="failed", last=self.stamp(48))
        self.write({self.SRC: e})
        (self.repo / W.QUEUE).write_text(self.SRC + "\n")
        self.cdx_calls.clear()
        W.run(self.repo, minutes=5)
        self.assertEqual((self.cdx_calls, self.submits, self.pushed), ([], [], []))

    def test_cap_is_configurable(self):
        W.PENDING_MAX_CYCLES = 1
        self.assertEqual(W.resolve_timed_out(self.SRC, self.pending(7)), "failed")

    def test_scomp_ordered_last(self):
        other = "https://swccg.com/snapshots/forum/t85193.html"
        scomp_host = "https://scomp.starwarsccg.org/card/287"
        self.write({self.SCOMP: self.pending(9), scomp_host: self.pending(9), other: self.pending(7)})
        (self.repo / W.QUEUE).write_text("https://swccg.com/snapshots/scomp/card-5618.html\nhttps://x.org/new\n")
        W.run(self.repo, minutes=5)
        self.assertEqual(self.cdx_calls, [other, self.SCOMP, scomp_host])   # timeout pass: Scomp last
        self.assertEqual(self.submits, ["https://x.org/new", "https://swccg.com/snapshots/scomp/card-5618.html"])
        self.NOW = self.NOW + W.RETRY_AFTER
        self.submits.clear()
        W.run(self.repo, minutes=5)
        self.assertEqual(self.submits[0], other)                            # re-saves: Scomp last
        self.assertEqual(set(self.submits[1:]), {self.SCOMP, scomp_host})

    def test_archive_org_down_leaves_entry(self):
        def down(url):
            raise W.VerifyRetry("CDX URLError: Connection refused", side="capture")
        W.cdx_captures = down
        e = self.pending(7)
        self.write({self.SRC: e})
        W.run(self.repo, minutes=5)
        self.assertEqual(self.read()[self.SRC], e)

    def test_tolerates_current_and_reconciled_done_json(self):
        verified = {"capture": "https://web.archive.org/web/20261020234753/" + self.SNAP, "last": "2026-10-21T01:49:20Z",
                    "status": "verified", "tries": 3, "verify": {"at": "2026-10-21T00:08:56Z", "method": "sha256"}}
        done = {
            self.SNAP: verified,                                                    # reconciled by hand (fb7d5508)
            "https://a.org/1": {"capture": "", "last": "2026-10-20T15:00:00-04:00", "status": "pending", "tries": "2"},  # 7 h, offset
            "https://a.org/1b": {"capture": "", "last": "2026-10-20T19:00:00-04:00", "status": "pending", "tries": 1},
            "https://a.org/2": {"capture": "", "status": "pending", "tries": 1},     # no "last"
            "https://a.org/3": {"capture": "", "last": "2026-10-20T00:00:00Z", "status": "manual-review", "tries": 1,
                                "reconciled_by": "Alpha1"},                        # status unknown to the worker
            "https://a.org/4": {"capture": "", "last": "2026-10-20T00:00:00Z", "status": "retry", "tries": "1"},
        }
        self.write(done)
        (self.repo / W.QUEUE).write_text("https://a.org/3\nhttps://a.org/4\n" + self.SNAP + "\n")
        W.run(self.repo, minutes=5)
        out = self.read()
        self.assertEqual(out[self.SNAP], verified)
        self.assertEqual(out["https://a.org/3"], done["https://a.org/3"])
        self.assertEqual(out["https://a.org/1"]["status"], "retry")
        self.assertEqual(out["https://a.org/1b"], done["https://a.org/1b"])   # 3 h by its offset: untouched
        self.assertEqual(out["https://a.org/2"]["status"], "retry")
        self.assertEqual(out["https://a.org/4"]["tries"], 2)
        self.assertEqual(set(self.submits), {"https://a.org/4"})
        for e in out.values():                       # nothing existing removed; new keys only added
            self.assertIn("status", e)


if __name__ == "__main__":
    unittest.main()
