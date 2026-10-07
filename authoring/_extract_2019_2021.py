#!/usr/bin/env python3
"""Extract H1, numbered standings, deck hrefs from fetched 2019-2021 HTML."""
from __future__ import annotations

import html as htmlmod
import re
from pathlib import Path

ROOT = Path("/tmp/pc-2019-2021")
OUT = Path("/tmp/pc-2019-2021-extract.txt")


def textify(html: str) -> str:
    html = re.sub(r"(?is)<script.*?</script>", " ", html)
    html = re.sub(r"(?is)<style.*?</style>", " ", html)
    html = re.sub(r"(?is)<br\s*/?>", "\n", html)
    html = re.sub(r"(?is)</p>", "\n", html)
    html = re.sub(r"(?is)</h[1-6]>", "\n", html)
    html = re.sub(r"(?is)</li>", "\n", html)
    html = re.sub(r"(?is)</div>", "\n", html)
    html = re.sub(r"(?s)<[^>]+>", " ", html)
    html = htmlmod.unescape(html)
    html = html.replace("\xa0", " ")
    html = re.sub(r"[ \t]+", " ", html)
    html = re.sub(r"\n{3,}", "\n\n", html)
    return html


def main() -> None:
    bits = []
    for path in sorted(ROOT.glob("*.html")):
        raw = path.read_text(encoding="utf-8", errors="replace")
        h1 = ""
        m = re.search(r"(?is)<h1[^>]*>(.*?)</h1>", raw)
        if m:
            h1 = re.sub(r"<[^>]+>", " ", m.group(1))
            h1 = re.sub(r"\s+", " ", h1).strip()
        is_404 = "Page not found" in raw or "Oops! That page" in raw
        hrefs = sorted(set(re.findall(r'https?://www\.starwarsccg\.org/[^"\'\s>]+', raw, re.I)))
        forum = sorted(set(re.findall(r'https?://forum\.starwarsccg\.org/[^"\'\s>#]+', raw, re.I)))
        body = textify(raw)
        # pull a content window around H1
        idx = body.lower().find(h1.lower()[:40]) if h1 else -1
        window = body[idx : idx + 7000] if idx >= 0 else body[2000:9000]
        numbered = re.findall(
            r"(?m)^\s*(\d{1,2})[.)]\s+([A-Z][^\n]{2,80})", window
        )
        bits.append("=" * 80)
        bits.append(f"FILE {path.name} size={path.stat().st_size} 404={is_404}")
        bits.append(f"H1 {h1}")
        bits.append("NUMBERED:")
        for n, name in numbered[:40]:
            bits.append(f"  {n}. {name.strip()}")
        bits.append("FORUM:")
        for u in forum[:12]:
            if "sid=" in u:
                continue
            bits.append("  " + u)
        bits.append("DECKISH HREFS:")
        for u in hrefs:
            low = u.lower()
            if any(
                k in low
                for k in (
                    "2019",
                    "2020",
                    "2021",
                    "ls-",
                    "ds-",
                    "light",
                    "dark",
                    "wrap",
                    "gempc",
                    "outrider",
                    "retro",
                    "jawa",
                    "ocs",
                    "regional",
                    "nationals",
                    "world",
                    "match-play",
                    "endor",
                    "texas",
                    "european",
                )
            ):
                bits.append("  " + u.rstrip("/"))
        bits.append("WINDOW:")
        bits.append(window[:4500])
        bits.append("")
    OUT.write_text("\n".join(bits), encoding="utf-8")
    print("wrote", OUT, "chars", OUT.stat().st_size)


if __name__ == "__main__":
    main()
