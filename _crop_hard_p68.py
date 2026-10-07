#!/usr/bin/env python3
"""Hard-crop unclear Worlds Day 2 p68-p73 lines."""
from pathlib import Path
from PIL import Image

SRC = Path("encyclopedia/pc-2013-events/extract")
OUT = SRC / "_strips" / "worlds" / "lines"
OUT.mkdir(parents=True, exist_ok=True)


def line_box(im, col: str, n: int, form2013: bool = False):
    """Approximate one numbered card row.
    2010 form: left 1-40, right 41-60. 2013 form similar with more shield rows.
    """
    w, h = im.size
    top = int(h * 0.155)
    mid = int(h * 0.78)
    lh = mid - top
    if col == "L":
        # 40 lines in left column
        y0 = top + int(lh * (n - 1) / 40)
        y1 = top + int(lh * n / 40)
        return (0, y0, int(w * 0.52), y1)
    if col == "R":
        rn = n - 40
        y0 = top + int(lh * (rn - 1) / 20)
        y1 = top + int(lh * rn / 20)
        return (int(w * 0.48), y0, w, y1)
    return (0, 0, w, h)


JOBS = [
    ("worlds_d2_p68.png", "L", 26),
    ("worlds_d2_p68.png", "L", 27),
    ("worlds_d2_p68.png", "L", 37),
    ("worlds_d2_p68.png", "L", 38),
    ("worlds_d2_p68.png", "L", 39),
    ("worlds_d2_p68.png", "R", 43),
    ("worlds_d2_p68.png", "R", 48),
    ("worlds_d2_p69.png", "L", 8),
    ("worlds_d2_p69.png", "L", 11),
    ("worlds_d2_p69.png", "L", 14),
    ("worlds_d2_p69.png", "L", 18),
    ("worlds_d2_p69.png", "L", 19),
    ("worlds_d2_p69.png", "L", 20),
    ("worlds_d2_p69.png", "L", 35),
    ("worlds_d2_p69.png", "R", 51),
    ("worlds_d2_p69.png", "R", 55),
    ("worlds_d2_p69.png", "R", 56),
    ("worlds_d2_p71.png", "L", 30),
    ("worlds_d2_p71.png", "L", 36),
    ("worlds_d2_p71.png", "R", 41),
    ("worlds_d2_p72.png", "L", 7),
    ("worlds_d2_p72.png", "L", 22),
    ("worlds_d2_p72.png", "L", 37),
    ("worlds_d2_p72.png", "L", 40),
    ("worlds_d2_p72.png", "R", 44),
    ("worlds_d2_p72.png", "R", 50),
    ("worlds_d2_p72.png", "R", 55),
    ("worlds_d2_p72.png", "R", 57),
    ("worlds_d2_p73.png", "L", 11),
    ("worlds_d2_p73.png", "L", 16),
    ("worlds_d2_p73.png", "L", 40),
    ("worlds_d2_p73.png", "R", 41),
]

for name, col, n in JOBS:
    im = Image.open(SRC / name)
    box = line_box(im, col, n)
    out = OUT / f"{name.replace('.png','')}_{col}{n}.png"
    im.crop(box).save(out)
    print("wrote", out.name, box)

# shield row 3 on p71 (2010 form shields sit in bottom-right)
im = Image.open(SRC / "worlds_d2_p71.png")
w, h = im.size
im.crop((int(w * 0.48), int(h * 0.78), w, int(h * 0.86))).save(OUT / "worlds_d2_p71_sh1_4.png")
im.crop((int(w * 0.48), int(h * 0.74), w, int(h * 0.90))).save(OUT / "worlds_d2_p71_sh_block.png")
print("DONE")
