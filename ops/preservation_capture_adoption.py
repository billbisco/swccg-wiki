"""Offline, explicitly approved adoption of an independently checked native capture.

The manifest hash is an operator approval boundary, not a signature from Archive.org.
No network client is used here. Both the observation and original bytes must already
have independent immutable backups and be supplied inside the approved bundle.
"""
from __future__ import annotations

import base64
import copy
import hashlib
import json
import re
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path, PureWindowsPath
from urllib.parse import parse_qs, urlsplit

from preservation_contracts import (object_id, registration_object_id,
                                    source_backup_subject, validate_backup_receipt,
                                    validate_registration_identity)
from preservation_registry import atomic_json, iter_records, object_state, source_receipt
from preservation_owner_receipts import load_event, store_object_event


HEX = re.compile(r"[0-9a-f]{64}")


def _require(condition, reason):
    if not condition:
        raise ValueError(reason)


def _local_file(root, entry, *, limit):
    name = entry.get("path")
    _require(isinstance(name, str) and name and "\\" not in name,
             "bundle file must have a relative POSIX path")
    relative = Path(name)
    _require(not relative.is_absolute() and not PureWindowsPath(name).drive and all(x not in {".", ".."} for x in name.split("/")),
             "bundle file escapes the approved directory")
    path = root / relative
    _require(all(not x.is_symlink() for x in [path, *path.parents]), "bundle symlinks are forbidden")
    size = entry.get("bytes")
    _require(type(size) is int and 0 < size <= limit and path.is_file() and path.stat().st_size == size,
             "bundle file size differs or exceeds its budget")
    with path.open("rb") as stream:
        data = stream.read(limit + 1)
    _require(len(data) == size, "bundle file changed during validation")
    _require(hashlib.sha256(data).hexdigest() == entry.get("sha256"), "bundle file hash differs")
    receipt = entry.get("backup_receipt", {})
    subject = receipt.get("subject", {})
    _require(subject.get("content_sha256") == entry["sha256"] and subject.get("bytes") == size,
             "backup receipt does not bind the exact supplied bytes")
    _require(not validate_backup_receipt(receipt, subject), "independent backup receipt is invalid")
    return data


