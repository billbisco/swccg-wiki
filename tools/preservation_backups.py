"""Immutable public-version artifacts and independent GitHub readback receipts."""
from __future__ import annotations

import hashlib
import io
import json
import os
import re
import contextlib
import tempfile
import tarfile
import urllib.parse
import urllib.request
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath

from preservation_contracts import (
    BACKUP_REPOSITORIES, canonical_bytes, object_id, subject_errors,
    validate_backup_receipt,
)

MAX_READBACK_BYTES = 128 * 1024 * 1024
MAX_CONTAINER_PAYLOAD_BYTES = 1024 * 1024 * 1024
HIDDEN_FIELDS = frozenset({"texthidden", "filehidden", "sha1hidden", "suppressed"})


class UnavailablePublicVersion(ValueError):
    """The requested version is not public or lacks its required identity."""


def _sha1_value(expected: str) -> int | None:
    try:
        return int(expected, 16) if re.fullmatch(r"[0-9a-fA-F]{40}", expected) else int(expected, 36)
    except (TypeError, ValueError):
        return None


@contextlib.contextmanager
def payload_reader(payload: bytes | Path):
    if isinstance(payload, Path):
        with payload.open("rb") as stream:
            yield stream
    else:
        with io.BytesIO(payload) as stream:
            yield stream


def payload_hashes(payload: bytes | Path) -> dict:
    sha1, sha256, size = hashlib.sha1(), hashlib.sha256(), 0
    with payload_reader(payload) as stream:
        while chunk := stream.read(128 * 1024):
            sha1.update(chunk)
            sha256.update(chunk)
            size += len(chunk)
    return {"sha1": sha1.hexdigest(), "sha256": sha256.hexdigest(), "bytes": size}


def _immutable_write(repository: Path, relative: str, payload: bytes | Path) -> None:
    target = repository / relative
    if not target.resolve().is_relative_to(repository.resolve()):
        raise ValueError("backup artifact escapes its repository")
    target.parent.mkdir(parents=True, exist_ok=True)
    if target.exists():
        if payload_hashes(target) != payload_hashes(payload):
            raise ValueError("immutable backup artifact has conflicting bytes")
        return
    fd, name = tempfile.mkstemp(prefix=".backup-", dir=target.parent)
    temporary = Path(name)
    try:
        with os.fdopen(fd, "wb") as stream:
            with payload_reader(payload) as source:
                while chunk := source.read(128 * 1024):
                    stream.write(chunk)
            stream.flush()
            os.fsync(stream.fileno())
        try:
            os.link(temporary, target)
        except FileExistsError:
            if payload_hashes(target) != payload_hashes(payload):
                raise ValueError("concurrent immutable backup has conflicting bytes")
    finally:
        temporary.unlink(missing_ok=True)


@dataclass(frozen=True)
class Artifact:
    subject: dict
    payload: bytes | Path
    provenance: dict

    @property
    def payload_path(self) -> str:
        sha = self.subject["content_sha256"]
        return "preservation/objects/" + sha[:2] + "/" + sha + ".bin"

    @property
    def metadata_path(self) -> str:
        return "preservation/versions/" + object_id(self.subject) + ".json"

    def metadata_bytes(self) -> bytes:
        return canonical_bytes({"schema_version": 1, "subject": self.subject,
                                "source": self.provenance, "payload_path": self.payload_path}) + b"\n"

    def write(self, repository: Path) -> list[str]:
        """Invoke inside the existing Git writer callback, never before its lock."""
        errors = subject_errors(self.subject)
        hashes = payload_hashes(self.payload)
        if errors or hashes["sha256"] != self.subject["content_sha256"] or hashes["bytes"] != self.subject["bytes"]:
            raise ValueError("artifact bytes/identity failed validation: " + "; ".join(errors))
        _immutable_write(repository, self.payload_path, self.payload)
        _immutable_write(repository, self.metadata_path, self.metadata_bytes())
        return [self.payload_path, self.metadata_path]


def revision_artifact(page: dict, revision: dict) -> Artifact:
    if HIDDEN_FIELDS.intersection(revision) or page.get("missing") or page.get("invalid"):
        raise UnavailablePublicVersion("revision is unavailable for public preservation")
    slot = revision.get("slots", {}).get("main", {})
    text = slot.get("content", revision.get("content"))
    if not isinstance(text, str):
        raise UnavailablePublicVersion("public revision text is absent")
    raw = text.encode("utf-8")
    if revision.get("sha1") and int(hashlib.sha1(raw).hexdigest(), 16) != _sha1_value(revision["sha1"]):
        raise ValueError("revision SHA-1 differs from the returned stored text")
    subject = dict(kind="wiki_revision", title=page.get("title"),
                   revision_id=revision.get("revid"), content_sha256=hashlib.sha256(raw).hexdigest(),
                   bytes=len(raw))
    errors = subject_errors(subject)
    if errors:
        raise UnavailablePublicVersion("; ".join(errors))
    provenance = {"api": "https://wiki.swccg.com/api.php", "page_id": page.get("pageid"),
                  "revision_id": revision["revid"], "parent_id": revision.get("parentid"),
                  "timestamp": revision.get("timestamp"), "wiki_sha1": revision.get("sha1"),
                  "content_model": slot.get("contentmodel", revision.get("contentmodel")),
                  "public": True}
    return Artifact(subject, raw, provenance)


