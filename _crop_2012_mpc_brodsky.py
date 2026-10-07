#!/usr/bin/env python3
"""Crop 10-line bands for 2012 MPC Day 1 p53–p54 Brian Brodsky."""
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"
OUT = EXTRACT / "_brodsky"
OUT.mkdir(parents=True, exist_ok=True)


def bands(src_name: str, prefix: str) -> None:
    im = Image.open(EXTRACT / src_name)
    w, h = im.size
    lx0, lx1 = int(w * 0.025), int(w * 0.495)
    rx0, rx1 = int(w * 0.495), int(w * 0.985)
    y0 = int(h * 0.188)
    pitch = h * 0.01845
    for start in (1, 11, 21, 31):
        y = int(y0 + (start - 1) * pitch)
        y2 = int(y0 + (start + 9) * pitch) + 6
        im.crop((lx0, y, lx1, min(y2, h))).save(OUT / f"{prefix}_L{start:02d}-{start+9:02d}.png")
    for start in (41, 51):
        y = int(y0 + (start - 41) * pitch)
        y2 = int(y0 + (start - 31) * pitch) + 6
        im.crop((rx0, y, rx1, min(y2, h))).save(OUT / f"{prefix}_R{start:02d}-{start+9:02d}.png")
    sh_y0 = int(y0 + 21 * pitch)
    sh_pitch = h * 0.0166
    y = int(sh_y0)
    y2 = int(sh_y0 + 12 * sh_pitch) + 6
    im.crop((rx0, y, rx1, min(y2, h))).save(OUT / f"{prefix}_SHIELDS.png")
    print(prefix, w, h)


bands("mpc_d1_p53.png", "p53")
bands("mpc_d1_p54.png", "p54")
