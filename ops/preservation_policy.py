"""Ticket auto-approval policy read by the existing Wayback owner run.

Bill, 2026-11-25 (swccg-guild/work#1359 Q1): "Have the worker auto-approve every
registered item that has a ticket number." A registered object is approved by
this policy when its latest observation is ``ready`` (valid backup receipts,
source proof and readiness), it carries a work ticket number in
``approval_scope.ticket``, it is not withdrawn or suppressed and it does not
carry the 14 Nov 2026 hold. Held, not-ready and ticketless objects stay out;
ticketless ready objects are flagged.

Approvals are recorded append-only in ``registry/policy-approvals.jsonl``
(first record per object wins). ``approved-objects.json`` is not rewritten: it
keeps its 5,000-ID / 1 MiB guard for operator approvals. Each run the owner gets
the explicit approvals plus a bounded first-approved-first window of policy
objects that are still ready and not yet verified, so the adapter's existing
5,000-object budget is unchanged. How many jobs are promoted per run is the
worker's adaptive queue-buffer cap (#1375), not this policy.

No capture submission, queue write or network call lives here.
"""
from __future__ import annotations

import fcntl
import json
import os
import re
import time
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

from preservation_contracts import registration_job_id, registration_object_id
from preservation_registry import atomic_json, object_state
from preservation_owner_receipts import load_event
from preservation_suppression import suppressed_source, suppressed_url

POLICY = "ticket-auto-approval-v1"
POLICY_REASON = ("Bill 2026-11-25 (swccg-guild/work#1359 Q1): auto-approve every registered "
                 "item that is ready, has a backup receipt and a work ticket number.")
HOLD_MARK = "Bill all-agent Archive.org hold 2026-11-14"
LOG_NAME = "policy-approvals.jsonl"
STATE_NAME = "policy-state.json"
FLAGGED_NAME = "policy-unapproved.json"
MAX_ALLOWED = 5000              # same budget as load_allowed_objects / OwnerAdapter
SCAN_INTERVAL_S = 3600          # full registry scan at most hourly
MIN_SCAN_SECONDS_LEFT = 540     # never spend the end of a run scanning
_ISSUE = re.compile(r"^https://github\.com/swccg-guild/work/issues/(\d{1,6})/?$")
_NUMBER = re.compile(r"^#?(\d{1,6})$")
_OID = re.compile(r"^[0-9a-f]{64}$")


def ticket_number(value) -> int | None:
    """A positive work ticket: 123, "123", "#123" or a swccg-guild/work issue URL."""
    if isinstance(value, bool) or value is None:
        return None
    if isinstance(value, int):
        return value if 0 < value < 1_000_000 else None
    text = str(value).strip()
    m = _NUMBER.match(text) or _ISSUE.match(text)
    if not m:
        return None
    n = int(m.group(1))
    return n if n > 0 else None


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _latest(directory: Path):
    best = None
    try:
        names = os.listdir(directory)
    except OSError:
        return None
    for name in names:
        if not name.endswith(".json"):
            continue
        try:
            with open(directory / name, encoding="utf-8") as fh:
                data = json.load(fh)
        except (OSError, ValueError):
            continue
        if not isinstance(data, dict):
            continue
        try:
            generation = int(data.get("generation", 0) or 0)
        except (TypeError, ValueError):
            continue
        if best is None or generation >= best[0]:
            best = (generation, data)
    return best[1] if best else None


def decide(registry: Path, object_id: str, request: dict) -> tuple[str, int | None]:
    """('approve', ticket) or a reason it stays out."""
    try:
        source, subject = request["source"], request["subject"]
        if registration_object_id(subject, source) != object_id:
            return "identity-mismatch", None
        state = object_state(request)
    except Exception:
        return "invalid", None
    reason = str((request.get("readiness") or {}).get("reason") or "")
    if HOLD_MARK in reason:
        return "held", None
    if state != "ready":
        return "not-ready", None
    try:
        if suppressed_source(registry, source) or suppressed_url(registry, source["url"]):
            return "suppressed", None
    except Exception:
        return "invalid", None
    ticket = ticket_number((request.get("approval_scope") or {}).get("ticket"))
    if ticket is None:
        return "no-ticket", None
    return "approve", ticket


def load_log(registry: Path) -> dict[str, dict]:
    """object_id -> first approval record (order preserved)."""
    out: dict[str, dict] = {}
    path = Path(registry) / LOG_NAME
    try:
        fh = open(path, encoding="utf-8")
    except OSError:
        return out
    with fh:
        for line in fh:
            try:
                rec = json.loads(line)
            except ValueError:
                continue
            oid = rec.get("object_id") if isinstance(rec, dict) else None
            if isinstance(oid, str) and _OID.match(oid) and oid not in out:
                out[oid] = rec
    return out


