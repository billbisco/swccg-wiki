#!/usr/bin/env python3
"""2012 Texas Mini Worlds leftover Xerox (Legacy Open / Virtual Block dests).

python generate_2012_tmw.py --xerox
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2012_nats as nats  # noqa: E402  loads CANON
import generate_2014_mpc as mpc  # noqa: E402
import generate_2014_worlds as w14  # noqa: E402
import generate_2015_2016 as g15  # noqa: E402
from generate_2019_2021 import tidy_player_page, wiki_fname  # noqa: E402
from generate_2026_sdso import load_bp_simple  # noqa: E402
from _xerox_delta import write_delta_tsv  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
TSV = ROOT / "y2012-tmw-xerox-titles.tsv"
DELTA = ROOT / "y2012-tmw-xerox-delta.tsv"
APPLIED = ROOT / "y2012-tmw-xerox-applied.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2012-events"

EVENT = "2012 Texas Mini Worlds"
DATES = "27–29 April 2012"
TAG = "2012-04-27"
FORMAT = "[[Legacy Open]]"
PC_PDF_D1 = "https://starwarsccg.org/phocadownload/2012/2012TMWDay1.pdf"
WB_PDF_D1 = "https://web.archive.org/web/20160806162806/http://www.starwarsccg.org/phocadownload/2012/2012TMWDay1.pdf"
PC_PDF_D2 = "https://starwarsccg.org/phocadownload/2012/2012TMWDay2.pdf"
WB_PDF_D2 = "https://web.archive.org/web/20160806162806/http://www.starwarsccg.org/phocadownload/2012/2012TMWDay2.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
WINNERS = "https://www.starwarsccg.org/major-event-winners/"
SITE = "Texas"
WINNER = "[[Mike Richards]]"

g15.CANON.update(
    {
        "Michael Richards": "Mike Richards",
        "Mike Richards": "Mike Richards",
        "Richards": "Mike Richards",
        "m007agent": "Mike Richards",
        "mr007agent": "Mike Richards",
        "Brian Herold": "Brian Herold",
        "Advocate": "Scott Lingrell",
        "Scott Lingrell": "Scott Lingrell",
        "Gregory Shaw": "Greg Shaw",
        "Greg Shaw": "Greg Shaw",
        "James Barnes": "James Barnes",
        "Robbie Hendon": "Robbie Hendon",
        "John Anderson": "John Anderson",
        "Matt Lush": "Matt Lush",
        "Nick Reisch": "Nick Reisch",
        "Reisch": "Nick Reisch",
        "Evan Kirkpatrick": "Evan Kirkpatrick",
        "Veez": "John Veasey",
        "VeeZ": "John Veasey",
        "John Veasey": "John Veasey",
        "Amar Banger": "Amar Banger",
        "abanger": "Amar Banger",
        "Steve Skilton": "Steve Skilton",
        "Jeremy Gardner": "Jeremy Gardner",
        "Charley Joe": "Charley Joe",
        "Wburg": "Charley Joe",
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


def emit_xerox(mod, side: str, by_title) -> tuple[str, str, str, str]:
    player = g15.CANON.get(mod.PLAYER, mod.PLAYER)
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
    title = f"{EVENT} {stage} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    if stage == "Day 2":
        sources = [
            f"[{PC_PDF_D2} 2012TMWDay2.pdf], starwarsccg.org",
            f"[{WB_PDF_D2} Wayback Machine], web.archive.org",
            f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
            f"[{WINNERS} Major Event Winners], starwarsccg.org",
        ]
    else:
        sources = [
            f"[{PC_PDF_D1} 2012TMWDay1.pdf], starwarsccg.org",
            f"[{WB_PDF_D1} Wayback Machine], web.archive.org",
            f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
            f"[{WINNERS} Major Event Winners], starwarsccg.org",
        ]
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2012]]"
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
        username=w14.username_for(mod, side),
    )
    return title, write(title, page_txt), label, stage


def _stage_table(players, dt, hl, stage: str) -> str:
    bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
    for p in players:
        ds_page = dt.get((p, stage, "Dark"))
        ls_page = dt.get((p, stage, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        bits += ["|-", f"| [[{p}]] || {ds} || {ls}"]
    bits.append("|}")
    return "\n".join(bits)


def write_hub(xerox_dt, xerox_hl, xerox_players) -> None:
    xerox_sections = ""
    for stage, heading in (
        ("Day 2", "Day 2"),
        ("Consolation", "Consolation"),
        ("Day 1", "Day 1"),
    ):
        plist = xerox_players.get(stage) or []
        if not plist:
            continue
        xerox_sections += f"\n== {heading} ==\n\n{_stage_table(plist, xerox_dt, xerox_hl, stage)}\n"
    body = f"""'''2012 Texas Mini Worlds''' was a Players Committee constructed event, 27–29 April 2012, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="tdl">{PC_TDL}</ref> Xerox Day 1 and Day 2 sheets from the tournament-decklists PDFs are listed below as those scans are transcribed. [[Mike Richards]] is the published Texas Mini-Worlds winner.<ref name="winners">{WINNERS}</ref>

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' {SITE}
* '''Dates:''' {DATES}
* '''Winner:''' {WINNER}
{xerox_sections}
== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF_D1} 2012TMWDay1.pdf], starwarsccg.org
* [{WB_PDF_D1} 2012TMWDay1.pdf (Wayback Machine)], web.archive.org
* [{PC_PDF_D2} 2012TMWDay2.pdf], starwarsccg.org
* [{WB_PDF_D2} 2012TMWDay2.pdf (Wayback Machine)], web.archive.org
* [{PC_TDL} Tournament Decklists], starwarsccg.org
* [{WINNERS} Major Event Winners], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2012]]
"""
    (PAGES / wiki_fname(EVENT)).write_text(
        body.replace("\r\n", "\n"), encoding="utf-8", newline="\n"
    )


def patch_list() -> bool:
    text = LIST.read_text(encoding="utf-8")
    row = (
        "| 2012-04-27 || [[2012 Texas Mini Worlds|Texas Mini Worlds]] "
        "|| 27–29 April 2012 || Texas || [[Legacy Open]] || [[Mike Richards]]\n"
    )
    if "2012 Texas Mini Worlds" in text:
        return False
    needle = (
        "| 2012-02-10 || [[2012 Match Play Championship|Match Play Championship]] "
        "|| 10–12 February 2012 || — || [[Legacy Open]] || —\n"
    )
    if needle in text:
        LIST.write_text(
            text.replace(needle, row + "|-\n" + needle, 1),
            encoding="utf-8",
            newline="\n",
        )
        return True
    raise SystemExit("List of tournaments missing 2012 MPC row")


def leftover_xerox() -> None:
    STUBS.mkdir(parents=True, exist_ok=True)
    _by_id, by_title = load_bp_simple()
    mpc.load_wiki_types()
    mpc.TYPE_OVERRIDE.update(
        {
            "phylo gandish": "Character",
            "the camp": "Location",
            "3720 to 1": "Effect",
            "3,720 to 1": "Effect",
            "rolling, rolling, rolling": "Interrupt",
            "obi-wan's apparition": "Effect",
            "kin kian": "Character",
            "rebel gunrunner": "Character",
            "keir santage": "Character",
            "kier santage": "Character",
            "massassi base sentry": "Character",
            "red 6": "Starship",
            "corran horn": "Character",
            "echo base garrison": "Effect",
            "red squadron 7": "Starship",
            "wounded warrior": "Interrupt",
            "master, destroyers!": "Interrupt",
            "p-13 & p-14": "Character",
            "droid racks": "Effect",
            "outflank": "Interrupt",
            "blockade support ship": "Starship",
            "we'll let fate decide, huh": "Defensive Shield",
            "come here you big coward": "Defensive Shield",
            "strike force": "Effect",
            "strikeforce": "Effect",
            "crossfire": "Interrupt",
            "elis helrot": "Character",
            "tatooine (coruscant)": "Location",
            "search and destroy": "Effect",
            "derek \"hobbie\" klivian": "Character",
            "rebel aces": "Effect",
            "biggs' rogue squadron": "Starship",
            "garidan": "Character",
            "a jedi's plans": "Effect",
            "captain verrack": "Character",
            "mon calamari dockyards": "Location",
            "republic logistics": "Effect",
            "kiffex": "Location",
            "defiant": "Starship",
            "escape pod": "Device",
            "on target": "Interrupt",
            "stay sharp!": "Interrupt",
            "blockade flagship: hallway": "Location",
            "naboo: theed palace generator core": "Location",
            "imperial propaganda": "Effect",
            "a sith's weapon": "Weapon",
            "revenge of the sith": "Effect",
            "blaster rack": "Device",
            "darth vader, betrayer of jedi": "Character",
            "4-lom with rifle": "Character",
            "boba fett, renowned bounty hunter": "Character",
            "scoundrel's guild": "Location",
            "paleso rashad": "Character",
            "mezian terrik": "Character",
            "boshek's modified freighter": "Starship",
            "mercenary sunset": "Interrupt",
            "myn kenaugh": "Character",
            "tarkin's doctrine": "Effect",
            "obi-wan kenobi with lightsaber": "Character",
            "visage of the empire": "Effect",
            "ig-bodyguard droid": "Character",
            "kashyyyk insurgent leader": "Character",
            "blind jedi": "Character",
            "you can either profit by this": "Objective",
            "toak": "Character",
            "admiral salish-bar": "Character",
            "gela yeosa": "Character",
            "porkins scanner": "Character",
            "palowick barter": "Interrupt",
            "assassin guns": "Weapon",
            "lightsaber pike": "Weapon",
            "raddle's blaster": "Weapon",
            "jedi prisoner": "Effect",
            "superficial demise": "Interrupt",
            "cloak of deception": "Effect",
            "os-61-3": "Starship",
            "chewie, protector": "Character",
            "blast the door kid": "Interrupt",
            "falling portal": "Interrupt",
            "taim & bak magnetic rail gun": "Weapon",
            "that's too old": "Interrupt",
            "igar": "Character",
        }
    )
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2012]]"
    titles: list[tuple[str, str]] = []
    xerox_dt, xerox_hl = {}, {}
    xerox_players: dict[str, list[str]] = {}
    mods = []
    for path in sorted(EVENTS_DIR.glob("transcribe_2012_tmw_*.py")):
        mods.append(_load_mod(path))
    for mod in mods:
        player = g15.CANON.get(mod.PLAYER, mod.PLAYER)
        stage = getattr(mod, "STAGE", "Day 1")
        if player not in xerox_players.setdefault(stage, []):
            xerox_players[stage].append(player)
        for side in ("Dark", "Light"):
            title, rel, label, st = emit_xerox(mod, side, by_title)
            if not title:
                continue
            xerox_dt[(player, st, side)] = title
            xerox_hl[title] = label
            titles.append((title, rel))
            print(st, side, title, "label", label)

    write_hub(xerox_dt, xerox_hl, xerox_players)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))
    cat = PAGES / "Category_2012.wiki"
    if cat.exists():
        titles.append(("Category:2012", "pages/Category_2012.wiki"))

    meta = {
        "title": EVENT,
        "year": "2012",
        "pc": PC_PDF_D1,
    }
    player_rows: dict[str, list[str]] = {}
    for mod in mods:
        p = g15.CANON.get(mod.PLAYER, mod.PLAYER)
        stage = getattr(mod, "STAGE", "Day 1")
        ds_page = xerox_dt.get((p, stage, "Dark"))
        ls_page = xerox_dt.get((p, stage, "Light"))
        ds = f"[[{ds_page}|{xerox_hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{xerox_hl[ls_page]}]]" if ls_page else "—"
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

    if patch_list():
        titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    if "Unknown Player" in player_rows:
        unk_idx = PAGES / "Unknown_players.wiki"
        if unk_idx.exists():
            titles.append(("Unknown players", "pages/Unknown_players.wiki"))
        titles.append(("Unknown Player", "pages/player-stubs/Unknown_Player.wiki"))

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
    print("xerox tsv", TSV, "n", len(ordered))
    write_delta_tsv(ordered, APPLIED, DELTA, {EVENT})


if __name__ == "__main__":
    leftover_xerox()
