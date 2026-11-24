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


if __name__ == "__main__":
    unittest.main()
