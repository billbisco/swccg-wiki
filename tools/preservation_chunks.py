"""Explicit manual chunk staging and bounded independent immutable Git recovery.

No worker/configuration integration, upload, Git writes, registry or source fetch.
The default whole-source readback cap remains 128MiB. Larger manual recovery
requires an explicit byte limit; this is never an implicit worker budget waiver.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import tempfile
import urllib.parse
from datetime import datetime, timezone
from pathlib import Path

from preservation_chunk_profile import KIND, METHOD, PART_LIMIT, PART_COUNT_LIMIT, MANIFEST_LIMIT, manifest_errors, safe_path, storage_errors
from preservation_contracts import canonical_bytes, subject_errors, validate_backup_receipt

BUFFER = 128 * 1024
DEFAULT_TOTAL_LIMIT = 128 * 1024 * 1024
LFS_HEADER = b"version https://git-lfs.github.com/spec/v1"
METADATA_LIMIT = 2 * 1024 * 1024


def _subject(subject, budget):
    errors = subject_errors(subject)
    if errors:
        raise ValueError("; ".join(errors))
    if type(budget) is not int or not 0 < subject["bytes"] <= budget:
        raise ValueError("complete source exceeds the explicitly authorized total byte budget")


def stage(subject, source: Path, destination: Path, *, part_bytes=PART_LIMIT,
          max_total_bytes=DEFAULT_TOTAL_LIMIT, prefix=None):
    """Local parts/manifest only; no immutable locator or remote proof invented."""
    _subject(subject, max_total_bytes)
    if type(part_bytes) is not int or not 1 <= part_bytes <= PART_LIMIT:
        raise ValueError("part size must be 1..64MiB")
    if (subject["bytes"] + part_bytes - 1) // part_bytes > PART_COUNT_LIMIT:
        raise ValueError("source would require too many bounded chunk parts")
    source, destination = Path(source), Path(destination)
    if source.is_symlink() or not source.is_file():
        raise ValueError("source must be a regular file, not a symlink")
    prefix = prefix if prefix is not None else "preservation/chunks/" + subject["content_sha256"]
    if not safe_path(prefix):
        raise ValueError("chunk repository prefix must be safe")
    # An isolated new directory prevents stale parts from joining this source.
    destination.mkdir(parents=True, exist_ok=False)
    parts, offset, full = [], 0, hashlib.sha256()
    with source.open("rb") as stream:
        if stream.read(len(LFS_HEADER)).startswith(LFS_HEADER):
            raise ValueError("LFS pointer is not complete source bytes")
        stream.seek(0)
        while offset < subject["bytes"]:
            size = min(part_bytes, subject["bytes"] - offset)
            index, part_hash = len(parts), hashlib.sha256()
            path = f"{prefix}/parts/{index:05d}.bin"
            target = destination / path
            target.parent.mkdir(parents=True, exist_ok=True)
            remaining = size
            with target.open("xb") as output:
                while remaining:
                    chunk = stream.read(min(BUFFER, remaining))
                    if not chunk:
                        raise ValueError("source truncated during chunk staging")
                    if remaining == size and chunk.startswith(LFS_HEADER):
                        raise ValueError("LFS pointer is not complete source bytes")
                    output.write(chunk)
                    part_hash.update(chunk)
                    full.update(chunk)
                    remaining -= len(chunk)
            parts.append(dict(index=index, offset=offset, path=path, sha256=part_hash.hexdigest(), bytes=size))
            offset += size
        if stream.read(1) or full.hexdigest() != subject["content_sha256"]:
            raise ValueError("complete staged source differs from exact original hash/bytes")
    manifest = dict(schema_version=1, profile=KIND, subject=subject, parts=parts)
    raw = canonical_bytes(manifest) + b"\n"
    if len(raw) > MANIFEST_LIMIT:
        raise ValueError("chunk manifest exceeds bounded contract")
    manifest_path = prefix + "/manifest.json"
    (destination / manifest_path).write_bytes(raw)
    return {"status": "LOCAL_ONLY_NOT_BACKED_UP", "manifest_sha256": hashlib.sha256(raw).hexdigest(),
            "manifest_bytes": len(raw), "manifest_path": manifest_path, "manifest": manifest}


def _strict_json(raw):
    def object_pairs(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("duplicate JSON field in chunk/Git metadata")
            result[key] = value
        return result
    def constant(unused):
        raise ValueError("nonfinite JSON value in chunk/Git metadata")
    return json.loads(raw, object_pairs_hook=object_pairs, parse_constant=constant)


def _read_json(url, fetch):
    raw = bytearray()
    with fetch(url) as response:
        while data := response.read(min(BUFFER, METADATA_LIMIT - len(raw) + 1)):
            raw.extend(data)
            if len(raw) > METADATA_LIMIT:
                raise ValueError("Git metadata exceeds bounded JSON budget")
    return _strict_json(raw)


def _blob(storage, part, fetch, consume):
    """Immutable Contents metadata AND streamed raw bytes, including Git SHA-1."""
    repo = storage["repository"].removeprefix("https://github.com/")
    path, commit = part["path"], storage["commit"]
    encoded = urllib.parse.quote(path, safe="/")
    api = "https://api.github.com/repos/" + repo + "/contents/" + encoded + "?ref=" + commit
    raw_url = "https://raw.githubusercontent.com/" + repo + "/" + commit + "/" + encoded
    meta = _read_json(api, fetch)
    git_sha = meta.get("sha") if isinstance(meta, dict) else None
    if (not isinstance(meta, dict) or meta.get("type") != "file" or meta.get("path") != path
            or type(meta.get("size")) is not int or meta["size"] != part["bytes"]
            or not isinstance(git_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", git_sha)
            or meta.get("download_url") != raw_url
            or meta.get("git_url") != "https://api.github.com/repos/" + repo + "/git/blobs/" + git_sha):
        raise ValueError("immutable Git metadata does not bind exact repository/commit/path/blob/size")
    sha256, git, count, prefix = hashlib.sha256(), hashlib.sha1(), 0, bytearray()
    git.update(b"blob " + str(part["bytes"]).encode("ascii") + b"\0")
    with fetch(raw_url) as response:
        while data := response.read(min(BUFFER, part["bytes"] - count + 1)):
            count += len(data)
            if count > part["bytes"]:
                raise ValueError("immutable Git blob exceeds expected byte count")
            if len(prefix) < len(LFS_HEADER):
                prefix.extend(data[:len(LFS_HEADER) - len(prefix)])
            if bytes(prefix).startswith(LFS_HEADER):
                raise ValueError("Git LFS pointer is not source/part payload")
            sha256.update(data)
            git.update(data)
            consume(data)
    if count != part["bytes"] or sha256.hexdigest() != part["sha256"] or git.hexdigest() != git_sha:
        raise ValueError("independent Git blob hash/size differs from exact original")
    return {**part, "git_blob_sha1": git_sha, "repository": storage["repository"], "commit": commit}


def independent_receipt(subject, storage, *, fetch, restore_to=None, max_total_bytes=DEFAULT_TOTAL_LIMIT):
    """Fetch manifest+EVERY part at one commit; receipt only after full recovery."""
    _subject(subject, max_total_bytes)
    errors = storage_errors(storage, subject)
    if errors:
        raise ValueError("; ".join(errors))
    manifest_raw = bytearray()
    manifest_part = {"path": storage["path"], "sha256": storage["manifest_sha256"], "bytes": storage["manifest_bytes"]}
    manifest_proof = _blob(storage, manifest_part, fetch, manifest_raw.extend)
    manifest = _strict_json(manifest_raw)
    errors = manifest_errors(manifest, storage, subject)
    if errors:
        raise ValueError("; ".join(errors))
    # Never expose a partial destination after a failed chunk or manifest.
    temporary = None
    try:
        if restore_to is not None:
            restore_to = Path(restore_to)
            restore_to.parent.mkdir(parents=True, exist_ok=True)
            fd, name = tempfile.mkstemp(prefix=".chunks-", dir=restore_to.parent)
            temporary = Path(name)
            output = os.fdopen(fd, "wb")
        else:
            output = None
        full, count, proofs, prefix = hashlib.sha256(), 0, [], bytearray()
        def consume(data):
            nonlocal count
            count += len(data)
            if len(prefix) < len(LFS_HEADER):
                prefix.extend(data[:len(LFS_HEADER) - len(prefix)])
            if bytes(prefix).startswith(LFS_HEADER):
                raise ValueError("LFS pointer is not the reconstructed full source")
            full.update(data)
            if output:
                output.write(data)
        try:
            for part in storage["parts"]:
                proofs.append(_blob(storage, part, fetch, consume))
            if count != subject["bytes"] or full.hexdigest() != subject["content_sha256"]:
                raise ValueError("reconstructed COMPLETE source SHA-256/size differs")
            if output:
                output.flush()
                os.fsync(output.fileno())
        finally:
            if output:
                output.close()
        receipt = dict(schema_version=1, subject=subject, storage=storage, verification=dict(
            status="verified", independent=True, restored_sha256=full.hexdigest(), restored_bytes=count,
            verified_at=datetime.now(timezone.utc).isoformat(), method=METHOD,
            manifest_readback=manifest_proof, part_readbacks=proofs))
        errors = validate_backup_receipt(receipt, subject)
        if errors:
            raise ValueError("; ".join(errors))
        if temporary:
            os.replace(temporary, restore_to)
        return receipt
    finally:
        if temporary:
            temporary.unlink(missing_ok=True)


def main():
    import argparse
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--subject", required=True, type=Path)
    parser.add_argument("--max-total-bytes", type=int, default=DEFAULT_TOTAL_LIMIT)
    sub = parser.add_subparsers(dest="command", required=True)
    staged = sub.add_parser("stage")
    staged.add_argument("--source", required=True, type=Path)
    staged.add_argument("--out", required=True, type=Path)
    staged.add_argument("--part-bytes", type=int, default=PART_LIMIT)
    verified = sub.add_parser("verify")
    verified.add_argument("--storage", required=True, type=Path)
    verified.add_argument("--restore-to", required=True, type=Path)
    verified.add_argument("--receipt", required=True, type=Path)
    args = parser.parse_args()
    subject = _strict_json(args.subject.read_bytes())
    if args.command == "stage":
        result = stage(subject, args.source, args.out, part_bytes=args.part_bytes,
                       max_total_bytes=args.max_total_bytes)
        print(json.dumps(result, indent=2))
    else:
        if args.receipt.exists():
            raise ValueError("retain existing receipt; select a new output")
        from preservation_backups import _fetch
        result = independent_receipt(subject, _strict_json(args.storage.read_bytes()), fetch=_fetch,
                                     restore_to=args.restore_to, max_total_bytes=args.max_total_bytes)
        with args.receipt.open("x", encoding="utf-8") as output:
            output.write(json.dumps(result, indent=2) + "\n")
        print(json.dumps({"status": "INDEPENDENT_REMOTE_FULL_SOURCE_RESTORE_VERIFIED",
                          "bytes": subject["bytes"], "sha256": subject["content_sha256"]}))


if __name__ == "__main__":
    main()
