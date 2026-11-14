#!/usr/bin/env python3
"""Existing nightly entry point: bounded exact-version backup and reconciliation.

The existing timer/unit/credentials stay unchanged. --state remains a compatible
health summary, not an all-items-success checkpoint. Durable discovery cursors,
pending tasks and independent receipts live outside Git on the approved work
volume. Immutable version objects retain history; current flat mirrors and
indexes remain compatible and reject historical or concurrent peer overwrite.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from backup_spool import DEFAULT_WORK
from backup_versions import Producer, backup_owner
from preservation_registry import atomic_json
from source_inventory import SourceInventory

API = "https://wiki.swccg.com/api.php"
MAX_API_BYTES = 16 * 1024 * 1024
REGISTRY = Path(os.environ.get("WAYBACK_CONTROL_DIR", str(Path.home() / ".local/state/swccg-wayback"))) / "registry"


def api(params: dict) -> dict:
    query = {"format": "json", "formatversion": "2", **params}
    request = urllib.request.Request(API + "?" + urllib.parse.urlencode(query),
                                    headers={"User-Agent": "swccg-wiki-version-backup/2.0"})
    with urllib.request.urlopen(request, timeout=120) as response:
        raw = response.read(MAX_API_BYTES + 1)
    if len(raw) > MAX_API_BYTES:
        raise ValueError("Wiki API response exceeds bounded backup budget")
    result = json.loads(raw.decode("utf-8"))
    if result.get("error") or result.get("warnings"):
        raise ValueError("Wiki API rejected or warned about a version query")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("pages_repo", type=Path)
    parser.add_argument("files_repo", type=Path)
    parser.add_argument("--state", type=Path, default=Path("/var/lib/swccg-ops/backup-state.json"))
    parser.add_argument("--since")
    parser.add_argument("--work", type=Path, default=DEFAULT_WORK)
    parser.add_argument("--registry", type=Path, default=REGISTRY)
    parser.add_argument("--task-limit", type=int, default=100)
    parser.add_argument("--seconds", type=int, default=1800)
    arguments = parser.parse_args()
    if arguments.task_limit < 1 or arguments.seconds < 1:
        parser.error("task and time budgets must be positive")
    if arguments.work == DEFAULT_WORK and not os.path.ismount(DEFAULT_WORK.parents[1]):
        raise RuntimeError("approved persistent backup volume is not mounted; refusing root-disk fallback")
    with backup_owner(arguments.work):
        old = json.loads(arguments.state.read_text(encoding="utf-8")) if arguments.state.exists() else {}
        producer = Producer(api, arguments.pages_repo.resolve(), arguments.files_repo.resolve(),
                            arguments.work, arguments.registry,
                            source_consumer=SourceInventory(arguments.work / "source-inventory", arguments.registry))
        # Import the legacy discovery watermark once; never infer all tasks
        # completed merely because a discovery or run timestamp advanced.
        status = producer.run(since=arguments.since or old.get("last"),
                              task_limit=arguments.task_limit, seconds=arguments.seconds)
        atomic_json(arguments.state, {"schema_version": 2, **status})
        print(json.dumps(status, sort_keys=True))
        return 1 if status["failed_tasks"] or status["discovery_failures"] or status.get("source_inventory_failures") else 0


if __name__ == "__main__":
    raise SystemExit(main())
