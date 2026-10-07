#!/usr/bin/env python3
from __future__ import annotations

import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2012-events"
MEDIA = ROOT / "y2012-bespin-media"
MEDIA.mkdir(parents=True, exist_ok=True)

JOBS = [
    (SRC / "2012BespinRegionals.pdf", "2012 Bespin Regionals.pdf"),
    (SRC / "extract" / "bespin_p02.png", "2012 Bespin Regionals Mitch Nieland LS.png"),
    (SRC / "extract" / "bespin_p01.png", "2012 Bespin Regionals Mitch Nieland DS.png"),
    (SRC / "extract" / "bespin_p04.png", "2012 Bespin Regionals Charlie Arlandson LS.png"),
    (SRC / "extract" / "bespin_p03.png", "2012 Bespin Regionals Charlie Arlandson DS.png"),
    (SRC / "extract" / "bespin_p05.png", "2012 Bespin Regionals Scott Morgan LS.png"),
    (SRC / "extract" / "bespin_p06.png", "2012 Bespin Regionals Scott Morgan DS.png"),
    (SRC / "extract" / "bespin_p08.png", "2012 Bespin Regionals Conrad Simmering LS.png"),
    (SRC / "extract" / "bespin_p07.png", "2012 Bespin Regionals Conrad Simmering DS.png"),
    (SRC / "extract" / "bespin_p10.png", "2012 Bespin Regionals Cooleo LS.png"),
    (SRC / "extract" / "bespin_p09.png", "2012 Bespin Regionals Cooleo DS.png"),
    (SRC / "extract" / "bespin_p11.png", "2012 Bespin Regionals Brandon Brist DS.png"),
    (SRC / "extract" / "bespin_p16.png", "2012 Bespin Regionals Calvin Kurten LS.png"),
    (SRC / "extract" / "bespin_p15.png", "2012 Bespin Regionals Calvin Kurten DS.png"),
    (SRC / "extract" / "bespin_p19.png", "2012 Bespin Regionals Mark Peterson LS.png"),
    (SRC / "extract" / "bespin_p20.png", "2012 Bespin Regionals Mark Peterson DS.png"),
    (SRC / "extract" / "bespin_p21.png", "2012 Bespin Regionals Nick Rambo LS.png"),
    (SRC / "extract" / "bespin_p22.png", "2012 Bespin Regionals Nick Rambo DS.png"),
    (SRC / "extract" / "bespin_p23.png", "2012 Bespin Regionals Jim Li LS.png"),
    (SRC / "extract" / "bespin_p24.png", "2012 Bespin Regionals Jim Li DS.png"),
    (SRC / "extract" / "bespin_p26.png", "2012 Bespin Regionals Brian Herold LS.png"),
    (SRC / "extract" / "bespin_p25.png", "2012 Bespin Regionals Brian Herold DS.png"),
    (SRC / "extract" / "bespin_p28.png", "2012 Bespin Regionals Morgan Dwyer LS.png"),
    (SRC / "extract" / "bespin_p27.png", "2012 Bespin Regionals Morgan Dwyer DS.png"),
    (SRC / "extract" / "bespin_p29.png", "2012 Bespin Regionals John Anderson LS.png"),
    (SRC / "extract" / "bespin_p30.png", "2012 Bespin Regionals John Anderson DS.png"),
    (SRC / "extract" / "bespin_p32.png", "2012 Bespin Regionals Jake Nelson LS.png"),
    (SRC / "extract" / "bespin_p31.png", "2012 Bespin Regionals Jake Nelson DS.png"),
    (SRC / "extract" / "bespin_p34.png", "2012 Bespin Regionals Matt Hanson LS.png"),
    (SRC / "extract" / "bespin_p33.png", "2012 Bespin Regionals Matt Hanson DS.png"),
    (SRC / "extract" / "bespin_p35.png", "2012 Bespin Regionals Mike DS.png"),
    (SRC / "extract" / "bespin_p37.png", "2012 Bespin Regionals Mark Walseth LS.png"),
    (SRC / "extract" / "bespin_p38.png", "2012 Bespin Regionals Mark Walseth DS.png"),
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
