"""Bounded original-byte spool outside Git for resumable version backups."""
from __future__ import annotations

import hashlib
import json
import os
import shutil
import sys
import time
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from preservation_backups import Artifact, file_artifact, payload_hashes, _immutable_write  # noqa: E402
from preservation_contracts import canonical_bytes, object_id, subject_errors, validate_backup_receipt  # noqa: E402
from preservation_registry import atomic_json  # noqa: E402

CHUNK_BYTES = 128 * 1024
DEFAULT_WORK = Path("/mnt/HC_Volume_107153504/work/swccg-preservation-backup")
MAX_FILE_BYTES = 64 * 1024 * 1024
MAX_SPOOL_BYTES = 256 * 1024 * 1024
DISK_RESERVE = 2 * 1024 * 1024 * 1024


class BackupDeferred(RuntimeError):
    """An item remains visible and resumable; it is not counted as backed up."""


class NoOriginalRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise BackupDeferred("original URL redirected; reconcile the exact public version URL")


def fetch_original(url: str, *, timeout=120):
    request = urllib.request.Request(url, headers={
        "User-Agent": "SWCCG-VersionBackup/1.0", "Accept-Encoding": "identity"})
    return urllib.request.build_opener(NoOriginalRedirect()).open(request, timeout=timeout)


def candidate_id(title: str, info: dict) -> str:
    identity = {"title": title, **{key: info.get(key) for key in ("timestamp", "url", "sha1", "size")}}
    return hashlib.sha256(canonical_bytes(identity)).hexdigest()


