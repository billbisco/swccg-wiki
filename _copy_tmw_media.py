#!/usr/bin/env python3
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2014-events"
MEDIA = ROOT / "y2014-tmw-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2014-TMW-Day-1.pdf", "2014 Texas Mini Worlds Day 1.pdf"),
    (SRC / "2014-TMW-Day-2.pdf", "2014 Texas Mini Worlds Day 2.pdf"),
    (SRC / "extract" / "tmw_d2_p03.png", "2014 Texas Mini Worlds Day 2 p03 Nick Reisch LS.png"),
    (SRC / "extract" / "tmw_d2_p04.png", "2014 Texas Mini Worlds Day 2 p04 Nick Reisch DS.png"),
    (SRC / "extract" / "tmw_d1_p07.png", "2014 Texas Mini Worlds Day 1 p07 Nick Reisch DS.png"),
    (SRC / "extract" / "tmw_d1_p08.png", "2014 Texas Mini Worlds Day 1 p08 Nick Reisch LS.png"),
    (SRC / "extract" / "tmw_d1_p11.png", "2014 Texas Mini Worlds Day 1 p11 Paul Bonsall DS.png"),
    (SRC / "extract" / "tmw_d1_p12.png", "2014 Texas Mini Worlds Day 1 p12 Paul Bonsall DS.png"),
]
for src, name in JOBS:
    dest = MEDIA / name
    if not src.exists():
        raise SystemExit(f"missing {src}")
    shutil.copy2(src, dest)
    print("copy", dest.name, dest.stat().st_size)
print("DONE", MEDIA)
