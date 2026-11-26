"""Self-tuning submit pace and adaptive promotion (#1375). No network."""
import contextlib
import io
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import wayback_pace as pace  # noqa: E402
import wayback_worker as W  # noqa: E402
from wayback_control import Control, Paused  # noqa: E402

CLEAN_ENV = {k: v for k, v in os.environ.items() if not k.startswith(("WAYBACK_PACE", "WAYBACK_GAP_MIN",
                                                                       "WAYBACK_PROMOTE", "WAYBACK_RUN_INTERVAL",
                                                                       "WAYBACK_FINISH", "WAYBACK_OWNER_OBSERVE"))}


class Env(unittest.TestCase):
    def setUp(self):
        env = patch.dict(os.environ, CLEAN_ENV, clear=True)
        env.start()
        self.addCleanup(env.stop)
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.dir = Path(self.temp.name)


class Aimd(Env):
    def step(self, allowance, submits=None, signals=(), refusals=0, outcome="completed"):
        return pace.decide(allowance, submits=allowance if submits is None else submits,
                           signals=list(signals), refusals=refusals, outcome=outcome)

    def test_clean_full_run_raises_by_two(self):
        new, reason, limited = self.step(12)
        self.assertEqual(14, new)
        self.assertFalse(limited)
        self.assertIn("raised", reason)

    def test_partial_run_holds(self):
        self.assertEqual(12, self.step(12, submits=7)[0])

    def test_paused_or_failed_run_without_pushback_holds(self):
        self.assertEqual(12, self.step(12, outcome="paused")[0])
        self.assertEqual(12, self.step(12, outcome="failed")[0])

    def test_every_pushback_signal_halves(self):
        for signals, refusals in (([{"kind": "provider", "status": 429, "retry_after": True}], 0),
                                  ([{"kind": "provider", "status": 503, "retry_after": False}], 0),
                                  ([{"kind": "auth", "status": 401}], 0),
                                  ([{"kind": "capacity", "reason": "network_refused"}], 0),
                                  ([], 1)):
            with self.subTest(signals=signals, refusals=refusals):
                new, reason, _ = self.step(12, signals=signals, refusals=refusals, outcome="paused")
                self.assertEqual(6, new)
                self.assertIn("halved", reason)

    def test_rate_limited_flag_is_429_or_retry_after(self):
        self.assertTrue(self.step(12, signals=[{"kind": "provider", "status": 429}])[2])
        self.assertTrue(self.step(12, signals=[{"kind": "provider", "status": 503, "retry_after": True}])[2])
        self.assertFalse(self.step(12, signals=[{"kind": "provider", "status": 503}])[2])

    def test_account_capacity_is_neutral_even_after_full_run(self):
        for reason in ("account_sessions", "capacity_unknown", "account_daily_limit"):
            with self.subTest(reason=reason):
                new, why, _ = self.step(12, signals=[{"kind": "capacity", "reason": reason}], outcome="paused")
                self.assertEqual(12, new)
                self.assertIn("holding", why)

    def test_bounds(self):
        self.assertEqual(3, self.step(3, refusals=1)[0])
        self.assertEqual(3, self.step(5, refusals=1)[0])
        self.assertEqual(40, self.step(39)[0])
        self.assertEqual(40, self.step(40)[0])
        # A cut never raises an allowance that started below the floor.
        self.assertEqual(1, self.step(1, refusals=1)[0])
        self.assertEqual(3, self.step(1)[0])
        with patch.dict(os.environ, {"WAYBACK_PACE_MIN": "5", "WAYBACK_PACE_MAX": "20"}):
            self.assertEqual(5, self.step(8, refusals=1)[0])
            self.assertEqual(20, self.step(19)[0])

    def test_gap_spreads_allowance_and_keeps_floors(self):
        self.assertEqual(52.5, pace.plan_gap(12, 630, 15))
        self.assertEqual(15, pace.plan_gap(40, 300, 15))
        self.assertEqual(60, pace.plan_gap(12, 630, 15, floor_s=60))
        self.assertEqual(15, pace.plan_gap(5, -10, 15))


