#!/usr/bin/env python3
"""2014 World Championship hub + small PDF/Holotable transcription slice."""
from __future__ import annotations

import importlib.util
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
from generate_2015_2016 import inject_result_rows  # noqa: E402
from generate_2019_2021 import tidy_player_page, wiki_fname  # noqa: E402

PAGES = ROOT / "pages"


def _load_mod(name: str, rel: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    return mod


_shaw = _load_mod("transcribe_shaw", "encyclopedia/pc-2014-worlds/transcribe_shaw.py")
_p01 = _load_mod("transcribe_p01_changes", "encyclopedia/pc-2014-worlds/transcribe_p01_changes.py")
_sokol = _load_mod("transcribe_sokol", "encyclopedia/pc-2014-worlds/transcribe_sokol.py")
_angelo = _load_mod("transcribe_angelo", "encyclopedia/pc-2014-worlds/transcribe_angelo.py")
_aaron = _load_mod("transcribe_aaron_day2", "encyclopedia/pc-2014-worlds/transcribe_aaron_day2.py")
_brian = _load_mod("transcribe_brian_day2", "encyclopedia/pc-2014-worlds/transcribe_brian_day2.py")
_shaw_d2 = _load_mod("transcribe_shaw_day2", "encyclopedia/pc-2014-worlds/transcribe_shaw_day2.py")
SHAW_DS_RESERVE = list(_shaw.SHAW_DS_RESERVE)
SHAW_DS_SHIELDS = list(_shaw.SHAW_DS_SHIELDS)
SHAW_LS_RESERVE = list(_shaw.SHAW_LS_RESERVE)
SHAW_LS_SHIELDS = list(_shaw.SHAW_LS_SHIELDS)
P01_DS_RESERVE = list(_p01.P01_DS_RESERVE)
P01_DS_SHIELDS = list(_p01.P01_DS_SHIELDS)
P01_DS_ADD = list(_p01.P01_DS_ADD)
AARON_P11 = _p01.AARON_P11
AARON_P12 = _p01.AARON_P12
BRIAN_DS_P13 = _p01.BRIAN_DS_P13
BRIAN_LS_P14 = _p01.BRIAN_LS_P14
SOKOL_LS_RESERVE = list(_sokol.SOKOL_LS_RESERVE)
SOKOL_LS_SHIELDS = list(_sokol.SOKOL_LS_SHIELDS)
SOKOL_DS_RESERVE = list(_sokol.SOKOL_DS_RESERVE)
SOKOL_DS_SHIELDS = list(_sokol.SOKOL_DS_SHIELDS)
ANGELO_DS_RESERVE = list(_angelo.ANGELO_DS_RESERVE)
ANGELO_DS_SHIELDS = list(_angelo.ANGELO_DS_SHIELDS)
ANGELO_LS_RESERVE = list(_angelo.ANGELO_LS_RESERVE)
ANGELO_LS_SHIELDS = list(_angelo.ANGELO_LS_SHIELDS)
AARON_D2_LS_RESERVE = list(_aaron.AARON_D2_LS_RESERVE)
AARON_D2_LS_SHIELDS = list(_aaron.AARON_D2_LS_SHIELDS)
AARON_D2_LS_ADD = list(_aaron.AARON_D2_LS_ADD)
AARON_D2_DS_RESERVE = list(_aaron.AARON_D2_DS_RESERVE)
AARON_D2_DS_SHIELDS = list(_aaron.AARON_D2_DS_SHIELDS)
AARON_D2_DS_ADD = list(_aaron.AARON_D2_DS_ADD)
BRIAN_D2_LS_RESERVE = list(_brian.BRIAN_D2_LS_RESERVE)
BRIAN_D2_LS_SHIELDS = list(_brian.BRIAN_D2_LS_SHIELDS)
BRIAN_D2_LS_ADD = list(_brian.BRIAN_D2_LS_ADD)
BRIAN_D2_DS_RESERVE = list(_brian.BRIAN_D2_DS_RESERVE)
BRIAN_D2_DS_SHIELDS = list(_brian.BRIAN_D2_DS_SHIELDS)
BRIAN_D2_DS_ADD = list(_brian.BRIAN_D2_DS_ADD)
SHAW_D2_DS_RESERVE = list(_shaw_d2.SHAW_D2_DS_RESERVE)
SHAW_D2_DS_SHIELDS = list(_shaw_d2.SHAW_D2_DS_SHIELDS)
SHAW_D2_DS_ADD = list(_shaw_d2.SHAW_D2_DS_ADD)
SHAW_D2_LS_RESERVE = list(_shaw_d2.SHAW_D2_LS_RESERVE)
SHAW_D2_LS_SHIELDS = list(_shaw_d2.SHAW_D2_LS_SHIELDS)
SHAW_D2_LS_ADD = list(_shaw_d2.SHAW_D2_LS_ADD)
STUBS = PAGES / "player-stubs"
MAP = json.loads((ROOT / "card_title_map.json").read_text(encoding="utf-8"))
TSV = ROOT / "y2014-worlds-titles.tsv"
EVENT = "2014 World Championship"
CAT = "[[Category:2014]]"
FORUM_DAY3 = "https://forum.starwarsccg.org/viewtopic.php?t=55887"
FORUM_EMIL = "https://forum.starwarsccg.org/viewtopic.php?t=55902"
FORUM_PDF = "https://forum.starwarsccg.org/viewtopic.php?t=56104"
FORUM_FINALS = "https://forum.starwarsccg.org/viewtopic.php?t=55897"
FORUM_FORMAT = "https://forum.starwarsccg.org/viewtopic.php?t=54863"
HOF = "https://www.starwarsccg.org/hall-of-fame-awards/"

DECIPHER_SETS = set()
for k in MAP:
    sid = k.split("|", 1)[0]
    if sid.isdigit() and 1 <= int(sid) <= 14:
        DECIPHER_SETS.add(sid)
    if sid.isdigit() and 100 <= int(sid) <= 114:
        DECIPHER_SETS.add(sid)


def _norm(s: str) -> str:
    s = s.replace("•", "").replace("**", "").replace("*", "")
    s = re.sub(r"\s+", " ", s).strip()
    s = s.replace(" / ", "/").replace("/", " / ")
    s = s.replace(" & ", " & ")
    return s


def _index() -> dict[str, dict[tuple[str, str], str]]:
    vb: dict[tuple[str, str], str] = {}
    dec: dict[tuple[str, str], str] = {}
    sh: dict[tuple[str, str], str] = {}
    anyd: dict[tuple[str, str], str] = {}
    for k, dest in MAP.items():
        parts = k.split("|", 2)
        if len(parts) < 3:
            continue
        sid, side, name = parts
        key = (side, _norm(name).lower())
        anyd.setdefault(key, dest)
        if sid.startswith("vb"):
            vb[key] = dest
        elif sid in ("vsh", "setd"):
            sh[key] = dest
        elif sid in DECIPHER_SETS:
            dec.setdefault(key, dest)
    return {"vb": vb, "dec": dec, "sh": sh, "any": anyd}


IDX = _index()


def _name_variants(name: str) -> list[str]:
    n = _norm(name)
    out: list[str] = []
    def add(x: str) -> None:
        x = _norm(x)
        if x and x.lower() not in {y.lower() for y in out}:
            out.append(x)
    add(n)
    no_v = re.sub(r"\s*\(V\)\s*$", "", n, flags=re.I).strip()
    add(no_v)
    if " / " in no_v:
        a, b = [p.strip() for p in no_v.split(" / ", 1)]
        add(a)
        # Printed (V) duals stamp (V) on both faces (VB dests).
        add(f"{a} (V) / {b} (V)")
        add(f"{a} (V) / {b}")
        add(f"{a} / {b} (V)")
    if not n.lower().endswith("(v)"):
        add(n + " (V)")
        add(no_v + " (V)")
    return out


def _dist1(a: str, b: str) -> bool:
    """True when a and b differ by one insert, delete, or substitute."""
    if a == b:
        return False
    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False
    if la == lb:
        return sum(x != y for x, y in zip(a, b)) == 1
    if la > lb:
        a, b, la, lb = b, a, lb, la
    i = 0
    while i < la and a[i] == b[i]:
        i += 1
    return a[i:] == b[i + 1 :]


def _prefix_in_pool(pool: dict[tuple[str, str], str], side: str, written: str) -> str | None:
    """Sheet locations often omit '(Nth Marker)'."""
    needle = _norm(written).lower()
    if not needle:
        return None
    hits = [
        dest
        for (s, n), dest in pool.items()
        if s == side and n.startswith(needle + " (")
    ]
    if len(hits) == 1:
        return hits[0]
    return None


def _close_in_pool(pool: dict[tuple[str, str], str], side: str, written: str) -> str | None:
    """Unique edit-distance-1 hit (sheet typos: Sai'tor → Sai'torr)."""
    needle = _norm(written).lower()
    if len(needle) < 8:
        return None
    hits = [
        dest
        for (s, n), dest in pool.items()
        if s == side and _dist1(needle, n)
    ]
    uniq = list(dict.fromkeys(hits))
    if len(uniq) == 1:
        return uniq[0]
    return None


def _lookup(name: str, side: str, is_v: bool, prefer_sh: bool = False) -> str | None:
    """2014 is Legacy Open.

    Unchecked (V) → Decipher dest when a printed card exists; virtual-only
    titles (Imperial Entanglements, Communing, …) still take the Virtual Block
    dest. Checked (V) → Virtual Block / Virtual Shields. Shield lines prefer
    vsh over a same-title Virtual Block reprint. Never fall through to current
    virtual (set 200+) dests.
    """
    keys = [(side, v.lower()) for v in _name_variants(name)]
    virt = ("sh", "vb") if prefer_sh else ("vb", "sh")

    def search(pool_names: tuple[str, ...]) -> str | None:
        for pool in pool_names:
            for k in keys:
                if k in IDX[pool]:
                    return IDX[pool][k]
            for v in _name_variants(name):
                hit = _prefix_in_pool(IDX[pool], side, v)
                if hit:
                    return hit
            for v in _name_variants(name):
                hit = _close_in_pool(IDX[pool], side, v)
                if hit:
                    return hit
        return None

    if is_v or prefer_sh:
        return search(virt) or search(("dec",))
    return search(("dec",)) or search(virt)


def visible_for(dest: str, written: str, is_v: bool) -> str:
    # Strip uniqueness and (Virtual Block N) from dest for display.
    core = re.sub(r" \(Virtual Block \d+\)$", "", dest)
    core = re.sub(r" \(Virtual Shields\)$", "", core)
    core = re.sub(r" \(Dark\)$", "", core)
    core = core.replace("•", "")
    # Dual-title dest already has both printed faces, with (V) on each when
    # that dest has (V). Do not keep a written slang 7-side (I'm On The Leader).
    if " / " in core:
        return core
    if "(V)" in core:
        base = re.sub(r"\s*\(V\)\s*$", "", written)
        base = re.sub(r"\s*\(V\)\s*$", "", base)
        return f"{base} (V)" if not base.endswith("(V)") else base
    return re.sub(r"\s*\(V\)\s*$", "", written).strip() or written


def wikilink(name: str, side: str, is_v: bool = False, prefer_sh: bool = False) -> str:
    dest = _lookup(name, side, is_v, prefer_sh=prefer_sh)
    if not dest:
        shown = name if not is_v else (name if name.endswith("(V)") else f"{name} (V)")
        return f"[[{shown}]]"
    shown = visible_for(dest, name, is_v)
    if dest == shown:
        return f"[[{dest}]]"
    return f"[[{dest}|{shown}]]"


def numbered_block(
    items: list[tuple[str | None, bool]], side: str, prefer_sh: bool = False
) -> str:
    lines = []
    for name, is_v in items:
        if not name:
            lines.append("# &nbsp;")
        else:
            lines.append(f"# {wikilink(name, side, is_v, prefer_sh=prefer_sh)}")
    return "\n".join(lines)


def type_groups(groups: list[tuple[str, list[tuple[int, str, bool]]]], side: str) -> str:
    """Two-column type-grouped list (Holotable / 1996 shape)."""
    blocks = []
    for heading, cards in groups:
        bits = [f"'''{heading}'''"]
        for qty, name, is_v in cards:
            link = wikilink(name, side, is_v)
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


def colon_file(wikitext: str) -> str:
    return wikitext.replace("[[File:", "[[:File:")


def scan_cite_table(scan_file: str, ref_body: str) -> str:
    return (
        '{| style="margin:0 auto;border:0;border-collapse:collapse;background:transparent"\n'
        "|-\n"
        f'| style="vertical-align:top;border:0;padding:0" | [[File:{scan_file}|800px]]\n'
        f'| style="vertical-align:top;border:0;padding:0 0 0 0.2em;line-height:1" | <ref>{ref_body}</ref>\n'
        "|}"
    )


_TRANSCRIBE_DUMP_MARKERS = (
    " dested ",
    "dested here",
    "dested on this page",
    "not dested",
    "dittos inherit",
    "form left column reprints",
    "(v) from the checkbox",
    "as written.",
    "handwritten 2010 xerox",
    "typed 2010 xerox",
    "typed printout (not a handwritten",
    "typed slang printout",
    "typed numbered printout",
    "typed holotable printout",
    "informal handwritten list",
    "informal overlay",
)


def public_extra_note(note: str | None) -> str:
    """Keep encyclopedia copy. Drop transcribe dest dumps (LS_NOTE / dested / as written)."""
    if not note:
        return ""
    text = str(note).strip()
    if not text:
        return ""
    low = text.lower()
    if any(m in low for m in _TRANSCRIBE_DUMP_MARKERS):
        return ""
    return text


def extra_note_for(mod, side: str) -> str:
    note = getattr(mod, "PUBLIC_NOTE", None) or getattr(
        mod, "LS_PUBLIC_NOTE" if side == "Light" else "DS_PUBLIC_NOTE", None
    )
    return public_extra_note(note)


def username_for(mod, side: str) -> str:
    specific = getattr(
        mod, "LS_USERNAME" if side == "Light" else "DS_USERNAME", None
    )
    if specific is not None:
        return str(specific).strip()
    return str(getattr(mod, "USERNAME", "") or "").strip()


def deck_page(
    title: str,
    player: str,
    side_word: str,
    starting: str,
    stage: str,
    body: str,
    sources: list[str],
    extra_note: str = "",
    files: list[str] | None = None,
    scan_file: str | None = None,
    scan_caption: str = "",
    extra_scans: list[tuple[str, str]] | None = None,
    extra_sections: list[tuple[str, str]] | None = None,
    player_page: str | None = None,
    username: str = "",
) -> str:
    start_link = starting
    extra_note = public_extra_note(extra_note)
    src = "\n".join(f"* {s}" for s in sources)
    scan_bits: list[str] = []
    if scan_file:
        ref = colon_file(scan_caption) if scan_caption else f"[[:File:{scan_file}]]"
        scan_bits.append(scan_cite_table(scan_file, ref))
    for extra_file, extra_cap in extra_scans or []:
        eref = colon_file(extra_cap) if extra_cap else f"[[:File:{extra_file}]]"
        scan_bits.append(scan_cite_table(extra_file, eref))
    if not scan_bits and files:
        scan_bits.extend(f"* [[File:{f}]]" for f in files)
    file_bits = ("\n\n".join(scan_bits) + "\n") if scan_bits else ""
    note = f"\n{extra_note}\n" if extra_note else "\n"
    extra_wiki = ""
    for heading, section_body in extra_sections or []:
        extra_wiki += f"\n== {heading} ==\n\n{section_body}\n"
    see = [
        f"* [[{EVENT}]]",
        "* [[List of SWCCG tournaments]]",
    ]
    dest = player_page or player
    if player and player not in {"unnamed", "Unknown Player"}:
        if dest and dest != player:
            who = f"[[{dest}|{player}]]"
            see.insert(1, f"* [[{dest}|{player}]]")
        else:
            who = f"[[{player}]]"
            see.insert(1, f"* [[{player}]]")
    else:
        who = "[[Unknown Player]]"
        see.insert(1, "* [[Unknown Player]]")
        see.insert(2, "* [[Unknown players]]")
    info = [f"* '''Starting Card:''' {start_link}"]
    if username:
        info.append(f"* '''Username:''' {username}")
    info += ["* '''Format:''' [[Legacy Open]]", f"* '''Stage:''' {stage}"]
    return f"""'''{title}''' was the {side_word} constructed list played by {who} at [[{EVENT}]] ({stage}).
{note}
== Deck info ==

{chr(10).join(info)}

== Decklist ==

{body}
{extra_wiki}
== Scan ==

{file_bits if file_bits else "Typed onto the Players Committee forum; no scan of this list is on the wiki yet."}

== See also ==

{chr(10).join(see)}

== Sources ==

{src}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
{CAT}
"""


def write(title: str, text: str) -> str:
    raw = wiki_fname(title)
    if raw.endswith(".wiki"):
        fn = raw
    else:
        fn = raw + ".wiki"
    fn = fn.replace(":", "_")
    path = PAGES / fn
    text = text.replace("\r\n", "\n")
    if not text.endswith("\n"):
        text += "\n"
    path.write_text(text, encoding="utf-8", newline="\n")
    return f"pages/{fn}"


# --- Emil Holotable (type-grouped; leave as typed, not 1–60) ---
EMIL_D3_LS_GROUPS = [
    ("Objective", [(1, "Mind What You Have Learned / Save You It Can (V)", True)]),
    ("Character", [
        (2, "Lando Calrissian, Unlikely Hero", False),
        (1, "Threepio With His Parts Showing", False),
        (1, "Yoda (V)", True),
        (1, "Jaina Solo", False),
        (1, "Wedge Antilles, Red Squadron Leader", False),
        (2, "Luke Skywalker (V)", True),
        (1, "Daughter Of Skywalker (V)", True),
        (1, "Major Haash'n", False),
        (1, "General Airen Cracken", False),
        (1, "Admiral Ackbar (V)", True),
    ]),
    ("Device", [(1, "Luke's Backpack", False)]),
    ("Effect", [
        (1, "Reflection (V)", True),
        (1, "Launching The Assault", False),
        (2, "Projection Of A Skywalker", False),
        (1, "Much To Learn, You Still Have", False),
        (1, "Battle Plan & Draw Their Fire", False),
        (1, "Do, Or Do Not & Wise Advice", False),
        (1, "Squadron Assignments", False),
        (1, "Seeking An Audience (V)", True),
        (1, "The Way Of Things", False),
        (2, "Imperial Atrocity (V)", True),
        (1, "Legendary Starfighter", False),
        (1, "Anger, Fear, Aggression (V)", True),
    ]),
    ("Epic Event", [
        (1, "Strong Is Vader", False),
        (1, "It Is The Future You See (V)", True),
    ]),
    ("Interrupt", [
        (3, "Rebel Leadership (V)", True),
        (1, "We're Doomed", False),
        (1, "A Few Maneuvers", False),
        (2, "It Could Be Worse", False),
        (2, "Escape Pod (V)", True),
        (2, "All Wings Report In & Darklighter Spin", False),
        (1, "Grimtaash", False),
        (3, "Let The Wookiee Win (V)", True),
    ]),
    ("Location", [
        (1, "Dagobah: Swamp", False),
        (1, "Dagobah: Jungle", False),
        (1, "Dagobah: Yoda's Hut", False),
        (1, "Dagobah", False),
        (1, "Nar Shaddaa", False),
        (1, "Naboo", False),
    ]),
    ("Starship", [
        (1, "Tantive IV (V)", True),
        (1, "Home One", False),
        (3, "Artoo-Detoo In Red 5", False),
        (1, "Lady Luck", False),
        (1, "Obi-Wan In Radiant VII", False),
        (1, "Red Squadron 1", False),
        (1, "Han, Chewie, And The Falcon (V)", True),
    ]),
]

EMIL_D3_DS_GROUPS = [
    ("Objective", [(1, "Wookiee Slaving Operation / Indentured To The Empire", False)]),
    ("Character", [
        (1, "Jango Fett, The Assassin", False),
        (1, "Ephant Mon", False),
        (1, "Velken Tezeri (V)", True),
        (1, "Garindan (V)", True),
        (1, "Prince Xizor", False),
        (1, "Dengar With Blaster Carbine (V)", True),
        (4, "Outer Rim Scout", False),
        (1, "Ponda Baba (V)", True),
        (1, "Jabba The Hutt (V)", True),
        (1, "Mercenary Pilot (V)", True),
        (1, "Lady Valarian", False),
        (1, "Bossk With Mortar Gun (V)", True),
        (1, "Boba Fett, Prepared Hunter", False),
        (1, "IG-88 With Riot Gun", False),
        (1, "OOM-9 (V)", True),
        (1, "P-59", False),
        (1, "4-LOM With Concussion Rifle", False),
        (1, "Probot", False),
    ]),
    ("Effect", [
        (1, "Something Special Planned For Them (V)", True),
        (1, "Hutt Bounty (V)", True),
        (1, "Den Of Thieves & Special Delivery", False),
        (2, "Scum And Villainy", False),
        (1, "Jabba's Haven", False),
        (1, "Power Of The Hutt", False),
        (1, "Mercenary Slavers", False),
        (1, "Search And Destroy", False),
        (1, "Imperial Propaganda (V)", True),
        (1, "Knowledge And Defense (V)", True),
    ]),
    ("Interrupt", [
        (1, "Ghhhk", False),
        (1, "Elis Helrot", False),
        (3, "Sonic Bombardment (V)", True),
        (1, "They're Still Coming Through!", False),
        (1, "Sith Fury & End This Destructive Conflict", False),
        (2, "Imperial Barrier", False),
        (1, "Force Push", False),
        (1, "Masterful Move", False),
        (1, "Imbalance & Kintan Strider", False),
        (1, "Why Didn't You Tell Me? (V)", True),
        (1, "Ommni Box & It's Worse", False),
        (1, "Monnok", False),
        (1, "Short Range Fighters & Watch Your Back!", False),
        (1, "Wookiee Subjugation", False),
    ]),
    ("Location", [
        (1, "Kashyyyk: Wookiee Slaving Camp", False),
        (1, "Kashyyyk: Skyhook Platform", False),
        (1, "Jabba's Sail Barge: Passenger Deck", False),
        (1, "Kashyyyk: Slaving Camp Headquarters", False),
        (1, "Kashyyyk", False),
        (1, "Nal Hutta", False),
    ]),
    ("Starship", [
        (1, "Jabba's Space Cruiser (V)", True),
        (1, "Zuckuss In Mist Hunter", False),
        (1, "Slave I, Symbol Of Fear", False),
    ]),
    ("Vehicle", [(1, "Jabba's Sail Barge (V)", True)]),
]

EMIL_D2_DS_GROUPS = [
    ("Objective", [(1, "Imperial Entanglements / No One To Stop Us This Time", False)]),
    ("Admiral's Order", [(1, "Intensify The Forward Batteries", False)]),
    ("Character", [
        (1, "Admiral Motti (V)", True),
        (1, "Admiral Piett", False),
        (4, "Elite Squadron Stormtrooper (V)", True),
        (1, "ISB Sector Commander", False),
        (6, "Imperial Stormtrooper", False),
        (1, "Grand Admiral Thrawn", False),
    ]),
    ("Device", [(1, "Deflector Shield Generators (V)", True)]),
    ("Effect", [
        (1, "Imperial Domination (V)", True),
        (1, "Imperial Stockpile", False),
        (1, "Strategic Reserves (V)", True),
        (2, "Tatooine Occupation", False),
        (1, "Endor Shield (V)", True),
        (1, "Imperial Academy Training (V)", True),
        (1, "Imperial Propaganda (V)", True),
        (1, "Knowledge And Defense (V)", True),
    ]),
    ("Interrupt", [
        (2, "Ghhhk", False),
        (1, "Control", False),
        (2, "A Dark Time For The Rebellion (V)", True),
        (1, "Operational As Planned (V)", True),
        (1, "Imperial Barrier", False),
        (2, "Masterful Move", False),
        (2, "Outflank (V)", True),
        (1, "Sith Fury & End This Destructive Conflict", False),
        (2, "Trooper Assault", False),
        (2, "Wounded Warrior", False),
        (1, "Cold Feet (V)", True),
        (3, "Imperial Command", False),
        (1, "Close Call (V)", True),
        (2, "Coordinated Attack (V)", True),
        (1, "Prepared Defenses", False),
    ]),
    ("Location", [
        (1, "Tatooine: Mos Eisley", False),
        (1, "Tatooine: Imperial Vanguard Camp", False),
        (1, "Tatooine: Watto's Junkyard", False),
        (1, "Tatooine: Imperial Outpost", False),
        (1, "Tatooine: Mos Espa", False),
        (1, "Tatooine", False),
    ]),
    ("Starship", [
        (1, "Devastator", False),
        (1, "Victory", False),
    ]),
    ("Weapon", [
        (1, "Blaster Rifle (V)", True),
        (1, "Laser Cannon Battery", False),
    ]),
]


def n(name: str | None, v: bool = False) -> tuple[str | None, bool]:
    return (name, v)


# Chris Terwilliger Y4 Light — 2010 form, one line per copy; "" expanded.
CHRIS_LS_RESERVE = [
    n("There Is Good In Him / I Can Save Him"),
    n("I Feel The Conflict"),
    n("Luke's Lightsaber"),
    n("Endor: Chief Chirpa's Hut"),
    n("Endor: Landing Platform (Docking Bay)"),
    n("Naboo: Battle Plains"),
    n("Rebel Barrier"),
    n("Lando Calrissian, Scoundrel"),
    n("Lando Calrissian, Scoundrel"),
    n("Sense"),
    n("Sense"),
    n("Seeking An Audience", True),
    n("Wesa Gotta Grand Army"),
    n("Wesa Gotta Grand Army"),
    n("Wesa Gotta Grand Army"),
    n("Blaster Deflection"),
    n("Blaster Deflection"),
    n("Houjix"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Qui-Gon Jinn With Lightsaber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Rebel Leadership", True),
    n("Rebel Leadership", True),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Chewie, Enraged"),
    n("Chewie, Enraged"),
    n("Leia With Blaster Rifle"),
    n("Han With Heavy Blaster Pistol"),
    n("Han With Heavy Blaster Pistol"),
    n("Grimtaash"),
    n("Imperial Atrocity", True),
    n("Yavin 4: Massassi War Room", True),
    n("Mace Windu, Master Of The Order", True),
    n(None),  # Obi-Wan's Stick — unread
    n(None),
    n("Home One: War Room"),
    n("Dark Approach", True),
    n("Dark Approach", True),
    n("Jedi Levitation", True),
    n("Don't Tread On Me", True),
    n("Escape Pod", True),
    n("Anakin Skywalker, Padawan Learner", True),
    n("Nabrun Leids"),
    n("Tantive IV"),  # box unchecked
    n("A Jedi's Resilience"),
    n("Luke Skywalker, Rebel Scout", True),
    n("Coruscant: Jedi Council Chamber", True),
    n("Luke Skywalker, Jedi Knight"),
    n("Clash Of Sabers"),
    n("Guardian's Lightsaber", True),
    n("Corran Horn"),
    n("Leia, Rebel Princess"),
    n("Admiral Ackbar", True),
    n("Home One"),
    n(None),  # Kashyyyk Forested… — unread
    n("Anger, Fear, Aggression", True),
]
CHRIS_LS_SHIELDS = [
    n("Jabba's Prize", True),
    n("Your Insight Serves You Well", True),
    n("Affect Mind", True),
    n("Ultimatum"),
    n("Simple Tricks And Nonsense", True),
    n("Wise Advice"),
    n("Aim High"),
    n("Yavin Sentry", True),
    n("The Professor", True),
    n("Let's Keep A Little Optimism Here", True),
    n("Weapons Display", True),
    n("Battle Plan"),
]
CHRIS_LS_ADD = [
    n("Chasm", True),
    n(None),
    n("A Tragedy Has Occurred"),
]


def numbered_deck(reserve, shields, additional, side: str) -> str:
    parts = ["=== Reserve Deck ===", numbered_block(reserve, side)]
    if shields:
        parts += ["", "=== Defensive Shields ===", numbered_block(shields, side, prefer_sh=True)]
    if additional:
        parts += [
            "",
            "=== Additional cards ===",
            numbered_block(additional, side, prefer_sh=True),
        ]
    return "\n".join(parts)


def change_section(d: dict, side: str) -> str:
    """OUT/IN change-sheet body. Items are (name, is_v, qty)."""

    def lines(items: list) -> str:
        out = []
        for item in items:
            name, is_v, qty = item[0], item[1], item[2] if len(item) > 2 else 1
            if not name:
                out.append("# &nbsp;")
                continue
            link = wikilink(name, side, is_v)
            out.append(f"# {qty}× {link}" if qty > 1 else f"# {link}")
        return "\n".join(out)

    return f"=== Out ===\n{lines(d['out'])}\n\n=== In ===\n{lines(d['in'])}\n"


# MHT Day 3 Light — 2013 typed form. Ditto expanded. Cross-outs use the replacement.
MHT_LS_RESERVE = [
    n("Tatooine: Slave Quarters"),
    n("Tatooine: Obi-Wan's Hut", True),
    n("Tatooine"),
    n("Jabba's Palace: Audience Chamber"),
    n("Naboo: Boss Nass' Chambers"),
    n("Communing"),
    n("Master Kenobi"),
    n("Quick Draw", True),
    n("Sai'torr Kal Fas", True),  # sheet types Sai'tor (one r); dest is Sai'torr VB1
    n("Wokling", True),
    n("Luke Skywalker, Strong In The Force"),
    n("Luke Skywalker, Strong In The Force"),
    n("Luke Skywalker, Strong In The Force"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Anakin Skywalker, Padawan Learner"),
    n("Yoda, Great Warrior"),
    n("Leia, Rebel Princess"),
    n("Leia, Rebel Princess"),
    n("Shmi Skywalker"),
    n("Threepio With His Parts Showing"),
    n("Corran Horn"),
    n("Han With Heavy Blaster Pistol"),
    n("All Wings Report In & Darklighter Spin"),
    n("Dash Rendar", True),
    n("Padme Naberrie", True),
    n("Wedge Antilles, Red Squadron Leader"),
    n("Lando Calrissian, Unlikely Hero"),
    n("Jaina Solo"),
    n("Lady Luck"),
    n("Artoo-Detoo In Red 5"),
    n("Luke's Lightsaber"),
    n("Anakin's Lightsaber"),
    n("Leia's Blaster Rifle"),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win", True),
    n("Let The Wookiee Win", True),
    n("All Wings Report In & Darklighter Spin"),
    n("Run Luke, Run!", True),
    n("Run Luke, Run!", True),
    n("Escape Pod", True),
    n("Escape Pod", True),
    n("Houjix"),
    n("Padme Naberrie", True),  # It Could Be Worse crossed out
    n("Wesa Gotta Grand Army"),
    n("Wesa Gotta Grand Army"),
    n("Wesa Gotta Grand Army"),
    n("Jedi Levitation", True),
    n("Yub Yub, Commander", True),
    n("Yub Yub, Commander", True),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Sorry About The Mess & Blaster Proficiency"),
    n("Flash Of Insight", True),
    n("Grimtaash"),  # handwritten; (V) box marked but no (V) printing
    n("Luke's Bionic Hand", True),
    n("Luke's Bionic Hand", True),
    n("Hear Me Baby, Hold Together", True),
    n("K'lor'slug", True),
    n("Seeking An Audience", True),
    n("Anger, Fear, Aggression", True),
]
MHT_LS_SHIELDS = [
    n("A Tragedy Has Occurred"),
    n("Chasm", True),
    n("Do, Or Do Not"),
    n("Wise Advice"),
    n("Weapons Display", True),
    n("The Professor", True),
    n("Affect Mind", True),
    n("Your Insight Serves You Well", True),
    n("Only Jedi Carry That Weapon"),
    n("Ultimatum"),
    n("Let's Keep A Little Optimism Here", True),
    n("Yavin Sentry", True),
    n("Simple Tricks And Nonsense"),
    n("Battle Plan"),
    n("Aim High"),
]

MHT_DS_RESERVE = [
    n("Imperial Occupation / Imperial Control", True),
    n("Hoth"),
    n("Hoth: Ice Plains", True),
    n("Hoth: Defensive Perimeter"),
    n("Hoth: Main Power Generators", True),
    n("Hoth: Mountains"),
    n("Imperial Decree"),
    n("You May Start Your Landing", True),
    n("Ni Chuba Na", True),
    n("Endor Shield", True),
    n("Prepared Defenses", True),
    n("Darth Vader, Dark Lord Of The Sith", True),
    n("Jango Fett, The Assassin"),
    n("Grand Moff Tarkin", True),
    n("General Nevar"),
    n("Garindan", True),
    n("Garindan", True),
    n("Grand Admiral Thrawn", True),
    n("General Veers", True),
    n("Commander Igar", True),
    n("Mara Jade With Lightsaber"),
    n("Admiral Piett"),
    n("Maarek Stele, The Emperor's Reach"),
    n("Admiral Motti", True),
    n("Blizzard 1", True),
    n("Blizzard 2", True),
    n("Blizzard 4"),
    n("Blizzard 4"),
    n("Marquand In Blizzard 6"),
    n("Tempest 1"),
    n("Victory"),
    n("Conquest", True),
    n("Conquest", True),
    n("Flagship Executor"),
    n("AT-AT Cannon", True),
    n("We're In Attack Position Now"),
    n("We're In Attack Position Now"),
    n("Image Of The Dark Lord", True),
    n("Do They Have A Code Clearance?"),
    n("No Escape"),
    n("Hoth Blockade"),
    n("Wipe Them Out, All Of Them", True),
    n("Cold Feet", True),
    n(None),  # Control + SFS — unread
    n("I Had No Choice"),  # Crash Landing crossed out
    n("Force Push", True),
    n("Force Push", True),
    n("Imperial Command"),
    n("Imperial Command"),
    n("Imperial Command"),
    n("A Dark Time For The Rebellion"),
    n("A Dark Time For The Rebellion", True),
    n("Stop Motion", True),
    n("Walker Garrison"),
    n("Trample"),
    n("Operational As Planned", True),
    n("Imperial Decree"),
    n("Target The Main Generator", True),
    n(None),  # Surprise crossed out; replacement unread
    n("Knowledge And Defense", True),
]
MHT_DS_SHIELDS = [
    n("Oppressive Enforcement"),
    n("Resistance"),
    n("Firepower", True),
    n("After Her", True),
    n("Secret Plans"),
    n("Abyss", True),
    n("Allegations Of Corruption"),
    n("There Is No Try"),
    n("Battle Order"),
    n("Come Here You Big Coward"),
    n("Fanfare", True),
    n("Death Star Sentry", True),
    n("You Cannot Hide Forever", True),
    n("A Useless Gesture", True),
    n("We'll Let Fate-a Decide, Huh?"),
]


def hub(day2_extra: str = "") -> str:
    emil_ls = "2014 Worlds Day 3 Emil Wallin LS Mind What You Have Learned"
    emil_ds = "2014 Worlds Day 3 Emil Wallin DS Wookiee Slaving Operation"
    emil_d2 = "2014 Worlds Day 2 Emil Wallin DS Imperial Entanglements"
    chris_ls = "2014 Worlds Day 3 Chris Terwilliger LS There Is Good In Him"
    chris_ds = "2014 Worlds Day 3 Chris Terwilliger DS Hoth (V)"
    mht_ls = "2014 Worlds Day 3 Matthew Harrison-Trainor LS Communing"
    mht_ds = "2014 Worlds Day 3 Matthew Harrison-Trainor DS Imperial Occupation"
    shaw_ls = "2014 Worlds Day 3 Greg Shaw LS It Is The Future You See"
    shaw_ds = "2014 Worlds Day 3 Greg Shaw DS Hunt Down"
    sokol_ls = "2014 Worlds Day 3 Matt Sokol LS Quiet Mining Colony"
    sokol_ds = "2014 Worlds Day 3 Matt Sokol DS Hunt Down"
    angelo_ls = "2014 Worlds Day 3 Angelo Consoli LS We'll Handle This (V)"
    angelo_ds = "2014 Worlds Day 3 Angelo Consoli DS A Stunning Move"
    aaron_ls = "2014 Worlds Day 3 Aaron Kingery LS Hidden Base"
    aaron_ds = "2014 Worlds Day 3 Aaron Kingery DS Separatist Uprising"
    brian_ls = "2014 Worlds Day 3 Brian Terwilliger LS Hidden Base"
    brian_ds = "2014 Worlds Day 3 Brian Terwilliger DS Wookiee Slaving Operation"
    return f"""'''2014 World Championship''' was the Players Committee World Championship in Toronto, Ontario, 21–24 August 2014. [[Emil Wallin]] defeated [[Brian Terwilliger]] (forum name Brian Twigg) in the finals.<ref name="finals">{FORUM_FINALS}</ref><ref name="hof">{HOF}</ref> The main event used the pre-reset virtual pool ([[Legacy Open]]); the 2014 Reset side event is a separate tournament.<ref name="format">{FORUM_FORMAT}</ref>

== Format ==

* '''Environment:''' [[Legacy Open]]
* '''Site:''' Toronto, Ontario
* '''Dates:''' 21–24 August 2014
* '''Winner:''' [[Emil Wallin]]
* '''Runner-up:''' [[Brian Terwilliger]]

== Finals ==

[[Emil Wallin]] vs [[Brian Terwilliger]]. Game 1: Emil Light by 6 on time.<ref name="finals" />

== Day 3 ==

Top 8 pairings as posted by raith.<ref name="day3">{FORUM_DAY3}</ref> Quarterfinals: Emil 2–0 [[Aaron Kingery]]; the semifinals were [[Matthew Harrison-Trainor]], [[Angelo Consoli]], Emil, and Brian Terwilliger.<ref name="day3" /> Live reports: Brian game 1 over MHT by 34 (Mon Cals over walkers); Angelo game 1 by 13 (A Stunning Move over Mind What You Have Learned).<ref name="day3" /> Emil beat Angelo and Brian beat MHT to reach the finals.

{{| class="wikitable sortable"
! Seed !! Player !! Dark !! Light
|-
| 1 || [[Emil Wallin]] || [[{emil_ds}|Wookiee Slaving Operation]] || [[{emil_ls}|Mind What You Have Learned]]
|-
| 2 || [[Matthew Harrison-Trainor]] || [[{mht_ds}|Imperial Occupation]] || [[{mht_ls}|Communing]]
|-
| 3 || [[Matt Sokol]] || [[{sokol_ds}|Hunt Down And Destroy The Jedi]] || [[{sokol_ls}|Quiet Mining Colony]]
|-
| 4 || [[Angelo Consoli]] || [[{angelo_ds}|A Stunning Move]] || [[{angelo_ls}|We'll Handle This (V)]]
|-
| 5 || [[Chris Terwilliger]] || [[{chris_ds}|Imperial Occupation (V)]] || [[{chris_ls}|There Is Good In Him]]
|-
| 6 || [[Brian Terwilliger]] || [[{brian_ds}|Wookiee Slaving Operation]] || [[{brian_ls}|Hidden Base]]
|-
| 7 || [[Greg Shaw]] || [[{shaw_ds}|Hunt Down And Destroy The Jedi (V)]] || [[{shaw_ls}|It Is The Future You See]]
|-
| 8 || [[Aaron Kingery]] || [[{aaron_ds}|Separatist Uprising]] || [[{aaron_ls}|Hidden Base]]
|}}

Chris Terwilliger, [[Aaron Kingery]], and [[Brian Terwilliger]] turned in Day 3 OUT/IN change sheets. Chris's submitted Dark 60 is page 1 of the Day 3 PDF (not in the Day 2 parts); that 60 and the change sheet are both on his Dark article. Aaron and Brian's submitted 60s are in the Day 2 PDFs and are copied onto their Day 3 articles.

== Day 2 ==

Emil went 3–1. [[Matt Sokol]] beat the Imperial Entanglements list by destroying Devastator and putting Legendary Starfighter on the Falcon.<ref name="emil">{FORUM_EMIL}</ref> Chris Terwilliger's Day 2 Dark was never in the zip (Advocate, t=56104).

{{| class="wikitable sortable"
! Player !! Dark !! Light
|-
| [[Emil Wallin]] || [[{emil_d2}|Imperial Entanglements]] || [[2014 Worlds Day 2 Emil Wallin LS Communing|Communing]]
|-
| [[Brian Terwilliger]] || [[2014 Worlds Day 2 Brian Terwilliger DS Wookiee Slaving Operation|Wookiee Slaving Operation]] || [[2014 Worlds Day 2 Brian Terwilliger LS Hidden Base|Hidden Base]]
|-
| [[Aaron Kingery]] || [[2014 Worlds Day 2 Aaron Kingery DS Separatist Uprising|Separatist Uprising]] || [[2014 Worlds Day 2 Aaron Kingery LS Hidden Base|Hidden Base]]
|-
| [[Greg Shaw]] || [[2014 Worlds Day 2 Greg Shaw DS Hunt Down|Hunt Down And Destroy The Jedi (V)]] || [[2014 Worlds Day 2 Greg Shaw LS Yavin 4|Yavin 4: Massassi Throne Room]]
{day2_extra}|}}

Day 2 Xerox scans: [[File:2014 Worlds Day 2 Part 1.pdf]], [[File:2014 Worlds Day 2 Part 2.pdf]], [[File:2014 Worlds Day 2 Part 3.pdf]].

== Scans ==

JediJer posted the Xerox scans on 6 September 2014; several files were upside down on the forum and are rotated 180° here.<ref name="pdf">{FORUM_PDF}</ref>

* [[File:2014 Worlds Day 3.pdf]]
* [[File:2014 Worlds Day 2 Part 1.pdf]]
* [[File:2014 Worlds Day 2 Part 2.pdf]]
* [[File:2014 Worlds Day 2 Part 3.pdf]]
* [[File:2014 Worlds Chris Terwilliger Y4.pdf]] — Chris Terwilliger Day 3 Light (deck name Y4)

== See also ==

* [[Legacy Open]]
* [[2014 Virtual Card Pool Reset]]
* [[Emil Wallin]]
* [[Brian Terwilliger]]
* [[Chris Terwilliger]]
* [[Matthew Harrison-Trainor]]
* [[Greg Shaw]]
* [[Matt Sokol]]
* [[Angelo Consoli]]
* [[Aaron Kingery]]
* [[List of SWCCG tournaments]]
* [[Championships]]

== Sources ==

* [https://forum.starwarsccg.org/viewtopic.php?t=55887 Day 3 pairings], forum.starwarsccg.org
* [https://forum.starwarsccg.org/viewtopic.php?t=55897 FINALS], forum.starwarsccg.org
* [https://forum.starwarsccg.org/viewtopic.php?t=55902 World Champions Decklists] (Emil typed lists), forum.starwarsccg.org
* [https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists] (PDF scans), forum.starwarsccg.org
* [https://forum.starwarsccg.org/viewtopic.php?t=54863 Worlds Format (card pool)], forum.starwarsccg.org
* [https://www.starwarsccg.org/hall-of-fame-awards/ Hall of Fame Awards], starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Championships]]
{CAT}
"""


def legacy_open() -> str:
    return """'''Legacy Open''' is the constructed format of Decipher-printed cards plus the pre-[[2014 Virtual Card Pool Reset|2014 reset]] virtual pool (black-diamond [[:Category:Virtual Legacy sets|Virtual Block]] cards). The [[2014 World Championship]] was the last championship-circuit event on that pool.

This is not [[Open]] (post-reset / current virtual constructed). On GEMP the matching environment code is <code>legacy</code>.

== See also ==

* [[Formats]]
* [[Open]]
* [[2014 Virtual Card Pool Reset]]
* [[:Category:Virtual Legacy sets]]
* [[List of SWCCG tournaments]]

[[Category:Formats]]
[[Category:Meta]]
"""


def file_page(label: str, extra: str = "") -> str:
    return f"""JediJer scan of 2014 World Championship decklists, posted 6 September 2014 on the Players Committee forum ([https://forum.starwarsccg.org/viewtopic.php?t=56104 t=56104]). {extra}

Used on [[2014 World Championship]].

[[Category:2014]]
"""


def redirect(target: str) -> str:
    return f"#REDIRECT [[{target}]]\n"


def add_see_source(path: Path, see: str, source: str) -> None:
    t = path.read_text(encoding="utf-8")
    see_block = ""
    if "== See also ==" in t:
        see_block = t.split("== See also ==", 1)[1].split("== ", 1)[0]
    if see not in see_block and "== See also ==" in t:
        t = t.replace("== See also ==", f"== See also ==\n\n* {see}", 1)
    if source not in t and "== Sources ==" in t:
        t = t.replace("== Sources ==", f"== Sources ==\n* {source}", 1)
    if CAT not in t:
        t = t.replace("[[Category:Players]]", f"[[Category:Players]]\n{CAT}")
    path.write_text(t, encoding="utf-8", newline="\n")


def ensure_player_stub(player: str) -> str:
    """Create a minimal person stub when none exists (Day 2 field)."""
    stub_name = player.replace(" ", "_") + ".wiki"
    path = STUBS / stub_name
    if path.exists():
        return stub_name
    lead = f"'''{player}''' played the [[{EVENT}]]."
    text = f"""{lead}

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|}}

== See also ==

* [[{EVENT}]]
* [[List of SWCCG tournaments]]
* [[Championships]]

== Sources ==

* [https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists], forum.starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
{CAT}
"""
    path.write_text(text.replace("\r\n", "\n"), encoding="utf-8", newline="\n")
    return stub_name


def inject_player(stub_name: str, rows: list[str], sources: list[str]) -> str:
    path = STUBS / stub_name
    if not path.exists():
        player = stub_name.replace(".wiki", "").replace("_", " ")
        ensure_player_stub(player)
    text = path.read_text(encoding="utf-8")
    text = inject_result_rows(text, rows, EVENT)
    path.write_text(text, encoding="utf-8", newline="\n")
    for s in sources:
        add_see_source(path, f"[[{EVENT}]]", s)
    tidy_player_page(path)
    return f"pages/player-stubs/{stub_name}"


def patch_list() -> None:
    path = PAGES / "List_of_SWCCG_tournaments.wiki"
    text = path.read_text(encoding="utf-8")
    if "== 2014 ==" in text:
        return
    block = """== 2014 ==

{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
|- 
| 2014-08-21 || [[2014 World Championship|World Championship]] || 21–24 August 2014 || Toronto, Ontario || [[Legacy Open]] || [[Emil Wallin]]
|}

"""
    text = text.replace("== Decipher World Championships ==", block + "== Decipher World Championships ==", 1)
    if "[[Category:2014]]" not in text:
        text = text.replace("[[Category:2015]]", "[[Category:2015]]\n[[Category:2014]]")
    path.write_text(text, encoding="utf-8", newline="\n")


def patch_formats() -> None:
    path = PAGES / "Formats.wiki"
    t = path.read_text(encoding="utf-8")
    if "[[Legacy Open]]" not in t:
        t = t.replace(
            "* '''Legacy''' - Decipher cards plus Legacy Virtual Cards from before the Fall 2014 reset (black-diamond virtual block icon). The 2014 World Championships was the last championship circuit to use that pool.<ref name=\"afg\" />",
            "* '''[[Legacy Open|Legacy]]''' - Decipher cards plus Legacy Virtual Cards from before the Fall 2014 reset (black-diamond virtual block icon). The [[2014 World Championship]] was the last championship circuit to use that pool.<ref name=\"afg\" />",
        )
        t = t.replace(
            "Later Players Committee events also use [[Open]], [[Jawa Format]], [[Premiere - Theed Palace]] (Decipher Cards Only), and (for the 2025 charity event) [[Premiere to Virtual Set 3]].",
            "Later Players Committee events also use [[Open]], [[Legacy Open]], [[Jawa Format]], [[Premiere - Theed Palace]] (Decipher Cards Only), and (for the 2025 charity event) [[Premiere to Virtual Set 3]].",
        )
        t = t.replace(
            "* [[Open]] &mdash; current virtual constructed environment (Decipher cards plus current Virtual Sets and Shields). Used for the [[2026 Tenth Annual GEMPC]].",
            "* [[Open]] &mdash; current virtual constructed environment (Decipher cards plus current Virtual Sets and Shields). Used for the [[2026 Tenth Annual GEMPC]].\n* [[Legacy Open]] (<code>legacy</code>) &mdash; Decipher cards plus pre-reset Virtual Block cards. Used for the [[2014 World Championship]].",
        )
        path.write_text(t, encoding="utf-8", newline="\n")


def patch_championships() -> None:
    path = PAGES / "Championships.wiki"
    t = path.read_text(encoding="utf-8")
    old = "Players Committee Worlds from 2002 on are indexed on [[List of SWCCG tournaments]] (this wiki currently has year hubs for 2025–2026)."
    new = "Players Committee Worlds from 2002 on are indexed on [[List of SWCCG tournaments]]. Year hubs on this wiki currently include [[2014 World Championship]] through [[2026 World Championship]] (gaps remain for some 2002–2013 years)."
    if old in t:
        t = t.replace(old, new)
        path.write_text(t, encoding="utf-8", newline="\n")


def patch_brian_lead() -> None:
    path = STUBS / "Brian_Terwilliger.wiki"
    t = path.read_text(encoding="utf-8")
    old = "'''Brian Terwilliger''' played the [[2020 World Championship]]."
    new = "'''Brian Terwilliger''' (Players Committee forum name '''Twigg''', also listed as Brian Twigg) played the [[2020 World Championship]] and was runner-up at the [[2014 World Championship]]."
    if old in t:
        t = t.replace(old, new)
        path.write_text(t, encoding="utf-8", newline="\n")


def patch_chris_lead() -> None:
    path = STUBS / "Chris_Terwilliger.wiki"
    t = path.read_text(encoding="utf-8")
    old = "'''Chris Terwilliger''' played in 2025 Players Committee constructed events."
    new = "'''Chris Terwilliger''' (Players Committee forum name Chris Twigg) played in 2025 Players Committee constructed events and reached the Top 8 of the [[2014 World Championship]]."
    if old in t:
        t = t.replace(old, new)
        path.write_text(t, encoding="utf-8", newline="\n")


def patch_lead_if(stub: str, old: str, new: str) -> None:
    path = STUBS / stub
    t = path.read_text(encoding="utf-8")
    if old in t:
        t = t.replace(old, new)
        path.write_text(t, encoding="utf-8", newline="\n")


def main() -> None:
    titles: list[tuple[str, str]] = []

    def add(title: str, text: str) -> None:
        titles.append((title, write(title, text)))

    # Hub written after Day 2 emit so the Day 2 table can include field rows.
    add("Legacy Open", legacy_open())
    add("2014 Worlds", redirect(EVENT))
    add("2014 World Championships", redirect(EVENT))
    add("World Championship 2014", redirect(EVENT))
    add("Brian Twigg", redirect("Brian Terwilliger"))
    add("Chris Twigg", redirect("Chris Terwilliger"))
    add("Category:2014", "Pages for 2014 events, players, and decklists.\n\n* [[List of SWCCG tournaments]]\n* [[2014 World Championship]]\n* [[Legacy Open]]\n\n[[Category:Tournaments]]\n")

    add(
        "File:2014 Worlds Day 3.pdf",
        file_page("Day 3", "Rotated 180° from the forum upload so the forms read upright. 16 pages."),
    )
    add(
        "File:2014 Worlds Day 2 Part 1.pdf",
        file_page("Day 2 Part 1", "Rotated 180° from the forum upload so the forms read upright."),
    )
    add(
        "File:2014 Worlds Day 2 Part 2.pdf",
        file_page("Day 2 Part 2", "Rotated 180° from the forum upload so the forms read upright."),
    )
    add(
        "File:2014 Worlds Day 2 Part 3.pdf",
        file_page("Day 2 Part 3", "Rotated 180° from the forum upload so the forms read upright."),
    )
    add(
        "File:2014 Worlds Chris Terwilliger Y4.pdf",
        file_page("Chris Terwilliger Y4", "Already upright in the forum upload. Chris Terwilliger Day 3 Light (deck name Y4)."),
    )
    for fn, extra in (
        (
            "File:2014 Worlds Day 3 p01 Chris Terwilliger DS Hoth (V).png",
            "Raster of page 1 (unnamed Dark 60, deck name HDv; Chris Terwilliger Imperial Occupation / Hoth (V) submitted 60).",
        ),
        (
            "File:2014 Worlds Day 3 p02 Chris Terwilliger DS.png",
            "Raster of page 2 (Chris Terwilliger Dark OUT/IN change sheet, Hoth (V)).",
        ),
        (
            "File:2014 Worlds Day 3 p03 Greg Shaw DS Hunt Down.png",
            "Raster of page 3 (Greg Shaw Dark, Hunt Down).",
        ),
        (
            "File:2014 Worlds Day 3 p04 Greg Shaw LS.png",
            "Raster of page 4 (Greg Shaw Light, It Is The Future You See / Jedi Council).",
        ),
        (
            "File:2014 Worlds Day 3 p09 Angelo Consoli DS A Stunning Move.png",
            "Raster of page 9 (Angelo Consoli Dark, A Stunning Move).",
        ),
        (
            "File:2014 Worlds Day 3 p10 Angelo Consoli LS.png",
            "Raster of page 10 (Angelo Consoli Light, We'll Handle This (V)).",
        ),
        (
            "File:2014 Worlds Day 3 p11 Aaron Kingery LS changes.png",
            "Raster of page 11 (Aaron Kingery Light Day 3 OUT/IN).",
        ),
        (
            "File:2014 Worlds Day 3 p12 Aaron Kingery DS changes.png",
            "Raster of page 12 (Aaron Kingery Dark Day 3 OUT/IN).",
        ),
        (
            "File:2014 Worlds Day 2 Part 2 p07 Aaron Kingery LS Hidden Base.png",
            "Raster of Day 2 Part 2 page 7 (Aaron Kingery Light, Pimpin' / Hidden Base).",
        ),
        (
            "File:2014 Worlds Day 2 Part 2 p08 Aaron Kingery DS Separatist Uprising.png",
            "Raster of Day 2 Part 2 page 8 (Aaron Kingery Dark, Why you hate Me? / Separatist Uprising).",
        ),
        (
            "File:2014 Worlds Day 3 p13 Brian Terwilliger DS changes.png",
            "Raster of page 13 (Brian Terwilliger Dark Day 3 OUT/IN).",
        ),
        (
            "File:2014 Worlds Day 3 p14 Brian Terwilliger LS changes.png",
            "Raster of page 14 (Brian Terwilliger Light Day 3 OUT/IN).",
        ),
        (
            "File:2014 Worlds Day 2 Part 3 p03 Brian Terwilliger LS Hidden Base.png",
            "Raster of Day 2 Part 3 page 3 (Brian Terwilliger Light, Where Did You Go? / Hidden Base), rotated 180° from the forum upload.",
        ),
        (
            "File:2014 Worlds Day 2 Part 3 p04 Brian Terwilliger DS Slavers.png",
            "Raster of Day 2 Part 3 page 4 (Brian Terwilliger Dark, Wookiee Slaving Operation), rotated 180° from the forum upload.",
        ),
        (
            "File:2014 Worlds Day 3 p15 Matt Sokol LS Quiet Mining Colony.png",
            "Raster of page 15 (Matt Sokol Light, Quiet Mining Colony).",
        ),
        (
            "File:2014 Worlds Day 3 p16 Matt Sokol DS Hunt Down.png",
            "Raster of page 16 (Matt Sokol Dark, Hunt Down).",
        ),
        (
            "File:2014 Worlds Day 3 p05 Matthew Harrison-Trainor LS.png",
            "Raster of page 5 (Matthew Harrison-Trainor Light, Communing LL).",
        ),
        (
            "File:2014 Worlds Day 3 p06 Matthew Harrison-Trainor DS.png",
            "Raster of page 6 (Matthew Harrison-Trainor Dark, Walkers).",
        ),
        (
            "File:2014 Worlds Day 3 p07 Emil Wallin LS.png",
            "Raster of page 7 (Emil Wallin Light, Mind What You Have Learned).",
        ),
        (
            "File:2014 Worlds Day 3 p08 Emil Wallin DS.png",
            "Raster of page 8 (Emil Wallin Dark, Wookiee Slaving Operation / Slavers).",
        ),
        (
            "File:2014 Worlds Chris Terwilliger Y4.png",
            "Raster of the single-page Xerox (Chris Terwilliger Light, Y4).",
        ),
        (
            "File:2014 Worlds Day 2 Part 1 p21 Greg Shaw DS Hunt Down.png",
            "Raster of Day 2 Part 1 page 21 (Greg Shaw Dark, Bonne Nuit / Hunt Down).",
        ),
        (
            "File:2014 Worlds Day 2 Part 1 p22 Greg Shaw LS Yavin 4.png",
            "Raster of Day 2 Part 1 page 22 (Greg Shaw Light, Bonne Chance / Yavin 4 Jedi Council).",
        ),
    ):
        add(fn, file_page(fn.replace("File:", ""), extra))

    emil_src = [
        f"[https://forum.starwarsccg.org/viewtopic.php?t=55902 World Champions Decklists], forum.starwarsccg.org",
        f"[https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists], forum.starwarsccg.org",
    ]
    add(
        "2014 Worlds Day 3 Emil Wallin LS Mind What You Have Learned",
        deck_page(
            "2014 Worlds Day 3 Emil Wallin LS Mind What You Have Learned",
            "Emil Wallin",
            "Light Side",
            wikilink("Mind What You Have Learned / Save You It Can (V)", "Light", True),
            "Day 3",
            type_groups(EMIL_D3_LS_GROUPS, "Light"),
            emil_src,
            extra_note="Typed onto the forum by AnakinSolo from Emil's Day 3 sheet (Holotable type groups). A numbered scan of the same Light list is page 7 of [[File:2014 Worlds Day 3.pdf]].",
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p07 Emil Wallin LS.png",
            scan_caption="Page 7 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 3 Emil Wallin DS Wookiee Slaving Operation",
        deck_page(
            "2014 Worlds Day 3 Emil Wallin DS Wookiee Slaving Operation",
            "Emil Wallin",
            "Dark Side",
            wikilink("Wookiee Slaving Operation / Indentured To The Empire", "Dark", False),
            "Day 3",
            type_groups(EMIL_D3_DS_GROUPS, "Dark"),
            emil_src,
            extra_note="Typed onto the forum by AnakinSolo. Several locations and Effects are marked starting on that post (Wookiee Slaving Operation deploy).",
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p08 Emil Wallin DS.png",
            scan_caption="Page 8 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 2 Emil Wallin DS Imperial Entanglements",
        deck_page(
            "2014 Worlds Day 2 Emil Wallin DS Imperial Entanglements",
            "Emil Wallin",
            "Dark Side",
            wikilink("Imperial Entanglements / No One To Stop Us This Time", "Dark", False),
            "Day 2",
            type_groups(EMIL_D2_DS_GROUPS, "Dark"),
            emil_src,
            extra_note="Typed onto the forum by AnakinSolo. Gogolen: Emil went 3–1 with this list. The matching Dark Xerox is page 2 of [[File:2014 Worlds Day 2 Part 3.pdf]]; Day 2 Light Xerox is page 1 of that PDF (Communing Girl Scouts).",
            files=None,
        ),
    )

    chris_note = (
        "2010 Players Committee sheet. Copies listed on separate numbered lines; "
        "ditto marks expanded to the card above. Unreadable slots are blank numbered lines. "
        "(V) follows the sheet checkbox. Deck name Y4; eltwigg (Brian Terwilliger) identified this as Chris's Day 3 Light."
    )
    add(
        "2014 Worlds Day 3 Chris Terwilliger LS There Is Good In Him",
        deck_page(
            "2014 Worlds Day 3 Chris Terwilliger LS There Is Good In Him",
            "Chris Terwilliger",
            "Light Side",
            wikilink("There Is Good In Him / I Can Save Him", "Light", False),
            "Day 3",
            numbered_deck(CHRIS_LS_RESERVE, CHRIS_LS_SHIELDS, CHRIS_LS_ADD, "Light"),
            [
                f"[https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists], forum.starwarsccg.org",
            ],
            extra_note=chris_note,
            files=["2014 Worlds Chris Terwilliger Y4.pdf"],
            scan_file="2014 Worlds Chris Terwilliger Y4.png",
            scan_caption="[[File:2014 Worlds Chris Terwilliger Y4.pdf]] (single-page Xerox).",
        ),
    )
    chris_changes = """=== Out ===
# {cyc}
# {stop}
# Darklighter Collector
# {atat}
# {nevar}
# {image}

=== In ===
# 2× {sense}
# {mara}
# {bliz}
# {gar}
# {over}
""".format(
        cyc=wikilink("Cyclone Walker", "Dark", True),
        stop=wikilink("Stop Motion", "Dark", True),
        atat=wikilink("AT-AT Deployment Platform", "Dark", True),
        nevar=wikilink("General Nevar", "Dark", False),
        image=wikilink("Image Of The Dark Lord", "Dark", True),
        sense=wikilink("Sense", "Dark", False),
        mara=wikilink("Mara Jade With Lightsaber", "Dark", False),
        bliz=wikilink("Blizzard 2", "Dark", True),
        gar=wikilink("Garindan", "Dark", True),
        over=wikilink("Overload", "Dark", False),
    )
    add(
        "2014 Worlds Day 3 Chris Terwilliger DS Hoth (V)",
        deck_page(
            "2014 Worlds Day 3 Chris Terwilliger DS Hoth (V)",
            "Chris Terwilliger",
            "Dark Side",
            wikilink("Imperial Occupation / Imperial Control", "Dark", True),
            "Day 3",
            numbered_deck(P01_DS_RESERVE, P01_DS_SHIELDS, P01_DS_ADD, "Dark"),
            [f"[https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists], forum.starwarsccg.org"],
            extra_note=(
                "2010 Players Committee sheet. Deck name HDv on page 1 of the Day 3 PDF "
                "(name field blank); that 60 is the list the page 2 change sheet modifies. "
                "Advocate wrote that Chris's Day 2 Dark was missing from the Day 2 zip "
                "([https://forum.starwarsccg.org/viewtopic.php?t=56104 t=56104]); it is not "
                "in [[File:2014 Worlds Day 2 Part 1.pdf]]–Part 3, so this Day 3 article has "
                "no Day 2 Dark scan to copy. "
                "OUT line Darklighter Collector has no matching wiki dest and no matching "
                "line in the submitted 60; OUT General Nevar (not Veers). "
                "(V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p01 Chris Terwilliger DS Hoth (V).png",
            scan_caption="Page 1 of [[File:2014 Worlds Day 3.pdf]].",
            extra_scans=[
                (
                    "2014 Worlds Day 3 p02 Chris Terwilliger DS.png",
                    "Page 2 of [[File:2014 Worlds Day 3.pdf]].",
                )
            ],
            extra_sections=[("Day 3 changes", chris_changes)],
        ),
    )

    mht_src = [f"[https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists], forum.starwarsccg.org"]
    add(
        "2014 Worlds Day 3 Matthew Harrison-Trainor LS Communing",
        deck_page(
            "2014 Worlds Day 3 Matthew Harrison-Trainor LS Communing",
            "Matthew Harrison-Trainor",
            "Light Side",
            wikilink("Communing", "Light", True),
            "Day 3",
            numbered_deck(MHT_LS_RESERVE, MHT_LS_SHIELDS, [], "Light"),
            mht_src,
            extra_note="2013 Players Committee sheet, mostly typed, name MHT, event Worlds Day 3, deck name Communing LL. Ditto marks expanded. Line 44 is Padme Naberrie (It Could Be Worse crossed out).",
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p05 Matthew Harrison-Trainor LS.png",
            scan_caption="Page 5 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 3 Matthew Harrison-Trainor DS Imperial Occupation",
        deck_page(
            "2014 Worlds Day 3 Matthew Harrison-Trainor DS Imperial Occupation",
            "Matthew Harrison-Trainor",
            "Dark Side",
            wikilink("Imperial Occupation / Imperial Control", "Dark", True),
            "Day 3",
            numbered_deck(MHT_DS_RESERVE, MHT_DS_SHIELDS, [], "Dark"),
            mht_src,
            extra_note="2013 Players Committee sheet, mostly typed, name MHT, deck name Walkers. Line 44 (Control + SFS) and line 59 (Surprise crossed out) are blank for a later read. Line 45 is I Had No Choice (Crash Landing crossed out).",
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p06 Matthew Harrison-Trainor DS.png",
            scan_caption="Page 6 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )

    pdf_src_list = [f"[https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists], forum.starwarsccg.org"]
    add(
        "2014 Worlds Day 3 Greg Shaw DS Hunt Down",
        deck_page(
            "2014 Worlds Day 3 Greg Shaw DS Hunt Down",
            "Greg Shaw",
            "Dark Side",
            wikilink("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", "Dark", True),
            "Day 3",
            numbered_deck(SHAW_DS_RESERVE, SHAW_DS_SHIELDS, [], "Dark"),
            pdf_src_list,
            extra_note=(
                "2013 Players Committee sheet. Copies listed on separate numbered lines; "
                "ditto marks expanded. (V) follows the sheet checkbox. "
                "Line 36 is written Galen's Fighter; dest is Rogue Shadow (no printed Galen's Fighter title)."
            ),
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p03 Greg Shaw DS Hunt Down.png",
            scan_caption="Page 3 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 3 Greg Shaw LS It Is The Future You See",
        deck_page(
            "2014 Worlds Day 3 Greg Shaw LS It Is The Future You See",
            "Greg Shaw",
            "Light Side",
            wikilink("It Is The Future You See", "Light", True),
            "Day 3",
            numbered_deck(SHAW_LS_RESERVE, SHAW_LS_SHIELDS, [], "Light"),
            pdf_src_list,
            extra_note=(
                "2013 Players Committee sheet. No Objective on the sheet; line 1 is "
                "Tatooine: Slave Quarters and line 2 is It Is The Future You See (V). "
                "Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p04 Greg Shaw LS.png",
            scan_caption="Page 4 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 3 Matt Sokol LS Quiet Mining Colony",
        deck_page(
            "2014 Worlds Day 3 Matt Sokol LS Quiet Mining Colony",
            "Matt Sokol",
            "Light Side",
            wikilink("Quiet Mining Colony / Independent Operation", "Light", False),
            "Day 3",
            numbered_deck(SOKOL_LS_RESERVE, SOKOL_LS_SHIELDS, [], "Light"),
            pdf_src_list,
            extra_note=(
                "2013 Players Committee sheet. Defensive Shields writes \"15 Shields\" on line 1 "
                "and leaves lines 2–15 blank; those slots are not invented. "
                "Line 9 Fuel Station and line 46 Hunt Gift (V) are unread. Line 40 Gola has no matching printed title. "
                "Day 2 was Yavin 4 / Restore Freedom (a different 60; not copied here)."
            ),
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p15 Matt Sokol LS Quiet Mining Colony.png",
            scan_caption="Page 15 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 3 Matt Sokol DS Hunt Down",
        deck_page(
            "2014 Worlds Day 3 Matt Sokol DS Hunt Down",
            "Matt Sokol",
            "Dark Side",
            wikilink("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", "Dark", False),
            "Day 3",
            numbered_deck(SOKOL_DS_RESERVE, SOKOL_DS_SHIELDS, [], "Dark"),
            pdf_src_list,
            extra_note=(
                "2013 Players Committee sheet. Defensive Shields writes \"15 Shields\" on line 1 "
                "and leaves lines 2–15 blank; those slots are not invented. "
                "(V) follows the sheet checkbox. Day 2 Dark was also Hunt Down (a different 60; not copied here)."
            ),
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p16 Matt Sokol DS Hunt Down.png",
            scan_caption="Page 16 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 3 Angelo Consoli DS A Stunning Move",
        deck_page(
            "2014 Worlds Day 3 Angelo Consoli DS A Stunning Move",
            "Angelo Consoli",
            "Dark Side",
            wikilink("A Stunning Move / A Valuable Hostage", "Dark", False),
            "Day 3",
            numbered_deck(ANGELO_DS_RESERVE, ANGELO_DS_SHIELDS, [], "Dark"),
            pdf_src_list,
            extra_note=(
                "2013 Players Committee sheet. Ditto marks expanded. (V) follows the sheet checkbox. "
                "Lines 52–53 are written Cyborg Commander and line 54 IG-Bodyguard Droid "
                "(no matching printed titles; left as written)."
            ),
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p09 Angelo Consoli DS A Stunning Move.png",
            scan_caption="Page 9 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 3 Angelo Consoli LS We'll Handle This (V)",
        deck_page(
            "2014 Worlds Day 3 Angelo Consoli LS We'll Handle This (V)",
            "Angelo Consoli",
            "Light Side",
            wikilink("We'll Handle This / Duel Of The Fates", "Light", True),
            "Day 3",
            numbered_deck(ANGELO_LS_RESERVE, ANGELO_LS_SHIELDS, [], "Light"),
            pdf_src_list,
            extra_note=(
                "2013 Players Committee sheet, deck name WHT(v). Ditto marks expanded. "
                "(V) follows the sheet checkbox. Line 47 is written Shady Jedi Combo "
                "(no matching printed combo; left as written)."
            ),
            files=["2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 3 p10 Angelo Consoli LS.png",
            scan_caption="Page 10 of [[File:2014 Worlds Day 3.pdf]].",
        ),
    )

    add(
        "2014 Worlds Day 3 Aaron Kingery LS Hidden Base",
        deck_page(
            "2014 Worlds Day 3 Aaron Kingery LS Hidden Base",
            "Aaron Kingery",
            "Light Side",
            wikilink("Hidden Base / Systems Will Slip Through Your Fingers", "Light", False),
            "Day 3",
            numbered_deck(AARON_D2_LS_RESERVE, AARON_D2_LS_SHIELDS, AARON_D2_LS_ADD, "Light"),
            pdf_src_list,
            extra_note=(
                "Day 3 is an OUT/IN change sheet on the Day 2 60 (2010 form, deck name Pimpin'). "
                "The numbered list below is that Day 2 sheet. "
                "OUT Fearlessness is not a line on the Day 2 60. "
                "Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 2.pdf", "2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 2 Part 2 p07 Aaron Kingery LS Hidden Base.png",
            scan_caption="Page 7 of [[File:2014 Worlds Day 2 Part 2.pdf]].",
            extra_scans=[
                (
                    "2014 Worlds Day 3 p11 Aaron Kingery LS changes.png",
                    "Page 11 of [[File:2014 Worlds Day 3.pdf]].",
                )
            ],
            extra_sections=[("Day 3 changes", change_section(AARON_P11, "Light"))],
        ),
    )
    add(
        "2014 Worlds Day 3 Aaron Kingery DS Separatist Uprising",
        deck_page(
            "2014 Worlds Day 3 Aaron Kingery DS Separatist Uprising",
            "Aaron Kingery",
            "Dark Side",
            wikilink("Separatist Uprising / At War With Itself", "Dark", True),
            "Day 3",
            numbered_deck(AARON_D2_DS_RESERVE, AARON_D2_DS_SHIELDS, AARON_D2_DS_ADD, "Dark"),
            pdf_src_list,
            extra_note=(
                "Day 3 is an OUT/IN change sheet on the Day 2 60 (2010 form, deck name Why you hate Me?). "
                "The numbered list below is that Day 2 sheet. "
                "OUT Walker Garrison (V) is not a line on the Day 2 60. "
                "IN MWCS is unexpanded (sheet abbreviation). "
                "Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 2.pdf", "2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 2 Part 2 p08 Aaron Kingery DS Separatist Uprising.png",
            scan_caption="Page 8 of [[File:2014 Worlds Day 2 Part 2.pdf]].",
            extra_scans=[
                (
                    "2014 Worlds Day 3 p12 Aaron Kingery DS changes.png",
                    "Page 12 of [[File:2014 Worlds Day 3.pdf]].",
                )
            ],
            extra_sections=[("Day 3 changes", change_section(AARON_P12, "Dark"))],
        ),
    )

    add(
        "2014 Worlds Day 3 Brian Terwilliger LS Hidden Base",
        deck_page(
            "2014 Worlds Day 3 Brian Terwilliger LS Hidden Base",
            "Brian Terwilliger",
            "Light Side",
            wikilink("Hidden Base / Systems Will Slip Through Your Fingers", "Light", False),
            "Day 3",
            numbered_deck(BRIAN_D2_LS_RESERVE, BRIAN_D2_LS_SHIELDS, BRIAN_D2_LS_ADD, "Light"),
            pdf_src_list,
            extra_note=(
                "Day 3 is an OUT/IN change sheet (deck name What some?) on the Day 2 60 "
                "(2010 form, deck name Where Did You Go?). The numbered list below is that Day 2 sheet. "
                "OUT Darklighter Spin and Out Of Commission are not lines on the Day 2 60. "
                "IN Escape Pod (V) is under heavy scribble and may have been voided. "
                "Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 3.pdf", "2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 2 Part 3 p03 Brian Terwilliger LS Hidden Base.png",
            scan_caption="Page 3 of [[File:2014 Worlds Day 2 Part 3.pdf]].",
            extra_scans=[
                (
                    "2014 Worlds Day 3 p14 Brian Terwilliger LS changes.png",
                    "Page 14 of [[File:2014 Worlds Day 3.pdf]].",
                )
            ],
            extra_sections=[("Day 3 changes", change_section(BRIAN_LS_P14, "Light"))],
        ),
    )
    add(
        "2014 Worlds Day 3 Brian Terwilliger DS Wookiee Slaving Operation",
        deck_page(
            "2014 Worlds Day 3 Brian Terwilliger DS Wookiee Slaving Operation",
            "Brian Terwilliger",
            "Dark Side",
            wikilink("Wookiee Slaving Operation / Indentured To The Empire", "Dark", True),
            "Day 3",
            numbered_deck(BRIAN_D2_DS_RESERVE, BRIAN_D2_DS_SHIELDS, BRIAN_D2_DS_ADD, "Dark"),
            pdf_src_list,
            extra_note=(
                "Day 3 is an OUT/IN change sheet (deck name Come get some!) on the Day 2 60. "
                "The numbered list below is that Day 2 sheet. Line 42 is unread. "
                "Forum (eltwigg) matches the OUT/IN pair; IN Garindan (V) is forum-only "
                "(Xerox box empty). Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 3.pdf", "2014 Worlds Day 3.pdf"],
            scan_file="2014 Worlds Day 2 Part 3 p04 Brian Terwilliger DS Slavers.png",
            scan_caption="Page 4 of [[File:2014 Worlds Day 2 Part 3.pdf]].",
            extra_scans=[
                (
                    "2014 Worlds Day 3 p13 Brian Terwilliger DS changes.png",
                    "Page 13 of [[File:2014 Worlds Day 3.pdf]].",
                )
            ],
            extra_sections=[("Day 3 changes", change_section(BRIAN_DS_P13, "Dark"))],
        ),
    )

    add(
        "2014 Worlds Day 2 Aaron Kingery LS Hidden Base",
        deck_page(
            "2014 Worlds Day 2 Aaron Kingery LS Hidden Base",
            "Aaron Kingery",
            "Light Side",
            wikilink("Hidden Base / Systems Will Slip Through Your Fingers", "Light", False),
            "Day 2",
            numbered_deck(AARON_D2_LS_RESERVE, AARON_D2_LS_SHIELDS, AARON_D2_LS_ADD, "Light"),
            pdf_src_list,
            extra_note=(
                "2010 Players Committee sheet, deck name Pimpin'. Same 60 as the numbered "
                "list on [[2014 Worlds Day 3 Aaron Kingery LS Hidden Base]] (Day 3 is OUT/IN). "
                "Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 2.pdf"],
            scan_file="2014 Worlds Day 2 Part 2 p07 Aaron Kingery LS Hidden Base.png",
            scan_caption="Page 7 of [[File:2014 Worlds Day 2 Part 2.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 2 Aaron Kingery DS Separatist Uprising",
        deck_page(
            "2014 Worlds Day 2 Aaron Kingery DS Separatist Uprising",
            "Aaron Kingery",
            "Dark Side",
            wikilink("Separatist Uprising / At War With Itself", "Dark", True),
            "Day 2",
            numbered_deck(AARON_D2_DS_RESERVE, AARON_D2_DS_SHIELDS, AARON_D2_DS_ADD, "Dark"),
            pdf_src_list,
            extra_note=(
                "2010 Players Committee sheet, deck name Why you hate Me?. Same 60 as the numbered "
                "list on [[2014 Worlds Day 3 Aaron Kingery DS Separatist Uprising]] (Day 3 is OUT/IN). "
                "Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 2.pdf"],
            scan_file="2014 Worlds Day 2 Part 2 p08 Aaron Kingery DS Separatist Uprising.png",
            scan_caption="Page 8 of [[File:2014 Worlds Day 2 Part 2.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 2 Brian Terwilliger LS Hidden Base",
        deck_page(
            "2014 Worlds Day 2 Brian Terwilliger LS Hidden Base",
            "Brian Terwilliger",
            "Light Side",
            wikilink("Hidden Base / Systems Will Slip Through Your Fingers", "Light", False),
            "Day 2",
            numbered_deck(BRIAN_D2_LS_RESERVE, BRIAN_D2_LS_SHIELDS, BRIAN_D2_LS_ADD, "Light"),
            pdf_src_list,
            extra_note=(
                "2010 Players Committee sheet, deck name Where Did You Go?. Same 60 as the numbered "
                "list on [[2014 Worlds Day 3 Brian Terwilliger LS Hidden Base]] (Day 3 is OUT/IN). "
                "Line 28 Chewie is crossed; Antilles Maneuver & Rebel Reinforcements (V) is kept. "
                "Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 3.pdf"],
            scan_file="2014 Worlds Day 2 Part 3 p03 Brian Terwilliger LS Hidden Base.png",
            scan_caption="Page 3 of [[File:2014 Worlds Day 2 Part 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 2 Brian Terwilliger DS Wookiee Slaving Operation",
        deck_page(
            "2014 Worlds Day 2 Brian Terwilliger DS Wookiee Slaving Operation",
            "Brian Terwilliger",
            "Dark Side",
            wikilink("Wookiee Slaving Operation / Indentured To The Empire", "Dark", True),
            "Day 2",
            numbered_deck(BRIAN_D2_DS_RESERVE, BRIAN_D2_DS_SHIELDS, BRIAN_D2_DS_ADD, "Dark"),
            pdf_src_list,
            extra_note=(
                "2010 Players Committee sheet, deck name Come get some!. Same 60 as the numbered "
                "list on [[2014 Worlds Day 3 Brian Terwilliger DS Wookiee Slaving Operation]] "
                "(Day 3 is OUT/IN). Line 42 is unread. Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 3.pdf"],
            scan_file="2014 Worlds Day 2 Part 3 p04 Brian Terwilliger DS Slavers.png",
            scan_caption="Page 4 of [[File:2014 Worlds Day 2 Part 3.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 2 Greg Shaw DS Hunt Down",
        deck_page(
            "2014 Worlds Day 2 Greg Shaw DS Hunt Down",
            "Greg Shaw",
            "Dark Side",
            wikilink("Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe", "Dark", True),
            "Day 2",
            numbered_deck(SHAW_D2_DS_RESERVE, SHAW_D2_DS_SHIELDS, SHAW_D2_DS_ADD, "Dark"),
            pdf_src_list,
            extra_note=(
                "2010 Players Committee sheet, deck name Bonne Nuit. Day 3 is a different 60 "
                "([[2014 Worlds Day 3 Greg Shaw DS Hunt Down]]). Line 35 is Rogue Shadow. "
                "Ditto marks expanded. (V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 1.pdf"],
            scan_file="2014 Worlds Day 2 Part 1 p21 Greg Shaw DS Hunt Down.png",
            scan_caption="Page 21 of [[File:2014 Worlds Day 2 Part 1.pdf]].",
        ),
    )
    add(
        "2014 Worlds Day 2 Greg Shaw LS Yavin 4",
        deck_page(
            "2014 Worlds Day 2 Greg Shaw LS Yavin 4",
            "Greg Shaw",
            "Light Side",
            wikilink("Yavin 4: Massassi Throne Room", "Light", False),
            "Day 2",
            numbered_deck(SHAW_D2_LS_RESERVE, SHAW_D2_LS_SHIELDS, SHAW_D2_LS_ADD, "Light"),
            pdf_src_list,
            extra_note=(
                "2010 Players Committee sheet, deck name Bonne Chance. No Objective on line 1 "
                "(Yavin 4: Massassi Throne Room / Jedi Council). Day 3 is a different 60 "
                "([[2014 Worlds Day 3 Greg Shaw LS It Is The Future You See]]). "
                "Line 39 is written Weapon Levitation. Line 58 Mace Windu crossed; "
                "ditto of Luke Skywalker, Jedi Knight kept. Ditto marks expanded. "
                "(V) follows the sheet checkbox."
            ),
            files=["2014 Worlds Day 2 Part 1.pdf"],
            scan_file="2014 Worlds Day 2 Part 1 p22 Greg Shaw LS Yavin 4.png",
            scan_caption="Page 22 of [[File:2014 Worlds Day 2 Part 1.pdf]].",
        ),
    )

    # Remaining Day 2 field + Top 8 leftover 60s from transcribe_*.py
    import _day2_emit  # noqa: E402

    day2_meta = _day2_emit.emit_day2(add, sys.modules[__name__])
    d2p = day2_meta["players"]

    def _d2_cell(player: str, side: str) -> str:
        slot = d2p.get(player) or {}
        if side == "Dark":
            t, h = slot.get("ds_title"), slot.get("ds_hub")
        else:
            t, h = slot.get("ls_title"), slot.get("ls_hub")
        if t:
            return f"[[{t}|{h}]]"
        return "—"

    extra_lines = []
    skip_hub = {"Emil Wallin", "Brian Terwilliger", "Aaron Kingery", "Greg Shaw"}
    for named, ds_t, ds_h, ls_t, ls_h in day2_meta["hub_rows"]:
        if named in skip_hub:
            continue
        ds = f"[[{ds_t}|{ds_h}]]" if ds_t else "—"
        ls = f"[[{ls_t}|{ls_h}]]" if ls_t else "—"
        who = "[[Unknown Player]]" if named in {"unnamed", "Unknown Player"} else f"[[{named}]]"
        extra_lines.append(f"|-\n| {who} || {ds} || {ls}\n")
    extra = "".join(extra_lines)
    add(EVENT, hub(extra))

    # Players
    forum_src = f"[https://forum.starwarsccg.org/viewtopic.php?t=55887 Day 3 pairings], forum.starwarsccg.org"
    pdf_src = f"[https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists], forum.starwarsccg.org"
    emil_d2_ls = _d2_cell("Emil Wallin", "Light")
    emil_rows = [
        "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 3) || [[Legacy Open]] || 1 || [[2014 Worlds Day 3 Emil Wallin DS Wookiee Slaving Operation|Wookiee Slaving Operation]] || [[2014 Worlds Day 3 Emil Wallin LS Mind What You Have Learned|Mind What You Have Learned]]",
        f"|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || [[2014 Worlds Day 2 Emil Wallin DS Imperial Entanglements|Imperial Entanglements]] || {emil_d2_ls}",
    ]
    titles.append((
        "Emil Wallin",
        inject_player("Emil_Wallin.wiki", emil_rows, [forum_src, f"[https://forum.starwarsccg.org/viewtopic.php?t=55902 World Champions Decklists], forum.starwarsccg.org"]),
    ))
    titles.append((
        "Brian Terwilliger",
        inject_player(
            "Brian_Terwilliger.wiki",
            [
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 3) || [[Legacy Open]] || 2 || [[2014 Worlds Day 3 Brian Terwilliger DS Wookiee Slaving Operation|Wookiee Slaving Operation]] || [[2014 Worlds Day 3 Brian Terwilliger LS Hidden Base|Hidden Base]]",
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || [[2014 Worlds Day 2 Brian Terwilliger DS Wookiee Slaving Operation|Wookiee Slaving Operation]] || [[2014 Worlds Day 2 Brian Terwilliger LS Hidden Base|Hidden Base]]",
            ],
            [forum_src, f"[https://forum.starwarsccg.org/viewtopic.php?t=55897 FINALS], forum.starwarsccg.org"],
        ),
    ))
    titles.append((
        "Chris Terwilliger",
        inject_player(
            "Chris_Terwilliger.wiki",
            [
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 3) || [[Legacy Open]] || QF || [[2014 Worlds Day 3 Chris Terwilliger DS Hoth (V)|Imperial Occupation (V)]] || [[2014 Worlds Day 3 Chris Terwilliger LS There Is Good In Him|There Is Good In Him]]",
                f"|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || — || {_d2_cell('Chris Terwilliger', 'Light')}",
            ],
            [forum_src, pdf_src],
        ),
    ))
    titles.append((
        "Matthew Harrison-Trainor",
        inject_player(
            "Matthew_Harrison-Trainor.wiki",
            [
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 3) || [[Legacy Open]] || SF || [[2014 Worlds Day 3 Matthew Harrison-Trainor DS Imperial Occupation|Imperial Occupation]] || [[2014 Worlds Day 3 Matthew Harrison-Trainor LS Communing|Communing]]",
                f"|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || {_d2_cell('Matthew Harrison-Trainor', 'Dark')} || {_d2_cell('Matthew Harrison-Trainor', 'Light')}",
            ],
            [forum_src, pdf_src],
        ),
    ))
    titles.append((
        "Greg Shaw",
        inject_player(
            "Greg_Shaw.wiki",
            [
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 3) || [[Legacy Open]] || QF || [[2014 Worlds Day 3 Greg Shaw DS Hunt Down|Hunt Down And Destroy The Jedi (V)]] || [[2014 Worlds Day 3 Greg Shaw LS It Is The Future You See|It Is The Future You See]]",
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || [[2014 Worlds Day 2 Greg Shaw DS Hunt Down|Hunt Down And Destroy The Jedi (V)]] || [[2014 Worlds Day 2 Greg Shaw LS Yavin 4|Yavin 4: Massassi Throne Room]]",
            ],
            [forum_src, pdf_src],
        ),
    ))
    titles.append((
        "Matt Sokol",
        inject_player(
            "Matt_Sokol.wiki",
            [
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 3) || [[Legacy Open]] || QF || [[2014 Worlds Day 3 Matt Sokol DS Hunt Down|Hunt Down And Destroy The Jedi]] || [[2014 Worlds Day 3 Matt Sokol LS Quiet Mining Colony|Quiet Mining Colony]]",
                f"|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || {_d2_cell('Matt Sokol', 'Dark')} || {_d2_cell('Matt Sokol', 'Light')}",
            ],
            [forum_src, pdf_src],
        ),
    ))
    titles.append((
        "Angelo Consoli",
        inject_player(
            "Angelo_Consoli.wiki",
            [
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 3) || [[Legacy Open]] || SF || [[2014 Worlds Day 3 Angelo Consoli DS A Stunning Move|A Stunning Move]] || [[2014 Worlds Day 3 Angelo Consoli LS We'll Handle This (V)|We'll Handle This (V)]]",
                f"|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || {_d2_cell('Angelo Consoli', 'Dark')} || {_d2_cell('Angelo Consoli', 'Light')}",
            ],
            [forum_src, pdf_src],
        ),
    ))
    titles.append((
        "Aaron Kingery",
        inject_player(
            "Aaron_Kingery.wiki",
            [
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 3) || [[Legacy Open]] || QF || [[2014 Worlds Day 3 Aaron Kingery DS Separatist Uprising|Separatist Uprising]] || [[2014 Worlds Day 3 Aaron Kingery LS Hidden Base|Hidden Base]]",
                "|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || [[2014 Worlds Day 2 Aaron Kingery DS Separatist Uprising|Separatist Uprising]] || [[2014 Worlds Day 2 Aaron Kingery LS Hidden Base|Hidden Base]]",
            ],
            [forum_src, pdf_src],
        ),
    ))
    patch_brian_lead()
    patch_chris_lead()
    patch_lead_if(
        "Angelo_Consoli.wiki",
        "'''Angelo Consoli''' played the [[2026 European Championship]].",
        "'''Angelo Consoli''' played the [[2026 European Championship]] and reached the Top 8 of the [[2014 World Championship]].",
    )
    patch_lead_if(
        "Matt_Sokol.wiki",
        "'''Matt Sokol''' played the [[2025 Ninth Annual GEMPC]].",
        "'''Matt Sokol''' played the [[2025 Ninth Annual GEMPC]] and reached the Top 8 of the [[2014 World Championship]].",
    )
    patch_lead_if(
        "Aaron_Kingery.wiki",
        "'''Aaron Kingery''' played the [[2022 Match Play Championship]].",
        "'''Aaron Kingery''' played the [[2022 Match Play Championship]] and reached the Top 8 of the [[2014 World Championship]].",
    )

    already_injected = {
        "Emil Wallin",
        "Brian Terwilliger",
        "Chris Terwilliger",
        "Matthew Harrison-Trainor",
        "Greg Shaw",
        "Matt Sokol",
        "Angelo Consoli",
        "Aaron Kingery",
        "unnamed",
        "Unknown Player",
    }
    for player, slot in d2p.items():
        if player in already_injected:
            continue
        stub = ensure_player_stub(player)
        ds = f"[[{slot['ds_title']}|{slot['ds_hub']}]]" if slot.get("ds_title") else "—"
        ls = f"[[{slot['ls_title']}|{slot['ls_hub']}]]" if slot.get("ls_title") else "—"
        titles.append((
            player,
            inject_player(
                stub,
                [f"|- \n| 21–24 August 2014 || [[2014 World Championship]] (Day 2) || [[Legacy Open]] || — || {ds} || {ls}"],
                [pdf_src],
            ),
        ))

    patch_list()
    patch_formats()
    patch_championships()
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    titles.append(("Formats", "pages/Formats.wiki"))
    titles.append(("Championships", "pages/Championships.wiki"))

    # TSV
    lines = []
    seen = set()
    for title, rel in titles:
        if title in seen:
            continue
        seen.add(title)
        lines.append(f"{title}\t{rel}")
    TSV.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("wrote", len(lines), "tsv rows")
    for title, rel in titles:
        print(title, "->", rel)


if __name__ == "__main__":
    main()
