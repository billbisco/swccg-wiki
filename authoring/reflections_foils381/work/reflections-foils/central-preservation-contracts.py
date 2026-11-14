"""Exact-version backup contracts shared by publishers and reconciliation.

Validation checks a recorded receipt, not the existence of its remote payload.
Only the backup/readback producer may create a verified receipt.
"""
from __future__ import annotations

import hashlib
import json
import re
import urllib.parse
from datetime import datetime
from pathlib import PurePosixPath

SCHEMA_VERSION = 1
BACKUP_REPOSITORIES = frozenset({
    "https://github.com/billbisco/swccg-wiki",
    "https://github.com/billbisco/swccg-wiki-files",
})
SUBJECT_KINDS = frozenset({"wiki_revision", "wiki_draft", "wiki_file_version", "source_snapshot"})


def canonical_bytes(value: dict) -> bytes:
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False).encode("utf-8")


def is_sha256(value: object) -> bool:
    return isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None


def is_nonnegative_int(value: object) -> bool:
    return type(value) is int and value >= 0


def is_utc_timestamp(value: object) -> bool:
    if not isinstance(value, str):
        return False
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
        return parsed.utcoffset() is not None and parsed.utcoffset().total_seconds() == 0
    except ValueError:
        return False


def subject_errors(subject: object) -> list[str]:
    if not isinstance(subject, dict):
        return ["subject must be an object"]
    errors = []
    kind = subject.get("kind")
    if kind not in SUBJECT_KINDS:
        errors.append("subject.kind is unsupported")
    if not isinstance(subject.get("title"), str) or not subject["title"].strip():
        errors.append("subject.title is required")
    if not is_sha256(subject.get("content_sha256")):
        errors.append("subject.content_sha256 must be a lowercase SHA-256")
    if not is_nonnegative_int(subject.get("bytes")):
        errors.append("subject.bytes must be a nonnegative integer")
    if kind == "wiki_revision" and not (
        type(subject.get("revision_id")) is int and subject["revision_id"] > 0
    ):
        errors.append("subject.revision_id must identify an exact revision")
    if kind == "wiki_file_version":
        if subject.get("bytes") == 0:
            errors.append("a public file version cannot have an empty payload")
        if not is_utc_timestamp(subject.get("upload_timestamp")):
            errors.append("subject.upload_timestamp must identify an exact UTC version")
        original = subject.get("original_version_url")
        try:
            url = urllib.parse.urlsplit(original) if isinstance(original, str) else None
            valid_original = url and url.scheme == "https" and url.hostname == "wiki.swccg.com" and not url.username and not url.password and url.path.startswith("/images/") and "/thumb/" not in url.path and not url.fragment
        except ValueError:
            valid_original = False
        if not valid_original:
            errors.append("subject.original_version_url must identify the public full-size Wiki original version")
    return errors


def object_id(subject: dict) -> str:
    errors = subject_errors(subject)
    if errors:
        raise ValueError("; ".join(errors))
    # A filename/version is retained even when its bytes share a payload job.
    return hashlib.sha256(canonical_bytes(subject)).hexdigest()


def payload_job_id(subject: dict) -> str:
    object_id(subject)
    return "payload:" + subject["content_sha256"]


def registration_job_id(source: dict) -> str:
    """A source payload may serve many distinct publication/version mappings."""
    if not isinstance(source, dict) or not is_sha256(source.get("sha256")):
        raise ValueError("source payload needs an exact SHA-256")
    return "payload:" + source["sha256"]


def registration_object_id(subject: dict, source: dict) -> str:
    subject_key = object_id(subject)
    registration_job_id(source)
    if not isinstance(source.get("url"), str) or not source["url"]:
        raise ValueError("source URL is required for a version/source mapping")
    return hashlib.sha256(canonical_bytes({"subject_id": subject_key,
                                         "source_url": source["url"],
                                         "source_sha256": source["sha256"]})).hexdigest()


def validate_registration_identity(record: dict) -> list[str]:
    try:
        expected_object = registration_object_id(record["subject"], record["source"])
        expected_job = registration_job_id(record["source"])
        expected_subject = object_id(record["subject"])
    except (KeyError, TypeError, ValueError) as error:
        return ["registration identity is invalid: " + str(error)]
    errors = []
    if record.get("object_id") != expected_object:
        errors.append("registration object_id does not bind the exact subject and source")
    if record.get("job_id") != expected_job:
        errors.append("registration job_id does not bind the exact source payload")
    if record.get("subject_id") != expected_subject:
        errors.append("registration subject_id does not bind the exact publication/version")
    return errors


def source_backup_subject(source: dict) -> dict:
    """Canonical separate source subject; callers need not guess its title/kind."""
    registration_job_id(source)
    if not isinstance(source.get("url"), str) or not source["url"]:
        raise ValueError("source URL is required")
    subject = {"kind": "source_snapshot", "title": source["url"],
               "original_version_url": source["url"],
               "content_sha256": source["sha256"], "bytes": source.get("bytes")}
    errors = subject_errors(subject)
    if errors:
        raise ValueError("; ".join(errors))
    return subject


