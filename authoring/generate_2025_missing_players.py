#!/usr/bin/env python3
"""Create remaining 2025 person stubs from tournament hubs; merge last-name stubs."""
from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"

# Last-name GEMP tokens that already have a stub, mapped to the legal name used on hubs.
LAST_TO_FULL = {
    "Boyle": "Jim Boyle",
    "Brown": "Keith Brown",
    "Chu": "Jonny Chu",
    "DMorrison": "David Morrison",
    "Davis": "Nate Davis",
    "Eier": "Brad Eier",
    "French": "Ryan French",
    "Grubb": "Jonathan Grubb",
    "Hoyt": "Ellie Hoyt",
    "JChu": "Jonny Chu",
    "JGosiaco": "Jordan Gosiaco",
    "Kramer": "Jacoby Kramer",
    "Larson": "Garrett Larson",
    "Lawrence": "Chad Lawrence",
    "MMorrison": "Michael Morrison",
    "Marcus": "Marcus",
    "Morris": "Travis Morris",
    "Nguyen": "Brandon Nguyen",
    "Pater": "L. Pater",
    "Phillips": "Joe Phillips",
    "RScott": "Randy Scott",
    "SGosiaco": "Spencer Gosiaco",
    "Smith": "Jacy Smith",
    "TGosiaco": "Taylor Gosiaco",
    "Tartaglione": "Dan Tartaglione",
    "Thornton": "Matt Thornton",
    "Veasey": "John Veasey",
    "Walseth": "Mark Walseth",
    "Werner": "John Werner",
    "Westergard": "Chris Westergard",
    "Woods": "David Woods",
    "Yim": "Gibson Yim",
}

# Hub typo → canonical person page.
ALIAS = {
    "Eric Spijksma": "Erik Spijksma",
}

HUBS = [
    (
        "2025_World_Championship.wiki",
        "2025 World Championship",
        "4–5 October 2025",
        "[[Open]]",
        "https://www.starwarsccg.org/2025-09-world-championship-seattle-washington-october-4-5-2025/",
    ),
    (
        "2025_U.S._National_Championship.wiki",
        "2025 U.S. National Championship",
        "23–24 August 2025",
        "[[Open]]",
        "https://www.starwarsccg.org/2025-07-u-s-national-championship-columbus-ohio-aug-23-24-2025/",
    ),
    (
        "2025_European_Championship.wiki",
        "2025 European Championship",
        "20–21 September 2025",
        "[[Open]]",
        "https://www.starwarsccg.org/2025-08-european-championship-bochum-germany-sept-20-21-2025/",
    ),
    (
        "2025_Ninth_Annual_GEMPC.wiki",
        "2025 Ninth Annual GEMPC",
        "May–July 2025",
        "[[Open]]",
        "https://www.starwarsccg.org/2025-05-9th-annual-gempc-may-to-july-2025/",
    ),
    (
        "2025_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki",
        "2025 Retro GEMP Match Play Championship (Premiere to DSII)",
        "May–July 2025",
        "[[Premiere - Death Star II]]",
        "https://www.starwarsccg.org/2025-04-retro-gemp-match-play-championship-premiere-to-dsii-may-to-july-2025/",
    ),
    (
        "2025_Online_Retro_Event_for_Charity.wiki",
        "2025 Online Retro Event for Charity",
        "May–June 2025",
        "[[Premiere to Virtual Set 3]]",
        "https://www.starwarsccg.org/2025-06-online-retro-event-for-charity-premiere-to-virtual-set-3/",
    ),
    (
        "2025_Online_Championship_Series_Playoffs.wiki",
        "2025 Online Championship Series Playoffs",
        "October–November 2025",
        "[[Open]]",
        "https://www.starwarsccg.org/2025-10-online-championship-series-ocs-playoffs-oct-to-nov-2025/",
    ),
    (
        "2025_Regional_Championships.wiki",
        "2025 Regional Championships",
        "2025",
        "[[Open]]",
        "https://www.starwarsccg.org/2025-03-regional-championships/",
    ),
    (
        "2025_Morristown_Melee.wiki",
        "2025 Morristown Melee",
        "24–27 April 2025",
        "[[Open]]",
        "https://www.starwarsccg.org/2025-02-morristown-melee-morristown-new-jersey-apr-24-27-2025/",
    ),
    (
        "2025_Las_Vegas_Grand_Prix.wiki",
        "2025 Las Vegas Grand Prix",
        "11–12 January 2025",
        "[[Open]]",
        "https://www.starwarsccg.org/2025-01-las-vegas-grand-prix-las-vegas-nevada-jan-11-12-2025/",
    ),
]

