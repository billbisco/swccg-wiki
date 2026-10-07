#!/usr/bin/env python3
"""Crop Name/Username header from Xerox scans."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_username_crops"
JOBS = [
    ROOT / "y2013-mpc-media" / "2013 Match Play Championship p90 Smith LS.png",
    ROOT / "y2013-mpc-media" / "2013 Match Play Championship p89 Smith DS.png",
    ROOT / "y2013-socal-media" / "2013 SoCal Grand Prix Day 1 p37 Reid Smith LS.png",
    ROOT / "y2013-socal-media" / "2013 SoCal Grand Prix Day 1 p38 Reid Smith DS.png",
]
# Right header: Name / Username / Email.
BOX = (980, 20, 1530, 250)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src in JOBS:
        im = Image.open(src)
        crop = im.crop(BOX)
        dest = OUT / (src.stem + " user.png")
        crop.save(dest)
        print("wrote", dest, im.size)


if __name__ == "__main__":
    main()
