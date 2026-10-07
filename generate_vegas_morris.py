#!/usr/bin/env python3
"""GEMP decks for 2025 Las Vegas GP and Morristown Melee."""
from __future__ import annotations

import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2026_remaining as g26  # noqa: E402
from generate_2026_sdso import load_bp_simple, parse_gemp_counts, wiki_fname  # noqa: E402
import update_gempc_start_fields as ug  # noqa: E402

PAGES = ROOT / "pages"
MEDIA = ROOT / "2025-media"
TD = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\td-2021-2026")

FILE = dict(g26.FILE_PLAYER)
FILE.update(
    {
        "Gogolen": "Chris Gogolen",
        "Gogoglen": "Chris Gogolen",
        "d'Amboise": "Mike d'Amboise",
        "dAmboise": "Mike d'Amboise",
        "Sokol": "Matt Sokol",
        "Johnson": "Patrick Johnson",
        "Anis": "Casey Anis",
        "Smith": "Jacy Smith",
        "Randy Scott": "Randy Scott",
        "Scott Lingrell": "Scott Lingrell",
        "Steve Harpster": "Steve Harpster",
        "AJ Hatoum": "AJ Hatoum",
        "Amar Banger": "Amar Banger",
        "Anthony Howard": "Anthony Howard",
        "Billings": "Mark Billings",
        "Brad Reinhold": "Brad Reinhold",
        "Chris Wirfs": "Chris Wirfs",
        "Cal Aldred": "Cal Aldred",
        "Joe Olson": "Joe Olson",
        "Jeff Lavigne": "Jeff Lavigne",
        "Sam Tashima": "Sam Tashima",
        "Logan Pietig": "Logan Pietig",
        "Mike Kessling": "Mike Kessling",
        "Dennis Reinhardt": "Dennis Reinhardt",
        "Karl Koenig": "Karl Koenig",
        "Kessling": "Mike Kessling",
        "Hatoum": "AJ Hatoum",
        "Silkwood": "Blake Silkwood",
        "Jacy Smith": "Jacy Smith",
        "Bowman": "Geoff Bowman",
        "KELLY": "Chris Kelly",
        "Kelly": "Chris Kelly",
        "Thornton": "Matt Thornton",
        "Veasey": "John Veasey",
        "Krueger": "Kyle Krueger",
        "Lutz": "Matt Lutz",
        "Tartaglione": "Dan Tartaglione",
        "Terwilliger": "Chris Terwilliger",
        "Pinto": "Joe Pinto",
        "Westergard": "Chris Westergard",
        "Halman": "Kendall Halman",
        "Horbey": "Joe Horbey",
        "Alperstein": "Barry Alperstein",
        "Fred": "Brian Fred",
        "Konsker": "Jarad Konsker",
        "Cullen": "Wayne Cullen",
        "Miyashiro": "Justin Miyashiro",
        "Harpster": "Steve Harpster",
        "Lingrell": "Scott Lingrell",
        "Wirfs": "Chris Wirfs",
        "Howard": "Anthony Howard",
        "Banger": "Amar Banger",
        "Koenig": "Karl Koenig",
        "Reinhardt": "Dennis Reinhardt",
        "Johnson": "Patrick Johnson",
        "Hunter": "Hayes Hunter",
        "Shaw": "Greg Shaw",
        "Kafer": "Bill Kafer",
        "Sokol": "Matt Sokol",
        "Moss": "Andrew Moss",
        "Anis": "Casey Anis",
        "Lavigne": "Jeff Lavigne",
        "Tashima": "Sam Tashima",
        "Olson": "Joe Olson",
        "Pietig": "Logan Pietig",
        "Reinhold": "Brad Reinhold",
        "Aldred": "Cal Aldred",
        "Billings": "Mark Billings",
        "Randy Scott": "Randy Scott",
        "Scott": "Randy Scott",
    }
)

