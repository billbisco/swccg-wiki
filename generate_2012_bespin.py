#!/usr/bin/env python3
"""2012 Bespin Regionals leftover Xerox (Legacy Open / Virtual Block dests).

python generate_2012_bespin.py --xerox
"""
from __future__ import annotations

import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2012_nats as nats  # noqa: E402
import generate_2014_mpc as mpc  # noqa: E402
import generate_2014_worlds as w14  # noqa: E402
import generate_2015_2016 as g15  # noqa: E402
from generate_2019_2021 import tidy_player_page, wiki_fname  # noqa: E402
from generate_2026_sdso import load_bp_simple  # noqa: E402
from _xerox_delta import write_delta_tsv  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
TSV = ROOT / "y2012-bespin-xerox-titles.tsv"
DELTA = ROOT / "y2012-bespin-xerox-delta.tsv"
APPLIED = ROOT / "y2012-bespin-xerox-applied.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2012-events"

EVENT = "2012 Bespin Regionals"
DATES = "14 July 2012"
TAG = "2012-07-14"
FORMAT = "[[Legacy Open]]"
PC_PDF = "https://starwarsccg.org/phocadownload/2012/2012BespinRegionals.pdf"
WB_PDF = "https://web.archive.org/web/20160806162806/http://www.starwarsccg.org/phocadownload/2012/2012BespinRegionals.pdf"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
WINNERS = "https://www.starwarsccg.org/major-event-winners/"
SITE = "—"
WINNER = "—"

g15.CANON.update(
    {
        "Mitch N.": "Mitch Nieland",
        "Mitch N": "Mitch Nieland",
        "Mitch Nieland": "Mitch Nieland",
        "Charles": "Charlie Arlandson",
        "Charles A.": "Charlie Arlandson",
        "Charles A": "Charlie Arlandson",
        "Charles Arlandson": "Charlie Arlandson",
        "Charlie Arlandson": "Charlie Arlandson",
        "Scott Morgan": "Scott Morgan",
        "Conrad Simmering": "Conrad Simmering",
        "Simmering": "Conrad Simmering",
        "Maul12555": "Conrad Simmering",
        "Cooleo": "Cooleo",
        "CooleoAc": "Cooleo",
        "Brandon Brist": "Brandon Brist",
        "bristicles": "Brandon Brist",
        "Calvin Kurten": "Calvin Kurten",
        "Mark Peterson": "Mark Peterson",
        "Lukes Bionic Hand": "Mark Peterson",
        "Nick Rambo": "Nick Rambo",
        "RamboIrish": "Nick Rambo",
        "Jim Li": "Jim Li",
        "jimli": "Jim Li",
        "Brian Herold": "Brian Herold",
        "Morgan Dwyer": "Morgan Dwyer",
        "John Anderson": "John Anderson",
        "puck71": "John Anderson",
        "Puck71": "John Anderson",
        "Jake N": "Jake Nelson",
        "Jake Nelson": "Jake Nelson",
        "Matt Hanson": "Matt Hanson",
        "Mike": "Mike (2012 Bespin Regionals)",
        "MIKE": "Mike (2012 Bespin Regionals)",
        "Mike (2012 Bespin Regionals)": "Mike (2012 Bespin Regionals)",
        "Walseth": "Mark Walseth",
        "Mark Walseth": "Mark Walseth",
    }
)

