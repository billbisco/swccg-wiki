#!/usr/bin/env python3
"""Crop a larger username header from remaining transcribe scans."""
from __future__ import annotations

import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "_username_crops"
MEDIA_DIRS = [
    ROOT / "y2013-mpc-media",
    ROOT / "y2013-socal-media",
    ROOT / "y2013-tmw-media",
    ROOT / "y2013-worlds-media",
    ROOT / "y2013-alderaan-media",
    ROOT / "y2014-alderaan-media",
    ROOT / "y2014-tmw-media",
    ROOT / "y2014-nats-media",
    ROOT / "y2014-worlds-media",
]


def find_scan(name: str) -> Path | None:
    for d in MEDIA_DIRS:
        p = d / name
        if p.exists():
            return p
    return None


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    n = 0
    for p in sorted(ROOT.glob("encyclopedia/**/transcribe_*.py")):
        t = p.read_text(encoding="utf-8")
        if re.search(r"^(USERNAME|LS_USERNAME|DS_USERNAME)\s*=", t, re.M):
            continue
        scans = []
        for key in ("LS_SCAN", "DS_SCAN", "SCAN"):
            m = re.search(rf'^{key}\s*=\s*"([^"]+)"', t, re.M)
            if m and m.group(1):
                scans.append(m.group(1))
        if not scans:
            print("NO_SCAN", p.name)
            continue
        src_name = scans[0]
        src = find_scan(src_name)
        if not src:
            print("MISSING", p.name, src_name)
            continue
        im = Image.open(src)
        w, h = im.size
        box = (int(w * 0.45), 0, w, int(h * 0.22))
        dest = OUT / (src.stem + " hdr.png")
        im.crop(box).save(dest)
        print("CROP", dest.name, im.size)
        n += 1
    print("n", n)


if __name__ == "__main__":
    main()
