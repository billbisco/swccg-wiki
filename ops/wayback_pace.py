"""Self-tuning Save Page Now pace for the Wayback owner (swccg-guild/work#1375, D4).

Bill 2026-11-26: "I thought we were letting the archive droid itself determine
the best speed to proceed." The worker keeps one number per run, the submit
allowance, and tunes it with AIMD (additive increase, multiplicative decrease):

* A run that used its whole allowance with no provider pushback raises the
  allowance by RAISE_STEP (+2), up to WAYBACK_PACE_MAX (default 40).
* Any provider pushback during the run (HTTP 429 / 403 / 5xx, Retry-After,
  connection refused, authentication stop) halves it, down to WAYBACK_PACE_MIN
  (default 3). Nothing raises it again until a later clean, full run.
* "Account capacity unavailable" (SPN2 concurrency slots, unknown capacity or
  the daily account limit) is neutral: it never raises the allowance and never
  cuts it; the existing short capacity wait already handles it.
* A run that ended early (queue empty, deadline, half-open canary, cooldown)
  holds the allowance.

The gap between submits spreads the allowance over the run's usable time
(gap = max(WAYBACK_GAP_MIN_S, usable_seconds / allowance)). It only paces our
own submits: provider cooldowns, Retry-After, auth_blocked and the one-canary
rule stay in wayback_control.Control and always win, because they raise Paused
before any submit.

The adaptive promotion target keeps about six hours of work buffered in
queue.txt (see target_buffer). State lives outside Git in the control
directory: pace-state.json (atomic) and pace-log.jsonl (one line per change).
No network call lives here.
"""
from __future__ import annotations

import json
import math
import os
from datetime import datetime, timezone
from pathlib import Path

from wayback_control import atomic_json

SCHEMA_VERSION = 1
STATE_FILE = "pace-state.json"
LOG_FILE = "pace-log.jsonl"
RAISE_STEP = 2            # additive increase after a clean, full run
CUT_DIVISOR = 2           # multiplicative decrease after provider pushback
DEFAULT_INITIAL = 12      # allowance when neither state nor WAYBACK_MAX_SUBMITS exists
BUFFER_FLOOR = 100        # never keep fewer untried queue URLs than this
BUFFER_HOURS = 6          # promotion keeps this many hours of submits buffered
SUBMIT_RESERVE_S = 90     # the submit loop stops 90 s before the run deadline

# Provider events that mean "slow down". capacity_wait reasons other than
# network_refused are SPN2 concurrency / accounting and stay neutral.
CUT_CAPACITY_REASONS = {"network_refused"}


def _env_int(name: str, default: int, low: int = 1) -> int:
    try:
        value = int(os.environ.get(name) or default)
    except ValueError:
        value = default
    return value if value >= low else default


def _env_float(name: str, default: float, low: float = 0.0) -> float:
    try:
        value = float(os.environ.get(name) or default)
    except ValueError:
        value = default
    return value if math.isfinite(value) and value >= low else default


def bounds() -> dict:
    low = _env_int("WAYBACK_PACE_MIN", 3)
    high = max(low, _env_int("WAYBACK_PACE_MAX", 40))
    return {"min": low, "max": high, "gap_min_s": _env_float("WAYBACK_GAP_MIN_S", 15.0, 1.0)}


def promote_max() -> int:
    return _env_int("WAYBACK_PROMOTE_MAX", 200, 0)


def promote_seconds() -> float:
    return _env_float("WAYBACK_PROMOTE_SECONDS", 150.0, 1.0)


def finish_checks() -> int:
    return _env_int("WAYBACK_FINISH_CHECKS", 20, 0)


def runs_per_hour() -> float:
    return 60.0 / _env_float("WAYBACK_RUN_INTERVAL_MIN", 13.0, 1.0)