def validate_bundle(path: Path, approved_sha256: str, registry: Path):
    """Validate the whole batch before any ledger, receipt or pointer is written."""
    _require(HEX.fullmatch(approved_sha256 or ""), "explicit approved manifest SHA256 required")
    _require(not path.is_symlink() and all(not x.is_symlink() for x in path.parents),
             "manifest symlinks are forbidden")
    _require(0 < path.stat().st_size <= 1024 * 1024, "manifest exceeds its metadata budget")
    with path.open("rb") as stream:
        raw = stream.read(1024 * 1024 + 1)
    _require(len(raw) <= 1024 * 1024, "manifest grew over its metadata budget")
    _require(hashlib.sha256(raw).hexdigest() == approved_sha256, "manifest approval hash differs")
    bundle = json.loads(raw)
    _require(type(bundle.get("schema_version")) is int and bundle["schema_version"] == 1 and bundle.get("kind") == "checked_native_capture_adoption",
             "unsupported adoption manifest")
    _require(type(bundle.get("approval_scope", {}).get("ticket")) is int,
             "adoption requires a traceable approval ticket")
    source = bundle["source"]
    _require(HEX.fullmatch(source.get("sha256", "")) and type(source.get("bytes")) is int,
             "source identity is malformed")
    source_url = urlsplit(source["url"])
    _require(source_url.scheme in {"http", "https"} and source_url.hostname and
             not source_url.username and not source_url.password and not source_url.fragment,
             "source URL must be an exact credential-free HTTP(S) URI")
    payload = _local_file(path.parent, bundle["payload"], limit=512 * 1024 * 1024)
    _require(bundle["payload"]["sha256"] == source["sha256"] and len(payload) == source["bytes"],
             "native bytes differ from the registered payload")
    _require(bundle["payload"]["backup_receipt"]["subject"] == source_backup_subject(source),
             "native backup subject differs from the exact source")
    proof = json.loads(_local_file(path.parent, bundle["proof"], limit=4 * 1024 * 1024))
    capture = bundle["capture"]
    stamp, original = capture["timestamp"], capture["capture_original_url"]
    _require(re.fullmatch(r"[0-9]{14}", stamp), "capture timestamp must be exact")
    date = datetime.strptime(stamp, "%Y%m%d%H%M%S").replace(tzinfo=timezone.utc)
    original_url = urlsplit(original)
    _require(original_url.scheme in {"http", "https"} and original_url.hostname and
             not original_url.username and not original_url.password and not original_url.fragment,
             "capture original must be an exact credential-free HTTP(S) URI")
    normal = "https://web.archive.org/web/" + stamp + "/" + original
    replay = "https://web.archive.org/web/" + stamp + "id_/" + original
    _require(capture["url"] == normal, "capture URL differs from its explicit timestamp/original")
    params = proof.get("cdx_parameters", {})
    _require(proof.get("target") == source["url"] and params.get("url") == source["url"] and
             params.get("filter") == "statuscode:200" and params.get("output") == "json" and
             params.get("collapse") == "digest" and params.get("limit") == "10" and
             params.get("fl") == "timestamp,original,mimetype,statuscode,digest,length",
             "CDX query is not bound to the exact registered source")
    query = urlsplit(proof.get("cdx_requested_url", ""))
    _require(query.scheme == "https" and query.netloc == "web.archive.org" and
             query.path == "/cdx/search/cdx" and
             parse_qs(query.query, keep_blank_values=True) == {k:[v] for k,v in params.items()},
             "observed CDX request URL differs from its declared query")
    row = proof.get("selected_candidate", {})
    _require(proof.get("cdx_status") == 200 and proof.get("capture_verified") is True and
             row in proof.get("rows", []) and row.get("timestamp") == stamp and
             row.get("original") == original and row.get("statuscode") == "200" and
             row.get("mimetype") == "application/pdf",
             "CDX selected record does not prove the exact successful native capture")
    sha1 = base64.b32encode(hashlib.sha1(payload).digest()).decode("ascii").rstrip("=")
    _require(row.get("digest") == sha1, "CDX digest differs from actual native payload")
    headers = {k.lower():v for k,v in proof.get("replay_headers", {}).items()}
    _require(proof.get("replay_url") == replay and proof.get("replay_status") == 200 and
             proof.get("redirects_followed") == 0 and proof.get("replay_sha256") == source["sha256"] and
             proof.get("replay_bytes") == len(payload) and payload.startswith(b"%PDF-") and
             headers.get("content-type", "").split(";", 1)[0].strip().lower() == "application/pdf",
             "raw replay is not an exact successful native PDF observation")
    _require(parsedate_to_datetime(headers.get("memento-datetime", "")) == date,
             "raw replay Memento date differs from the indexed timestamp")
    bindings = bundle.get("bindings")
    _require(isinstance(bindings, list) and 0 < len(bindings) <= 100,
             "adoption requires a bounded explicit object cohort")
    ids = [x.get("object_id") for x in bindings]
    _require(all(isinstance(x,str) and HEX.fullmatch(x) for x in ids) and len(set(ids)) == len(ids),
             "duplicate or malformed adoption object")
    entries = {registration_object_id(e["request"]["subject"], e["request"]["source"]):e
               for e in iter_records(registry, object_ids=set(ids))}
    for binding in bindings:
        entry = entries.get(binding["object_id"])
        _require(entry is not None, "exact registered object is missing")
        request = entry["request"]
        identity = {"object_id":binding["object_id"], "subject_id":binding["subject_id"],
                    "subject":request["subject"], "source":request["source"],
                    "job_id":"payload:" + source["sha256"]}
        _require(not validate_registration_identity(identity), "registration identity differs")
        _require(binding["request_id"] == entry["request_id"] and
                 binding["subject"] == request["subject"] and
                 binding["subject_id"] == object_id(request["subject"]) and
                 all(request["source"].get(k) == v for k,v in source.items()) and
                 object_state(request) == "ready",
                 "latest request/subject/source/readiness differs from approved binding")
        existing = load_event(registry, request["source"], object_id=binding["object_id"],
                              request_id=binding["request_id"], subject=request["subject"])
        object_pointer = registry / "owner-objects" / (binding["object_id"] + ".json")
        _require(not object_pointer.exists() or (existing and existing.get("adoption")),
                 "a prior object receipt belongs to a different request; reconcile before adoption")
        if existing and existing.get("adoption"):
            _require(existing["adoption"].get("manifest_sha256") == approved_sha256,
                     "a different object adoption must be reconciled first")
        actual = source_receipt(request)
        _require(actual["subject"] == bundle["payload"]["backup_receipt"]["subject"] and
                 actual["storage"] == bundle["payload"]["backup_receipt"]["storage"],
                 "native receipt does not match the independently backed registered source")
    return bundle


