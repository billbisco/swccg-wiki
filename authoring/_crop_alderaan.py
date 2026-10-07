#!/usr/bin/env python3
"""Crop 2014 Alderaan Regionals Xerox pages (confirmed names) into line PNGs."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "encyclopedia" / "pc-2014-worlds"))
from _crop_xerox import crop_page  # noqa: E402

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2014-events" / "extract"
OUT = EXTRACT / "_alderaan_crops"

JOBS = [
    ("alderaan_p01.png", "yanaga_ls", "xerox_2013"),
    ("alderaan_p02.png", "yanaga_ds", "xerox_2013"),
    ("alderaan_p03.png", "massung_ls", "xerox_2013"),
    ("alderaan_p04.png", "massung_ds", "xerox_2013"),
    ("alderaan_p07.png", "huderich_ls", "xerox_2013"),
    ("alderaan_p08.png", "huderich_ds", "xerox_2013"),
    ("alderaan_p13.png", "mccarthy_ls", "xerox_2013"),
    ("alderaan_p14.png", "mccarthy_ds", "xerox_2013"),
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src_name, dest_name, form in JOBS:
        src = EXTRACT / src_name
        dest = OUT / dest_name
        crop_page(src, dest, "xerox_2010")
    print("DONE", OUT)


if __name__ == "__main__":
    main()
