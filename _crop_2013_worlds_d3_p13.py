#!/usr/bin/env python3
"""Crop 2013 Print Form strips for Worlds Day 3 p13-p14 (Reid Smith)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "worlds"
OUT.mkdir(parents=True, exist_ok=True)


def main() -> None:
    for page in (13, 14):
        im = Image.open(SRC / f"worlds_d3_p{page:02d}.png")
        w, h = im.size
        stem = f"worlds_d3_p{page:02d}"
        top = int(h * 0.155)
        mid = int(h * 0.78)
        im.crop((0, 0, w, int(h * 0.22))).save(OUT / f"{stem}_hdr.png")
        im.crop((0, top, int(w * 0.52), mid)).save(OUT / f"{stem}_L.png")
        im.crop((int(w * 0.48), top, w, mid)).save(OUT / f"{stem}_R.png")
        im.crop((0, int(h * 0.74), w, h)).save(OUT / f"{stem}_SH.png")
        lh = mid - top
        im.crop((0, top, int(w * 0.52), top + lh // 2)).save(OUT / f"{stem}_Ltop.png")
        im.crop((0, top + lh // 2, int(w * 0.52), mid)).save(OUT / f"{stem}_Lbot.png")
        im.crop((int(w * 0.48), top, w, top + lh // 2)).save(OUT / f"{stem}_Rtop.png")
        im.crop((int(w * 0.48), top + lh // 2, w, mid)).save(OUT / f"{stem}_Rbot.png")
        print("cropped", stem, im.size)


if __name__ == "__main__":
    main()
