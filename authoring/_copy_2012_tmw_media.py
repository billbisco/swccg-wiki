#!/usr/bin/env python3
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2012-events"
MEDIA = ROOT / "y2012-tmw-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2012TMWDay1.pdf", "2012 Texas Mini Worlds Day 1.pdf"),
    (SRC / "extract" / "tmw_d1_p01.png", "2012 Texas Mini Worlds Day 1 Mike Richards LS.png"),
    (SRC / "extract" / "tmw_d1_p02.png", "2012 Texas Mini Worlds Day 1 Mike Richards DS.png"),
    (SRC / "extract" / "tmw_d1_p03.png", "2012 Texas Mini Worlds Day 1 Brian Herold LS.png"),
    (SRC / "extract" / "tmw_d1_p04.png", "2012 Texas Mini Worlds Day 1 Brian Herold DS.png"),
    (SRC / "extract" / "tmw_d1_p05.png", "2012 Texas Mini Worlds Day 1 Scott Lingrell DS.png"),
    (SRC / "extract" / "tmw_d1_p06.png", "2012 Texas Mini Worlds Day 1 Scott Lingrell LS.png"),
    (SRC / "extract" / "tmw_d1_p07.png", "2012 Texas Mini Worlds Day 1 Greg Shaw DS.png"),
    (SRC / "extract" / "tmw_d1_p08.png", "2012 Texas Mini Worlds Day 1 Greg Shaw LS.png"),
    (SRC / "extract" / "tmw_d1_p09.png", "2012 Texas Mini Worlds Day 1 James Barnes LS.png"),
    (SRC / "extract" / "tmw_d1_p10.png", "2012 Texas Mini Worlds Day 1 James Barnes DS.png"),
    (SRC / "extract" / "tmw_d1_p11.png", "2012 Texas Mini Worlds Day 1 Robbie Hendon LS.png"),
    (SRC / "extract" / "tmw_d1_p12.png", "2012 Texas Mini Worlds Day 1 Robbie Hendon DS.png"),
    (SRC / "extract" / "tmw_d1_p13.png", "2012 Texas Mini Worlds Day 1 John Anderson DS.png"),
    (SRC / "extract" / "tmw_d1_p14.png", "2012 Texas Mini Worlds Day 1 John Anderson LS.png"),
    (SRC / "extract" / "tmw_d1_p15.png", "2012 Texas Mini Worlds Day 1 Matt Lush DS.png"),
    (SRC / "extract" / "tmw_d1_p16.png", "2012 Texas Mini Worlds Day 1 Matt Lush LS.png"),
    (SRC / "extract" / "tmw_d1_p17.png", "2012 Texas Mini Worlds Day 1 Nick Reisch DS.png"),
    (SRC / "extract" / "tmw_d1_p18.png", "2012 Texas Mini Worlds Day 1 Nick Reisch LS.png"),
    (SRC / "extract" / "tmw_d1_p19.png", "2012 Texas Mini Worlds Day 1 Evan Kirkpatrick LS.png"),
    (SRC / "extract" / "tmw_d1_p20.png", "2012 Texas Mini Worlds Day 1 Evan Kirkpatrick DS.png"),
    (SRC / "extract" / "tmw_d1_p21.png", "2012 Texas Mini Worlds Day 1 John Veasey LS.png"),
    (SRC / "extract" / "tmw_d1_p23.png", "2012 Texas Mini Worlds Day 1 John Veasey DS.png"),
    (SRC / "extract" / "tmw_d1_p25.png", "2012 Texas Mini Worlds Day 1 Amar Banger LS.png"),
    (SRC / "extract" / "tmw_d1_p24.png", "2012 Texas Mini Worlds Day 1 Amar Banger DS.png"),
    (SRC / "extract" / "tmw_d1_p26.png", "2012 Texas Mini Worlds Day 1 Steve Skilton LS.png"),
    (SRC / "extract" / "tmw_d1_p27.png", "2012 Texas Mini Worlds Day 1 Steve Skilton DS.png"),
    (SRC / "extract" / "tmw_d1_p29.png", "2012 Texas Mini Worlds Day 1 Jeremy Gardner LS.png"),
    (SRC / "extract" / "tmw_d1_p28.png", "2012 Texas Mini Worlds Day 1 Jeremy Gardner DS.png"),
    (SRC / "extract" / "tmw_d1_p31.png", "2012 Texas Mini Worlds Day 1 Charley Joe LS.png"),
    (SRC / "extract" / "tmw_d1_p30.png", "2012 Texas Mini Worlds Day 1 Charley Joe DS.png"),
    (SRC / "2012TMWDay2.pdf", "2012 Texas Mini Worlds Day 2.pdf"),
    (SRC / "extract" / "tmw_d2_p02.png", "2012 Texas Mini Worlds Day 2 Mike Richards LS.png"),
    (SRC / "extract" / "tmw_d2_p01.png", "2012 Texas Mini Worlds Day 2 Mike Richards DS.png"),
    (SRC / "extract" / "tmw_d2_p03.png", "2012 Texas Mini Worlds Day 2 Scott Lingrell LS.png"),
    (SRC / "extract" / "tmw_d2_p04.png", "2012 Texas Mini Worlds Day 2 Scott Lingrell DS.png"),
    (SRC / "extract" / "tmw_d2_p06.png", "2012 Texas Mini Worlds Day 2 Brian Herold LS.png"),
    (SRC / "extract" / "tmw_d2_p05.png", "2012 Texas Mini Worlds Day 2 Brian Herold DS.png"),
    (SRC / "extract" / "tmw_d2_p08.png", "2012 Texas Mini Worlds Day 2 James Barnes LS.png"),
    (SRC / "extract" / "tmw_d2_p07.png", "2012 Texas Mini Worlds Day 2 James Barnes DS.png"),
    (SRC / "extract" / "tmw_d2_p09.png", "2012 Texas Mini Worlds Day 2 Greg Shaw LS.png"),
    (SRC / "extract" / "tmw_d2_p10.png", "2012 Texas Mini Worlds Day 2 Greg Shaw DS.png"),
    (SRC / "extract" / "tmw_d2_p11.png", "2012 Texas Mini Worlds Day 2 Robbie Hendon LS.png"),
    (SRC / "extract" / "tmw_d2_p12.png", "2012 Texas Mini Worlds Day 2 Robbie Hendon DS.png"),
    (SRC / "extract" / "tmw_d2_p14.png", "2012 Texas Mini Worlds Day 2 John Anderson LS.png"),
    (SRC / "extract" / "tmw_d2_p13.png", "2012 Texas Mini Worlds Day 2 John Anderson DS.png"),
    (SRC / "extract" / "tmw_d2_p16.png", "2012 Texas Mini Worlds Day 2 Matt Lush LS.png"),
    (SRC / "extract" / "tmw_d2_p15.png", "2012 Texas Mini Worlds Day 2 Matt Lush DS.png"),
]

for src, name in JOBS:
    dest = MEDIA / name
    if not src.exists():
        print("MISSING", src)
        continue
    shutil.copy2(src, dest)
    print("copied", dest.name)
