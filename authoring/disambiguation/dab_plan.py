#!/usr/bin/env python3
"""Plan the disambiguation of shared card titles (SWCCG Wiki:Disambiguation).

    python3 dab_plan.py SCAN.json OUTDIR "Jawa" "Tatooine: Cantina" ...

SCAN.json: every card page with page/title/side/set/uid/image/prev/next (scan of the live wiki).
Writes OUTDIR/ops.jsonl (moves, then decision pages, then hatnotes, then relinked pages), OUTDIR/pages/*.wiki,
OUTDIR/report.md (new names, unresolved links). Nothing is sent to the wiki.

Naming (Bill 2026-10-15): bare title = decision page; each card gets (Side) when the cards span both sides and
(Set) when two cards share a side. Text-state pages ((Original)/(Errata)/(PC Errata)) and (AI) pages follow
their card. Links are resolved from the card image (CardLink), the card page's own set/side/uid, or the deck's side.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
from collections import defaultdict
from pathlib import Path

API = "https://wiki.swccg.com/api.php"
STATE = re.compile(r" \((Original|Errata|PC Errata|AI)\)$")
SHORT = {"Premiere Limited": "Premiere", "A New Hope Limited": "A New Hope", "Hoth Limited": "Hoth",
         "Dagobah Limited": "Dagobah", "Cloud City Limited": "Cloud City", "Jabba's Palace Limited": "Jabba's Palace",
         "Reflections III: A Collector's Bounty": "Reflections III"}


def api(**p) -> dict:
    q = urllib.parse.urlencode({**p, "format": "json", "formatversion": "2"})
    with urllib.request.urlopen(API + "?" + q, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def norm(t: str) -> str:
    return re.sub(r"^[•<>\s]+", "", t).replace("•", "").strip()


def set_short(s: str) -> str:
    return SHORT.get(s, re.sub(r" Limited$", "", s))


def uid_key(u: str) -> tuple:
    m = re.match(r"(\d+)_(\d+)", u or "")
    return (int(m.group(1)), int(m.group(2))) if m else (9999, 0)


def texts(titles: list[str]) -> dict[str, str]:
    out = {}
    for i in range(0, len(titles), 50):
        r = api(action="query", titles="|".join(titles[i:i + 50]), prop="revisions", rvprop="content", rvslots="main")
        for p in r["query"]["pages"]:
            if "revisions" in p:
                out[p["title"]] = p["revisions"][0]["slots"]["main"]["content"]
    return out


def backlinks(title: str) -> list[str]:
    out, cont = [], {}
    while True:
        r = api(action="query", list="backlinks", bltitle=title, bllimit="max", blnamespace="0|4|10|14", **cont)
        out += [b["title"] for b in r["query"]["backlinks"]]
        if "continue" not in r:
            return out
        cont = {"blcontinue": r["continue"]["blcontinue"]}


def plan_group(T: str, scan: list[dict]) -> dict:
    allp = [c for c in scan if norm(c["title"]) == T]
    members = [c for c in allp if not STATE.search(c["page"])]
    states = [c for c in allp if STATE.search(c["page"])]
    sides = {c["side"] for c in members}
    by_side = defaultdict(list)
    for c in members:
        by_side[c["side"]].append(c)
    for c in members:
        name = T
        if len(sides) > 1:
            name += f" ({c['side']})"
        if len(by_side[c["side"]]) > 1:
            name += f" ({set_short(c['set'])})"
        c["new"] = name
    names = [c["new"] for c in members]
    if len(set(names)) != len(names):
        raise SystemExit(f"{T}: name clash {names}")
    for s in states:  # follow the card: "X (Dark) (Original)" -> base "X (Dark)"
        base = STATE.sub("", s["page"])
        owner = next((c for c in members if c["page"] == base), None)
        s["new"] = (owner["new"] + STATE.search(s["page"]).group(0)) if owner else s["page"]
    members.sort(key=lambda c: uid_key(c["uid"]))
    return {"title": T, "members": members, "states": states}


def dab_text(g: dict, extra: str = "") -> str:
    T = g["title"]
    rows = []
    for c in g["members"]:
        also = [s["new"] for s in g["states"] if s["new"].startswith(c["new"] + " (")]
        also_txt = " · ".join(f"[[{a}|{re.search(r'\(([^()]+)\)$', a).group(1)}]]" for a in also)
        typ = c["type"] + (f" ({c['subtype']})" if c.get("subtype") else "")
        rows.append(f"|-\n| [[File:{c['image']}|80px|link={c['new']}]] || [[{c['new']}]] || [[{c['side']}]] || "
                    f"[[{c['set']}|{set_short(c['set'])}]] || {typ}" + (f" || {also_txt}" if any(
                        s['new'].startswith(m['new'] + ' (') for m in g['members'] for s in g['states']) else ""))
    has_also = any(s["new"].startswith(m["new"] + " (") for m in g["members"] for s in g["states"])
    head = "! !! Card !! Side !! Set !! Type" + (" !! Also" if has_also else "")
    see = f"\n== See also ==\n* [[Special:PrefixIndex/{T}|All titles starting with {T}]]\n"
    return (f"'''{T}''' may refer to:\n\n== Cards ==\n{{| class=\"wikitable\"\n{head}\n" + "\n".join(rows) +
            "\n|}\n" + extra + see + "\n{{Disambiguation}}\n")


HAT = re.compile(r"^\{\{(?:Hatnote|Other versions)\|.*\}\}\s*\n?", re.M)


def with_hatnote(text: str, g: dict, c: dict) -> str:
    olds = {m["page"] for m in g["members"]} | {g["title"]}
    lines = []
    for m in HAT.finditer(text[:3000]):
        h = m.group(0)
        if h.startswith("{{Other versions") or any(f"[[{o}]]" in h or f"[[{o}|" in h for o in olds - {c['page']}):
            lines.append(h)
    for h in lines:  # cross-version hatnotes are replaced by the standard one
        text = text.replace(h, "", 1)
    side = f"{c['side']} Side {set_short(c['set'])}"
    return f"{{{{Other versions|{g['title']}|{side}}}}}\n" + text.lstrip("\n")


LINK = re.compile(r"\[\[\s*([^\]|#]+?)\s*(\|[^\]]*)?\]\]")
CARDLINK = re.compile(r"\{\{CardLink\|([^|}]+)\|([^|}]+)((?:\|[^}]*)?)\}\}")
PARAM = re.compile(r"^(\|\s*(prev|next)\s*=\s*)(.*?)\s*$", re.M)


# Decipher set number -> release year (a deck cannot hold a card printed after its year)
SET_YEAR = {1: 1995, 2: 1996, 3: 1996, 4: 1997, 5: 1997, 6: 1998, 7: 1998, 8: 1998, 9: 1999, 10: 2000, 11: 2001,
            12: 2001, 13: 2001, 14: 2001}
GEMP_CACHE: dict[str, list[str]] = {}


def gemp_ids(text: str) -> list[str]:
    """Card IDs from the deck's uploaded GEMP file (exact printings)."""
    m = re.search(r"\[\[Media:([^|\]]+?\.txt)\s*\|", text)
    if not m:
        return []
    fn = m.group(1).strip()
    if fn not in GEMP_CACHE:
        try:
            ii = api(action="query", titles="File:" + fn, prop="imageinfo", iiprop="url")["query"]["pages"][0]
            with urllib.request.urlopen(ii["imageinfo"][0]["url"], timeout=60) as r:
                GEMP_CACHE[fn] = re.findall(r'blueprintId="([^"]+)"', r.read().decode("utf-8", "replace"))
        except Exception:
            GEMP_CACHE[fn] = []
    return GEMP_CACHE[fn]


