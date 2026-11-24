import json
import sys
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


if __name__ == "__main__":
    unittest.main()
