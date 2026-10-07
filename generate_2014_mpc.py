#!/usr/bin/env python3
"""2014 Match Play Championship Holotable typed lists (Legacy Open / Virtual Block dests).

Xerox Day 1/2/cons leftover: python generate_2014_mpc.py --xerox
"""
from __future__ import annotations

import importlib.util
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2014_worlds as w14  # noqa: E402
import generate_2015_2016 as g15  # noqa: E402
from generate_2019_2021 import tidy_player_page, wiki_fname  # noqa: E402
from generate_2026_sdso import load_bp_simple  # noqa: E402
import _parse_htd as htd  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
HTD = ROOT / "encyclopedia" / "pc-2014-events" / "holotable"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
TSV = ROOT / "y2014-mpc-titles.tsv"
XEROX_TSV = ROOT / "y2014-mpc-xerox-titles.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2014-events"
MEDIA = ROOT / "y2014-mpc-media"

EVENT = "2014 Match Play Championship"
DATES = "24–26 January 2014"
TAG = "2014-01-24"
FORMAT = "[[Legacy Open]]"
PC_ZIP = "https://res.starwarsccg.org/wp/wp-content/uploads/2014MPC_Holotable.zip"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
PC_PDF_D1 = "https://res.starwarsccg.org/wp/wp-content/uploads/MPC-2014-Day-1-Main-Event.pdf"
PC_PDF_D2 = "https://res.starwarsccg.org/wp/wp-content/uploads/MPC-2014-Day-2-Main-Event.pdf"
PC_PDF_CONS = "https://res.starwarsccg.org/wp/wp-content/uploads/MPC-2014-Day-2-Consolation-Event.pdf"

g15.CANON.update(
    {
        "Chris Twigg": "Chris Terwilliger",
        "Matt H-T": "Matthew Harrison-Trainor",
        "Matt HT": "Matthew Harrison-Trainor",
        "Stephen Cellucci": "Stephen Cellucci",
        "Brian Fred": "Brian Fred",
        "Cole Lepine": "Cole Lepine",
        "C Lepine": "Cole Lepine",
        "Kyle Krueger": "Kyle Krueger",
        "Aaron Kingery": "Aaron Kingery",
        "Aaron Kia": "Aaron Kia",
        "MHT": "Matthew Harrison-Trainor",
        "PISTONE": "Mike Pistone",
        "Pistone": "Mike Pistone",
        "Greg Shaw": "Greg Shaw",
        "Kevin Shannon": "Kevin Shannon",
        "Reid Smith": "Reid Smith",
        "Nick Amato": "Nicholas Amato",
        "Nicholas Amato": "Nicholas Amato",
        "Barry Alperstein": "Barry Alperstein",
        "Nate Lowderback": "Nate Louderback",
        "Nate Louderback": "Nate Louderback",
        "Ross Lithauer": "Ross Littauer",
        "Ross Littauer": "Ross Littauer",
        "Jarrod": "Jared",
        "Jared": "Jared",
        "Joe G": "Joe G",
        "Joe G.": "Joe G",
        "Shannon": "Kevin Shannon",
        "Kevin Shannon": "Kevin Shannon",
        "HARPSTER": "Steve Harpster",
        "Steve Harpster": "Steve Harpster",
        "Mack": "Josh Mack",
        "Josh Mack": "Josh Mack",
        "Matthew Carulli": "Matt Carulli",
        "Matt Carulli": "Matt Carulli",
        "Mike d'Amboise": "Mike D'Ambrosio",
        "Mike D'Ambrosio": "Mike D'Ambrosio",
        "Unknown Player": "Unknown Player",
        "Steve Skilton": "Steve Skilton",
        "Stephen Skilton": "Steve Skilton",
        "Skilton": "Steve Skilton",
        "Chris Westergard": "Chris Westergard",
        "Chris Wirfs": "Chris Wirfs",
        "WIRFS": "Chris Wirfs",
    }
)

TYPE_ORDER = [
    "Objective",
    "Admiral's Order",
    "Character",
    "Creature",
    "Device",
    "Effect",
    "Epic Event",
    "Interrupt",
    "Jedi Test",
    "Location",
    "Podracer",
    "Starship",
    "Vehicle",
    "Weapon",
    "Defensive Shield",
    "Unknown",
]

