#!/usr/bin/env python3
"""Crop selected 2010-form lines for 2012 MPC Day 1 p49–p50 Andrew Bollentino."""
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"
OUT = EXTRACT / "_bollemo"
OUT.mkdir(parents=True, exist_ok=True)


def crop_lines(src_name: str, prefix: str, left_ns: list[int], right_ns: list[int], shields: list[int]) -> None:
    im = Image.open(EXTRACT / src_name)
    w, h = im.size
    lx0, lx1 = int(w * 0.025), int(w * 0.495)
    rx0, rx1 = int(w * 0.495), int(w * 0.985)
    y0 = int(h * 0.188)
    pitch = h * 0.01845
    for n in left_ns:
        y = int(y0 + (n - 1) * pitch)
        y2 = int(y0 + n * pitch) + 4
        im.crop((lx0, y, lx1, min(y2, h))).save(OUT / f"{prefix}_L{n:02d}.png")
    for n in right_ns:
        y = int(y0 + (n - 41) * pitch)
        y2 = int(y0 + (n - 40) * pitch) + 4
        im.crop((rx0, y, rx1, min(y2, h))).save(OUT / f"{prefix}_R{n:02d}.png")
    sh_y0 = int(y0 + 21 * pitch)
    sh_pitch = h * 0.0166
    for n in shields:
        y = int(sh_y0 + (n - 1) * sh_pitch)
        y2 = int(sh_y0 + n * sh_pitch) + 4
        im.crop((rx0, y, rx1, min(y2, h))).save(OUT / f"{prefix}_S{n:02d}.png")
    print(prefix, w, h)


crop_lines("mpc_d1_p49.png", "p49", [9, 10, 20, 24, 36], [50, 51, 55, 56], [1, 8, 12])
crop_lines("mpc_d1_p50.png", "p50", [10, 12, 21, 32, 38, 39, 40], [43, 44, 58, 60], [1, 9, 12])
