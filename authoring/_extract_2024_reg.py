#!/usr/bin/env python3
import html as htmllib
import re
from pathlib import Path

p = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2022-2024\2024-02-regionals.html")
raw = p.read_text(encoding="utf-8", errors="replace")
# strong headings
for m in re.finditer(r"<strong>([\s\S]{5,160})</strong>", raw, re.I):
    t = re.sub(r"<[^>]+>", " ", m.group(1))
    t = htmllib.unescape(re.sub(r"\s+", " ", t)).strip()
    if re.search(r"Region|January|February|March|April|May|June|July|August|September|October|November|December|\d{4}", t, re.I):
        print(t)