def adopt(worker, repository: Path, control, manifest: Path, approved_sha256: str):
    """Run under the real owner lock, without provider begin/recovery/reconcile."""
    _require(control.lock and not control.lock.closed, "existing owner lock is required")
    registry = control.directory / "registry"
    bundle = validate_bundle(manifest, approved_sha256, registry)
    _, done = worker.load(repository)
    baseline = copy.deepcopy(done)
    # Recover acknowledged updates unchanged; the normal writer's CAS protects
    # them from an intervening Git ledger update. No journal is discarded here.
    control.restore_updates(done)
    source, capture = bundle["source"], bundle["capture"]
    url = source["url"]
    current = done.get(url, {})
    _require(current.get("registered_payload_sha256") in {None, source["sha256"]} and
             current.get("registry_job_id") in {None, "payload:" + source["sha256"]},
             "existing ledger registration metadata differs from the approved payload")
    _require(not current.get("capture") or current["capture"] == capture["url"],
             "a different existing capture must be reconciled, not overwritten")
    _require(not current.get("job_id") or current.get("status") == "verified",
             "an acknowledged pending provider job must be reconciled first")
    marker = {"manifest_sha256":approved_sha256,
              "bindings":bundle["bindings"], "proof":bundle["proof"],
              "payload_backup_receipt":bundle["payload"]["backup_receipt"]}
    verification = {"method":"sha256", "sha256":source["sha256"], "bytes":source["bytes"],
                    "capture_id":"https://web.archive.org/web/" + capture["timestamp"] + "id_/" + capture["capture_original_url"],
                    "index":"cdx", "lane":"approved-native-adoption",
                    "adoption":{"manifest_sha256":approved_sha256,
                                "object_ids":[b["object_id"] for b in bundle["bindings"]],
                                "request_ids":[b["request_id"] for b in bundle["bindings"]]}}
    if current.get("status") == "verified":
        old_verify = current.get("verify", {})
        _require(old_verify.get("sha256") in {None, source["sha256"]} and
                 old_verify.get("bytes") in {None, source["bytes"]},
                 "existing verified payload differs from the approved source")
    entry = dict(current)
    entry.update(status="verified", capture=capture["url"], verify=verification,
                 registered_payload_sha256=source["sha256"], registry_job_id="payload:" + source["sha256"])
    entry.setdefault("tries", 0)
    # Stable verified metadata makes crash recovery/repeated execution idempotent.
    done[url] = entry
    control.checkpoint(done, baseline)
    changed = {u:e for u,e in done.items() if e != baseline.get(u)}
    worker.persist_changes(repository, done, changed, baseline)
    # Only publish object receipts after the actual owner ledger is durable. A
    # crash in between safely resumes from the same approved bundle and ledger.
    for binding in bundle["bindings"]:
        event = {"schema_version":1, "job_id":"payload:" + source["sha256"], "source_sha256":source["sha256"],
                 "source_bytes":source["bytes"], "approved_object_ids":[binding["object_id"]],
                 "binding":binding, "state":"verified", "reason":"Approved independently checked native capture adopted without provider requests",
                 "owner":"server-wayback-owner", "capture":capture["url"],
                 "capture_original_url":capture["capture_original_url"], "adoption":marker,
                 "verification":{"raw_sha256":source["sha256"], "raw_bytes":source["bytes"], "strict_index":True}}
        store_object_event(registry, binding["object_id"], event)
    control.ledger_saved()
    disposition = {"schema_version":1, "manifest_sha256":approved_sha256,
                   "status":"adopted", "source":source, "bindings":bundle["bindings"],
                   "capture":capture, "network_requests":0}
    atomic_json(control.directory / "capture-adoptions" / (approved_sha256 + ".json"), disposition,
                create_only=True)
    return disposition
