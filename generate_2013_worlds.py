#!/usr/bin/env python3
"""2013 World Championship — typed + Xerox published lists (Legacy Open).

Day 1 leftover Xerox this slice: Aaron Kia dest as written (Dark name field first-name Aaron).
Day 2 leftover Xerox this slice: Barry Alperstein, Charlie Arlandson (sheet Charles),
Vikram Bali, Amar Banger, Steve Baroni, Pär Birgander, Brandon Stern, Victor G. Brusca,
Justin Carulli (2012 Print Form), Jonny Chu (username mryellow),
Stephen Cellucci Day 2 (informal overlay, LS Same as Yesterday), Angelo Consoli
(username Gravityslada), Justin Desai DS Walkers + LS MWYHL p31 (Name blank, Deck Same as Yest), Brian Fred (sheet B Fred),
Jeremy G (username Jedi Jer; DS Same as Day 1 unpublished), Joe Giannetti
(username Sigga), Chris Gogolen, Tom Haid (username Xenth), Matthew
Harrison-Trainor (Matt HT, WYS / Walkers), Brian Herold (usernames Zero Cool /
Crash Override), Tom H (name as written; not Tom Haid), Ryan Jellison
(username sac89837), Stephen Kin (Worlds Username blank; do not rewrite MPC),
Aaron Kinser (Worlds Username blank; do not rewrite MPC), Jack Koswicki
(name as written), Cole Lepine (username clepines), Scott Lingrell
(p59 name box empty; dested from adjacent Linsanity), Ross Littauer Day 2
(Norsense Same as Yesterday with substitutions; do not rewrite Day 1),
Josh Mack (name box Mack; do not rewrite MPC), Chris Menzel (typed Senate /
Hunt Down; do not rewrite Alderaan), Aaron Nelson (username Airdog2003;
do not rewrite MPC; do not dest as Jake Nelson), Jake Nelson (Username blank;
QMC / NMNPND), Mitch Wieland (Username blank; QMC / NMNPND), Matt Paragano
(username GunganStyle; Contract Killers / Hyperdrive; do not rewrite MPC),
Pistone (Username blank; dest as Pistone; WYS / Walkers; do not rewrite MPC Hunt Down),
Drew Powers Day 2 (Username blank; Same as Day 1 with Light substitutions; do not rewrite Day 1),
Nick Reisch (Username blank; typed QMC / Hunt Down (V) p78-p79; do not dest as a new person; do not rewrite MPC or TMW),
Mike Richards (username m007agent; Hunt Down / QMC; do not rewrite MPC),
Kevin Shannon Day 2 (name box Shannon; Same as Yesterday both sides; no Worlds Day 1 60 — hub empty cells),
Schwartz (Username blank; dest as Schwartz; Wookiee Slaving / Profit; do not dest as Matt Schmaltz or Tom Haid),
Greg Shaw (Username blank; NX Slavers / Not Slavers; do not rewrite MPC or SoCal Shaw),
Steve Skilton (name box stevetotheizzo; Username blank; Wookiee Slaving / Profit; do not dest as Tom Haid; do not rewrite MPC or SoCal Skilton),
RSmith (LS Username Conway East / DS Username Buck Faston; Senate / Kessel; dest as RSmith; do not dest as Reid Smith),
Matt Sokol (Username blank; Walker Garrison / Profit),
Conrad Simmering (Username blank; Communing / Spice),
Nicholas Tobin (Username blank; Senate / Contract Killers; do not rewrite 2014 Worlds),
Chris Terwilliger (name box Chris Twigg; Username blank; email [redacted]; Hyperdrive / Walkers; do not dest as BTwigg),
John Veasey (name box VeeZ; Username blank; Communing Light + typed Agents Dark p99; 2013 MPC Username veez; do not dest as Veez as a new person; do not rewrite MPC),
Micah Wall (Username blank; Walkers / Profit; do not rewrite MPC),
Nathan Wall (Username blank; Hyperdrive Light only; dest as Nathan Wall; do not dest as Nathan Way),
Nathan Way Day 2 (Assassins Same as Yesterday; copy Day 1 Contract Killers; do not dest as Nathan Wall),
Stu Wall (Username blank; WYS / Slavers; dest as Stu Wall; do not dest as Steve Wall),
Emil Wallin Day 2 (Username Darth-Link; TIGH / Imperial Entanglements),
Emil Wallin Day 3 (Same as Yesterday with In/Out substitutions; Username Darth-Link),
Walseth (Username blank; Endor Ops / Space; dest as Walseth; do not dest as Mark Walseth),
Ryan Washeleski (Username Nicodarius; Agents / Hidden Base X-wings),
Chris Westergard (Username blank; Infiltration / Agents; do not rewrite MPC),
Thomas Whaley (Username blank; Senate / Hunt Down),
Chris Wirfs (sheet WIRFS, Username itcouldbewirfs; Hunt Down / Communing; do not rewrite MPC WIRFS).
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
TSV = ROOT / "y2013-worlds-titles.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2013-events"

EVENT = "2013 World Championship"
DATES = "9–11 August 2013"
TAG = "2013-08-09"
FORMAT = "[[Legacy Open]]"
PC_PDF_D1 = "https://starwarsccg.org/phocadownload/2013/2013WorldsDay1.pdf"
PC_PDF_D2 = "https://starwarsccg.org/phocadownload/2013/2013WorldsDay2.pdf"
PC_PDF_D3 = "https://starwarsccg.org/phocadownload/2013/2013WorldsDay3.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
WB_D1 = "https://web.archive.org/web/20160806225452/https://starwarsccg.org/phocadownload/2013/2013WorldsDay1.pdf"

g15.CANON.update(
    {
        "Stephen Cellucci": "Stephen Cellucci",
        "Steve Cellucci": "Stephen Cellucci",
        "Jeremy Gardner": "Jeremy Gardner",
        "Ross Littauer": "Ross Littauer",
        "Drew Powers": "Drew Powers",
        "Nathan Way": "Nathan Way",
        "Aaron Kia": "Aaron Kia",
        "Barry Alperstein": "Barry Alperstein",
        "Charles Arlandson": "Charlie Arlandson",
        "Charlie Arlandson": "Charlie Arlandson",
        "Steve Baroni": "Steve Baroni",
        "Baroni": "Steve Baroni",
        "Vikram Bali": "Vikram Bali",
        "Jonny Chu": "Jonny Chu",
        "Kevin Shannon": "Kevin Shannon",
        "Reid Smith": "Reid Smith",
        "RSmith": "RSmith",
        "Matt Sokol": "Matt Sokol",
        "Sokol": "Matt Sokol",
        "Conrad Simmering": "Conrad Simmering",
        "Simmering": "Conrad Simmering",
        "Nicholas Tobin": "Nicholas Tobin",
        "Tobin": "Nicholas Tobin",
        "Chris Terwilliger": "Chris Terwilliger",
        "Chris Twigg": "Chris Terwilliger",
        "John Veasey": "John Veasey",
        "Veez": "John Veasey",
        "VeeZ": "John Veasey",
        "Micah Wall": "Micah Wall",
        "Nathan Wall": "Nathan Wall",
        "Stu Wall": "Stu Wall",
        "Emil Wallin": "Emil Wallin",
        "Darth-Link": "Emil Wallin",
        "Walseth": "Mark Walseth",
        "Mark Walseth": "Mark Walseth",
        "Ryan Washeleski": "Ryan Washeleski",
        "Nicodarius": "Ryan Washeleski",
        "Chris Westergard": "Chris Westergard",
        "Thomas Whaley": "Thomas Whaley",
        "Chris Wirfs": "Chris Wirfs",
        "WIRFS": "Chris Wirfs",
        "itcouldbewirfs": "Chris Wirfs",
        "Seth Acree": "Seth Acree",
        "Matt H-T": "Matthew Harrison-Trainor",
        "Matt HT": "Matthew Harrison-Trainor",
        "John Anderson": "John Anderson",
        "Casey Anis": "Casey Anis",
        "Casey Anus": "Casey Anis",
        "Amar Banger": "Amar Banger",
        "Pär Birgander": "Pär Birgander",
        "Par Birgander": "Pär Birgander",
        "Birgander": "Pär Birgander",
        "Brandon Stern": "Brandon Stern",
        "Brandon": "Brandon Stern",
        "Victor G. Brusca": "Victor G. Brusca",
        "Justin Carulli": "Justin Carulli",
        "Angelo Consoli": "Angelo Consoli",
        "Angelo": "Angelo Consoli",
        "Consoli": "Angelo Consoli",
        "Justin Desai": "Justin Desai",
        "Desai": "Justin Desai",
        "Brian Fred": "Brian Fred",
        "B Fred": "Brian Fred",
        "BFred": "Brian Fred",
        "Fred": "Brian Fred",
        "Jeremy G": "Jeremy G",
        "JediJer": "Jeremy G",
        "Jedi Jer": "Jeremy G",
        "Joe Giannetti": "Joe Giannetti",
        "Chris Gogolen": "Chris Gogolen",
        "Tom Haid": "Tom Haid",
        "Tom H": "Tom H",
        "Brian Herold": "Brian Herold",
        "Ryan Jellison": "Ryan Jellison",
        "Stephen Kin": "Stephen Kin",
        "Aaron Kinser": "Aaron Kinser",
        "Jack Koswicki": "Jack Koswicki",
        "Cole Lepine": "Cole Lepine",
        "Clepines": "Cole Lepine",
        "Scott Lingrell": "Scott Lingrell",
        "Josh Mack": "Josh Mack",
        "Mack": "Josh Mack",
        "Chris Menzel": "Chris Menzel",
        "Aaron Nelson": "Aaron Nelson",
        "Jake Nelson": "Jake Nelson",
        "Mitch Wieland": "Mitch Wieland",
        "Matt Paragano": "Matt Paragano",
        "Pistone": "Mike Pistone",
        "Mike Pistone": "Mike Pistone",
        "Michael Richards": "Mike Richards",
        "Mike Richards": "Mike Richards",
        "Nick Reisch": "Nick Reisch",
        "Reisch": "Nick Reisch",
        "Schwartz": "Matt Schmaltz",
        "Matt Schmaltz": "Matt Schmaltz",
        "Greg Shaw": "Greg Shaw",
        "Steve Skilton": "Steve Skilton",
        "stevetotheizzo": "Steve Skilton",
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
    title = f"2013 Worlds {stage} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    pdf_url = PC_PDF_D1
    pdf_label = "2013WorldsDay1.pdf"
    if "Day 3" in getattr(mod, "PDF", ""):
        pdf_url, pdf_label = PC_PDF_D3, "2013WorldsDay3.pdf"
    elif "Day 2" in getattr(mod, "PDF", ""):
        pdf_url, pdf_label = PC_PDF_D2, "2013WorldsDay2.pdf"
    sources = [
        f"[{pdf_url} {pdf_label}], starwarsccg.org",
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

    d3 = [
        "Steve Baroni",
        "Vikram Bali",
        "Jonny Chu",
        "Justin Desai",
        "Kevin Shannon",
        "Reid Smith",
        "Emil Wallin",
    ]
    d2 = [
        "Seth Acree",
        "Barry Alperstein",
        "John Anderson",
        "Casey Anis",
        "Charlie Arlandson",
        "Vikram Bali",
        "Amar Banger",
        "Steve Baroni",
        "Pär Birgander",
        "Victor G. Brusca",
        "Justin Carulli",
        "Stephen Cellucci",
        "Jonny Chu",
        "Angelo Consoli",
        "Justin Desai",
        "Brian Fred",
        "Chris Gogolen",
        "Jeremy G",
        "Joe Giannetti",
        "Ryan Jellison",
        "Stephen Kin",
        "Aaron Kinser",
        "Jack Koswicki",
        "Cole Lepine",
        "Scott Lingrell",
        "Ross Littauer",
        "Josh Mack",
        "Chris Menzel",
        "Aaron Nelson",
        "Jake Nelson",
        "Mitch Wieland",
        "Matt Paragano",
        "Mike Pistone",
        "Drew Powers",
        "Nick Reisch",
        "Mike Richards",
        "RSmith",
        "Kevin Shannon",
        "Matt Sokol",
        "Conrad Simmering",
        "Nicholas Tobin",
        "Chris Terwilliger",
        "John Veasey",
        "Micah Wall",
        "Nathan Wall",
        "Nathan Way",
        "Stu Wall",
        "Emil Wallin",
        "Mark Walseth",
        "Ryan Washeleski",
        "Chris Westergard",
        "Thomas Whaley",
        "Chris Wirfs",
        "Schwartz",
        "Greg Shaw",
        "Steve Skilton",
        "Tom H",
        "Tom Haid",
        "Matthew Harrison-Trainor",
        "Brian Herold",
        "Brandon Stern",
    ]
    d1 = [
        "Aaron Kia",
        "Stephen Cellucci",
        "Jeremy Gardner",
        "Ross Littauer",
        "Drew Powers",
        "Nathan Way",
    ]
    tbl3 = table(d3, "Day 3")
    tbl2 = table(d2, "Day 2")
    tbl1 = table(d1, "Day 1")
    body = f"""'''2013 World Championship''' was a Players Committee constructed World Championship, 9–11 August 2013, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="tdl">{PC_TDL}</ref> Published lists are the Day 1, Day 2, and Day 3 PDFs on the Players Committee decklist desk. Dates on the sheets are 9 August 2013 (Day 1), 10 August 2013 (Day 2), and 11 August 2013 (Day 3). Day 1 lists on this page are [[Aaron Kia]] (name field Aaron / Aaron Kia), [[Stephen Cellucci]], [[Jeremy Gardner]], [[Ross Littauer]], [[Drew Powers]], and [[Nathan Way]] (name field Nathan Wall). Remaining Day 2 and Day 3 Xerox sheets are listed below with empty cells until those pages are transcribed. The PDFs do not name a champion.

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' —
* '''Dates:''' {DATES}
* '''Winner:''' —

