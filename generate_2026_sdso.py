#!/usr/bin/env python3
"""Generate 2026 San Diego Super Open hub + two-column deck pages."""
from __future__ import annotations

import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import update_gempc_start_fields as ug  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
MEDIA = ROOT / "sdso-2026-media"
DECK_ROOT = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\td-2021-2026\2026-sdso")

EVENT_TITLE = "2026 San Diego Super Open"
PC_HUB = "https://www.starwarsccg.org/2026-04-san-diego-super-open-san-diego-california-apr-11-to-12-2026/"
PC_WRAP = "https://www.starwarsccg.org/2026-san-diego-super-open-wrap-up-joe-olson-conquers/"
PC_FORUM = "https://forum.starwarsccg.org/viewforum.php?f=1592"
PC_DECKS = "https://forum.starwarsccg.org/viewtopic.php?t=86618"
YT = "https://www.youtube.com/playlist?list=PLQSFYZX0M9YTcAIe2G5fmIGbmz-M8bYNs"

FILE_PLAYER = {
    "Aasen": "Phil Aasen",
    "Amor": "Daniel Amor",
    "Baity": "Brandon Baity",
    "Billings": "Mark Billings",
    "Fred": "Brian Fred",
    "Harpster": "Steve Harpster",
    "Hatoum": "AJ Hatoum",
    "Howard": "Anthony Howard",
    "Jellison": "Ryan Jellison",
    "Kafer": "Bill Kafer",
    "Kelly": "Chris Kelly",
    "Koenig": "Karl Koenig",
    "Lavigne": "Jeff Lavigne",
    "Lutz": "Matt Lutz",
    "Miyashiro": "Justin Miyashiro",
    "Olson": "Joe Olson",
    "RScott": "Randy Scott",
    "Sersen": "Ryan Sersen",
    "Silkwood": "Blake Silkwood",
    "Smith": "Jacy Smith",
    "Swedal": "Nick Swedal",
    "Tashima": "Sam Tashima",
    "Turner": "Mike Turner",
    "Veasey": "John Veasey",
    "Wadden": "Matt Wadden",
    "Wirfs": "Chris Wirfs",
}

LEFT = [
    "CHARACTER",
    "DEVICE",
    "EFFECT",
    "EPIC_EVENT",
    "LOCATION",
    "OBJECTIVE",
    "JEDI_TEST",
    "PODRACER",
]
RIGHT = [
    "STARSHIP",
    "VEHICLE",
    "WEAPON",
    "INTERRUPT",
    "DEFENSIVE_SHIELD",
    "ADMIRAL'S_ORDER",
    "ADMIRALS_ORDER",
]
CAT_LABEL = {
    "CHARACTER": "Character",
    "DEVICE": "Device",
    "EFFECT": "Effect",
    "EPIC_EVENT": "Epic Event",
    "LOCATION": "Location",
    "OBJECTIVE": "Objective",
    "STARSHIP": "Starship",
    "VEHICLE": "Vehicle",
    "WEAPON": "Weapon",
    "INTERRUPT": "Interrupt",
    "DEFENSIVE_SHIELD": "Defensive Shield",
    "ADMIRAL'S_ORDER": "Admiral's Order",
    "ADMIRALS_ORDER": "Admiral's Order",
    "JEDI_TEST": "Jedi Test",
    "PODRACER": "Podracer",
}

# PC results page finish order (Day 1+2 combined).
PC_FINISH = [
    "Joe Olson",
    "Daniel Amor",
    "Sam Tashima",
    "Chris Wirfs",
    "Bill Kafer",
    "Chris Kelly",
    "Phil Aasen",
    "Ryan Jellison",
    "Justin Miyashiro",
    "Mike Turner",
    "Jeff Lavigne",
    "Brian Fred",
    "Ryan Sersen",
    "Nick Swedal",
    "AJ Hatoum",
    "Brandon Baity",
    "Blake Silkwood",
    "Jacy Smith",
    "John Veasey",
    "Anthony Howard",
    "Matt Lutz",
    "Karl Koenig",
    "Matt Wadden",
    "Randy Scott",
    "Steve Harpster",
    "Mark Billings",
]