CAT_MAP = {
    "OBJECTIVE": "Objective",
    "CHARACTER": "Character",
    "CREATURE": "Creature",
    "DEVICE": "Device",
    "EFFECT": "Effect",
    "EPIC_EVENT": "Epic Event",
    "EPICEVENT": "Epic Event",
    "EPIC EVENT": "Epic Event",
    "INTERRUPT": "Interrupt",
    "USED INTERRUPT": "Interrupt",
    "LOST INTERRUPT": "Interrupt",
    "JEDI_TEST": "Jedi Test",
    "JEDITEST": "Jedi Test",
    "JEDI TEST": "Jedi Test",
    "LOCATION": "Location",
    "PODRACER": "Podracer",
    "STARSHIP": "Starship",
    "VEHICLE": "Vehicle",
    "WEAPON": "Weapon",
    "CHARACTER WEAPON": "Weapon",
    "STARSHIP WEAPON": "Weapon",
    "ADMIRAL'S_ORDER": "Admiral's Order",
    "ADMIRALS_ORDER": "Admiral's Order",
    "ADMIRAL'S ORDER": "Admiral's Order",
    "DEFENSIVE_SHIELD": "Defensive Shield",
    "DEFENSIVESHIELD": "Defensive Shield",
    "DEFENSIVE SHIELD": "Defensive Shield",
}

