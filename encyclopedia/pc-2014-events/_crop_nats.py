#!/usr/bin/env python3
"""Crop 2014 US Nationals rasters: headers, Vince name, Eier shields."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "extract"
OUT = EXTRACT / "_nats_crops"
OUT.mkdir(parents=True, exist_ok=True)


def crop(src: Path, box, dest: Path) -> None:
    im = Image.open(src)
    im.crop(box).save(dest)
    print("crop", dest.name, dest.stat().st_size)


def main() -> None:
    # Vince name, top-right of p25
    p25 = EXTRACT / "nats_d1_p25.png"
    if p25.exists():
        im = Image.open(p25)
        w, h = im.size
        crop(p25, (int(w * 0.70), 0, w, int(h * 0.12)), OUT / "vince_name.png")
        crop(p25, (0, 0, int(w * 0.45), int(h * 0.12)), OUT / "vince_p25_hdr.png")
    p27 = EXTRACT / "nats_d1_p27.png"
    if p27.exists():
        im = Image.open(p27)
        w, h = im.size
        crop(p27, (int(w * 0.70), 0, w, int(h * 0.12)), OUT / "vince_p27_name.png")
        crop(p27, (0, 0, int(w * 0.40), int(h * 0.10)), OUT / "vince_p27_obj.png")
    # Eier handwritten shields
    p30 = EXTRACT / "nats_d1_p30.png"
    if p30.exists():
        im = Image.open(p30)
        w, h = im.size
        crop(p30, (int(w * 0.58), 0, w, h), OUT / "eier_ls_right.png")
        crop(p30, (int(w * 0.58), int(h * 0.28), w, int(h * 0.92)), OUT / "eier_ls_shields.png")
    p31 = EXTRACT / "nats_d1_p31.png"
    if p31.exists():
        im = Image.open(p31)
        w, h = im.size
        crop(p31, (int(w * 0.55), 0, w, h), OUT / "eier_ds_right.png")
    # Day 1 Xerox headers for remaining inventory
    hdr = EXTRACT / "_nats_headers"
    hdr.mkdir(parents=True, exist_ok=True)
    for i in range(1, 32):
        src = EXTRACT / f"nats_d1_p{i:02d}.png"
        if not src.exists():
            continue
        im = Image.open(src)
        w, h = im.size
        dest = hdr / f"d1_h{i:02d}.png"
        # Xerox form name box vs typed printout top
        im.crop((int(w * 0.55), 0, w, int(h * 0.18))).save(dest)
    print("headers", len(list(hdr.glob("*.png"))))
    print("DONE")


if __name__ == "__main__":
    main()
