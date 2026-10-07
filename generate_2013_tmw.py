#!/usr/bin/env python3
"""2013 Texas Mini Worlds — typed published lists (Legacy Open).

Typed slice: Nick Reisch, Mike Richards, Evan Kirkpatrick, James Barnes.
Xerox leftover LIVE: Aaron Nelson Day 1 WYS / NMNPND (Username Airdog2003).
Xerox leftover LIVE: Robbie Hendon Day 1 Senate (Username /hendon).
Xerox leftover LIVE: Greg Shaw Day 1 Hunt Down (V) (Username blank;
p08 Light empty Same as Barry, no Light 60).
Xerox leftover LIVE: Greg Shaw Day 1 Agents / TIGIH second pair
(Username blank; p09 Dark Werewolf Tech / p10 Light Good Luck Choosing Four).
Xerox leftover LIVE: Steve Baroni Day 1 Hunt Down (V) / TIGIH
(Username blank; p14 Dark MIKE likes / p15 Light Are You?).
Xerox leftover LIVE: Bobby Hilbun Day 1 Ralltiir Operations / Communing
(Username blank; p16 Dark Ral OPS / p17 Light Communichkin).
Xerox leftover LIVE: JW Millet Day 1 TIGIH / A Stunning Move
(Username Asphalizo; p20 Light What Else?! / p21 Dark Hunt's Deck).
Xerox leftover LIVE: Steve Skilton Day 1 TIGIH
(Username blank; p24 Light Baroni's TIGIH; Dark unpublished).
Xerox leftover LIVE: Steve Izzo Day 1 Contract Killers
(Username blank; p25 Dark; Light unpublished).
Xerox leftover LIVE: Brian Herold Day 1 Hyperdrive / Contract Killers
(Username Carly Rae Cyrus Light / Psy Snootles Dark;
p26 Light Achy Breaky, Maybe? / p27 Dark WHOOPAH! Goo Nee Style).
Xerox leftover LIVE: Blake Huffman Day 1 CCT / Hyperdrive
(Username blank; p28 Dark / p29 Light).
Xerox leftover LIVE: John Anderson Day 1 Contract Killers / WYS
(Username Puck71 Dark / puck71 Light; p30 Dark / p31 Light).
Xerox leftover LIVE: Barry Alperstein Day 1 Hunt Down (V) / MWYHL (V)
(Username blank; p32 Dark / p33 Light signed Barry A + Matt S).
Xerox leftover LIVE: Amar Banger Day 1 AFA (V) / K&D (V)
(Username abanger; p34 Light The 1/1 Deck / p35 Dark ATL Mistryl).
Xerox leftover LIVE: Allen Gamble Day 1 typed AFA (V) / K&D (V)
(Username blank; p37 Light AFAv WYSv / p36 Dark K&D v ASM).
Xerox leftover LIVE: Olaf Schroeder Day 1 Hunt Down (V) / Plead My Case
(Username Joe Freedom; p38 Dark Search & Destroy / p39 Light Senate Redemption).
Xerox leftover this slice: Matt Wehner Day 1 typed MWYHL / SYCFA
(Username blank; p40 Light a jedi's plans / p41 Dark Set your course).
Always dest incomplete/blank names as written. A player with two published
Day 1 pairs gets both hub rows.
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2014_mpc as mpc  # noqa: E402
import generate_2014_worlds as w14  # noqa: E402
import generate_2015_2016 as g15  # noqa: E402
from generate_2019_2021 import tidy_player_page, wiki_fname  # noqa: E402
from generate_2026_sdso import load_bp_simple  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
TSV = ROOT / "y2013-tmw-titles.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2013-events"

EVENT = "2013 Texas Mini Worlds"
DATES = "19–21 April 2013"
TAG = "2013-04-19"
FORMAT = "[[Legacy Open]]"
PC_PDF_D1 = "https://starwarsccg.org/phocadownload/2013/2013TMWDay1.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
WB_D1 = "https://web.archive.org/web/20160806225452/https://starwarsccg.org/phocadownload/2013/2013TMWDay1.pdf"

g15.CANON.update(
    {
        "Nick Reisch": "Nick Reisch",
        "Aaron Nelson": "Aaron Nelson",
        "Robbie Hendon": "Robbie Hendon",
        "Greg Shaw": "Greg Shaw",
        "Gregory Shaw": "Greg Shaw",
        "Steve Baroni": "Steve Baroni",
        "Baroni": "Steve Baroni",
        "Michael Richards": "Mike Richards",
        "Mike Richards": "Mike Richards",
        "Evan Kirkpatrick": "Evan Kirkpatrick",
        "James Barnes": "James Barnes",
        "Bobby Hilbun": "Bobby Hilbun",
        "JW Millet": "JW Millet",
        "Steve Skilton": "Steve Skilton",
        "Steve Izzo": "Steve Izzo",
        "Brian Herold": "Brian Herold",
        "Blake Huffman": "Blake Huffman",
        "John Anderson": "John Anderson",
        "Barry Alperstein": "Barry Alperstein",
        "Amar Banger": "Amar Banger",
        "Allen Gamble": "Allen Gamble",
        "Olaf Schroeder": "Olaf Schroeder",
        "Matt Wehner": "Matt Wehner",
    }
)


def _load_mod(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write(title: str, text: str) -> str:
    fn = wiki_fname(title)
    if not fn.endswith(".wiki"):
        fn += ".wiki"
    fn = fn.replace(":", "_")
    path = PAGES / fn
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return f"pages/{fn}"


def emit_typed(mod, side: str, by_title) -> tuple[str, str, str, str]:
    player = mod.PLAYER
    if side == "Light":
        raw = getattr(mod, "LS_CARDS", [])
        if not raw:
            return "", "", "", getattr(mod, "STAGE", "Day 1")
        cards = [(q, n, v, False) for q, n, v in raw]
        shields = [(q, n, v, True) for q, n, v in getattr(mod, "LS_SHIELDS", [])]
        add = [(q, n, v, True) for q, n, v in getattr(mod, "LS_ADD", [])]
        scan = mod.LS_SCAN
        page = mod.LS_PAGE
    else:
        raw = getattr(mod, "DS_CARDS", [])
        if not raw:
            return "", "", "", getattr(mod, "STAGE", "Day 1")
        cards = [(q, n, v, False) for q, n, v in raw]
        shields = [(q, n, v, True) for q, n, v in getattr(mod, "DS_SHIELDS", [])]
        add = [(q, n, v, True) for q, n, v in getattr(mod, "DS_ADD", [])]
        scan = mod.DS_SCAN
        page = mod.DS_PAGE
    n_main = sum(q for q, *_ in cards)
    if n_main != 60:
        print(f"WARN {player} {side} main={n_main} (want 60)")
    groups = mpc.group_cards(cards + shields + add, by_title)
    body = mpc.render_groups(groups, side)
    n_obj, is_v, prefer_sh, label = mpc.starting_from_groups(groups, side)
    forced = getattr(mod, "LS_START" if side == "Light" else "DS_START", "") or ""
    if forced:
        n_obj, is_v = forced, False
        head = forced.split(" / ")[0].strip()
        for _q, n, v in raw:
            if n == forced or n.startswith(head):
                is_v = v
                if " / " in n:
                    n_obj = n
                break
        label = n_obj.split(" / ")[0].strip()
        dest = w14._lookup(n_obj, side, is_v) or ""
        if dest and "(V)" in dest and not label.endswith("(V)"):
            label = re.sub(r"\s*\(V\)\s*$", "", label) + " (V)"
    start_link = w14.wikilink(n_obj, side, is_v, prefer_sh=prefer_sh)
    stage = getattr(mod, "STAGE", "Day 1")
    title = f"2013 Texas Mini Worlds {stage} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    sources = [
        f"[{PC_PDF_D1} 2013TMWDay1.pdf], starwarsccg.org",
        f"[{WB_D1} Wayback Machine], web.archive.org",
        f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
    ]
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2013]]"
    extra_scans = getattr(
        mod, "LS_EXTRA_SCANS" if side == "Light" else "DS_EXTRA_SCANS", None
    )
    page_txt = w14.deck_page(
        title,
        player,
        "Light Side" if side == "Light" else "Dark Side",
        start_link,
        stage,
        body,
        sources,
        extra_note=w14.extra_note_for(mod, side),
        scan_file=scan,
        scan_caption=f"Page {page} of [[:File:{mod.PDF}]].",
        extra_scans=extra_scans,
        username=w14.username_for(mod, side),
    )
    return title, write(title, page_txt), label, stage


def write_hub(dt, hl, pairs) -> None:
    def cell(player, stage, side):
        page = dt.get((player, stage, side))
        if page:
            return f"[[{page}|{hl[page]}]]"
        return "—"

    def cell_pair(pair, side):
        page = pair.get(side)
        if page:
            return f"[[{page}|{hl[page]}]]"
        return "—"

    def table(players, stage):
        bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
        for p in players:
            p_pairs = [x for x in pairs if x["player"] == p and x["stage"] == stage]
            if len(p_pairs) > 1:
                for pair in p_pairs:
                    bits += [
                        "|-",
                        f"| [[{p}]] || {cell_pair(pair, 'Dark')} || {cell_pair(pair, 'Light')}",
                    ]
                continue
            bits += [
                "|-",
                f"| [[{p}]] || {cell(p, stage, 'Dark')} || {cell(p, stage, 'Light')}",
            ]
        bits.append("|}")
        return "\n".join(bits)

    d1 = [
        "Nick Reisch",
        "Aaron Nelson",
        "Robbie Hendon",
        "Greg Shaw",
        "Mike Richards",
        "Steve Baroni",
        "Bobby Hilbun",
        "Evan Kirkpatrick",
        "JW Millet",
        "James Barnes",
        "Steve Skilton",
        "Steve Izzo",
        "Brian Herold",
        "Blake Huffman",
        "John Anderson",
        "Barry Alperstein",
        "Amar Banger",
        "Allen Gamble",
        "Olaf Schroeder",
        "Matt Wehner",
    ]
    tbl1 = table(d1, "Day 1")
    body = f"""'''2013 Texas Mini Worlds''' was a Players Committee constructed event, 19–21 April 2013, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="tdl">{PC_TDL}</ref> The published list is the Day 1 PDF on the Players Committee decklist desk. Dates on the sheets are 20 April 2013. Published Day 1 lists on this page are [[Nick Reisch]], [[Aaron Nelson]], [[Robbie Hendon]], [[Greg Shaw]], [[Mike Richards]], [[Steve Baroni]], [[Bobby Hilbun]], [[Evan Kirkpatrick]], [[JW Millet]], [[James Barnes]], [[Steve Skilton]], [[Steve Izzo]], [[Brian Herold]], [[Blake Huffman]], [[John Anderson]], [[Barry Alperstein]], [[Amar Banger]], [[Allen Gamble]], [[Olaf Schroeder]], and [[Matt Wehner]]. Sheets signed only with a last name, first name, last initial, or an unreadable name are omitted until the player is confirmed. The PDF does not name a champion.

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' Texas
* '''Dates:''' {DATES}
* '''Winner:''' —

