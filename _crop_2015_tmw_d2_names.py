#!/usr/bin/env python3
"""Extra name-box crops for 2015 TMW Day 2 pages whose top strip missed the header."""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2015-events" / "extract"
OUT = ROOT / "_tmw_headers"
# full page 1530x1978; name box on 2010 form is ~y 80-220; handwritten lists often top-left
JOBS = {
    "tmw_d2_p01.png": [(0, 0, 1530, 400), (0, 1700, 1530, 1978)],
    "tmw_d2_p03.png": [(0, 0, 1530, 450), (0, 1650, 1530, 1983)],
    "tmw_d2_p04.png": [(0, 0, 1530, 450), (0, 1650, 1530, 1983)],
    "tmw_d2_p17.png": [(0, 0, 1530, 400), (0, 1650, 1530, 1978)],
    "tmw_d2_p18.png": [(0, 0, 1530, 400), (0, 1650, 1530, 1978)],
}

def main() -> None:
    for name, boxes in JOBS.items():
        im = Image.open(ROOT / name)
        for i, box in enumerate(boxes, 1):
            dest = OUT / f"{Path(name).stem}_n{i}.png"
            im.crop(box).save(dest, "PNG")
            print("wrote", dest.name, im.size)
    # landscape p02: rotate then crop top
    p2 = Image.open(ROOT / "tmw_d2_p02.png")
    if p2.size[0] > p2.size[1]:
        p2 = p2.rotate(-90, expand=True)
    p2.crop((0, 0, p2.size[0], 400)).save(OUT / "tmw_d2_p02_n1.png", "PNG")
    print("wrote tmw_d2_p02_n1.png", p2.size)

if __name__ == "__main__":
    main()
