#!/usr/bin/env python3
"""DS2 starter decks, Enhanced pack variants, First/Second Anthology thumbs."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

import generate_set_lists as gsl

ROOT = Path(__file__).resolve().parent
SETN = {
    "1": "Premiere",
    "2": "A New Hope",
    "3": "Hoth",
    "4": "Dagobah",
    "5": "Cloud City",
    "6": "Jabba's Palace",
    "7": "Special Edition",
    "8": "Endor",
    "9": "Death Star II",
}
PREFIX = {
    "1": "Premiere",
    "2": "ANH",
    "3": "Hoth",
    "4": "Dagobah",
    "5": "CC",
    "6": "JP",
    "7": "SE",
    "8": "Endor",
    "9": "DS2",
}
TYPE_PAGE = {
    "Character": "Character",
    "Creature": "Creature",
    "Device": "Device",
    "Effect": "Effect",
    "Interrupt": "Interrupt",
    "Location": "Location",
    "Starship": "Starship",
    "Vehicle": "Vehicle",
    "Weapon": "Weapon",
    "Objective": "Objective",
    "Epic Event": "Epic Event",
    "Admiral's Order": "Admiral's Order",
}
TYPE_ORDER = [
    "Character",
    "Creature",
    "Device",
    "Effect",
    "Interrupt",
    "Location",
    "Starship",
    "Vehicle",
    "Weapon",
    "Admiral's Order",
]

DS_STARTER = [
    ("Admiral Piett", 1),
    ("Captain Jonus", 1),
    ("Corporal Drazin", 1),
    ("DS-181-3", 1),
    ("DS-181-4", 1),
    ("Elite Squadron Stormtrooper", 3),
    ("Lieutenant Arnet", 1),
    ("Lieutenant Grond", 1),
    ("Lieutenant Hebsly", 1),
    ("Reserve Pilot", 1),
    ("Sergeant Tarl", 1),
    ("Battle Order", 1),
    ("Combat Response", 1),
    ("Inconsequential Losses", 1),
    ("Combat Readiness", 1),
    ("Dark Maneuvers", 2),
    ("Flawless Marksmanship", 1),
    ("Ghhhk", 1),
    ("Imperial Reinforcements", 1),
    ("Monnok", 2),
    ("Prepared Defenses", 1),
    ("Endor", 1),
    ("Endor: Ancient Forest", 1),
    ("Endor: Back Door", 1),
    ("Endor: Great Forest", 1),
    ("Endor: Landing Platform (Docking Bay)", 1),
    ("Kessel", 1),
    ("Mon Calamari", 1),
    ("Sullust", 1),
    ("Black 3", 1),
    ("Saber 3", 1),
    ("Saber 4", 1),
    ("Scimitar 2", 1),
    ("Scythe 3", 1),
    ("Scythe Squadron TIE", 2),
    ("TIE Defender Mark I", 3),
    ("TIE Interceptor", 3),
    ("Victory-Class Star Destroyer", 3),
    ("Tempest 1", 1),
    ("Tempest Scout", 2),
    ("Tempest Scout 3", 1),
    ("Blaster Rifle", 2),
    ("Concussion Missiles", 1),
    ("Enhanced TIE Laser Cannon", 1),
    ("Intruder Missile", 2),
    ("SFS L-s7.2 TIE Cannon", 1),
]
LS_STARTER = [
    ("Admiral Ackbar", 1),
    ("Captain Yutani", 1),
    ("Chewbacca Of Kashyyyk", 1),
    ("Corporal Beezer", 1),
    ("Corporal Delevar", 1),
    ("Corporal Janse", 1),
    ("Corporal Midge", 1),
    ("Derek 'Hobbie' Klivian", 1),
    ("Dresselian Commando", 2),
    ("General Solo", 1),
    ("Gray Squadron Y-wing Pilot", 2),
    ("Karie Neth", 1),
    ("Keir Santage", 1),
    ("Kin Kian", 1),
    ("Sergeant Junkin", 1),
    ("Battle Plan", 1),
    ("Squadron Assignments", 1),
    ("Superficial Damage", 1),
    ("A Few Maneuvers", 2),
    ("Careful Planning", 1),
    ("Grimtaash", 2),
    ("Heading For The Medical Frigate", 1),
    ("Houjix", 1),
    ("Steady Aim", 1),
    ("Take The Initiative", 1),
    ("Bespin", 1),
    ("Endor", 1),
    ("Endor: Back Door", 1),
    ("Endor: Great Forest", 1),
    ("Endor: Hidden Forest Trail", 1),
    ("Endor: Landing Platform (Docking Bay)", 1),
    ("Sullust", 1),
    ("Tatooine", 1),
    ("A-wing", 3),
    ("B-wing Bomber", 3),
    ("Gray Squadron 1", 1),
    ("Gray Squadron 2", 1),
    ("Nebulon-B Frigate", 3),
    ("Red Squadron 4", 1),
    ("Red Squadron 7", 1),
    ("X-wing", 2),
    ("Y-wing", 1),
    ("BlasTech E-11B Blaster Rifle", 2),
    ("Concussion Missiles", 2),
    ("Enhanced Proton Torpedoes", 1),
    ("Intruder Missile", 2),
]
FIRST_ANTH = {
    "Light": ["Commander Wedge Antilles", "Hit And Run", "X-wing Assault Squadron"],
    "Dark": ["Boba Fett", "Death Star Assault Squadron", "Jabba's Influence"],
}
SECOND_ANTH = {
    "Light": ["Mon Calamari Star Cruiser", "Mon Mothma", "Rapid Deployment"],
    "Dark": ["Flagship Operations", "Sarlacc", "Thunderflare"],
}

# Die-cut face card first. Encyclopedia 2.0 pack maps; Lando With Blaster Rifle
# is a known encyclopedia typo for Lando With Blaster Pistol.
EPP_PACKS = [
    ("Luke With Lightsaber pack", [("Light", "Luke With Lightsaber")]),
    ("Obi-Wan With Lightsaber pack", [("Light", "Obi-Wan With Lightsaber")]),
    ("Darth Vader With Lightsaber pack", [("Dark", "Darth Vader With Lightsaber")]),
    ("Han With Heavy Blaster Pistol pack", [("Light", "Han With Heavy Blaster Pistol")]),
    ("Leia With Blaster Rifle pack", [("Light", "Leia With Blaster Rifle")]),
    ("Boba Fett With Blaster Rifle pack", [("Dark", "Boba Fett With Blaster Rifle")]),
]
ECC_PACKS = [
    (
        "Boba Fett In Slave I pack",
        [
            ("Dark", "Boba Fett In Slave I"),
            ("Dark", "4-LOM With Concussion Rifle"),
            ("Dark", "Any Methods Necessary"),
        ],
    ),
    (
        "Lando With Blaster Pistol pack",
        [
            ("Light", "Lando With Blaster Pistol"),
            ("Light", "Z-95 Bespin Defense Fighter"),
            ("Dark", "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further"),
        ],
    ),
    (
        "IG-88 With Riot Gun pack",
        [
            ("Dark", "IG-88 With Riot Gun"),
            ("Dark", "Dengar In Punishing One"),
            ("Dark", "Crush The Rebellion"),
        ],
    ),
    (
        "Chewie With Blaster Rifle pack",
        [
            ("Light", "Chewie With Blaster Rifle"),
            ("Light", "Lando In Millennium Falcon"),
            ("Light", "Quiet Mining Colony / Independent Operation"),
        ],
    ),
]
EJP_PACKS = [
    (
        "Boushh pack",
        [
            ("Light", "Boushh"),
            ("Dark", "Zuckuss In Mist Hunter"),
            ("Dark", "Court Of The Vile Gangster / I Shall Enjoy Watching You Die"),
        ],
    ),
    (
        "Mara Jade, The Emperor's Hand pack",
        [
            ("Dark", "Mara Jade, The Emperor's Hand"),
            ("Dark", "Bossk With Mortar Gun"),
            ("Light", "You Can Either Profit By This... / Or Be Destroyed"),
        ],
    ),
    (
        "Master Luke pack",
        [
            ("Light", "Master Luke"),
            ("Dark", "Dengar With Blaster Carbine"),
            ("Dark", "IG-88 In IG-2000"),
        ],
    ),
    (
        "See-Threepio pack",
        [
            ("Light", "See-Threepio"),
            ("Dark", "Jodo Kast"),
            ("Dark", "Mara Jade's Lightsaber"),
        ],
    ),
]


def wiki_escape(text: str) -> str:
    if not text:
        return ""
    return (
        text.replace("&", "&amp;")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
        .replace("|", "&#124;")
        .replace("\n", " ")
    )


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", s.lower())


def load_scomp():
    out = []
    for side in ("Light", "Dark"):
        data = json.loads((ROOT / f"scomp-{side}.json").read_text(encoding="utf-8"))
        out.extend(data["cards"] if isinstance(data, dict) else data)
    return out


def resolve(cards, title: str, side: str):
    t = norm(title)
    hits = []
    for c in cards:
        if c.get("side") != side:
            continue
        pt = re.sub(r"^[•*<>]+", "", ((c.get("front") or {}).get("title") or "")).strip()
        if "(V)" in pt or "(AI)" in pt:
            continue
        if norm(pt) != t:
            continue
        hits.append(c)
    if not hits:
        return None
    hits.sort(key=lambda c: int(re.sub(r"\D", "", str(c.get("set") or "999") or "999") or "999"))
    return hits[0]


def file_for(c: dict, url: str | None = None) -> str:
    if not url:
        url = (c.get("front") or {}).get("imageUrl") or ""
    stem = url.split("/")[-1].split("?")[0]
    letter = "L" if c.get("side") == "Light" else "D"
    sid = str(c.get("set"))
    pref = PREFIX.get(sid, "X")
    extra = {
        "108": "EP",
        "109": "ECC",
        "110": "EJP",
        "111": "TA",
        "112": "JPSD",
        "10": "Ref2",
        "13": "Ref3",
    }
    pref = extra.get(sid, pref)
    if sid == "1":
        return f"Premiere-{letter}-{stem}"
    return f"{pref}-{letter}-{stem}"


def recs(c: dict, qty: int = 1) -> list[dict]:
    front = c.get("front") or {}
    title = re.sub(r"^[•*<>]+", "", (front.get("title") or "")).strip()
    typ = front.get("type") or ""
    if typ.startswith("Jedi Test"):
        typ = "Jedi Test"
    if typ.startswith("Admiral"):
        typ = "Admiral's Order"
    if typ == "Objective":
        back = c.get("back") or {}
        labels = gsl.split_objective_sides(title, front.get("gametext") or "")
        faces = [front]
        if back:
            faces.append(back)
        rows = []
        for i, face in enumerate(faces):
            _side_name, text = labels[i] if i < len(labels) else (title, front.get("gametext") or "")
            url = face.get("imageUrl") or ""
            fname = file_for(c, url)
            if url and fname:
                gsl.download(url, gsl.ART / fname)
            rows.append(
                {
                    "title": title,
                    "wiki": gsl.wiki_dest(title, c.get("side") or "", str(c.get("set") or "")),
                    "label": gsl.decipher_objective_name(title),
                    "qty": qty,
                    "type": typ,
                    "type_page": TYPE_PAGE.get(typ, typ),
                    "rarity": c.get("rarity") or "",
                    "destiny": face.get("destiny") or ("0" if i == 0 else "7"),
                    "gtext": wiki_escape(text),
                    "exp": SETN.get(str(c.get("set")), str(c.get("set"))),
                    "file": fname,
                    "side": c.get("side"),
                }
            )
        return rows
    return [
        {
            "title": title,
            "wiki": gsl.wiki_dest(title, c.get("side") or "", str(c.get("set") or "")),
            "label": title,
            "qty": qty,
            "type": typ,
            "type_page": TYPE_PAGE.get(typ, typ),
            "rarity": c.get("rarity") or "",
            "destiny": front.get("destiny") or "",
            "gtext": wiki_escape(front.get("gametext") or ""),
            "exp": SETN.get(str(c.get("set")), str(c.get("set"))),
            "file": file_for(c),
            "side": c.get("side"),
        }
    ]


def table_rows(rows: list, extra_headers: list[str], extra_cells) -> str:
    heads = "! Image !! Card !! Type !! Rarity !! Destiny"
    if extra_headers:
        heads += " !! " + " !! ".join(extra_headers)
    heads += " !! Game text"
    lines = ['{| class="wikitable card-thumbs"', heads]
    for r in rows:
        dest = r.get("wiki") or r["title"]
        img = f"[[File:{r['file']}|200px|link={dest}]]" if r["file"] else ""
        extra = extra_cells(r)
        extra_s = (" || " + " || ".join(extra)) if extra else ""
        label = r.get("label") or r["title"]
        card = f"[[{dest}|{label}]]" if label != dest else f"[[{dest}]]"
        lines.append("|-")
        lines.append(
            f"| {img} || {card} || [[{r['type_page']}|{r['type']}]] || {r['rarity']} || {r['destiny']}{extra_s} || {r['gtext']}"
        )
    lines.append("|}")
    return "\n".join(lines)


def grouped_tables(rows: list, extra_headers, extra_cells) -> str:
    g = defaultdict(list)
    for r in rows:
        g[r["type"]].append(r)
    parts = []
    for t in TYPE_ORDER:
        if t not in g:
            continue
        page = TYPE_PAGE.get(t, t)
        parts.append(f"==== [[{page}]] ====")
        parts.append(table_rows(g[t], extra_headers, extra_cells))
        parts.append("")
    return "\n".join(parts)


def main():
    cards = load_scomp()
    out = ROOT / "pages" / "set-lists"
    out.mkdir(parents=True, exist_ok=True)

    def pack(names, side):
        rows = []
        for title, qty in names:
            c = resolve(cards, title, side)
            if not c:
                print("MISSING", side, title)
                continue
            rows.extend(recs(c, qty))
        return rows

    ds_rows = pack(DS_STARTER, "Dark")
    ls_rows = pack(LS_STARTER, "Light")

    def qty_exp(r):
        q = str(r["qty"]) if r["qty"] != 1 else "1"
        return [q, f"[[{r['exp']}]]"]

    lines = []
    lines.append("Reprints from earlier expansions in these decks carry a 2000 copyright and may have revised text from their first printing.")
    lines.append("")
    lines.append("== Card list ==")
    lines.append("")
    lines.append("=== [[Dark|Dark Side]] ===")
    lines.append("60 predetermined cards.")
    lines.append("")
    lines.append(grouped_tables(ds_rows, ["Qty", "Original expansion"], qty_exp))
    lines.append("=== [[Light|Light Side]] ===")
    lines.append("60 predetermined cards.")
    lines.append("")
    lines.append(grouped_tables(ls_rows, ["Qty", "Original expansion"], qty_exp))
    (out / "Death_Star_II_Starter_Decks.wiki").write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("wrote DS2 starters")

    def anth(names_by_side, later_note: str) -> str:
        parts = ["== Card list ==", ""]
        parts.append(later_note)
        parts.append("")
        for side in ("Light", "Dark"):
            parts.append(f"=== [[{side}|{side} Side]] ===")
            rows = []
            for title in names_by_side[side]:
                c = resolve(cards, title, side)
                if not c:
                    print("MISSING anth", side, title)
                    continue
                rows.extend(recs(c, 1))
            g = defaultdict(list)
            for r in rows:
                g[r["type"]].append(r)
            for t in TYPE_ORDER:
                if t not in g:
                    continue
                page = TYPE_PAGE.get(t, t)
                parts.append(f"==== [[{page}]] ====")
                parts.append(
                    table_rows(
                        g[t],
                        ["Later printed in"],
                        lambda r: [f"[[{r['exp']}]] (black border)"],
                    )
                )
                parts.append("")
        return "\n".join(parts)

    fa = (
        "These six cards were '''white-bordered previews''' in the First Anthology (May 1997). "
        "They are the same cards later printed with black borders in [[Special Edition]], and they became tournament-legal when this product was released. "
        "They are listed here and again under Special Edition."
    )
    sa = (
        "These six cards were '''white-bordered previews''' in the Second Anthology (July 1998). "
        "They were later printed with black borders in [[Special Edition]], [[Endor]], or [[Death Star II]]. "
        "They became tournament-legal when this product was released, and they are listed here and again under those expansions."
    )
    (out / "First_Anthology.wiki").write_text(anth(FIRST_ANTH, fa) + "\n", encoding="utf-8")
    (out / "Second_Anthology.wiki").write_text(anth(SECOND_ANTH, sa) + "\n", encoding="utf-8")
    print("wrote anthologies")

    def write_packs(fn: str, intro: str, packs: list) -> None:
        parts = ["== Card list ==", "", intro, ""]
        for pack_name, members in packs:
            parts.append(f"=== {pack_name} ===")
            rows = []
            for side, title in members:
                c = resolve(cards, title, side)
                if not c:
                    print("MISSING pack", pack_name, side, title)
                    continue
                rows.extend(recs(c, 1))
            parts.append(table_rows(rows, [], lambda r: []))
            parts.append("")
        (out / fn).write_text("\n".join(parts) + "\n", encoding="utf-8")
        print("wrote", fn)

    write_packs(
        "Enhanced_Premiere.wiki",
        "Six die-cut packs. Each pack contains '''one''' premium character (visible through the window) plus four [[Premiere Unlimited]] boosters. The boosters are not listed.",
        EPP_PACKS,
    )
    write_packs(
        "Enhanced_Cloud_City.wiki",
        "Four die-cut packs. Each pack contains '''three''' premium cards (the face card is visible through the window) plus four [[Cloud City]] Limited boosters. The boosters are not listed.",
        ECC_PACKS,
    )
    write_packs(
        "Enhanced_Jabba_s_Palace.wiki",
        "Four die-cut packs. Each pack contains '''three''' premium cards (the face card is visible through the window) plus four [[Jabba's Palace]] Limited boosters. The boosters are not listed. One pack is the [[Boushh]] window; another is [[Mara Jade, The Emperor's Hand]].",
        EJP_PACKS,
    )


if __name__ == "__main__":
    main()
