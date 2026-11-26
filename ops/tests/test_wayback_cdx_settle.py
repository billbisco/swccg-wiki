import json
import sys
import time
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_cdx_settle as S

P = "https://swccg.com/snapshots/pc/"
A, B, C, D = P + "a.html", P + "b.html", P + "c.html", P + "d.html"


def fake_get(rows):
    def get(url):
        return json.dumps([["timestamp", "original", "statuscode", "digest"]] + rows).encode()
    return get


class SettleTests(unittest.TestCase):
    def test_settles_matching_digest_and_skips_others(self):
        done = {
            A: {"status": "unverified", "capture": "https://web.archive.org/web/20261020000000/" + A},
            B: {"status": "pending", "job_id": "spn2-x"},
            C: {"status": "unverified", "capture": "https://web.archive.org/web/20261020000000/" + C},
            D: {"status": "verified", "capture": "https://web.archive.org/web/20261020000000/" + D},
        }
        rows = [["20261020000000", "http://www.swccg.com:80/snapshots/pc/a.html", "200", "AAA"],
                ["20261021000000", B, "200", "BBB"], ["20261022000000", B, "200", "BBB"],
                ["20261021000000", C, "200", "CCC"]]  # C's own capture is not the matching one
        sha = {A: "AAA", B: "BBB", C: "CCC", D: "DDD"}.get
        r, st = S.settle(done, [P], get=fake_get(rows), sha=sha, now="T")
        self.assertEqual({A, B}, set(r))
        self.assertEqual(done[A]["capture"], r[A]["capture"])
        self.assertEqual("https://web.archive.org/web/20261022000000/" + B, r[B]["capture"])
        self.assertEqual("spn2-x", r[B]["job_id"])
        self.assertEqual("cdx-sha1", r[A]["verify"]["method"])
        self.assertEqual(1, st["other_capture_matches"])
        self.assertNotIn(D, r)

    def test_digest_mismatch_and_missing_file_not_verified(self):
        done = {A: {"status": "unverified"}, B: {"status": "unverified"}}
        rows = [["20261020000000", A, "200", "OLD"]]
        r, st = S.settle(done, [P], get=fake_get(rows), sha={A: "NEW", B: None}.get, now="T")
        self.assertEqual({}, r)
        self.assertEqual({"digest_differs": 1, "no_local_file": 1}, st)

    def test_pruned_file_uses_prune_log_timestamp(self):
        done = {A: {"status": "unverified", "capture": "https://web.archive.org/web/20261020000000/" + A},
                B: {"status": "unverified"}, C: {"status": "unverified"}}
        rows = [["20261020000000", A, "200", "X"], ["20261021000000", B, "200", "Y"]]
        pruned = {A: "20261020000000", B: "20261099000000"}
        r, st = S.settle(done, [P], get=fake_get(rows), sha=lambda u: None, now="T", pruned=pruned)
        self.assertEqual({A}, set(r)); self.assertEqual("cdx-200+prune-log-sha", r[A]["verify"]["method"])
        self.assertEqual({"verified_pruned": 1, "deleted_capture_not_indexed": 1, "no_local_file": 1}, st)

    def test_source_gone_accepts_only_own_capture_listed_200(self):
        done = {A: {"status": "unverified", "capture": "https://web.archive.org/web/20261020000000/" + A},
                B: {"status": "unverified", "capture": "https://web.archive.org/web/20261020000000/" + B}}
        rows = [["20261020000000", A, "200", "X"], ["20261021000000", B, "200", "Y"]]
        r, st = S.settle(done, [P], get=fake_get(rows), sha=lambda u: None, now="T", pruned={})
        self.assertEqual({A}, set(r)); self.assertIn("source deleted", r[A]["verify"]["method"])
        self.assertEqual({"verified_source_gone": 1, "deleted_capture_not_indexed": 1}, st)

    def test_prune_log_parsing(self):
        import tempfile
        with tempfile.NamedTemporaryFile("w", delete=False, suffix=".log") as f:
            f.write("T\tdelete\tpc/a.html\t20261020000000\tverified (sha256) by x\n"
                    "T\tdelete\tpc/b.html\t20261020000000\tverified (text) by x\n"
                    "T\tdelete\tpc/c.html\t20261020000000\tcdx\n"
                    "T\tdelete\tpc/d.html\t20261020000000\tverified (done.json verified sha256) by x\n")
        self.assertEqual({A: "20261020000000", D: "20261020000000"}, S.prune_proofs(Path(f.name)))

    def test_cdx_outage_skips_prefix(self):
        def boom(url): raise RuntimeError("CDX unavailable")
        r, st = S.settle({A: {"status": "pending"}}, [P], get=boom, sha=lambda u: "X", now="T")
        self.assertEqual({}, r); self.assertEqual(1, st["prefix_unavailable"])


