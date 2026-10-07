#!/usr/bin/env python3
"""Line-crop 2014 MPC Day 1 Barry Alperstein p01 Dark / p02 Light (2013 form)."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "encyclopedia" / "pc-2014-worlds"))
from _crop_xerox import crop_page  # noqa: E402

ROOT = Path(__file__).resolve().parent
EXTRACT = ROOT / "encyclopedia" / "pc-2014-events" / "extract"
OUT = EXTRACT / "_mpc_d1_crops"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    crop_page(EXTRACT / "mpc_d1_p01.png", OUT / "alperstein_ds", "xerox_2013")
    crop_page(EXTRACT / "mpc_d1_p02.png", OUT / "alperstein_ls", "xerox_2013")
    print("DONE")


if __name__ == "__main__":
    main()