== Day 3 ==

{tbl3}

Remaining Day 3 Xerox and typed Print Form sheets are in [[:File:2013 Worlds Day 3.pdf]]. [[Matthew Harrison-Trainor]] Day 2 Walkers / Communing Xerox sheets were bound into that PDF (pages 9–10).

== Day 2 ==

{tbl2}

Remaining Day 2 Xerox and typed Print Form sheets are in [[:File:2013 Worlds Day 2.pdf]].

== Day 1 ==

{tbl1}

Remaining Day 1 Xerox is in [[:File:2013 Worlds Day 1.pdf]].

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF_D1} 2013WorldsDay1.pdf], starwarsccg.org
* [{WB_D1} 2013WorldsDay1.pdf (Wayback Machine)], web.archive.org
* [{PC_PDF_D2} 2013WorldsDay2.pdf], starwarsccg.org
* [{PC_PDF_D3} 2013WorldsDay3.pdf], starwarsccg.org
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
    section = (
        "== 2013 ==\n\n"
        '{| class="wikitable sortable"\n'
        "|-\n"
        "! Tag !! Event !! Dates !! Site !! Format !! Winner\n"
        "|- \n"
        "| 2013-08-09 || [[2013 World Championship|World Championship]] "
        "|| 9–11 August 2013 || — || [[Legacy Open]] || —\n"
        "|}\n\n\n"
    )
    if "== 2013 ==" in text:
        return
    needle = "== Decipher World Championships =="
    if needle not in text:
        raise SystemExit("List of tournaments missing Decipher heading")
    text = text.replace(needle, section + needle, 1)
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
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_aaron.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_cellucci.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_gardner.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_littauer.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_powers.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_way.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_acree.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_alperstein.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_anderson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_anis.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_arlandson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_bali.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_bali_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_banger.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_baroni.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_baroni_d3.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_birgander.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_stern.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_brusca.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_carulli.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_chu.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_chu_d3.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_cellucci_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_consoli.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_desai.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_desai_d3.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_shannon_d3.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_smith_d3.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_fred.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_jeremy_g.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_giannetti.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_gogolen.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_haid.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_harrison_trainor.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_herold.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_tom_h.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_jellison.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_kin.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_kinser.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_koswicki.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_lepine.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_lingrell.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_littauer_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_mack.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_menzel.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_nelson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_jake_nelson.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_wieland.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_paragano.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_pistone.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_powers_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_reisch.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_richards_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_schwartz.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_shaw.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_skilton.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_rsmith.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_sokol.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_simmering.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_tobin.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_twigg.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_veasey.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_micah_wall.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_nathan_wall.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_way_d2.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_stu_wall.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_wallin.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_wallin_d3.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_walseth.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_washeleski.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_westergard.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_whaley.py"),
        _load_mod(EVENTS_DIR / "transcribe_2013_worlds_wirfs.py"),
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
    hub_only_stages = {
        "Kevin Shannon": ["Day 2", "Day 3"],
        "Reid Smith": ["Day 3"],
    }
    for p, stages in hub_only_stages.items():
        rows = player_rows.setdefault(p, [])
        have = " ".join(rows)
        for stage in stages:
            if f"({stage})" in have:
                continue
            rows.append(
                f"|- \n| {DATES} || [[{EVENT}]] ({stage}) || {FORMAT} "
                f"|| — || — || —"
            )
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
