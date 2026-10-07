#!/usr/bin/env python3
"""Crop typed 2013 Worlds Day 2 p78-p79 Nick Reisch."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "worlds"
OUT.mkdir(parents=True, exist_ok=True)

for page in (78, 79):
    im = Image.open(SRC / f"worlds_d2_p{page:02d}.png")
    w, h = im.size
    print(page, w, h)
    im.crop((0, 0, w, 180)).save(OUT / f"worlds_d2_p{page:02d}_hdr.png")
    im.crop((0, 150, w // 2 + 30, int(h * 0.55))).save(OUT / f"worlds_d2_p{page:02d}_Ltop.png")
    im.crop((0, int(h * 0.50), w // 2 + 30, h)).save(OUT / f"worlds_d2_p{page:02d}_Lbot.png")
    im.crop((w // 2 - 20, 150, w, int(h * 0.55))).save(OUT / f"worlds_d2_p{page:02d}_Rtop.png")
    im.crop((w // 2 - 20, int(h * 0.50), w, h)).save(OUT / f"worlds_d2_p{page:02d}_Rbot.png")
print("cropped")
