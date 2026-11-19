"""Stage-only maintenance using the existing preservation owner's real lock.

No queue, Save Page Now, credentials, schedule or provider-control mutation lives
here. An operator may inject a genuine authenticated independent-backup reader.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "tools"))
from preservation_backups import independent_receipt
from preservation_contracts import is_sha256
from preservation_owner import OwnerAdapter, load_allowed_objects
from wayback_control import Control


def stage_native_objects(repository: Path, object_ids: set[str], *, readback=independent_receipt,
                         seconds=600, maintenance_allowance=None):
    import wayback_worker as worker
    if (not object_ids or len(object_ids) > 50 or
            any(not is_sha256(key) for key in object_ids) or not 120 <= seconds <= 900):
        raise ValueError("stage-only maintenance needs a bounded explicit native cohort")
    directory = worker.control_directory(repository)
    approved = load_allowed_objects(directory / "registry")
    if not object_ids.issubset(approved):
        raise PermissionError("stage-only object cohort is not explicitly owner-approved")
    if worker.ACTIVE_CONTROL is not None:
        raise PermissionError("another owner is active in this process")
    with Control(directory, credential=None) as control:
        worker.ACTIVE_CONTROL = control
        try:
            adapter = OwnerAdapter(worker, repository, control, object_ids,
                                   readback=readback, limit=len(object_ids))
            if maintenance_allowance is None:
                return adapter.stage_native_only(time.monotonic() + seconds)
            return adapter.stage_native_only(time.monotonic() + seconds,
                                             maintenance_allowance=maintenance_allowance)
        finally:
            worker.ACTIVE_CONTROL = None


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--objects-file", type=Path, required=True)
    args = parser.parse_args()
    with args.objects_file.open("rb") as stream:
        raw = stream.read(65537)
    if len(raw) > 65536:
        raise ValueError("native staging cohort metadata exceeds its limit")
    document = json.loads(raw)
    print(json.dumps(stage_native_objects(Path(__file__).resolve().parents[1],
                                         set(document["object_ids"]))))


if __name__ == "__main__":
    main()