class StateFiles(Env):
    def test_initial_values_come_from_existing_env_knobs(self):
        self.assertEqual(6, pace.load(self.dir, initial=6, initial_gap_s=60, usable_s=630)["allowance"])
        fresh = pace.load(self.dir, initial=0, initial_gap_s=0, usable_s=630)
        self.assertEqual(pace.DEFAULT_INITIAL, fresh["allowance"])
        self.assertTrue(fresh["fresh"])
        self.assertEqual(40, pace.load(self.dir, initial=100, initial_gap_s=0, usable_s=630)["allowance"])
        self.assertEqual(60, pace.load(self.dir, initial=12, initial_gap_s=60, usable_s=630)["gap_s"])

    def test_saved_state_wins_over_env_and_is_clamped_to_bounds(self):
        state = pace.load(self.dir, initial=12, initial_gap_s=60, usable_s=630)
        pace.record(self.dir, state, new_allowance=30, reason="r", last_run={}, gap_used_s=60,
                    usable_s=630, promotion=None)
        self.assertEqual(30, pace.load(self.dir, initial=6, initial_gap_s=60, usable_s=630)["allowance"])
        with patch.dict(os.environ, {"WAYBACK_PACE_MAX": "20"}):
            self.assertEqual(20, pace.load(self.dir, initial=6, initial_gap_s=60, usable_s=630)["allowance"])

    def test_corrupt_state_falls_back_to_initial(self):
        (self.dir / pace.STATE_FILE).write_text("{not json")
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(7, pace.load(self.dir, initial=7, initial_gap_s=0, usable_s=630)["allowance"])

    def test_state_and_log_shape(self):
        state = pace.load(self.dir, initial=12, initial_gap_s=60, usable_s=630)
        last = {"submits": 12, "refusals": 0, "rate_limited": False, "used_full_allowance": True,
                "ended": "2026-11-26T12:00:00Z"}
        promo = {"target_buffer": 333, "buffer_before": 40, "promoted": 200, "cap": 200, "seconds": 12.5}
        saved = pace.record(self.dir, state, new_allowance=14, reason="clean full run", last_run=last,
                            gap_used_s=60, usable_s=630, promotion=promo, at="2026-11-26T12:00:00Z")
        disk = json.loads((self.dir / pace.STATE_FILE).read_text())
        self.assertEqual(saved, disk)
        self.assertEqual({"schema_version", "updated_at", "allowance", "gap_s", "bounds", "last_run", "reason",
                          "promotion", "run_starts"}, set(disk))
        self.assertEqual([], disk["run_starts"])
        self.assertEqual(1, disk["schema_version"])
        self.assertEqual(14, disk["allowance"])
        self.assertEqual(45.0, disk["gap_s"])
        self.assertEqual({"min": 3, "max": 40, "gap_min_s": 15.0}, disk["bounds"])
        self.assertEqual(last, disk["last_run"])
        self.assertEqual(promo, disk["promotion"])
        lines = (self.dir / pace.LOG_FILE).read_text().splitlines()
        self.assertEqual([{"at": "2026-11-26T12:00:00Z", "from": 12, "to": 14, "gap_from": 60.0,
                           "gap_to": 45.0, "reason": "clean full run"}], [json.loads(x) for x in lines])
        # Unchanged allowance and gap: state refreshed, no new log line.
        again = pace.load(self.dir, initial=12, initial_gap_s=60, usable_s=630)
        pace.record(self.dir, again, new_allowance=14, reason="holding", last_run=last, gap_used_s=45.0,
                    usable_s=630, promotion=promo)
        self.assertEqual(1, len((self.dir / pace.LOG_FILE).read_text().splitlines()))
        self.assertEqual("holding", json.loads((self.dir / pace.STATE_FILE).read_text())["reason"])


class ReviewFixes(Env):
    """#1375 review: pushback that is not a refusal, neutral scoped limits,
    accepted-only full runs, measured run interval, modest finish budget."""

    def test_timeout_or_unclassified_pushback_halves(self):
        new, reason, _ = pace.decide(12, submits=12, signals=[], refusals=0, outcome="completed", pushback=1)
        self.assertEqual(6, new)
        self.assertIn("timeout or unclassified", reason)

    def test_scoped_limit_holds_without_raising(self):
        new, reason, _ = pace.decide(12, submits=12, signals=[], refusals=0, outcome="completed", scoped=2)
        self.assertEqual(12, new)
        self.assertIn("per-source limit", reason)

    def test_full_allowance_counts_only_accepted_submits(self):
        self.assertEqual(12, pace.decide(12, submits=12, signals=[], refusals=0, outcome="completed",
                                         accepted=11)[0])
        self.assertEqual(14, pace.decide(12, submits=12, signals=[], refusals=0, outcome="completed",
                                         accepted=12)[0])

    def test_replay_throttle_capacity_reason_halves(self):
        self.assertEqual(6, pace.decide(12, submits=12, signals=[{"kind": "capacity", "reason": "replay_throttled"}],
                                        refusals=0, outcome="paused")[0])

    def test_runs_per_hour_uses_measured_starts(self):
        # Runs actually start every ~15.5 min, not every 13.
        starts = [1000.0 + i * 930 for i in range(5)]
        self.assertAlmostEqual(3600 / 930, pace.runs_per_hour({"run_starts": starts}))
        self.assertEqual(279, pace.target_buffer(12, {"run_starts": starts}))  # 12 x 3.871 x 6
        # Outage gaps (> 3 h) and garbage are ignored; nothing usable -> env default.
        self.assertAlmostEqual(60 / 13, pace.runs_per_hour({"run_starts": [0, 20000]}))
        self.assertAlmostEqual(60 / 13, pace.runs_per_hour({"run_starts": ["x"]}))
        self.assertAlmostEqual(60 / 13, pace.runs_per_hour(None))

    def test_record_keeps_recent_run_starts(self):
        state = pace.load(self.dir, initial=12, initial_gap_s=60, usable_s=630)
        for i in range(10):
            state = pace.record(self.dir, state, new_allowance=12, reason="r", last_run={}, gap_used_s=60,
                                usable_s=630, promotion=None, run_started=100.0 * i)
        saved = pace.load(self.dir, initial=12, initial_gap_s=60, usable_s=630)
        self.assertEqual([100.0 * i for i in range(2, 10)], saved["run_starts"])

    def test_defaults(self):
        self.assertEqual(6, pace.finish_checks())
        self.assertEqual(10, pace.owner_observe_max())
        with patch.dict(os.environ, {"WAYBACK_OWNER_OBSERVE_MAX": "0"}):
            self.assertEqual(0, pace.owner_observe_max())


