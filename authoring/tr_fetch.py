#!/usr/bin/env python3
"""Fetch DeckTech tournament reports from Stephen Skilton's archive into
tournament-reports/decktech/<id>.json (verbatim body). Claude 2026-10-24.
  python3 tr_fetch.py <slug-or-id> ...      (ids are the dNNN suffix, e.g. d3)"""
import html, json, re, sys, urllib.request
from pathlib import Path

D = Path(__file__).parent / "tournament-reports" / "decktech"
SK = "https://www.stephenskilton.com/decktech_archives/reports/"
GH = "https://stevetotheizz0.github.io/decktech_archives/reports/"
INDEX = [l.strip().split("/")[3] for l in open(D / "index.txt") if l.strip()]

def slug_of(x):
    if x in INDEX: return x
    m = [s for s in INDEX if s.endswith(x) and re.search(r"-?" + re.escape(x) + "$", s) and re.search(r"d\d+$", s).group() == x]
    if len(m) != 1: raise SystemExit(f"{x}: {len(m)} matches")
    return m[0]

def text_of(frag):
    frag = re.sub(r"(?is)<script.*?</script>|<style.*?</style>", "", frag)
    frag = re.sub(r"(?i)<br\s*/?>\n?", "\n", frag)
    frag = re.sub(r"(?i)</p>\s*<p[^>]*>", "\n\n", frag)
    frag = re.sub(r"<[^>]+>", "", frag)
    t = html.unescape(frag).replace("\r", "")
    return "\n".join(l.rstrip() for l in t.split("\n")).strip("\n")

def fetch(slug):
    h = urllib.request.urlopen(urllib.request.Request(SK + slug + "/", headers={"User-Agent": "swccg-wiki"}), timeout=90).read().decode("utf-8", "replace")
    meta = re.search(r"(?s)Title:(.*?)<br>\s*Author:(.*?)<br>\s*Date:(.*?)<br>\s*</b></p>(.*?)<div class=\"search-content\">", h)
    if not meta: raise SystemExit(f"{slug}: layout not recognised")
    body = re.sub(r"(?s)\s*</div>\s*$", "", meta.group(4).rstrip())
    rid = re.search(r"d(\d+)$", slug).group()
    d = {"source": "decktech", "id": rid, "slug": slug, "url": SK + slug + "/", "mirror": GH + slug + "/",
         "posted_title": html.unescape(meta.group(1)).strip(), "byline": html.unescape(meta.group(2)).strip(),
         "date": html.unescape(meta.group(3)).strip(), "body": text_of(body)}
    f = D / f"{rid}.json"
    if f.exists():  # keep finished fields; refresh only the fetched ones
        old = json.loads(f.read_text(encoding="utf-8")); old.update(d); d = old
    f.write_text(json.dumps(d, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return rid, len(d["body"])

if __name__ == "__main__":
    for x in sys.argv[1:]:
        print(*fetch(slug_of(x)))
