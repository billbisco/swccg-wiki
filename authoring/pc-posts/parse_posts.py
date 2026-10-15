#!/usr/bin/env python3
"""Parse 2015 PC WordPress deck posts (Wayback raw HTML) into deck dicts.

python3 parse_posts.py <html_dir> <cdx_dir> <out.json>
Each deck: slug, url, wayback, post_title, lines(raw), side, cards[(qty,name,v)], shields[...], notes[]
"""
import html as H, json, re, sys
from pathlib import Path

HEAD = re.compile(r"^([A-Za-z’' &/-]+?)\s*(?:\(\s*\d+\s*\))?\s*:\s*(?:\([^)]*\))?\s*$")
SHIELD_HEADS = {"defensive shields", "defensive shield", "shields"}
BARE_HEADS = {"starting", "locations", "location", "characters", "character", "starships", "starship", "vehicles", "vehicle",
              "weapons", "weapon", "devices", "device", "weapons/devices", "effects", "effect", "interrupts", "interrupt",
              "admiral's orders", "admiral's order", "admirals' orders", "epic events", "epic event", "creatures", "creature",
              "jedi tests", "jedi test", "record", "admirals order", "admirals orders"} | SHIELD_HEADS


def post_body(raw: str) -> tuple[str, str]:
    t = re.search(r"<title>(.*?)</title>", raw, re.S)
    title = H.unescape(t.group(1)).split(" | ")[0].strip() if t else ""
    m = re.search(r'class="entry-content"[^>]*>([\s\S]*?)(?:<div class="sharedaddy|<footer|</article>)', raw)
    c = m.group(1) if m else raw
    c = re.sub(r"(?i)<br\s*/?>|</p>|</li>|</h\d>|</div>", "\n", c)
    c = H.unescape(re.sub(r"<[^>]+>", "", c)).replace("\xa0", " ")
    c = c.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    lines = [re.sub(r"\s+", " ", l).strip() for l in c.splitlines()]
    return title, [l for l in lines if l and not l.lower().startswith(("share this", "facebook", "twitter"))]


def split_item(line: str):
    s = re.sub(r"[\u200b-\u200f\u2060\ufeff]", "", line).strip().lstrip("•*-").rstrip("*").strip()
    q = 1
    m = (re.search(r"\s*[x×]\s*(\d+)\s*$", s, re.I) or re.search(r"\s*\((?:x\s*)?(\d+)\)\s*$", s, re.I)
         or re.search(r"\s*\((\d+)\s*x\)\s*$", s, re.I))
    if m:
        q = int(m.group(1)); s = s[: m.start()].strip()
    else:
        m = re.match(r"^(\d+)\s*[x×]?\s+(.+)$", s, re.I)
        if m:
            q = int(m.group(1)); s = m.group(2).strip()
    s = re.sub(r"\s*\(\s*\+[^)]*\)\s*", " ", s).strip()      # "(+3 effects)", "(+Defensive Shields)"
    v = False
    if re.search(r"\(\s*v\s*\)\s*$", s, re.I) or re.search(r"\s+v$", s):
        v = True
        s = re.sub(r"\s*\(\s*v\s*\)\s*$", "", s, flags=re.I)
        s = re.sub(r"\s+v$", "", s)
    s = re.sub(r"\s*\(\d+(?:st|nd|rd|th)\s+marker\)", "", s, flags=re.I)
    s = re.sub(r"(?<=\S)/(?=\S)", " / ", s)
    s = s.rstrip("*").strip()
    return q, s, v


def parse(path: Path, force_start: bool = False):
    raw = path.read_text(encoding="utf-8", errors="replace")
    title, lines = post_body(raw)
    m = re.search(r"\b(DS|LS)\b", title)
    side = m.group(1) if m else None
    cards, shields, notes, head, starting = [], [], [], None, []
    started = False
    if force_start:
        m2 = re.search(r'class="entry-content[^"]*"[^>]*>', raw)
        if m2:
            _t, lines = post_body(raw[:m2.start()] + '<div class="entry-content">' + raw[m2.end():])
            lines = [l for l in lines if not re.search(r"\b20\d\d\b|^day \d", l, re.I)]
        started, head = True, "unknown"
    for l in lines:
        h = HEAD.match(l) or re.match(r"^[\[{]\s*([A-Za-z’' &/-]+?)\s*[\]}]\s*$", l)
        bare = re.sub(r"\s*\([^)]*\)\s*$", "", l).strip().lower()
        if h or bare in BARE_HEADS:
            head = h.group(1).strip().lower() if h else bare; started = True
            if not h and re.search(r"illegible", l, re.I):
                notes.append(l)
            continue
        if not started:
            continue
        if l.lower().startswith(("this entry was posted", "posted in", "leave a")) or re.match(r"^(?:\d+\s+)?(?:replies|reply|responses?|comments?)$", l, re.I):
            break
        if head == "record" or l.startswith(("(", "+")) or re.search(r"illegible", l, re.I) or l.lower() in ("none", "n/a"):
            notes.append(l); continue
        q, name, v = split_item(l)
        if not name or len(name) > 90:
            notes.append(l); continue
        if head in SHIELD_HEADS and len(shields) >= 16:
            head = "unknown"
        (shields if head in SHIELD_HEADS else cards).append([q, name, v])
        if head and head.startswith('start'):
            starting.append([q, name, v])
    if not force_start and sum(c[0] for c in cards) < 30:
        return parse(path, force_start=True)
    return dict(post_title=title, side=side, starting=starting, cards=cards, shields=shields, notes=notes,
                header_lines=[l for l in lines[:6]])


if __name__ == "__main__":
    hdir, cdir, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
    wb = {}
    for f in cdir.glob("cdx-*.txt"):
        for line in f.read_text().split("\n"):
            if line.strip():
                ts, url = line.split()
                slug = url.rstrip("/").split("/")[-1]
                wb[slug] = (url.replace(":80/", "/").replace("http://", "https://"), f"https://web.archive.org/web/{ts}/{url}")
    decks = []
    for p in sorted(hdir.glob("*.html")):
        d = parse(p); d["slug"] = p.stem
        d["url"], d["wayback"] = wb.get(p.stem, ("", ""))
        decks.append(d)
    out.write_text(json.dumps(decks, ensure_ascii=False, indent=0))
    print(len(decks), "decks;", sum(1 for d in decks if sum(c[0] for c in d["cards"]) != 60), "not 60")
