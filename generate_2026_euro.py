#!/usr/bin/env python3
"""Generate 2026 European Championship hub + two-column decks from PC HTML lists."""
from __future__ import annotations

import html as htmlmod
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import update_gempc_start_fields as ug  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
DECK_HTML = ROOT / "encyclopedia" / "euro2026-decks"
STANDINGS = ROOT / "encyclopedia" / "tournament-sources" / "euro2026-standings.json"

EVENT_TITLE = "2026 European Championship"
PC_HUB = "https://www.starwarsccg.org/2026-10-european-championship-bochum-germany-sept-19-20-2026/"
PC_FORUM = "https://forum.starwarsccg.org/viewforum.php?f=1594"

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
HEAD_CAT = {
    "CHARACTER": "CHARACTER",
    "CHARACTERS": "CHARACTER",
    "EFFECT": "EFFECT",
    "EFFECTS": "EFFECT",
    "INTERRUPT": "INTERRUPT",
    "INTERRUPTS": "INTERRUPT",
    "LOCATION": "LOCATION",
    "LOCATIONS": "LOCATION",
    "OBJECTIVE": "OBJECTIVE",
    "OBJECTIVES": "OBJECTIVE",
    "STARSHIP": "STARSHIP",
    "STARSHIPS": "STARSHIP",
    "VEHICLE": "VEHICLE",
    "VEHICLES": "VEHICLE",
    "WEAPON": "WEAPON",
    "WEAPONS": "WEAPON",
    "DEVICE": "DEVICE",
    "DEVICES": "DEVICE",
    "EPIC EVENT": "EPIC_EVENT",
    "EPIC EVENTS": "EPIC_EVENT",
    "DEFENSIVE SHIELD": "DEFENSIVE_SHIELD",
    "DEFENSIVE SHIELDS": "DEFENSIVE_SHIELD",
    "ADMIRAL'S ORDER": "ADMIRALS_ORDER",
    "ADMIRAL’S ORDER": "ADMIRALS_ORDER",
    "ADMIRAL'S ORDERS": "ADMIRALS_ORDER",
    "JEDI TEST": "JEDI_TEST",
    "JEDI TESTS": "JEDI_TEST",
    "PODRACER": "PODRACER",
    "PODRACERS": "PODRACER",
}

SLUG = {
    "Thrawn": "Thrawn",
    "Zero Hour": "Zero Hour",
    "SYCFA": "SYCFA",
    "Chewie’s Hut": "Chewie's Hut",
    "Chewie's Hut": "Chewie's Hut",
    "Hunt Down (V)": "HD(V)",
    "Diplo": "Diplo",
    "MKOS": "MKOS",
    "Court": "Court",
    "HITCO": "HITCO",
    "Shadow Collective": "SC",
    "No Idea": "No Idea",
    "WYS": "WYS",
    "Walkers": "Walkers",
    "WHAP": "WHAP",
    "AOBS": "AOBS",
    "TDIGWATT(V)": "TDIGWATT(V)",
    "A Stunning Move": "A Stunning Move",
    "Speeders": "Speeders",
    "MWYHL(V)": "MWYHL(V)",
    "Endor Operations": "EOps",
    "Hunt Down": "Hunt Down",
    "LS Senate": "Senate",
    "DS Senate": "Senate",
    "BHBM": "BHBM",
    "Hyperdrive (V)": "Hyperdrive (V)",
    "Profit": "Profit",
    "Old Allies": "OA",
    "ROTS Dooku": "ROTS Dooku",
    "RST": "RST",
    "ROTS Vader": "ROTS Vader",
    "TDIGWATT": "TDIGWATT",
    "Hidden Base": "Hidden Base",
    "Verge": "Verge",
}


def wiki_fname(title: str) -> str:
    return title.replace(" ", "_").replace("/", "_").replace("'", "'") + ".wiki"


def deck_page_title(player: str, t8: bool, side: str, obj_short: str) -> str:
    prefix = "2026 European Championship Top 8" if t8 else "2026 European Championship"
    return f"{prefix} {player} {side} {obj_short}"


def slug_url(url: str) -> str:
    return url.rstrip("/").split("/")[-1] + ".html"