def parse_filename(name: str):
    m = re.match(r"26SD D([12]) (\S+) (DS|LS) (.+)\.(txt|html)$", name)
    if not m:
        return None
    day = int(m.group(1))
    token = m.group(2)
    side = m.group(3)
    obj_short = m.group(4)
    player = FILE_PLAYER.get(token, token)
    return player, day, side, obj_short, name


def wiki_fname(title: str) -> str:
    return title.replace(" ", "_").replace("/", "_") + ".wiki"


def deck_page_title(player: str, day: int, side: str, obj_short: str) -> str:
    return f"2026 SDSO Day {day} {player} {side} {obj_short}"


def col(cat_map, cats):
    bits = []
    for cat in cats:
        items = cat_map.get(cat) or []
        if not items:
            continue
        bits.append(f"'''{CAT_LABEL.get(cat, cat.title())}'''")
        for n, title, dest in items:
            vis = ug.visible_label(title, dest)
            bits.append(f"* {n}x {ug.wiki_link(vis, dest)}")
        bits.append("")
    return "\n".join(bits).rstrip()


def render_deck(
    player,
    day,
    side,
    obj_short,
    counts,
    cards,
    media_name,
    companion,
    bp,
    dests,
    title_map,
):
    side_word = "Dark" if side == "DS" else "Light"
    title_dest, obj, ints, effs, loc_title, loc_note, has_ltww = ug.analyze(
        cards, bp, dests, title_map
    )
    if not obj and not loc_title:
        for cid, title, tag in cards:
            if tag == "card" and title == "Yavin 4: Massassi Throne Room":
                loc_title = title
                loc_note = "inferred: no Objective; Throne Room Mains start"
                break
    cat_map = defaultdict(list)
    seen = {}
    for (cat, title), n in sorted(counts.items(), key=lambda x: (x[0][0], x[0][1].lower())):
        dest = title_dest.get(title)
        cat_map[cat].append((n, title, dest))
        seen[title] = dest

    loc_line_bits = []
    if loc_title:
        ld = title_dest.get(loc_title) or loc_title
        loc_bit = ug.wiki_link(loc_title, ld if ld != loc_title else loc_title)
        if loc_note:
            loc_bit += f" <small>({loc_note})</small>"
        loc_line_bits.append(loc_bit)
    if obj:
        loc_line_bits.append(ug.link_pair(obj[0], obj[2]))
    loc_line = "* '''Starting Card:''' " + (
        " · ".join(loc_line_bits) if loc_line_bits else "—"
    )
    if ints:
        int_line = "* '''Starting Interrupt:''' " + " · ".join(
            ug.link_pair(t, d) for t, c, d in ints
        )
    else:
        int_line = "* '''Starting Interrupt:''' —"
    eff_line = None
    if effs:
        eff_line = "* '''Starting Effect:''' " + " · ".join(
            ug.link_pair(t, d) for t, c, d in effs
        )

    extra = [c for c in cat_map if c not in LEFT and c not in RIGHT]
    left = col(cat_map, LEFT)
    right = col(cat_map, RIGHT)
    extra_txt = col(cat_map, extra) if extra else ""
    if extra_txt:
        right = (right + "\n\n" + extra_txt).strip()

    title = deck_page_title(player, day, side, obj_short)
    companion_line = f"* [[{companion}]]" if companion else ""
    info = [
        f"* '''Player:''' [[{player}]]",
        f"* '''Event:''' [[{EVENT_TITLE}]]",
        f"* '''Day:''' Day {day}",
        "* '''Format:''' [[Open]]",
        f"* '''Side:''' [[{side_word}]]",
        loc_line,
        int_line,
    ]
    if eff_line:
        info.append(eff_line)
    info.append(f"* '''GEMP Importable deck:''' [[Media:{media_name}|Download]]")

    hub_label = None
    if obj:
        hub_label = ug.visible_label(obj[0], obj[2])
    else:
        strat = [t for t, c, d in ints if t not in ug.GENERIC_START]
        if strat:
            t = strat[0]
            d = next(d for x, c, d in ints if x == t)
            hub_label = ug.visible_label(t, d)
        elif loc_title:
            hub_label = loc_title
        else:
            hub_label = obj_short

    body = f"""== Deck info ==
{chr(10).join(info)}

== Decklist ==

{{| class="wikitable" style="width:100%;"
|-
| style="width:50%; vertical-align:top;" |
{left}

| style="width:50%; vertical-align:top;" |
{right}

|}}

== See also ==
* [[{EVENT_TITLE}]]
{companion_line}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:{side_word} Side decks]]
[[Category:2026]]
"""
    return title, body.replace("\r\n", "\n"), hub_label


