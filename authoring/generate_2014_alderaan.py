#!/usr/bin/env python3
"""2014 Alderaan Regionals — confirmed published lists (Legacy Open).

Xerox/typed sheets for Ganden Yanaga, Anthony Massung, Peter Huderich,
and Roy McCarthy. Remaining unconfirmed-name sheets stay on the hub as —.
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
TSV = ROOT / "y2014-alderaan-titles.tsv"
XEROX_TSV = ROOT / "y2014-alderaan-xerox-titles.tsv"
MEDIA = ROOT / "y2014-alderaan-media"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2014-events"
TYPED_STEMS = {
    "transcribe_alderaan_yanaga",
    "transcribe_alderaan_massung",
    "transcribe_alderaan_huderich",
    "transcribe_alderaan_mccarthy",
}

EVENT = "2014 Alderaan Regionals"
DATES = "28 June 2014"
FORMAT = "[[Legacy Open]]"
PC_PDF = "https://res.starwarsccg.org/wp/wp-content/uploads/2014-Alderaan-Regionals.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"

g15.CANON.update(
    {
        "Ganden Yanaga": "Ganden Yanaga",
        "Anthony Massung": "Anthony Massung",
        "Peter Huderich": "Peter Huderich",
        "Roy McCarthy": "Roy McCarthy",
        "Nathan": "Nathan",
        "Nathan T": "Nathan",
        "Steve": "Steve",
        "Gabe": "Gabe",
        "Jeffrey W": "Jeffrey W",
        "Adam K": "Adam K",
        "Brandon": "Brandon",
    }
)

PLAYERS = [
    "Ganden Yanaga",
    "Anthony Massung",
    "Peter Huderich",
    "Roy McCarthy",
]


def _load_mod(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def write(title: str, text: str) -> str:
    fn = wiki_fname(title)
    if not fn.endswith(".wiki"):
        fn += ".wiki"
    path = PAGES / fn
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return f"pages/{fn}"


def emit_typed(
    mod, side: str, by_title, write_page: bool = True, leftover: bool = False
) -> tuple[str, str, str, str]:
    player = g15.CANON.get(mod.PLAYER, mod.PLAYER)
    if side == "Light":
        cards = [(q, n, v, False) for q, n, v in mod.LS_CARDS]
        shields = [(q, n, v, True) for q, n, v in mod.LS_SHIELDS]
        add = [(q, n, v, True) for q, n, v in mod.LS_ADD]
        scan = mod.LS_SCAN
        page = mod.LS_PAGE
    else:
        cards = [(q, n, v, False) for q, n, v in mod.DS_CARDS]
        shields = [(q, n, v, True) for q, n, v in mod.DS_SHIELDS]
        add = [(q, n, v, True) for q, n, v in mod.DS_ADD]
        scan = mod.DS_SCAN
        page = mod.DS_PAGE
    n_main = sum(q for q, *_ in cards)
    if n_main != 60:
        print(f"WARN {player} {side} main={n_main} (want 60)")
    groups = mpc.group_cards(cards + shields + add, by_title)
    body = mpc.render_groups(groups, side)
    n_obj, is_v, prefer_sh, label = mpc.starting_from_groups(groups, side)
    start_link = w14.wikilink(n_obj, side, is_v, prefer_sh=prefer_sh)
    title = f"2014 Alderaan Regionals {player} {'LS' if side == 'Light' else 'DS'} {label}"
    sources = [
        f"[{PC_PDF} 2014-Alderaan-Regionals.pdf], res.starwarsccg.org",
        f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
    ]
    w14.EVENT = EVENT
    extra_note = (
        w14.extra_note_for(mod, side)
        if leftover
        else getattr(mod, "NOTE", "Handwritten Xerox form.")
    )
    if not write_page:
        return title, "", label, "Regionals"
    page_txt = w14.deck_page(
        title,
        player,
        "Light Side" if side == "Light" else "Dark Side",
        start_link,
        "Regionals",
        body,
        sources,
        extra_note=extra_note,
        scan_file=scan,
        scan_caption=f"Page {page} of [[:File:{mod.PDF}]].",
        username=w14.username_for(mod, side),
    )
    return title, write(title, page_txt), label, "Regionals"


def write_hub(dt, hl) -> None:
    def cell(player, side):
        page = dt.get((player, side))
        if page:
            return f"[[{page}|{hl[page]}]]"
        return "—"

    bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
    seen = list(PLAYERS)
    for p, _side in dt:
        if p not in seen:
            seen.append(p)
    for p in seen:
        bits += ["|-", f"| [[{p}]] || {cell(p, 'Dark')} || {cell(p, 'Light')}"]
    bits.append("|}")
    tbl = "\n".join(bits)
    body = f"""'''2014 Alderaan Regionals''' was a Players Committee constructed regional, 28 June 2014, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="tdl">{PC_TDL}</ref> Published lists are the 20-page PDF on the Players Committee decklist desk. Xerox sheets from the same event are listed below as those scans are transcribed. The PDF does not name a champion.

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' —
* '''Dates:''' {DATES}
* '''Winner:''' —

== Published lists ==