# First-name collision: dest First (Event), pipe display First analog leftover nats George.
DISPLAY = {
    "Mike (2012 Bespin Regionals)": "Mike",
}


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
    display = DISPLAY.get(player, player)
    if side == "Light":
        raw = getattr(mod, "LS_CARDS", [])
        if not raw:
            return "", "", "", getattr(mod, "STAGE", "")
        cards = [(q, n, v, False) for q, n, v in raw]
        shields = [(q, n, v, True) for q, n, v in getattr(mod, "LS_SHIELDS", [])]
        add = [(q, n, v, False) for q, n, v in getattr(mod, "LS_ADD", [])]
        scan = mod.LS_SCAN
        page = mod.LS_PAGE
    else:
        raw = getattr(mod, "DS_CARDS", [])
        if not raw:
            return "", "", "", getattr(mod, "STAGE", "")
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
    stage = getattr(mod, "STAGE", "") or ""
    if stage:
        title = f"{EVENT} {stage} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    else:
        title = f"{EVENT} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    sources = [
        f"[{PC_PDF} 2012BespinRegionals.pdf], starwarsccg.org",
        f"[{WB_PDF} Wayback Machine], web.archive.org",
        f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
        f"[{WINNERS} Major Event Winners], starwarsccg.org",
    ]
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2012]]"
    page_txt = w14.deck_page(
        title,
        display,
        "Light Side" if side == "Light" else "Dark Side",
        start_link,
        stage or "Regionals",
        body,
        sources,
        extra_note=w14.extra_note_for(mod, side),
        scan_file=scan,
        scan_caption=f"Page {page} of [[:File:{mod.PDF}]].",
        username=w14.username_for(mod, side),
        player_page=player if player != display else None,
    )
    return title, write(title, page_txt), label, stage


