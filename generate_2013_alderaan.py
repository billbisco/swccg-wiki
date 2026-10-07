#!/usr/bin/env python3
"""2013 Alderaan Regionals — typed published lists (Legacy Open).

Typed dest: Jellison, Menzel, Yanaga, Derlin, Massung LS, McCarthy.
Xerox dest: Harrison-Trainor LS+DS, Atkin LS+DS, Massung DS,
Tom LS+DS, Kevin Shannon LS+DS, Chris Schoenthal LS+DS, Nathan LS+DS.
Skip sheets from other events bound into the PDF (California States, U.S. Nationals).
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
TSV = ROOT / "y2013-alderaan-titles.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2013-events"

EVENT = "2013 Alderaan Regionals"
DATES = "13–14 July 2013"
FORMAT = "[[Legacy Open]]"
PC_PDF = "https://starwarsccg.org/phocadownload/2013/2013AlderaanRegionals.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
WB_PDF = "https://web.archive.org/web/20160806162806/http://www.starwarsccg.org/phocadownload/2013/2013AlderaanRegionals.pdf"

g15.CANON.update(
    {
        "Ryan Jellison": "Ryan Jellison",
        "Clayton Atkin": "Clayton Atkin",
        "Bren Derlin": "Bren Derlin",
        "Chris Menzel": "Chris Menzel",
        "Ganden Yanaga": "Ganden Yanaga",
        "Camden Yanaga": "Ganden Yanaga",
        "Anthony Massung": "Anthony Massung",
        "Roy McCarthy": "Roy McCarthy",
        "Matthew Harrison-Trainor": "Matthew Harrison-Trainor",
        "Matt HT": "Matthew Harrison-Trainor",
        "Matt H-T": "Matthew Harrison-Trainor",
        "Tom": "Tom",
        "Shannon": "Kevin Shannon",
        "Kevin Shannon": "Kevin Shannon",
        "Chris Schoenthal": "Chris Schoenthal",
        "Nathan": "Nathan",
    }
)

HUB_PLAYERS = [
    "Clayton Atkin",
    "Bren Derlin",
    "Ryan Jellison",
    "Anthony Massung",
    "Roy McCarthy",
    "Chris Menzel",
    "Matthew Harrison-Trainor",
    "Ganden Yanaga",
    "Tom",
    "Kevin Shannon",
    "Chris Schoenthal",
    "Nathan",
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
    fn = fn.replace(":", "_")
    path = PAGES / fn
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return f"pages/{fn}"


def emit_typed(mod, side: str, by_title) -> tuple[str, str, str]:
    player = mod.PLAYER
    if side == "Light":
        raw = getattr(mod, "LS_CARDS", [])
        if not raw:
            return "", "", ""
        cards = [(q, n, v, False) for q, n, v in raw]
        shields = [(q, n, v, True) for q, n, v in getattr(mod, "LS_SHIELDS", [])]
        add = [(q, n, v, True) for q, n, v in getattr(mod, "LS_ADD", [])]
        scan = mod.LS_SCAN
        page = mod.LS_PAGE
    else:
        raw = getattr(mod, "DS_CARDS", [])
        if not raw:
            return "", "", ""
        cards = [(q, n, v, False) for q, n, v in raw]
        shields = [(q, n, v, True) for q, n, v in getattr(mod, "DS_SHIELDS", [])]
        add = [(q, n, v, True) for q, n, v in getattr(mod, "DS_ADD", [])]
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
    title = f"2013 Alderaan Regionals {player} {'LS' if side == 'Light' else 'DS'} {label}"
    sources = [
        f"[{PC_PDF} 2013AlderaanRegionals.pdf], starwarsccg.org",
        f"[{WB_PDF} Wayback Machine], web.archive.org",
        f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
    ]
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2013]]"
    page_txt = w14.deck_page(
        title,
        player,
        "Light Side" if side == "Light" else "Dark Side",
        start_link,
        "Regionals",
        body,
        sources,
        extra_note=w14.extra_note_for(mod, side),
        scan_file=scan,
        scan_caption=f"Page {page} of [[:File:{mod.PDF}]].",
        username=w14.username_for(mod, side),
    )
    return title, write(title, page_txt), label


def write_hub(dt, hl) -> None:
    def cell(player, side):
        page = dt.get((player, side))
        if page:
            return f"[[{page}|{hl[page]}]]"
        return "—"

    bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
    for p in HUB_PLAYERS:
        bits += ["|-", f"| [[{p}]] || {cell(p, 'Dark')} || {cell(p, 'Light')}"]
    bits.append("|}")
    tbl = "\n".join(bits)
    body = f"""'''2013 Alderaan Regionals''' was a Players Committee constructed regional, 13–14 July 2013, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="tdl">{PC_TDL}</ref> The published list is the Alderaan Regionals PDF on the Players Committee decklist desk. Dates on the sheets are 13 July 2013, with [[Roy McCarthy]] Dark dated 14 July 2013. Typed printouts dested on this page are [[Ryan Jellison]], [[Chris Menzel]], [[Ganden Yanaga]], [[Bren Derlin]], [[Anthony Massung]] Light, and [[Roy McCarthy]]. Xerox dested on this page are [[Matthew Harrison-Trainor]], [[Clayton Atkin]], Massung Dark, [[Tom]], [[Kevin Shannon]], [[Chris Schoenthal]], and [[Nathan]]. Sheets from other events bound into the same PDF (California States, U.S. Nationals) are omitted. The PDF does not name a champion. [[Ganden Yanaga]] is typed Camden Yanaga on the sheet (username Cam Solusar). [[Chris Menzel]] spreadsheets are headed California / California 2013 and dated 13 July 2013. Name field Matt HT is dested [[Matthew Harrison-Trainor]]. Name field Shannon is dested [[Kevin Shannon]]. Name field Chris Schowthyl (username imrhil327) is dested [[Chris Schoenthal]]. Name fields Tom and Nathan are dested as written (same SoCal Tom and Nathan).

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' —
* '''Dates:''' {DATES}
* '''Winner:''' —