== Day 1 ==

{tbl1}

Remaining Day 1 Xerox and typed slang sheets are in [[:File:2013 Texas Mini Worlds Day 1.pdf]].

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF_D1} 2013TMWDay1.pdf], starwarsccg.org
* [{WB_D1} 2013TMWDay1.pdf (Wayback Machine)], web.archive.org
* [{PC_TDL} Tournament Decklists], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2013]]
"""
    (PAGES / wiki_fname(EVENT)).write_text(
        body.replace("\r\n", "\n"), encoding="utf-8", newline="\n"
    )


def patch_list() -> None:
    text = LIST.read_text(encoding="utf-8")
    if "2013 Texas Mini Worlds" in text:
        return
    row = (
        "|- \n"
        "| 2013-04-19 || [[2013 Texas Mini Worlds|Texas Mini Worlds]] "
        "|| 19–21 April 2013 || Texas || [[Legacy Open]] || —\n"
    )
    needle = (
        "| 2013-08-09 || [[2013 World Championship|World Championship]] "
        "|| 9–11 August 2013 || — || [[Legacy Open]] || —\n"
    )
    if needle in text:
        text = text.replace(needle, needle + row, 1)
        LIST.write_text(text, encoding="utf-8", newline="\n")
        return
    m = re.search(r"(== 2013 ==.*?)\|}\n", text, re.S)
    if not m:
        raise SystemExit("List of tournaments missing 2013 section")
    text = text[: m.end() - 3] + row + "|}\n" + text[m.end() :]
    LIST.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    STUBS.mkdir(parents=True, exist_ok=True)
    _by_id, by_title = load_bp_simple()
    mpc.load_wiki_types()
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2013]]"
    titles: list[tuple[str, str]] = []
    dt, hl = {}, {}
    pairs: list[dict] = []

    mods = [
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_reisch.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_nelson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_hendon.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_shaw.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_shaw_agents.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_richards.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_baroni.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_hilbun.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_kirkpatrick.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_millet.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_barnes.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_skilton.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_izzo.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_herold.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_huffman.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_anderson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_alperstein.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_banger.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_gamble.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_schroeder.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_tmw_wehner.py"),
    ]
    for mod in mods:
        pair = {
            "player": mod.PLAYER,
            "stage": getattr(mod, "STAGE", "Day 1"),
            "Dark": None,
            "Light": None,
        }
        for side in ("Dark", "Light"):
            title, rel, label, stage = emit_typed(mod, side, by_title)
            if not title:
                continue
            pair[side] = title
            dt[(mod.PLAYER, stage, side)] = title
            hl[title] = label
            titles.append((title, rel))
            print(stage, side, title, "label", label)
        pairs.append(pair)

    write_hub(dt, hl, pairs)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))

    meta = {
        "title": EVENT,
        "year": "2013",
        "pc": PC_PDF_D1,
        "format": FORMAT,
    }
    player_rows: dict[str, list[str]] = {}
    for pair in pairs:
        p = pair["player"]
        stage = pair["stage"]
        ds_page = pair["Dark"]
        ls_page = pair["Light"]
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        row = (
            f"|- \n| {DATES} || [[{EVENT}]] ({stage}) || {FORMAT} "
            f"|| — || {ds} || {ls}"
        )
        player_rows.setdefault(p, []).append(row)
    for p in (
        "Aaron Nelson",
        "Robbie Hendon",
        "Greg Shaw",
        "Bobby Hilbun",
        "JW Millet",
        "Steve Skilton",
        "Steve Izzo",
        "Brian Herold",
        "Blake Huffman",
        "John Anderson",
        "Barry Alperstein",
        "Amar Banger",
        "Allen Gamble",
        "Olaf Schroeder",
        "Matt Wehner",
    ):
        if p in player_rows:
            continue
        player_rows[p] = [
            f"|- \n| {DATES} || [[{EVENT}]] (Day 1) || {FORMAT} "
            f"|| — || — || —"
        ]
    for p, rows in player_rows.items():
        got = g15.upsert_player(p, rows, meta)
        if got:
            titles.append(got)
            for cand in (PAGES / wiki_fname(p), STUBS / (p.replace(" ", "_") + ".wiki")):
                if cand.exists():
                    tidy_player_page(cand)

    patch_list()
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))

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
    print("tsv", TSV, "n", len(ordered))


if __name__ == "__main__":
    main()
