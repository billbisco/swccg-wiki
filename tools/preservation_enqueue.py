"""Send metadata to the one server registration inbox; never submit a capture."""
from __future__ import annotations

import argparse
import json
import shlex
import subprocess
import sys
from pathlib import Path, PurePosixPath

from preservation_contracts import canonical_bytes, object_id, registration_job_id, registration_object_id

REMOTE_PROGRAM = "/opt/swccg-ops/repos/swccg-wiki/ops/preservation_registry.py"
MAX_REQUEST_BYTES = 1024 * 1024


def deliver(request: dict, registry: str, *, run=subprocess.run) -> dict:
    """The host/program are fixed; only the approved server-local inbox varies."""
    path = PurePosixPath(registry)
    if not path.is_absolute() or ".." in path.parts or str(path).startswith("/opt/swccg-ops/repos/"):
        raise ValueError("registry must be an absolute server control path outside Git")
    expected_object = registration_object_id(request["subject"], request["source"])
    expected_job = registration_job_id(request["source"])
    raw = canonical_bytes(request)
    if len(raw) > MAX_REQUEST_BYTES:
        raise ValueError("registration exceeds 1 MiB metadata cap")
    command = " ".join(shlex.quote(part) for part in (
        "python3", REMOTE_PROGRAM, "register", "--registry", str(path)))
    result = run(["ssh", "-o", "BatchMode=yes", "-o", "ConnectTimeout=15", "gemp", command],
                 input=raw, capture_output=True, timeout=60)
    if result.returncode:
        # Do not print server output, source content or environment diagnostics.
        raise RuntimeError("server registration failed with exit " + str(result.returncode))
    receipt = json.loads(result.stdout)
    if receipt.get("object_id") != expected_object or receipt.get("job_id") != expected_job:
        raise ValueError("server receipt does not identify the submitted version")
    if receipt.get("subject_id") != object_id(request["subject"]):
        raise ValueError("server receipt does not identify the publication subject")
    if receipt.get("submitted") is not False:
        raise ValueError("registration must not claim an archive submission")
    return receipt


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("request", type=Path)
    parser.add_argument("--registry", required=True)
    args = parser.parse_args()
    if args.request.stat().st_size > MAX_REQUEST_BYTES:
        raise ValueError("registration exceeds 1 MiB metadata cap")
    receipt = deliver(json.loads(args.request.read_text(encoding="utf-8")), args.registry)
    print(json.dumps(receipt, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