== Published lists ==

{tbl}

Remaining Day Xerox and typed slang sheets are in [[:File:2013 Alderaan Regionals.pdf]].

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF} 2013AlderaanRegionals.pdf], starwarsccg.org
* [{WB_PDF} 2013AlderaanRegionals.pdf (Wayback Machine)], web.archive.org
* [{PC_TDL} Tournament Decklists], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2013]]
"""
    write(EVENT, body)


def patch_list() -> None:
    text = LIST.read_text(encoding="utf-8")
    if "2013 Alderaan Regionals" in text:
        return
    row = (
        "|- \n"
        "| 2013-07-13 || [[2013 Alderaan Regionals|Alderaan Regionals]] "
        "|| 13–14 July 2013 || — || [[Legacy Open]] || —\n"
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

    mods = [
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_jellison.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_menzel.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_yanaga.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_derlin.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_massung.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_mccarthy.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_harrison_trainor.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_atkin.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_tom.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_shannon.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_schoenthal.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_alderaan_nathan.py"),
    ]
    for mod in mods:
        for side in ("Dark", "Light"):
            title, rel, label = emit_typed(mod, side, by_title)
            if not title:
                continue
            dt[(mod.PLAYER, side)] = title
            hl[title] = label
            titles.append((title, rel))
            print(side, title, "label", label)

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
        ds_page = dt.get((p, "Dark"))
        ls_page = dt.get((p, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        row = (
            f"|- \n| {DATES} || [[{EVENT}]] || {FORMAT} "
            f"|| — || {ds} || {ls}"
        )
        player_rows.setdefault(p, []).append(row)
    for p in HUB_PLAYERS:
        if p in player_rows:
            continue
        player_rows[p] = [
            f"|- \n| {DATES} || [[{EVENT}]] || {FORMAT} "
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