def file_artifact(title: str, info: dict, raw: bytes | Path) -> Artifact:
    if HIDDEN_FIELDS.intersection(info):
        raise UnavailablePublicVersion("file version is unavailable for public preservation")
    hashes = payload_hashes(raw)
    if type(info.get("size")) is not int or info["size"] != hashes["bytes"]:
        raise ValueError("original file byte count differs from version metadata")
    if int(hashes["sha1"], 16) != _sha1_value(info.get("sha1")):
        raise ValueError("original file SHA-1 differs from version metadata")
    subject = dict(kind="wiki_file_version", title=title,
                   upload_timestamp=info.get("timestamp"), original_version_url=info.get("url"),
                   content_sha256=hashes["sha256"], bytes=hashes["bytes"])
    errors = subject_errors(subject)
    if errors:
        raise UnavailablePublicVersion("; ".join(errors))
    provenance = {key: info[key] for key in (
        "timestamp", "url", "sha1", "size", "mime", "width", "height", "archivename", "user"
    ) if key in info}
    provenance["public"] = True
    return Artifact(subject, raw, provenance)


def _backup_url(storage: dict, field: str = "path") -> str:
    repository = storage.get("repository")
    commit = storage.get("commit")
    relative = storage.get(field)
    if storage.get("kind") != "git" or repository not in BACKUP_REPOSITORIES:
        raise ValueError("an existing independent Git backup repository is required")
    if not isinstance(commit, str) or not re.fullmatch(r"[0-9a-f]{40}", commit):
        raise ValueError("backup commit must be immutable")
    if not isinstance(relative, str) or not relative or PurePosixPath(relative).is_absolute() or ".." in PurePosixPath(relative).parts or "\\" in relative:
        raise ValueError("backup path is not repository-relative")
    owner_repo = repository.removeprefix("https://github.com/")
    return "https://raw.githubusercontent.com/" + owner_repo + "/" + commit + "/" + urllib.parse.quote(relative, safe="/")


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise ValueError("independent backup URL redirected unexpectedly")


def _fetch(url: str):
    headers = {"User-Agent": "SWCCG-Preservation-Recovery/1.0", "Accept-Encoding": "identity"}
    if url.startswith("https://api.github.com/repos/"):
        # Contents metadata for 1–100 MB requires the object custom media type.
        headers["Accept"] = "application/vnd.github.object+json"
    request = urllib.request.Request(url, headers=headers)
    return urllib.request.build_opener(_NoRedirect()).open(request, timeout=60)


def _readback(url: str, expected_bytes: int, *, fetch, destination: Path | None = None,
              retain: bool = False) -> tuple[str, bytes | Path | None]:
    if type(expected_bytes) is not int or not 0 <= expected_bytes <= MAX_READBACK_BYTES:
        raise ValueError("independent readback exceeds its bounded byte budget")
    sha, total = hashlib.sha256(), 0
    retained = bytearray() if retain else None
    stream = None
    temporary = None
    try:
        if destination is not None:
            destination.parent.mkdir(parents=True, exist_ok=True)
            fd, name = tempfile.mkstemp(prefix=".restore-", dir=destination.parent)
            temporary = Path(name)
            stream = os.fdopen(fd, "wb")
        with fetch(url) as response:
            while True:
                chunk = response.read(min(128 * 1024, expected_bytes - total + 1))
                if not chunk:
                    break
                total += len(chunk)
                if total > expected_bytes:
                    raise ValueError("backup readback exceeds the exact expected byte count")
                sha.update(chunk)
                if stream:
                    stream.write(chunk)
                elif retained is not None:
                    retained.extend(chunk)
        if total != expected_bytes:
            raise ValueError("backup readback byte count differs from the original")
        if stream:
            stream.flush()
            os.fsync(stream.fileno())
            stream.close()
            stream = None
        return sha.hexdigest(), bytes(retained) if retained is not None else temporary
    except BaseException:
        if stream:
            stream.close()
        if temporary:
            temporary.unlink(missing_ok=True)
        raise