REGIONAL_DATES = {
    "Coruscant": "15 November 2025",
    "Corellia": "8 November 2025",
    "Nal Hutta": "21 September 2025",
    "Tatooine": "14 September 2025",
    "Endor": "16 August 2025",
    "Bespin": "28 June 2025",
    "Naboo": "21 June 2025",
}

SKIP_OVERWRITE = (
    "Squadron Member",
    "Anagrams",
    "is a member of the",
    "Players Committee Advocate",
)


def stub_path(name: str) -> Path:
    return STUBS / (name.replace(" ", "_") + ".wiki")


def canon(name: str) -> str:
    name = name.strip()
    return ALIAS.get(name, name)


def is_deck_title(title: str) -> bool:
    return bool(re.match(r"^\d{4} ", title)) or title.startswith("File:")


def parse_cells(block: str) -> list[str]:
    block = block.strip()
    if not block or block.startswith("!"):
        return []
    parts = [p.strip() for p in re.split(r"\s*\|\|\s*", block)]
    if parts and parts[0].startswith("|"):
        parts[0] = parts[0][1:].strip()
    return [p for p in parts if p]


def player_and_sides(cells: list[str]):
    player = None
    pidx = None
    for i, c in enumerate(cells):
        m = re.search(r"\[\[([^\]|#]+)(?:\|[^\]]+)?\]\]", c)
        if not m:
            continue
        title = m.group(1).strip()
        if is_deck_title(title):
            continue
        if title in ("Open", "Light", "Dark", "Jawa Format"):
            continue
        player = title
        pidx = i
        break
    if player is None:
        return None
    rest = cells[pidx + 1 :] if pidx is not None else []
    dark = rest[0] if rest else "—"
    light = rest[1] if len(rest) > 1 else "—"
    finish = cells[0] if pidx and pidx > 0 else "—"
    if finish == player or finish.startswith("[["):
        finish = "—"
    if re.fullmatch(r"\d+", finish or ""):
        finish = f"#{finish}"
    return player, finish, dark, light


def split_sections(text: str) -> list[tuple[str, str]]:
    parts = re.split(r"\n(?===+ )", text)
    out = []
    for part in parts:
        m = re.match(r"(=+)\s*(.+?)\s*\1\s*\n?", part)
        if not m:
            continue
        out.append((m.group(2).strip(), part[m.end() :]))
    return out


def collect_from_hubs() -> dict[str, list[tuple]]:
    """player -> list of (date, event, stage, fmt, finish, dark, light, src)."""
    by: dict[str, list] = defaultdict(list)
    for fname, event, date, fmt, src in HUBS:
        path = PAGES / fname
        if not path.exists():
            print("NOHUB", fname)
            continue
        text = path.read_text(encoding="utf-8")
        for heading, body in split_sections(text):
            stage = heading
            stage = re.sub(r"^\[\[|\]\]$", "", stage)
            if heading.startswith("See also") or heading.startswith("Sources") or heading.startswith("Format"):
                continue
            if heading == "Results":
                continue
            local_date = date
            local_stage = stage
            mreg = re.match(r"(.+?) Regionals$", stage)
            if mreg:
                planet = mreg.group(1)
                local_date = REGIONAL_DATES.get(planet, date)
                local_stage = f"{planet} Regionals"
            for block in re.split(r"\n\|-\n", body):
                cells = parse_cells(block)
                if len(cells) < 2:
                    continue
                parsed = player_and_sides(cells)
                if not parsed:
                    continue
                player, finish, dark, light = parsed
                player = canon(player)
                if heading in ("Decklists", "Bracket") and finish not in ("—",) and not str(finish).startswith("#"):
                    local_stage = finish
                    finish = "—"
                by[player].append(
                    (local_date, event, local_stage, fmt, finish, dark, light, src)
                )
    return by