class SharedCooldownTests(unittest.TestCase):
    """#1375 review: the exact-URL CDX pass obeys the worker's shared cooldown."""
    FP = "https://swccg.com/snapshots/forum/"

    def setUp(self):
        import tempfile
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.dir = Path(self.tmp.name)

    def control(self, **state):
        path = self.dir / "control.json"
        path.write_text(json.dumps(dict({"schema": 1, "mode": "healthy", "failure_count": 0,
                                         "next_attempt": 0, "probe_url": None}, **state)))
        return path

    def test_defaults_are_modest(self):
        self.assertEqual(500, S.EXACT_MAX)
        self.assertEqual(4.0, S.EXACT_GAP_S)
        self.assertEqual(900, S.REFUSED_HOLD_S)

    def test_control_blocked_reads_worker_state(self):
        self.assertIsNone(S.control_blocked(self.dir / "missing.json"))
        self.assertIsNone(S.control_blocked(self.control(next_attempt=500), now=1000))
        self.assertIn("cooldown", S.control_blocked(self.control(next_attempt=2000, provider_event="network_refused"),
                                                    now=1000))
        for mode in ("open", "half_open", "auth_blocked", "probe_blocked"):
            self.assertIn(mode, S.control_blocked(self.control(mode=mode), now=1000))
        bad = self.dir / "bad.json"
        bad.write_text("{not json")
        self.assertIn("unreadable", S.control_blocked(bad))

    def test_live_main_makes_no_request_during_cooldown(self):
        from unittest.mock import patch
        repo = self.dir / "repo"
        (repo / "ops/wayback").mkdir(parents=True)
        (repo / "ops/wayback/done.json").write_text(json.dumps({self.FP + "a.html": {"status": "ok"}}))
        with patch.object(sys, "argv", ["settle", "--repo", str(repo)]), \
             patch.object(S, "CONTROL", self.control(next_attempt=time.time() + 3600)), \
             patch.object(S, "HOLD", self.dir / "hold.json"), \
             patch.object(S, "settle", side_effect=AssertionError("no settle")), \
             patch.object(S.urllib.request, "urlopen", side_effect=AssertionError("network")):
            self.assertEqual(0, S.main())

    def test_cooldown_appearing_mid_run_stops_the_exact_pass(self):
        urls = [self.FP + f"p{i}.html" for i in range(4)]
        done = {u: {"status": "ok", "last": f"2026-11-2{i}T00:00:00Z"} for i, u in enumerate(urls)}
        calls, answers = [], iter([None, None, "worker cooldown until later"])
        r, st = S.settle(done, [self.FP], get=lambda q: json.dumps([]).encode(), sha=lambda u: "X", now="T",
                         exact_get=lambda u: calls.append(u) or json.dumps([]).encode(), exact_max=10,
                         blocked=lambda: next(answers))
        self.assertEqual(1, len(calls))
        self.assertEqual(1, st["exact_lookups"])
        self.assertIn("shared cooldown", st["stopped"])

    def test_cooldown_before_prefix_makes_no_request(self):
        done = {self.FP + "a.html": {"status": "ok"}}
        r, st = S.settle(done, [self.FP], get=lambda q: self.fail("prefix request"), sha=lambda u: "X", now="T",
                         exact_get=lambda u: self.fail("exact request"), exact_max=10,
                         blocked=lambda: "worker circuit is open")
        self.assertEqual({}, r)
        self.assertEqual(1, st["prefix_unavailable"])

    def test_refusal_saves_a_refused_hold_the_worker_honours(self):
        import urllib.error
        from types import SimpleNamespace
        from unittest.mock import patch
        import wayback_worker as W

        def urlopen(req, timeout=None):
            raise urllib.error.URLError(ConnectionRefusedError(111, "Connection refused"))
        done = {self.FP + "a.html": {"status": "ok"}}
        with patch.object(S.urllib.request, "urlopen", side_effect=urlopen):
            _, st = S.settle(done, [self.FP], sha=lambda u: "X", now="T", exact_max=10, sleep=lambda s: None)
        self.assertTrue(st["refused"])
        hold = self.dir / "cdx-settle-hold.json"
        self.assertEqual(900, S.save_hold(st, hold, now=1000))
        saved = json.loads(hold.read_text())
        self.assertEqual({"until": 1900, "refused": True}, {k: saved[k] for k in ("until", "refused")})
        self.assertEqual(1900, S.hold_active(hold, now=1000))
        # The worker carries it into its shared cooldown before any request.
        saves = []
        control = SimpleNamespace(directory=self.dir, clock=lambda: 1000.0, state={"next_attempt": 0},
                                  save=lambda: saves.append(1))
        with patch("builtins.print"):
            W.cdx_hold_cooldown(control)
        self.assertEqual(1900, control.state["next_attempt"])
        self.assertEqual("cdx_network_refused", control.state["provider_event"])
        self.assertEqual([1], saves)
        # A 429-only hold (not refused) stays the CDX pass's own business.
        hold.write_text(json.dumps({"until": 9000, "refused": False}))
        control.state = {"next_attempt": 0}
        W.cdx_hold_cooldown(control)
        self.assertEqual(0, control.state["next_attempt"])


