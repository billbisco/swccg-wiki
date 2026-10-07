#!/usr/bin/env python3
"""Crop username header from transcribe files that still lack USERNAME."""
from __future__ import annotations

import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_username_crops"
MEDIA = {
    "2013 Match Play Championship.pdf": ROOT / "y2013-mpc-media",
    "2013 SoCal Grand Prix Day 1.pdf": ROOT / "y2013-socal-media",
    "2013 SoCal Grand Prix Day 2.pdf": ROOT / "y2013-socal-media",
    "2013 Texas Mini Worlds Day 1.pdf": ROOT / "y2013-tmw-media",
    "2013 World Championship Day 1.pdf": ROOT / "y2013-worlds-media",
    "2013 Alderaan Regionals.pdf": ROOT / "y2013-alderaan-media",
}
BOX_1980 = (980, 20, 1530, 250)
BOX_2103 = (980, 20, 1530, 280)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for p in sorted((ROOT / "encyclopedia" / "pc-2013-events").glob("transcribe_*.py")):
        t = p.read_text(encoding="utf-8")
        if re.search(r"^(USERNAME|LS_USERNAME|DS_USERNAME)\s*=", t, re.M):
            continue
        pdf_m = re.search(r'^PDF\s*=\s*"([^"]+)"', t, re.M)
        ls_m = re.search(r'^LS_SCAN\s*=\s*"([^"]+)"', t, re.M)
        if not pdf_m or not ls_m:
            print("NO_SCAN", p.name)
            continue
        media = MEDIA.get(pdf_m.group(1))
        if not media:
            print("NO_MEDIA", p.name, pdf_m.group(1))
            continue
        src = media / ls_m.group(1)
        if not src.exists():
            print("MISSING_FILE", src)
            continue
        im = Image.open(src)
        box = BOX_2103 if im.size[1] > 2000 else BOX_1980
        dest = OUT / (src.stem + " user.png")
        im.crop(box).save(dest)
        print("CROP", dest.name, im.size)
        n += 1
    print("n", n)


if __name__ == "__main__":
    main()
