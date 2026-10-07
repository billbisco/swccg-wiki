#!/usr/bin/env python3
from pathlib import Path
from PIL import Image

EXTRACT = Path(__file__).resolve().parent / "encyclopedia" / "pc-2013-events" / "extract"
OUT = EXTRACT / "_strips" / "alderaan"

jobs = [
    ("alderaan_p02.png", "p02_L23_26", (40, 1180, 780, 1380)),
    ("alderaan_p02.png", "p02_sh8_12", (760, 1380, 1490, 1680)),
    ("alderaan_p01.png", "p01_sh8_12", (760, 1380, 1490, 1680)),
    ("alderaan_p01.png", "p01_R43_46", (760, 380, 1490, 560)),
    ("alderaan_p02.png", "p02_L34_36", (40, 1480, 780, 1680)),
]

def main() -> None:
    for src_name, key, box in jobs:
        im = Image.open(EXTRACT / src_name)
        w, h = im.size
        x1, y1, x2, y2 = box
        dest = OUT / src_name.replace(".png", "")
        dest.mkdir(parents=True, exist_ok=True)
        im.crop((x1, y1, min(x2, w), min(y2, h))).save(dest / f"{key}.png")
        print("wrote", dest / f"{key}.png")

if __name__ == "__main__":
    main()
