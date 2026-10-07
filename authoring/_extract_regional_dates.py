#!/usr/bin/env python3
"""Print regional heading dates from wrap HTML."""
from __future__ import annotations

import html as htmllib
import re
from pathlib import Path

WRAP = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2022-2024")
FILES = [
    "2022-06-regionals.html",
    "2023-03-regionals.html",
    "2024-02-regionals.html",
    "2022-07-nats.html",
    "2022-04-egp.html",
    "2022-01-mpc.html",
    "2022-02-jawa.html",
    "2022-03-gempc.html",
    "2022-04-pc20.html",
    "2022-05-retro.html",
    "2022-09-euro.html",
    "2022-10-worlds.html",
    "2022-11-ocs.html",
    "2023-01-cl.html",
    "2023-02-sdso.html",
    "2023-04-nats.html",
    "2023-05-gempc.html",
    "2023-06-retro.html",
    "2023-07-worlds.html",
    "2023-08-euro.html",
    "2023-09-egp.html",
    "2023-10-ocs.html",
    "2023-11-outrider.html",
]


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
    r"((?:Toola|Bothawui|Naboo|Coruscant|Bespin|Alderaan|Endor|Nal Hutta|Tatooine|Yavin 4|Dagobah|Kashyyyk|Corellia|Scarif|Ryloth|Ithor|Ralltiir|Hoth|Kessel)\s*\([^)]+\)\s*[–—-]\s*[A-Za-z]+ \d{1,2})",
    re.I,
)

for fn in FILES:
    p = WRAP / fn
    if not p.exists():
        print("NOFILE", fn)
        continue
    t = text_of(p)
    print("\n========", fn, "========")
    title = re.search(r"\n ([^\n]{10,120})\n", t[:2500])
    # first 15 non-empty lines of content-ish
    hits = HEAD.findall(t)
    if hits:
        for h in hits:
            print(" ", h.strip())
    else:
        # date-ish lines
        for m in re.finditer(r"(January|February|March|April|May|June|July|August|September|October|November|December)[^\n]{0,40}\d{4}", t):
            print(" DATE", m.group(0)[:80])
            if m.start() > 20000:
                break
