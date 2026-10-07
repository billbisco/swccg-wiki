#!/usr/bin/env python3
"""Column crops for 2013 SoCal Day 1 p03-p04 Gabe typed Print Form."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "socal"

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


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for page in (3, 4):
        name = f"socal_d1_p{page:02d}.png"
        src = EXTRACT / name
        dest = OUT / name.replace(".png", "")
        dest.mkdir(parents=True, exist_ok=True)
        im = Image.open(src)
        print("size", name, im.size)
        for key, box in PRINT.items():
            im.crop(box).save(dest / f"{key}.png")
        print("cropped", name, "->", dest)


if __name__ == "__main__":
    main()