WIKI_TYPES: dict[str, str] | None = None
TYPE_CACHE = ROOT / "_wiki_card_types.json"
TYPE_OVERRIDE = {
    "spice mine operations": "Objective",
    "weapon levitation (jabba's palace)": "Interrupt",
    "weapon levitation (jabba's palace) (dark)": "Interrupt",
    # Premiere Anakin is a Character; GEMP bp wrongly stores it as INTERRUPT.
    "anakin skywalker": "Character",
    "tatooine (location)": "Location",
    "sai'torr kal fas": "Character",
    "rycar ryjerd": "Character",
    "quick draw": "Interrupt",
    "a gift": "Interrupt",
    "what about that blue one?": "Interrupt",
    "iceheart": "Effect",
    "the emperor's reach": "Effect",
    "defense of muunilinst": "Effect",
    "assault on muunilinst": "Effect",
    "imperial artillery": "Weapon",
    "rebel artillery": "Weapon",
    "arena execution": "Effect",
    "arena pillars": "Effect",
    "the phantom menace": "Effect",
    "gift of the master": "Effect",
    "war has begun": "Effect",
    "ni chuba na": "Effect",
    "ghhhk": "Interrupt",
    "ghtm & bp": "Interrupt",
    "u-2po": "Character",
    "skywalker avenger": "Interrupt",
    "bp, dh": "Interrupt",
    "another weapon": "Weapon",
    "oictw": "Defensive Shield",
    "chasm": "Location",
    "a close call": "Interrupt",
    "general bob hudson": "Character",
    "turbulence": "Interrupt",
    "after her": "Interrupt",
    "imperial detention": "Defensive Shield",
    "abyss": "Defensive Shield",
    "leave them to me": "Effect",
    "limited resources": "Effect",
    "owen lars and beru lars": "Character",
    "qui-gon with lightsaber": "Character",
    "slave one, symbol of fear": "Starship",
    "anger, fear, aggression": "Interrupt",
    # Virtual Block reprint is an Effect; Decipher AFA is the Lost Interrupt.
    "anger, fear, aggression (v)": "Effect",
    "are you brain dead?!": "Interrupt",
    "wes janson, veteran rogue": "Character",
    "kier santage": "Character",
    "drop!": "Interrupt",
    "imperial city": "Location",
    "sith's plans": "Effect",
    "quiet mining colony": "Objective",
    "set your course for alderaan": "Objective",
    "commence primary ignition": "Epic Event",
    "superlaser": "Device",
    "master kenobi": "Effect",
    "communing": "Epic Event",
    "combat response": "Effect",
    "redeemed apprentice": "Character",
    "elegant lightsaber": "Weapon",
    "visage of the emperor": "Effect",
    "spice mine administrator": "Character",
    "kessel: spice mines administration office": "Location",
    "kessel: spice mines extraction facility": "Location",
    "he is not ready & imperial propaganda": "Interrupt",
    "ghhhk & all too easy": "Interrupt",
    "masterful move & endor celebration": "Interrupt",
    "where are you taking this thing?": "Interrupt",
    "spice mine operations": "Objective",
    "knowledge and defense": "Interrupt",
    "the mandalorian, father of fett": "Character",
    "lando's luxury yacht": "Starship",
    "keeping the empire out forever": "Effect",
    "beldon's eye": "Effect",
    "imperial stockpile": "Effect",
    "a million voices crying out": "Effect",
    "tarkin doctrine": "Effect",
    "presence of the force": "Effect",
    "operational as planned": "Interrupt",
    "cease fire!": "Interrupt",
    "overwhelmed": "Interrupt",
    "force push": "Interrupt",
    "lateral damage": "Interrupt",
    "relentless pursuit": "Interrupt",
    "stunning leader": "Interrupt",
    "laser cannon battery": "Weapon",
    "fury fury": "Interrupt",
    "rebel gunrunner": "Character",
    "rug hug": "Interrupt",
    "draw their fire": "Effect",
    "use the force": "Interrupt",
    "blaster deflection": "Interrupt",
    "i hope she's all right": "Effect",
    "luke's bionic hand": "Device",
    "chewie's bowcaster": "Weapon",
    "great warrior": "Jedi Test",
    "a jedi's strength": "Jedi Test",
    "domain of evil": "Jedi Test",
    "size matters not": "Jedi Test",
    "it is the future you see": "Jedi Test",
    "you must confront vader": "Jedi Test",
    # Virtual Block reprint is an Epic Event; Decipher IITFYS is the Jedi Test.
    "it is the future you see (v)": "Epic Event",
    "hcfe": "Effect",
    "icbz": "Interrupt",
    "luvkk": "Character",
    "roltan": "Character",
    "vengeance of the sith": "Effect",
    "commander": "Character",
    "uutik": "Character",
    "gas tar girls": "Character",
    "incon barriers": "Effect",
    "scramble new meaning": "Interrupt",
    "scramble say the bits": "Interrupt",
    "iotdl": "Interrupt",
    "dthacc": "Interrupt",
    "stunned brawls": "Interrupt",
    "at-at deployment platform": "Location",
    "there is another": "Defensive Shield",
    "at-at": "Vehicle",
    "temporary truce": "Interrupt",
    "republic gunship": "Vehicle",
    "artoo-detoo": "Character",
    "jabba's palace": "Location",
    "cyborg commander": "Character",
    "embrace of the dark lord": "Interrupt",
    "tatooine (coruscant)": "Location",
    "sniper & dark strike": "Interrupt",
    "inconsequential barriers": "Effect",
    "chewie, enraged": "Character",
    "galen, secret apprentice": "Character",
    "mechanical failure": "Interrupt",
    "he will die for you": "Interrupt",
    "boshek's modified light freighter": "Starship",
    "desperate plea": "Interrupt",
    "we're jamming": "Interrupt",
    "garto, corellian": "Character",
    "fallen skies": "Effect",
    "relian": "Interrupt",
    "dark thunder": "Starship",
    "we're moving": "Interrupt",
    "oance ta": "Defensive Shield",
    "yes yak": "Character",
    "raikel ueesnn": "Character",
    "federation box gun": "Weapon",
    "system defense": "Effect",
    "cyborg commander, hunter of jedi": "Character",
    "moff disra, kessel admin": "Character",
    "mennek": "Character",
    "obsidian 16": "Starship",
    "a stunning move": "Interrupt",
    "lucky sighting": "Effect",
    "hoth blockade": "Effect",
    "retraining bolt": "Device",
    "obi-wan in radiant vii": "Starship",
    "wesa gotta grand army": "Interrupt",
    "trophy of a kill": "Device",
    "ability, ability, ability": "Effect",
    "it's a trap": "Interrupt",
    "galen's fighter": "Starship",
    "corellian engineer": "Character",
    "passport search": "Interrupt",
    "captured": "Effect",
    "battle": "Interrupt",
    "excellent": "Interrupt",
    "spaceport prefect": "Character",
    "cannon fodder": "Weapon",
    "men to load, you still have a choice": "Effect",
    "deception": "Interrupt",
    "crush of the saber": "Interrupt",
    "11-4d": "Character",
    "nocoo!": "Interrupt",
    "forgot ops": "Defensive Shield",
    "anger, fear, aggression & struggle of the throne": "Interrupt",
    "kashyyyk: security tower": "Location",
    "a jedi's concentration": "Interrupt",
    "han's blaster, so uncivilized": "Weapon",
    "captain yutani with blaster cannon": "Character",
    "comscan detection": "Interrupt",
    "kessel: cave": "Location",
    "spice mine administrator": "Character",
    "plan b": "Effect",
    "moynleyneugh": "Character",
    "dark maneuvers": "Interrupt",
    "inaccurate?": "Interrupt",
    "clutch": "Interrupt",
    "asoca": "Character",
    "stop! stop!": "Interrupt",
}