class Spool:
    def __init__(self, directory: Path, *, fetch=fetch_original, max_file_bytes=MAX_FILE_BYTES,
                 max_spool_bytes=MAX_SPOOL_BYTES, disk_reserve=DISK_RESERVE):
        self.directory = Path(directory)
        self.fetch = fetch
        self.max_file_bytes = max_file_bytes
        self.max_spool_bytes = max_spool_bytes
        self.disk_reserve = disk_reserve
        for name in ("objects", "versions", "inflight", "receipts", "issues"):
            (self.directory / name).mkdir(parents=True, exist_ok=True)

    def used_bytes(self) -> int:
        return sum(path.stat().st_size for name in ("objects", "inflight")
                   for path in (self.directory / name).iterdir() if path.is_file())

    def save_artifact(self, artifact: Artifact) -> Artifact:
        """Keep only a verified disk path, not each binary's bytes, in a batch."""
        key = object_id(artifact.subject)
        target = self.directory / "objects" / (artifact.subject["content_sha256"] + ".bin")
        if not target.exists():
            self._reserve(artifact.subject["bytes"])
        hashes = payload_hashes(artifact.payload)
        if hashes["sha256"] != artifact.subject["content_sha256"] or hashes["bytes"] != artifact.subject["bytes"]:
            raise ValueError("spool artifact differs from its exact subject")
        _immutable_write(self.directory, "objects/" + target.name, artifact.payload)
        result = Artifact(artifact.subject, target, artifact.provenance)
        atomic_json(self.directory / "versions" / (key + ".json"),
                    {"subject": result.subject, "provenance": result.provenance,
                     "payload": target.name}, create_only=True)
        return result

    def _reserve(self, size: int) -> None:
        if type(size) is not int or size < 0 or size > self.max_file_bytes:
            raise BackupDeferred("original exceeds the explicit per-file byte budget")
        if self.used_bytes() + size > self.max_spool_bytes:
            raise BackupDeferred("verified spool budget is full; commit/read back current items before continuing")
        if shutil.disk_usage(self.directory).free < size + self.disk_reserve:
            raise BackupDeferred("persistent work volume reserve reached")

    def file(self, title: str, info: dict, *, require_payload=False, deadline=None) -> Artifact:
        # Recheck current public eligibility before trusting even a previously
        # verified receipt. Suppression/replacement metadata may have changed.
        preliminary = {"kind": "wiki_file_version", "title": title,
                       "upload_timestamp": info.get("timestamp"),
                       "original_version_url": info.get("url"),
                       "content_sha256": "0" * 64, "bytes": info.get("size")}
        errors = subject_errors(preliminary)
        if errors or any(field in info for field in ("filehidden", "sha1hidden", "suppressed")):
            raise BackupDeferred("file version is not an eligible public original")
        key = candidate_id(title, info)
        saved = self.directory / "versions" / (key + ".json")
        if saved.exists():
            row = json.loads(saved.read_text(encoding="utf-8"))
            subject = row.get("subject", {})
            if subject_errors(subject) or any(subject.get(field) != value for field, value in preliminary.items()
                                              if field != "content_sha256"):
                raise ValueError("cached spool subject differs from the requested exact original")
            if row.get("payload") != subject["content_sha256"] + ".bin" or any(row.get("provenance", {}).get(field) != info.get(field) for field in ("timestamp", "url", "sha1", "size")):
                raise ValueError("cached spool path/hash metadata differs from the requested original")
            path = self.directory / "objects" / row["payload"]
            receipt = self.receipt(row["subject"])
            if receipt is not None:
                if not require_payload and not validate_backup_receipt(receipt, row["subject"]):
                    return Artifact(row["subject"], path, row["provenance"])
            if path.is_file():
                return file_artifact(title, info, path)
        partial = self.directory / "inflight" / (key + ".part")
        # The backup owner exclusively owns this spool; only its known partial
        # candidate is replaced on resume. Never remove another worker's files.
        partial.unlink(missing_ok=True)
        self._reserve(info.get("size"))
        def remaining():
            seconds = 120 if deadline is None else deadline - time.monotonic()
            if seconds <= 0:
                raise BackupDeferred("absolute backup deadline reached; exact version remains pending")
            return min(120, seconds)
        try:
            size = 0
            timeout = remaining()
            response = fetch_original(info["url"], timeout=timeout) if self.fetch is fetch_original else self.fetch(info["url"])
            with response, partial.open("wb") as output:
                encoding = getattr(response, "headers", {}).get("Content-Encoding", "identity")
                if encoding not in ("identity", ""):
                    raise BackupDeferred("unexpected transfer encoding; original byte identity needs reconciliation")
                while True:
                    remaining()
                    reader = getattr(response, "read1", response.read)
                    chunk = reader(min(CHUNK_BYTES, info["size"] - size + 1))
                    remaining()
                    if not chunk:
                        break
                    size += len(chunk)
                    if size > info["size"]:
                        raise ValueError("source exceeded its inventoried original size")
                    output.write(chunk)
                output.flush()
                os.fsync(output.fileno())
            artifact = file_artifact(title, info, partial)
            target = self.directory / "objects" / (artifact.subject["content_sha256"] + ".bin")
            if target.exists():
                if payload_hashes(target)["sha256"] != artifact.subject["content_sha256"]:
                    raise ValueError("existing verified spool payload is corrupt")
            else:
                os.link(partial, target)
            result = Artifact(artifact.subject, target, artifact.provenance)
            atomic_json(saved, {"subject": result.subject, "provenance": result.provenance,
                                "payload": target.name}, create_only=True)
            return result
        finally:
            partial.unlink(missing_ok=True)

    def receipt(self, subject: dict) -> dict | None:
        path = self.directory / "receipts" / (object_id(subject) + ".json")
        return json.loads(path.read_text(encoding="utf-8")) if path.exists() else None

    def record_receipt(self, receipt: dict) -> None:
        from preservation_contracts import validate_backup_receipt
        errors = validate_backup_receipt(receipt, receipt["subject"])
        if errors:
            raise ValueError("; ".join(errors))
        atomic_json(self.directory / "receipts" / (object_id(receipt["subject"]) + ".json"), receipt)

    def record_issue(self, key: str, reason: str) -> None:
        if not key or any(character not in "0123456789abcdef" for character in key):
            raise ValueError("issue key must be a safe content identity")
        atomic_json(self.directory / "issues" / (key + ".json"),
                    {"state": "needs_reconciliation", "reason": reason,
                     "owner": "existing nightly backup", "continuation": "retry the exact recorded version; do not advance completion checkpoint"})

    def release(self, artifact: Artifact) -> None:
        """Release payload only after this version's independent receipt exists.

        Other metadata mappings remain durable; their remote receipt can be
        revalidated without retaining a second local copy of the payload.
        """
        from preservation_contracts import validate_backup_receipt
        receipt = self.receipt(artifact.subject)
        if receipt is None or validate_backup_receipt(receipt, artifact.subject):
            raise ValueError("cannot release an unverified backup payload")
        target = self.directory / "objects" / (artifact.subject["content_sha256"] + ".bin")
        if artifact.payload != target:
            raise ValueError("refusing to release a payload outside the owned spool")
        target.unlink(missing_ok=True)
        (self.directory / "issues" / (object_id(artifact.subject) + ".json")).unlink(missing_ok=True)
