"""Strict, versioned complete-source Git chunk receipt contract (no I/O)."""
from __future__ import annotations

import re
from pathlib import PurePosixPath

from preservation_contracts import BACKUP_REPOSITORIES, canonical_bytes, is_sha256, subject_errors

KIND = "git_raw_chunks_v1"
PART_LIMIT = 64 * 1024 * 1024
MANIFEST_LIMIT = 4 * 1024 * 1024
PART_COUNT_LIMIT = 16384
METHOD = "immutable-git-metadata-and-streamed-parts-v1"


def safe_path(path):
    return (isinstance(path, str) and bool(path) and "\\" not in path
            and not PurePosixPath(path).is_absolute() and ":" not in path
            and all(ord(c) >= 32 and ord(c) != 127 for c in path)
            and all(p not in {"", ".", ".."} for p in path.split("/")))


def keys(value, expected):
    return isinstance(value, dict) and set(value) == set(expected)


def exact_subject(candidate, subject):
    # Python equality alone treats True as 1, including inside nested objects.
    try:
        return not subject_errors(candidate) and canonical_bytes(candidate) == canonical_bytes(subject)
    except (TypeError, ValueError):
        return False


def parts_errors(parts, subject, manifest_path):
    if not isinstance(parts, list) or not 1 <= len(parts) <= PART_COUNT_LIMIT:
        return ["chunk parts must be a bounded nonempty ordered list"]
    errors, paths, offset = [], {manifest_path} if isinstance(manifest_path, str) else set(), 0
    for index, part in enumerate(parts):
        if not keys(part, ("index", "offset", "path", "sha256", "bytes")):
            errors.append("chunk part has unknown or missing fields")
            continue
        if type(part["index"]) is not int or part["index"] != index:
            errors.append("chunk part index/order differs")
        if type(part["offset"]) is not int or part["offset"] != offset:
            errors.append("chunk parts contain a gap, overlap or wrong offset")
        if not safe_path(part["path"]) or part["path"] in paths:
            errors.append("chunk paths must be safe and unique, separate from manifest")
        if isinstance(part["path"], str):
            paths.add(part["path"])
        if not is_sha256(part["sha256"]):
            errors.append("chunk part SHA-256 is invalid")
        if type(part["bytes"]) is not int or not 1 <= part["bytes"] <= PART_LIMIT:
            errors.append("chunk part must contain 1..64MiB bytes")
        else:
            offset += part["bytes"]
    if offset != subject.get("bytes"):
        errors.append("chunk byte sum does not equal the COMPLETE original subject")
    return errors


def storage_errors(storage, subject):
    if not keys(storage, ("kind", "repository", "commit", "path", "manifest_sha256", "manifest_bytes", "parts")):
        return ["chunk storage has unknown or missing fields"]
    errors = []
    if storage["kind"] != KIND:
        errors.append("chunk storage profile is unsupported")
    if not isinstance(storage["repository"], str) or storage["repository"] not in BACKUP_REPOSITORIES:
        errors.append("chunk repository is not an approved independent backup repository")
    if not isinstance(storage["commit"], str) or not re.fullmatch(r"[0-9a-f]{40}", storage["commit"]):
        errors.append("chunk commit must be immutable")
    if not safe_path(storage["path"]):
        errors.append("chunk manifest path must be safe")
    if not is_sha256(storage["manifest_sha256"]):
        errors.append("chunk manifest SHA-256 is required")
    if type(storage["manifest_bytes"]) is not int or not 1 <= storage["manifest_bytes"] <= MANIFEST_LIMIT:
        errors.append("chunk manifest size exceeds its bounded contract")
    errors.extend(parts_errors(storage["parts"], subject, storage["path"]))
    return errors


def manifest_errors(manifest, storage, subject):
    if not keys(manifest, ("schema_version", "profile", "subject", "parts")):
        return ["chunk manifest has unknown or missing fields"]
    errors = []
    if type(manifest["schema_version"]) is not int or manifest["schema_version"] != 1 or manifest["profile"] != KIND:
        errors.append("chunk manifest version/profile is unsupported")
    if not exact_subject(manifest["subject"], subject):
        errors.append("chunk manifest does not bind the COMPLETE original subject")
    errors.extend(parts_errors(manifest["parts"], subject, storage["path"]))
    if manifest["parts"] != storage["parts"]:
        errors.append("chunk manifest parts do not match the pinned storage order/identity")
    return errors


def readback_errors(proof, expected, storage, *, part=False):
    fields = {"path", "sha256", "bytes", "git_blob_sha1", "repository", "commit"}
    if part:
        fields |= {"index", "offset"}
    if not keys(proof, fields):
        return ["chunk readback evidence has unknown or missing fields"]
    errors = []
    for name in ("path", "sha256", "bytes") + (("index", "offset") if part else ()):
        if proof[name] != expected[name] or (name in {"bytes", "index", "offset"} and type(proof[name]) is not int):
            errors.append("chunk readback does not bind " + name)
    if proof["repository"] != storage["repository"] or proof["commit"] != storage["commit"]:
        errors.append("chunk readback mixes repositories or commits")
    if not isinstance(proof["git_blob_sha1"], str) or not re.fullmatch(r"[0-9a-f]{40}", proof["git_blob_sha1"]):
        errors.append("chunk readback Git blob identity is absent")
    return errors


def receipt_errors(receipt, subject):
    """Common exact subject/full restore checks remain in preservation_contracts."""
    if not keys(receipt, ("schema_version", "subject", "storage", "verification")):
        return ["chunk receipt has unknown or missing fields"]
    storage = receipt["storage"]
    errors = storage_errors(storage, subject)
    if not exact_subject(receipt["subject"], subject):
        errors.append("chunk receipt does not bind the exact typed original subject")
    if errors:
        return errors
    proof = receipt["verification"]
    fields = ("status", "independent", "restored_sha256", "restored_bytes", "verified_at", "method", "manifest_readback", "part_readbacks")
    if not keys(proof, fields):
        return ["chunk verification has unknown or missing fields"]
    if proof["method"] != METHOD:
        errors.append("chunk evidence needs independent immutable Git metadata and every streamed part")
    expected = {"path": storage["path"], "sha256": storage["manifest_sha256"], "bytes": storage["manifest_bytes"]}
    errors.extend(readback_errors(proof["manifest_readback"], expected, storage))
    rows = proof["part_readbacks"]
    if not isinstance(rows, list) or len(rows) != len(storage["parts"]):
        return errors + ["every ordered chunk needs independent remote readback evidence"]
    for row, expected in zip(rows, storage["parts"]):
        errors.extend(readback_errors(row, expected, storage, part=True))
    return errors
