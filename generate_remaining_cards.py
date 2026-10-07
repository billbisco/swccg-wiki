#!/usr/bin/env python3
"""Template:Card pages for every remaining Decipher unique-card set."""
from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_set_lists as gsl
import premiere_extras as extras

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "pages" / "remaining"
MAP_PATH = ROOT / "card_title_map.json"
DECIPHER_INDEX = "https://web.archive.org/web/20081225225012/http://www.decipher.com/starwars/cardlists/index.html"
DECIPHER_PDF = "https://web.archive.org/web/20070928014432/http://www.decipher.com/starwars/cardlists/swallcards.pdf"

SETS = [
    ("2", "A New Hope", "ANH"),
    ("3", "Hoth", "Hoth"),
    ("4", "Dagobah", "Dagobah"),
    ("5", "Cloud City", "CC"),
    ("6", "Jabba's Palace", "JP"),
    ("7", "Special Edition", "SE"),
    ("8", "Endor", "Endor"),
    ("9", "Death Star II", "DS2"),
    ("11", "Tatooine", "Tat"),
    ("12", "Coruscant", "Cor"),
    ("14", "Theed Palace", "Theed"),
    ("101", "Premiere Two-Player Introductory Game", "P2P"),
    ("102", "Jedi Pack", "Jedi"),
    ("103", "Rebel Leader Packs", "RL"),
    ("104", "The Empire Strikes Back Introductory Two-Player Game", "ESB2P"),
    ("106", "Official Tournament Sealed Deck", "OTSD"),
    ("108", "Enhanced Premiere", "EP"),
    ("109", "Enhanced Cloud City", "ECC"),
    ("110", "Enhanced Jabba's Palace", "EJP"),
    ("111", "Third Anthology", "TA"),
    ("112", "Jabba's Palace Sealed Deck", "JPSD"),
    ("10", "Reflections II: Expanding the Galaxy", "Ref2"),
    ("13", "Reflections III: A Collector's Bounty", "Ref3"),
]
SET_NAME = {sid: name for sid, name, _p in SETS}
SET_PREFIX = {sid: pref for sid, _n, pref in SETS}
SET_PREFIX["1"] = "Premiere"

CONCEPTS = {
    "Interrupt", "Used Interrupt", "Lost Interrupt", "Used or Lost Interrupt",
    "Used or Starting Interrupt", "Effect", "Utinni Effect", "Immediate Effect",
    "Political Effect", "Character", "Device", "Weapon", "Starship", "Vehicle",
    "Location", "Site", "System", "Sector", "Light", "Dark", "Rebel", "Imperial",
    "Alien", "Droid", "Used", "Lost", "Character Weapon", "Starship Weapon",
    "Automated Weapon", "Artillery Weapon", "Vehicle Weapon", "Starfighter",
    "Capital", "Transport", "Shuttle", "Squadron", "Creature Vehicle",
    "Combat Vehicle", "Creature", "Objective", "Admiral's Order", "Epic Event",
    "Jedi Test", "Podracer", "Defensive Shield", "Republic", "Sith",
    "Jedi Master", "Scavenger", "Permanent Weapon", "Pilot", "Warrior",
    "Rarity", "Premiere Limited",
}
EXPLICIT_NICKS = extras.EXPLICIT_NICKS
SKIP_ICON = {
    "A New Hope", "Hoth", "Dagobah", "Cloud City", "Jabba's Palace",
    "Special Edition", "Endor", "Death Star II", "Tatooine", "Coruscant",
    "Theed Palace", "Premiere", "Reflections II", "Reflections III",
    "Episode I", "Premium", "Enhanced Premiere", "Enhanced Cloud City",
    "Enhanced Jabba's Palace",
}
RARITY_LINK = {
    "C": "Rarity#Common",
    "U": "Rarity#Uncommon",
    "R": "Rarity#Rare",
    "F": "Rarity#Fixed",
    "P": "Rarity#Premium",
    "X": "Rarity#Exclusive",
}
WEAPON_SUB = {
    "Character": ("Character", "Character Weapon"),
    "Starship": ("Starship", "Starship Weapon"),
    "Automated": ("Automated", "Automated Weapon"),
    "Artillery": ("Artillery", "Artillery Weapon"),
    "Vehicle": ("Vehicle", "Vehicle Weapon"),
}
INTERRUPT_SUB = {
    "Used": ("Used Interrupt", "Used Interrupt"),
    "Lost": ("Lost Interrupt", "Lost Interrupt"),
    "Used Or Lost": ("Used or Lost Interrupt", "Used or Lost Interrupt"),
    "Used Or Starting": ("Used or Starting Interrupt", "Used or Starting Interrupt"),
}
EFFECT_SUB = {
    "Utinni": ("Utinni Effect", "Utinni Effect"),
    "Immediate": ("Immediate Effect", "Immediate Effect"),
    "Political": ("Political Effect", "Political Effect"),
}
CREATURE_HABITAT = {
    "Swamp", "Snow", "Desert", "Forest", "Jungle", "Cave", "Space",
    "Underwater", "Mountain", "Gas",
}


