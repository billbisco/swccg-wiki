#!/usr/bin/env python3
"""2013 Match Play Championship — typed published lists (Legacy Open).

Typed dest: Amar Banger Day 1 Print Form, Keith Brown Day 1 Holotable,
Wayne Cullen Day 1 Print Form. Xerox dest: Barry Alperstein, Nicholas Amato,
John Anderson, Steve Baroni, Andrew Bollentino, Brian Brodsky, Carl Buck,
Matt Carulli, Justin Carulli, Mike D'Ambrosio, Matt Fink, Jerry Heine, Matthew Harrison-Trainor,
Brian Hunter, Brian Herold, Aaron Kinser, Tuan Le, Cole Lepine, Scott Lingrell, Josh Mack,
Sam Marlow, Aaron Nelson, Cuong Nguyen, Chris O'Hara, Matt Paragano, Joe Pinto,
Nick Reisch, Mike Richards, Greg Shaw, Peter Tenneson, Michael Thomas, Mike Tomashewski,
John Veasey, Chris Westergard Day 1. Informal overlay: Rustin Sharer. Incomplete name fields dest as written
(Tony G, Jeremy G, Gogolen, HARPSTER, Stephen Kin, Jared, Pistone,
Shannon, Sokol, BTwigg, Mauer, SAN, Alex W, WIRFS).
Username 3MW0J8 on the Smith sheet is Reid Smith.
Username dashmudtz on the Schwartz sheet is Matt Schmaltz
(2014 Philadelphia Premiere Event Matt Schmaltz LS EBO).
Username stevetotheizzo on the Steve S. sheet is Steve Skilton
(2014 Philadelphia Premiere Event 3rd Place DS Steve Skilton Combat Racing).
Complete names also dested from later Xerox pages: Micah Wall, Steve Wall.
Steve Baroni is the champion (forum.starwarsccg.org/viewtopic.php?t=49932).
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
TSV = ROOT / "y2013-mpc-titles.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2013-events"

EVENT = "2013 Match Play Championship"
DATES = "24–27 January 2013"
TAG = "2013-01-24"
FORMAT = "[[Legacy Open]]"
PC_PDF = "https://starwarsccg.org/phocadownload/2013/2013MPCDecklists.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
WB_PDF = "https://web.archive.org/web/20160806162806/http://www.starwarsccg.org/phocadownload/2013/2013MPCDecklists.pdf"
FORUM = "https://forum.starwarsccg.org/viewforum.php?f=755"
WINNER_THREAD = "https://forum.starwarsccg.org/viewtopic.php?t=49932"
SITE = "New Brunswick, New Jersey"
WINNER = "Steve Baroni"

g15.CANON.update(
    {
        "Amar Banger": "Amar Banger",
        "Steve Baroni": "Steve Baroni",
        "Baroni": "Steve Baroni",
        "Keith Brown": "Keith Brown",
        "Barry Alperstein": "Barry Alperstein",
        "Nicholas Amato": "Nicholas Amato",
        "Nick Amato": "Nicholas Amato",
        "John Anderson": "John Anderson",
        "Casey Anis": "Casey Anis",
        "Andrew Bollentino": "Andrew Bollentino",
        "Brian Brodsky": "Brian Brodsky",
        "Carl Buck": "Carl Buck",
        "Matt Carulli": "Matt Carulli",
        "Matthew Carulli": "Matt Carulli",
        "Justin Carulli": "Justin Carulli",
        "Wayne Cullen": "Wayne Cullen",
        "KissMyWookiee": "Wayne Cullen",
        "Mike Tomashewski": "Mike Tomashewski",
        "Chris Westergard": "Chris Westergard",
        "Brian Herold": "Brian Herold",
        "Brian Hunter": "Brian Hunter",
        "Cole Lepine": "Cole Lepine",
        "Jerry Heine": "Jerry Heine",
        "Joe Pinto": "Joe Pinto",
        "Sam Marlow": "Sam Marlow",
        "Matthew Harrison-Trainor": "Matthew Harrison-Trainor",
        "Matt HT": "Matthew Harrison-Trainor",
        "Matt H-T": "Matthew Harrison-Trainor",
        "Mike D'Ambrosio": "Mike D'Ambrosio",
        "Scott Lingrell": "Scott Lingrell",
        "Nick Reisch": "Nick Reisch",
        "Greg Shaw": "Greg Shaw",
        "Gregory Shaw": "Greg Shaw",
        "Peter Tenneson": "Peter Tenneson",
        "Michael Thomas": "Michael Thomas",
        "John Veasey": "John Veasey",
        "Matt Fink": "Matt Fink",
        "Aaron Kinser": "Aaron Kinser",
        "Tuan Le": "Tuan Le",
        "Josh Mack": "Josh Mack",
        "Aaron Nelson": "Aaron Nelson",
        "Cuong Nguyen": "Cuong Nguyen",
        "Chris O'Hara": "Chris O'Hara",
        "Matt Paragano": "Matt Paragano",
        "Mike Richards": "Mike Richards",
        "Michael Richards": "Mike Richards",
        "Rustin Sharer": "Rustin Sharer",
        "Tony G": "Tony Garcia",
        "Tony Garcia": "Tony Garcia",
        "Jeremy G": "Jeremy G",
        "Gogolen": "Chris Gogolen",
        "Chris Gogolen": "Chris Gogolen",
        "HARPSTER": "Steve Harpster",
        "Steve Harpster": "Steve Harpster",
        "Stephen Kin": "Stephen Kin",
        "Jared": "Jared",
        "Pistone": "Mike Pistone",
        "Mike Pistone": "Mike Pistone",
        "Schwartz": "Matt Schmaltz",
        "Matt Schmaltz": "Matt Schmaltz",
        "Shannon": "Kevin Shannon",
        "Kevin Shannon": "Kevin Shannon",
        "Steve S.": "Steve Skilton",
        "Steve Skilton": "Steve Skilton",
        "Smith": "Reid Smith",
        "Reid Smith": "Reid Smith",
        "Sokol": "Matt Sokol",
        "Matt Sokol": "Matt Sokol",
        "BTwigg": "Brian Terwilliger",
        "Brian Terwilliger": "Brian Terwilliger",
        "Mauer": "Mauer",
        "SAN": "SAN",
        "Micah Wall": "Micah Wall",
        "Steve Wall": "Steve Wall",
        "Alex W": "Alex W",
        "WIRFS": "Chris Wirfs",
        "Chris Wirfs": "Chris Wirfs",
    }
)

HUB_PLAYERS = [
    "Barry Alperstein",
    "Nicholas Amato",
    "John Anderson",
    "Casey Anis",
    "Amar Banger",
    "Steve Baroni",
    "Andrew Bollentino",
    "Brian Brodsky",
    "Keith Brown",
    "Brian Terwilliger",
    "Carl Buck",
    "Matt Carulli",
    "Justin Carulli",
    "Wayne Cullen",
    "Mike D'Ambrosio",
    "Matt Fink",
    "Jeremy G",
    "Tony Garcia",
    "Chris Gogolen",
    "Steve Harpster",
    "Jerry Heine",
    "Brian Herold",
    "Brian Hunter",
    "Jared",
    "Stephen Kin",
    "Aaron Kinser",
    "Tuan Le",
    "Cole Lepine",
    "Scott Lingrell",
    "Josh Mack",
    "Sam Marlow",
    "Mauer",
    "Matthew Harrison-Trainor",
    "Aaron Nelson",
    "Cuong Nguyen",
    "Chris O'Hara",
    "Matt Paragano",
    "Joe Pinto",
    "Mike Pistone",
    "Nick Reisch",
    "Mike Richards",
    "SAN",
    "Matt Schmaltz",
    "Kevin Shannon",
    "Greg Shaw",
    "Rustin Sharer",
    "Steve Skilton",
    "Reid Smith",
    "Matt Sokol",
    "Peter Tenneson",
    "Michael Thomas",
    "Mike Tomashewski",
    "John Veasey",
    "Alex W",
    "Micah Wall",
    "Steve Wall",
    "Chris Westergard",
    "Chris Wirfs",
]

# Last-name sheets that would steal an existing player page.
PLAYER_PAGE = {}


def player_wikilink(p: str) -> str:
    dest = PLAYER_PAGE.get(p, p)
    if dest != p:
        return f"[[{dest}|{p}]]"
    return f"[[{p}]]"


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
        add = [(q, n, v, False) for q, n, v in getattr(mod, "LS_ADD", [])]
        scan = mod.LS_SCAN
        page = mod.LS_PAGE
    else:
        raw = getattr(mod, "DS_CARDS", [])
        if not raw:
            return "", "", "", getattr(mod, "STAGE", "Day 1")
        cards = [(q, n, v, False) for q, n, v in raw]
        shields = [(q, n, v, True) for q, n, v in getattr(mod, "DS_SHIELDS", [])]
        add = [(q, n, v, False) for q, n, v in getattr(mod, "DS_ADD", [])]
        scan = mod.DS_SCAN
        page = mod.DS_PAGE
    n_main = sum(q for q, *_ in cards)
    if n_main != 60:
        print(f"WARN {player} {side} main={n_main} (want 60)")
    groups = mpc.group_cards(cards + shields + add, by_title)
    unknown = [n for h, rows in groups if h == "Unknown" for _q, n, *_ in rows]
    if unknown:
        print(f"WARN {player} {side} Unknown types:", unknown)
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
    title = f"2013 Match Play Championship {stage} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    sources = [
        f"[{PC_PDF} 2013MPCDecklists.pdf], starwarsccg.org",
        f"[{WB_PDF} Wayback Machine], web.archive.org",
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
        player_page=PLAYER_PAGE.get(player),
        username=w14.username_for(mod, side),
    )
    return title, write(title, page_txt), label, stage


def write_hub(dt, hl) -> None:
    def cell(player, stage, side):
        page = dt.get((player, stage, side))
        if page:
            return f"[[{page}|{hl[page]}]]"
        return "—"

    def table(players, stage):
        bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
        for p in players:
            bits += [
                "|-",
                f"| {player_wikilink(p)} || {cell(p, stage, 'Dark')} || {cell(p, stage, 'Light')}",
            ]
        bits.append("|}")
        return "\n".join(bits)

    tbl1 = table(HUB_PLAYERS, "Day 1")
    body = f"""'''2013 Match Play Championship''' was a Players Committee constructed event in New Brunswick, New Jersey, 24–27 January 2013, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="forum">{FORUM}</ref> [[Steve Baroni]] won the championship.<ref name="winner">{WINNER_THREAD}</ref> The published list is the MPC PDF on the Players Committee decklist desk. Dates on the Day 1 sheets are 26 January 2013. The name field on pages 11–12 is Baroni; that player is Steve Baroni. Day 1 sheets whose name field is a last name, first name, last initial, or otherwise incomplete are listed with the name as written.

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' {SITE}
* '''Dates:''' {DATES}
* '''Winner:''' [[{WINNER}]]

