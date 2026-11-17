#!/usr/bin/env python3
"""Lane 2: open Wayback captures from manpc and drop verified receipts for the VPS worker.

The VPS worker (lane 1) submits Save Page Now and tries to confirm. When the VPS
cannot open web.archive.org, it leaves pending/ok rows. Run this on manpc:

    py -3 ops/wayback_verify_manpc.py

It SSHs to gemp, verifies up to --limit URLs locally, and scp's a receipt into
/root/.local/state/swccg-wayback/verify-inbox/ for the next worker run.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import wayback_worker as W  # noqa: E402

HOST = os.environ.get("WAYBACK_SSH", "gemp")
REMOTE_INBOX = "/root/.local/state/swccg-wayback/verify-inbox"
REMOTE_REPO = "/opt/swccg-ops/repos/swccg-wiki"


def ssh(args: list[str], *, check=True) -> subprocess.CompletedProcess:
    return subprocess.run(["ssh", HOST, *args], check=check, capture_output=True, text=True)


def load_manpc_keys() -> None:
    if W.AUTH:
        return
    ini = Path.home() / ".config" / "ia.ini"
    if not ini.exists():
        return
    acc = sec = ""
    for line in ini.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line.startswith("access"):
            acc = line.split("=", 1)[-1].strip()
        elif line.startswith("secret"):
            sec = line.split("=", 1)[-1].strip()
    if acc and sec:
        W.AUTH = f"LOW {acc}:{sec}"


def dump_candidates(limit: int) -> list[dict]:
    remote = (
        f"python3 {REMOTE_REPO}/ops/wayback_verify_manpc.py --dump-candidates --limit {int(limit)}"
    )
    out = ssh([remote])
    return json.loads(out.stdout)


def confirm_pending(row: dict) -> dict | None:
    if row.get("capture"):
        return row
    job = row.get("job_id")
    if not job:
        return None
    try:
        st = W.spn2_status(job)
    except Exception as error:  # noqa: BLE001
        print("STATUS-ERR", row["url"], str(error)[:80], flush=True)
        return None
    if st.get("status") == "success" and st.get("timestamp"):
        url = row["url"]
        row = dict(row)
        row["capture"] = f"https://web.archive.org/web/{st['timestamp']}/{st.get('original_url') or url}"
        return row
    return None


def verify_row(row: dict) -> dict | None:
    url, cap = row["url"], row.get("capture")
    if not cap:
        return None
    try:
        status, info = W.verify(url, cap)
    except W.VerifyRetry as error:
        print("VERIFY-ERR", url, str(error)[:80], flush=True)
        return None
    if status != "verified":
        print("UNVERIFIED", url, info.get("reason") or info.get("method"), flush=True)
        return None
    info["at"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print("VERIFIED", url, info.get("method"), flush=True)
    return {"capture": cap, "status": "verified", "verify": info, "job_id": row.get("job_id") or ""}


def drop_inbox(updates: dict) -> str:
    name = datetime.now(timezone.utc).strftime("manpc-%Y%m%dT%H%M%SZ.json")
    payload = {"schema": 1, "lane": "manpc", "updates": updates}
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", suffix=".json", delete=False) as fh:
        json.dump(payload, fh)
        local = fh.name
    ssh(["mkdir", "-p", REMOTE_INBOX])
    subprocess.run(["scp", local, f"{HOST}:{REMOTE_INBOX}/{name}"], check=True)
    Path(local).unlink(missing_ok=True)
    return name


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--dump-candidates", action="store_true")
    args = ap.parse_args()
    if args.dump_candidates:
        done_path = Path(os.environ.get("SWCCG_WIKI_REPO", REMOTE_REPO)) / "ops/wayback/done.json"
        done = json.loads(done_path.read_text(encoding="utf-8"))
        json.dump(W.verify_candidates(done, limit=args.limit), sys.stdout)
        return 0
    load_manpc_keys()
    rows = dump_candidates(args.limit)
    print("candidates", len(rows), flush=True)
    updates = {}
    for row in rows:
        ready = confirm_pending(row)
        if not ready:
            continue
        receipt = verify_row(ready)
        if receipt:
            updates[row["url"]] = receipt
    if not updates:
        print("no verified receipts", flush=True)
        return 0
    name = drop_inbox(updates)
    print("inbox", name, len(updates), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