def printed(c: dict) -> str:
    t = ((c.get("front") or {}).get("title") or "")
    return re.sub(r"^[•*<>]+", "", t).strip()


def tpl_escape(s: str) -> str:
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("|", "{{!}}")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def uniqueness(raw) -> str:
    if raw in (None, "", "None"):
        return "Unrestricted"
    if raw == "*":
        return "Unique"
    if raw == "**":
        return "Restricted (••)"
    if raw == "***":
        return "Restricted (•••)"
    if raw == "<>":
        return "Independent (<>)"
    return str(raw)


def rarity_link(r: str) -> str:
    if not r:
        return "Rarity"
    return RARITY_LINK.get(r[0], "Rarity")


def split_model(sub: str) -> tuple[str, str]:
    if ": " in sub:
        return sub.split(": ", 1)
    return sub, ""


def subtype_fields(typ: str, sub: str) -> tuple[str, str, str]:
    """visible subtype, subtype_link, model."""
    sub = (sub or "").strip()
    if typ == "Weapon":
        label, page = WEAPON_SUB.get(sub, (sub, "Weapon"))
        return label, page, ""
    if typ == "Interrupt":
        label, page = INTERRUPT_SUB.get(sub, (sub, "Interrupt"))
        return label, page, ""
    if typ == "Effect":
        label, page = EFFECT_SUB.get(sub, (sub, "Effect"))
        return label, page, ""
    if typ == "Vehicle":
        kind, model = split_model(sub)
        if kind == "Creature":
            return "Creature", "Creature Vehicle", model
        if kind == "Combat":
            return "Combat", "Combat Vehicle", model
        if kind == "Shuttle":
            return "Shuttle", "Shuttle", model
        if kind == "Transport":
            return "Transport", "Transport", model
        return kind, kind or "Vehicle", model
    if typ == "Starship":
        kind, model = split_model(sub)
        if kind == "Starfighter":
            return "Starfighter", "Starfighter", model
        if kind == "Capital":
            return "Capital", "Capital", model
        if kind == "Squadron":
            return "Squadron", "Squadron", model
        if kind == "Shuttle":
            return "Shuttle", "Shuttle", model
        return kind, kind or "Starship", model
    if typ == "Location":
        if sub == "System":
            return "System", "System", ""
        if sub == "Sector":
            return "Sector", "Sector", ""
        if sub:
            return sub, "Site", ""
        return "Site", "Site", ""
    if typ == "Creature":
        if sub in CREATURE_HABITAT:
            return sub, "Creature", ""
        return sub, sub or "Creature", ""
    if typ.startswith("Jedi Test"):
        return typ, "Jedi Test", ""
    if typ == "Character":
        if "/" in sub:
            return sub, sub.split("/")[0].strip(), ""
        return sub, sub, ""
    return sub, sub, ""


def icon_link(raw: str) -> str:
    m = re.match(r"^(.*?)(?:\s*[x×]\s*(\d+))?$", raw.strip(), re.I)
    name = (m.group(1) if m else raw).strip()
    count = int(m.group(2)) if m and m.group(2) else 1
    if name.lower() == "permanent weapon":
        name = "Permanent Weapon"
    if count > 1:
        return f"[[{name}]] ×{count}"
    return f"[[{name}]]"