def parse_pc_html(path: Path) -> tuple[Counter, list]:
    raw = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(
        r"fl-module-fl-post-content[\s\S]*?fl-module-content fl-node-content\">([\s\S]*?)<div class=\"fl-col fl-node-5d13d237ac255\"",
        raw,
    )
    if not m:
        m = re.search(
            r"fl-module-fl-post-content[\s\S]*?fl-module-content fl-node-content\">([\s\S]*?)</div>\s*</div>\s*</div>\s*</div>",
            raw,
        )
    chunk = m.group(1) if m else raw
    chunk = re.sub(r"</div>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<div[^>]*>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<br\s*/?>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</p>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<p[^>]*>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<[^>]+>", "\n", chunk)
    chunk = htmlmod.unescape(chunk)
    chunk = re.sub(r"\n\s*\(V\)", " (V)", chunk)
    chunk = re.sub(r"[ \t]+", " ", chunk)
    cat = None
    counts = Counter()
    cards = []
    for line in chunk.splitlines():
        line = line.strip()
        if not line or line.startswith("Posted"):
            continue
        key = line.upper().replace('’', "'").replace('‘', "'")
        if key.startswith('DECK:'):
            continue
        if key in HEAD_CAT:
            cat = HEAD_CAT[key]
            continue
        if not cat:
            continue
        for part in re.split(r"(?=\d+\s*x\s+)", line):
            part = part.strip()
            mm = re.match(r"(\d+)\s*x\s+(.+)$", part, re.I)
            if not mm:
                continue
            n = int(mm.group(1))
            title = mm.group(2).strip().rstrip("*")
            title = title.replace("’", "'")
            title = re.sub(r"\s+v$", " (V)", title, flags=re.I)
            counts[(cat, title)] += n
            for _ in range(n):
                cards.append(("", title, "card"))
    return counts, cards


def col(cat_map, cats):
    bits = []
    for cat in cats:
        items = cat_map.get(cat) or []
        if not items:
            continue
        bits.append(f"'''{CAT_LABEL.get(cat, cat.title())}'''")
        for n, title, dest in items:
            vis = ug.visible_label(title.replace(" (V)", ""), dest) if dest else title
            if dest and " / " in dest:
                vis = zero_side_label(dest, vis)
            if dest and ug.dest_has_v(dest) and not vis.endswith(" (V)"):
                vis = vis + " (V)"
            bits.append(f"* {n}x {ug.wiki_link(vis, dest)}")
        bits.append("")
    return "\n".join(bits).rstrip()


def norm_pc_title(title: str) -> str:
    t = title.replace(" (V)", "").replace(" (AI)", "").strip()
    t = t.replace("&", "And")
    t = re.sub(r"\s*/\s*", " / ", t)
    t = re.sub(r"\s+", " ", t)
    return t


def zero_side_label(dest: str | None, fallback: str) -> str:
    if dest and " / " in dest:
        vis = dest.split(" / ")[0]
        if ug.dest_has_v(dest) and not vis.endswith(" (V)"):
            vis = vis + " (V)"
        return vis
    return fallback


def lookup_dest(title: str, dests, title_map, bp, side_word: str):
    bare = norm_pc_title(title)
    want_v = " (V)" in title
    dest = ug.dest_for_card(bare, "", {}, dests, title_map)
    if not dest:
        dest = ug.dest_for_card(title.replace(" (V)", "").replace(" (AI)", "").strip(), "", {}, dests, title_map)
    hits = []
    for d in dests:
        s = ug.strip_u(d)
        if s == title or s == bare or s == bare + " (V)" or s.startswith(bare + " / "):
            hits.append(d)
    if dest:
        hits.append(dest)
    if not hits:
        return dest
    if want_v:
        vhits = [d for d in hits if ug.dest_has_v(d)]
        if vhits:
            return vhits[0]
    spaced = [d for d in hits if " / " in d]
    return (spaced[0] if spaced else None) or dest or hits[0]