if __name__ == "__main__":
    unittest.main()


class WorkerBatchTests(unittest.TestCase):
    def test_own_file_success_skips_replay_and_waits_for_batch(self):
        from unittest.mock import patch
        import wayback_worker as W
        e = {"status": "pending", "job_id": "spn2-x", "tries": 1, "last": "2026-11-24T00:00:00Z"}
        with patch.object(W, "AUTH", "fixture"), \
             patch.object(W, "spn2_status", return_value={"status": "success", "timestamp": "20261124000000", "original_url": A}), \
             patch.object(W, "capture_ok", side_effect=AssertionError("replay request")), \
             patch.object(W, "verify_entry", side_effect=AssertionError("replay request")):
            self.assertTrue(W.confirm(A, e))
        self.assertEqual("ok", e["status"]); self.assertEqual("cdx-batch", e["verify"]["defer"])

    def test_other_sites_still_checked_one_by_one(self):
        from unittest.mock import patch
        import wayback_worker as W
        url = "https://example.com/x"
        e = {"status": "pending", "job_id": "spn2-x", "tries": 1, "last": "2026-11-24T00:00:00Z"}
        with patch.object(W, "AUTH", "fixture"), \
             patch.object(W, "spn2_status", return_value={"status": "success", "timestamp": "20261124000000"}), \
             patch.object(W, "capture_ok", return_value=True) as ok, patch.object(W, "verify_entry") as ve:
            W.confirm(url, e)
        ok.assert_called_once(); ve.assert_called_once()