def _append(path: Path, records: list[dict]) -> None:
    if not records:
        return
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_APPEND, 0o600)
    with os.fdopen(fd, "a", encoding="utf-8") as fh:
        fcntl.flock(fh.fileno(), fcntl.LOCK_EX)
        for rec in records:
            fh.write(json.dumps(rec, sort_keys=True, separators=(",", ":")) + "\n")
        fh.flush()
        os.fsync(fh.fileno())


def scan(registry: Path, explicit: set[str], approved: dict[str, dict], *, at: str | None = None):
    """Walk the registry once; return (new approval records, flagged summary)."""
    registry = Path(registry)
    at = at or _now_iso()
    new, reasons, flagged_ids = [], Counter(), {"no-ticket": []}
    requests = registry / "requests"
    try:
        jobs = sorted(os.listdir(requests))
    except OSError:
        jobs = []
    for job in jobs:
        jdir = requests / job
        try:
            objects = sorted(os.listdir(jdir))
        except OSError:
            continue
        for oid in objects:
            if not _OID.match(oid) or oid in explicit or oid in approved:
                continue
            request = _latest(jdir / oid)
            if request is None:
                continue
            verdict, ticket = decide(registry, oid, request)
            reasons[verdict] += 1
            if verdict == "approve":
                source = request["source"]
                new.append({"schema_version": 1, "kind": "auto-approval", "policy": POLICY,
                            "object_id": oid, "job_id": registration_job_id(source), "ticket": ticket,
                            "at": at, "source": {"url": source["url"], "sha256": source["sha256"],
                                                 "bytes": source["bytes"]}})
            elif verdict == "no-ticket":
                flagged_ids["no-ticket"].append(oid)
    flagged = {"schema_version": 1, "policy": POLICY, "checked_at": at,
               "counts": dict(reasons), "no_ticket": len(flagged_ids["no-ticket"]),
               "no_ticket_object_ids": flagged_ids["no-ticket"]}
    return new, flagged


def window(registry: Path, approved: dict[str, dict], explicit: set[str], *, cap: int) -> set[str]:
    """First-approved-first policy objects still ready and not yet owner-verified."""
    registry = Path(registry)
    out: set[str] = set()
    if cap <= 0:
        return out
    for oid, rec in approved.items():
        if len(out) >= cap:
            break
        if oid in explicit:
            continue
        job = str(rec.get("job_id") or "")
        sha = job.split(":", 1)[1] if job.startswith("payload:") else ""
        if not re.fullmatch(r"[0-9a-f]{64}", sha):
            continue
        request = _latest(registry / "requests" / sha / oid)
        if request is None or decide(registry, oid, request)[0] != "approve":
            # Re-check every run: held, withdrawn or no-longer-ready objects drop out.
            continue
        try:
            event = load_event(registry, request["source"])
        except Exception:
            event = None
        if event and event.get("state") == "verified":
            continue
        out.add(oid)
    return out


def apply(registry: Path, explicit: set[str], *, seconds_left: float, now: float | None = None,
          force_scan: bool = False) -> dict:
    """Record new policy approvals (hourly scan) and return this run's bounded window."""
    registry = Path(registry)
    now = time.time() if now is None else now
    state_path = registry / STATE_NAME
    try:
        state = json.loads(state_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        state = {}
    approved = load_log(registry)
    new: list[dict] = []
    scanned = False
    last = state.get("last_scan_epoch")
    due = force_scan or last is None or now - float(last) >= SCAN_INTERVAL_S
    if due and seconds_left >= MIN_SCAN_SECONDS_LEFT:
        started = time.monotonic()
        new, flagged = scan(registry, set(explicit), approved)
        _append(registry / LOG_NAME, new)
        for rec in new:
            approved.setdefault(rec["object_id"], rec)
        atomic_json(registry / FLAGGED_NAME, flagged)
        state = {"schema_version": 1, "policy": POLICY, "last_scan_epoch": now,
                 "last_scan_at": datetime.fromtimestamp(now, timezone.utc).isoformat(timespec="seconds"),
                 "scan_seconds": round(time.monotonic() - started, 1),
                 "approved_total": len(approved), "new_last_scan": len(new),
                 "no_ticket": flagged["no_ticket"]}
        atomic_json(state_path, state)
        scanned = True
    cap = MAX_ALLOWED - len(set(explicit))
    win = window(registry, approved, set(explicit), cap=cap)
    return {"window": win, "new": len(new), "new_by_ticket": dict(Counter(r["ticket"] for r in new)),
            "approved_total": len(approved), "no_ticket": state.get("no_ticket"),
            "scanned": scanned, "cap": cap}
