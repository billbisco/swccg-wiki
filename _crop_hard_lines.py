#!/usr/bin/env python3
"""Crop individual Xerox line rows for hard handwriting."""
from __future__ import annotations

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "encyclopedia" / "pc-2013-events" / "extract"
OUT = SRC / "_strips" / "worlds" / "lines"
OUT.mkdir(parents=True, exist_ok=True)

# Approximate Xerox 2010 form: header ~15.5%, lines 1-40 left, 41-60 right.
# Empirically from 1530x1980 pages used in this event.


def line_box(w: int, h: int, n: int) -> tuple[int, int, int, int]:
    """Return crop box for card-title line n (1-60)."""
    top0 = int(h * 0.168)
    bot40 = int(h * 0.755)
    row_h = (bot40 - top0) / 40
    if n <= 40:
        y1 = int(top0 + (n - 1) * row_h)
        y2 = int(top0 + n * row_h) + 4
        return (0, y1, int(w * 0.54), y2)
    n2 = n - 40
    y1 = int(top0 + (n2 - 1) * row_h)
    y2 = int(top0 + n2 * row_h) + 4
    return (int(w * 0.46), y1, w, y2)


JOBS = {
    "d2_p09": [
        9, 10, 12, 17, 28, 33, 36, 38, 41, 46, 47, 53, 55, 56, 59,
    ],
    "d2_p03": list(range(1, 61)),
    "d2_p04": list(range(1, 61)),
    "d1_p07": list(range(1, 61)),
    "d1_p08": list(range(1, 61)),
}


def main() -> None:
    mapping = {
        "d2_p09": SRC / "worlds_d2_p09.png",
        "d2_p03": SRC / "worlds_d2_p03.png",
        "d2_p04": SRC / "worlds_d2_p04.png",
        "d1_p07": SRC / "worlds_d1_p07.png",
        "d1_p08": SRC / "worlds_d1_p08.png",
    }
    for key, lines in JOBS.items():
        im = Image.open(mapping[key])
        w, h = im.size
        dest_dir = OUT / key
        dest_dir.mkdir(parents=True, exist_ok=True)
        for n in lines:
            box = line_box(w, h, n)
            im.crop(box).save(dest_dir / f"l{n:02d}.png")
        print(key, im.size, "n", len(lines))
    print("DONE", OUT)


if __name__ == "__main__":
    main()
