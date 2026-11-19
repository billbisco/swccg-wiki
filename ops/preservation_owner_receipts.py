"""Actual owner lifecycle receipts, distinct from registration and queue intent."""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path

from preservation_contracts import (canonical_bytes, registration_job_id, registration_object_id,
                                    object_id as subject_identity, source_backup_subject)
from preservation_registry import atomic_json


def store_event(registry: Path, event: dict):
    digest = event["source_sha256"]
    if not re.fullmatch(r"[0-9a-f]{64}", digest) or event["job_id"] != "payload:" + digest:
        raise ValueError("owner event does not bind an exact payload job")
    data_hash = hashlib.sha256(canonical_bytes(event)).hexdigest()
    relative = "owner-events/" + digest + "/" + data_hash + ".json"
    atomic_json(registry / relative, event, create_only=True)
    atomic_json(registry / "owner-jobs" / (digest + ".json"),
                {"event": relative, "event_sha256": data_hash})
    return {"event": relative, "event_sha256": data_hash}


def store_object_event(registry: Path, object_id: str, event: dict):
    """Publish an exact-version receipt without replacing the shared payload job."""
    if (not re.fullmatch(r"[0-9a-f]{64}", object_id) or
            event.get("approved_object_ids") != [object_id] or
            event.get("binding", {}).get("object_id") != object_id):
        raise ValueError("object receipt lacks its exact binding")
    digest = event["source_sha256"]
    if not re.fullmatch(r"[0-9a-f]{64}", digest) or event["job_id"] != "payload:" + digest:
        raise ValueError("owner event does not bind an exact payload job")
    data_hash = hashlib.sha256(canonical_bytes(event)).hexdigest()
    relative = "owner-events/" + digest + "/" + data_hash + ".json"
    atomic_json(registry / relative, event, create_only=True)
    pointer = {"event":relative, "event_sha256":data_hash}
    path = registry / "owner-objects" / (object_id + ".json")
    if path.exists():
        prior = json.loads(path.read_text(encoding="utf-8"))
        if prior != pointer:
            raise ValueError("a different object adoption must be reconciled first")
    atomic_json(path, pointer)
    return pointer


def load_event(registry: Path, source: dict, *, object_id=None, request_id=None, subject=None):
    path = registry / "owner-jobs" / (source["sha256"] + ".json")
    object_path = registry / "owner-objects" / (object_id + ".json") if object_id else None
    scoped = bool(object_path and object_path.exists())
    if scoped:
        path = object_path
    if not path.exists():
        return None
    pointer = json.loads(path.read_text(encoding="utf-8"))
    expected = "owner-events/" + source["sha256"] + "/" + pointer["event_sha256"] + ".json"
    if pointer["event"] != expected:
        raise ValueError("owner receipt pointer escapes its exact payload identity")
    event = json.loads((registry / expected).read_text(encoding="utf-8"))
    if hashlib.sha256(canonical_bytes(event)).hexdigest() != pointer["event_sha256"]:
        raise ValueError("owner receipt event hash differs")
    if (event.get("job_id") != registration_job_id(source) or event.get("source_bytes") != source["bytes"] or
            event.get("source_sha256") != source["sha256"]):
        raise ValueError("owner event differs from registered source payload")
    if scoped:
        binding = event.get("binding", {})
        if (binding.get("object_id") != object_id or not isinstance(subject, dict) or
                binding.get("subject") != subject or binding.get("subject_id") != subject_identity(subject) or
                registration_object_id(subject, source) != object_id or
                event.get("adoption", {}).get("payload_backup_receipt", {}).get("subject") != source_backup_subject(source)):
            raise ValueError("object receipt pointer differs from exact object")
        if binding.get("request_id") != request_id:
            return None  # Later registrations do not inherit an older version's receipt.
    return event


def apply_export(row: dict, registry: Path):
    event = load_event(registry, row["source"], object_id=row["object_id"], request_id=row["request_id"], subject=row["subject"])
    if not event or row["object_id"] not in event.get("approved_object_ids", []):
        return
    row["owner_job_receipt"] = event
    row["payload_job_state"] = event["state"]
    row["reason"] = event["reason"]
    if row["state"] not in {"ready", "queued", "awaiting_stage"}:
        return
    if event["state"] == "queued":
        receipt = event.get("queue_receipt", {})
        if receipt.get("queued") is not True or receipt.get("job_id") != row["job_id"] or not receipt.get("url"):
            raise ValueError("queued owner event differs from the exact source URL/job")
        if receipt["url"] == row["source"]["url"]:
            row.update(state="queued", submitted=False, queue_receipt=receipt)
    elif event["state"] == "submitted" and event.get("accepted_job_id"):
        row.update(state="submitted", submitted=True)
    elif event["state"] == "verified":
        verification = event.get("verification", {})
        capture = event.get("capture", "")
        match = re.fullmatch(r"https://web\.archive\.org/web/\d{14}(?:id_)?/(https?://.+)", capture)
        if (not match or match[1] != event.get("capture_original_url") or
                verification.get("raw_sha256") != row["source"]["sha256"] or
                verification.get("raw_bytes") != row["source"]["bytes"] or
                verification.get("strict_index") is not True):
            raise ValueError("verified owner receipt lacks exact raw capture and original-URL proof")
        row.update(state="verified", submitted=bool(event.get("accepted_job_id")) if event.get("adoption") else True, capture=capture,
                   capture_original_url=event["capture_original_url"])
    elif event["state"] in {"needs_version_retry", "needs_attention"}:
        row.update(state="needs_attention", submitted=bool(event.get("accepted_job_id")))