def _cards_from_xml_text(text: str):
    import xml.etree.ElementTree as ET

    i = text.find("<?xml")
    if i < 0:
        i = text.find("<deck")
    if i >= 0:
        text = text[i:]
    j = text.find("</deck>")
    if j >= 0:
        text = text[: j + 7]
    root = ET.fromstring(text)
    cards = []
    for el in root:
        if el.tag not in ("card", "cardOutsideDeck"):
            continue
        cid = ug.norm_id(el.attrib.get("blueprintId"))
        title = (el.attrib.get("title") or "").replace("&amp;", "&")
        cards.append((cid, title, el.tag))
    return cards


def _cards_from_text_list(text: str, by_title):
    cards = []
    for m in re.finditer(r"(?i)(?:<br\s*/?>|\n|^)\s*(\d+)\s*x\s+([^<\n]+)", text):
        n = int(m.group(1))
        title = m.group(2).strip().replace("&amp;", "&")
        rec = by_title.get(title.lower())
        cid = rec["title"] if rec else title
        # blueprint unknown; keep printed title
        bp = ""
        if rec:
            # by_title values don't include id; leave empty
            bp = ""
        for _ in range(n):
            cards.append((bp, title, "card"))
    return cards


def parse_gemp_counts(path: Path, by_id, by_title):
    raw = path.read_bytes()
    if raw.startswith(b"\xef\xbb\xbf"):
        raw = raw[3:]
    text = raw.decode("utf-8", "replace")
    cards = []
    if "<deck" in text and "<card" in text:
        try:
            cards = _cards_from_xml_text(text)
        except Exception:
            cards = []
    if not cards and ("<html" in text.lower() or "1x " in text or "1X " in text):
        cards = _cards_from_text_list(text, by_title)
    if not cards:
        cards = ug.parse_xml(path)
    counts = Counter()
    for cid, title, tag in cards:
        if tag != "card":
            continue
        rec = by_id.get(cid) or by_title.get(title.lower())
        cat = rec["cat"] if rec else "UNKNOWN"
        counts[(cat, title)] += 1
    return counts, cards


def load_bp_simple():
    rows = ug.load_json(ug.BP_PATH)
    by_id = {}
    by_title = {}
    for r in rows:
        cid = str(r.get("cardId") or "")
        title = r.get("title") or ""
        cat = (r.get("cardCategory") or "UNKNOWN").upper()
        rec = {"title": title, "cat": cat, "side": r.get("side")}
        by_id[cid] = rec
        by_id[cid.replace("^", "")] = rec
        by_title[title.lower()] = rec
    return by_id, by_title


