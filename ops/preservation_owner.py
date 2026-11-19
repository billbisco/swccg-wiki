"""Bounded registry adapter called inside the existing Wayback owner.

No capture submission endpoint or executable entry point lives here. The worker
keeps its one Control lock, accepted-job journal, provider circuit and timer.
"""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import time
from datetime import datetime, timezone
from pathlib import Path

from preservation_backups import independent_receipt, payload_hashes
from preservation_contracts import canonical_bytes, registration_object_id, registration_job_id
from preservation_registry import (SERVER_OWNER, advance_readiness, atomic_json,
                                   iter_records, object_state, source_receipt)
from preservation_owner_receipts import load_event, store_event
from wayback_control import Paused
from preservation_suppression import suppressed_source, suppressed_url

PUBLIC_STAGE_BUDGET = 32 * 1024 * 1024
STAGE_SCAN_LIMIT = 50000
DISK_RESERVE = 2 * 1024 * 1024 * 1024
DEFAULT_WORK = Path("/mnt/HC_Volume_107153504/work/swccg-preservation-owner")


def load_allowed_objects(registry: Path) -> set[str]:
    """Read an explicitly installed owner approval, never the global inbox."""
    path = registry / "approved-objects.json"
    if not path.exists():
        return set()
    with path.open("rb") as stream:
        raw = stream.read(1024 * 1024 + 1)
    if len(raw) > 1024 * 1024:
        raise ValueError("owner cohort approval exceeds its metadata budget")
    document = json.loads(raw)
    if document.get("schema_version") != 1 or document.get("owner") != SERVER_OWNER or not document.get("approval_scope"):
        raise ValueError("exact owner cohort approval is required")
    objects = document.get("object_ids")
    if not isinstance(objects, list) or len(objects) > 5000 or any(not isinstance(item, str) or len(item) != 64 or any(c not in "0123456789abcdef" for c in item) for item in objects):
        raise ValueError("approved cohort must list exact object identities")
    return set(objects)


