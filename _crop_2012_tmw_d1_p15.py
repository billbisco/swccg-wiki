#!/usr/bin/env python3
"""Typed-dump bands for 2012 TMW Day 1 p15 Dark / p16 Light Matt Lush."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"


def bands(src: Path, out: Path) -> None:
    im = Image.open(src)
    w, h = im.size
    out.mkdir(parents=True, exist_ok=True)
    im.crop((0, 0, w, int(h * 0.12))).save(out / "TOP.png")
    lx0, lx1 = int(w * 0.02), int(w * 0.52)
    rx0, rx1 = int(w * 0.48), int(w * 0.99)
    jobs = (
        ("L1", 0.08, 0.28),
        ("L2", 0.26, 0.46),
        ("L3", 0.44, 0.64),
        ("L4", 0.62, 0.82),
        ("L5", 0.80, 1.00),
        ("R1", 0.08, 0.28),
        ("R2", 0.26, 0.46),
        ("R3", 0.44, 0.64),
        ("R4", 0.62, 0.82),
        ("R5", 0.80, 1.00),
    )
    for name, y0f, y1f in jobs:
        x0, x1 = (lx0, lx1) if name.startswith("L") else (rx0, rx1)
        im.crop((x0, int(h * y0f), x1, int(h * y1f))).save(out / f"{name}.png")
    print("cropped", src.name, w, h, "->", out)


def main() -> None:
    bands(EXTRACT / "tmw_d1_p15.png", EXTRACT / "_tmw_d1_p15")
    bands(EXTRACT / "tmw_d1_p16.png", EXTRACT / "_tmw_d1_p16")


if __name__ == "__main__":
    main()
