#!/usr/bin/env python3
"""Keep [[People]] and its letter tables (People/A … People/Z, People/0–9) in step with the wiki.

  python3 people_index_sync.py --out DIR      # writes DIR/pages/*.wiki + DIR/people.tsv (for wiki_api_apply / dtchunk)

* Existing rows are kept verbatim.
* Rows whose link is now a redirect or a missing page are dropped (merged handles such as [[Psyokid]] → Kyle Ishimaru);
  the target gets its own row if it lacks one.
* Person pages in the person categories (People, Players, Squadron Members) that have no
  row get one: sort key "Surname, Given" (handles sort by themselves), "Known for" from the page (DeckTech / GPN /
  first tournament played), years from the page's year categories.
* Counts in the page leads and the per-letter name lists on [[People]] are rebuilt from the tables.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import regen_gemp_from_wiki as R

CATS = ["People", "Players", "Squadron Members"]  # person categories only (Retro League / Players Committee hold event pages too)
LETTERS = [chr(c) for c in range(ord("A"), ord("Z") + 1)] + ["0–9"]
ROW = re.compile(r"^\| (?:data-sort-value=\"([^\"]*)\" \| )?\[\[([^\]|]+)(?:\|[^\]]*)?\]\].*$")


def sort_key(title: str) -> str:
    t = re.sub(r" \([^)]*\)$", "", title)
    parts = t.split()
    if len(parts) >= 2 and all(re.match(r"^[A-ZÀ-Þ][\w.'’-]*$", p) for p in parts) and not any(c.isdigit() for c in t):
        return f"{parts[-1]}, {' '.join(parts[:-1])}"
    return title


def letter_of(key: str) -> str:
    c = key[:1].upper()
    c = {"Á": "A", "À": "A", "Ä": "A", "É": "E", "Ö": "O", "Ü": "U", "Ñ": "N", "Ç": "C"}.get(c, c)
    return c if "A" <= c <= "Z" else "0–9"


def resolve(titles: list[str]) -> dict[str, str | None]:
    """title -> final title (itself if a page), or None if missing."""
    out = {}
    for i in range(0, len(titles), 50):
        chunk = titles[i:i + 50]
        r = R.api(action="query", titles="|".join(chunk), redirects=1)
        q = r["query"]
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        red = {n["from"]: n["to"] for n in q.get("redirects", [])}
        missing = {p["title"] for p in q["pages"] if p.get("missing")}
        for t in chunk:
            n = norm.get(t, t)
            f = red.get(n, n)
            out[t] = None if f in missing else f
    return out


def known_for(text: str) -> str:
    if "DeckTech" in text:
        return "DeckTech deck author"
    if "Game Players Network" in text:
        return "Deck lists on Game Players Network"
    m = re.search(r"== Tournament Results ==.*?\n\| [^|\n]*\|\| \[\[([^\]|]+)", text, re.S)
    if m:
        return f"Played the {m.group(1)}"
    return ""


def years(text: str) -> str:
    ys = sorted({int(y) for y in re.findall(r"\[\[Category:(19[89]\d|20[0-3]\d)\]\]", text)})
    if not ys:
        return ""
    a, b = ys[0], ys[-1]
    return f'data-sort-value="{a}{b}" | ' + (f"{a}" if a == b else f"{a}–{b}")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    out = Path(a.out)
    (out / "pages").mkdir(parents=True, exist_ok=True)
    titles = ["People"] + [f"People/{L}" for L in LETTERS]
    T = R.page_texts(titles)
    rows: dict[str, list[tuple[str, str, str]]] = {}  # letter -> [(key, link, rowtext)]
    for L in LETTERS:
        rows[L] = []
        for line in T.get(f"People/{L}", "").splitlines():
            m = ROW.match(line)
            if m:
                rows[L].append((m.group(1) or m.group(2), m.group(2), line))
    links = [r[1] for L in LETTERS for r in rows[L]]
    res = resolve(links)
    dropped, have = [], set()
    for L in LETTERS:
        keep = []
        for k, t, line in rows[L]:
            if res.get(t) == t:
                keep.append((k, t, line))
                have.add(t)
            else:
                dropped.append((t, res.get(t)))
        rows[L] = keep
    universe = []
    for c in CATS:
        universe += R.category_titles(c)
    universe = sorted(set(universe) | {f for _, f in dropped if f})
    universe = [t for t in universe if not t.startswith(("People", "List of")) and not re.match(r"^(19|20)\d\d ", t)]
    grp = T["People"].split("== Notable groups ==", 1)[-1].split("\n== ", 1)[0]  # teams and groups live there, not in the tables
    groups = set(re.findall(r"\[\[([^\]|]+)", grp)) | {"Unknown players", "Unknown Player"}
    universe = [t for t in universe if t not in groups]
    final = resolve(universe)
    new = sorted({final[t] for t in universe if final[t] and final[t] not in have})
    texts = R.page_texts(new)
    added = []
    for t in new:
        x = texts.get(t, "")
        if not x or x.lstrip().upper().startswith("#REDIRECT"):
            continue
        k = sort_key(t)
        line = f'| data-sort-value="{k}" | [[{t}]] ||  || {known_for(x)} || {years(x)}'.rstrip()
        rows[letter_of(k)].append((k, t, line))
        added.append(t)
    tsv = []
    total = 0
    namelists = {}
    for L in LETTERS:
        rs = sorted(rows[L], key=lambda r: r[0].casefold())
        total += len(rs)
        namelists[L] = " · ".join(f"[[{t}]]" for _, t, _ in rs)
        old = T.get(f"People/{L}", "")
        head, sep, rest = old.partition("! Name !! Country/region !! Known for !! Years active\n")
        tail = rest[rest.index("\n|}"):] if "\n|}" in rest else "\n|}\n"
        body = "".join(f"|-\n{r}\n" for _, _, r in rs).rstrip("\n")
        head = re.sub(r"\d[\d,]* people pages", f"{len(rs):,} people pages", head, count=1)
        new_text = head + sep + body + tail
        if new_text != old:
            fn = f"People_{'0-9' if L == '0–9' else L}.wiki"
            (out / "pages" / fn).write_text(new_text, encoding="utf-8")
            tsv.append(f"People/{L}\tpages/{fn}")
    hub = T["People"]
    hub = re.sub(r"It lists [\d,]+ people pages", f"It lists {total:,} people pages", hub, count=1)
    for L in LETTERS:
        hub = re.sub(r"(=== " + re.escape(L) + r" ===\n<small>\[\[People/" + re.escape(L) + r"\|Table for [^\]]*\]\]</small><br />\n)[^\n]*",
                     lambda m: m.group(1) + namelists[L], hub, count=1)
    if hub != T["People"]:
        (out / "pages" / "People.wiki").write_text(hub, encoding="utf-8")
        tsv.insert(0, "People\tpages/People.wiki")
    (out / "people.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    (out / "report.txt").write_text("DROPPED (redirect/missing -> target)\n" + "\n".join(f"{a} -> {b}" for a, b in dropped)
                                    + "\n\nADDED\n" + "\n".join(added) + "\n", encoding="utf-8")
    print(f"total {total}, dropped {len(dropped)}, added {len(added)}, pages {len(tsv)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
