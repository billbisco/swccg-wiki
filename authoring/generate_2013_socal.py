#!/usr/bin/env python3
"""2013 SoCal Grand Prix — typed and Xerox published lists (Legacy Open).

Typed dest: John Anderson Day 1 Light, Matthew Harrison-Trainor Day 1 LS+DS
and Day 2 LS+DS, Joe Olson Day 1 LS+DS, Gabe Day 1 LS+DS. Xerox dest: Phil Aasen Day 1,
John Anderson Day 1 Dark, Clayton Atkin Day 1 and Day 2 (Same as Yesterday),
Steve Brentson Day 1 LS+DS, Brian Fred Day 1 LS+DS, Steve Harpster Day 1 LS+DS, Tom Day 1 LS+DS, Bill Day 1 LS+DS, Josh Day 1 LS+DS, Nathan Day 1 LS+DS, Jan Westergard Day 1 LS+DS, Ganden Yanaga Day 1, Brian Herold Day 1, Anthony Massung Day 1, Kevin Shannon
Day 1 and Day 2, Greg Shaw Day 1, Steve Skilton Day 1, Reid Smith Day 1 and
Day 2, Matt Thornton Day 1. Always dest incomplete/blank names as written;
blank Name and blank Username dest [[Unknown Player]].
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
TSV = ROOT / "y2013-socal-titles.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2013-events"

EVENT = "2013 SoCal Grand Prix"
DATES = "25–27 October 2013"
TAG = "2013-10-25"
FORMAT = "[[Legacy Open]]"
PC_PDF_D1 = "https://starwarsccg.org/phocadownload/2013/2013SoCalDay1.pdf"
PC_PDF_D2 = "https://starwarsccg.org/phocadownload/2013/2013SoCalDay2.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
FORUM = "https://forum.starwarsccg.org/viewtopic.php?t=52931"
WB_D1 = "https://web.archive.org/web/20160809085659/http://www.starwarsccg.org/phocadownload/2013/2013SoCalDay1.pdf"
WB_D2 = "https://web.archive.org/web/20160806162302/http://www.starwarsccg.org/phocadownload/2013/2013SoCalDay2.pdf"

g15.CANON.update(
    {
        "Phil Aasen": "Phil Aasen",
        "Gabe": "Gabe",
        "Brentson": "Steve Brentson",
        "Steve Brentson": "Steve Brentson",
        "B Fred": "Brian Fred",
        "Brian Fred": "Brian Fred",
        "HARPSTER": "Steve Harpster",
        "Harpster": "Steve Harpster",
        "Steve Harpster": "Steve Harpster",
        "Tom": "Tom",
        "Bill": "Bill",
        "Josh": "Josh",
        "Nathan": "Nathan",
        "JAN": "Jan Westergard",
        "Jan": "Jan Westergard",
        "Jan Westergard": "Jan Westergard",
        "John Anderson": "John Anderson",
        "Clayton Atkin": "Clayton Atkin",
        "Brian Herold": "Brian Herold",
        "Matthew Harrison-Trainor": "Matthew Harrison-Trainor",
        "Matt HT": "Matthew Harrison-Trainor",
        "Matt H-T": "Matthew Harrison-Trainor",
        "Anthony Massung": "Anthony Massung",
        "Joe Olson": "Joe Olson",
        "Kevin Shannon": "Kevin Shannon",
        "Greg Shaw": "Greg Shaw",
        "Gregory Shaw": "Greg Shaw",
        "Steve Skilton": "Steve Skilton",
        "Reid Smith": "Reid Smith",
        "RSmith": "Reid Smith",
        "Matt Thornton": "Matt Thornton",
        "Ganden Yanaga": "Ganden Yanaga",
        "Camden Yanaga": "Ganden Yanaga",
    }
)

HUB_D1 = [
    "Phil Aasen",
    "John Anderson",
    "Clayton Atkin",
    "Steve Brentson",
    "Brian Fred",
    "Steve Harpster",
    "Tom",
    "Bill",
    "Josh",
    "Nathan",
    "Jan Westergard",
    "Gabe",
    "Brian Herold",
    "Matthew Harrison-Trainor",
    "Anthony Massung",
    "Joe Olson",
    "Kevin Shannon",
    "Greg Shaw",
    "Steve Skilton",
    "Reid Smith",
    "Matt Thornton",
    "Ganden Yanaga",
]
HUB_D2 = [
    "Kevin Shannon",
    "Matthew Harrison-Trainor",
    "Reid Smith",
    "Clayton Atkin",
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
    title = f"2013 SoCal Grand Prix {stage} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    sources = [
        f"[{PC_PDF_D1} 2013SoCalDay1.pdf], starwarsccg.org",
        f"[{WB_D1} Wayback Machine (Day 1)], web.archive.org",
        f"[{PC_PDF_D2} 2013SoCalDay2.pdf], starwarsccg.org",
        f"[{WB_D2} Wayback Machine (Day 2)], web.archive.org",
        f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
        f"[{FORUM} Main Event Update Thread], forum.starwarsccg.org",
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
                f"| [[{p}]] || {cell(p, stage, 'Dark')} || {cell(p, stage, 'Light')}",
            ]
        bits.append("|}")
        return "\n".join(bits)

    tbl2 = table(HUB_D2, "Day 2")
    tbl1 = table(HUB_D1, "Day 1")
    body = f"""'''2013 SoCal Grand Prix''' was a Players Committee constructed event, 25–27 October 2013, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="tdl">{PC_TDL}</ref> [[Kevin Shannon]] won the event, defeating [[Matthew Harrison-Trainor]] in the final.<ref name="forum">{FORUM}</ref> The published lists are the SoCal Day 1 and Day 2 PDFs on the Players Committee decklist desk. Day 1 sheets are dated 26 October 2013; Day 2 sheets are dated 27 October 2013. The forum board lists the weekend as SoCal Grand Prix - Oct 25-27. Day 2 was the Top 4: Shannon, Harrison-Trainor, [[Reid Smith]], and [[Clayton Atkin]]. Typed printouts dested on this page are [[John Anderson]] Day 1 Light, Harrison-Trainor Day 1 and Day 2, [[Joe Olson]] Day 1, [[Gabe]] Day 1, and [[Nathan]] Day 1. Xerox dested on this page are [[Phil Aasen]] Day 1, Anderson Day 1 Dark, Atkin Day 1 and Day 2, [[Steve Brentson]] Day 1, [[Brian Fred]] Day 1, [[Steve Harpster]] Day 1, [[Tom]] Day 1, [[Bill]] Day 1, [[Josh]] Day 1, [[Jan Westergard]] Day 1, [[Ganden Yanaga]] Day 1, [[Brian Herold]] Day 1, [[Anthony Massung]] Day 1, Shannon Day 1 and Day 2, [[Greg Shaw]] Day 1, [[Steve Skilton]] Day 1, Reid Smith Day 1 and Day 2, and [[Matt Thornton]] Day 1. Atkin Day 2 Final Four forms are headed Same as Yesterday (the Day 1 Communing and Hunt Down lists). Shannon Day 2 Light crosses out Phil Aasen as a joke; Day 2 Dark is the James Shenanigans sticky. Sheets signed only with a last name, first name, last initial, or an unreadable name are dested as written when the 60 is readable. Yanaga is handwritten Camden Yanaga on the sheet (username Cam Solusar). Shaw is handwritten Gregory Shaw. Anderson Event Name was '13 Worlds Day #2 overwritten SoCal 2013. Aasen username is Korreshark. Gabe is first-name-only on both typed Print Forms. Brentson is handwritten last-name-only dested Steve Brentson. B Fred is dested Brian Fred. HARPSTER is dested Steve Harpster. Tom is first-name-only dested as written. Bill is first-name-only dested as written. Josh is first-name-only dested as written (username Renmaker). Nathan is first-name-only dested as written (username SolaGratia). JAN / Jan username Ghosttrain is dested Jan Westergard.

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' San Diego, California
* '''Dates:''' {DATES}
* '''Winner:''' [[Kevin Shannon]]

