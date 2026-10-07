#!/usr/bin/env python3
"""Extract 2017–2018 wrap standings, dest slang, and deck hrefs."""
from __future__ import annotations

import html as htmlmod
import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
WRAP = ROOT / "encyclopedia" / "pc-2017-2018"
OUT = ROOT / "encyclopedia" / "pc-2017-2018-extract.json"

WRAP_FILES = {
    "17worlds": "17worlds.html",
    "17euro": "17euro.html",
    "17mpc": "17mpc.html",
    "17tmw": "17tmw.html",
    "17nats": "17nats.html",
    "17egp": "17egp.html",
    "18worlds": "18worlds.html",
    "18euro": "18euro.html",
    "18nats": "18nats.html",
    "18egp": "18egp.html",
    "18mpc": "18mpc.html",
    "18eumpc": "18eumpc.html",
    "23retro": "23retro.html",
}


def wrap_visible(raw: str) -> str:
    m = re.search(r"<h1[^>]*>.*?</h1>([\s\S]+?)Posted in", raw, re.I)
    if not m:
        m = re.search(r"<h1[^>]*>.*?</h1>([\s\S]{0,40000})", raw, re.I)
    s = m.group(1) if m else raw
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p>", "\n", s, flags=re.I)
    s = re.sub(r"</h[1-6]>", "\n", s, flags=re.I)
    s = re.sub(r"<li[^>]*>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmlmod.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    return "\n".join(ln for ln in lines if not ln.startswith("{") and "function" not in ln[:18])


def hrefs(raw: str) -> list[str]:
    found = []
    seen = set()
    for h in re.findall(r'https?://(?:www\.)?starwarsccg\.org/[^"\'\s<>]+', raw, re.I):
        h = htmlmod.unescape(h).split("#")[0].rstrip("/")
        if "/wp-json" in h or "/category/" in h or "/feed" in h:
            continue
        if h not in seen:
            seen.add(h)
            found.append(h)
    return found


def heading_stage(line: str) -> str | None:
    t = re.sub(r"[–—:].*$", "", line).strip()
    t = re.sub(r"^\d+\.?\s*", "", t)
    tl = t.lower()
    if re.match(r"^day\s*3$", tl):
        return "d3"
    if re.match(r"^day\s*2$", tl):
        return "d2"
    if re.match(r"^day\s*1$", tl):
        return "d1"
    if re.match(r"^drops?$", tl):
        return "drop"
    return None


ROW = re.compile(
    r"^(?:\(?(\d{1,2})\)?[.\)]\s*)?([A-Za-z][A-Za-z .'\-éøæåüßÖöÄäÜÉØÆÅ/]+?)\s+[–—-]\s+(.+)$"
)


def parse_rows(text: str):
    stage = None
    out = defaultdict(list)
    dest = defaultdict(dict)
    for ln in text.splitlines():
        hs = heading_stage(ln)
        if hs:
            stage = hs
            continue
        if not stage:
            # unnumbered first block often Day 2 / the only list
            if " – " in ln or " — " in ln:
                stage = "list"
            else:
                continue
        m = ROW.match(ln)
        if not m:
            continue
        place, name, rest = m.groups()
        name = re.sub(r"\s+", " ", name).strip(" .")
        if name.lower() in ("day 1", "day 2", "day 3", "results", "drops"):
            continue
        parts = re.split(r"\s+[–—-]\s+", rest)
        ds = parts[0].strip() if parts else ""
        ls = parts[1].strip() if len(parts) > 1 else ""
        rec = {"place": int(place) if place else None, "name": name, "ds": ds, "ls": ls, "raw": ln}
        out[stage].append(rec)
        dest[stage][name] = (ds, ls)
    return out, dest


def accordion_sections(raw: str):
    """Pull text around 2017/2018 headings from resources-td."""
    s = re.sub(r"<script[\s\S]*?</script>", " ", raw, flags=re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p>", "\n", s, flags=re.I)
    s = re.sub(r"</h[1-6]>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmlmod.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    text = "\n".join(lines)
    keys = [
        "2017 US Nationals",
        "2017 Endor Grand Prix",
        "2017 Match Play",
        "2017 World",
        "2017 European",
        "2017 Texas",
        "2018 World",
        "2018 US Nationals",
        "2018 European Championship",
        "2018 Endor",
        "2018 Match Play",
        "2018 European Match",
        "2018 Online Championship",
        "OCS 2018",
        "2018 OCS",
    ]
    hits = {}
    for k in keys:
        i = text.lower().find(k.lower())
        if i >= 0:
            hits[k] = text[max(0, i - 80) : i + 4000]
    return hits


def main():
    data = {}
    all_hrefs = []
    seen = set()
    for key, fname in WRAP_FILES.items():
        path = WRAP / fname
        if not path.exists():
            data[key] = {"missing": True}
            continue
        raw = path.read_text(encoding="utf-8", errors="replace")
        vis = wrap_visible(raw)
        rows, dest = parse_rows(vis)
        hs = hrefs(raw)
        data[key] = {
            "size": path.stat().st_size,
            "h1": (re.search(r"<h1[^>]*>(.*?)</h1>", raw, re.I | re.S) or type("x", (), {"group": lambda *_: ""})()).group(1),
            "visible_head": vis[:1500],
            "stages": {st: recs for st, recs in rows.items()},
            "counts": {st: len(recs) for st, recs in rows.items()},
            "hrefs": [h for h in hs if re.search(r"2017|2018|worlds|nationals|endor|match-play|texas|european|mpc", h, re.I)],
        }
        for h in data[key]["hrefs"]:
            if h not in seen:
                seen.add(h)
                all_hrefs.append(h)
        print(key, data[key]["counts"], "hrefs", len(data[key]["hrefs"]))

    res = WRAP / "resources-td.html"
    if res.exists():
        acc = accordion_sections(res.read_text(encoding="utf-8", errors="replace"))
        data["resources_hits"] = {k: v[:2500] for k, v in acc.items()}
        print("resources keys", list(acc))

    cat17 = WRAP / "2017-decks.html"
    if cat17.exists():
        data["cat2017_hrefs"] = hrefs(cat17.read_text(encoding="utf-8", errors="replace"))
        print("cat2017", len(data["cat2017_hrefs"]))

    (WRAP / "deck-hrefs.txt").write_text("\n".join(all_hrefs) + "\n", encoding="utf-8")
    OUT.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
    print("wrote", OUT, "hrefs", len(all_hrefs))


if __name__ == "__main__":
    main()
