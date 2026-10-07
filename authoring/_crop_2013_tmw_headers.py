#!/usr/bin/env python3
"""Crop headers of unpublished 2013 TMW Day 1 pages."""
from __future__ import annotations
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "tmw"
OUT.mkdir(parents=True, exist_ok=True)

# Skip LIVE typed leftovers: 1-2 Reisch, 11-13 Richards, 18-19 Kirkpatrick, 22-23 Barnes
SKIP = {1, 2, 11, 12, 13, 18, 19, 22, 23}
PAGES = sorted(
    int(p.stem.split("_p")[-1])
    for p in SRC.glob("tmw_d1_p*.png")
)

def main() -> None:
    for n in PAGES:
        if n in SKIP:
            continue
        im = Image.open(SRC / f"tmw_d1_p{n:02d}.png")
        w, h = im.size
        # Top header band; 2010 Xerox analog.
        box = (0, 0, w, min(h, int(h * 0.22)))
        im.crop(box).save(OUT / f"tmw_d1_p{n:02d}_hdr.png")
        print(n, im.size)
    print("cropped", OUT)

if __name__ == "__main__":
    main()