def iso(t: datetime | None = None) -> str:
    return (t or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ")


def plan_gap(allowance: int, usable_s: float, gap_min_s: float, floor_s: float = 0.0) -> float:
    """Spread the allowance over the usable seconds, never below the floors."""
    spread = max(0.0, usable_s) / max(1, allowance)
    return round(max(gap_min_s, floor_s, spread), 1)


def load(directory: Path, *, initial: int, initial_gap_s: float, usable_s: float) -> dict:
    """Saved pace state, or a fresh one from WAYBACK_MAX_SUBMITS / WAYBACK_GAP_S."""
    b = bounds()
    path = Path(directory) / STATE_FILE
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
        if state.get("schema_version") != SCHEMA_VERSION or type(state.get("allowance")) is not int:
            raise ValueError("unknown pace state")
        # Bounds may have been changed in the drop-in since the last run.
        state["allowance"] = max(1, min(b["max"], max(b["min"], state["allowance"])))
        state["bounds"] = b
        state["fresh"] = False
        return state
    except FileNotFoundError:
        pass
    except (OSError, ValueError, TypeError, AttributeError):
        print("PACE-STATE unreadable; starting from the configured initial pace", flush=True)
    # The operator's initial value is taken as-is (1..max); AIMD then works in [min, max].
    allowance = max(1, min(b["max"], int(initial) if initial and initial > 0 else DEFAULT_INITIAL))
    return {"schema_version": SCHEMA_VERSION, "updated_at": None, "allowance": allowance,
            "gap_s": plan_gap(allowance, usable_s, b["gap_min_s"], initial_gap_s), "bounds": b,
            "last_run": None, "reason": "initial pace from WAYBACK_MAX_SUBMITS / WAYBACK_GAP_S",
            "promotion": None, "fresh": True, "initial_gap_s": float(initial_gap_s or 0)}


def classify(signals: list[dict], refusals: int) -> tuple[str | None, bool]:
    """('cut' | 'hold' | None, rate_limited) from Control.pace_signals and submit refusals."""
    rate_limited = any(s.get("kind") == "provider" and (s.get("status") == 429 or s.get("retry_after"))
                       for s in signals)
    cut = refusals > 0 or any(
        s.get("kind") in {"provider", "auth"} or
        (s.get("kind") == "capacity" and s.get("reason") in CUT_CAPACITY_REASONS) for s in signals)
    if cut:
        return "cut", rate_limited
    if any(s.get("kind") == "capacity" for s in signals):
        return "hold", rate_limited
    return None, rate_limited


def decide(allowance: int, *, submits: int, signals: list[dict], refusals: int,
           outcome: str, b: dict | None = None) -> tuple[int, str, bool]:
    """AIMD step: (new_allowance, reason, rate_limited)."""
    b = b or bounds()
    verdict, rate_limited = classify(signals, refusals)
    if verdict == "cut":
        new = min(allowance, max(b["min"], allowance // CUT_DIVISOR))
        what = ", ".join(sorted({s.get("event") or s.get("reason") or s.get("kind") for s in signals} |
                                ({"connection refused on submit"} if refusals else set())))
        return new, f"archive.org pushed back ({what}); halved and holding until a clean full run", rate_limited
    if verdict == "hold":
        what = ", ".join(sorted({s.get("reason") for s in signals if s.get("kind") == "capacity"}))
        return allowance, f"account capacity unavailable ({what}) is SPN2 concurrency, not a speed signal; holding", rate_limited
    if outcome != "completed":
        return allowance, f"run {outcome} without provider pushback; holding", rate_limited
    if submits < allowance:
        return allowance, f"run used {submits} of {allowance} submits (queue or time ran out); holding", rate_limited
    new = min(b["max"], max(b["min"], allowance + RAISE_STEP))
    if new == allowance:
        return allowance, f"clean full run at the {b['max']}-submit ceiling; holding", rate_limited
    return new, f"clean full run ({submits} submits, no refusal or 429); raised by {RAISE_STEP}", rate_limited


def record(directory: Path, state: dict, *, new_allowance: int, reason: str, last_run: dict,
           gap_used_s: float, usable_s: float, promotion: dict | None, at: str | None = None) -> dict:
    """Persist the next pace atomically and append a log line if anything changed."""
    directory = Path(directory)
    b = bounds()
    at = at or iso()
    new_gap = plan_gap(new_allowance, usable_s, b["gap_min_s"])
    out = {"schema_version": SCHEMA_VERSION, "updated_at": at, "allowance": int(new_allowance),
           "gap_s": float(new_gap), "bounds": b, "last_run": last_run, "reason": reason,
           "promotion": promotion}
    atomic_json(directory / STATE_FILE, out)
    old = int(state.get("allowance", new_allowance))
    if old != new_allowance or abs(float(gap_used_s) - new_gap) >= 0.05 or state.get("fresh"):
        line = {"at": at, "from": old, "to": int(new_allowance), "gap_from": float(gap_used_s),
                "gap_to": float(new_gap), "reason": reason}
        with (directory / LOG_FILE).open("a", encoding="utf-8") as stream:
            stream.write(json.dumps(line, sort_keys=True) + "\n")
    return out


def journal_line(old: int, new: int, gap_from: float, gap_to: float, last_run: dict, reason: str) -> str:
    return (f"PACE allowance={old}->{new} gap={gap_from}s->{gap_to}s submits={last_run['submits']}/{old} "
            f"refusals={last_run['refusals']} rate_limited={str(last_run['rate_limited']).lower()} "
            f"full={str(last_run['used_full_allowance']).lower()} reason={json.dumps(reason)}")


def target_buffer(allowance: int) -> int:
    """About BUFFER_HOURS of submits at the current pace, never under BUFFER_FLOOR.

    allowance submits per run x runs per hour (60 / WAYBACK_RUN_INTERVAL_MIN,
    13 min on gemp) x 6 h. 12/run -> 333, 40/run -> 1108.
    """
    return max(BUFFER_FLOOR, math.ceil(allowance * runs_per_hour() * BUFFER_HOURS))


def untried_buffer(urls: list[str], done: dict) -> int:
    """Queue URLs nobody has tried yet: no ledger entry, or status 'new'."""
    return sum(1 for url in dict.fromkeys(urls) if url not in done or (done[url] or {}).get("status") == "new")


def promotion_cap(buffer: int, target: int, cap: int | None = None) -> int:
    cap = promote_max() if cap is None else cap
    return max(0, min(cap, target - buffer))
