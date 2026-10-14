#!/usr/bin/env python3
"""Pre-save style lint for wiki.swccg.com articles (SWCCG Wiki:Style guide).

Usage:
  style_lint.py "Page title"            # lint current revision, compare to previous
  style_lint.py page.wiki [--title T]   # lint a local draft; with --title, compare to live page
Exit 1 if any flag is raised.
"""
import json, re, sys, urllib.parse, urllib.request, argparse, os

API = "https://wiki.swccg.com/api.php"
BANNED = ["note", "research", "this pass", "not found", "no source", "unverified", "soft", "reportedly",
          "appears to", "appear to", "it is unclear", "unclear", "pending", "inferred", "is said to",
          "allegedly", "apparently", "possibly", "probably", "likely", "seems", "gaps", "we ", "this page",
          "this article", "see talk", "according to sources"]
BAD_HEADINGS = {"gaps", "notes", "research", "open questions", "sources", "research notes", "notes and gaps"}
CAPTION_WORDS = ["shows", "showing", "visible", "left", "right", "pictured", "depicts", "seen", "background",
                 "foreground", "top", "bottom", "behind"]
MAX_SENT = 30
MAX_CAPTION = 12

def fetch(title, n=2):
    q = urllib.parse.urlencode({"action": "query", "titles": title, "prop": "revisions", "rvprop": "content|ids",
                                "rvslots": "main", "rvlimit": n, "format": "json", "formatversion": 2})
    req = urllib.request.Request(f"{API}?{q}", headers={"User-Agent": "swccg-style-lint/1.0"})
    p = json.load(urllib.request.urlopen(req, timeout=60))["query"]["pages"][0]
    return [(r["revid"], r["slots"]["main"]["content"]) for r in p.get("revisions", [])]

def captions(t):
    out = []
    for m in re.finditer(r"\[\[(?:File|Image):[^\[\]]*?(?:\[\[[^\]]*\]\][^\[\]]*?)*\]\]", t):
        parts = re.split(r"\|(?![^\[]*\]\])", m.group(0)[2:-2])
        cap = [p for p in parts[1:] if not re.fullmatch(r"\s*(thumb|thumbnail|frame|frameless|left|right|center|none|upright[=\d.]*|\d+(x\d+)?px|alt=.*|link=.*)\s*", p)]
        if cap: out.append(cap[-1])
    for g in re.finditer(r"<gallery[^>]*>(.*?)</gallery>", t, re.S):
        for line in g.group(1).splitlines():
            if "|" in line: out.append(line.split("|", 1)[1])
    return out

def body(t):
    t = re.sub(r"<!--.*?-->", " ", t, flags=re.S)
    t = re.sub(r"<ref[^>/]*/>", " ", t)
    t = re.sub(r"<ref[^>]*>.*?</ref>", " ", t, flags=re.S)
    t = re.sub(r"<references[^>]*>.*?</references>|<references\s*/>", " ", t, flags=re.S)
    t = re.sub(r"<gallery[^>]*>.*?</gallery>", " ", t, flags=re.S)
    for _ in range(3): t = re.sub(r"\{\{[^{}]*\}\}", " ", t)
    for _ in range(3): t = re.sub(r"\[\[(?:File|Image|Category):[^\[\]]*(?:\[\[[^\]]*\]\][^\[\]]*)*\]\]", " ", t)
    # drop See also / References sections entirely
    t = re.split(r"^==\s*(?:See also|References|External links)\s*==", t, flags=re.M | re.I)[0]
    t = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\[\[([^\]]*)\]\]", r"\1", t)
    t = re.sub(r"\[https?://\S+\s([^\]]*)\]", r"\1", t)
    t = re.sub(r"'''?|<[^>]+>|^[*#:;]+", "", t, flags=re.M)
    return t

def words(t): return len(re.findall(r"[A-Za-z0-9][\w'’.-]*", re.sub(r"^=+.*?=+\s*$", "", t, flags=re.M)))

def lint(text):
    flags = []
    for h in re.findall(r"^=+\s*(.*?)\s*=+\s*$", text, re.M):
        if h.strip().lower() in BAD_HEADINGS: flags.append(f"HEADING  '{h}' is not allowed")
    for c in captions(text):
        plain = re.sub(r"\[\[[^|\]]*\|([^\]]*)\]\]|\[\[([^\]]*)\]\]", lambda m: m.group(1) or m.group(2), c)
        n = len(plain.split())
        if n > MAX_CAPTION: flags.append(f"CAPTION  {n} words (> {MAX_CAPTION}): {plain[:90]}")
        for wd in CAPTION_WORDS:
            if re.search(rf"\b{wd}\b", plain, re.I): flags.append(f"CAPTION  describes image ('{wd}'): {plain[:90]}")
    b = body(text)
    prose = re.sub(r"^=+.*?=+\s*$", "", b, flags=re.M)
    for wd in BANNED:
        for m in re.finditer(rf"\b{re.escape(wd.strip())}\b", prose, re.I):
            ctx = " ".join(prose[max(0, m.start()-50):m.end()+50].split())
            flags.append(f"BANNED   '{wd.strip()}': …{ctx}…")
    for s in re.split(r"(?<=[.!?])\s+(?=[A-Z\"'])", " ".join(prose.split())):
        n = len(s.split())
        if n > MAX_SENT: flags.append(f"LONG     {n} words: {s[:100]}…")
    return flags, words(b)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("target"); ap.add_argument("--title")
    a = ap.parse_args()
    prev = None
    if os.path.isfile(a.target):
        text = open(a.target, encoding="utf-8").read()
        if a.title:
            r = fetch(a.title, 1); prev = r[0][1] if r else None
    else:
        r = fetch(a.target, 2)
        if not r: sys.exit(f"no such page: {a.target}")
        text = r[0][1]; prev = r[1][1] if len(r) > 1 else None
    flags, n = lint(text)
    for f in flags: print(f)
    if prev is not None:
        pn = lint(prev)[1]; print(f"WORDS    body {n} (previous {pn}, {n-pn:+d})")
    else: print(f"WORDS    body {n}")
    print(f"{len(flags)} flag(s)")
    sys.exit(1 if flags else 0)

if __name__ == "__main__": main()