def validate_source_representation(source: dict) -> list[str]:
    """Bind a cited primary page to an explicitly checked snapshot representation."""
    if not isinstance(source, dict):
        return ["source representation must be an object"]
    primary = source.get("primary_url", source.get("url"))
    representation = source.get("representation", "original")
    if representation == "original":
        return [] if primary == source.get("url") else ["different primary/capture URLs need a checked snapshot representation"]
    if representation != "checked_self_contained_snapshot":
        return ["source representation is unsupported"]
    errors = []
    proof = source.get("provenance_equivalence")
    if not isinstance(proof, dict):
        return ["snapshot provenance equivalence proof is required"]
    if proof.get("primary_url") != primary or proof.get("snapshot_url") != source.get("url"):
        errors.append("equivalence proof URLs do not bind this primary/snapshot pair")
    try:
        primary_parts = urllib.parse.urlsplit(primary)
        snapshot_parts = urllib.parse.urlsplit(source.get("url", ""))
        if primary_parts.scheme not in {"http", "https"} or not primary_parts.hostname or primary_parts.username or primary_parts.password:
            errors.append("primary source URL is invalid")
        if snapshot_parts.scheme != "https" or snapshot_parts.hostname != "swccg.com" or not snapshot_parts.path.startswith("/snapshots/") or snapshot_parts.username or snapshot_parts.password:
            errors.append("snapshot capture target is not the approved public snapshot location")
    except (TypeError, ValueError):
        errors.append("primary/snapshot URL is invalid")
    for field in ("primary_html_sha256", "snapshot_html_sha256", "primary_article_text_sha256", "snapshot_article_text_sha256", "evidence_sha256"):
        if not is_sha256(proof.get(field)):
            errors.append("equivalence proof needs " + field)
    if proof.get("snapshot_html_sha256") != source.get("sha256"):
        errors.append("snapshot hash differs from the actual capture-target payload")
    if proof.get("primary_article_text_sha256") != proof.get("snapshot_article_text_sha256"):
        errors.append("primary/snapshot article text does not match")
    if not isinstance(proof.get("evidence_path"), str) or not proof["evidence_path"].strip():
        errors.append("equivalence proof needs its durable evidence path")
    return errors


def validate_source_backup_receipt(receipt: object, source: dict, shared_subject: dict | None = None) -> list[str]:
    try:
        expected = source_backup_subject(source)
    except (TypeError, ValueError) as error:
        return [str(error)]
    errors = validate_backup_receipt(receipt, expected)
    if errors and isinstance(shared_subject, dict) and (
        shared_subject.get("content_sha256") == source.get("sha256")
        and shared_subject.get("bytes") == source.get("bytes")
    ):
        # Content dedup is permitted only for exactly equal payload hashes/sizes.
        # The registry still retains the distinct filename/version/URL mapping.
        return validate_backup_receipt(receipt, shared_subject)
    return errors


def validate_backup_receipt(receipt: object, subject: dict) -> list[str]:
    """Return explicit structural errors; do not perform network access."""
    errors = subject_errors(subject)
    if errors:
        return errors
    if not isinstance(receipt, dict):
        return errors + ["backup receipt must be an object"]
    if type(receipt.get("schema_version")) is not int or receipt["schema_version"] != SCHEMA_VERSION:
        errors.append("backup receipt schema_version must be 1")
    if receipt.get("subject") != subject:
        errors.append("backup receipt subject does not bind the exact object/version/hash")
    storage = receipt.get("storage")
    if not isinstance(storage, dict):
        errors.append("backup receipt storage is required")
    else:
        if storage.get("kind") != "git" or storage.get("repository") not in BACKUP_REPOSITORIES:
            errors.append("backup must identify an existing independent backup repository")
        if not isinstance(storage.get("commit"), str) or not re.fullmatch(r"[0-9a-f]{40}", storage["commit"]):
            errors.append("backup storage commit must be immutable")
        path = storage.get("path")
        if not isinstance(path, str) or not path or PurePosixPath(path).is_absolute() or ".." in PurePosixPath(path).parts or "\\" in path:
            errors.append("backup storage path must be a safe repository-relative path")
    verification = receipt.get("verification")
    if not isinstance(verification, dict):
        return errors + ["independent restore/readback verification is required"]
    if verification.get("status") != "verified":
        errors.append("backup is not verified by restore/readback")
    if verification.get("independent") is not True:
        errors.append("local scratch/staging is not an independent backup")
    if verification.get("restored_sha256") != subject.get("content_sha256"):
        errors.append("restored backup SHA-256 does not match the exact subject")
    if type(verification.get("restored_bytes")) is not int or verification["restored_bytes"] != subject.get("bytes"):
        errors.append("restored backup byte count does not match the exact subject")
    if not is_utc_timestamp(verification.get("verified_at")):
        errors.append("restore/readback verification needs a UTC timestamp")
    if isinstance(storage, dict) and storage.get("container") is not None:
        if storage["container"] != "tar.xz":
            errors.append("backup container type is unsupported")
        member = storage.get("member")
        if not isinstance(member, str) or not member or PurePosixPath(member).is_absolute() or ".." in PurePosixPath(member).parts or "\\" in member:
            errors.append("backup container member must be a safe relative path")
        if not is_sha256(storage.get("artifact_sha256")):
            errors.append("backup container needs its compressed artifact SHA-256")
        if not is_nonnegative_int(storage.get("artifact_bytes")) or storage.get("artifact_bytes") == 0:
            errors.append("backup container needs its compressed artifact byte count")
        if not is_nonnegative_int(storage.get("uncompressed_bytes")) or storage.get("uncompressed_bytes", -1) < subject["bytes"]:
            errors.append("backup container needs its complete member-payload byte tally")
        if verification.get("restored_container_sha256") != storage.get("artifact_sha256") or not is_sha256(verification.get("restored_container_sha256")):
            errors.append("independent container readback SHA-256 is absent or mismatched")
        if type(verification.get("restored_container_bytes")) is not int or verification["restored_container_bytes"] != storage.get("artifact_bytes"):
            errors.append("independent container readback byte count is absent or mismatched")
    return errors
