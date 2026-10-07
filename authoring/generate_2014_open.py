#!/usr/bin/env python3
"""2014 post-reset Open events from typed PC HTML wrap lists.

Philadelphia Premiere, European Championship Reset Beta, Worlds Reset Beta.
Format is [[Open]] (current-virtual dests), not [[Legacy Open]].
"""
from __future__ import annotations

import html as htmlmod
import re
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2015_2016 as g15  # noqa: E402
import generate_2019_2021 as g19  # noqa: E402
import generate_2026_remaining as g26  # noqa: E402
import update_gempc_start_fields as ug  # noqa: E402
from generate_2026_sdso import load_bp_simple, wiki_fname  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
HTML = ROOT / "encyclopedia" / "pc-2014-events" / "html"
TDL = ROOT / "encyclopedia" / "pc-2014-events" / "legacy-deck-inv" / "tdl.html"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
EC = PAGES / "European_Championships.wiki"
TSV = ROOT / "y2014-open-titles.tsv"
PC = "https://www.starwarsccg.org/resources/tournament-decklists/"

g15.CANON.update(
    {
        "Jarad Konkster": "Jarad Konsker",
        "Vikrim Bali": "Vikram Bali",
        "Andrew Bolletino": "Andrew Bollentino",
        "Floris DeVries": "Floris de Vries",
        "Floris de Vries": "Floris de Vries",
        "Case Anis": "Casey Anis",
        "Jon Holtet": "Jon Benkert Holtet",
        "Pär Birgander": "Pär Birgander",
        "Par Birgander": "Pär Birgander",
        "Enno Fred Haede": "Enno Fred Haede",
        "Nico Oster": "Nico Oster",
        "Paul McPherson": "Paul McPherson",
        "David Destefanis": "David Destefanis",
        "Keith Brown": "Keith Brown",
        "Jake Nelson": "Jake Nelson",
        "Tom Hollingworth": "Tom Hollingworth",
        "Brian Bolletta": "Brian Bolletta",
        "Norman Lansing": "Norman Lansing",
        "Nicholas Tobin": "Nicholas Tobin",
        "Greg Zinn": "Greg Zinn",
        "James Booker": "James Booker",
        "Ross Littauer": "Ross Littauer",
        "Tim Simon": "Tim Simon",
        "Anthony Natale": "Anthony Natale",
        "Phil Zhang": "Phil Zhang",
        "Cole Lepine": "Cole Lepine",
        "Chris Twigg": "Chris Terwilliger",
        "Matt H-T": "Matthew Harrison-Trainor",
        "Matt H-T.": "Matthew Harrison-Trainor",
        "Stephen Skilton": "Steve Skilton",
        "Steve Skilton": "Steve Skilton",
        "David Destefanis DDM": "David Destefanis",
        "David Destefanis": "David Destefanis",
    }
)

URL_OBJ = {
    "profit": "You Can Either Profit By This",
    "proft": "You Can Either Profit By This",
    "careful-planning": "Careful Planning (V)",
    "combat-readiness": "Combat Readiness (V)",
}