def load_wiki_types() -> dict[str, str]:
    global WIKI_TYPES
    if WIKI_TYPES is not None:
        return WIKI_TYPES
    if TYPE_CACHE.exists():
        import json
        WIKI_TYPES = json.loads(TYPE_CACHE.read_text(encoding="utf-8"))
        print("wiki types cache", len(WIKI_TYPES))
        return WIKI_TYPES
    idx: dict[str, str] = {}
    for p in PAGES.rglob("*.wiki"):
        try:
            head = p.read_text(encoding="utf-8", errors="replace")[:2500]
        except OSError:
            continue
        if "{{Card" not in head[:80] and not head.startswith("{{Card"):
            continue
        tm = re.search(r"\|title=([^\n]+)", head)
        ty = re.search(r"\|type=([^\n]+)", head)
        if not tm or not ty:
            continue
        title = tm.group(1).strip()
        typ = ty.group(1).strip()
        key = re.sub(r"\s+", " ", title.lower())
        idx.setdefault(key, typ)
        idx.setdefault(re.sub(r"\s*\(V\)\s*$", "", key, flags=re.I).strip(), typ)
        if " / " in title:
            a = title.split(" / ", 1)[0].strip().lower()
            idx.setdefault(a, typ)
    WIKI_TYPES = idx
    import json
    TYPE_CACHE.write_text(json.dumps(idx), encoding="utf-8")
    print("wiki types", len(idx))
    return idx


def canon_player(raw: str) -> str:
    return g15.canon(raw.strip())


def _norm_type(raw: str) -> str | None:
    t = (raw or "").strip()
    key = t.upper().replace("—", " ")
    if key in CAT_MAP:
        return CAT_MAP[key]
    # "Interrupt (Used Interrupt)" etc.
    base = re.split(r"[\s(]", t, maxsplit=1)[0].upper()
    return CAT_MAP.get(base)


def card_heading(
    name: str, prefer_sh: bool, by_title: dict, is_v: bool = False
) -> str:
    if prefer_sh:
        return "Defensive Shield"
    bare = re.sub(r"\s*\(V\)\s*$", "", name, flags=re.I).lower()
    ov_keys = [name.lower()]
    if is_v:
        ov_keys.insert(0, f"{bare} (v)")
    else:
        ov_keys.append(bare)
    for k in ov_keys:
        ov = TYPE_OVERRIDE.get(k)
        if ov:
            return ov
    if " / " in name:
        return "Objective"
    if ":" in name:
        return "Location"
    keys = [
        name.lower(),
        bare,
        name.split(" / ")[0].strip().lower(),
        re.sub(r"\s*\(AI\)\s*$", "", name, flags=re.I).lower(),
    ]
    if is_v:
        keys.insert(0, f"{bare} (v)")
    for k in keys:
        rec = by_title.get(k) or {}
        cat = (rec.get("cat") or rec.get("cardCategory") or "").upper().replace(" ", "_")
        if cat in CAT_MAP:
            return CAT_MAP[cat]
    dest = (
        w14._lookup(name, "Light", is_v) or w14._lookup(name, "Dark", is_v) or ""
    )
    wiki = load_wiki_types()
    dest_has_v = "(V)" in dest or is_v
    cands = [name, dest]
    if dest:
        cands.append(re.sub(r" \(Virtual Block \d+\)$", "", dest))
        cands.append(re.sub(r" \(Virtual Shields\)$", "", dest))
    for cand in cands:
        k = re.sub(r"\s+", " ", (cand or "").lower())
        k = re.sub(r" \(dark\)$", "", k)
        hit = wiki.get(k)
        if not hit and not dest_has_v:
            hit = wiki.get(re.sub(r"\s*\(v\)\s*$", "", k).strip())
        mapped = _norm_type(hit or "")
        if mapped:
            return mapped
    if dest:
        if "(Virtual Shields)" in dest:
            return "Defensive Shield"
        if " / " in dest:
            return "Objective"
        if ":" in dest:
            return "Location"
    return "Unknown"


