#!/usr/bin/env python3
"""Recrop hard lines from aligned Harpster column strips."""
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
    p13 = ST / "socal_d1_p13"
    p14 = ST / "socal_d1_p14"
    split(p13 / "La.png", 2, 12, [6, 8, 9, 11, 12, 13], p13)
    split(p13 / "Lb.png", 13, 12, [13, 15, 19, 21, 23], p13)
    split(p13 / "Lc.png", 24, 13, [25, 27, 28, 29, 31, 32, 33, 34], p13)
    split(p13 / "Lbot.png", 35, 6, [37, 38, 39], p13)
    split(p13 / "R37_41.png", 41, 5, [41, 42, 43, 44], p13)
    split(p13 / "Rtop.png", 42, 17, [42, 45, 46, 50, 51, 52, 55, 57, 58], p13)
    split(p13 / "Rmid.png", 58, 16, [59, 60, 61, 62, 63, 64], p13)
    split(p14 / "La.png", 2, 12, [5, 6, 7, 9, 11, 12], p14)
    split(p14 / "Lb.png", 13, 12, [15, 17, 19, 20, 21, 22], p14)
    split(p14 / "Lc.png", 24, 13, [25, 28, 29, 33, 34], p14)
    split(p14 / "Lbot.png", 35, 6, [37, 38, 39, 40], p14)
    split(p14 / "R37_41.png", 41, 5, [41, 43, 44], p14)
    split(p14 / "Rtop.png", 42, 17, [43, 45, 46, 49, 53, 55], p14)
    split(p14 / "Rmid.png", 58, 16, [59, 60, 61, 64, 67, 68], p14)
    print("ok")


if __name__ == "__main__":
    main()
