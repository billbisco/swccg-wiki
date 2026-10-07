#!/usr/bin/env python3
"""Hard line recrops for 2012 MPC Day 1 p51–p52 Roy Bordier."""
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2012-events" / "extract"
OUT = EXTRACT / "_bordier"

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

crop_lines("mpc_d1_p51.png", "p51", [10, 11, 13, 27], [50], [8, 9])
crop_lines("mpc_d1_p52.png", "p52", [18, 25, 28], [43], [])