def independent_receipt(subject: dict, storage: dict, *, fetch=None, restore_to: Path | None = None,
                        chunk_max_total_bytes: int = MAX_READBACK_BYTES) -> dict:
    """Recover from the immutable independent repository, not the live Wiki.

    A receipt is returned only after exact remote payload verification. Optional
    metadata readback verifies the stored subject/provenance as well. A retained
    restore is published atomically only after its hash passes.
    """
    errors = subject_errors(subject)
    if errors:
        raise ValueError("; ".join(errors))
    if storage.get("kind") == "git_raw_chunks_v1":
        from preservation_chunks import independent_receipt as chunk_receipt
        return chunk_receipt(subject, storage, fetch=fetch or _fetch, restore_to=restore_to,
                             max_total_bytes=chunk_max_total_bytes)
    container_proof = {}
    if storage.get("container") is not None:
        sha, recovered, container_proof = _container_readback(subject, storage, fetch=fetch or _fetch, destination=restore_to)
    else:
        sha, recovered = _readback(_backup_url(storage), subject["bytes"], fetch=fetch or _fetch,
                                   destination=restore_to)
    temporary = recovered if isinstance(recovered, Path) else None
    try:
        if sha != subject["content_sha256"]:
            raise ValueError("independent restored payload SHA-256 differs from the original")
        verification = dict(status="verified", independent=True, restored_sha256=sha,
                            restored_bytes=subject["bytes"],
                            verified_at=datetime.now(timezone.utc).isoformat())
        verification.update(container_proof)
        if storage.get("metadata_path"):
            if type(storage.get("metadata_bytes")) is not int or storage["metadata_bytes"] > 1024 * 1024:
                raise ValueError("exact bounded metadata byte count is required")
            meta_sha, meta_raw = _readback(_backup_url(storage, "metadata_path"), storage["metadata_bytes"], fetch=fetch or _fetch, retain=True)
            metadata = json.loads(meta_raw)
            if metadata.get("subject") != subject:
                raise ValueError("restored metadata does not bind the exact original version")
            if storage.get("metadata_sha256") != meta_sha:
                raise ValueError("restored metadata SHA-256 differs from the stored artifact")
            verification.update(metadata_restored_sha256=meta_sha, metadata_matches_subject=True)
        receipt = dict(schema_version=1, subject=subject, storage=storage, verification=verification)
        errors = validate_backup_receipt(receipt, subject)
        if errors:
            raise ValueError("; ".join(errors))
        if temporary:
            os.replace(temporary, restore_to)
        return receipt
    finally:
        if temporary:
            temporary.unlink(missing_ok=True)


def _container_readback(subject: dict, storage: dict, *, fetch, destination: Path | None):
    if storage.get("container") != "tar.xz":
        raise ValueError("only the reviewed tar.xz backup representation is supported")
    member_name = storage.get("member")
    if not isinstance(member_name, str) or not member_name or PurePosixPath(member_name).is_absolute() or ".." in PurePosixPath(member_name).parts or "\\" in member_name:
        raise ValueError("backup container member path is unsafe")
    budget = storage.get("uncompressed_bytes")
    if type(budget) is not int or not subject["bytes"] <= budget <= MAX_CONTAINER_PAYLOAD_BYTES:
        raise ValueError("container payload tally exceeds the bounded restore budget")
    artifact_hash = storage.get("artifact_sha256")
    if not isinstance(artifact_hash, str) or not re.fullmatch(r"[0-9a-f]{64}", artifact_hash):
        raise ValueError("container artifact SHA-256 is required")
    sha, compressed = _readback(_backup_url(storage), storage.get("artifact_bytes"), fetch=fetch, retain=True)
    if sha != artifact_hash:
        raise ValueError("independent compressed container SHA-256 differs")
    with tarfile.open(fileobj=io.BytesIO(compressed), mode="r:xz") as archive:
        found, total, members = None, 0, 0
        for member in archive:
            members += 1
            if members > 10000:
                raise ValueError("backup container has too many members")
            name = PurePosixPath(member.name)
            if name.is_absolute() or ".." in name.parts or "\\" in member.name or not (member.isfile() or member.isdir()):
                raise ValueError("backup container contains an unsafe member")
            if member.isfile():
                total += member.size
                if total > budget:
                    raise ValueError("backup container exceeds its declared member-payload tally")
            if member.name == member_name:
                if found is not None or not member.isfile():
                    raise ValueError("backup member is ambiguous or not an ordinary file")
                found = member
        if total != budget:
            raise ValueError("backup container member-payload tally differs")
        if found is None or found.size != subject["bytes"]:
            raise ValueError("exact backup member is absent or has a different size")
        payload = archive.extractfile(found)
        payload_sha, recovered = _readback("checked-container-member", subject["bytes"],
                                          fetch=lambda unused: payload, destination=destination)
    proof = {"restored_container_sha256": sha, "restored_container_bytes": len(compressed),
             "container_member": member_name, "container_payload_tally": total}
    return payload_sha, recovered, proof