EVENTS = [
    {
        "key": "philly",
        "accordion": "2014 Philadelphia Premiere Event Decklists",
        "title": "2014 Philadelphia Premiere Event",
        "year": "2014",
        "tag": "2014-10-03",
        "dates": "3–5 October 2014",
        "site": "Philadelphia, Pennsylvania",
        "format": "[[Open]]",
        "winner": "Chris Gogolen",
        "pc": PC,
        "deck_prefix": "2014 Philadelphia Premiere",
        "list_label": "Philadelphia Premiere Event",
        "stage": "d1",
        "stage_lab": "Results",
        "lead": (
            "'''2014 Philadelphia Premiere Event''' was a Players Committee constructed "
            "event in Philadelphia, Pennsylvania, 3–5 October 2014, using the post-reset "
            "virtual pool ([[Open]]). [[Chris Gogolen]] finished 1st."
        ),
    },
    {
        "key": "eurobeta",
        "accordion": "2014 European Championship Beta Reset Event Decklists",
        "title": "2014 European Championship Reset Beta",
        "year": "2014",
        "tag": "2014-09-12",
        "dates": "12–14 September 2014",
        "site": "—",
        "format": "[[Open]]",
        "winner": "Cedrik Vanderhaegen",
        "pc": PC,
        "deck_prefix": "2014 European Championship Reset Beta",
        "list_label": "European Championship Reset Beta",
        "stage": "d1",
        "stage_lab": "Results",
        "lead": (
            "'''2014 European Championship Reset Beta''' was a post-reset ([[Open]]) side "
            "event at the 2014 European Championship, 12–14 September 2014. "
            "[[Cedrik Vanderhaegen]] finished 1st. The main European Championship that "
            "weekend used the pre-reset pool; [[Casper Jørgensen]] is the published "
            "European Champion for 2014."
        ),
    },
    {
        "key": "worldsbeta",
        "accordion": "2014 Worlds Beta Reset Event Decklists",
        "title": "2014 World Championship Reset Beta",
        "year": "2014",
        "tag": "2014-08-21",
        "dates": "21–24 August 2014",
        "site": "Toronto, Ontario",
        "format": "[[Open]]",
        "winner": "Keith Brown",
        "pc": PC,
        "deck_prefix": "2014 Worlds Reset Beta",
        "list_label": "World Championship Reset Beta",
        "stage": "d1",
        "stage_lab": "Results",
        "lead": (
            "'''2014 World Championship Reset Beta''' was a post-reset ([[Open]]) side "
            "event at the [[2014 World Championship]] in Toronto, Ontario, 21–24 August "
            "2014. [[Keith Brown]] finished 1st. The main championship used [[Legacy Open]]."
        ),
    },
]


def slug_url(url: str) -> str:
    s = unquote(url.rstrip("/").split("/")[-1])
    return re.sub(r"[^a-zA-Z0-9._-]+", "-", s)[:180]


def find_html(url: str) -> Path | None:
    name = slug_url(url) + ".html"
    p = HTML / name
    if p.exists():
        return p
    # /wp/ vs public permalink
    alt = name.replace("philadelphia-premier-event", "philadelphia-premiere-event")
    p2 = HTML / alt
    if p2.exists():
        return p2
    hits = list(HTML.glob("*" + slug_url(url)[-40:] + ".html"))
    return hits[0] if len(hits) == 1 else None


def parse_accordion() -> dict[str, list[dict]]:
    raw = TDL.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'\[wc_toggle title="2014"[\s\S]*?\[/wc_toggle\]', raw)
    body = m.group(0) if m else raw
    out: dict[str, list[dict]] = {}
    for meta in EVENTS:
        sm = re.search(
            rf'\[wc_accordion_section title="{re.escape(meta["accordion"])}"\]([\s\S]*?)\[/wc_accordion_section\]',
            body,
        )
        if not sm:
            print("NOACC", meta["key"])
            out[meta["key"]] = []
            continue
        rows = []
        for line in sm.group(1).splitlines():
            line = htmlmod.unescape(line)
            hrefs = re.findall(r'href="([^"]+)"', line)
            titles = re.findall(r'title="([^"]+)"', line)
            hrefs = [h.split("#")[0].rstrip("/") + "/" for h in hrefs if "starwarsccg.org" in h]
            if len(hrefs) < 2:
                continue
            text = re.sub(r"<[^>]+>", " ", line)
            text = re.sub(r"\s+", " ", text).strip()
            place = None
            pm = re.match(
                r"^(?:(\d+)(?:st|nd|rd|th)?\s*place|(\d+)\.)\s*",
                text,
                re.I,
            )
            if pm:
                place = int(pm.group(1) or pm.group(2))
                text = text[pm.end() :].lstrip(" -–—")
            player_part = re.split(r"\s+--\s+", text, maxsplit=1)[0]
            player_part = re.split(r"\s+[–—]\s+", player_part, maxsplit=1)[0]
            player_part = player_part.strip(" -")
            player_part = re.sub(r"\s+[A-Z]{2,8}$", "", player_part).strip()
            player = g15.canon(player_part)
            ds_url = ls_url = None
            for h, t in zip(hrefs, titles + [""] * len(hrefs)):
                blob = (h + " " + t).lower()
                if re.search(r"(^|-)ls(-|$)|light", blob) and ls_url is None:
                    ls_url = h
                elif re.search(r"(^|-)ds(-|$)|dark", blob) and ds_url is None:
                    ds_url = h
            if ds_url is None:
                ds_url = hrefs[0]
            if ls_url is None and len(hrefs) > 1:
                ls_url = hrefs[1]
            if player.lower() in ("ds", "ls") or " " not in player:
                # Anthony Natale DS URL has no name in slug; keep accordion name.
                pass
            rows.append(
                {
                    "player": player,
                    "place": place,
                    "ds_url": ds_url,
                    "ls_url": ls_url,
                }
            )
        out[meta["key"]] = rows
        print("acc", meta["key"], len(rows))
    return out


