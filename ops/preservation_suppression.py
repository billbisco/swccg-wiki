"""Exact withdrawn-object/payload tombstones; no deletion or capture client."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from preservation_contracts import is_sha256, registration_object_id

MAX_METADATA = 1024 * 1024


def _read(path: Path):
    if not path.exists():
        return None
    raw = path.read_bytes()
    if len(raw) > MAX_METADATA:
        raise ValueError("suppression metadata exceeds its bound")
    return json.loads(raw)


def _payload(registry: Path, digest: str):
    if not is_sha256(digest):
        raise ValueError("suppression needs an exact payload SHA-256")
    record = _read(registry / "suppressed-payloads" / (digest + ".json"))
    if record is not None and (record.get("schema_version") != 1 or
                              record.get("payload_sha256") != digest or
                              record.get("owner") != "server-wayback-owner" or
                              not record.get("approval_scope") or not record.get("reason")):
        raise ValueError("invalid exact payload suppression")
    return record


def suppressed_source(registry: Path, source: dict):
    """Payload identity wins even if a future registration uses another URL."""
    return _payload(registry, source["sha256"])


def suppressed_url(registry: Path, url: str):
    """Check only this URL's bounded index, not a registry-wide scan."""
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
    index = _read(registry / "suppressed-urls" / (digest + ".json"))
    if index is None:
        return None
    if index.get("url") != url:
        raise ValueError("suppression URL index differs from its exact identity")
    record = _payload(registry, index.get("payload_sha256"))
    if record is None or url not in record.get("source_urls", []):
        raise ValueError("suppression URL index has no exact payload record")
    return record


def suppress_objects(registry: Path, object_ids: set[str], *, owner: str,
                     reason: str, approval_scope: dict):
    """Retain immutable registrations and cancel only explicitly withdrawn bytes.

    Registration serialization makes the seven payload/index writes durable.
    The running owner checks these records again immediately before submission;
    an already accepted external capture cannot be recalled by this operation.
    """
    from preservation_registry import (SERVER_OWNER, atomic_json, iter_records,
                                       now, registration_lock)
    if owner != SERVER_OWNER or not reason.strip() or not approval_scope:
        raise PermissionError("exact owner and explicit withdrawal approval required")
    if not object_ids or len(object_ids) > 5000 or any(not is_sha256(x) for x in object_ids):
        raise ValueError("suppression needs bounded exact object identities")
    with registration_lock(registry):
        rows = list(iter_records(registry, object_ids=object_ids))
        if {registration_object_id(x["request"]["subject"], x["request"]["source"])
                for x in rows} != object_ids:
            raise ValueError("suppression object set is incomplete")
        groups = {}
        for row in rows:
            q = row["request"]
            digest = q["source"]["sha256"]
            group = groups.setdefault(digest, {"objects": set(), "urls": set()})
            group["objects"].add(registration_object_id(q["subject"], q["source"]))
            group["urls"].add(q["source"]["url"])
        # Validate all existing records before writing any new ones.
        planned = []
        for digest, group in groups.items():
            prior = _payload(registry, digest)
            if prior:
                if (not group["objects"].issubset(prior["object_ids"]) or
                        not group["urls"].issubset(prior["source_urls"])):
                    raise ValueError("existing suppression needs an explicit extension")
                record = prior
            else:
                record = {"schema_version": 1, "payload_sha256": digest,
                          "object_ids": sorted(group["objects"]),
                          "source_urls": sorted(group["urls"]), "owner": owner,
                          "reason": reason, "approval_scope": approval_scope,
                          "cancelled_at": now(), "state": "cancelled"}
            for url in group["urls"]:
                old = suppressed_url(registry, url)
                if old and old["payload_sha256"] != digest:
                    raise ValueError("withdrawn URL is bound to another exact payload")
            planned.append(record)
        for record in planned:
            digest = record["payload_sha256"]
            atomic_json(registry / "suppressed-payloads" / (digest + ".json"),
                        record, create_only=True)
            for url in record["source_urls"]:
                key = hashlib.sha256(url.encode("utf-8")).hexdigest()
                atomic_json(registry / "suppressed-urls" / (key + ".json"),
                            {"url": url, "payload_sha256": digest}, create_only=True)
        return {"object_ids": sorted(object_ids), "payloads": planned,
                "existing_registrations_deleted": 0, "capture_submissions": 0}


def apply_suppression_export(row: dict, registry: Path):
    record = suppressed_source(registry, row["source"])
    if record:
        # Keep a genuine prior submitted/capture receipt if one exists.
        row.update(state="cancelled", payload_job_state="cancelled",
                   reason=record["reason"], suppression_receipt=record)
