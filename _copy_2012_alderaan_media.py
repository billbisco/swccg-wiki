#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2012-events"
MEDIA = ROOT / "y2012-alderaan-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2012AlderaanRegionals.pdf", "2012 Alderaan Regionals.pdf"),
    (SRC / "extract" / "alderaan_p01.png", "2012 Alderaan Regionals Clayton Atkin LS.png"),
    (SRC / "extract" / "alderaan_p02.png", "2012 Alderaan Regionals Clayton Atkin DS.png"),
    (SRC / "extract" / "alderaan_p03.png", "2012 Alderaan Regionals Anthony Massung LS.png"),
    (SRC / "extract" / "alderaan_p04.png", "2012 Alderaan Regionals Anthony Massung DS.png"),
    (SRC / "extract" / "alderaan_p05.png", "2012 Alderaan Regionals Chris Schoenthal LS.png"),
    (SRC / "extract" / "alderaan_p06.png", "2012 Alderaan Regionals Chris Schoenthal DS.png"),
    (SRC / "extract" / "alderaan_p07.png", "2012 Alderaan Regionals Bill Kafer LS.png"),
    (SRC / "extract" / "alderaan_p08.png", "2012 Alderaan Regionals Bill Kafer DS.png"),
    (SRC / "extract" / "alderaan_p11.png", "2012 Alderaan Regionals Ganden Yanaga LS.png"),
    (SRC / "extract" / "alderaan_p12.png", "2012 Alderaan Regionals Ganden Yanaga DS.png"),
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