def render_deck(player, t8, side, obj_short, counts, cards, source_url, companion, dests, title_map, bp):
    side_word = "Dark" if side == "DS" else "Light"
    title_dest = {}
    objs = []
    epics = []
    ints = []
    loc_title = None
    loc_note = ""
    has_ltww = False
    start_epics = {
        "Revenge Of The Sith",
        "The Shield Will Be Down in Moments",
        "The Shield Will Be Down in Moments (AI)",
        "The Force Is Strong In My Family",
        "Invasion",
    }
    start_ints = {
        "Prepared Defenses",
        "Heading For The Medical Frigate",
        "Let The Wookiee Win",
        "Any Methods Necessary",
        "Combat Readiness",
        "Surface Defense",
        "Operational As Planned",
        "Rise Of The Sith",
    }
    for cat, title in {(c, t) for (c, t) in counts}:
        dest = lookup_dest(title, dests, title_map, bp, side_word)
        if dest:
            title_dest[title] = dest
        if cat == "OBJECTIVE":
            if not any(o[0] == title for o in objs):
                objs.append((title, "", dest))
        elif dest and " / " in dest and cat in ("LOCATION", "EFFECT"):
            if not any(o[0] == title for o in objs):
                objs.append((title, "", dest))
        if cat == "EPIC_EVENT" and (
            title in start_epics
            or "Shield Will Be Down" in title
            or title == "Revenge Of The Sith"
            or title == "The Force Is Strong In My Family"
        ):
            epics.append((title, "", dest))
        if cat == "INTERRUPT":
            bare_int = title.replace(" (V)", "")
            if bare_int in start_ints or "Let The Wookiee Win" in title:
                ints.append((bare_int if "Let The Wookiee Win" in title else title, "", dest))
                if "Let The Wookiee Win" in title:
                    has_ltww = True
                    ints[-1] = ("Let The Wookiee Win", "", dest if dest else "Let The Wookiee Win (V)")
    for (cat, title), n in counts.items():
        if cat == "LOCATION" and title in {
            "Kashyyyk: Chewie's Hut",
            "Chewie's Hut",
        }:
            loc_title = "Kashyyyk: Chewie's Hut" if "Kashyyyk" not in title else title
            loc_note = "inferred: game text deploys only as a starting location"
        if cat == "LOCATION" and title == "Yavin 4: Massassi Throne Room" and not loc_title:
            loc_title = title
            loc_note = "inferred: no Objective; Throne Room Mains start"

    obj = objs[0] if objs else (epics[0] if epics else None)
    cat_map = defaultdict(list)
    for (cat, title), n in sorted(counts.items(), key=lambda x: (x[0][0], x[0][1].lower())):
        cat_map[cat].append((n, title, title_dest.get(title)))

    loc_bits = []
    if loc_title:
        ld = title_dest.get(loc_title) or loc_title
        bit = ug.wiki_link(loc_title, ld if ld != loc_title else loc_title)
        if loc_note:
            bit += f" <small>({loc_note})</small>"
        loc_bits.append(bit)
    if obj:
        t0 = zero_side_label(obj[2], obj[0].split("/")[0].strip() if "/" in obj[0] else obj[0])
        loc_bits.append(ug.wiki_link(t0, obj[2]))
    loc_line = "* '''Starting Card:''' " + (
        " · ".join(loc_bits) if loc_bits else "—"
    )
    # unique ints
    seen = set()
    int_bits = []
    for t, c, d in ints:
        vis = "Let The Wookiee Win (V)" if t == "Let The Wookiee Win" else t
        key = vis
        if key in seen:
            continue
        seen.add(key)
        dest = d if t != "Let The Wookiee Win" else "Let The Wookiee Win (V)"
        int_bits.append(ug.wiki_link(vis, dest))
    int_line = "* '''Starting Interrupt:''' " + (" · ".join(int_bits) if int_bits else "—")

    extra = [c for c in cat_map if c not in LEFT and c not in RIGHT]
    left = col(cat_map, LEFT)
    right = col(cat_map, RIGHT)
    extra_txt = col(cat_map, extra) if extra else ""
    if extra_txt:
        right = (right + "\n\n" + extra_txt).strip()

    title = deck_page_title(player, t8, side, obj_short)
    companion_line = f"* [[{companion}]]" if companion else ""
    info = [
        f"* '''Player:''' [[{player}]]",
        f"* '''Event:''' [[{EVENT_TITLE}]]",
        f"* '''Stage:''' {'Top 8' if t8 else 'Day 1'}",
        "* '''Format:''' [[Open]]",
        f"* '''Side:''' [[{side_word}]]",
        loc_line,
        int_line,
        f"* '''Source list:''' [{source_url} PC decklist]",
    ]
    hub_label = None
    if obj:
        hub_label = zero_side_label(obj[2], obj[0])
        if "/" in str(hub_label) and " / " not in str(hub_label):
            hub_label = str(hub_label).split("/")[0].strip()
    elif has_ltww:
        hub_label = "Let The Wookiee Win (V)"
    elif loc_title:
        hub_label = loc_title
    elif ints:
        vis = ints[0][0]
        dest = ints[0][2]
        if vis == "Let The Wookiee Win":
            hub_label = "Let The Wookiee Win (V)"
        else:
            hub_label = ug.visible_label(vis.replace(" (V)", ""), dest) if dest else vis
            if dest and ug.dest_has_v(dest) and not str(hub_label).endswith(" (V)"):
                hub_label = str(hub_label) + " (V)"
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
* [[European Championships]]
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


