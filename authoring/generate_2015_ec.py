#!/usr/bin/env python3
"""2015 European Championship leftover Xerox (Open / current virtual dests).

Fills wrap dest titles with Xerox 60s. Does not rewrite the wrap hub or List.

python generate_2015_ec.py --xerox
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
from _xerox_delta import write_delta_tsv  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
TSV = ROOT / "y2015-ec-xerox-titles.tsv"
DELTA = ROOT / "y2015-ec-xerox-delta.tsv"
APPLIED = ROOT / "y2015-ec-xerox-applied.tsv"
EVENTS_DIR = ROOT / "encyclopedia" / "pc-2015-events"

EVENT = "2015 European Championship"
DATES = "16–18 October 2015"
TAG = "2015"
FORMAT = "[[Open]]"
PC_PDF_P1 = "https://res.starwarsccg.org/wp/wp-content/uploads/SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf"
PC_PDF_P18 = "https://res.starwarsccg.org/wp/wp-content/uploads/SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf"
PC_WRAP = "https://www.starwarsccg.org/2015-european-championships/"
PC_TDL = "https://www.starwarsccg.org/resources/tournament-decklists/"
SITE = "Bochum, Germany"
WINNER = "Ziemowit Skwara"

g15.CANON.update(
    {
        "Joe Olson": "Joe Olson",
        "Olson, Joe": "Joe Olson",
    }
)

DISPLAY = {}


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


def _open_index() -> dict[str, dict[tuple[str, str], str]]:
    """Current-virtual Open pools. Never Virtual Block."""
    cur: dict[tuple[str, str], str] = {}
    dec: dict[tuple[str, str], str] = {}
    sh: dict[tuple[str, str], str] = {}
    for k, dest in w14.MAP.items():
        parts = k.split("|", 2)
        if len(parts) < 3:
            continue
        sid, side, name = parts
        key = (side, w14._norm(name).lower())
        if sid.startswith("vb"):
            continue
        if sid in ("vsh", "setd"):
            sh[key] = dest
        elif sid.isdigit() and int(sid) >= 200:
            cur[key] = dest
        elif sid in w14.DECIPHER_SETS:
            dec.setdefault(key, dest)
        elif sid.isdigit() and 15 <= int(sid) <= 199:
            cur.setdefault(key, dest)
    return {"cur": cur, "dec": dec, "sh": sh}


OPEN_IDX = _open_index()


def open_lookup(name: str, side: str, is_v: bool, prefer_sh: bool = False) -> str | None:
    keys = [(side, v.lower()) for v in w14._name_variants(name)]
    virt = ("sh", "cur") if prefer_sh else ("cur", "sh")

    def search(pool_names: tuple[str, ...]) -> str | None:
        for pool in pool_names:
            for k in keys:
                if k in OPEN_IDX[pool]:
                    return OPEN_IDX[pool][k]
            for v in w14._name_variants(name):
                hit = w14._prefix_in_pool(OPEN_IDX[pool], side, v)
                if hit:
                    return hit
            for v in w14._name_variants(name):
                hit = w14._close_in_pool(OPEN_IDX[pool], side, v)
                if hit:
                    return hit
        return None

    if is_v or prefer_sh:
        return search(virt) or search(("dec",))
    return search(("dec",)) or search(virt)


def install_open_lookup() -> None:
    w14._lookup = open_lookup  # type: ignore[assignment]


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
        f"[{PC_PDF_P1} Place 1-17 PDF], res.starwarsccg.org",
        f"[{PC_PDF_P18} Place 18-35 PDF], res.starwarsccg.org",
        f"[{PC_WRAP} 2015 European Championship], starwarsccg.org",
        f"[{PC_TDL} Tournament Decklists], starwarsccg.org",
    ]
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2015]]"
    page_txt = w14.deck_page(
        title,
        display,
        "Light Side" if side == "Light" else "Dark Side",
        start_link,
        stage or "European Championship",
        body,
        sources,
        extra_note=w14.extra_note_for(mod, side),
        scan_file=scan,
        scan_caption=f"Page {page} of [[:File:{mod.PDF}]].",
        username=w14.username_for(mod, side),
        player_page=player if player != display else None,
    )
    page_txt = page_txt.replace("* '''Format:''' [[Legacy Open]]", f"* '''Format:''' {FORMAT}")
    return title, write(title, page_txt), label, stage


def leftover_xerox() -> None:
    STUBS.mkdir(parents=True, exist_ok=True)
    _by_id, by_title = load_bp_simple()
    mpc.load_wiki_types()
    mpc.TYPE_OVERRIDE.update(
        {
            "tatooine (theed palace)": "Location",
            "ominous rumblings": "Effect",
            "ability, ability, ability": "Effect",
            "knowledge and defense": "Effect",
            "something special planned for them": "Effect",
            "according to my design": "Interrupt",
            "short-range fighters & watch your back": "Interrupt",
            "sfs l-s9.3 laser cannons": "Weapon",
            "we'll let fate decide, huh?": "Defensive Shield",
            "come here you big coward": "Defensive Shield",
            "houjix": "Interrupt",
            "goldenrod": "Defensive Shield",
            "the republic no longer functions": "Defensive Shield",
            "your ship?": "Defensive Shield",
            "vote of no confidence": "Defensive Shield",
            "imperial detention": "Defensive Shield",
            "fighters coming in": "Admiral's Order",
            "i'll take the leader": "Admiral's Order",
            "ounee ta": "Effect",
            "tatooine celebration": "Effect",
            "wesa gotta grand army": "Interrupt",
            "were you looking for me?": "Interrupt",
            "mindful of the future": "Interrupt",
            "sorry about the mess & blaster proficiency": "Interrupt",
            "control & tunnel vision": "Interrupt",
            "free ride & endor celebration": "Interrupt",
            "all wings report in & darklighter spin": "Interrupt",
            "threepio with his parts showing": "Character",
            "luke skywalker, jedi knight": "Character",
            "booster in pulsar skate": "Starship",
            "obi-wan's journal": "Device",
            "naboo: boss nass' chambers": "Location",
            "endor: landing platform": "Location",
            "dr. evazan & ponda baba": "Character",
            "mara jade with lightsaber": "Character",
            "darth maul with lightsaber": "Character",
            "stormtrooper garrison": "Effect",
            "janus greejatus": "Character",
            "major turr phennir": "Character",
            "baron soontir fel": "Character",
            "maul's sith infiltrator": "Starship",
            "saber 1": "Starship",
            "saber 2": "Starship",
            "black 2": "Starship",
            "blizzard 4": "Vehicle",
            "masterful move & endor occupation": "Effect",
            "all power to weapons": "Interrupt",
            "i have you now": "Interrupt",
            "establish control": "Effect",
            "combat response": "Effect",
            "endor shield": "Effect",
            "imperial decree": "Effect",
            "force push": "Interrupt",
            "close call": "Interrupt",
            "a useless gesture": "Defensive Shield",
            "fanfare": "Defensive Shield",
            "firepower": "Defensive Shield",
            "you cannot hide forever": "Defensive Shield",
            "death star sentry": "Defensive Shield",
            "do they have a code clearance?": "Defensive Shield",
            "jabba's prize": "Defensive Shield",
            "yavin sentry": "Defensive Shield",
            "your insight serves you well": "Defensive Shield",
            "don't do that again": "Defensive Shield",
            "weapons display": "Defensive Shield",
            "only jedi carry that weapon": "Defensive Shield",
            "he can go about his business": "Defensive Shield",
            "a tragedy has occurred": "Defensive Shield",
            "simple tricks and nonsense": "Defensive Shield",
            "there is no try": "Defensive Shield",
            "resistance": "Defensive Shield",
            "secret plans": "Defensive Shield",
            "allegations of corruption": "Defensive Shield",
            "battle order": "Defensive Shield",
            "aim high": "Defensive Shield",
            "battle plan": "Defensive Shield",
            "ultimatum": "Defensive Shield",
        }
    )
    install_open_lookup()
    w14.EVENT = EVENT
    w14.CAT = "[[Category:2015]]"
    titles: list[tuple[str, str]] = []
    xerox_dt, xerox_hl = {}, {}
    xerox_players: list[str] = []
    mods = []
    for path in sorted(EVENTS_DIR.glob("transcribe_2015_ec_*.py")):
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

    # Wrap dest already injected Day 2 / Day 3 rows. inject_result_rows
    # strips every [[2015 European Championship]] row, so skip upsert here.

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
    write_delta_tsv(ordered, APPLIED, DELTA, set())


if __name__ == "__main__":
    leftover_xerox()
