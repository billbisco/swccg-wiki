#!/usr/bin/env python3
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events"
MEDIA = ROOT / "y2013-tmw-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2013TMWDay1.pdf", "2013 Texas Mini Worlds Day 1.pdf"),
    (SRC / "extract" / "tmw_d1_p01.png", "2013 Texas Mini Worlds Day 1 p01 Nick Reisch DS.png"),
    (SRC / "extract" / "tmw_d1_p02.png", "2013 Texas Mini Worlds Day 1 p02 Nick Reisch LS.png"),
    (SRC / "extract" / "tmw_d1_p03.png", "2013 Texas Mini Worlds Day 1 p03 Aaron Nelson LS.png"),
    (SRC / "extract" / "tmw_d1_p04.png", "2013 Texas Mini Worlds Day 1 p04 Aaron Nelson DS.png"),
    (SRC / "extract" / "tmw_d1_p05.png", "2013 Texas Mini Worlds Day 1 p05 Robbie Hendon LS.png"),
    (SRC / "extract" / "tmw_d1_p06.png", "2013 Texas Mini Worlds Day 1 p06 Robbie Hendon DS.png"),
    (SRC / "extract" / "tmw_d1_p07.png", "2013 Texas Mini Worlds Day 1 p07 Greg Shaw DS.png"),
    (SRC / "extract" / "tmw_d1_p08.png", "2013 Texas Mini Worlds Day 1 p08 Greg Shaw LS.png"),
    (SRC / "extract" / "tmw_d1_p09.png", "2013 Texas Mini Worlds Day 1 p09 Greg Shaw DS.png"),
    (SRC / "extract" / "tmw_d1_p10.png", "2013 Texas Mini Worlds Day 1 p10 Greg Shaw LS.png"),
    (SRC / "extract" / "tmw_d1_p11.png", "2013 Texas Mini Worlds Day 1 p11 Mike Richards DS.png"),
    (SRC / "extract" / "tmw_d1_p12.png", "2013 Texas Mini Worlds Day 1 p12 Mike Richards LS.png"),
    (SRC / "extract" / "tmw_d1_p13.png", "2013 Texas Mini Worlds Day 1 p13 Mike Richards LS.png"),
    (SRC / "extract" / "tmw_d1_p14.png", "2013 Texas Mini Worlds Day 1 p14 Steve Baroni DS.png"),
    (SRC / "extract" / "tmw_d1_p15.png", "2013 Texas Mini Worlds Day 1 p15 Steve Baroni LS.png"),
    (SRC / "extract" / "tmw_d1_p16.png", "2013 Texas Mini Worlds Day 1 p16 Bobby Hilbun DS.png"),
    (SRC / "extract" / "tmw_d1_p17.png", "2013 Texas Mini Worlds Day 1 p17 Bobby Hilbun LS.png"),
    (SRC / "extract" / "tmw_d1_p18.png", "2013 Texas Mini Worlds Day 1 p18 Evan Kirkpatrick LS.png"),
    (SRC / "extract" / "tmw_d1_p19.png", "2013 Texas Mini Worlds Day 1 p19 Evan Kirkpatrick DS.png"),
    (SRC / "extract" / "tmw_d1_p20.png", "2013 Texas Mini Worlds Day 1 p20 JW Millet LS.png"),
    (SRC / "extract" / "tmw_d1_p21.png", "2013 Texas Mini Worlds Day 1 p21 JW Millet DS.png"),
    (SRC / "extract" / "tmw_d1_p22.png", "2013 Texas Mini Worlds Day 1 p22 James Barnes LS.png"),
    (SRC / "extract" / "tmw_d1_p23.png", "2013 Texas Mini Worlds Day 1 p23 James Barnes DS.png"),
    (SRC / "extract" / "tmw_d1_p24.png", "2013 Texas Mini Worlds Day 1 p24 Steve Skilton LS.png"),
    (SRC / "extract" / "tmw_d1_p25.png", "2013 Texas Mini Worlds Day 1 p25 Steve Izzo DS.png"),
    (SRC / "extract" / "tmw_d1_p26.png", "2013 Texas Mini Worlds Day 1 p26 Brian Herold LS.png"),
    (SRC / "extract" / "tmw_d1_p27.png", "2013 Texas Mini Worlds Day 1 p27 Brian Herold DS.png"),
    (SRC / "extract" / "tmw_d1_p28.png", "2013 Texas Mini Worlds Day 1 p28 Blake Huffman DS.png"),
    (SRC / "extract" / "tmw_d1_p29.png", "2013 Texas Mini Worlds Day 1 p29 Blake Huffman LS.png"),
    (SRC / "extract" / "tmw_d1_p30.png", "2013 Texas Mini Worlds Day 1 p30 John Anderson DS.png"),
    (SRC / "extract" / "tmw_d1_p31.png", "2013 Texas Mini Worlds Day 1 p31 John Anderson LS.png"),
    (SRC / "extract" / "tmw_d1_p32.png", "2013 Texas Mini Worlds Day 1 p32 Barry Alperstein DS.png"),
    (SRC / "extract" / "tmw_d1_p33.png", "2013 Texas Mini Worlds Day 1 p33 Barry Alperstein LS.png"),
    (SRC / "extract" / "tmw_d1_p34.png", "2013 Texas Mini Worlds Day 1 p34 Amar Banger LS.png"),
    (SRC / "extract" / "tmw_d1_p35.png", "2013 Texas Mini Worlds Day 1 p35 Amar Banger DS.png"),
    (SRC / "extract" / "tmw_d1_p36.png", "2013 Texas Mini Worlds Day 1 p36 Allen Gamble DS.png"),
    (SRC / "extract" / "tmw_d1_p37.png", "2013 Texas Mini Worlds Day 1 p37 Allen Gamble LS.png"),
    (SRC / "extract" / "tmw_d1_p38.png", "2013 Texas Mini Worlds Day 1 p38 Olaf Schroeder DS.png"),
    (SRC / "extract" / "tmw_d1_p39.png", "2013 Texas Mini Worlds Day 1 p39 Olaf Schroeder LS.png"),
    (SRC / "extract" / "tmw_d1_p40.png", "2013 Texas Mini Worlds Day 1 p40 Matt Wehner LS.png"),
    (SRC / "extract" / "tmw_d1_p41.png", "2013 Texas Mini Worlds Day 1 p41 Matt Wehner DS.png"),
]
for src, name in JOBS:
    dest = MEDIA / name
    if not src.exists():
        raise SystemExit(f"missing {src}")
    shutil.copy2(src, dest)
    print("copy", dest.name, dest.stat().st_size)
print("DONE", MEDIA)
