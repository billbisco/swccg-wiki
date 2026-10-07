#!/usr/bin/env python3
"""Pack 2012 US Nationals leftover Xerox. Default is the delta tarball."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from _xerox_delta import pack  # noqa: E402

DELTA = ROOT / "y2012-nats-xerox-delta.tsv"
FULL = ROOT / "y2012-nats-xerox-titles.tsv"
MEDIA = ROOT / "y2012-nats-media"
APPLIED_MEDIA = ROOT / "y2012-nats-media-applied.txt"
OUT = ROOT / "y2012-nats-xerox.tgz"
APPLY = "apply-2012-nats-xerox.sh"
# Non-existent path so --full treats every PNG/PDF as new.
NO_APPLIED = ROOT / ".xerox-no-applied-media"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--full", action="store_true", help="pack every title + all media")
    args = ap.parse_args()
    if args.full:
        pack(FULL, MEDIA, NO_APPLIED, OUT, APPLY, "y2012-nats-media")
        return
    tsv = DELTA if DELTA.exists() and DELTA.stat().st_size else FULL
    pack(tsv, MEDIA, APPLIED_MEDIA, OUT, APPLY, "y2012-nats-media-delta")


if __name__ == "__main__":
    main()