def upsert_stub(player, rows):
    STUBS.mkdir(parents=True, exist_ok=True)
    path = STUBS / (player.replace(" ", "_") + ".wiki")
    event_link = f"[[{EVENT_TITLE}]]"
    extra = f"* [{PC_HUB} 2026-10 European Championship], starwarsccg.org\n"
    if path.exists():
        text = path.read_text(encoding="utf-8")
        text = re.sub(
            r"\|-\s*\n\| [^\n]*\[\[2026 European Championship\]\][^\n]*\n",
            "",
            text,
        )
        if "|}" in text and "Tournament Results" in text:
            text = text.replace("|}\n", "\n".join(rows) + "\n|}\n", 1)
        if event_link not in text.split("== Tournament Results ==")[0]:
            if "* [[Championships]]" in text:
                text = text.replace(
                    "* [[Championships]]",
                    f"* {event_link}\n* [[European Championships]]\n* [[Championships]]",
                    1,
                )
            elif "== See also ==" in text and event_link not in text:
                text = text.replace(
                    "== See also ==\n",
                    f"== See also ==\n\n* {event_link}\n* [[European Championships]]\n",
                    1,
                )
        if "== Sources ==" in text and PC_HUB not in text:
            text = text.replace("== Sources ==\n", "== Sources ==\n" + extra, 1)
        path.write_text(text, encoding="utf-8", newline="\n")
        return
    body = f"""'''{player}''' played the [[{EVENT_TITLE}]].<ref name="pc-euro">[{PC_HUB} 2026-10 European Championship], starwarsccg.org</ref>

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
{chr(10).join(rows)}
|}}

== See also ==

* {event_link}
* [[European Championships]]
* [[Championships]]

== Sources ==

* [{PC_HUB} 2026-10 European Championship], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2026]]
"""
    path.write_text(body, encoding="utf-8", newline="\n")


def hub(deck_titles, hub_labels, top8, day1):
    def cell(player, t8, side):
        page = deck_titles.get((player, t8, side))
        if not page:
            return "—"
        return f"[[{page}|{hub_labels.get(page, page)}]]"

    t8_rows = ['{| class="wikitable sortable"', "! Finish !! Player !! Dark !! Light"]
    for r in top8:
        p = r["player"]
        t8_rows += [
            "|-",
            f"| {r['finish']} || [[{p}]] || {cell(p, True, 'DS')} || {cell(p, True, 'LS')}",
        ]
    t8_rows.append("|}")

    d1_rows = ['{| class="wikitable sortable"', "! Day 1 !! Player !! Dark !! Light"]
    for r in day1:
        p = r["player"]
        ds = cell(p, False, "DS")
        ls = cell(p, False, "LS")
        d1_rows += ["|-", f"| {r['day1']} || [[{p}]] || {ds} || {ls}"]
    d1_rows.append("|}")

    return f"""'''{EVENT_TITLE}''' was the Players Committee European Championship at Zu Den Vier Winden in Bochum, Germany, 18–20 September 2026 (constructed 19–20 September). [[Timo Dusel]] won; [[Quirin Fürgut]] finished second.<ref name="pc">{PC_HUB}</ref>

The main event is [[Open]] constructed: Day 1 Swiss, then Top 8. Friday of the weekend was a team event. This year is listed with earlier ECs on [[European Championships]].

== Format ==

* '''Environment:''' [[Open]]
* '''Site:''' Bochum, Germany (Zu Den Vier Winden)
* '''Dates:''' 18–20 September 2026
* '''Forum:''' [{PC_FORUM} 2026 European Championship Forum]

== Top 8 ==

As published on the PC results page. Dark/Light cells use the printed objective (or inferred start) from that list.<ref name="pc" />

{chr(10).join(t8_rows)}

== Day 1 ==

Day 1 lists as published (order on the PC page). Top 8 lists can differ from Day 1 (Olson Day 1 Dark is This Deal Is Getting Worse All The Time (V); Top 8 Dark is Shadow Collective).<ref name="pc" />

{chr(10).join(d1_rows)}

== See also ==

* [[European Championships]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [{PC_HUB} PC results]
* [{PC_FORUM} Forum]

== Sources ==

* [{PC_HUB} 2026-10 European Championship – Bochum, Germany (Sept. 19-20, 2026)], starwarsccg.org
* [{PC_FORUM} 2026 European Championship Forum], f=1594

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
"""


