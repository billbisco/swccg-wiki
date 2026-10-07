#!/usr/bin/env python3
"""2014 US Nationals — typed published lists (Legacy Open).

Typed slice: Matthew Harrison-Trainor Day 2 (PDF pages 1–2),
Mike Tomashewski Day 1 (pages 1–2), Brad Eier Day 1 (pages 30–31).
Remaining Xerox sheets are inventoried on the hub.
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
TSV = ROOT / "y2014-nats-titles.tsv"
XEROX_TSV = ROOT / "y2014-nats-xerox-titles.tsv"
MEDIA = ROOT / "y2014-nats-media"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2014-events"
TYPED_STEMS = {
    "transcribe_nats_mht",
    "transcribe_nats_tomashewski",
    "transcribe_nats_eier",
}

EVENT = "2014 US Nationals"
DATES = "13–15 June 2014"
TAG = "2014-06-13"
FORMAT = "[[Legacy Open]]"
PC_PDF_D2 = "https://res.starwarsccg.org/wp/wp-content/uploads/Nationals-2014-day-2.pdf"
PC_PDF_D1 = "https://res.starwarsccg.org/wp/wp-content/uploads/Nationals-2014-day-1.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"

g15.CANON.update(
    {
        "Matt H-T": "Matthew Harrison-Trainor",
        "Matt Harrison-Trainor": "Matthew Harrison-Trainor",
        "Matthew Carulli": "Matt Carulli",
        "Matt Carulli": "Matt Carulli",
        "Chris Twigg": "Chris Terwilliger",
        "Mike Tomashewski": "Mike Tomashewski",
        "Brad Eier": "Brad Eier",
        "Bill Kafer": "Bill Kafer",
        "Nate Louderback": "Nate Louderback",
        "Vince Hutchins": "Vince Hutchins",
        "Matt Sokol": "Matt Sokol",
        "Josh Mack": "Josh Mack",
        "Mike D'Ambrosio": "Mike D'Ambrosio",
        "Kendall Halman": "Kendall Halman",
        "Justin Carulli": "Justin Carulli",
        "Jon Boy": "Jon Boy",
        "Reid Smith": "Reid Smith",
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
        start_name = mod.LS_START
        scan = mod.LS_SCAN
        page = mod.LS_PAGE
        is_v_start = False
    else:
        cards = [(q, n, v, False) for q, n, v in mod.DS_CARDS]
        shields = [(q, n, v, True) for q, n, v in mod.DS_SHIELDS]
        add = [(q, n, v, True) for q, n, v in mod.DS_ADD]
        start_name = mod.DS_START
        scan = mod.DS_SCAN
        page = mod.DS_PAGE
        is_v_start = True if "Hunt Down" in start_name else False
    groups = mpc.group_cards(cards + shields + add, by_title)
    body = mpc.render_groups(groups, side)
    n_obj, is_v, prefer_sh, label = mpc.starting_from_groups(groups, side)
    forced = start_name or ""
    if forced:
        n_obj, is_v = forced, False
        head = forced.split(" / ")[0].strip()
        raw = getattr(mod, "LS_CARDS" if side == "Light" else "DS_CARDS", [])
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
    stage = getattr(mod, "STAGE", "Day 2")
    title = f"2014 US Nationals {stage} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    pdf_url = PC_PDF_D2 if "Day 2" in mod.PDF else PC_PDF_D1
    pdf_label = "Nationals-2014-day-2.pdf" if "Day 2" in mod.PDF else "Nationals-2014-day-1.pdf"
    sources = [
        f"[{pdf_url} {pdf_label}], res.starwarsccg.org",
        f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
    ]
    w14.EVENT = EVENT
    extra_note = (
        w14.extra_note_for(mod, side)
        if leftover
        else "Typed printout (not a handwritten Xerox form)."
    )
    if not write_page:
        return title, "", label, stage
    page_txt = w14.deck_page(
        title,
        player,
        "Light Side" if side == "Light" else "Dark Side",
        start_link,
        stage,
        body,
        sources,
        extra_note=extra_note,
        scan_file=scan,
        scan_caption=f"Page {page} of [[:File:{mod.PDF}]].",
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
            bits += ["|-", f"| [[{p}]] || {cell(p, stage, 'Dark')} || {cell(p, stage, 'Light')}"]
        bits.append("|}")
        return "\n".join(bits)

    d2 = [
        "Matthew Harrison-Trainor",
        "Matt Sokol",
        "Matt Carulli",
        "Chris Terwilliger",
    ]
    d1 = [
        "Mike Tomashewski",
        "Brad Eier",
        "Bill Kafer",
    ]
    extra1, extra2 = [], []
    for p, stage, _side in dt:
        if stage == "Day 1" and p not in d1 and p not in extra1:
            extra1.append(p)
        if stage == "Day 2" and p not in d2 and p not in extra2:
            extra2.append(p)
    d1 = d1 + extra1
    d2 = d2 + extra2
    tbl2 = table(d2, "Day 2")
    tbl1 = table(d1, "Day 1")
    body = f"""'''2014 US Nationals''' was a Players Committee constructed event, 13–15 June 2014, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="tdl">{PC_TDL}</ref> Published lists are the Day 1 and Day 2 PDFs on the Players Committee decklist desk. Typed printouts on this page are [[Matthew Harrison-Trainor]] Day 2, [[Mike Tomashewski]] Day 1, and [[Brad Eier]] Day 1. Xerox Day 1 and Day 2 sheets from the same event are listed below as those scans are transcribed. [[Matthew Harrison-Trainor]] is the published US National Champion.<ref name="winners">https://www.starwarsccg.org/major-event-winners/</ref>

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' —
* '''Dates:''' {DATES}
* '''Winner:''' [[Matthew Harrison-Trainor]]