class OwnerAdapter:
    def __init__(self, worker, repository: Path, control, allowed_objects: set[str], *,
                 work=DEFAULT_WORK,
                 stage_budget=PUBLIC_STAGE_BUDGET, limit=2, readback=independent_receipt):
        self.worker, self.repository, self.control = worker, repository, control
        if getattr(worker, "ACTIVE_CONTROL", None) is not control or not getattr(control, "lock", None) or control.lock.closed:
            raise PermissionError("adapter requires the existing active Control owner; no client-local owner claim")
        self.registry = control.directory / "registry"
        self.allowed = frozenset(allowed_objects)
        if len(self.allowed) > 5000:
            raise ValueError("approved cohort exceeds its explicit mapping budget")
        self.work, self.stage_budget, self.limit = Path(work), stage_budget, limit
        self.readback = readback
        self.observations = []
        self.last_capture_observation = None

    def healthy(self):
        return self.control.state.get("mode") == "healthy"

    def _eligible(self, entry):
        request = entry["request"]
        key = registration_object_id(request["subject"], request["source"])
        if suppressed_source(self.registry, request["source"]):
            return False
        # Registration owner names the client's continuation owner. Capture
        # authority is the active Control lock plus the exact approved cohort.
        adopted = load_event(self.registry, request["source"], object_id=key,
                             request_id=entry["request_id"], subject=request["subject"])
        if adopted and adopted.get("adoption") and adopted.get("state") == "verified":
            return False
        return (key in self.allowed and
                object_state(request) in {"ready", "awaiting_stage"})

    def _groups(self):
        groups = {}
        for entry in iter_records(self.registry, object_ids=self.allowed):
            if self._eligible(entry):
                request = entry["request"]
                key = registration_job_id(request["source"])
                group = groups.setdefault(key, {"entry": entry, "objects": []})
                group["objects"].append(registration_object_id(request["subject"], request["source"]))
        return groups

    def protected_snapshot_urls(self):
        """Approved managed targets await their separate strict cleanup seam."""
        protected = set()
        for entry in iter_records(self.registry, object_ids=self.allowed):
            request = entry["request"]
            key = registration_object_id(request["subject"], request["source"])
            url = request["source"]["url"]
            if key in self.allowed and self.worker.snapshot_file(url) is not None:
                protected.add(url)
        return protected

    def _event(self, entries, state, reason, *, approved_object_ids=None, **details):
        request = entries[0]["request"]
        return {"schema_version": 1, "job_id": registration_job_id(request["source"]),
                "source_sha256": request["source"]["sha256"], "source_bytes": request["source"]["bytes"],
                "approved_object_ids": approved_object_ids or [registration_object_id(row["request"]["subject"], row["request"]["source"]) for row in entries],
                "state": state, "reason": reason, "owner": SERVER_OWNER, **details}

    def _stage_usage(self):
        total, count = 0, 0
        root = self.worker.snapshot_root()
        if not root.exists():
            return 0
        for parent, directories, files in os.walk(root, followlinks=False):
            directories[:] = [name for name in directories if not (Path(parent) / name).is_symlink()]
            for name in files:
                count += 1
                if count > STAGE_SCAN_LIMIT:
                    raise ValueError("public staging inventory exceeds its bounded scan budget")
                total += (Path(parent) / name).stat().st_size
        return total

    def _stage(self, entry, deadline):
        request = entry["request"]
        source = request["source"]
        if suppressed_source(self.registry, source):
            return False
        if source.get("representation") != "checked_self_contained_snapshot":
            if source.get("representation", "original") != "original" or not self._check_public(source):
                return False
            advanced = advance_readiness(self.registry, entry,
                                         {"ready": True, "reason": "owner checked the already-public exact original payload", "stage_bytes": 0},
                                         owner=SERVER_OWNER)
            return advanced["state"] == "ready"
        target = self.worker.snapshot_file(source["url"])
        if target is None:
            raise ValueError("capture target is not an approved snapshot path")
        if target.exists():
            hashes = payload_hashes(target)
            if hashes["sha256"] != source["sha256"] or hashes["bytes"] != source["bytes"]:
                raise ValueError("existing public target has different bytes; do not overwrite peer staging")
        else:
            if self.work == DEFAULT_WORK and not os.path.ismount(DEFAULT_WORK.parents[1]):
                raise ValueError("approved persistent owner volume is not mounted; refusing root-disk fallback")
            if self._stage_usage() + source["bytes"] > self.stage_budget:
                return False
            if time.monotonic() > deadline - 90:
                return False
            self.work.mkdir(parents=True, exist_ok=True)
            if shutil.disk_usage(self.work).free < source["bytes"] + DISK_RESERVE:
                return False
            private = self.work / (source["sha256"] + ".restored")
            backup = source_receipt(request)
            # The original subject may be a page; this is the separately
            # validated source-payload receipt, never the wikitext receipt.
            temporary = None
            try:
                self.readback(backup["subject"], backup["storage"], restore_to=private)
                hashes = payload_hashes(private)
                if hashes["sha256"] != source["sha256"] or hashes["bytes"] != source["bytes"]:
                    raise ValueError("restored source differs from its approved capture payload")
                if not self.healthy() or time.monotonic() > deadline - 60:
                    return False
                target.parent.mkdir(parents=True, exist_ok=True)
                # Publish a fully fsynced sibling across volumes without
                # overwriting peer staging. Cleanup also covers late restores.
                temporary = target.with_name("." + target.name + "." + source["sha256"] + ".part")
                temporary.unlink(missing_ok=True)
                with private.open("rb") as original, temporary.open("xb") as output:
                    shutil.copyfileobj(original, output, 128 * 1024)
                    output.flush()
                    os.fsync(output.fileno())
                os.chmod(temporary, 0o644)
                os.link(temporary, target)
            finally:
                if temporary is not None:
                    temporary.unlink(missing_ok=True)
                private.unlink(missing_ok=True)
        readiness = {"ready": True, "reason": "owner restored the independently backed exact approved snapshot",
                     "stage_bytes": source["bytes"]}
        advanced = advance_readiness(self.registry, entry, readiness, owner=SERVER_OWNER)
        return advanced["state"] == "ready"

    def _check_public(self, source):
        if suppressed_source(self.registry, source):
            return False
        actual = self.worker.fetch(source["url"])
        return (actual.get("status") == 200 and actual.get("sha256") == source["sha256"] and
                actual.get("size") == source["bytes"])

    def _enqueue(self, url):
        if suppressed_url(self.registry, url):
            raise PermissionError("exact withdrawn source cannot be queued")
        def write():
            path = self.repository / self.worker.QUEUE
            text = path.read_text(encoding="utf-8") if path.exists() else ""
            if url not in {line.strip() for line in text.splitlines()}:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(text + ("\n" if text and not text.endswith("\n") else "") + url + "\n", encoding="utf-8")
            return [self.worker.QUEUE]
        self.worker.commit_and_push(self.repository, [], "register approved exact-payload capture target", write)

    @staticmethod
    def _retry_delta(source, previous):
        return {"status": "retry", "tries": 0, "last": "1970-01-01T00:00:00Z",
                "registered_payload_sha256": source["sha256"],
                "registry_job_id": registration_job_id(source),
                "previous_capture": previous["capture"], "recapture": True}

    @staticmethod
    def _epoch_applied(source, legacy):
        return (legacy.get("registered_payload_sha256") == source["sha256"] and
                legacy.get("registry_job_id") == registration_job_id(source))

    def _queued_epoch_delta(self, event, source, legacy):
        previous = event.get("superseded_worker_receipt")
        if (not previous or not legacy or self._epoch_applied(source, legacy) or
                legacy.get("status") == "pending" and legacy.get("job_id") or
                legacy.get("capture") != previous.get("capture")):
            return {}
        proof = event.get("superseded_capture_raw", {})
        if (not proof.get("strict_index") or proof.get("capture") != previous.get("capture") or
                (proof.get("raw_sha256") == source["sha256"] and proof.get("raw_bytes") == source["bytes"])):
            raise ValueError("queued version epoch lacks retained strict old-payload evidence")
        return self._retry_delta(source, previous)

    def _attention(self, entry, object_ids, job, error):
        if isinstance(error, Paused):
            raise error
        reason = type(error).__name__ + ": " + str(error)
        self.observations.append({"job_id": job, "state": "needs_attention", "reason": reason})
        store_event(self.registry, self._event([entry], "needs_attention", reason,
            approved_object_ids=object_ids,
            continuation="existing owner resolves this exact source/backup/staging finding while independent jobs continue"))

    def prepare(self, deadline):
        """Stage/promote only the supplied cohort; never submit or reset jobs."""
        if not self.healthy() or not self.allowed:
            return {"prepared": 0, "reason": "provider paused or no exact approved cohort supplied", "ledger_updates": {}}
        prepared = 0
        attempted, ledger_updates = 0, {}
        cursor_path = self.registry / "owner-prepare-cursor.json"
        cursor = json.loads(cursor_path.read_text(encoding="utf-8")).get("after", "") if cursor_path.exists() else ""
        groups = self._groups()
        ordered = [(key, value) for key, value in groups.items() if key > cursor] + [(key, value) for key, value in groups.items() if key <= cursor]
        for job, group in ordered:
            if attempted >= self.limit or time.monotonic() > deadline - 60 or not self.healthy():
                break
            entry, object_ids = group["entry"], group["objects"]
            request = entry["request"]
            source, job = request["source"], registration_job_id(request["source"])
            try:
                existing = load_event(self.registry, source)
            except Exception as error:
                attempted += 1
                atomic_json(cursor_path, {"after": job})
                self._attention(entry, object_ids, job, error)
                continue
            if existing and existing["state"] in {"queued", "submitted", "verified"}:
                if existing["approved_object_ids"] != object_ids:
                    store_event(self.registry, dict(existing, approved_object_ids=object_ids))
                if existing["state"] == "queued":
                    try:
                        delta = self._queued_epoch_delta(existing, source, self.control.done.get(source["url"], {}))
                        if delta:
                            attempted += 1
                            atomic_json(cursor_path, {"after": job})
                            if not self._check_public(source):
                                raise ValueError("queued epoch source no longer matches its exact payload")
                            self._enqueue(source["url"])
                            ledger_updates[source["url"]] = delta
                            prepared += 1
                    except Exception as error:
                        self._attention(entry, object_ids, job, error)
                continue
            attempted += 1
            atomic_json(cursor_path, {"after": job})
            try:
                if object_state(request) == "awaiting_stage":
                    if not self._stage(entry, deadline):
                        continue
                if not self._check_public(source):
                    raise ValueError("public capture target does not match its registered exact payload")
                # An existing accepted legacy job remains owned by the worker;
                # do not reset or duplicate it just to manufacture registry progress.
                legacy = self.control.done.get(source["url"], {})
                if legacy.get("job_id") and legacy.get("status") == "pending":
                    self._observe([entry], legacy, deadline, object_ids)
                    continue
                if legacy.get("capture") and legacy.get("status") in {"verified", "ok", "unverified", "failed", "retry"}:
                    outcome = self._observe([entry], legacy, deadline, object_ids)
                    if outcome == "different_payload":
                        if self._epoch_applied(source, legacy):
                            store_event(self.registry, self._event([entry], "needs_attention",
                                "applied version epoch still has different capture bytes; preserve retries for owned repair",
                                approved_object_ids=object_ids, superseded_worker_receipt=legacy,
                                accepted_job_id=legacy.get("job_id"),
                                continuation="review the existing epoch/provider result; do not reset this payload's retry budget"))
                            continue
                        # Preserve the complete prior URL receipt durably before
                        # asking the worker to retry this new exact payload.
                        self._enqueue(source["url"])
                        event = self._event([entry], "queued", "different historical payload retained; current exact version queued for an owned retry",
                                           approved_object_ids=object_ids,
                                           superseded_worker_receipt=legacy,
                                           superseded_capture_raw=self.last_capture_observation,
                                           queue_receipt={"queued": True, "url": source["url"], "job_id": job})
                        store_event(self.registry, event)
                        ledger_updates[source["url"]] = self._retry_delta(source, legacy)
                        prepared += 1
                    elif outcome != "verified":
                        store_event(self.registry, self._event([entry], "capture_check_pending",
                                    "existing capture cannot yet establish this exact version; preserve its receipt and retry verification", approved_object_ids=object_ids))
                    continue
                if legacy.get("status") == "failed":
                    store_event(self.registry, self._event([entry], "needs_attention",
                                "existing URL exhausted its retries without a usable exact-version capture; preserve receipt and request owned repair",
                                approved_object_ids=object_ids, superseded_worker_receipt=legacy,
                                continuation="existing owner reviews the terminal URL receipt; do not silently reset retries for the same payload"))
                    continue
                self._enqueue(source["url"])
                event = self._event([entry], "queued", "exact public payload registered with the existing ordered URL queue",
                                    approved_object_ids=object_ids,
                                    queue_receipt={"queued": True, "url": source["url"], "job_id": job})
                store_event(self.registry, event)
                prepared += 1
            except Exception as error:
                self._attention(entry, object_ids, job, error)
        return {"prepared": prepared, "attempted": attempted, "observations": self.observations, "ledger_updates": ledger_updates}

    def _observe(self, entries, legacy, deadline, object_ids=None):
        source = entries[0]["request"]["source"]
        self.last_capture_observation = None
        if legacy.get("job_id") and legacy.get("status") == "pending":
            store_event(self.registry, self._event(entries, "submitted", "existing owner has an accepted capture job",
                        approved_object_ids=object_ids,
                        accepted_job_id=legacy["job_id"], worker_entry_sha256=hashlib.sha256(canonical_bytes(legacy)).hexdigest()))
        capture = legacy.get("capture")
        if not capture or not self.healthy() or time.monotonic() > deadline - 30:
            return "pending"
        _, original = self.worker.capture_parts(capture)
        if original != source["url"]:
            return "identity_mismatch"
        good, why = self.worker.strict_check(capture)
        if not good or why != "ok":
            return "pending"
        actual = self.worker.fetch(self.worker.id_url(capture))
        if actual.get("status") != 200:
            return "pending"
        self.last_capture_observation = {"capture": capture, "capture_original_url": original,
                                         "strict_index": True, "raw_sha256": actual.get("sha256"), "raw_bytes": actual.get("size")}
        if actual.get("sha256") != source["sha256"] or actual.get("size") != source["bytes"]:
            return "different_payload"
        store_event(self.registry, self._event(entries, "verified", "strict indexed replay matches the exact registered original bytes",
                    approved_object_ids=object_ids,
                    capture=capture, capture_original_url=original,
                    verified_at=datetime.now(timezone.utc).isoformat(),
                    verification={"strict_index": True, "raw_sha256": actual["sha256"], "raw_bytes": actual["size"]}))
        return "verified"

    def finish(self, deadline):
        """Record real accepted jobs even while paused; verify only when healthy."""
        checked = 0
        cursor_path = self.registry / "owner-finish-cursor.json"
        cursor = json.loads(cursor_path.read_text(encoding="utf-8")).get("after", "") if cursor_path.exists() else ""
        groups = self._groups()
        for wrap in (False, True):
            for job, group in groups.items():
                if checked >= self.limit or time.monotonic() >= deadline:
                    return checked
                if (job <= cursor) != wrap:
                    continue
                entry = group["entry"]
                request = entry["request"]
                event = load_event(self.registry, request["source"])
                if event and event["state"] == "verified":
                    continue
                legacy = self.control.done.get(request["source"]["url"])
                if legacy:
                    outcome = self._observe([entry], legacy, deadline, group["objects"])
                    if outcome == "different_payload" and self._epoch_applied(request["source"], legacy):
                        store_event(self.registry, self._event([entry], "needs_attention",
                            "applied version epoch returned different raw capture bytes",
                            approved_object_ids=group["objects"], superseded_worker_receipt=legacy,
                            accepted_job_id=legacy.get("job_id"),
                            continuation="review the provider result without resetting accepted jobs or retry budgets"))
                    elif outcome == "different_payload":
                        store_event(self.registry, self._event([entry], "capture_check_pending",
                            "queued URL resolved to another payload; next prepare establishes a checked version epoch",
                            approved_object_ids=group["objects"], superseded_worker_receipt=legacy))
                    checked += 1
                    atomic_json(cursor_path, {"after": job})
        return checked