def icons_row(front: dict, typ: str) -> tuple[str, str, str]:
    raw = [i for i in (front.get("icons") or []) if i not in SKIP_ICON]
    if typ == "Location":
        shared = " ".join(icon_link(i) for i in raw)
        d_n = front.get("darkSideIcons")
        l_n = front.get("lightSideIcons")
        dark = []
        light = []
        if d_n:
            dark.append(f"[[Dark Force]] ×{d_n}" if int(d_n) > 1 else "[[Dark Force]]")
        if l_n:
            light.append(f"[[Light Force]] ×{l_n}" if int(l_n) > 1 else "[[Light Force]]")
        if shared:
            dark.append(shared)
            light.append(shared)
        return "", " ".join(dark), " ".join(light)
    return " ".join(icon_link(i) for i in raw), "", ""


def wiki_file_url(c: dict, url: str) -> str:
    stem = url.split("/")[-1].split("?")[0]
    letter = "L" if c.get("side") == "Light" else "D"
    sid = str(c.get("set"))
    pref = SET_PREFIX.get(sid, "X")
    if sid == "1":
        return f"Premiere-{letter}-{stem}"
    # Legacy Virtual Block / Shields crops were imported as *-pre.gif.
    if (pref.startswith("VB") or pref == "VSh") and stem.endswith(".gif") and not stem.endswith("-pre.gif"):
        stem = stem[:-4] + "-pre.gif"
    return f"{pref}-{letter}-{stem}"


def wiki_file(c: dict) -> str:
    front = c.get("front") or {}
    return wiki_file_url(c, front.get("imageUrl") or "")


def location_text(gametext: str) -> str:
    text = gametext or ""
    light, dark = "", ""
    if "Light:" in text and "Dark:" in text:
        if text.strip().startswith("Light:"):
            a, b = text.split("Dark:", 1)
            light = a.replace("Light:", "", 1).strip()
            dark = b.strip()
        else:
            a, b = text.split("Light:", 1)
            dark = a.replace("Dark:", "", 1).strip()
            light = b.strip()
        parts = []
        if light:
            parts.append("'''Light Side:''' " + tpl_escape(light))
        if dark:
            parts.append("'''Dark Side:''' " + tpl_escape(dark))
        return "\n\n".join(parts)
    return tpl_escape(text)


def objective_text(title: str, gametext: str) -> str:
    sides = gsl.split_objective_sides(title, gametext or "")
    parts = []
    labels = ("0 side", "7 side")
    for i, (name, text) in enumerate(sides):
        lab = labels[i] if i < 2 else f"side {i}"
        body = tpl_escape(text)
        if body:
            parts.append(f"'''{lab} — {name}'''\n\n{body}")
        else:
            parts.append(f"'''{lab} — {name}'''")
    return "\n\n".join(parts)


def safe_game_text(text: str) -> str:
    if not text:
        return ""
    if text.startswith(("*", "#", ":", ";")):
        return "<nowiki>" + text[0] + "</nowiki>" + text[1:]
    return text


def seed_occupied() -> set[str]:
    occ = set(CONCEPTS)
    for folder in (
        ROOT / "pages" / "ls-chars",
        ROOT / "pages" / "ls-rest",
        ROOT / "pages" / "ds-cards",
    ):
        for name in ("index.tsv", "aliases.tsv"):
            p = folder / name
            if not p.exists():
                continue
            for line in p.read_text(encoding="utf-8").splitlines():
                if not line.strip():
                    continue
                parts = line.split("\t")
                if name == "index.tsv" and len(parts) >= 2:
                    occ.add(parts[1])
                elif name == "aliases.tsv" and len(parts) >= 1:
                    occ.add(parts[0])
    occ.add("2X-3KPR (Tooex)")
    occ.add("Tooex")
    occ.add("2X-3KPR")
    occ.add("C-3PO")
    occ.add("See-Threepio")
    occ.update(EXPLICIT_NICKS.keys())
    occ.update(SET_NAME.values())
    return occ


