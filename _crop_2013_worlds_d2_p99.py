#!/usr/bin/env python3
"""Crop typed GEMP list 2013 Worlds Day 2 p99 VeeZ DS."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "worlds"
OUT.mkdir(parents=True, exist_ok=True)

im = Image.open(SRC / "worlds_d2_p99.png")
w, h = im.size
print("size", w, h)
# two-column typed list; left has shield bracket
im.crop((0, 0, w // 2 + 40, int(h * 0.42))).save(OUT / "worlds_d2_p99_Ltop.png")
im.crop((0, int(h * 0.38), w // 2 + 40, int(h * 0.72))).save(OUT / "worlds_d2_p99_Lmid.png")
im.crop((0, int(h * 0.68), w // 2 + 40, h)).save(OUT / "worlds_d2_p99_Lbot.png")
im.crop((w // 2 - 20, 0, w, int(h * 0.55))).save(OUT / "worlds_d2_p99_Rtop.png")
im.crop((w // 2 - 20, int(h * 0.50), w, h)).save(OUT / "worlds_d2_p99_Rbot.png")
print("cropped p99")