{tbl}

Remaining sheets are in [[:File:2014 Alderaan Regionals.pdf]].

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF} 2014-Alderaan-Regionals.pdf], res.starwarsccg.org
* [{PC_TDL} Tournament Decklists], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2014]]
"""
    write(EVENT, body)


def patch_list() -> None:
    text = LIST.read_text(encoding="utf-8")
    if "2014 Alderaan Regionals" in text:
        return
    row = (
        f"| 2014-06-28 || [[2014 Alderaan Regionals|Alderaan Regionals]] "
        f"|| 28 June 2014 || — || [[Legacy Open]] || —"
    )
    needle = (
        "| 2014-08-21 || [[2014 World Championship|World Championship]] || "
        "21–24 August 2014 || Toronto, Ontario || [[Legacy Open]] || [[Emil Wallin]]"
    )
    if needle in text:
        text = text.replace(needle, needle + "\n|- \n" + row, 1)
        LIST.write_text(text, encoding="utf-8", newline="\n")
        return
    m = re.search(r"(== 2014 ==.*?)\|}\n", text, re.S)
    if m:
        text = text[: m.end() - 3] + "|- \n" + row + "\n|}\n" + text[m.end() :]
        LIST.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    STUBS.mkdir(parents=True, exist_ok=True)
    _by_id, by_title = load_bp_simple()
    mpc.load_wiki_types()
    w14.EVENT = EVENT
    titles: list[tuple[str, str]] = []
    dt, hl = {}, {}

    mods = [
        _load_mod(EVENTS_DIR / "transcribe_alderaan_yanaga.py"),
        _load_mod(EVENTS_DIR / "transcribe_alderaan_massung.py"),
        _load_mod(EVENTS_DIR / "transcribe_alderaan_huderich.py"),
        _load_mod(EVENTS_DIR / "transcribe_alderaan_mccarthy.py"),
    ]
    for mod in mods:
        for side in ("Dark", "Light"):
            title, rel, label, stage = emit_typed(mod, side, by_title)
            dt[(mod.PLAYER, side)] = title
            hl[title] = label
            titles.append((title, rel))
            print(stage, side, title, "label", label)

    write_hub(dt, hl)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))

    meta = {
        "title": EVENT,
        "year": "2014",
        "pc": PC_PDF,
        "format": FORMAT,
    }
    for mod in mods:
        p = mod.PLAYER
        ds_page = dt.get((p, "Dark"))
        ls_page = dt.get((p, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        row = (
            f"|- \n| {DATES} || [[{EVENT}]] || {FORMAT} "
            f"|| — || {ds} || {ls}"
        )
        got = g15.upsert_player(p, [row], meta)
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


def leftover_xerox() -> None:
    """Emit Xerox leftover pages only. Do not rewrite typed Yanaga/Massung/Huderich/McCarthy decks."""
    STUBS.mkdir(parents=True, exist_ok=True)
    _by_id, by_title = load_bp_simple()
    mpc.load_wiki_types()
    w14.EVENT = EVENT
    titles: list[tuple[str, str]] = []
    dt, hl = {}, {}

    for stem in sorted(TYPED_STEMS):
        path = EVENTS_DIR / f"{stem}.py"
        if not path.exists():
            continue
        mod = _load_mod(path)
        player = g15.CANON.get(mod.PLAYER, mod.PLAYER)
        for side in ("Dark", "Light"):
            title, _rel, label, _stage = emit_typed(
                mod, side, by_title, write_page=False
            )
            if not title:
                continue
            dt[(player, side)] = title
            hl[title] = label

    xerox_mods = []
    for path in sorted(EVENTS_DIR.glob("transcribe_alderaan_*.py")):
        if path.stem in TYPED_STEMS:
            continue
        xerox_mods.append(_load_mod(path))
    for mod in xerox_mods:
        player = g15.CANON.get(mod.PLAYER, mod.PLAYER)
        for side in ("Dark", "Light"):
            title, rel, label, stage = emit_typed(
                mod, side, by_title, write_page=True, leftover=True
            )
            if not title:
                continue
            dt[(player, side)] = title
            hl[title] = label
            titles.append((title, rel))
            print("xerox", stage, side, title, "label", label)

    write_hub(dt, hl)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))

    meta = {
        "title": EVENT,
        "year": "2014",
        "pc": PC_PDF,
        "format": FORMAT,
    }
    for mod in xerox_mods:
        p = g15.CANON.get(mod.PLAYER, mod.PLAYER)
        ds_page = dt.get((p, "Dark"))
        ls_page = dt.get((p, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        row = (
            f"|- \n| {DATES} || [[{EVENT}]] || {FORMAT} "
            f"|| — || {ds} || {ls}"
        )
        got = g15.upsert_player(p, [row], meta)
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
    XEROX_TSV.write_text(
        "".join(f"{t}\t{r}\n" for t, r in ordered), encoding="utf-8", newline="\n"
    )
    print("xerox tsv", XEROX_TSV, "n", len(ordered))


if __name__ == "__main__":
    if "--xerox" in sys.argv:
        leftover_xerox()
    else:
        main()