def _player_table(players, dt, hl) -> str:
    bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
    for p in players:
        ds_page = dt.get((p, "Dark"))
        ls_page = dt.get((p, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        disp = DISPLAY.get(p, p)
        who = f"[[{p}|{disp}]]" if disp != p else f"[[{p}]]"
        bits += ["|-", f"| {who} || {ds} || {ls}"]
    bits.append("|}")
    return "\n".join(bits)


def write_hub(xerox_dt, xerox_hl, xerox_players) -> None:
    body = f"""'''2012 Bespin Regionals''' was a Players Committee constructed regional, 14 July 2012, using the pre-reset virtual pool ([[Legacy Open]]).<ref name="tdl">{PC_TDL}</ref> Xerox sheets from the tournament-decklists PDF are listed below as those scans are transcribed. The PDF does not name a champion.

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' {SITE}
* '''Dates:''' {DATES}
* '''Winner:''' {WINNER}

== Xerox ==

{_player_table(xerox_players, xerox_dt, xerox_hl)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]

== Sources ==

* [{PC_PDF} 2012BespinRegionals.pdf], starwarsccg.org
* [{WB_PDF} 2012BespinRegionals.pdf (Wayback Machine)], web.archive.org
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
        "| 2012-07-14 || [[2012 Bespin Regionals|Bespin Regionals]] "
        "|| 14 July 2012 || — || [[Legacy Open]] || —\n"
    )
    if "2012 Bespin Regionals" in text:
        return False
    needle = (
        "| 2012-07-07 || [[2012 Alderaan Regionals|Alderaan Regionals]] "
        "|| 7 July 2012 || — || [[Legacy Open]] || —\n"
    )
    if needle in text:
        LIST.write_text(
            text.replace(needle, row + "|-\n" + needle, 1),
            encoding="utf-8",
            newline="\n",
        )
        return True
    raise SystemExit("List of tournaments missing 2012 Alderaan Regionals row")


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
            "boba fett, prepared hunter": "Character",
            "galen's lightsaber, vader's gift": "Weapon",
            "general nevar": "Character",
            "cyborg commander's lightsabers": "Weapon",
            "i've lost artoo": "Interrupt",
            "endor shield": "Effect",
            "a sith's plans": "Effect",
            "ghhhk": "Interrupt",
            "sniper & dark strike": "Interrupt",
            "battle droid squadron": "Character",
            "dark reconnaissance": "Interrupt",
            "sith fury": "Interrupt",
            "cold feet": "Interrupt",
            "sonic bombardment": "Interrupt",
            "uncharted settlements": "Location",
            "quite a mercenary": "Character",
            "first officer thaneespi": "Character",
            "commander vanden willard": "Character",
            "on the edge": "Interrupt",
            "run luke run": "Interrupt",
            "bothawui": "Location",
            "another pathetic lifeform": "Defensive Shield",
            "let's keep a little optimism here": "Defensive Shield",
            "he can go about his business": "Defensive Shield",
            "there is no try": "Defensive Shield",
            "i find your lack of faith disturbing": "Defensive Shield",
            "noooooooooooo": "Interrupt",
            "cantina": "Location",
            "han, courageous smuggler": "Character",
            "spice mines operations": "Effect",
            "admiral kellaeen": "Character",
            "rebel agent's blaster rifle": "Weapon",
            "booster's star destroyer": "Starship",
            "rebel agent": "Character",
            "relentless": "Starship",
            "inoge": "Character",
            "mmnr + ip": "Interrupt",
            "speak": "Interrupt",
            "rebel art": "Interrupt",
            "leia, opposition leader": "Character",
            "galen": "Character",
            "aurra sing, district attorney": "Character",
            "hutt bounty & death mark": "Effect",
            "artoo bld": "Character",
            "twhps": "Interrupt",
            "scramble": "Interrupt",
            "kebyc": "Character",
            "tanus spijek": "Character",
            "after her": "Defensive Shield",
            "abyss": "Defensive Shield",
            "he hasn't come back yet": "Interrupt",
            "masterful move & endor occupation": "Effect",
            "lieutenant commander arden": "Character",
            "emperor's personal shuttle": "Starship",
            "insignificant rebellion": "Effect",
            "ni chuba na?": "Interrupt",
            "spaceport street": "Location",
            "spaceport docking bay": "Location",
            "spaceport prefect's office": "Location",
            "le-bo2d9 (leebo)": "Character",
            "boshek": "Character",
            "alternatives to fighting": "Interrupt",
            "off the edge": "Interrupt",
            "projection of a skywalker": "Effect",
            "cloud city celebration": "Effect",
            "enter the unknown": "Interrupt",
            "return fire": "Interrupt",
            "enter the boma": "Interrupt",
            "azgo rifle": "Weapon",
            "obi's mistake": "Interrupt",
            "mvc suit": "Device",
            "ith & aim high": "Interrupt",
            "flops": "Starship",
            "gal dorn": "Character",
            "where are you taking this... cargo?": "Interrupt",
            "sergeant brooks": "Character",
            "corporal kensell": "Character",
            "emperor's royal guard": "Character",
            "kepler the black": "Character",
            "duty, betrayal and sacrifice": "Interrupt",
            "baskol yeesim": "Character",
            "tie/ln": "Starship",
            "always in motion the future is": "Effect",
            "tatooine: native hut": "Location",
            "at-at": "Starship",
            "i love you.": "Interrupt",
            "what have you done?": "Interrupt",
            "gentle touch": "Interrupt",
            "reckless": "Interrupt",
            "ztmll": "Character",
            "mauler mithel": "Character",
            "screaming teroch": "Character",
            "wylcfm": "Interrupt",
            "wcja": "Interrupt",
            "wcss": "Interrupt",
            "corporal jacosyn": "Character",
            "if the armor's fully operational": "Effect",
            "offer": "Interrupt",
            "han's blaster pistol": "Weapon",
        }
    )
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2012]]"
    titles: list[tuple[str, str]] = []
    xerox_dt, xerox_hl = {}, {}
    xerox_players: list[str] = []
    mods = []
    for path in sorted(EVENTS_DIR.glob("transcribe_2012_bespin_*.py")):
        mods.append(_load_mod(path))
    for mod in mods:
        player = g15.CANON.get(mod.PLAYER, mod.PLAYER)
        if player not in xerox_players:
            xerox_players.append(player)
        for side in ("Dark", "Light"):
            title, rel, label, _st = emit_xerox(mod, side, by_title)
            if not title:
                continue
            xerox_dt[(player, side)] = title
            xerox_hl[title] = label
            titles.append((title, rel))
            print(side, title, "label", label)

    write_hub(xerox_dt, xerox_hl, xerox_players)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))
    cat = PAGES / "Category_2012.wiki"
    if cat.exists():
        titles.append(("Category:2012", "pages/Category_2012.wiki"))

    meta = {
        "title": EVENT,
        "year": "2012",
        "pc": PC_PDF,
    }
    player_rows: dict[str, list[str]] = {}
    for mod in mods:
        p = g15.CANON.get(mod.PLAYER, mod.PLAYER)
        ds_page = xerox_dt.get((p, "Dark"))
        ls_page = xerox_dt.get((p, "Light"))
        ds = f"[[{ds_page}|{xerox_hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{xerox_hl[ls_page]}]]" if ls_page else "—"
        row = (
            f"|- \n| {DATES} || [[{EVENT}]] || {FORMAT} "
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
