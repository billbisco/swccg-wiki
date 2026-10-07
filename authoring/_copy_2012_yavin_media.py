#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2012-events"
MEDIA = ROOT / "y2012-yavin-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "Yavin42012.pdf", "2012 Yavin 4 Regionals.pdf"),
    (SRC / "extract" / "yavin_p01.png", "2012 Yavin 4 Regionals Chris Westergard LS.png"),
    (SRC / "extract" / "yavin_p02.png", "2012 Yavin 4 Regionals Chris Westergard DS.png"),
    (SRC / "extract" / "yavin_p03.png", "2012 Yavin 4 Regionals Scott LS.png"),
    (SRC / "extract" / "yavin_p04.png", "2012 Yavin 4 Regionals Scott DS.png"),
    (SRC / "extract" / "yavin_p05.png", "2012 Yavin 4 Regionals Steve Skilton LS.png"),
    (SRC / "extract" / "yavin_p07.png", "2012 Yavin 4 Regionals Steve Skilton DS.png"),
    (SRC / "extract" / "yavin_p09.png", "2012 Yavin 4 Regionals Vincent Rossi LS.png"),
    (SRC / "extract" / "yavin_p11.png", "2012 Yavin 4 Regionals Vincent Rossi DS.png"),
    (SRC / "extract" / "yavin_p15.png", "2012 Yavin 4 Regionals Joe Orthner LS.png"),
    (SRC / "extract" / "yavin_p14.png", "2012 Yavin 4 Regionals Joe Orthner DS.png"),
    (SRC / "extract" / "yavin_p17.png", "2012 Yavin 4 Regionals Matt Schmaltz LS.png"),
    (SRC / "extract" / "yavin_p16.png", "2012 Yavin 4 Regionals Matt Schmaltz DS.png"),
    (SRC / "extract" / "yavin_p18.png", "2012 Yavin 4 Regionals Alex Klimenko LS.png"),
    (SRC / "extract" / "yavin_p20.png", "2012 Yavin 4 Regionals Alex Klimenko DS.png"),
    (SRC / "extract" / "yavin_p24.png", "2012 Yavin 4 Regionals Ben Brummett LS.png"),
    (SRC / "extract" / "yavin_p23.png", "2012 Yavin 4 Regionals Ben Brummett DS.png"),
    (SRC / "extract" / "yavin_p26.png", "2012 Yavin 4 Regionals Tom Haid LS.png"),
    (SRC / "extract" / "yavin_p25.png", "2012 Yavin 4 Regionals Tom Haid DS.png"),
    (SRC / "extract" / "yavin_p28.png", "2012 Yavin 4 Regionals Greg Shaw LS.png"),
    (SRC / "extract" / "yavin_p27.png", "2012 Yavin 4 Regionals Greg Shaw DS.png"),
    (SRC / "extract" / "yavin_p30.png", "2012 Yavin 4 Regionals Vikram Bali LS.png"),
    (SRC / "extract" / "yavin_p29.png", "2012 Yavin 4 Regionals Vikram Bali DS.png"),
    (SRC / "extract" / "yavin_p32.png", "2012 Yavin 4 Regionals Michael Klimenko LS.png"),
    (SRC / "extract" / "yavin_p31.png", "2012 Yavin 4 Regionals Michael Klimenko DS.png"),
    (SRC / "extract" / "yavin_p33.png", "2012 Yavin 4 Regionals Bentley Boyd LS.png"),
    (SRC / "extract" / "yavin_p34.png", "2012 Yavin 4 Regionals Bentley Boyd DS.png"),
    (SRC / "extract" / "yavin_p36.png", "2012 Yavin 4 Regionals Tim Murray LS.png"),
    (SRC / "extract" / "yavin_p35.png", "2012 Yavin 4 Regionals Tim Murray DS.png"),
]


def main() -> None:
    n = 0
    for src, dest_name in JOBS:
        dest = MEDIA / dest_name
        if not src.exists():
            print("MISSING", src)
            continue
        shutil.copy2(src, dest)
        n += 1
        print("copied", dest_name)
    print("copied", n, "of", len(JOBS))


if __name__ == "__main__":
    main()
