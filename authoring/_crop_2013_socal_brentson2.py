#!/usr/bin/env python3
"""Per-line recrops for Brentson p09-p10 hard handwriting."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "socal"


def lines(im: Image.Image, box, n0: int, nvis: int, want: list[int], tag: str) -> None:
    x0, y0, x1, y1 = box
    crop = im.crop(box)
    w, h = crop.size
    dest = OUT / tag
    dest.mkdir(parents=True, exist_ok=True)
    for n in want:
        i = n - n0
        ya = int(h * i / nvis) - 6
        yb = int(h * (i + 1) / nvis) + 10
        crop.crop((0, max(0, ya), w, min(h, yb))).save(dest / f"ln{n:02d}.png")


def main() -> None:
    p09 = Image.open(EXTRACT / "socal_d1_p09.png")
    p10 = Image.open(EXTRACT / "socal_d1_p10.png")
    # left 1-36 area
    lines(p09, (40, 400, 780, 1680), 1, 36, [1, 2, 4, 5, 9, 12, 13, 14, 17, 18, 19, 20, 22], "socal_d1_p09")
    lines(p09, (40, 1600, 780, 1900), 35, 6, [35, 36, 37, 38], "socal_d1_p09")
    lines(p09, (760, 400, 1490, 1020), 42, 17, [42, 43, 44, 45, 47, 49, 50, 51, 52, 53, 54, 57, 58], "socal_d1_p09")
    lines(p09, (760, 1000, 1490, 1500), 58, 14, [58, 59, 60], "socal_d1_p09")
    # shields in Rmid after 60
    sh = p09.crop((760, 1180, 1490, 1680))
    sh.save(OUT / "socal_d1_p09" / "shA.png")
    shb = p09.crop((760, 1480, 1490, 1780))
    shb.save(OUT / "socal_d1_p09" / "shB.png")
    p09.crop((760, 1680, 1490, 1920)).save(OUT / "socal_d1_p09" / "shC.png")
    # dark
    lines(p10, (40, 400, 780, 1680), 1, 36, list(range(1, 37)), "socal_d1_p10")
    lines(p10, (40, 1600, 780, 1900), 35, 6, [35, 36, 37, 38, 39, 40], "socal_d1_p10")
    lines(p10, (760, 400, 1490, 1020), 41, 18, list(range(41, 59)), "socal_d1_p10")
    p10.crop((760, 1000, 1490, 1500)).save(OUT / "socal_d1_p10" / "Rmid.png")
    p10.crop((760, 1480, 1490, 2080)).save(OUT / "socal_d1_p10" / "Rbot.png")
    p10.crop((40, 330, 780, 520)).save(OUT / "socal_d1_p10" / "L01_04.png")
    print("ok")


if __name__ == "__main__":
    main()
