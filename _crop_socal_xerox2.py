#!/usr/bin/env python3
"""Column crops for remaining 2013 SoCal Xerox (1530x2103)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "socal"

# Measured from socal_d1_p01 (2010 Xerox, Chewie art).
XEROX = {
    "hdr": (0, 0, 1530, 462),
    "L": (0, 462, 735, 1976),
    "La": (0, 462, 735, 974),
    "Lb": (0, 962, 735, 1475),
    "Lc": (0, 1463, 735, 1976),
    "Rtop": (765, 462, 1530, 1198),
    "Rbot": (765, 1094, 1530, 2103),
}

# Print Form (dark header) — tuned after first look at p27.
PRINT = {
    "hdr": (0, 0, 1530, 430),
    "L": (40, 400, 780, 1680),
    "La": (40, 400, 780, 830),
    "Lb": (40, 810, 780, 1240),
    "Lc": (40, 1220, 780, 1680),
    "Rtop": (760, 400, 1490, 1020),
    "Rmid": (760, 1000, 1490, 1500),
    "Rbot": (760, 1480, 1490, 2080),
}

JOBS = [
    ("socal_d1_p35.png", "print"),
    ("socal_d1_p36.png", "print"),
    ("socal_d1_p37.png", "print"),
    ("socal_d1_p38.png", "print"),
    ("socal_d1_p39.png", "print"),
    ("socal_d1_p40.png", "print"),
    ("socal_d2_p06.png", "print"),
    ("socal_d2_p07.png", "print"),
]


def main() -> None:
    for name, kind in JOBS:
        src = EXTRACT / name
        dest = OUT / name.replace(".png", "")
        dest.mkdir(parents=True, exist_ok=True)
        im = Image.open(src)
        boxes = XEROX if kind == "xerox" else PRINT
        for key, box in boxes.items():
            im.crop(box).save(dest / f"{key}.png")
        print("cropped", name, im.size, kind, "->", dest)


if __name__ == "__main__":
    main()
