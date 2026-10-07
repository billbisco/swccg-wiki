#!/usr/bin/env python3
"""Typed-dump bands for 2012 Nats Day 1 p78–p81 (not 2010 Xerox forms)."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"


def bands(src: Path, out: Path) -> None:
    im = Image.open(src)
    w, h = im.size
    out.mkdir(parents=True, exist_ok=True)
    # Very top for Name / title (xerox_2010 HDR crops miss typed-dump titles)
    im.crop((0, 0, w, int(h * 0.12))).save(out / "TOP.png")
    # Mid-page columns of typed list
    lx0, lx1 = int(w * 0.02), int(w * 0.52)
    rx0, rx1 = int(w * 0.48), int(w * 0.99)
    jobs = (
        ("L1", 0.10, 0.28),
        ("L2", 0.26, 0.44),
        ("L3", 0.42, 0.60),
        ("L4", 0.58, 0.76),
        ("L5", 0.74, 0.92),
        ("L6", 0.88, 1.00),
    )
    for name, y0f, y1f in jobs:
        im.crop((lx0, int(h * y0f), lx1, int(h * y1f))).save(out / f"{name}.png")
        im.crop((rx0, int(h * y0f), rx1, int(h * y1f))).save(out / f"R{name[1]}.png")
    print("cropped", src.name, w, h, "->", out)


def main() -> None:
    for n in (78, 79, 80, 81):
        bands(EXTRACT / f"nats_d1_p{n:02d}.png", EXTRACT / f"_p{n:02d}")


if __name__ == "__main__":
    main()