def assign_titles(cards: list[dict]) -> dict[str, str]:
    """gempId -> wiki title. Also writes card_title_map.json keys set|side|printed."""
    occ = seed_occupied()
    prem_light = set()
    prem_dark = set()
    key_to_page = {}
    for folder, side in (
        (ROOT / "pages" / "ls-chars", "Light"),
        (ROOT / "pages" / "ls-rest", "Light"),
        (ROOT / "pages" / "ds-cards", "Dark"),
    ):
        p = folder / "index.tsv"
        if not p.exists():
            continue
        for line in p.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            _uid, title, _fn = line.split("\t")
            printed_name = title.replace(" (Dark)", "") if side == "Dark" and title.endswith(" (Dark)") else title
            key_to_page[f"1|{side}|{printed_name}"] = title
            if side == "Light":
                prem_light.add(title)
            else:
                prem_dark.add(title)
    gid_to_page = {}
    by_set = defaultdict(list)
    for c in cards:
        by_set[str(c.get("set"))].append(c)
    for sid, _name, _pref in SETS:
        bucket = by_set.get(sid) or []
        bucket.sort(key=lambda c: (0 if c.get("side") == "Light" else 1, printed(c).lower()))
        for c in bucket:
            t = printed(c)
            side = c.get("side") or "Light"
            gid = c.get("gempId") or ""
            typ = (c.get("front") or {}).get("type") or ""
            page = t
            if t in EXPLICIT_NICKS and EXPLICIT_NICKS.get(t) != t:
                page = f"{t} ({SET_NAME[sid]})"
            elif t in occ:
                if side == "Dark":
                    cand = f"{t} (Dark)"
                    if cand not in occ:
                        page = cand
                    else:
                        page = f"{t} (Dark) ({SET_NAME[sid]})"
                        if page in occ:
                            page = f"{t} ({SET_NAME[sid]})"
                elif typ == "Location" and t in SET_NAME.values():
                    page = f"{t} (location)"
                else:
                    page = f"{t} ({SET_NAME[sid]})"
            n = 2
            base = page
            while page in occ:
                page = f"{base} ({n})"
                n += 1
            occ.add(page)
            if gid:
                gid_to_page[gid] = page
            key_to_page[f"{sid}|{side}|{t}"] = page
    MAP_PATH.write_text(json.dumps(key_to_page, indent=0, ensure_ascii=False), encoding="utf-8")
    return gid_to_page


def hatnote_for(c: dict, page: str, dests: dict) -> str:
    t = printed(c)
    side = c.get("side")
    sid = str(c.get("set"))
    notes = []
    other = "Dark" if side == "Light" else "Light"
    other_page = dests.get(f"{sid}|{other}|{t}")
    if other_page:
        notes.append(f"For the {other} Side card, see [[{other_page}]].")
    prem = dests.get(f"1|{side}|{t}")
    if prem and page != prem:
        notes.append(f"For the Premiere card, see [[{prem}]].")
    return " ".join(notes)