def deck_year(page: str, text: str) -> int | None:
    m = re.match(r"((?:19|20)\d\d) ", page) or re.search(r"'''Published:''' [^\n]*?((?:19|20)\d\d)", text)
    return int(m.group(1)) if m else None


def resolve(text: str, page: str, groups: dict[str, dict], img2page: dict[str, str], uid2page: dict,
            card: dict | None) -> tuple[str, list[str]]:
    """Rewrite links to bare group titles where the source says which card. Card pages change only prev/next:
    game text naming a title means every card of that title, so it keeps linking the decision page.
    Returns (new_text, unresolved descriptions)."""
    unresolved = []
    deck_side = None
    m = re.search(r"\* '''Side:''' \[\[(Light|Dark)\]\]", text)
    if m:
        deck_side = m.group(1)
    is_deck = bool(deck_side) and not card
    ids = set(gemp_ids(text)) if is_deck else set()
    year = deck_year(page, text) if is_deck else None

    def pick(T: str) -> str | None:
        cands = [c for c in groups[T]["members"] if c["side"] == deck_side]
        if len(cands) > 1 and ids:
            hit = [c for c in cands if c["uid"] in ids]
            if len(hit) == 1:
                return hit[0]["new"]
        if len(cands) > 1 and year:
            def yr(c):
                n = uid_key(c["uid"])[0]
                return SET_YEAR.get(n, 2100 if n >= 100 else 0)
            cands = [c for c in cands if yr(c) <= year]
        return cands[0]["new"] if len(cands) == 1 else None

    def cl(m):
        T = m.group(1).strip()
        if T not in groups:
            return m.group(0)
        dest = img2page.get(m.group(2).strip()) or (pick(T) if is_deck else None)
        if not dest:
            unresolved.append(f"CardLink {T} ({m.group(2)})")
            return m.group(0)
        tail = m.group(3)
        if "label=" not in tail:
            tail = tail + f"|label={T}"
        return f"{{{{CardLink|{dest}|{m.group(2)}{tail}}}}}"

    text = CARDLINK.sub(cl, text)

    def pv(m):
        T = norm(m.group(3))
        if T not in groups or not card:
            return m.group(0)
        a, b = uid_key(card["uid"])
        want = f"{a}_{b - 1 if m.group(2) == 'prev' else b + 1}"
        dest = uid2page.get(want)
        if dest:
            return m.group(1) + dest
        unresolved.append(f"{m.group(2)}={T}")
        return m.group(0)

    if card:
        text = PARAM.sub(pv, text)

    def wl(m):
        T = m.group(1).strip()
        if T not in groups or not is_deck:
            return m.group(0)
        dest = pick(T)
        if not dest:
            unresolved.append(f"[[{T}]]")
            return m.group(0)
        label = m.group(2) or f"|{T}"
        return f"[[{dest}{label}]]"

    text = LINK.sub(wl, text)
    return text, unresolved


