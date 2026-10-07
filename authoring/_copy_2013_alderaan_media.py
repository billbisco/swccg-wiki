#!/usr/bin/env python3
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events"
MEDIA = ROOT / "y2013-alderaan-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2013AlderaanRegionals.pdf", "2013 Alderaan Regionals.pdf"),
    (SRC / "extract" / "alderaan_p11.png", "2013 Alderaan Regionals p11 Ryan Jellison LS.png"),
    (SRC / "extract" / "alderaan_p12.png", "2013 Alderaan Regionals p12 Ryan Jellison DS.png"),
    (SRC / "extract" / "alderaan_p13.png", "2013 Alderaan Regionals p13 Chris Menzel LS.png"),
    (SRC / "extract" / "alderaan_p14.png", "2013 Alderaan Regionals p14 Chris Menzel DS.png"),
    (SRC / "extract" / "alderaan_p15.png", "2013 Alderaan Regionals p15 Ganden Yanaga DS.png"),
    (SRC / "extract" / "alderaan_p16.png", "2013 Alderaan Regionals p16 Ganden Yanaga LS.png"),
    (SRC / "extract" / "alderaan_p17.png", "2013 Alderaan Regionals p17 Bren Derlin LS.png"),
    (SRC / "extract" / "alderaan_p18.png", "2013 Alderaan Regionals p18 Bren Derlin DS.png"),
    (SRC / "extract" / "alderaan_p23.png", "2013 Alderaan Regionals p23 Anthony Massung LS.png"),
    (SRC / "extract" / "alderaan_p01.png", "2013 Alderaan Regionals p01 Matthew Harrison-Trainor LS.png"),
    (SRC / "extract" / "alderaan_p02.png", "2013 Alderaan Regionals p02 Matthew Harrison-Trainor DS.png"),
    (SRC / "extract" / "alderaan_p09.png", "2013 Alderaan Regionals p09 Clayton Atkin DS.png"),
    (SRC / "extract" / "alderaan_p10.png", "2013 Alderaan Regionals p10 Clayton Atkin LS.png"),
    (SRC / "extract" / "alderaan_p24.png", "2013 Alderaan Regionals p24 Anthony Massung DS.png"),
    (SRC / "extract" / "alderaan_p03.png", "2013 Alderaan Regionals p03 Tom LS.png"),
    (SRC / "extract" / "alderaan_p04.png", "2013 Alderaan Regionals p04 Tom DS.png"),
    (SRC / "extract" / "alderaan_p07.png", "2013 Alderaan Regionals p07 Kevin Shannon DS.png"),
    (SRC / "extract" / "alderaan_p08.png", "2013 Alderaan Regionals p08 Kevin Shannon LS.png"),
    (SRC / "extract" / "alderaan_p21.png", "2013 Alderaan Regionals p21 Chris Schoenthal LS.png"),
    (SRC / "extract" / "alderaan_p22.png", "2013 Alderaan Regionals p22 Chris Schoenthal DS.png"),
    (SRC / "extract" / "alderaan_p25.png", "2013 Alderaan Regionals p25 Nathan DS.png"),
    (SRC / "extract" / "alderaan_p26.png", "2013 Alderaan Regionals p26 Nathan LS.png"),
    (SRC / "extract" / "alderaan_p27.png", "2013 Alderaan Regionals p27 Roy McCarthy LS.png"),
    (SRC / "extract" / "alderaan_p28.png", "2013 Alderaan Regionals p28 Roy McCarthy DS.png"),
]
for src, name in JOBS:
    dest = MEDIA / name
    if not src.exists():
        raise SystemExit(f"missing {src}")
    shutil.copy2(src, dest)
    print("copy", dest.name, dest.stat().st_size)
print("DONE", MEDIA)
