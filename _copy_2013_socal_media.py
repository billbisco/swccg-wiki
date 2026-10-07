#!/usr/bin/env python3
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events"
MEDIA = ROOT / "y2013-socal-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2013SoCalDay1.pdf", "2013 SoCal Grand Prix Day 1.pdf"),
    (SRC / "2013SoCalDay2.pdf", "2013 SoCal Grand Prix Day 2.pdf"),
    (SRC / "extract" / "socal_d1_p01.png", "2013 SoCal Grand Prix Day 1 p01 Phil Aasen LS.png"),
    (SRC / "extract" / "socal_d1_p02.png", "2013 SoCal Grand Prix Day 1 p02 Phil Aasen DS.png"),
    (SRC / "extract" / "socal_d1_p05.png", "2013 SoCal Grand Prix Day 1 p05 John Anderson LS.png"),
    (SRC / "extract" / "socal_d1_p06.png", "2013 SoCal Grand Prix Day 1 p06 John Anderson DS.png"),
    (SRC / "extract" / "socal_d1_p07.png", "2013 SoCal Grand Prix Day 1 p07 Clayton Atkin LS.png"),
    (SRC / "extract" / "socal_d1_p08.png", "2013 SoCal Grand Prix Day 1 p08 Clayton Atkin DS.png"),
    (SRC / "extract" / "socal_d1_p03.png", "2013 SoCal Grand Prix Day 1 p03 Gabe LS.png"),
    (SRC / "extract" / "socal_d1_p04.png", "2013 SoCal Grand Prix Day 1 p04 Gabe DS.png"),
    (SRC / "extract" / "socal_d1_p09.png", "2013 SoCal Grand Prix Day 1 p09 Steve Brentson LS.png"),
    (SRC / "extract" / "socal_d1_p10.png", "2013 SoCal Grand Prix Day 1 p10 Steve Brentson DS.png"),
    (SRC / "extract" / "socal_d1_p11.png", "2013 SoCal Grand Prix Day 1 p11 Brian Fred LS.png"),
    (SRC / "extract" / "socal_d1_p12.png", "2013 SoCal Grand Prix Day 1 p12 Brian Fred DS.png"),
    (SRC / "extract" / "socal_d1_p13.png", "2013 SoCal Grand Prix Day 1 p13 Steve Harpster LS.png"),
    (SRC / "extract" / "socal_d1_p14.png", "2013 SoCal Grand Prix Day 1 p14 Steve Harpster DS.png"),
    (SRC / "extract" / "socal_d1_p21.png", "2013 SoCal Grand Prix Day 1 p21 Tom LS.png"),
    (SRC / "extract" / "socal_d1_p22.png", "2013 SoCal Grand Prix Day 1 p22 Tom DS.png"),
    (SRC / "extract" / "socal_d1_p23.png", "2013 SoCal Grand Prix Day 1 p23 Bill LS.png"),
    (SRC / "extract" / "socal_d1_p24.png", "2013 SoCal Grand Prix Day 1 p24 Bill DS.png"),
    (SRC / "extract" / "socal_d1_p25.png", "2013 SoCal Grand Prix Day 1 p25 Josh LS.png"),
    (SRC / "extract" / "socal_d1_p26.png", "2013 SoCal Grand Prix Day 1 p26 Josh DS.png"),
    (SRC / "extract" / "socal_d1_p41.png", "2013 SoCal Grand Prix Day 1 p41 Nathan LS.png"),
    (SRC / "extract" / "socal_d1_p42.png", "2013 SoCal Grand Prix Day 1 p42 Nathan DS.png"),
    (SRC / "extract" / "socal_d1_p43.png", "2013 SoCal Grand Prix Day 1 p43 Jan Westergard LS.png"),
    (SRC / "extract" / "socal_d1_p44.png", "2013 SoCal Grand Prix Day 1 p44 Jan Westergard DS.png"),
    (SRC / "extract" / "socal_d1_p45.png", "2013 SoCal Grand Prix Day 1 p45 Ganden Yanaga LS.png"),
    (SRC / "extract" / "socal_d1_p46.png", "2013 SoCal Grand Prix Day 1 p46 Ganden Yanaga DS.png"),
    (SRC / "extract" / "socal_d1_p19.png", "2013 SoCal Grand Prix Day 1 p19 Brian Herold LS.png"),
    (SRC / "extract" / "socal_d1_p20.png", "2013 SoCal Grand Prix Day 1 p20 Brian Herold DS.png"),
    (SRC / "extract" / "socal_d1_p27.png", "2013 SoCal Grand Prix Day 1 p27 Anthony Massung LS.png"),
    (SRC / "extract" / "socal_d1_p28.png", "2013 SoCal Grand Prix Day 1 p28 Anthony Massung DS.png"),
    (SRC / "extract" / "socal_d1_p31.png", "2013 SoCal Grand Prix Day 1 p31 Kevin Shannon LS.png"),
    (SRC / "extract" / "socal_d1_p32.png", "2013 SoCal Grand Prix Day 1 p32 Kevin Shannon DS.png"),
    (SRC / "extract" / "socal_d1_p33.png", "2013 SoCal Grand Prix Day 1 p33 Greg Shaw LS.png"),
    (SRC / "extract" / "socal_d1_p34.png", "2013 SoCal Grand Prix Day 1 p34 Greg Shaw DS.png"),
    (SRC / "extract" / "socal_d1_p15.png", "2013 SoCal Grand Prix Day 1 p15 Matthew Harrison-Trainor LS.png"),
    (SRC / "extract" / "socal_d1_p16.png", "2013 SoCal Grand Prix Day 1 p16 Matthew Harrison-Trainor LS.png"),
    (SRC / "extract" / "socal_d1_p17.png", "2013 SoCal Grand Prix Day 1 p17 Matthew Harrison-Trainor DS.png"),
    (SRC / "extract" / "socal_d1_p18.png", "2013 SoCal Grand Prix Day 1 p18 Matthew Harrison-Trainor DS.png"),
    (SRC / "extract" / "socal_d1_p29.png", "2013 SoCal Grand Prix Day 1 p29 Joe Olson LS.png"),
    (SRC / "extract" / "socal_d1_p30.png", "2013 SoCal Grand Prix Day 1 p30 Joe Olson DS.png"),
    (SRC / "extract" / "socal_d2_p03.png", "2013 SoCal Grand Prix Day 2 p03 Matthew Harrison-Trainor LS.png"),
    (SRC / "extract" / "socal_d2_p04.png", "2013 SoCal Grand Prix Day 2 p04 Matthew Harrison-Trainor DS.png"),
    (SRC / "extract" / "socal_d2_p05.png", "2013 SoCal Grand Prix Day 2 p05 Matthew Harrison-Trainor DS.png"),
    (SRC / "extract" / "socal_d2_p01.png", "2013 SoCal Grand Prix Day 2 p01 Clayton Atkin LS.png"),
    (SRC / "extract" / "socal_d2_p02.png", "2013 SoCal Grand Prix Day 2 p02 Clayton Atkin DS.png"),
    (SRC / "extract" / "socal_d2_p08.png", "2013 SoCal Grand Prix Day 2 p08 Kevin Shannon LS.png"),
    (SRC / "extract" / "socal_d2_p09.png", "2013 SoCal Grand Prix Day 2 p09 Kevin Shannon DS.png"),
    (SRC / "extract" / "socal_d1_p35.png", "2013 SoCal Grand Prix Day 1 p35 Steve Skilton LS.png"),
    (SRC / "extract" / "socal_d1_p36.png", "2013 SoCal Grand Prix Day 1 p36 Steve Skilton DS.png"),
    (SRC / "extract" / "socal_d1_p37.png", "2013 SoCal Grand Prix Day 1 p37 Reid Smith LS.png"),
    (SRC / "extract" / "socal_d1_p38.png", "2013 SoCal Grand Prix Day 1 p38 Reid Smith DS.png"),
    (SRC / "extract" / "socal_d1_p39.png", "2013 SoCal Grand Prix Day 1 p39 Matt Thornton LS.png"),
    (SRC / "extract" / "socal_d1_p40.png", "2013 SoCal Grand Prix Day 1 p40 Matt Thornton DS.png"),
    (SRC / "extract" / "socal_d2_p06.png", "2013 SoCal Grand Prix Day 2 p06 Reid Smith LS.png"),
    (SRC / "extract" / "socal_d2_p07.png", "2013 SoCal Grand Prix Day 2 p07 Reid Smith DS.png"),
]
for src, name in JOBS:
    dest = MEDIA / name
    if not src.exists():
        raise SystemExit(f"missing {src}")
    shutil.copy2(src, dest)
    print("copy", dest.name, dest.stat().st_size)
print("DONE", MEDIA)
