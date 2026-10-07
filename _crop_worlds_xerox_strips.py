#!/usr/bin/env python3
"""Crop left/right card columns + shields from selected 2013 Worlds Xerox pages."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "worlds"
OUT.mkdir(parents=True, exist_ok=True)

# Full-page PNG names (in extract/) to crop.
PAGES = [
    "worlds_d2_p101.png",
    "worlds_d2_p102.png",
]


def main() -> None:
    for name in PAGES:
        src = SRC / name
        im = Image.open(src)
        w, h = im.size
        stem = name.replace(".png", "")
        # Card title block starts under the header (~22% down).
        top = int(h * 0.155)
        mid = int(h * 0.78)
        # Left 1-40, right 41-60, bottom shields.
        im.crop((0, top, int(w * 0.52), mid)).save(OUT / f"{stem}_L.png")
        im.crop((int(w * 0.48), top, w, mid)).save(OUT / f"{stem}_R.png")
        im.crop((0, int(h * 0.74), w, h)).save(OUT / f"{stem}_SH.png")
        # Split left/right into top/bot halves for readability.
        lh = mid - top
        im.crop((0, top, int(w * 0.52), top + lh // 2)).save(OUT / f"{stem}_Ltop.png")
        im.crop((0, top + lh // 2, int(w * 0.52), mid)).save(OUT / f"{stem}_Lbot.png")
        im.crop((int(w * 0.48), top, w, top + lh // 2)).save(OUT / f"{stem}_Rtop.png")
        im.crop((int(w * 0.48), top + lh // 2, w, mid)).save(OUT / f"{stem}_Rbot.png")
        print("strips", stem, im.size)
    print("DONE", OUT)


if __name__ == "__main__":
    main()