== Day 1 ==

{tbl1}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF} 2013MPCDecklists.pdf], starwarsccg.org
* [{WB_PDF} 2013MPCDecklists.pdf (Wayback Machine)], web.archive.org
* [{PC_TDL} Tournament Decklists], starwarsccg.org
* [{FORUM} 2013 Match Play Championship (forum)], forum.starwarsccg.org
* [{WINNER_THREAD} BARONIIII… (winner thread)], forum.starwarsccg.org

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
    old = (
        "| 2013-01-24 || [[2013 Match Play Championship|Match Play Championship]] "
        "|| 24–27 January 2013 || — || [[Legacy Open]] || —\n"
    )
    new = (
        "| 2013-01-24 || [[2013 Match Play Championship|Match Play Championship]] "
        "|| 24–27 January 2013 || New Brunswick, New Jersey || [[Legacy Open]] "
        "|| [[Steve Baroni]]\n"
    )
    if old in text:
        LIST.write_text(text.replace(old, new, 1), encoding="utf-8", newline="\n")
        return
    if "2013 Match Play Championship" in text:
        return
    row = "|- \n" + new
    needle = (
        "| 2013-04-19 || [[2013 Texas Mini Worlds|Texas Mini Worlds]] "
        "|| 19–21 April 2013 || Texas || [[Legacy Open]] || —\n"
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

    mods = [
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_banger.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_brown.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_cullen.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_alperstein.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_amato.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_anderson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_baroni.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_bollentino.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_brodsky.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_buck.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_carulli.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_anis.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_justin_carulli.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_heine.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_harrison_trainor.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_hunter.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_herold.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_lepine.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_marlow.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_pinto.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_tomashewski.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_westergard.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_dambrosio.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_lingrell.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_reisch.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_shaw.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_tenneson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_thomas.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_veasey.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_fink.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_kinser.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_tuan_le.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_mack.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_nelson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_nguyen.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_ohara.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_paragano.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_richards.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_sharer.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_tony_g.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_jeremy_g.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_gogolen.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_harpster.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_kin.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_jared.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_pistone.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_schwartz.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_shannon.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_steve_s.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_smith.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_sokol.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_btwigg.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_mauer.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_san.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_micah_wall.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_steve_wall.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_alex_w.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_mpc_wirfs.py"),
    ]
    for mod in mods:
        for side in ("Dark", "Light"):
            title, rel, label, stage = emit_typed(mod, side, by_title)
            if not title:
                continue
            dt[(mod.PLAYER, stage, side)] = title
            hl[title] = label
            titles.append((title, rel))
            print(stage, side, title, "label", label)

    write_hub(dt, hl)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))

    meta = {
        "title": EVENT,
        "year": "2013",
        "pc": PC_PDF,
        "format": FORMAT,
    }
    player_rows: dict[str, list[str]] = {}
    for mod in mods:
        p = mod.PLAYER
        stage = getattr(mod, "STAGE", "Day 1")
        ds_page = dt.get((p, stage, "Dark"))
        ls_page = dt.get((p, stage, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        row = (
            f"|- \n| {DATES} || [[{EVENT}]] ({stage}) || {FORMAT} "
            f"|| — || {ds} || {ls}"
        )
        player_rows.setdefault(p, []).append(row)
    for p in HUB_PLAYERS:
        if p in player_rows:
            continue
        player_rows[p] = [
            f"|- \n| {DATES} || [[{EVENT}]] (Day 1) || {FORMAT} "
            f"|| — || — || —"
        ]
    for p, rows in player_rows.items():
        dest_p = PLAYER_PAGE.get(p, p)
        if dest_p != p:
            stub_path = STUBS / (dest_p.replace(" ", "_") + ".wiki")
            if stub_path.exists():
                titles.append((dest_p, f"pages/player-stubs/{stub_path.name}"))
            continue
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