class Promotion(Env):
    def test_target_is_six_hours_of_submits_with_a_floor(self):
        self.assertEqual(333, pace.target_buffer(12))   # 12 x 60/13 x 6 = 332.3
        self.assertEqual(1108, pace.target_buffer(40))
        self.assertEqual(100, pace.target_buffer(3))
        with patch.dict(os.environ, {"WAYBACK_RUN_INTERVAL_MIN": "30"}):
            self.assertEqual(144, pace.target_buffer(12))

    def test_cap_from_buffer_target_and_max(self):
        self.assertEqual(200, pace.promotion_cap(0, 333))
        self.assertEqual(33, pace.promotion_cap(300, 333))
        self.assertEqual(0, pace.promotion_cap(400, 333))
        with patch.dict(os.environ, {"WAYBACK_PROMOTE_MAX": "50"}):
            self.assertEqual(50, pace.promotion_cap(0, 333))

    def test_untried_buffer_counts_queue_urls_without_ledger_entry(self):
        urls = ["a", "b", "c", "d", "a"]
        done = {"b": {"status": "verified"}, "c": {"status": "new"}}
        self.assertEqual(3, pace.untried_buffer(urls, done))


class WorkerHooks(Env):
    def test_control_records_pushback_signals_without_changing_pauses(self):
        with Control(self.dir, "LOW a:b") as control:
            with self.assertRaises(Paused):
                control.provider_failed(429, "120")
            with self.assertRaises(Paused):
                control.capacity_wait("account_sessions")
            self.assertEqual("open", control.state["mode"])
            self.assertEqual([{"kind": "provider", "status": 429, "event": "http_throttled", "retry_after": True},
                              {"kind": "capacity", "reason": "account_sessions", "retry_after": False}],
                             control.pace_signals)

    def fake(self, **stats):
        plan = pace.load(self.dir, initial=12, initial_gap_s=0, usable_s=630)
        run = {"plan": plan, "allowance": plan["allowance"], "gap_s": 52.5, "submits": 12, "refusals": 0,
               "usable_s": 630}
        run.update(stats)
        return SimpleNamespace(directory=self.dir, pace_run=run, pace_signals=[],
                               pace_promotion={"target_buffer": 333, "buffer_before": 0, "promoted": 2,
                                               "cap": 200, "seconds": 3.0})

    def test_finish_pace_raises_and_prints_one_journal_line(self):
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            W.finish_pace(self.fake(), "completed")
        state = json.loads((self.dir / pace.STATE_FILE).read_text())
        self.assertEqual(14, state["allowance"])
        self.assertTrue(state["last_run"]["used_full_allowance"])
        self.assertEqual(2, state["promotion"]["promoted"])
        lines = [x for x in out.getvalue().splitlines() if x.startswith("PACE ")]
        self.assertEqual(1, len(lines))
        self.assertIn("allowance=12->14", lines[0])

    def test_finish_pace_cuts_on_network_refused_capacity_check(self):
        control = self.fake(submits=3)
        control.pace_signals.append({"kind": "capacity", "reason": "network_refused"})
        with contextlib.redirect_stdout(io.StringIO()):
            W.finish_pace(control, "paused")
        state = json.loads((self.dir / pace.STATE_FILE).read_text())
        self.assertEqual(6, state["allowance"])
        self.assertEqual(1, state["last_run"]["refusals"])

    def test_finish_pace_without_a_submit_window_leaves_state_alone(self):
        control = SimpleNamespace(directory=self.dir, pace_signals=[])
        out = io.StringIO()
        with contextlib.redirect_stdout(out):
            W.finish_pace(control, "paused")
        self.assertFalse((self.dir / pace.STATE_FILE).exists())
        self.assertIn("PACE held", out.getvalue())


if __name__ == "__main__":
    unittest.main()