def page_for(
    c: dict,
    page: str,
    prev: str,
    nxt: str,
    dests: dict,
    *,
    set_band: str = "Decipher",
    sources: str | None = None,
    hatnote: str | None = None,
    version_label: str = "printed",
) -> str:
    front = c.get("front") or {}
    t = printed(c)
    sid = str(c.get("set"))
    set_name = SET_NAME[sid]
    side = c.get("side") or "Light"
    typ = front.get("type") or "Card"
    if typ.startswith("Jedi Test"):
        typ_label = "Jedi Test"
    else:
        typ_label = typ
    sub_raw = front.get("subType") or ""
    subtype, subtype_link, model = subtype_fields(typ, sub_raw)
    gtext_raw = front.get("gametext") or ""
    if typ == "Location":
        gtext = location_text(gtext_raw)
    elif typ == "Objective":
        gtext = objective_text(t, gtext_raw)
    else:
        gtext = safe_game_text(tpl_escape(gtext_raw))
    icons, dark_icons, light_icons = icons_row(front, typ)
    lore = tpl_escape(front.get("lore") or "")
    uid = c.get("gempId") or ""
    r = c.get("rarity") or ""
    if sources is None:
        sources = (
            f"* [{DECIPHER_INDEX} Star Wars CCG cardlists index] at Decipher.com (archive, 25 December 2008)\n"
            f"* [{DECIPHER_PDF} Complete Card List] (Decipher PDF, archive 28 September 2007) — {side} {typ_label}: {t}, {set_name}, {r}"
        )
    printings = f"'''{set_name}''' — this page"
    back = c.get("back") or {}
    image2 = ""
    if typ == "Objective" and back.get("imageUrl"):
        image2 = wiki_file_url(c, back["imageUrl"])
    fields = {
        "title": t,
        "card_uid": uid,
        "image": wiki_file(c),
        "image2": image2,
        "image2_layout": "responsive" if image2 else "",
        "side": side,
        "type": typ_label,
        "subtype": subtype,
        "subtype_link": subtype_link,
        "model": model,
        "set": set_name,
        "rarity": r,
        "rarity_link": rarity_link(r),
        "uniqueness": uniqueness(front.get("uniqueness")),
        "destiny": front.get("destiny") or "",
        "power": front.get("power") or "",
        "ability": front.get("ability") or "",
        "deploy": front.get("deploy") or "",
        "forfeit": front.get("forfeit") or "",
        "armor": front.get("armor") or "",
        "maneuver": front.get("maneuver") or "",
        "hyperspeed": front.get("hyperspeed") or "",
        "landspeed": front.get("landspeed") or "",
        "icons": icons,
        "dark_icons": dark_icons,
        "light_icons": light_icons,
        "version_label": version_label,
        "set_band": set_band,
        "prev": prev,
        "next": nxt,
        "lore": lore,
        "game_text": gtext,
        "printings": printings,
        "see_also": "",
        "sources": sources,
        "hatnote": hatnote if hatnote is not None else hatnote_for(c, page, dests),
    }
    try:
        fields.update(extras.extras_fields(uid))
    except Exception:
        pass
    skip_empty = {
        "model", "prev", "next", "deploy", "notes", "game_text_note",
        "power", "ability", "forfeit", "armor", "maneuver", "hyperspeed",
        "landspeed", "icons", "dark_icons", "light_icons", "subtype",
        "subtype_link", "see_also", "lore", "hatnote", "strategy", "combos",
        "image2", "image2_layout",
        "rulings", "pulled_by", "pulls", "canceled_by", "cancels", "matching",
        "matching_weapon", "also_known_as", "personas", "characteristics",
        "counterpart", "underlying_card_for", "has_refs",
    }
    lines = ["{{Card"]
    for k, v in fields.items():
        if v in ("", None) and k in skip_empty:
            continue
        lines.append(f"|{k}={v}")
    lines.append("}}")
    return "\n".join(lines) + "\n"


def aliases_for(printed_title: str) -> list[str]:
    out = []
    m = re.match(r"^(.+?) \((.+)\)$", printed_title)
    if m:
        head, inner = m.group(1).strip(), m.group(2).strip()
        if inner not in ("V", "AI", "Dark", "Light", "EP1") and len(inner) > 1:
            out.append(inner)
        if head and len(head) > 1:
            out.append(head)
    m2 = re.match(r"^([A-Z0-9]+(?:-[A-Z0-9]+)+) ", printed_title)
    if m2:
        head = m2.group(1)
        if head not in out:
            out.append(head)
    return out


def load_cards() -> list[dict]:
    wanted = {sid for sid, _n, _p in SETS}
    out = []
    for side in ("Light", "Dark"):
        data = json.loads((ROOT / f"scomp-{side}.json").read_text(encoding="utf-8"))
        cards = data["cards"] if isinstance(data, dict) else data
        for c in cards:
            if str(c.get("set")) not in wanted:
                continue
            t = printed(c)
            if not t or "(V)" in t or "(AI)" in t:
                continue
            typ = (c.get("front") or {}).get("type") or ""
            if typ == "Game Aid":
                continue
            out.append(c)
    return out


