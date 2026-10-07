#!/usr/bin/env python3
"""2009 Print Form bands for 2012 TMW Day 1 p26 Light / p27 Dark Steve Skilton.

Analog leftover 2012 TMW Herold p03: left 1-36 / right 37-60 / 12 shields.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"


def bands(src: Path, out: Path) -> None:
    im = Image.open(src)
    w, h = im.size
    out.mkdir(parents=True, exist_ok=True)
    lx0, lx1 = 20, 780
    rx0, rx1 = 750, w - 10
    y0 = 375
    pitch_l = 38.8
    pitch_r = 38.8
    jobs = (
        ("L0110", y0, 0, 10, pitch_l, lx0, lx1),
        ("L1120", y0, 10, 10, pitch_l, lx0, lx1),
        ("L2130", y0, 20, 10, pitch_l, lx0, lx1),
        ("L3140", y0, 30, 6, pitch_l, lx0, lx1),
        ("R3746", y0, 0, 10, pitch_r, rx0, rx1),
        ("R4756", y0, 10, 10, pitch_r, rx0, rx1),
        ("R5760", y0, 20, 4, pitch_r, rx0, rx1),
    )
    for name, base, start, n, pitch, x0, x1 in jobs:
        y = int(base + start * pitch)
        y2 = int(base + (start + n) * pitch) + 6
        im.crop((x0, y, x1, min(y2, h))).save(out / f"{name}.png")
    sh0 = int(y0 + 24 * pitch_r) + 40
    im.crop((rx0, sh0, rx1, min(sh0 + int(13 * 32), h))).save(out / "S.png")
    im.crop((rx0, sh0 + int(7 * 32), rx1, min(sh0 + int(13 * 32), h))).save(out / "S812.png")
    im.crop((lx0, int(y0 + 27 * pitch_l), lx1, int(y0 + 36 * pitch_l) + 8)).save(
        out / "L2836.png"
    )
    im.crop((lx0, int(y0 + 33 * pitch_l), lx1, int(y0 + 36 * pitch_l) + 10)).save(
        out / "L3536.png"
    )
    im.crop((lx0, int(y0 + 34.5 * pitch_l), lx1, min(int(y0 + 40 * pitch_l), h))).save(
        out / "Lbot2.png"
    )
    im.crop((rx0, int(y0 + 21 * pitch_r), rx1, int(y0 + 24 * pitch_r) + 10)).save(
        out / "R5960.png"
    )
    im.crop((rx0, sh0 + int(8 * 32), rx1, min(sh0 + int(13 * 32) + 20, h))).save(
        out / "S1012.png"
    )
    im.crop((rx0, sh0 + int(9 * 32), rx1, min(h, sh0 + int(16 * 32)))).save(
        out / "S1112.png"
    )
    im.crop((lx0, int(y0 + 18 * pitch_l), lx1, int(y0 + 20 * pitch_l) + 8)).save(
        out / "L19.png"
    )
    im.crop((0, 0, w, 360)).save(out / "HDR.png")
    print("cropped", src.name, "->", out, im.size)


def main() -> None:
    bands(EXTRACT / "tmw_d1_p26.png", EXTRACT / "_tmw_d1_p26")
    bands(EXTRACT / "tmw_d1_p27.png", EXTRACT / "_tmw_d1_p27")


if __name__ == "__main__":
    main()
