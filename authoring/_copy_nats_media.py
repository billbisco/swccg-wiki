#!/usr/bin/env python3
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2014-events"
MEDIA = ROOT / "y2014-nats-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "Nationals-2014-day-1.pdf", "2014 US Nationals Day 1.pdf"),
    (SRC / "Nationals-2014-day-2.pdf", "2014 US Nationals Day 2.pdf"),
    (SRC / "extract" / "nats_d2_p01.png", "2014 US Nationals Day 2 p01 Matthew Harrison-Trainor LS.png"),
    (SRC / "extract" / "nats_d2_p02.png", "2014 US Nationals Day 2 p02 Matthew Harrison-Trainor DS.png"),
    (SRC / "extract" / "nats_d1_p01.png", "2014 US Nationals Day 1 p01 Mike Tomashewski LS.png"),
    (SRC / "extract" / "nats_d1_p02.png", "2014 US Nationals Day 1 p02 Mike Tomashewski DS.png"),
    (SRC / "extract" / "nats_d1_p30.png", "2014 US Nationals Day 1 p30 Brad Eier LS.png"),
    (SRC / "extract" / "nats_d1_p31.png", "2014 US Nationals Day 1 p31 Brad Eier DS.png"),
]
for src, name in JOBS:
    dest = MEDIA / name
    if not src.exists():
        raise SystemExit(f"missing {src}")
    shutil.copy2(src, dest)
    print("copy", dest.name, dest.stat().st_size)
print("DONE", MEDIA)
