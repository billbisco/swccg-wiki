import sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_worker as W


class LinkBudgetTests(unittest.TestCase):
    def test_full_budget_when_run_was_short(self):
        self.assertEqual((90.0, 90.0), W.link_budget(600, wall=840, wayback_s=90, ia_s=90))

    def test_item_phase_shrinks_first(self):
        # 16:30:20 start, worker done 16:43:06 (766 s): 54 s left before the 14-min wall.
        self.assertEqual((54.0, 0.0), W.link_budget(766, wall=840, wayback_s=90, ia_s=90))

    def test_skip_when_nothing_left(self):
        self.assertIsNone(W.link_budget(810, wall=840, wayback_s=90, ia_s=90))

    def test_never_past_unit_timeout(self):
        for elapsed in range(0, 900, 7):
            b = W.link_budget(elapsed, wall=840, wayback_s=90, ia_s=90)
            if b:
                self.assertLessEqual(elapsed + b[0] + b[1], 840 - 20)


class SaveMinutesTests(unittest.TestCase):
    def test_reserve_shortens_a_12_minute_run(self):
        # 14-min wall, 3-min reserve, 1 min margin for prepare/finish overrun: 10 minutes of saving.
        self.assertAlmostEqual(10.0, W.save_minutes(12, 0, wall=840, reserve=180))

    def test_short_requests_unchanged(self):
        self.assertEqual(5, W.save_minutes(5, 0, wall=840, reserve=180))

    def test_never_below_one_minute(self):
        self.assertEqual(1.0, W.save_minutes(12, 800, wall=840, reserve=180))


if __name__ == "__main__":
    unittest.main()
