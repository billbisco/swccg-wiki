#!/usr/bin/env python3
"""Crop full-page headers and name boxes for leftover Day 2 p25, p28-p40."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_nameboxes"
HDR = SRC / "headers"
OUT.mkdir(parents=True, exist_ok=True)
HDR.mkdir(parents=True, exist_ok=True)

PAGES = [25] + list(range(28, 41))


def main() -> None:
    for i in PAGES:
        src = SRC / f"worlds_d2_p{i:02d}.png"
        if not src.exists():
            print("MISSING", src.name)
            continue
        im = Image.open(src)
        w, h = im.size
        im.crop((0, 0, w, int(h * 0.22))).save(HDR / f"worlds_d2_p{i:02d}_hdr.png")
        # Xerox top-right name/username
        im.crop((int(w * 0.55), 0, w, int(h * 0.22))).save(
            OUT / f"d2_p{i:02d}_name.png"
        )
        # Informal overlay often puts name top-left
        im.crop((0, 0, int(w * 0.55), int(h * 0.18))).save(
            OUT / f"d2_p{i:02d}_left.png"
        )
        print(src.name, im.size)
    print("DONE", PAGES)


if __name__ == "__main__":
    main()