def row_wiki(date, event, stage, fmt, finish, dark, light) -> str:
    st = ""
    if stage and stage not in ("Results", event):
        if not stage.startswith(event):
            st = f" ({stage})"
    return (
        f"|- \n| {date} || [[{event}]]{st} || {fmt} || {finish} || {dark} || {light}"
    )


def protected(text: str) -> bool:
    return any(s in text for s in SKIP_OVERWRITE)


def insert_missing(player: str, recs: list) -> str:
    path = stub_path(player)
    text = path.read_text(encoding="utf-8")
    if protected(text):
        return "protect"
    added = 0
    for date, event, stage, fmt, finish, dark, light, src in recs:
        key = f"[[{event}]] ({stage})" if stage not in ("Results", event, "Decklists", "") else f"[[{event}]]"
        if key in text:
            continue
        row = row_wiki(date, event, stage, fmt, finish, dark, light)
        if "|}" in text and "Tournament Results" in text:
            text = text.replace("|}\n", row + "\n|}\n", 1)
            added += 1
        if src not in text and "== Sources ==" in text:
            text = text.replace(
                "== Sources ==\n",
                f"== Sources ==\n* [{src} {event}], starwarsccg.org\n",
                1,
            )
        if f"[[{event}]]" not in text.split("== Tournament Results ==")[0] and "* [[Championships]]" in text:
            text = text.replace("* [[Championships]]", f"* [[{event}]]\n* [[Championships]]", 1)
    if added:
        path.write_text(text, encoding="utf-8", newline="\n")
        return "merge"
    return "skip"


def upsert(player: str, rows: list[str], events: set[str], srcs: set[str]):
    STUBS.mkdir(parents=True, exist_ok=True)
    path = stub_path(player)
    extra_see = "".join(f"* [[{e}]]\n" for e in sorted(events))
    extra_src = "".join(f"* [{u} {e}], starwarsccg.org\n" for e, u in sorted((e, u) for e in events for u in srcs))
    if path.exists():
        text = path.read_text(encoding="utf-8")
        if protected(text):
            print("PROTECT", player)
            return "protect"
        for e in events:
            text = re.sub(
                rf"\|-\s*\n\| [^\n]*\[\[{re.escape(e)}\]\][^\n]*\n",
                "",
                text,
            )
        if "|}" in text and "Tournament Results" in text:
            text = text.replace("|}\n", "\n".join(rows) + "\n|}\n", 1)
        if "* [[Championships]]" in text:
            for e in sorted(events):
                if f"[[{e}]]" not in text.split("== Tournament Results ==")[0]:
                    text = text.replace(
                        "* [[Championships]]",
                        f"* [[{e}]]\n* [[Championships]]",
                        1,
                    )
        if "== Sources ==" in text:
            for line in extra_src.splitlines(True):
                if line.strip() and line.split("]", 1)[0] not in text:
                    text = text.replace("== Sources ==\n", "== Sources ==\n" + line, 1)
        if "[[Category:2025]]" not in text:
            text = text.replace("[[Category:Players]]", "[[Category:Players]]\n[[Category:2025]]")
        path.write_text(text, encoding="utf-8", newline="\n")
        return "merge"
    lead = f"'''{player}''' played in 2025 Players Committee constructed events."
    src0 = next(iter(srcs))
    ev0 = next(iter(events))
    body = f"""'''{player}''' played in 2025 Players Committee constructed events.<ref name="pc-2025">[{src0} {ev0}], starwarsccg.org</ref>

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
{chr(10).join(rows)}
|}}

== See also ==

{extra_see}* [[List of SWCCG tournaments]]
* [[Championships]]

== Sources ==

{extra_src}
{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
[[Category:2025]]
"""
    path.write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    return "create"