VEGAS_T8 = [
    "Joe Olson",
    "Sam Tashima",
    "Logan Pietig",
    "Jeff Lavigne",
    "Mike Kessling",
    "Dennis Reinhardt",
    "Brad Reinhold",
    "Karl Koenig",
]
VEGAS_D1 = [
    "Joe Olson",
    "Logan Pietig",
    "Mike Kessling",
    "Sam Tashima",
    "Jeff Lavigne",
    "Dennis Reinhardt",
    "Brad Reinhold",
    "Karl Koenig",
    "Cal Aldred",
    "Chris Kelly",
    "Scott Lingrell",
    "AJ Hatoum",
    "Amar Banger",
    "Kyle Krueger",
    "Chris Wirfs",
    "Steve Harpster",
    "Justin Miyashiro",
    "Jacy Smith",
    "Anthony Howard",
    "Blake Silkwood",
    "Matt Thornton",
    "Brian Fred",
    "John Veasey",
    "Mark Billings",
    "Randy Scott",
    "Geoff Bowman",
]
MORRIS_T8 = [
    "Greg Shaw",
    "Jeff Lavigne",
    "Hayes Hunter",
    "Chris Gogolen",
    "Bill Kafer",
    "Mike Kessling",
    "AJ Hatoum",
    "Matt Sokol",
]
MORRIS_D1 = [
    "Hayes Hunter",
    "Chris Gogolen",
    "Greg Shaw",
    "Jeff Lavigne",
    "Bill Kafer",
    "Mike Kessling",
    "AJ Hatoum",
    "Matt Sokol",
    "Chris Kelly",
    "Matt Lutz",
    "Barry Alperstein",
    "Joe Horbey",
    "Mike d'Amboise",
    "Dan Tartaglione",
    "Andrew Moss",
    "Patrick Johnson",
    "Brian Fred",
    "Jarad Konsker",
    "Karl Koenig",
    "Chris Terwilliger",
    "Joe Pinto",
    "Wayne Cullen",
    "Chris Westergard",
    "Kendall Halman",
    "Casey Anis",
    "Blake Silkwood",
    "Scott Lingrell",
]


def canon(tok: str) -> str:
    tok = tok.strip().replace("_", " ")
    return FILE.get(tok, tok)


def parse_vegas(path: Path):
    name = path.name
    parent = path.parent.name.lower()
    t8 = "day 2" in name.lower() or parent == "day 2"
    m = re.search(r"\b(DS|LS)\b(?:\s*(?:[-_]+\s*)?(.+?))?(?:\s*-\s*Vegas.*)?\.txt$", name, re.I)
    if not m:
        m = re.search(r"(DS|LS)[ _](.+)\.txt$", name, re.I)
    if not m:
        m = re.search(r"(DS|LS)_(.+)\.txt$", name, re.I)
    if not m:
        return None
    side = m.group(1).upper()
    obj = re.sub(r"\s+", " ", (m.group(2) or "")).strip()
    obj = re.sub(r"\s*-\s*Vegas.*$", "", obj, flags=re.I).strip()
    obj = re.sub(r"\s*\(no v-cards\)\s*", " ", obj, flags=re.I).strip()
    left = name[: m.start()].strip()
    left = re.sub(r"^2024 Vegas Day 1\s*", "", left, flags=re.I)
    left = re.sub(r"^25\s*LVGP\s*(Day 2\s*)?", "", left, flags=re.I)
    left = re.sub(r"^25Vegas\s*", "", left, flags=re.I)
    left = re.sub(r"2025 Vegas\s*", "", left, flags=re.I)
    left = re.sub(r"Vegas 2025\s*", "", left, flags=re.I)
    left = re.sub(r"Cal Aldred.*", "Cal Aldred", left)
    left = re.sub(r"KELLY[_ ]Vegas", "Chris Kelly", left, flags=re.I)
    left = re.sub(r"\s+Vegas$", "", left, flags=re.I)
    player = canon(left.strip(" -_"))
    if player.lower() in {"vegas", "day", "day 2", ""}:
        return None
    return "vegas", player, t8, side, obj, name


def parse_morris(path: Path):
    name = path.name
    parent = path.parent.name.lower()
    if name.startswith("24MorrisT8") and parent == "top 8":
        name = "25" + name[2:]
    elif name.startswith("24Morris"):
        return None
    if not name.startswith("25Morris"):
        return None
    t8 = "T8" in name or parent == "top 8"
    rest = re.sub(r"^25MorrisT8\s*", "", name)
    rest = re.sub(r"^25Morris\s*", "", rest)
    rest = rest[: -4] if rest.endswith(".txt") else rest
    m = re.search(r" (DS|LS) ", rest)
    if m:
        player = canon(rest[: m.start()])
        side = m.group(1)
        obj = rest[m.end() :]
        return "morris", player, t8, side, obj, name
    parts = rest.split()
    if len(parts) < 2:
        return None
    player = canon(parts[0])
    obj = " ".join(parts[1:])
    side = (
        "LS"
        if obj.lower()
        in {
            "profit",
            "wys",
            "whap",
            "qmc",
            "hitco",
            "speeders",
            "no idea",
            "trm",
            "rtp",
            "rtpv",
            "oa",
            "tigih",
        }
        else "DS"
    )
    return "morris", player, t8, side, obj, name