def load_one_deck(url: str):
    if not url:
        return None, None
    p = DECK_HTML / slug_url(url)
    if not p.exists():
        print("MISSING", p.name)
        return None, None
    return parse_pc_html(p)


def main():
    data = json.loads(STANDINGS.read_text(encoding="utf-8"))
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    PAGES.mkdir(parents=True, exist_ok=True)

    parsed = []
    for t8, rows in ((True, data["top8"]), (False, data["day1"])):
        for r in rows:
            player = r["player"]
            for side, key in (("DS", "ds"), ("LS", "ls")):
                label = r.get(key)
                url = r.get(key + "_url")
                if not label or not url:
                    continue
                obj_short = SLUG.get(label, label)
                counts, cards = load_one_deck(url)
                if counts is None:
                    continue
                parsed.append((player, t8, side, obj_short, counts, cards, url))

    deck_titles = {}
    hub_labels = {}
    for player, t8, side, obj_short, counts, cards, url in parsed:
        deck_titles[(player, t8, side)] = deck_page_title(player, t8, side, obj_short)

    for player, t8, side, obj_short, counts, cards, url in parsed:
        other = "LS" if side == "DS" else "DS"
        companion = deck_titles.get((player, t8, other))
        title, body, hub_label = render_deck(
            player, t8, side, obj_short, counts, cards, url, companion, dests, title_map, bp
        )
        (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
        hub_labels[title] = hub_label
        print("deck", title, "->", hub_label, "cards", sum(counts.values()))

    for player in sorted({p for p, *_ in parsed} | {r["player"] for r in data["day1"]}):
        rows = []
        t8r = next((x for x in data["top8"] if x["player"] == player), None)
        d1r = next((x for x in data["day1"] if x["player"] == player), None)
        if t8r:
            ds = deck_titles.get((player, True, "DS"))
            ls = deck_titles.get((player, True, "LS"))
            ds_c = f"[[{ds}|{hub_labels.get(ds, ds)}]]" if ds else "—"
            ls_c = f"[[{ls}|{hub_labels.get(ls, ls)}]]" if ls else "—"
            rows.append(
                f"|- \n| 19–20 September 2026 || [[{EVENT_TITLE}]] (Top 8) || [[Open]] || #{t8r['finish']} || {ds_c} || {ls_c}"
            )
        if d1r:
            ds = deck_titles.get((player, False, "DS"))
            ls = deck_titles.get((player, False, "LS"))
            ds_c = f"[[{ds}|{hub_labels.get(ds, ds)}]]" if ds else "—"
            ls_c = f"[[{ls}|{hub_labels.get(ls, ls)}]]" if ls else "—"
            rows.append(
                f"|- \n| 19 September 2026 || [[{EVENT_TITLE}]] (Day 1) || [[Open]] || — || {ds_c} || {ls_c}"
            )
        if rows:
            upsert_stub(player, rows)

    hub_body = hub(deck_titles, hub_labels, data["top8"], data["day1"])
    (PAGES / "2026_European_Championship.wiki").write_text(
        hub_body, encoding="utf-8", newline="\n"
    )
    print("hub", EVENT_TITLE, "decks", len(parsed))


if __name__ == "__main__":
    main()