def write_redirect(src: str, dest: str):
    path = stub_path(src)
    path.write_text(f"#REDIRECT [[{dest}]]\n", encoding="utf-8", newline="\n")


def patch_hub_typos():
    p = PAGES / "2025_World_Championship.wiki"
    if p.exists():
        t = p.read_text(encoding="utf-8")
        n = t.replace("[[Eric Spijksma]]", "[[Erik Spijksma]]")
        if n != t:
            p.write_text(n, encoding="utf-8", newline="\n")
            print("patched Eric Spijksma -> Erik Spijksma on Worlds hub")


def main():
    by = collect_from_hubs()
    existing = {p.stem.replace("_", " ") for p in STUBS.glob("*.wiki")}
    print("hub players", len(by), "stubs", len(existing))

    # Merge last-name stubs into full names before creating.
    for last, full in LAST_TO_FULL.items():
        lp = stub_path(last)
        if not lp.exists() or last == full:
            continue
        text = lp.read_text(encoding="utf-8")
        if text.startswith("#REDIRECT"):
            continue
        fp = stub_path(full)
        if fp.exists():
            # Pull last-name rows into the full-name page via later upsert.
            write_redirect(last, full)
            print("redirect", last, "->", full, "(full exists)")
            continue
        text = text.replace(f"'''{last}'''", f"'''{full}'''", 1)
        fp.write_text(text, encoding="utf-8", newline="\n")
        write_redirect(last, full)
        print("rename", last, "->", full)

    created = merged = skipped = 0
    changed = []
    renamed_full = set(LAST_TO_FULL.values())
    for player, recs in sorted(by.items()):
        exists = stub_path(player).exists()
        if exists and player not in renamed_full:
            continue
        if exists:
            action = insert_missing(player, recs)
            if action == "merge":
                merged += 1
                changed.append(player)
                print("insert", player)
            else:
                skipped += 1
            continue
        rows = []
        events = set()
        srcs = set()
        seen = set()
        for date, event, stage, fmt, finish, dark, light, src in recs:
            key = (event, stage, dark, light)
            if key in seen:
                continue
            seen.add(key)
            rows.append(row_wiki(date, event, stage, fmt, finish, dark, light))
            events.add(event)
            srcs.add(src)
        if not rows:
            continue
        action = upsert(player, rows, events, srcs)
        if action == "create":
            created += 1
            changed.append(player)
        elif action == "merge":
            merged += 1
            changed.append(player)
        else:
            skipped += 1

    # Redirect leftover last-name stubs even if the player was not on a 2025 hub table.
    for last, full in LAST_TO_FULL.items():
        lp = stub_path(last)
        if lp.exists() and last != full:
            t = lp.read_text(encoding="utf-8")
            if not t.startswith("#REDIRECT"):
                if stub_path(full).exists():
                    write_redirect(last, full)
                    print("redirect leftover", last, "->", full)
                    changed.append(last)

    patch_hub_typos()
    still = sorted(p for p in by if not stub_path(p).exists())
    print("created", created, "merged", merged, "skipped", skipped)
    print("still missing", still)
    tsv = ROOT / "y2025-player-titles.tsv"
    lines = []
    for name in sorted(set(changed) | set(by) | set(LAST_TO_FULL) | set(LAST_TO_FULL.values())):
        p = stub_path(name)
        if p.exists():
            lines.append(f"{name}\t{p.relative_to(ROOT).as_posix()}")
    tsv.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("tsv", tsv, "n", len(lines))


if __name__ == "__main__":
    main()
