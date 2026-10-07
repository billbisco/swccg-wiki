#!/usr/bin/env python3
from __future__ import annotations
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2014-events"
EXTRACT = SRC / "extract"
MEDIA = ROOT / "y2014-alderaan-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2014-Alderaan-Regionals.pdf", "2014 Alderaan Regionals.pdf"),
    (EXTRACT / "alderaan_p01.png", "2014 Alderaan Regionals p01 Ganden Yanaga LS.png"),
    (EXTRACT / "alderaan_p02.png", "2014 Alderaan Regionals p02 Ganden Yanaga DS.png"),
    (EXTRACT / "alderaan_p03.png", "2014 Alderaan Regionals p03 Anthony Massung LS.png"),
    (EXTRACT / "alderaan_p04.png", "2014 Alderaan Regionals p04 Anthony Massung DS.png"),
    (EXTRACT / "alderaan_p07.png", "2014 Alderaan Regionals p07 Peter Huderich LS.png"),
    (EXTRACT / "alderaan_p08.png", "2014 Alderaan Regionals p08 Peter Huderich DS.png"),
    (EXTRACT / "alderaan_p13.png", "2014 Alderaan Regionals p13 Roy McCarthy LS.png"),
    (EXTRACT / "alderaan_p14.png", "2014 Alderaan Regionals p14 Roy McCarthy DS.png"),
]
for src, name in JOBS:
    dest = MEDIA / name
    if not src.exists():
        raise SystemExit(f"missing {src}")
    shutil.copy2(src, dest)
    print("copy", dest.name, dest.stat().st_size)
print("DONE", MEDIA)
