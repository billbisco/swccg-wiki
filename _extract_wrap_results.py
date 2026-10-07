#!/usr/bin/env python3
"""Pull article body, Top 8 names, and winner lines from wrap-up HTML."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2022-2024")
OUT = Path(__file__).resolve().parent / "encyclopedia" / "y2022-2024-results.txt"


def article(html: str) -> str:
    m = re.search(
        r'<article[\s\S]*?<(?:div|section)[^>]*class="[^"]*(?:entry-content|post-content)[^"]*"[\s\S]*?</(?:div|section)>',
        html,
        re.I,
    )
    chunk = m.group(0) if m else html
    chunk = re.sub(r"<script[\s\S]*?</script>", " ", chunk, flags=re.I)
    chunk = re.sub(r"<style[\s\S]*?</style>", " ", chunk, flags=re.I)
    chunk = re.sub(r"<br\s*/?>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</p>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</(?:h[1-6]|li|tr|div)>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<[^>]+>", " ", chunk)
    chunk = re.sub(r"&nbsp;", " ", chunk)
    chunk = re.sub(r"&amp;", "&", chunk)
    chunk = re.sub(r"&ndash;", "–", chunk)
    chunk = re.sub(r"[ \t]+", " ", chunk)
    chunk = re.sub(r"\n[ \t]+", "\n", chunk)
    chunk = re.sub(r"\n{3,}", "\n\n", chunk)
    return chunk.strip()


def main():
    bits = []
    for path in sorted(ROOT.glob("*.html")):
        if path.name.startswith("tdl-") or path.name == "tournaments.html":
            continue
        html = path.read_text(encoding="utf-8", errors="replace")
        body = article(html)
        bits.append(f"===== {path.name} =====")
        bits.append(body[:4500])
        bits.append("")
    OUT.write_text("\n".join(bits), encoding="utf-8")
    print("wrote", OUT, "chars", OUT.stat().st_size)


if __name__ == "__main__":
    main()
