"""Persistent circuit and exclusive owner for the existing Wayback queue.

Control files live outside Git. All clients enqueue to this server owner; this
filesystem lock deliberately does not claim to coordinate other hosts.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import time
from collections import Counter
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path


class Paused(Exception):
    """The durable control record explains when or how work can resume."""


class Busy(Exception):
    """Another process owns the same control directory."""


def timestamp(epoch: float | None) -> str | None:
    return datetime.fromtimestamp(epoch, timezone.utc).isoformat() if epoch else None


def retry_seconds(value: str | None, clock: float) -> float:
    """Retry-After can be delay-seconds or an HTTP date; never shorten it."""
    if not value:
        return 0
    try:
        return max(0, float(int(value)))
    except ValueError:
        try:
            date = parsedate_to_datetime(value)
            if date.tzinfo is None:
                return 0
            return max(0, date.timestamp() - clock)
        except (ValueError, TypeError, OverflowError):
            return 0


def atomic_json(path: Path, data: dict) -> None:
    temp = path.with_name(path.name + f".{os.getpid()}.part")
    try:
        with temp.open("w", encoding="utf-8") as stream:
            json.dump(data, stream, indent=2, sort_keys=True, allow_nan=False)
            stream.write("\n")
            stream.flush()
            os.fsync(stream.fileno())
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


class Control:
    MIN_PAUSE = 15 * 60
    MAX_PAUSE = 24 * 60 * 60
    SUBMISSION_GAP = 10
    PROBE_DEADLINE = 24 * 60 * 60

    def __init__(self, directory: Path, credential: str | None, clock=time.time):
        self.directory = Path(directory)
        self.clock = clock
        # Never emit this digest in health, logs, repository records or evidence.
        self.credential = hashlib.sha256(credential.encode()).hexdigest() if credential else None
        self.state: dict = {}
        self.lock = None
        # Runtime ledger snapshots support crash recovery; not control.json data.
        self.done: dict = {}
        self.initial_done: dict = {}

    def __enter__(self):
        self.directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        self.lock = (self.directory / "owner.lock").open("a+b")
        self.lock.seek(0, os.SEEK_END)
        if self.lock.tell() == 0:
            self.lock.write(b"0")
            self.lock.flush()
        self.lock.seek(0)
        try:
            if os.name == "nt":
                import msvcrt
                msvcrt.locking(self.lock.fileno(), msvcrt.LK_NBLCK, 1)
            else:
                import fcntl
                fcntl.flock(self.lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except OSError as error:
            self.lock.close()
            self.lock = None
            raise Busy("existing Wayback owner is active") from error
        path = self.directory / "control.json"
        try:
            self.state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {
                "schema": 1, "mode": "healthy", "failure_count": 0,
                "next_attempt": 0, "probe_url": None,
            }
            self._validate()
        except Exception:
            self.__exit__(None, None, None)
            raise
        return self

    def __exit__(self, *args):
        if self.lock:
            try:
                self.lock.seek(0)
                if os.name == "nt":
                    import msvcrt
                    msvcrt.locking(self.lock.fileno(), msvcrt.LK_UNLCK, 1)
                else:
                    import fcntl
                    fcntl.flock(self.lock, fcntl.LOCK_UN)
            finally:
                self.lock.close()
                self.lock = None

    def _validate(self):
        s = self.state
        if (s.get("schema") != 1 or s.get("mode") not in
                {"healthy", "open", "auth_blocked", "half_open", "probe_blocked"} or
                not isinstance(s.get("failure_count"), int) or s["failure_count"] < 0 or
                not isinstance(s.get("next_attempt"), (int, float)) or
                not math.isfinite(s["next_attempt"]) or s["next_attempt"] < 0 or
                not isinstance(s.get("next_submission_at", 0), (int, float)) or
                not math.isfinite(s.get("next_submission_at", 0)) or
                s.get("next_submission_at", 0) < 0 or
                not isinstance(s.get("probe_started_at", 0), (int, float)) or
                not math.isfinite(s.get("probe_started_at", 0)) or
                s.get("probe_started_at", 0) < 0 or
                not (s.get("probe_url") is None or isinstance(s["probe_url"], str))):
            raise ValueError("Invalid Wayback control state; refusing network work")

    def save(self):
        self.state["updated_at"] = timestamp(self.clock())
        atomic_json(self.directory / "control.json", self.state)

    def restore_updates(self, done: dict) -> dict:
        """Recover acknowledged jobs that had not reached the Git ledger yet."""
        path = self.directory / "pending-updates.json"
        if not path.exists():
            return {}
        data = json.loads(path.read_text(encoding="utf-8"))
        if data.get("schema") != 1 or not isinstance(data.get("updates"), dict):
            raise ValueError("Invalid pending-job journal; refusing network work")
        restored = {}
        for url, entry in data["updates"].items():
            current = done.get(url)
            if current != data["base"].get(url) and current != entry:
                raise ValueError("Pending-job journal conflicts with newer ledger; preserve both and reconcile")
            if current != entry:
                done[url] = entry
                restored[url] = entry
        return restored

    def checkpoint(self, done: dict, baseline: dict):
        updates = {u:e for u,e in done.items() if e != baseline.get(u)}
        if updates:
            atomic_json(self.directory / "pending-updates.json", {
                "schema": 1, "base": {u:baseline.get(u) for u in updates}, "updates": updates,
            })

    def ledger_saved(self):
        path = self.directory / "pending-updates.json"
        if path.exists():
            path.unlink()

    def begin(self):
        s = self.state
        if s["mode"] == "probe_blocked":
            if self.done.get(s.get("probe_url"), {}).get("status") == "verified":
                self.reconcile(self.done, set())
            else:
                raise Paused("accepted recovery canary needs reconciliation; no request made")
        if s["mode"] == "auth_blocked":
            if not self.credential or self.credential == s.get("rejected_credential"):
                raise Paused("authentication repair required; no request made")
            s.update(mode="half_open", next_attempt=0,
                     reason="changed credential requires verified canary")
        if s["next_attempt"] > self.clock():
            raise Paused("shared cooldown is still active; no request made")
        if s.get("next_submission_at", 0) > self.clock():
            raise Paused("shared submission pacing is still active; no request made")
        if s["mode"] == "open":
            s.update(mode="half_open",
                     reason="provider recovery requires verified canary")
        self.save()

    def may_submit(self, url: str) -> bool:
        return (self.state["mode"] in {"healthy", "half_open"} and
                self.state.get("next_submission_at", 0) <= self.clock() and
                not (self.state["mode"] == "half_open" and self.state.get("probe_url")))

    def submitting(self, url: str):
        if not self.may_submit(url):
            raise Paused("one recovery canary is awaiting verification")
        if self.state["mode"] == "half_open":
            self.state["probe_url"] = url
            self.state["probe_started_at"] = self.clock()
        self.state["last_submission_attempt_at"] = timestamp(self.clock())
        self.state["next_submission_at"] = self.clock() + self.SUBMISSION_GAP
        self.save()

    def authentication_failed(self):
        accepted = self.accepted_probe()
        self.state.update(mode="auth_blocked", reason="authentication rejected",
                          http_status=401, rejected_credential=self.credential,
                          next_attempt=0, probe_url=accepted)
        self.save()
        self._pause_with_repair("authentication rejected; authorized account repair required",
                               "authentication rejected; no anonymous fallback")

    def provider_failed(self, status: int | None = None, retry_after: str | None = None):
        count = self.state["failure_count"] + 1
        delay = min(self.MAX_PAUSE, self.MIN_PAUSE * 2 ** min(count - 1, 7))
        delay = max(delay, retry_seconds(retry_after, self.clock()))
        self.state.update(mode="open", failure_count=count,
                          reason="provider throttled" if status == 429 else "provider unavailable",
                          http_status=status, next_attempt=self.clock() + delay, probe_url=self.accepted_probe())
        self.save()
        self._pause_with_repair(self.state["reason"], "provider circuit opened; shared cooldown persisted")

    def accepted_probe(self):
        probe = self.state.get("probe_url")
        entry = self.done.get(probe, {})
        return probe if entry.get("job_id") or entry.get("capture") else None

    def probe_needs_repair(self, reason: str):
        # Keep probe_url and its accepted job/capture in the ledger and journal.
        self.state.update(mode="probe_blocked", reason=reason, next_attempt=0)
        self.save()
        self._pause_with_repair(reason, "accepted recovery canary requires owned reconciliation")

    def _pause_with_repair(self, reason: str, message: str):
        try:
            self._repair(reason)
        except (OSError, ValueError, KeyError, TypeError) as error:
            self.state["repair_record_error"] = type(error).__name__
            self.save()
        raise Paused(message)

    def _repair(self, reason: str):
        path = self.directory / "repair.json"
        old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {}
        identity = hashlib.sha256(reason.encode()).hexdigest()[:16]
        same = old.get("incident_id") == identity and old.get("status") == "open"
        atomic_json(path, {
            "schema": 1, "incident_id": identity, "status": "open", "reason": reason,
            "owner": "MemoryCoreChatGPT", "repair_issue": 407,
            "first_seen_at": old["first_seen_at"] if same else timestamp(self.clock()),
            "last_seen_at": timestamp(self.clock()),
            "occurrences": old.get("occurrences", 0) + 1 if same else 1,
            "next_eligible_attempt_at": timestamp(self.state["next_attempt"]),
        })

    def reconcile(self, done: dict, previously_verified: set[str]):
        newly_verified = [u for u, e in done.items() if e.get("status") == "verified"
                          and u not in previously_verified]
        if newly_verified:
            self.state["last_verified_progress_at"] = timestamp(self.clock())
        probe = self.state.get("probe_url")
        if self.state["mode"] in {"half_open", "probe_blocked"} and probe:
            entry = done.get(probe, {})
            if entry.get("status") == "verified":
                self.state.update(mode="healthy", failure_count=0, next_attempt=0,
                                  probe_url=None, reason="verified recovery canary")
                repair = self.directory / "repair.json"
                if repair.exists():
                    data = json.loads(repair.read_text(encoding="utf-8"))
                    data.update(status="recovered", recovered_at=timestamp(self.clock()))
                    atomic_json(repair, data)
            elif self.state["mode"] == "half_open" and entry.get("status") in {"retry", "failed", "unverified"}:
                # A source-specific rejection does not certify provider recovery.
                self.state.update(probe_url=None, next_attempt=self.clock() + self.MIN_PAUSE,
                                  reason="canary unverified; next bounded probe deferred")
        self.save()

    def health(self, done: dict, outcome: str):
        counts = Counter(e.get("status", "unknown") for e in done.values())
        pending = [e.get("last") for e in done.values()
                   if e.get("status") in {"pending", "retry"} and e.get("last")]
        awaiting = bool(self.state["mode"] == "half_open" and self.state.get("probe_url"))
        health = {
            "schema": 1, "checked_at": timestamp(self.clock()), "owner": "server-wayback-queue",
            "outcome": outcome, "mode": self.state["mode"],
            "reason": self.state.get("reason"), "http_status": self.state.get("http_status"),
            "next_eligible_attempt_at": None if self.state["mode"] in {"auth_blocked", "probe_blocked"} or awaiting else
                timestamp(max(self.state["next_attempt"], self.state.get("next_submission_at", 0))),
            "awaiting_canary_verification": awaiting,
            "last_submission_attempt_at": self.state.get("last_submission_attempt_at"),
            "last_verified_progress_at": self.state.get("last_verified_progress_at"),
            "ledger_status_counts": dict(counts),
            "oldest_pending_activity_at": min(pending) if pending else None,
            "repair_issue": 407 if self.state["mode"] != "healthy" else None,
            "process_success_is_capture_success": False,
        }
        atomic_json(self.directory / "health.json", health)
        return health
