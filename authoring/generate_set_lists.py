#!/usr/bin/env python3
"""Thumbs tables for Decipher set hubs from scomp + PC card art URLs."""
from __future__ import annotations

import json
import re
import urllib.request
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
ART = ROOT / "set-card-art"
UA = {"User-Agent": "SWCCGWiki/1.0"}

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
    "Objective",
    "Epic Event",
    "Jedi Test",
    "Admiral's Order",
    "Podracer",
    "Defensive Shield",
]
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
    "Jedi Test": "Jedi Test",
    "Jedi Test #6": "Jedi Test",
    "Admiral's Order": "Admiral's Order",
    "Podracer": "Podracer",
    "Defensive Shield": "Defensive Shield",
}

# Booster expansions: unique cards only. Skip Unlimited/Revised.
EXPANSIONS = [
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
]
# Premium unique-only (scomp already has just the unique cards for these).
# Enhanced Premiere / Cloud City / Jabba's Palace are pack-variant lists
# in generate_premium_lists.py, not a flat unique dump.
PREMIUM_UNIQUE = [
    ("101", "Premiere Two-Player Introductory Game", "P2P"),
    ("104", "The Empire Strikes Back Introductory Two-Player Game", "ESB2P"),
    ("103", "Rebel Leader Packs", "RL"),
    ("102", "Jedi Pack", "Jedi"),
    ("106", "Official Tournament Sealed Deck", "OTSD"),
    ("111", "Third Anthology", "TA"),
    ("112", "Jabba's Palace Sealed Deck", "JPSD"),
    ("10", "Reflections II: Expanding the Galaxy", "Ref2"),
    ("13", "Reflections III: A Collector's Bounty", "Ref3"),
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


def printed(card: dict) -> str:
    t = ((card.get("front") or {}).get("title") or "")
    return re.sub(r"^[•*<>]+", "", t).strip()


def norm_type(raw: str) -> str:
    t = (raw or "Character").strip()
    if t.startswith("Jedi Test"):
        return "Jedi Test"
    return TYPE_PAGE.get(t, t)


def load_scomp():
    out = []
    for side in ("Light", "Dark"):
        data = json.loads((ROOT / f"scomp-{side}.json").read_text(encoding="utf-8"))
        cards = data["cards"] if isinstance(data, dict) else data
        for c in cards:
            out.append(c)
    return out


_TITLE_MAP = None


def title_map() -> dict:
    global _TITLE_MAP
    if _TITLE_MAP is None:
        p = ROOT / "card_title_map.json"
        if p.exists():
            _TITLE_MAP = json.loads(p.read_text(encoding="utf-8"))
        else:
            _TITLE_MAP = {}
    return _TITLE_MAP


def wiki_dest(title: str, side: str, sid: str) -> str:
    return title_map().get(f"{sid}|{side}|{title}") or title


def wiki_file(prefix: str, side: str, url: str) -> str:
    name = url.split("/")[-1].split("?")[0]
    letter = "L" if side == "Light" else "D"
    return f"{prefix}-{letter}-{name}"


def decipher_objective_name(title: str) -> str:
    """Decipher cardlists: Hidden Base/Systems Will Slip Through Your Fingers."""
    return title.replace(" / ", "/")


def strip_side_heading(name: str, text: str) -> str:
    """Game text should not repeat the side title already in the Card column."""
    prefix = name + ":"
    if text.startswith(prefix):
        return text[len(prefix) :].strip()
    return text


def split_objective_sides(title: str, gametext: str) -> list[tuple[str, str]]:
    """0-side then 7-side game text, without the side-name prefix."""
    if " / " not in title:
        return [(title, gametext)]
    front_name, back_name = title.split(" / ", 1)
    marker = back_name + ":"
    idx = gametext.find(marker)
    if idx > 0:
        return [
            (front_name, strip_side_heading(front_name, gametext[:idx].strip())),
            (back_name, strip_side_heading(back_name, gametext[idx:].strip())),
        ]
    return [
        (front_name, strip_side_heading(front_name, gametext)),
        (back_name, strip_side_heading(back_name, gametext)),
    ]


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 400:
        return
    req = urllib.request.Request(url, headers=UA)
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            dest.write_bytes(r.read())
    except Exception as e:
        print("fail", url, e)


def objective_faces(c: dict, prefix: str, fetch: bool) -> list[dict]:
    """One thumbs row for the 0 side, then one for the 7 side."""
    front = c.get("front") or {}
    back = c.get("back") or {}
    title = printed(c)
    side = c.get("side") or "Light"
    gtext = front.get("gametext") or ""
    labels = split_objective_sides(title, gtext)
    faces = [front]
    if back:
        faces.append(back)
    rows = []
    for i, face in enumerate(faces):
        _side_name, text = labels[i] if i < len(labels) else (title, gtext)
        url = face.get("imageUrl") or ""
        fname = wiki_file(prefix, side, url) if url else ""
        if fetch and url and fname:
            download(url, ART / fname)
        rows.append(
            {
                "title": title,
                "wiki": wiki_dest(title, side, str(c.get("set") or "")),
                "label": decipher_objective_name(title),
                "file": fname,
                "rarity": c.get("rarity") or "",
                "destiny": face.get("destiny") or ("0" if i == 0 else "7"),
                "gtext": wiki_escape(text),
                "type": "Objective",
            }
        )
    return rows


def rows_for(cards: list, prefix: str, fetch: bool) -> dict:
    grouped = defaultdict(list)
    for c in cards:
        front = c.get("front") or {}
        title = printed(c)
        if not title:
            continue
        side = c.get("side") or "Light"
        typ = norm_type(front.get("type") or "")
        if typ == "Objective":
            for row in objective_faces(c, prefix, fetch):
                grouped[(side, typ)].append(row)
            continue
        url = front.get("imageUrl") or ""
        fname = wiki_file(prefix, side, url) if url else ""
        if fetch and url and fname:
            download(url, ART / fname)
        gtext = front.get("gametext") or ""
        grouped[(side, typ)].append(
            {
                "title": title,
                "wiki": wiki_dest(title, side, str(c.get("set") or "")),
                "label": title,
                "file": fname,
                "rarity": c.get("rarity") or "",
                "destiny": front.get("destiny") or "",
                "gtext": wiki_escape(gtext),
                "type": typ,
            }
        )
    return grouped


def table(grouped: dict) -> str:
    lines = ["== Card list ==", ""]
    for side in ("Light", "Dark"):
        any_side = any(grouped.get((side, t)) for t in TYPE_ORDER)
        if not any_side:
            continue
        lines.append(f"=== [[{side}|{side} Side]] ===")
        for t in TYPE_ORDER:
            rows = grouped.get((side, t)) or []
            if not rows:
                continue
            page = TYPE_PAGE.get(t, t)
            lines.append(f"==== [[{page}]] ====")
            lines.append('{| class="wikitable card-thumbs"')
            lines.append("! Image !! Card !! Type !! Rarity !! Destiny !! Game text")
            for r in rows:
                dest = r.get("wiki") or r["title"]
                img = (
                    f"[[File:{r['file']}|200px|link={dest}]]"
                    if r["file"]
                    else ""
                )
                label = r.get("label") or r["title"]
                card = (
                    f"[[{dest}|{label}]]"
                    if label != dest
                    else f"[[{dest}]]"
                )
                page = TYPE_PAGE.get(r["type"], r["type"])
                lines.append("|-")
                lines.append(
                    f"| {img} || {card} || [[{page}|{r['type']}]] || {r['rarity']} || {r['destiny']} || {r['gtext']}"
                )
            lines.append("|}")
            lines.append("")
    return "\n".join(lines) + "\n"


def main(fetch: bool = True):
    all_cards = load_scomp()
    by_set = defaultdict(list)
    for c in all_cards:
        by_set[str(c.get("set"))].append(c)
    outdir = ROOT / "pages" / "set-lists"
    outdir.mkdir(parents=True, exist_ok=True)
    for sid, title, prefix in EXPANSIONS + PREMIUM_UNIQUE:
        cards = by_set.get(sid) or []
        print("set", sid, title, len(cards))
        grouped = rows_for(cards, prefix, fetch)
        text = table(grouped)
        path = outdir / (re.sub(r"[^A-Za-z0-9]+", "_", title).strip("_") + ".wiki")
        path.write_text(text, encoding="utf-8")
        print(" wrote", path.name, "bytes", path.stat().st_size)
    print("art dir", ART, "files", len(list(ART.glob("*.gif"))) if ART.exists() else 0)


if __name__ == "__main__":
    main()