def group_cards(cards: list[tuple[int, str, bool, bool]], by_title: dict):
    buckets: dict[str, list[tuple[int, str, bool, bool]]] = defaultdict(list)
    for qty, name, is_v, prefer_sh in cards:
        buckets[card_heading(name, prefer_sh, by_title, is_v)].append(
            (qty, name, is_v, prefer_sh)
        )
    groups = []
    for heading in TYPE_ORDER:
        if buckets.get(heading):
            groups.append((heading, buckets[heading]))
    for heading, rows in buckets.items():
        if heading not in TYPE_ORDER:
            groups.append((heading, rows))
    return groups


def render_groups(groups, side: str) -> str:
    blocks = []
    for heading, cards in groups:
        bits = [f"'''{heading}'''"]
        for qty, name, is_v, prefer_sh in cards:
            link = w14.wikilink(name, side, is_v, prefer_sh=prefer_sh)
            bits.append(f"* {qty}x {link}" if qty > 1 else f"* {link}")
        blocks.append("\n".join(bits))
    mid = (len(blocks) + 1) // 2
    left = "\n\n".join(blocks[:mid])
    right = "\n\n".join(blocks[mid:])
    return (
        '{| class="wikitable" style="width:100%;"\n'
        "|-\n"
        '| style="width:50%; vertical-align:top;" |\n'
        f"{left}\n"
        '| style="width:50%; vertical-align:top;" |\n'
        f"{right}\n"
        "|}\n"
    )


def starting_from_groups(groups, side: str) -> tuple[str, bool, bool, str]:
    """Return (name, is_v, prefer_sh, hub label) from Objective, else Jedi Test / Epic Event."""
    pick = None
    for want in ("Objective", "Epic Event", "Jedi Test"):
        for heading, cards in groups:
            if heading == want and cards:
                pick = cards[0]
                break
        if pick is not None:
            break
    if pick is None and groups and groups[0][1]:
        pick = groups[0][1][0]
    if pick is None:
        return "constructed", False, False, "constructed"
    _qty, name, is_v, prefer_sh = pick
    label = name.split(" / ")[0].strip()
    dest = w14._lookup(name, side, is_v, prefer_sh=prefer_sh) or ""
    if dest and "(V)" in dest and not label.endswith("(V)"):
        label = re.sub(r"\s*\(V\)\s*$", "", label) + " (V)"
    return name, is_v, prefer_sh, label


def deck_page(title, player, side_word, start_link, body) -> str:
    return f"""'''{title}''' was the {side_word} constructed list played by [[{player}]] at [[{EVENT}]] (Holotable).

== Deck info ==

* '''Starting Card:''' {start_link}
* '''Format:''' {FORMAT}
* '''Stage:''' Holotable

== Decklist ==

{body}
== Scan ==

Typed Holotable export from the Players Committee zip; no Xerox scan is on this page.

== See also ==

* [[{EVENT}]]
* [[{player}]]
* [[List of SWCCG tournaments]]

== Sources ==

* [{PC_ZIP} 2014 MPC Holotable zip], res.starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:2014]]
"""


