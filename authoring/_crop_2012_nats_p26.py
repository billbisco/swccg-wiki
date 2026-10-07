#!/usr/bin/env python3
"""10-line bands for 2012 Nats Day 1 p26 Dark / p27 Light Matt Hanson."""
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
    print("cropped", src.name, "->", out)


def main() -> None:
    bands(EXTRACT / "nats_d1_p26.png", EXTRACT / "_p26")
    bands(EXTRACT / "nats_d1_p27.png", EXTRACT / "_p27")


if __name__ == "__main__":
    main()