== Day 2 ==

{tbl2}

Remaining Day 2 Xerox sheets are in [[:File:2014 US Nationals Day 2.pdf]].

== Day 1 ==

{tbl1}

Remaining Day 1 Xerox sheets are in [[:File:2014 US Nationals Day 1.pdf]].

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF_D2} Nationals-2014-day-2.pdf], res.starwarsccg.org
* [{PC_PDF_D1} Nationals-2014-day-1.pdf], res.starwarsccg.org
* [{PC_TDL} Tournament Decklists], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2014]]
"""
    (PAGES / wiki_fname(EVENT)).write_text(
        body.replace("\r\n", "\n"), encoding="utf-8", newline="\n"
    )


def patch_list() -> None:
    text = LIST.read_text(encoding="utf-8")
    row = (
        f"| 2014-06-13 || [[2014 US Nationals|US Nationals]] "
        f"|| 13–15 June 2014 || — || [[Legacy Open]] || —"
    )
    if "2014 US Nationals" in text:
        # keep existing; still rewrite if we need to move it
        return
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
        _load_mod(ROOT / "encyclopedia" / "pc-2014-events" / "transcribe_nats_mht.py"),
        _load_mod(ROOT / "encyclopedia" / "pc-2014-events" / "transcribe_nats_tomashewski.py"),
        _load_mod(ROOT / "encyclopedia" / "pc-2014-events" / "transcribe_nats_eier.py"),
    ]
    for mod in mods:
        for side in ("Dark", "Light"):
            title, rel, label, stage = emit_typed(mod, side, by_title)
            player = g15.CANON.get(mod.PLAYER, mod.PLAYER)
            dt[(player, stage, side)] = title
            hl[title] = label
            titles.append((title, rel))
            print(stage, side, title, "label", label)

    write_hub(dt, hl)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))

    meta = {
        "title": EVENT,
        "year": "2014",
        "pc": PC_PDF_D2,
        "format": FORMAT,
    }
    for mod in mods:
        p = g15.CANON.get(mod.PLAYER, mod.PLAYER)
        stage = getattr(mod, "STAGE", "Day 2")
        ds_page = dt.get((p, stage, "Dark"))
        ls_page = dt.get((p, stage, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        row = (
            f"|- \n| {DATES} || [[{EVENT}]] ({stage}) || {FORMAT} "
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
    """Emit Xerox leftover pages only. Do not rewrite typed MHT/Tomashewski/Eier decks."""
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
            title, _rel, label, stage = emit_typed(
                mod, side, by_title, write_page=False
            )
            if not title:
                continue
            dt[(player, stage, side)] = title
            hl[title] = label

    xerox_mods = []
    for path in sorted(EVENTS_DIR.glob("transcribe_nats_*.py")):
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
            dt[(player, stage, side)] = title
            hl[title] = label
            titles.append((title, rel))
            print("xerox", stage, side, title, "label", label)

    write_hub(dt, hl)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))

    meta = {
        "title": EVENT,
        "year": "2014",
        "pc": PC_PDF_D1,
        "format": FORMAT,
    }
    player_rows: dict[str, list[str]] = {}
    for mod in xerox_mods:
        p = g15.CANON.get(mod.PLAYER, mod.PLAYER)
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
    XEROX_TSV.write_text(
        "".join(f"{t}\t{r}\n" for t, r in ordered), encoding="utf-8", newline="\n"
    )
    print("xerox tsv", XEROX_TSV, "n", len(ordered))


if __name__ == "__main__":
    if "--xerox" in sys.argv:
        leftover_xerox()
    else:
        main()