def _load_mod(path: Path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


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
    groups = group_cards(cards + shields + add, by_title)
    unknown = [n for h, rows in groups if h == "Unknown" for _q, n, *_ in rows]
    if unknown:
        print(f"WARN {player} {side} Unknown types:", unknown)
    body = render_groups(groups, side)
    n_obj, is_v, prefer_sh, label = starting_from_groups(groups, side)
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
    title = f"2014 Match Play Championship {stage} {player} {'LS' if side == 'Light' else 'DS'} {label}"
    pdf_name = getattr(mod, "PDF", "2014 Match Play Championship Day 1.pdf")
    if "Consolation" in pdf_name or stage == "Consolation":
        pdf_url = PC_PDF_CONS
        pdf_label = "MPC-2014-Day-2-Consolation-Event.pdf"
    elif "Day 2" in pdf_name or stage == "Day 2":
        pdf_url = PC_PDF_D2
        pdf_label = "MPC-2014-Day-2-Main-Event.pdf"
    else:
        pdf_url = PC_PDF_D1
        pdf_label = "MPC-2014-Day-1-Main-Event.pdf"
    sources = [
        f"[{pdf_url} {pdf_label}], res.starwarsccg.org",
        f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
    ]
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2014]]"
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
        scan_caption=f"Page {page} of [[:File:{pdf_name}]].",
        username=w14.username_for(mod, side),
    )
    return title, write(title, page_txt), label, stage


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


