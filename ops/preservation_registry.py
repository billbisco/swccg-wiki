"""Durable registration inbox; only the existing server owner promotes URLs.

There is deliberately no Archive.org submission client in this module. Clients
send immutable requests to the server inbox. Promotion is an integration function
for the existing owner's locked run, not a second worker or a PC-local lock.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import ipaddress
import json
import os
import sys
import tempfile
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from preservation_contracts import (  # noqa: E402
    canonical_bytes, is_nonnegative_int, is_sha256, object_id,
    registration_job_id, registration_object_id, subject_errors,
    validate_backup_receipt, validate_source_backup_receipt,
)

MAX_REQUEST_BYTES = 1024 * 1024
SERVER_OWNER = "server-wayback-owner"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def public_url(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = urllib.parse.urlsplit(value)
        host = parsed.hostname or ""
        if host == "localhost" or host.endswith((".localhost", ".local", ".internal")):
            return False
        try:
            if not ipaddress.ip_address(host).is_global:
                return False
        except ValueError:
            pass
        return parsed.scheme in {"http", "https"} and bool(host) and not parsed.username and not parsed.password and not parsed.fragment
    except ValueError:
        return False


def validate_request(request: object) -> list[str]:
    if not isinstance(request, dict):
        return ["registration request must be an object"]
    errors = subject_errors(request.get("subject"))
    if request.get("schema_version") != 1 or type(request.get("schema_version")) is not int:
        errors.append("registration schema_version must be 1")
    source = request.get("source")
    subject = request.get("subject") if isinstance(request.get("subject"), dict) else {}
    if not isinstance(source, dict):
        errors.append("source is required")
    else:
        if not public_url(source.get("url")):
            errors.append("source.url must be an exact public source URL without credentials")
        if not is_sha256(source.get("sha256")):
            errors.append("source SHA-256 must identify its exact payload")
        if not is_nonnegative_int(source.get("bytes")):
            errors.append("source byte count must identify its exact payload")
    readiness = request.get("readiness")
    if not isinstance(readiness, dict) or type(readiness.get("ready")) is not bool:
        errors.append("explicit readiness.ready boolean is required")
    elif not isinstance(readiness.get("reason"), str) or not readiness["reason"].strip():
        errors.append("readiness.reason is required")
    elif not is_nonnegative_int(readiness.get("stage_bytes")):
        errors.append("readiness.stage_bytes must be a nonnegative integer")
    if not isinstance(request.get("owner"), str) or not request["owner"].strip():
        errors.append("a continuation owner is required")
    if not isinstance(request.get("continuation"), str) or not request["continuation"].strip():
        errors.append("an exact continuation is required")
    if not isinstance(request.get("approval_scope"), dict) or not request["approval_scope"]:
        errors.append("approval_scope is required")
    if not is_nonnegative_int(request.get("generation", 0)):
        errors.append("generation must be a nonnegative integer")
    return errors


@contextlib.contextmanager
def registration_lock(registry: Path):
    """Serialize metadata updates only; this is not the archive submission lock."""
    registry.mkdir(parents=True, exist_ok=True)
    with (registry / ".registration.lock").open("a+b") as stream:
        if stream.tell() == 0:
            stream.write(b"0")
            stream.flush()
        stream.seek(0)
        if os.name == "nt":
            import msvcrt
            msvcrt.locking(stream.fileno(), msvcrt.LK_LOCK, 1)
        else:
            import fcntl
            fcntl.flock(stream, fcntl.LOCK_EX)
        try:
            yield
        finally:
            stream.seek(0)
            if os.name == "nt":
                msvcrt.locking(stream.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                fcntl.flock(stream, fcntl.LOCK_UN)


def atomic_json(path: Path, value: dict, *, create_only: bool = False) -> bool:
    """Fsync, then publish atomically. Immutable inbox writes never clobber peers."""
    path.parent.mkdir(parents=True, exist_ok=True)
    data = canonical_bytes(value) + b"\n"
    fd, temporary = tempfile.mkstemp(prefix=".register-", dir=path.parent)
    temp = Path(temporary)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        if create_only:
            try:
                os.link(temp, path)
            except FileExistsError:
                if json.loads(path.read_text(encoding="utf-8")) != value:
                    raise ValueError("conflicting immutable registry record: " + path.name)
                return False
        else:
            os.replace(temp, path)
        if os.name != "nt":
            directory = os.open(path.parent, os.O_RDONLY | os.O_DIRECTORY)
            try:
                os.fsync(directory)
            finally:
                os.close(directory)
        return True
    finally:
        temp.unlink(missing_ok=True)


def register(registry: Path, request: dict) -> dict:
    errors = validate_request(request)
    if errors:
        raise ValueError("; ".join(errors))
    request = dict(request, generation=request.get("generation", 0))
    if len(canonical_bytes(request)) > MAX_REQUEST_BYTES:
        raise ValueError("registration exceeds 1 MiB metadata cap")
    object_key = registration_object_id(request["subject"], request["source"])
    job_key = registration_job_id(request["source"])
    # A changed readiness/evidence record is another immutable observation. It
    # does not erase prior observations or merge away filename/version mappings.
    request_key = hashlib.sha256(canonical_bytes(request)).hexdigest()
    relative = Path("requests", job_key.split(":", 1)[1], object_key, request_key + ".json")
    with registration_lock(registry):
        prior = [json.loads(path.read_text(encoding="utf-8"))
                 for path in (registry / relative.parent).glob("*.json")]
        latest_generation = max((r.get("generation", 0) for r in prior), default=-1)
        if not (registry / relative).exists() and request["generation"] <= latest_generation:
            raise ValueError("changed observations need a strictly increasing generation")
        created = atomic_json(registry / relative, request, create_only=True)
    state = "superseded" if request["generation"] < latest_generation else object_state(request)
    return {"schema_version": 1, "job_id": job_key, "object_id": object_key,
            "subject_id": object_id(request["subject"]),
            "request_id": request_key, "record": relative.as_posix(),
            "record_sha256": hashlib.sha256(canonical_bytes(request) + b"\n").hexdigest(),
            "state": state, "reason": state_reason(request)[1],
            "submitted": False, "created": created}


def object_state(request: dict) -> str:
    return state_reason(request)[0]


def state_reason(request: dict) -> tuple[str, str]:
    errors = validate_backup_receipt(request.get("backup_receipt"), request["subject"])
    if errors:
        return "awaiting_backup", "Independent subject backup: " + "; ".join(errors)
    errors = validate_source_backup_receipt(source_receipt(request), request["source"], request["subject"])
    if errors:
        return "awaiting_backup", "Independent source backup: " + "; ".join(errors)
    if not request["readiness"]["ready"]:
        return "awaiting_stage", request["readiness"]["reason"]
    evidence = request["source"].get("checked_evidence")
    if not isinstance(evidence, dict) or not evidence.get("path") or not is_sha256(evidence.get("sha256")):
        return "needs_attention", "Checked source evidence is absent or malformed"
    return "ready", request["readiness"]["reason"]


def source_receipt(request: dict) -> dict | None:
    return request.get("source_backup_receipt") or request.get("backup_receipt")


def records(registry: Path) -> list[dict]:
    latest = {}
    for path in sorted((registry / "requests").glob("*/*/*.json")):
        request = json.loads(path.read_text(encoding="utf-8"))
        errors = validate_request(request)
        if errors:
            raise ValueError(path.name + ": " + "; ".join(errors))
        key = registration_object_id(request["subject"], request["source"])
        request_key = hashlib.sha256(canonical_bytes(request)).hexdigest()
        if path.stem != request_key or path.parent.name != key or path.parent.parent.name != request["source"]["sha256"]:
            raise ValueError("registry record content does not match its immutable identity")
        entry = {"path": path.relative_to(registry).as_posix(),
                 "request_id": path.stem, "request": request}
        if key not in latest or request.get("generation", 0) > latest[key]["request"].get("generation", 0):
            latest[key] = entry
        elif request.get("generation", 0) == latest[key]["request"].get("generation", 0):
            raise ValueError("conflicting observations share a generation")
    return sorted(latest.values(), key=lambda row: row["path"])


def export_records(registry: Path) -> dict:
    """A caller may Git-pin this bounded metadata export; private staging stays private."""
    rows = []
    for entry in records(registry):
        request = entry["request"]
        row = {key: request[key] for key in (
            "subject", "source", "readiness", "owner", "continuation", "approval_scope")}
        # Only whitelisted public fields enter the shared evidence export.
        row["source"] = {key: request["source"][key] for key in (
            "url", "sha256", "bytes", "checked_evidence") if key in request["source"]}
        row["readiness"] = {key: request["readiness"][key] for key in ("ready", "reason", "stage_bytes")}
        row.update(object_id=registration_object_id(request["subject"], request["source"]),
                   subject_id=object_id(request["subject"]),
                   job_id=registration_job_id(request["source"]), request_id=entry["request_id"],
                   generation=request.get("generation", 0),
                   record_sha256=hashlib.sha256((registry / entry["path"]).read_bytes()).hexdigest(),
                   record=entry["path"], state=object_state(request),
                   reason=state_reason(request)[1], submitted=False,
                   backup_receipt=request.get("backup_receipt"),
                   source_backup_receipt=source_receipt(request))
        promotion_path = registry / "promotions" / (row["job_id"].split(":", 1)[1] + ".json")
        if promotion_path.exists():
            promotion = json.loads(promotion_path.read_text(encoding="utf-8"))
            row["payload_job_state"] = promotion["state"]
            if promotion["request_id"] == row["request_id"] and row["state"] == "ready":
                row["state"] = "queued"
                row["queue_receipt"] = promotion["queue_receipt"]
        rows.append(row)
    return {"schema_version": 1, "objects": rows, "submission_owner": SERVER_OWNER}


def promote_ready(
    registry: Path, *, queued_urls: set[str], stage_budget_bytes: int,
    limit: int, owner: str, check_public: Callable[[dict], bool],
    enqueue: Callable[[str, str], dict], check_approval: Callable[[dict], bool],
) -> list[dict]:
    """Call only inside the existing server owner's global run lock.

    The owner supplies its ordered queue append, exact pinned approval-scope
    check, and fresh public-byte check. A client readiness flag is not approval.
    This function neither uploads stages nor calls an archive service. Registering
    private snapshots early cannot expose nonexistent URLs to the URL worker.
    """
    if owner != SERVER_OWNER:
        raise ValueError("promotion belongs to the existing server submission owner")
    if not is_nonnegative_int(stage_budget_bytes) or type(limit) is not int or limit < 1:
        raise ValueError("bounded promotion budget and positive limit are required")
    promoted, jobs = [], set()
    used = 0
    for entry in records(registry):
        request = entry["request"]
        if object_state(request) != "ready":
            continue
        if not check_approval(request):
            continue
        job = registration_job_id(request["source"])
        url = request["source"]["url"]
        if job in jobs:
            continue
        cost = request["readiness"]["stage_bytes"]
        if url not in queued_urls and used + cost > stage_budget_bytes:
            continue
        if not check_public(request):
            continue
        # Existing URL entries are reused after crash/restart. The owner callback
        # must append idempotently and retain the queue's current order.
        receipt = enqueue(url, job)
        if not isinstance(receipt, dict) or receipt.get("queued") is not True or receipt.get("url") != url or receipt.get("job_id") != job:
            raise RuntimeError("server owner did not confirm durable queue registration")
        atomic_json(registry / "promotions" / (job.split(":", 1)[1] + ".json"),
                    {"schema_version": 1, "job_id": job, "source_url": url,
                     "request_id": entry["request_id"], "queued_at": now(),
                     "owner": owner, "queue_receipt": receipt, "state": "queued"})
        if url not in queued_urls:
            used += cost
        queued_urls.add(url)
        jobs.add(job)
        promoted.append({"job_id": job, "source_url": url, "state": "queued"})
        if len(promoted) >= limit:
            break
    return promoted


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("register", "export"))
    parser.add_argument("--registry", type=Path, required=True,
                        help="existing server-local control/inbox directory, outside Git")
    args = parser.parse_args()
    if args.command == "register":
        raw = sys.stdin.buffer.read(MAX_REQUEST_BYTES + 1)
        if len(raw) > MAX_REQUEST_BYTES:
            raise ValueError("registration exceeds 1 MiB metadata cap")
        result = register(args.registry, json.loads(raw))
    else:
        result = export_records(args.registry)
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
