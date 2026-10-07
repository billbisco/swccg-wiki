#!/usr/bin/env python3
"""Recrop hard lines from aligned column strips."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
ST = ROOT / "encyclopedia" / "pc-2013-events" / "extract" / "_strips" / "socal"


def split(src: Path, n0: int, nvis: int, want: list[int], dest: Path) -> None:
    im = Image.open(src)
    w, h = im.size
    dest.mkdir(parents=True, exist_ok=True)
    for n in want:
        i = n - n0
        y0 = int(h * i / nvis) - 4
        y1 = int(h * (i + 1) / nvis) + 8
        im.crop((0, max(0, y0), w, min(h, y1))).save(dest / f"s{n:02d}.png")


def main() -> None:
    p9 = ST / "socal_d1_p09"
    p10 = ST / "socal_d1_p10"
    split(p9 / "La.png", 2, 12, [2, 4, 5, 9, 12, 13], p9)
    split(p9 / "Lb.png", 13, 12, [13, 14, 17, 18, 19, 20, 22, 24], p9)
    split(p9 / "Rtop.png", 42, 17, [42, 43, 44, 47, 50, 51, 52, 53, 57, 58], p9)
    split(p9 / "Rmid.png", 58, 16, [58, 59, 60], p9)
    split(p10 / "La.png", 2, 12, [2, 4, 5, 6, 8, 9, 10, 11, 12, 13], p10)
    split(p10 / "Lb.png", 13, 12, [13, 14, 18, 23, 24], p10)
    split(p10 / "Lc.png", 24, 13, [25, 29, 31, 32, 33, 34, 35, 36], p10)
    split(p10 / "Rtop.png", 42, 17, [42, 43, 44, 46, 48, 49, 51, 52, 53, 54, 55, 56, 57, 58], p10)
    split(p10 / "Rmid.png", 58, 16, [58, 59, 60], p10)
    print("ok")


if __name__ == "__main__":
    main()