class ExactTests(unittest.TestCase):
    """#1375: prefix CDX queries miss recent captures; look the rest up by exact URL."""
    F = "https://swccg.com/snapshots/forum/p1259062.html"
    FP = "https://swccg.com/snapshots/forum/"
    HEAD = ["timestamp", "original", "statuscode", "digest"]

    def exact(self, table, calls=None):
        def get(url):
            if calls is not None:
                calls.append(url)
            value = table[url]
            if isinstance(value, Exception):
                raise value
            return json.dumps(value).encode()
        return get

    def test_exact_lookup_accepts_matching_digest_after_empty_prefix(self):
        done = {self.F: {"status": "ok", "capture": "https://web.archive.org/web/20261125052008/" + self.F,
                         "job_id": "spn2-x"}}
        answer = [self.HEAD, ["20261125052008", self.F, "200", "TLPLUXQ5MHUXVDYD7JJLDOIUKMSHBWCE"]]
        r, st = S.settle(done, [self.FP], get=fake_get([]), sha=lambda u: "TLPLUXQ5MHUXVDYD7JJLDOIUKMSHBWCE",
                         now="T", exact_get=self.exact({self.F: answer}), exact_max=10)
        self.assertEqual({self.F}, set(r))
        self.assertEqual({"capture": done[self.F]["capture"], "status": "verified", "job_id": "spn2-x",
                          "verify": {"at": "T", "method": "cdx-sha1", "sha1_b32": "TLPLUXQ5MHUXVDYD7JJLDOIUKMSHBWCE",
                                     "capture_id": "https://web.archive.org/web/20261125052008id_/" + self.F,
                                     "index": "cdx"}}, r[self.F])
        self.assertEqual({"verified": 1, "exact_lookups": 1, "exact_verified": 1}, st)

    def test_exact_lookup_rejects_different_digest_and_non_200_rows(self):
        done = {self.F: {"status": "ok", "capture": "https://web.archive.org/web/20261125052008/" + self.F}}
        answer = [self.HEAD, ["20261125052008", self.F, "200", "OTHER"],
                  ["20261125052008", self.F, "404", "MINE"],
                  ["20261125052008", "https://swccg.com/snapshots/forum/p1.html", "200", "MINE"]]
        r, st = S.settle(done, [self.FP], get=fake_get([]), sha=lambda u: "MINE", now="T",
                         exact_get=self.exact({self.F: answer}), exact_max=10)
        self.assertEqual({}, r)
        self.assertEqual(1, st["digest_differs"])

    def test_exact_lookups_are_bounded_newest_first_and_skip_no_local_file(self):
        urls = [self.FP + f"p{i}.html" for i in range(4)]
        done = {u: {"status": "ok", "last": f"2026-11-2{i}T00:00:00Z"} for i, u in enumerate(urls)}
        calls = []
        table = {u: [self.HEAD] for u in urls}
        r, st = S.settle(done, [self.FP], get=fake_get([]), sha=lambda u: None if u == urls[3] else "X",
                         now="T", exact_get=self.exact(table, calls), exact_max=2)
        self.assertEqual([urls[2], urls[1]], calls)
        self.assertEqual(1, st["exact_over_budget"])
        self.assertEqual(1, st["no_local_file"])

    def test_live_exact_stops_on_429_and_keeps_earlier_receipts(self):
        import io
        import urllib.error
        from unittest.mock import patch
        a, b, c = self.FP + "a.html", self.FP + "b.html", self.FP + "c.html"
        done = {a: {"status": "ok", "last": "2026-11-26T00:00:00Z"}, b: {"status": "ok", "last": "2026-11-25T00:00:00Z"},
                c: {"status": "ok", "last": "2026-11-24T00:00:00Z"}}
        calls, sleeps = [], []

        class R(io.BytesIO):
            def __enter__(self): return self
            def __exit__(self, *exc): return False

        def urlopen(req, timeout=None):
            calls.append(req.full_url)
            if len(calls) == 1:
                return R(json.dumps([self.HEAD, ["20261126000000", a, "200", "X"]]).encode())
            raise urllib.error.HTTPError(req.full_url, 429, "Too Many", {"Retry-After": "600"}, None)
        with patch.object(S.urllib.request, "urlopen", side_effect=urlopen):
            r, st = S.settle(done, [self.FP], get=fake_get([]), sha=lambda u: "X", now="T",
                             exact_max=10, exact_gap=1.5, sleep=sleeps.append)
        self.assertEqual(2, len(calls))  # c is never asked
        self.assertIn("url=https%3A%2F%2Fswccg.com%2Fsnapshots%2Fforum%2Fa.html", calls[0])
        self.assertIn("filter=statuscode%3A200", calls[0])
        self.assertEqual({a}, set(r))
        self.assertEqual("600", st["retry_after"])
        self.assertIn("429", st["stopped"])
        self.assertEqual([1.5], sleeps)
        self.assertEqual(600.0, S.retry_after_seconds("600"))

    def test_refused_connection_stops_without_retry(self):
        import urllib.error
        from unittest.mock import patch
        calls = []

        def urlopen(req, timeout=None):
            calls.append(req.full_url)
            raise urllib.error.URLError(ConnectionRefusedError(111, "Connection refused"))
        done = {self.FP + "a.html": {"status": "ok"}, self.FP + "b.html": {"status": "ok"}}
        with patch.object(S.urllib.request, "urlopen", side_effect=urlopen), \
             patch.object(S.time, "sleep", side_effect=AssertionError("no retry wait")):
            r, st = S.settle(done, [self.FP], sha=lambda u: "X", now="T", exact_max=10, sleep=lambda s: None)
        self.assertEqual(1, len(calls))  # the prefix query; no retry and no exact pass
        self.assertIn("refused", st["stopped"])
        self.assertEqual(2, st["prefix_unavailable"])

    def test_hold_file_blocks_until_retry_after(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            hold = Path(tmp) / "hold.json"
            self.assertIsNone(S.hold_active(hold))
            hold.write_text(json.dumps({"until": 2000}))
            self.assertEqual(2000, S.hold_active(hold, now=1000))
            self.assertIsNone(S.hold_active(hold, now=3000))

    def test_cdx_dir_exact_files_named_by_sha1_of_ledger_url(self):
        import hashlib
        import tempfile
        from unittest.mock import patch
        iri = "https://swccg.com/wiki/images/a/ab/Bjørn.jpg"
        self.assertEqual("exact-4f200595accd7f6858e738bf0863c4017d8c8be1.json", S.exact_name(self.F))
        self.assertEqual("exact-" + hashlib.sha1(iri.encode("utf-8")).hexdigest() + ".json", S.exact_name(iri))
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            repo, cdx, state = tmp / "repo", tmp / "cdx", tmp / "state"
            (repo / "ops/wayback").mkdir(parents=True)
            cdx.mkdir()
            image = tmp / "image.jpg"
            image.write_bytes(b"jpeg bytes")
            digest = S.sha1_b32(image)
            missing = "https://swccg.com/wiki/images/a/cd/Gone.jpg"
            done = {iri: {"status": "ok", "capture": "https://web.archive.org/web/20261125000000/" + iri},
                    missing: {"status": "ok", "capture": "https://web.archive.org/web/20261125000000/" + missing}}
            (repo / "ops/wayback/done.json").write_text(json.dumps(done), encoding="utf-8")
            # default CDX columns (no fl=), as a plain exact query returns them
            (cdx / S.exact_name(iri)).write_text(json.dumps([
                ["urlkey", "timestamp", "original", "mimetype", "statuscode", "digest", "length"],
                ["com,swccg)/wiki/images/a/ab/bj%c3%b8rn.jpg", "20261125000000",
                 "https://swccg.com/wiki/images/a/ab/Bj%C3%B8rn.jpg", "image/jpeg", "200", digest, "10"]]))
            argv = ["settle", "--repo", str(repo), "--cdx-dir", str(cdx),
                    "--prefix", "https://swccg.com/wiki/images/a/"]
            # --cdx-dir makes no network request, so a worker cooldown does not stop it.
            blocked = tmp / "control.json"
            blocked.write_text(json.dumps({"mode": "open", "next_attempt": 9e12}))
            with patch.object(sys, "argv", argv), patch.object(S, "INBOX", state / "verify-inbox"), \
                 patch.object(S, "CONTROL", blocked), patch.object(S, "HOLD", tmp / "no-hold.json"), \
                 patch.object(S, "prune_proofs", return_value={}), \
                 patch.object(S, "local_file", side_effect=lambda u: image if u == iri else None), \
                 patch.object(S.urllib.request, "urlopen", side_effect=AssertionError("network")):
                self.assertEqual(0, S.main())
            (receipt,) = list((state / "verify-inbox").glob("cdx-settle-*.json"))
            data = json.loads(receipt.read_text())
            self.assertEqual({"schema", "lane", "updates"}, set(data))
            self.assertEqual("cdx-sha1", data["lane"])
            self.assertEqual([iri], list(data["updates"]))
            self.assertEqual(digest, data["updates"][iri]["verify"]["sha1_b32"])

    def test_exact_list_names_what_to_fetch(self):
        a = self.FP + "a.html"
        listing = []
        r, st = S.settle({a: {"status": "ok"}, self.FP + "n.html": {"status": "ok"}}, [self.FP],
                         get=fake_get([]), sha=lambda u: "X" if u == a else None, now="T",
                         exact_max=10, exact_list=listing)
        self.assertEqual([a], listing)
        self.assertEqual({}, r)
