#!/usr/bin/env python3
"""Print ~20 lines of wrap text after each regional heading."""
from __future__ import annotations

import html as htmllib
import re
from pathlib import Path

WRAP = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2022-2024")


def text_of(p: Path) -> str:
    raw = p.read_text(encoding="utf-8", errors="replace")
    raw = re.sub(r"<script[\s\S]*?</script>", " ", raw, flags=re.I)
    raw = re.sub(r"<br\s*/?>", "\n", raw, flags=re.I)
    raw = re.sub(r"</p>", "\n", raw, flags=re.I)
    raw = re.sub(r"</h[1-6]>", "\n", raw, flags=re.I)
    raw = re.sub(r"<[^>]+>", " ", raw)
    raw = htmllib.unescape(raw)
    return re.sub(r"[ \t]+", " ", raw)


HEAD = re.compile(
    r"((?:Toola|Bothawui|Naboo|Coruscant|Bespin|Alderaan|Endor|Nal Hutta|Tatooine|Yavin 4|Dagobah|Kashyyyk|Corellia|Scarif|Ryloth|Ithor|Ralltiir|Hoth|Kessel)(?:\s+Regionals)?\s*\([^)]+\))",
    re.I,
)

for fn in ["2022-06-regionals.html", "2023-03-regionals.html", "2024-02-regionals.html"]:
    p = WRAP / fn
    t = text_of(p)
    print("\n========", fn, "========")
    for m in HEAD.finditer(t):
        snippet = t[m.start() : m.start() + 700]
        snippet = re.sub(r"\n+", " | ", snippet)
        print("HEAD", m.group(1).strip())
        print("  ", snippet[:500])
        print()
