#!/usr/bin/env python3
"""Crop 2010/2013 PC decklist rasters (1530x1980) into line PNGs."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "extract"


def crop_page(src: Path, dest_dir: Path, form: str = "xerox_2010") -> None:
    im = Image.open(src)
    w, h = im.size
    dest_dir.mkdir(parents=True, exist_ok=True)
    im.crop((0, 0, w, int(h * 0.22))).save(dest_dir / "hdr.png")

    # Empirically 1530x1980 2010/2013 Xerox at 180 dpi.
    lx0, lx1 = int(w * 0.025), int(w * 0.495)
    rx0, rx1 = int(w * 0.495), int(w * 0.985)
    y0 = int(h * 0.214)
    pitch = h * 0.01845  # ~36.5px at 1980
    for i in range(40):
        y = int(y0 + i * pitch)
        y2 = int(y0 + (i + 1) * pitch) + 2
        im.crop((lx0, y, lx1, y2)).save(dest_dir / f"L{i+1:02d}.png")
    for i in range(20):
        y = int(y0 + i * pitch)
        y2 = int(y0 + (i + 1) * pitch) + 2
        im.crop((rx0, y, rx1, y2)).save(dest_dir / f"R{i+41:02d}.png")
    # Shields start after a header row below line 60.
    sh_y0 = int(y0 + 21 * pitch)
    sh_n = 15 if form == "xerox_2013" else 12
    sh_pitch = h * 0.0166
    for i in range(sh_n):
        y = int(sh_y0 + i * sh_pitch)
        y2 = int(sh_y0 + (i + 1) * sh_pitch) + 2
        im.crop((rx0, y, rx1, y2)).save(dest_dir / f"S{i+1:02d}.png")
    add_y0 = int(sh_y0 + (sh_n + 1.4) * sh_pitch)
    add_n = 6 if form != "xerox_2013" else 3
    for i in range(add_n):
        y = int(add_y0 + i * sh_pitch)
        y2 = int(add_y0 + (i + 1) * sh_pitch) + 2
        im.crop((rx0, y, rx1, y2)).save(dest_dir / f"A{i+1:02d}.png")
    print("cropped", src.name, "->", dest_dir, "form", form)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("usage: _crop_xerox.py relpath/from/extract out_dirname [xerox_2010|xerox_2013]")
        return 2
    src = EXTRACT / argv[0]
    dest = EXTRACT / "_day2_crops" / argv[1]
    form = argv[2] if len(argv) > 2 else "xerox_2010"
    crop_page(src, dest, form)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