def clean_card(title: str) -> str | None:
    t = title.strip()
    t = re.sub(r"\s*\(\+[^)]*\)\s*$", "", t)
    t = t.replace("’", "'")
    if not t or t.lower() in {
        "shields not listed",
        "record:",
        "record",
        "starting:",
        "starting",
    }:
        return None
    if t.lower().startswith(("home ", "posted", "skip to")):
        return None
    return t


def parse_one(path: Path, bp, by_title):
    counts, cards = g19.parse_html_deck(path, bp, by_title)
    cleaned = []
    for cid, title, tag in cards:
        t = clean_card(title)
        if not t:
            continue
        cleaned.append((cid, t, tag))
    return g19.enrich(cleaned, bp, by_title)


def write_hub(meta, players, dest, dt, hl) -> None:
    bits = ['{| class="wikitable sortable"', "! Place !! Player !! Dark !! Light"]
    for i, p in enumerate(players, 1):
        rec = dest.get(p) or {}
        fin = rec.get("place") or i
        ds_page = dt.get((p, "DS"))
        ls_page = dt.get((p, "LS"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        bits += ["|-", f"| {fin} || [[{p}]] || {ds} || {ls}"]
    bits.append("|}")
    tbl = "\n".join(bits)
    body = f"""{meta["lead"]}<ref name="pc">{PC}</ref>

== Format ==

* '''Environment:''' {meta["format"]}
* '''Site:''' {meta["site"]}
* '''Dates:''' {meta["dates"]}
* '''Winner:''' [[{meta["winner"]}]]

== {meta["stage_lab"]} ==

Published constructed lists (every published pair, not Top 8 only).

{tbl}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Open]]
* [{PC} PC tournament decklists]

== Sources ==

* [{PC} Tournament Decklists], starwarsccg.org

{g19.refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:{meta["year"]}]]
"""
    if meta["key"] == "eurobeta":
        body = body.replace(
            "* [[List of SWCCG tournaments]]",
            "* [[List of SWCCG tournaments]]\n* [[European Championships]]",
        )
    if meta["key"] == "worldsbeta":
        body = body.replace(
            "* [[List of SWCCG tournaments]]",
            "* [[2014 World Championship]]\n* [[List of SWCCG tournaments]]",
        )
    (PAGES / wiki_fname(meta["title"])).write_text(
        body.replace("\r\n", "\n"), encoding="utf-8", newline="\n"
    )


def patch_list() -> None:
    text = LIST.read_text(encoding="utf-8")
    block = """== 2014 ==

{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
|- 
| 2014-10-03 || [[2014 Philadelphia Premiere Event|Philadelphia Premiere Event]] || 3–5 October 2014 || Philadelphia, Pennsylvania || [[Open]] || [[Chris Gogolen]]
|- 
| 2014-09-12 || [[2014 European Championship Reset Beta|European Championship Reset Beta]] || 12–14 September 2014 || — || [[Open]] || [[Cedrik Vanderhaegen]]
|- 
| 2014-08-21 || [[2014 World Championship Reset Beta|World Championship Reset Beta]] || 21–24 August 2014 || Toronto, Ontario || [[Open]] || [[Keith Brown]]
|- 
| 2014-08-21 || [[2014 World Championship|World Championship]] || 21–24 August 2014 || Toronto, Ontario || [[Legacy Open]] || [[Emil Wallin]]
|- 
| 2014-01-24 || [[2014 Match Play Championship|Match Play Championship]] || 24–26 January 2014 || — || [[Legacy Open]] || —
|}

"""
    text = re.sub(r"\n== 2014 ==.*?(?=\n== )", "\n" + block, text, count=1, flags=re.S)
    LIST.write_text(text, encoding="utf-8", newline="\n")


def patch_ec() -> None:
    if not EC.exists():
        return
    t = EC.read_text(encoding="utf-8")
    old = "| 2014 || 2014 European Championship || — || — || [[Casper Jørgensen]]"
    new = (
        "| 2014 || 2014 European Championship || — || [[Legacy Open]] || [[Casper Jørgensen]]\n"
        "|-\n"
        "| 2014 || [[2014 European Championship Reset Beta]] || — || [[Open]] || [[Cedrik Vanderhaegen]]"
    )
    if old in t and "2014 European Championship Reset Beta" not in t:
        t = t.replace(old, new, 1)
    if "* [[2014 European Championship Reset Beta]]" not in t:
        t = t.replace(
            "* [[List of SWCCG tournaments]]",
            "* [[2014 European Championship Reset Beta]]\n* [[List of SWCCG tournaments]]",
            1,
        )
    EC.write_text(t, encoding="utf-8", newline="\n")


def patch_worlds_hub() -> None:
    path = PAGES / "2014_World_Championship.wiki"
    if not path.exists():
        return
    t = path.read_text(encoding="utf-8")
    if "2014 World Championship Reset Beta" in t:
        return
    t = t.replace(
        "* [[Legacy Open]]",
        "* [[2014 World Championship Reset Beta]]\n* [[Legacy Open]]",
        1,
    )
    path.write_text(t, encoding="utf-8", newline="\n")


def main() -> None:
    STUBS.mkdir(parents=True, exist_ok=True)
    HTML.mkdir(parents=True, exist_ok=True)
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    by_id, by_title = load_bp_simple()
    acc = parse_accordion()
    titles: list[tuple[str, str]] = []
    thin = []

    for meta in EVENTS:
        rows = acc.get(meta["key"]) or []
        players = []
        dest = {}
        dt, hl = {}, {}
        for row in rows:
            p = row["player"]
            if g19.is_junk_player(p) or p.lower() in {"unnamed", "ds", "ls"}:
                continue
            if p not in players:
                players.append(p)
            dest.setdefault(p, {"place": row["place"]})
            if row["place"] and not dest[p].get("place"):
                dest[p]["place"] = row["place"]
            for side, url in (("DS", row["ds_url"]), ("LS", row["ls_url"])):
                if not url:
                    continue
                path = find_html(url)
                if not path:
                    print("NOHTML", side, p, url)
                    continue
                try:
                    counts, cards = parse_one(path, bp, by_title)
                except Exception as e:
                    print("BADHTML", path.name, e)
                    continue
                n = sum(counts.values())
                if n < 10:
                    thin.append((path.name, n))
                    print("THIN", path.name, n)
                    continue
                inferred = g19.side_from_cards(cards, by_id, by_title)
                use_side = inferred or side
                obj = None
                for _cid, title, tag in cards:
                    if tag != "card":
                        continue
                    rec = by_title.get((title or "").lower()) or {}
                    if (rec.get("cat") or "").upper() == "OBJECTIVE":
                        obj = title.split("/")[0].strip()
                        break
                obj = g19.hub_obj_from_cards(
                    cards, bp, dests, title_map, by_title, obj or "constructed", use_side
                )
                slug = slug_url(url).lower()
                if not obj or obj.lower() in {"constructed", "unknown", ""}:
                    for key, printed in URL_OBJ.items():
                        if key in slug:
                            obj = printed
                            break
                    else:
                        mapped = g19.slang_obj(slug.split("-")[-1] if slug else "")
                        if mapped and mapped.lower() not in {"constructed", slug.split("-")[-1]}:
                            obj = mapped
                obj = (obj or "constructed").replace("(v)", "(V)")
                pub = url.replace("/wp/", "/")
                title, hub_lab = g19.emit_deck(
                    meta,
                    p,
                    False,
                    use_side,
                    obj,
                    meta["stage"],
                    counts,
                    cards,
                    "",
                    None,
                    bp,
                    dests,
                    title_map,
                    pc_url=pub,
                )
                dpath = PAGES / wiki_fname(title)
                body = dpath.read_text(encoding="utf-8")
                body = body.replace("* '''Stage:''' Day 1", "* '''Stage:''' Results")
                body = re.sub(r"\(v\)", "(V)", body)
                if "* '''Starting Card:''' —" in body:
                    start = obj.split("/")[0].strip()
                    if start and start.lower() not in {"constructed", "unknown"}:
                        body = body.replace(
                            "* '''Starting Card:''' —",
                            f"* '''Starting Card:''' [[{start}]]",
                            1,
                        )
                if "== Deck info ==" in body and not body.startswith("'"):
                    lead = (
                        f"'''{title}''' was the "
                        f"{'Dark' if use_side == 'DS' else 'Light'} Side constructed list "
                        f"played by [[{p}]] at [[{meta['title']}]].\n\n"
                    )
                    body = lead + body
                dpath.write_text(body, encoding="utf-8", newline="\n")
                dt[(p, use_side)] = title
                hl[title] = hub_lab
                titles.append((title, f"pages/{wiki_fname(title)}"))
        # fill missing place numbers in accordion order
        n = 0
        for p in players:
            if dest[p].get("place"):
                n = dest[p]["place"]
            else:
                n += 1
                dest[p]["place"] = n
        write_hub(meta, players, dest, dt, hl)
        titles.append((meta["title"], f"pages/{wiki_fname(meta['title'])}"))
        for p in players:
            ds_page = dt.get((p, "DS"))
            ls_page = dt.get((p, "LS"))
            ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
            ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
            fin = dest[p].get("place") or "—"
            row = (
                f"|- \n| {meta['dates']} || [[{meta['title']}]] || {meta['format']} "
                f"|| {fin} || {ds} || {ls}"
            )
            got = g15.upsert_player(p, [row], meta)
            if got:
                titles.append(got)
        print("hub", meta["title"], "players", len(players), "decks", sum(1 for p in players for s in ("DS", "LS") if (p, s) in dt))

    patch_list()
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    patch_ec()
    if EC.exists():
        titles.append(("European Championships", "pages/European_Championships.wiki"))
    patch_worlds_hub()
    wpath = PAGES / "2014_World_Championship.wiki"
    if wpath.exists():
        titles.append(("2014 World Championship", "pages/2014_World_Championship.wiki"))

    seen = {}
    ordered = []
    for title, rel in titles:
        if title in seen:
            ordered[seen[title]] = (title, rel)
        else:
            seen[title] = len(ordered)
            ordered.append((title, rel))
    TSV.write_text(
        "".join(f"{t}\t{r}\n" for t, r in ordered), encoding="utf-8", newline="\n"
    )
    print("tsv", TSV, "n", len(ordered), "thin", len(thin))


if __name__ == "__main__":
    main()