def write_xml(pages: list[tuple[str, str]], dest: Path | None = None) -> None:
    parts = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/" version="0.11" xml:lang="en">',
    ]
    for title, text in pages:
        parts.append("<page>")
        parts.append(f"<title>{xml_escape(title)}</title>")
        parts.append("<ns>0</ns>")
        parts.append("<revision>")
        parts.append(f'<text xml:space="preserve">{xml_escape(text)}</text>')
        parts.append("</revision>")
        parts.append("</page>")
    parts.append("</mediawiki>")
    path = dest or (ROOT / "remaining-cards.xml")
    path.write_text("\n".join(parts), encoding="utf-8")


def load_remaining_index() -> dict[str, tuple[str, str, str, str]]:
    """gempId -> (page, fn, side, sid) from the last remaining import."""
    out = {}
    p = OUT / "index.tsv"
    if not p.exists():
        return out
    for line in p.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        gid, page, fn, side, sid = line.split("\t")
        out[gid] = (page, fn, side, sid)
    return out


def main():
    starred_only = "--starred-only" in sys.argv
    cards = load_cards()
    print("cards", len(cards))
    extras._CACHE = None
    extras._LINKER = None
    extras._STAR_CACHE = None
    OUT.mkdir(parents=True, exist_ok=True)
    by_set_side = defaultdict(list)
    for c in cards:
        by_set_side[(str(c.get("set")), c.get("side"))].append(c)
    for key in by_set_side:
        by_set_side[key].sort(key=lambda c: printed(c).lower())
    written = []
    xml_pages = []
    if starred_only:
        sm = extras.starred_map()
        wanted = {
            gid
            for gid, v in sm.items()
            if v.get("has_html") and str(v.get("set")) != "1"
        }
        index = load_remaining_index()
        dests = json.loads(MAP_PATH.read_text(encoding="utf-8"))
        gid_pages = {gid: page for gid, (page, _fn, _side, _sid) in index.items()}
        print("starred remaining", len(wanted), flush=True)
        xml_dest = ROOT / "strategy-remaining.xml"
    else:
        wanted = None
        gid_pages = assign_titles(cards)
        dests = json.loads(MAP_PATH.read_text(encoding="utf-8"))
        xml_dest = ROOT / "remaining-cards.xml"
        occ_alias = seed_occupied() | set(gid_pages.values())
        alias_rows = []
    for sid, _n, _p in SETS:
        for side in ("Light", "Dark"):
            group = by_set_side.get((sid, side)) or []
            titles = [gid_pages.get(c.get("gempId") or "", printed(c)) for c in group]
            for i, c in enumerate(group):
                gid = c.get("gempId") or ""
                if wanted is not None and gid not in wanted:
                    continue
                page = gid_pages.get(gid, printed(c))
                prev = titles[i - 1] if i else ""
                nxt = titles[i + 1] if i + 1 < len(titles) else ""
                text = page_for(c, page, prev, nxt, dests)
                fn = f"{gid}.wiki".replace("/", "_")
                path = OUT / fn
                path.write_text(text, encoding="utf-8")
                written.append((page, gid, fn, printed(c), side, sid))
                xml_pages.append((page, text))
                if wanted is None:
                    xml_pages.append((f"Card:{gid}", f"#REDIRECT [[{page}]]\n"))
                    for alias in aliases_for(printed(c)):
                        if alias and alias not in occ_alias:
                            alias_rows.append((alias, page))
                            occ_alias.add(alias)
                            xml_pages.append((alias, f"#REDIRECT [[{page}]]\n"))
    if wanted is None:
        (OUT / "index.tsv").write_text(
            "\n".join(f"{gid}\t{page}\t{fn}\t{side}\t{sid}" for page, gid, fn, _t, side, sid in written) + "\n",
            encoding="utf-8",
        )
        (OUT / "aliases.tsv").write_text(
            "\n".join(f"{a}\t{d}" for a, d in alias_rows) + "\n",
            encoding="utf-8",
        )
    write_xml(xml_pages, xml_dest)
    print("wrote", len(written), "pages")
    print("xml", xml_dest, xml_dest.stat().st_size)
    dis = sum(1 for page, _g, _f, t, _s, _sid in written if page != t)
    print("disambiguated", dis)


if __name__ == "__main__":
    main()
