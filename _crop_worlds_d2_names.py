#!/usr/bin/env python3
"""Crop name/username boxes from 2013 Worlds Day 1 Aaron + unpublished Day 2."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_nameboxes"
OUT.mkdir(parents=True, exist_ok=True)

# Already dested Day 2 pages.
DONE_D2 = {1, 2, 5, 6, 7, 8}


def crop_name(src: Path, dest: Path) -> None:
    im = Image.open(src)
    w, h = im.size
    # Xerox form name/username/email is the top-right block.
    box = (int(w * 0.68), 0, w, int(h * 0.18))
    im.crop(box).save(dest)


def main() -> None:
    crop_name(SRC / "worlds_d1_p07.png", OUT / "d1_p07_name.png")
    crop_name(SRC / "worlds_d1_p08.png", OUT / "d1_p08_name.png")
    n = 0
    for i in range(1, 119):
        if i in DONE_D2:
            continue
        src = SRC / f"worlds_d2_p{i:02d}.png"
        if not src.exists():
            print("MISSING", src.name)
            continue
        dest = OUT / f"d2_p{i:02d}_name.png"
        crop_name(src, dest)
        n += 1
    print("wrote", n, "d2 nameboxes plus d1 p07/p08", "out", OUT)


if __name__ == "__main__":
    main()
