#!/usr/bin/env python3
"""Crop 2014 MPC Day 2 Xerox pages into line PNGs."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "encyclopedia" / "pc-2014-worlds"))
from _crop_xerox import crop_page  # noqa: E402

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2014-events" / "extract"
OUT = EXTRACT / "_mpc_d2_crops"

JOBS = [
    ("mpc_d2_p01.png", "cellucci_ds", "xerox_2013"),
    ("mpc_d2_p02.png", "cellucci_ls", "xerox_2013"),
    ("mpc_d2_p03.png", "mht_ds", "xerox_2013"),
    ("mpc_d2_p04.png", "mht_ls", "xerox_2013"),
    ("mpc_d2_p07.png", "shaw_ds", "xerox_2010"),
    ("mpc_d2_p08.png", "shaw_ls", "xerox_2010"),
]


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for src_name, dest_name, form in JOBS:
        src = EXTRACT / src_name
        dest = OUT / dest_name
        crop_page(src, dest, form)
    # Shannon informal notes: keep the written block
    from PIL import Image

    for i, name in [(5, "shannon_a"), (6, "shannon_b")]:
        src = EXTRACT / f"mpc_d2_p{i:02d}.png"
        im = Image.open(src)
        w, h = im.size
        dest = OUT / name
        dest.mkdir(exist_ok=True)
        im.crop((int(w * 0.45), 0, w, int(h * 0.55))).save(dest / "notes.png")
        im.crop((0, 0, int(w * 0.45), int(h * 0.4))).save(dest / "label.png")
        print("shannon crop", name)
    print("DONE")


if __name__ == "__main__":
    main()
