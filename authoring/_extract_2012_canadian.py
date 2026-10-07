#!/usr/bin/env python3
"""Extract 2012 Canadian Nationals leftover Xerox rasters analog leftover Yavin."""
from __future__ import annotations

from pathlib import Path

import fitz

ROOT = Path(__file__).resolve().parent
PDF = ROOT / "encyclopedia" / "pc-2012-events" / "CanadianNationals2012Decklists.pdf"
OUT = ROOT / "encyclopedia" / "pc-2012-events" / "extract"


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(PDF)
    mat = fitz.Matrix(2.5, 2.5)
    for i, page in enumerate(doc, start=1):
        pix = page.get_pixmap(matrix=mat, alpha=False)
        dest = OUT / f"canadian_p{i:02d}.png"
        pix.save(dest)
        print("wrote", dest.name, pix.width, pix.height)
    print("pages", doc.page_count)


if __name__ == "__main__":
    main()
