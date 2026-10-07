#!/usr/bin/env python3
"""Recrop remaining Hilbun hard lines from column strips."""
from __future__ import annotations
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "encyclopedia" / "pc-2013-events" / "extract" / "_strips" / "tmw"

JOBS = [
    ("tmw_d1_p16_R.png", (0, 540, 800, 640), "p16_l56b.png"),
    ("tmw_d1_p16_R.png", (0, 620, 800, 720), "p16_l58b.png"),
    ("tmw_d1_p16_R.png", (0, 690, 800, 755), "p16_l60b.png"),
    ("tmw_d1_p16_SH.png", (0, 40, 800, 120), "p16_sh1b.png"),
    ("tmw_d1_p16_Lbot.png", (0, 300, 800, 400), "p16_l39b.png"),
    ("tmw_d1_p16_ADD.png", (0, 0, 800, 80), "p16_add3.png"),
    ("tmw_d1_p17_ADD.png", (0, 0, 800, 90), "p17_add3.png"),
    ("tmw_d1_p17_R.png", (0, 0, 800, 90), "p17_l41b.png"),
]


def main() -> None:
    for src, box, out_name in JOBS:
        im = Image.open(OUT / src)
        im.crop(box).save(OUT / out_name)
        print("cropped", out_name, im.size)


if __name__ == "__main__":
    main()