def upsert_stub(player: str, day_rows: list[str]):
    STUBS.mkdir(parents=True, exist_ok=True)
    path = STUBS / (player.replace(" ", "_") + ".wiki")
    event_link = f"[[{EVENT_TITLE}]]"
    extra_row_src = (
        f"* [{PC_HUB} 2026-04 San Diego Super Open], starwarsccg.org\n"
        f"* [{PC_WRAP} 2026 San Diego Super Open wrap-up]\n"
    )
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if EVENT_TITLE in text and "2026 SDSO Day" in text:
            return
        # insert rows after header
        if "|}" in text and "Tournament Results" in text:
            rows = "\n".join(day_rows) + "\n"
            text = text.replace("|}\n", rows + "|}\n", 1)
        if "* [[Championships]]" in text and event_link not in text.split("See also")[-1]:
            text = text.replace(
                "* [[Championships]]",
                f"* {event_link}\n* [[Championships]]",
                1,
            )
        if "== Sources ==" in text and PC_HUB not in text:
            text = text.replace("== Sources ==\n", "== Sources ==\n" + extra_row_src, 1)
        path.write_text(text, encoding="utf-8", newline="\n")
        return

    rows = "\n".join(day_rows)
    body = f"""'''{player}''' played the [[{EVENT_TITLE}]].<ref name="pc-sdso">[{PC_HUB} 2026-04 San Diego Super Open], starwarsccg.org</ref>

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
{rows}
|}}

== See also ==

* {event_link}
* [[Championships]]
* [[GEMP]]

== Sources ==

* [{PC_HUB} 2026-04 San Diego Super Open], starwarsccg.org
* [{PC_WRAP} 2026 San Diego Super Open wrap-up]

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2026]]
"""
    path.write_text(body, encoding="utf-8", newline="\n")


def hub(deck_titles, hub_labels, players_by_day):
    def cell(player, day, side):
        page = deck_titles.get((player, day, side))
        if not page:
            return "—"
        label = hub_labels.get(page, page)
        return f"[[{page}|{label}]]"

    def table(day, ordered):
        bits = [
            '{| class="wikitable sortable"',
            "! Player !! Dark !! Light",
        ]
        for p in ordered:
            bits += [
                "|-",
                f"| [[{p}]] || {cell(p, day, 'DS')} || {cell(p, day, 'LS')}",
            ]
        bits.append("|}")
        return "\n".join(bits)

    ordered = [p for p in PC_FINISH if p in players_by_day[1] or p in players_by_day[2]]
    extra = sorted(
        (players_by_day[1] | players_by_day[2]) - set(PC_FINISH)
    )
    ordered += extra

    def results_table():
        bits = [
            '{| class="wikitable sortable"',
            "! Finish !! Player !! Day 1 Dark !! Day 1 Light !! Day 2 Dark !! Day 2 Light",
        ]
        for i, p in enumerate(ordered, 1):
            bits += [
                "|-",
                f"| {i} || [[{p}]] || {cell(p, 1, 'DS')} || {cell(p, 1, 'LS')} || {cell(p, 2, 'DS')} || {cell(p, 2, 'LS')}",
            ]
        bits.append("|}")
        return "\n".join(bits)

    return f"""'''{EVENT_TITLE}''' was a Players Committee major event in San Diego, California, 10–12 April 2026 (constructed days 11–12 April). [[Joe Olson]] defeated [[Daniel Amor]] in the Final Confrontation. [[Sam Tashima]] finished third; [[Chris Wirfs]] fourth. Tournament Advocate / director: [[Chris Schoenthal]]. Streaming: [[Dan Tartaglione]] and [[Garrett Larson]]. Local organizer: [[Karl Koenig]].<ref name="pc">{PC_HUB}</ref><ref name="wrap">{PC_WRAP}</ref>

The main event is [[Open]] constructed: Day 1 Swiss plus Day 2 (ten games across the two days), then Final Confrontation. A Sunday Retro event was won undefeated by [[Eddie Szwabowski]].<ref name="wrap" />

[[File:SDSO26-banner.jpg|640px]]

[[File:SDSO26-Joe.jpg|220px|thumb|Champion [[Joe Olson]]]]

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' San Diego, California
* '''Dates:''' 10–12 April 2026
* '''Forum:''' [{PC_FORUM} 2026 San Diego Super Open Forum]
* '''GEMP importable decks:''' [{PC_DECKS} forum t=86618] (<code>2026 SDSO Day One.zip</code> / <code>2026 SDSO Day Two.zip</code>)
* '''Video:''' [{YT} YouTube playlist]

== Results ==

Finish as published on the PC results page (Day 1+2 combined). Dark/Light cells use the GEMP printed objective (or inferred start). Some players changed lists between days (Olson Day 1 Dark is My Kind Of Scum; Day 2 Dark is Endor Operations).<ref name="pc" />

{results_table()}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]] · [[GEMP]]
* [[2026 Tenth Annual GEMPC]]
* [{PC_HUB} PC results]
* [{PC_WRAP} Wrap-up]
* [{PC_DECKS} GEMP importable decks]
* [{PC_FORUM} Forum]

== Sources ==

* [{PC_HUB} 2026-04 San Diego Super Open – San Diego, California (Apr. 11 to 12, 2026)], starwarsccg.org
* [{PC_WRAP} 2026 San Diego Super Open wrap-up – Joe Olson conquers]
* [{PC_DECKS} GEMP Importable Decklist Files], forum.starwarsccg.org t=86618
* [{PC_FORUM} 2026 San Diego Super Open Forum], f=1592
* [{YT} 2026 San Diego Super Open YouTube playlist]

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
"""


