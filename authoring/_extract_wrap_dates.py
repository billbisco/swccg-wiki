#!/usr/bin/env python3
"""Pull titles, forum links, and date-ish text from local PC wrap HTML."""
from __future__ import annotations

import re
from html.parser import HTMLParser
from pathlib import Path

WRAP = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2022-2024")
OUT = Path(__file__).resolve().parent / "_wrap_date_extract.txt"

DATE_RE = re.compile(
    r"(?i)("
    r"\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|"
    r"aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
    r"\.?\s+\d{1,2}(?:\s*[–\-]\s*\d{1,2})?(?:,?\s+\d{4})?"
    r"|"
    r"\b\d{1,2}\s*[–\-]\s*\d{1,2}\s+"
    r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|"
    r"aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
    r"(?:,?\s+\d{4})?"
    r"|"
    r"\b(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|"
    r"aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
    r"\s*[–\-]\s*"
    r"(?:jan(?:uary)?|feb(?:ruary)?|mar(?:ch)?|apr(?:il)?|may|june?|july?|"
    r"aug(?:ust)?|sept?(?:ember)?|oct(?:ober)?|nov(?:ember)?|dec(?:ember)?)"
    r"(?:\s+\d{4})?"
    r")"
)
FORUM_RE = re.compile(r"https?://forum\.starwarsccg\.org/viewtopic\.php\?[^\"'\s<>]+", re.I)
TITLE_RE = re.compile(r"<title>(.*?)</title>", re.I | re.S)
OG_RE = re.compile(r'<meta property="og:description" content="(.*?)"', re.I | re.S)
CANON_RE = re.compile(r'<link rel="canonical" href="(.*?)"', re.I)
PUB_RE = re.compile(r'<meta property="article:published_time" content="(.*?)"', re.I)


class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.skip = 0
        self.parts: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style", "noscript", "svg"}:
            self.skip += 1

    def handle_endtag(self, tag):
        if tag in {"script", "style", "noscript", "svg"} and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if self.skip:
            return
        t = " ".join(data.split())
        if t:
            self.parts.append(t)


def visible_text(html: str) -> str:
    p = TextExtractor()
    try:
        p.feed(html)
    except Exception:
        pass
    return " ".join(p.parts)


def main() -> None:
    lines = []
    files = sorted(WRAP.glob("*.html"))
    for f in files:
        html = f.read_text(encoding="utf-8", errors="replace")
        title = TITLE_RE.search(html)
        og = OG_RE.search(html)
        canon = CANON_RE.search(html)
        pub = PUB_RE.search(html)
        forums = sorted(set(FORUM_RE.findall(html)))
        text = visible_text(html)
        # keep a slice around the article heading
        idx = text.lower().find("star wars players committee")
        snippet = text[idx : idx + 2500] if idx >= 0 else text[:2500]
        dates = DATE_RE.findall(snippet)
        uniq_dates = []
        for d in dates:
            d = " ".join(d.split())
            if d not in uniq_dates:
                uniq_dates.append(d)
        lines.append("=" * 72)
        lines.append(f"FILE {f.name}")
        lines.append(f"TITLE {title.group(1).strip() if title else ''}")
        lines.append(f"CANON {canon.group(1).strip() if canon else ''}")
        lines.append(f"PUB {pub.group(1).strip() if pub else ''}")
        lines.append(f"OG {og.group(1).strip() if og else ''}")
        lines.append("FORUM " + " | ".join(forums[:8]))
        lines.append("DATES " + " | ".join(uniq_dates[:20]))
        lines.append("SNIP " + snippet[:1200])
        lines.append("")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("wrote", OUT, "files", len(files))


if __name__ == "__main__":
    main()