def main(argv: list[str]) -> None:
    scan = json.loads(Path(argv[1]).read_text(encoding="utf-8"))
    out = Path(argv[2])
    (out / "pages").mkdir(parents=True, exist_ok=True)
    titles = argv[3:]
    cards = [c for c in scan if c.get("card")]
    groups = {T: plan_group(T, cards) for T in titles}
    page2new = {c["page"]: c["new"] for g in groups.values() for c in g["members"] + g["states"]}
    img2page, uid2page = {}, {}
    for c in cards:
        dest = page2new.get(c["page"], c["page"])
        if c.get("image") and not STATE.search(c["page"]):
            img2page.setdefault(c["image"], dest)
        if c.get("uid") and not STATE.search(c["page"]):
            uid2page.setdefault(c["uid"], dest)
    ops, report = [], []

    def fname(t: str) -> str:
        return "pages/" + re.sub(r"[^A-Za-z0-9._-]+", "_", t)[:150] + ".wiki"

    # 1. moves (members, then text-state pages)
    for g in groups.values():
        for c in g["members"] + g["states"]:
            if c["new"] != c["page"]:
                ops.append({"op": "move", "from": c["page"], "to": c["new"]})
        report.append(f"## {g['title']}\n" + "\n".join(f"- {c['page']} → **{c['new']}** ({c['side']}, {c['set']}, {c['uid']})"
                                                        for c in g["members"] + g["states"]))
    # 2. decision pages
    for T, g in groups.items():
        f = fname(T + "__dab")
        (out / f).write_text(dab_text(g), encoding="utf-8")
        ops.append({"op": "edit", "title": T, "file": f, "summary": "Disambiguation page (SWCCG Wiki:Disambiguation)"})
    # 3. hatnotes on members (by new title; the moved page keeps its text)
    old_texts = texts([c["page"] for g in groups.values() for c in g["members"]])
    edited: dict[str, str] = {}
    for g in groups.values():
        for c in g["members"]:
            t = old_texts.get(c["page"], "")
            edited[c["new"]] = with_hatnote(t, g, c)
    # 4. relink every page that links a bare group title
    linkers = sorted({b for T in titles for b in backlinks(T)})
    lt = texts([p for p in linkers if p not in page2new])
    pagecard = {page2new.get(c["page"], c["page"]): c for c in cards}
    unresolved_all = defaultdict(list)
    for p, t in list(lt.items()) + [(k, v) for k, v in edited.items()]:
        newt, un = resolve(t, p, groups, img2page, uid2page, pagecard.get(p))
        if un:
            unresolved_all[p] += un
        if newt != t or p in edited:
            edited[p] = newt
    for p, t in edited.items():
        f = fname(p)
        (out / f).write_text(t, encoding="utf-8")
        ops.append({"op": "edit", "title": p, "file": f})
    (out / "ops.jsonl").write_text("\n".join(json.dumps(o, ensure_ascii=False) for o in ops) + "\n", encoding="utf-8")
    report.append(f"\n## Linking pages: {len(linkers)}; edited {len(edited)}; with unresolved links {len(unresolved_all)}")
    for p, u in sorted(unresolved_all.items()):
        report.append(f"- {p}: {', '.join(sorted(set(u)))[:300]}")
    (out / "report.md").write_text("\n".join(report) + "\n", encoding="utf-8")
    print(f"ops {len(ops)} (moves {sum(o['op']=='move' for o in ops)}, edits {sum(o['op']=='edit' for o in ops)}); "
          f"unresolved pages {len(unresolved_all)}")


if __name__ == "__main__":
    main(sys.argv)