def write_hub(players, dest, dt, hl, xerox_dt=None, xerox_hl=None, xerox_players=None) -> None:
    bits = ['{| class="wikitable sortable"', "! Player !! Dark !! Light"]
    for p in players:
        ds_page = dt.get((p, "Dark"))
        ls_page = dt.get((p, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        bits += ["|-", f"| [[{p}]] || {ds} || {ls}"]
    bits.append("|}")
    tbl = "\n".join(bits)
    xerox_sections = ""
    if xerox_dt and xerox_players:
        xhl = xerox_hl or {}
        for stage, heading in (
            ("Day 2", "Day 2"),
            ("Consolation", "Consolation"),
            ("Day 1", "Day 1"),
        ):
            plist = xerox_players.get(stage) or []
            if not plist:
                continue
            xerox_sections += f"\n== {heading} ==\n\n{_stage_table(plist, xerox_dt, xhl, stage)}\n"
    body = f"""'''2014 Match Play Championship''' was a Players Committee constructed event, 24–26 January 2014, using the pre-reset virtual pool ([[Legacy Open]]). The Holotable exports below are the published typed lists from that weekend.<ref name="zip">{PC_ZIP}</ref> Xerox Day 1, Day 2, and consolation sheets from the same event are listed below as those scans are transcribed. [[Kevin Shannon]] is the published Match Play Champion.<ref name="winners">https://www.starwarsccg.org/major-event-winners/</ref>

== Format ==

* '''Environment:''' {FORMAT}
* '''Site:''' —
* '''Dates:''' {DATES}
* '''Winner:''' [[Kevin Shannon]]

== Holotable ==

Published typed lists (every pair in the Holotable zip).

{tbl}
{xerox_sections}
== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[Legacy Open]]
* [{PC_ZIP} 2014 MPC Holotable zip]

== Sources ==

* [{PC_ZIP} 2014MPC_Holotable.zip], res.starwarsccg.org
* [{PC_PDF_D1} MPC-2014-Day-1-Main-Event.pdf], res.starwarsccg.org
* [{PC_PDF_D2} MPC-2014-Day-2-Main-Event.pdf], res.starwarsccg.org
* [{PC_PDF_CONS} MPC-2014-Day-2-Consolation-Event.pdf], res.starwarsccg.org
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
        f"| 2014-01-24 || [[2014 Match Play Championship|Match Play Championship]] "
        f"|| 24–26 January 2014 || — || [[Legacy Open]] || —"
    )
    if "2014 Match Play Championship" in text:
        return
    needle = (
        "| 2014-08-21 || [[2014 World Championship|World Championship]] || "
        "21–24 August 2014 || Toronto, Ontario || [[Legacy Open]] || [[Emil Wallin]]\n|}"
    )
    if needle in text:
        text = text.replace(
            needle,
            needle[:-2]
            + "|- \n"
            + row
            + "\n|}",
            1,
        )
        LIST.write_text(text, encoding="utf-8", newline="\n")
        return
    # fallback: insert before closing of 2014 table
    m = re.search(r"(== 2014 ==.*?)\|}\n", text, re.S)
    if m and "2014 Match Play Championship" not in m.group(0):
        text = text[: m.end() - 3] + "|- \n" + row + "\n|}\n" + text[m.end() :]
        LIST.write_text(text, encoding="utf-8", newline="\n")


def main() -> None:
    STUBS.mkdir(parents=True, exist_ok=True)
    _by_id, by_title = load_bp_simple()
    w14.EVENT = EVENT
    titles: list[tuple[str, str]] = []
    players: list[str] = []
    dt, hl = {}, {}
    dest = {}
    miss_total = 0
    unknown_total = 0

    files = sorted(HTD.glob("*.htd"))
    parsed = []
    for path in files:
        d = htd.parse_htd(path)
        stem = path.stem
        if " - " in stem:
            raw_player, _slang = stem.split(" - ", 1)
        else:
            raw_player = stem
        player = canon_player(raw_player)
        side = d["side"]
        miss_total += len(d["miss"])
        for m in d["miss"]:
            print("MISS", path.name, m)
        parsed.append((player, side, d, path))
        if player not in players:
            players.append(player)

    for player, side, d, path in parsed:
        groups = group_cards(d["cards"], by_title)
        unknown_total += sum(q for h, cards in groups if h == "Unknown" for q, *_ in cards)
        n_obj, is_v, prefer_sh, label = starting_from_groups(groups, side)
        start_link = w14.wikilink(n_obj, side, is_v, prefer_sh=prefer_sh)
        body = render_groups(groups, side)
        n = sum(q for q, *_ in d["cards"])
        print(path.name, player, side, "n", n, "start", label, "unknown", sum(1 for h, _ in groups if h == "Unknown"))
        title = f"2014 MPC Holotable {player} {'DS' if side == 'Dark' else 'LS'} {label}"
        page = deck_page(
            title,
            player,
            "Dark Side" if side == "Dark" else "Light Side",
            start_link,
            body,
        )
        rel = write(title, page)
        dt[(player, side)] = title
        hl[title] = label
        titles.append((title, rel))

    write_hub(players, dest, dt, hl)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))
    meta = {
        "title": EVENT,
        "year": "2014",
        "pc": PC_ZIP,
        "format": FORMAT,
    }
    for p in players:
        ds_page = dt.get((p, "Dark"))
        ls_page = dt.get((p, "Light"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        row = (
            f"|- \n| {DATES} || [[{EVENT}]] (Holotable) || {FORMAT} "
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
    print("tsv", TSV, "n", len(ordered), "miss", miss_total, "unknown_qty", unknown_total)


def leftover_xerox() -> None:
    """Emit Xerox leftover pages only. Do not rewrite Holotable deck pages."""
    STUBS.mkdir(parents=True, exist_ok=True)
    _by_id, by_title = load_bp_simple()
    load_wiki_types()
    w14.EVENT = EVENT
    titles: list[tuple[str, str]] = []
    xerox_dt, xerox_hl = {}, {}
    xerox_players: dict[str, list[str]] = {"Day 1": [], "Day 2": [], "Consolation": []}
    mods = []
    for path in sorted(EVENTS_DIR.glob("transcribe_mpc_*.py")):
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

    # Holotable table only (do not rewrite those deck pages).
    ht_players, ht_dt, ht_hl = [], {}, {}
    for path in sorted(HTD.glob("*.htd")):
        d = htd.parse_htd(path)
        stem = path.stem
        raw_player = stem.split(" - ", 1)[0] if " - " in stem else stem
        player = canon_player(raw_player)
        if player not in ht_players:
            ht_players.append(player)
        side = d["side"]
        groups = group_cards(d["cards"], by_title)
        n_obj, is_v, prefer_sh, label = starting_from_groups(groups, side)
        ht_title = f"2014 MPC Holotable {player} {'DS' if side == 'Dark' else 'LS'} {label}"
        ht_dt[(player, side)] = ht_title
        ht_hl[ht_title] = label

    write_hub(ht_players, {}, ht_dt, ht_hl, xerox_dt, xerox_hl, xerox_players)
    titles.append((EVENT, f"pages/{wiki_fname(EVENT)}"))

    meta = {
        "title": EVENT,
        "year": "2014",
        "pc": PC_PDF_D1,
        "format": FORMAT,
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