== Day 2 ==

{tbl2}

Day 2 published lists are in [[:File:2013 SoCal Grand Prix Day 2.pdf]].

== Day 1 ==

{tbl1}

Day 1 published lists are in [[:File:2013 SoCal Grand Prix Day 1.pdf]].

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF_D1} 2013SoCalDay1.pdf], starwarsccg.org
* [{WB_D1} 2013SoCalDay1.pdf (Wayback Machine)], web.archive.org
* [{PC_PDF_D2} 2013SoCalDay2.pdf], starwarsccg.org
* [{WB_D2} 2013SoCalDay2.pdf (Wayback Machine)], web.archive.org
* [{PC_TDL} Tournament Decklists], starwarsccg.org
* [{FORUM} Main Event Update Thread], forum.starwarsccg.org

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
    old = (
        "| 2013-10-25 || [[2013 SoCal Grand Prix|SoCal Grand Prix]] "
        "|| 25–27 October 2013 || San Diego, California || [[Legacy Open]] || —"
    )
    new = (
        "| 2013-10-25 || [[2013 SoCal Grand Prix|SoCal Grand Prix]] "
        "|| 25–27 October 2013 || San Diego, California || [[Legacy Open]] || [[Kevin Shannon]]"
    )
    if old in text:
        text = text.replace(old, new, 1)
        LIST.write_text(text, encoding="utf-8", newline="\n")
        return
    if "2013 SoCal Grand Prix" in text:
        return
    row = "|- \n" + new + "\n"
    needle = (
        "| 2013-08-09 || [[2013 World Championship|World Championship]] "
        "|| 9–11 August 2013 || — || [[Legacy Open]] || —\n"
    )
    if needle in text:
        text = text.replace(needle, row + needle, 1)
    else:
        m = re.search(r"(== 2013 ==.*?)\|}\n", text, re.S)
        if not m:
            raise SystemExit("List of tournaments missing 2013 section")
        text = text[: m.end() - 3] + row + "|}\n" + text[m.end() :]
    if "[[Category:2013]]" not in text:
        text = text.replace("[[Category:2014]]", "[[Category:2014]]\n[[Category:2013]]")
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
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_aasen.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_anderson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_atkin.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_gabe.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_brentson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_fred.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_harpster.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_tom.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_bill.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_josh.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_nathan.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_jan.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_harrison_trainor.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_olson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_harrison_trainor_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_yanaga.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_herold.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_massung.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_shannon.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_shaw.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_atkin_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_shannon_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_skilton.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_smith.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_smith_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_socal_thornton.py"),
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
        "pc": PC_PDF_D1,
        "format": FORMAT,
    }
    player_rows: dict[str, list[str]] = {}
    for p in HUB_D1:
        rows = []
        if p in HUB_D2:
            ds_page = dt.get((p, "Day 2", "Dark"))
            ls_page = dt.get((p, "Day 2", "Light"))
            ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
            ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
            rows.append(
                f"|- \n| {DATES} || [[{EVENT}]] (Day 2) || {FORMAT} "
                f"|| — || {ds} || {ls}"
            )
        ds_page = dt.get((p, "Day 1", "Dark"))
        ls_page = dt.get((p, "Day 1", "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        rows.append(
            f"|- \n| {DATES} || [[{EVENT}]] (Day 1) || {FORMAT} "
            f"|| — || {ds} || {ls}"
        )
        player_rows[p] = rows
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
