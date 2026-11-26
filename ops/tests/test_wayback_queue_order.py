import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_worker as W


class QueueOrderTests(unittest.TestCase):
    def test_new_own_first_then_round_robin_then_retries(self):
        q = ["https://a.com/1", "https://a.com/2", "https://a.com/3", "https://b.com/1",
             "https://swccg.com/snapshots/forum/p1.html", "https://c.com/old"]
        done = {"https://c.com/old": {"status": "retry"}}
        self.assertEqual(["https://swccg.com/snapshots/forum/p1.html", "https://a.com/1", "https://b.com/1",
                          "https://a.com/2", "https://a.com/3", "https://c.com/old"], W.order_queue(q, done))

    def test_alias_skipped_when_target_known(self):
        gh = "https://stevetotheizz0.github.io/decktech_archives/14510/"
        sk = "https://www.stephenskilton.com/decktech_archives/14510/"
        other = "https://stevetotheizz0.github.io/decktech_archives/99999/"
        self.assertEqual([other], W.order_queue([gh, other], {sk: {"status": "verified"}}))
        self.assertEqual([sk], W.order_queue([gh, sk], {}))

    def test_nothing_lost(self):
        q = [f"https://h{i % 4}.com/{i}" for i in range(50)]
        self.assertEqual(sorted(q), sorted(W.order_queue(q, {})))


class IACopyDemotionTests(unittest.TestCase):  # #1375 D3
    OWN_IA = "https://swccg.com/wiki/images/0/00/Has_copy.png"
    OWN = "https://swccg.com/wiki/images/a/ab/No_copy.png"
    SNAP_IA = "https://swccg.com/snapshots/forum/p1.html"
    OUT = ["https://a.com/1", "https://b.com/1"]

    def test_own_with_verified_copy_goes_after_outside_and_own_without(self):
        q = [self.OWN_IA, self.SNAP_IA, self.OUT[0], self.OWN, self.OUT[1], "https://c.com/old"]
        done = {"https://c.com/old": {"status": "retry"}}
        covered = {"swccg-wiki-images-0/00/Has_copy.png", "swccg-com-snapshots/forum/p1.html"}
        self.assertEqual([self.OWN, self.OUT[0], self.OUT[1], self.OWN_IA, self.SNAP_IA, "https://c.com/old"],
                         W.order_queue(q, done, covered))

    def test_retries_stay_after_never_saved(self):
        q = [self.OWN_IA, "https://c.com/old", self.OWN]
        done = {self.OWN_IA: {"status": "retry"}, "https://c.com/old": {"status": "retry"}}
        self.assertEqual([self.OWN, "https://c.com/old", self.OWN_IA],
                         W.order_queue(q, done, {"swccg-wiki-images-0/00/Has_copy.png"}))

    def test_encoded_url_matches_ledger_name(self):
        url = "https://swccg.com/wiki/images/8/81/Beer_Wars_rules_%28Team_Wales%2C_2019%29.pdf"
        self.assertEqual([self.OUT[0], url], W.order_queue(
            [url, self.OUT[0]], {}, {"swccg-wiki-images-8/81/Beer_Wars_rules_(Team_Wales,_2019).pdf"}))

    def test_missing_or_bad_ledger_is_todays_order(self):
        q = [self.OWN_IA, self.OUT[0], self.OWN, self.SNAP_IA, self.OUT[1]]
        before = W.order_queue(q, {})
        self.assertEqual(before, W.order_queue(q, {}, None))
        self.assertEqual(before, W.order_queue(q, {}, set()))
        import tempfile
        from unittest.mock import patch
        import ia_item_backup
        with tempfile.TemporaryDirectory() as d:
            with patch.object(ia_item_backup, "STATE", Path(d)):
                self.assertIsNone(W.ia_covered_keys())
                (Path(d) / "ledger.json").write_text("[broken")
                self.assertIsNone(W.ia_covered_keys())
                (Path(d) / "ledger.json").write_text(
                    '{"swccg-wiki-images-0/00/Has_copy.png": {"item": "swccg-wiki-images-0", "name": "00/Has_copy.png",'
                    ' "sha1": "ab", "verified": "2026-11-25T00:48:24Z"}, "x/y": {"item": "x", "name": "y", "sha1": "c"}}')
                self.assertEqual(W.ia_covered_keys(), {"swccg-wiki-images-0/00/Has_copy.png"})


class RetryOldFailuresTests(unittest.TestCase):
    def test_old_401_and_host_limit_failures_get_a_new_round(self):
        from datetime import datetime, timezone
        t = datetime(2026, 11, 25, tzinfo=timezone.utc)
        for err in ("HTTP Error 401: UNAUTHORIZED", "no job_id: This host has been already captured 1000 times today",
                    "no job_id: The same snapshot had been made 40 minutes ago"):
            self.assertTrue(W.stale({"status": "failed", "error": err, "last": "2026-11-14T00:00:00Z"}, t), err)
        self.assertFalse(W.stale({"status": "failed", "error": "error:not-found", "last": "2026-11-14T00:00:00Z"}, t))


if __name__ == "__main__":
    unittest.main()