def main() -> None:
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    by_id, by_title = load_bp_simple()

    MEDIA.mkdir(parents=True, exist_ok=True)
    PAGES.mkdir(parents=True, exist_ok=True)

    files = list((DECK_ROOT / "day1").glob("26SD *")) + list(
        (DECK_ROOT / "day2").glob("26SD *")
    )
    parsed = []
    for path in files:
        info = parse_filename(path.name)
        if not info:
            print("SKIP", path.name)
            continue
        player, day, side, obj_short, media_name = info
        dest = MEDIA / media_name
        shutil.copy2(path, dest)
        counts, cards = parse_gemp_counts(path, by_id, by_title)
        parsed.append((player, day, side, obj_short, media_name, counts, cards))

    deck_titles = {}
    hub_labels = {}
    players_by_day = defaultdict(set)
    companions = {}
    for player, day, side, obj_short, media_name, counts, cards in parsed:
        title = deck_page_title(player, day, side, obj_short)
        deck_titles[(player, day, side)] = title
        players_by_day[day].add(player)

    for player, day, side, obj_short, media_name, counts, cards in parsed:
        other = "LS" if side == "DS" else "DS"
        companion = deck_titles.get((player, day, other))
        title, body, hub_label = render_deck(
            player,
            day,
            side,
            obj_short,
            counts,
            cards,
            media_name,
            companion,
            bp,
            dests,
            title_map,
        )
        (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
        hub_labels[title] = hub_label
        print("deck", title, "->", hub_label)

    # stubs
    for player in sorted(set(p for p, *_ in parsed)):
        rows = []
        for day in (1, 2):
            ds = deck_titles.get((player, day, "DS"))
            ls = deck_titles.get((player, day, "LS"))
            if not ds and not ls:
                continue
            ds_c = f"[[{ds}|{hub_labels.get(ds, ds)}]]" if ds else "—"
            ls_c = f"[[{ls}|{hub_labels.get(ls, ls)}]]" if ls else "—"
            finish = "—"
            if player in PC_FINISH:
                finish = f"#{PC_FINISH.index(player)+1}"
            rows.append(
                f"|- \n| 11–12 April 2026 || [[{EVENT_TITLE}]] (Day {day}) || [[Open]] || {finish} || {ds_c} || {ls_c}"
            )
        upsert_stub(player, rows)

    hub_body = hub(deck_titles, hub_labels, players_by_day)
    (PAGES / "2026_San_Diego_Super_Open.wiki").write_text(
        hub_body, encoding="utf-8", newline="\n"
    )
    print("hub", EVENT_TITLE, "decks", len(parsed))


if __name__ == "__main__":
    main()
