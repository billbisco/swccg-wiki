#!/usr/bin/env python3
"""2010 Xerox 10-line bands for 2012 Alderaan Regionals p11 Light / p12 Dark Camden Yanaga dested Ganden Yanaga.

Analog leftover Alderaan p01/p03/p05/p07: y0=h*0.188 pitch=h*0.01845 extra L01 / R41 / S1112.
"""
from __future__ import annotations

from pathlib import Path

from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"


def bands(src: Path, out: Path) -> None:
    im = Image.open(src)
    w, h = im.size
    out.mkdir(parents=True, exist_ok=True)
    lx0, lx1 = int(w * 0.025), int(w * 0.495)
    rx0, rx1 = int(w * 0.495), int(w * 0.985)
    y0 = int(h * 0.188)
    pitch = h * 0.01845
    jobs = (
        ("L0110", 0, 10, lx0, lx1),
        ("L1120", 10, 10, lx0, lx1),
        ("L2130", 20, 10, lx0, lx1),
        ("L3140", 30, 10, lx0, lx1),
        ("R4150", 0, 10, rx0, rx1),
        ("R5160", 10, 10, rx0, rx1),
    )
    for name, start, n, x0, x1 in jobs:
        y = int(y0 + start * pitch)
        y2 = int(y0 + (start + n) * pitch) + 4
        im.crop((x0, y, x1, y2)).save(out / f"{name}.png")
    sh_y0 = int(y0 + 21 * pitch)
    sh_pitch = h * 0.0166
    y2 = int(sh_y0 + 12 * sh_pitch) + 4
    im.crop((rx0, sh_y0, rx1, y2)).save(out / "S.png")
    y1 = int(h * 0.168)
    y1b = int(y0 + 1 * pitch) + 4
    im.crop((lx0, y1, lx1, y1b)).save(out / "L01.png")
    im.crop((rx0, y1, rx1, y1b)).save(out / "R41.png")
    im.crop((lx0, int(y0 + 39 * pitch), lx1, int(y0 + 40 * pitch) + 8)).save(out / "L40.png")
    im.crop((rx0, int(sh_y0 + 10 * sh_pitch), rx1, y2)).save(out / "S1112.png")
    im.crop((rx0, sh_y0, rx1, int(sh_y0 + 6 * sh_pitch) + 8)).save(out / "S16.png")
    im.crop((0, 0, w, int(h * 0.188))).save(out / "HDR.png")
    print("cropped", src.name, "->", out, im.size)


def main() -> None:
    bands(EXTRACT / "alderaan_p11.png", EXTRACT / "_alderaan_p11")
    bands(EXTRACT / "alderaan_p12.png", EXTRACT / "_alderaan_p12")


if __name__ == "__main__":
    main()