def deck_title(ev, player, t8, side, obj):
    if ev == "vegas":
        pfx = "2025 LVGP Day 2" if t8 else "2025 LVGP"
    else:
        pfx = "2025 Morristown Top 8" if t8 else "2025 Morristown"
    bits = [pfx, player, side]
    if obj:
        bits.append(obj)
    return " ".join(bits)


def event_title(ev):
    return "2025 Las Vegas Grand Prix" if ev == "vegas" else "2025 Morristown Melee"


def main():
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    by_id, by_title = load_bp_simple()
    MEDIA.mkdir(parents=True, exist_ok=True)
    parsed = []
    for folder, parser in [
        (TD / "2025-vegas", parse_vegas),
        (TD / "2025-morristown", parse_morris),
    ]:
        for path in folder.rglob("*.txt"):
            info = parser(path)
            if not info:
                print("SKIP", path.name)
                continue
            ev, player, t8, side, obj, media = info
            try:
                counts, cards = parse_gemp_counts(path, by_id, by_title)
            except Exception as e:
                print("BADXML", path.name, e)
                continue
            safe = re.sub(r"[^\w.\- ]+", "", media)[:120]
            shutil.copy2(path, MEDIA / safe)
            parsed.append((ev, player, t8, side, obj, safe, counts, cards))
    best = {}
    for item in parsed:
        key = item[:4]
        prev = best.get(key)
        if not prev or sum(item[6].values()) >= sum(prev[6].values()):
            best[key] = item
    parsed = list(best.values())

    deck_titles = {}
    hub_labels = {}
    for ev, player, t8, side, obj, media, counts, cards in parsed:
        deck_titles[(ev, player, t8, side)] = deck_title(ev, player, t8, side, obj)

    for ev, player, t8, side, obj, media, counts, cards in parsed:
        other = "LS" if side == "DS" else "DS"
        companion = deck_titles.get((ev, player, t8, other))
        g26.deck_title = lambda e, p, t, s, o, ev=ev: deck_title(ev, p, t, s, o)
        g26.event_title = lambda e, ev=ev: event_title(ev)
        title, body, hub = g26.render_deck(
            ev, player, t8, side, obj, counts, cards, media, companion, bp, dests, title_map
        )
        body = body.replace("[[Category:2026]]", "[[Category:2025]]")
        (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
        hub_labels[title] = hub
        print("deck", title, "->", hub, "n", sum(counts.values()))

    def subset(ev):
        dt, hl = {}, {}
        for (e, player, t8, side), title in deck_titles.items():
            if e != ev:
                continue
            dt[(player, t8, side)] = title
            hl[title] = hub_labels.get(title, title)
        return dt, hl

    def cell(dt, hl, p, t8, side):
        page = dt.get((p, t8, side))
        if not page:
            return "—"
        return f"[[{page}|{hl.get(page, page)}]]"

    def table(players, dt, hl, t8, heading):
        bits = ['{| class="wikitable sortable"', f"! {heading} !! Player !! Dark !! Light"]
        for i, p in enumerate(players, 1):
            bits += [
                "|-",
                f"| {i} || [[{p}]] || {cell(dt, hl, p, t8, 'DS')} || {cell(dt, hl, p, t8, 'LS')}",
            ]
        bits.append("|}")
        return "\n".join(bits)

    def patch_hub(path: Path, t8_players, d1_players, dt, hl):
        text = path.read_text(encoding="utf-8")
        t8_tbl = table(t8_players, dt, hl, True, "Finish")
        d1_tbl = table(d1_players, dt, hl, False, "Day 1")
        text = re.sub(
            r"== Top 8 ==\n.*?(?=\n== )",
            "== Top 8 ==\n\n" + t8_tbl + "\n\n",
            text,
            count=1,
            flags=re.S,
        )
        d1_block = (
            "== Day 1 ==\n\nDay 1 lists as published (order on the PC page). "
            "Top 8 lists can differ from Day 1.<ref name=\"pc\" />\n\n"
            + d1_tbl
            + "\n\n"
        )
        if "== Day 1 ==" in text:
            text = re.sub(
                r"== Day 1 ==\n.*?(?=\n== )",
                d1_block,
                text,
                count=1,
                flags=re.S,
            )
        else:
            text = text.replace("== See also ==", d1_block + "== See also ==", 1)
        path.write_text(text, encoding="utf-8", newline="\n")

    vdt, vhl = subset("vegas")
    mdt, mhl = subset("morris")
    patch_hub(PAGES / "2025_Las_Vegas_Grand_Prix.wiki", VEGAS_T8, VEGAS_D1, vdt, vhl)
    patch_hub(PAGES / "2025_Morristown_Melee.wiki", MORRIS_T8, MORRIS_D1, mdt, mhl)
    print("vegas/morris decks", len(parsed))


if __name__ == "__main__":
    main()
