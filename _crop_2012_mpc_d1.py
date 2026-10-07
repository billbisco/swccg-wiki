#!/usr/bin/env python3
"""Crop 2012 MPC Day 1 leftover Xerox (2010 form, 12 shields) into line PNGs + contacts."""
from __future__ import annotations

import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "encyclopedia" / "pc-2014-worlds"))
from _crop_xerox import crop_page  # noqa: E402

EXTRACT = ROOT / "encyclopedia" / "pc-2012-events" / "extract"
CROPS = EXTRACT / "_mpc_d1_crops"
CONTACTS = EXTRACT / "_mpc_d1_contacts"


def contact(src_dir: Path, dest: Path, keys: list[str], cols: int = 2) -> None:
    imgs = []
    for k in keys:
        p = src_dir / f"{k}.png"
        if p.exists():
            im = Image.open(p).convert("RGB")
            imgs.append((k, im))
    if not imgs:
        return
    pad = 4
    label_h = 16
    cell_w = max(im.width for _, im in imgs)
    cell_h = max(im.height for _, im in imgs) + label_h
    rows = (len(imgs) + cols - 1) // cols
    canvas = Image.new("RGB", (cols * (cell_w + pad) + pad, rows * (cell_h + pad) + pad), (255, 255, 255))
    draw = ImageDraw.Draw(canvas)
    font = ImageFont.load_default()
    for i, (k, im) in enumerate(imgs):
        r, c = divmod(i, cols)
        x = pad + c * (cell_w + pad)
        y = pad + r * (cell_h + pad)
        draw.text((x, y), k, fill=(0, 0, 0), font=font)
        canvas.paste(im, (x, y + label_h))
    dest.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(dest, "PNG", optimize=True)
    print("contact", dest.name, canvas.size)


def main() -> None:
    CROPS.mkdir(parents=True, exist_ok=True)
    CONTACTS.mkdir(parents=True, exist_ok=True)
    for i in range(13, 17):
        src = EXTRACT / f"mpc_d1_p{i:02d}.png"
        dest = CROPS / f"p{i:02d}"
        crop_page(src, dest, "xerox_2010")
        left = [f"L{n:02d}" for n in range(1, 41)]
        right = [f"R{n:02d}" for n in range(41, 61)]
        shields = [f"S{n:02d}" for n in range(1, 13)]
        contact(dest, CONTACTS / f"p{i:02d}_L.png", left, cols=1)
        contact(dest, CONTACTS / f"p{i:02d}_R.png", right, cols=1)
        contact(dest, CONTACTS / f"p{i:02d}_S.png", shields, cols=1)


if __name__ == "__main__":
    main()
