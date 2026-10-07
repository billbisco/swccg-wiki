#!/usr/bin/env python3
"""Generate Premiere Light Side character card pages from GEMP JSON + Tooex template."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "pages" / "ls-chars"
JSON_PATHS = [
    ROOT / "premiere-cards.json",
    ROOT.parent / "src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json",
]
THUMBS = ROOT / "premiere-thumbs.wiki"

DECIPHER_LS = "https://web.archive.org/web/20020611184117/http://www.decipher.com/starwars/cardlists/premiere/light/index.html"
DECIPHER_INDEX = "https://web.archive.org/web/20081225225012/http://www.decipher.com/starwars/cardlists/index.html"
DECIPHER_PDF = "https://web.archive.org/web/20070928014432/http://www.decipher.com/starwars/cardlists/swallcards.pdf"

RARITY_LINK = {
    "C": "Rarity#Common",
    "U": "Rarity#Uncommon",
    "R": "Rarity#Rare",
}
UNI = {
    "UNRESTRICTED": "Unrestricted",
    "UNIQUE": "Unique",
    "RESTRICTED_2": "Restricted (••)",
    "RESTRICTED_3": "Restricted (•••)",
}

# Names to wiki-link in game text / see also when they appear.
LINK_NAMES = [
    "Hydroponics Station",
    "Owen Lars",
    "Beru Lars",
    "Luke Skywalker",
    "Han Solo",
    "Leia Organa",
    "Obi-Wan Kenobi",
    "C-3PO",
    "R2-D2",
    "Rebel Planners",
    "Wrong Turn",
    "Millennium Falcon",
    "Falcon",
    "Red 5",
    "Red 3",
    "Red 6",
    "Red 1",
    "Gold 1",
    "Gold 5",
    "Lateral Damage",
    "Nightfall",
    "Restraining Bolt",
    "Vaporator",
    "Tatooine",
    "Yavin 4",
    "Death Star",
    "Lars' Moisture Farm",
    "Utinni Effect",
    "Used Interrupt",
    "Lost Interrupt",
    "Interrupt",
    "Effect",
    "Device",
    "Weapon",
]


def load_db():
    for p in JSON_PATHS:
        if p.exists():
            data = json.loads(p.read_text(encoding="utf-8"))
            if data and data[0].get("expansionSet") != "PREMIERE":
                data = [c for c in data if c.get("expansionSet") == "PREMIERE"]
            return data
    raise SystemExit("no json")


def image_map():
    text = THUMBS.read_text(encoding="utf-8")
    m = {}
    for uid, fn in re.findall(
        r"\[\[File:(Premiere-L-[a-z0-9]+\.gif)\|200px\|link=Card:(1_\d+)\]\]",
        text,
    ):
        m[uid] = uid and fn
    # fix: groups are file, id
    m = {}
    for fn, uid in re.findall(
        r"\[\[File:(Premiere-L-[a-z0-9]+\.gif)\|200px\|link=Card:(1_\d+)\]\]",
        text,
    ):
        m[uid] = fn
    return m


def tpl_escape(s: str) -> str:
    if s is None:
        return ""
    return (
        str(s)
        .replace("&", "&amp;")
        .replace("|", "{{!}}")
        .replace("{{{", "{{(}}")
        .replace("<", "&lt;")
        .replace(">", "&gt;")
    )


def link_text(text: str) -> str:
    # longest names first
    names = sorted(LINK_NAMES, key=len, reverse=True)
    out = text
    for n in names:
        out = re.sub(rf"(?<!\[\[){re.escape(n)}(?!\]\])", f"[[{n}]]", out)
    return out


def is_self_name(n: str, title: str) -> bool:
    if n == title:
        return True
    return title.startswith(n + " (") or title.startswith(n + " ")


def see_also_from(text: str, title: str) -> list[str]:
    items = []
    for n in sorted(LINK_NAMES, key=len, reverse=True):
        if is_self_name(n, title):
            continue
        if n in text and n not in items:
            items.append(n)
    return items


def aliases_for(title: str) -> list[str]:
    out = []
    m = re.match(r"^(.+?) \((.+)\)$", title)
    if m:
        out.append(m.group(1).strip())
        out.append(m.group(2).strip())
    m2 = re.match(r"^([A-Z0-9]+(?:-[A-Z0-9]+)*) ", title)
    if m2:
        head = m2.group(1)
        if head not in out and head != title:
            out.append(head)
    return out


def wiki_safe_gametext(gtext: str) -> str:
    escaped = tpl_escape(gtext)
    if gtext.startswith(("*", "#", ":", ";")):
        escaped = "<nowiki>" + escaped[0] + "</nowiki>" + escaped[1:]
    return link_text(escaped)


def rarity_link(r: str) -> str:
    if not r:
        return "Rarity"
    return RARITY_LINK.get(r[0], "Rarity")


def icon_links(icons) -> str:
    if not icons:
        return ""
    parts = []
    for ic in icons:
        name = ic["icon"].title()
        parts.append(f"[[{name}]]")
    return " ".join(parts)


def page_for(c, prev_title, next_title, img):
    title = c["title"]
    uid = c["cardId"]
    types = c.get("cardTypes") or []
    subtype = types[0].title() if types else "Character"
    models = c.get("modelTypes") or []
    model = models[0].title() if models else ""
    lore = c.get("lore") or ""
    gtext = c.get("gameText") or ""
    uni = UNI.get(c.get("uniqueness") or "", c.get("uniqueness") or "")
    r = c.get("rarity") or ""
    deploy = c.get("deployCost")
    if deploy is None:
        deploy_s = "*" if (c.get("gameText") or "").lstrip().startswith("*") else ""
    else:
        deploy_s = str(deploy)
    also = see_also_from(gtext + " " + lore, title)
    also_txt = "\n".join(f"* [[{x}]]" for x in also) if also else "* [[Premiere Limited]]"
    printings = (
        "'''Premiere Limited''' (1995, black border) — this page<br />"
        "'''Premiere Unlimited''' (1995/96, white border) — same art and text<br />"
        "Japanese Takara Premiere"
    )
    sources = (
        f"* [{DECIPHER_LS} Premiere Light Side card list] at Decipher.com (archive, 11 June 2002)\n"
        f"* [{DECIPHER_INDEX} Star Wars CCG cardlists index] at Decipher.com (archive, 25 December 2008)\n"
        f"* [{DECIPHER_PDF} Complete Card List] (Decipher PDF, archive 28 September 2007) — Light Character: {title}, Premiere, {r}"
    )
    fields = {
        "title": title,
        "card_uid": uid,
        "image": img,
        "side": "Light",
        "type": "Character",
        "subtype": subtype,
        "subtype_link": subtype,
        "model": model,
        "set": "Premiere Limited",
        "rarity": r,
        "rarity_link": rarity_link(r),
        "uniqueness": uni,
        "destiny": c.get("destiny") if c.get("destiny") is not None else "",
        "power": c.get("power") if c.get("power") is not None else "",
        "ability": c.get("ability") if c.get("ability") is not None else "",
        "deploy": deploy_s,
        "forfeit": c.get("forfeit") if c.get("forfeit") is not None else "",
        "landspeed": c.get("landspeed") if c.get("landspeed") is not None else "",
        "icons": icon_links(c.get("icons")),
        "version_label": "printed",
        "set_band": "Decipher",
        "prev": prev_title or "",
        "next": next_title or "",
        "lore": tpl_escape(lore),
        "game_text": wiki_safe_gametext(gtext),
        "printings": printings,
        "notes": "",
        "see_also": also_txt,
        "sources": sources,
        "hatnote": "For the Dark Side card, see [[Jawa (Dark)]]." if title == "Jawa" else "",
        "strategy": "",
        "rulings": "",
    }
    try:
        from premiere_extras import extras_fields

        fields.update(extras_fields(uid))
    except Exception:
        pass
    lines = ["{{Card"]
    for k, v in fields.items():
        if v == "" and k in (
            "model", "prev", "next", "deploy", "notes", "game_text_note", "hatnote",
            "strategy", "combos", "rulings", "pulled_by", "pulls", "canceled_by",
            "cancels", "matching", "matching_weapon", "also_known_as", "personas",
            "characteristics", "counterpart", "underlying_card_for", "has_refs",
        ):
            continue
        lines.append(f"|{k}={v}")
    lines.append("}}")
    return "\n".join(lines) + "\n"


def main():
    db = load_db()
    imgs = image_map()
    chars = [
        c
        for c in db
        if c.get("side") == "LIGHT" and c.get("cardCategory") == "CHARACTER"
    ]
    chars.sort(key=lambda c: int(c["cardId"].split("_")[1]))
    OUT.mkdir(parents=True, exist_ok=True)
    titles = [c["title"] for c in chars]
    written = []
    for i, c in enumerate(chars):
        if c["cardId"] == "1_1":
            continue  # keep hand-written Tooex page
        prev_t = titles[i - 1] if i else ""
        next_t = titles[i + 1] if i + 1 < len(titles) else ""
        img = imgs.get(c["cardId"], "")
        text = page_for(c, prev_t, next_t, img)
        safe = re.sub(r"[^\w\-. ()']+", "_", c["title"])
        path = OUT / f"{c['cardId']}.wiki"
        path.write_text(text, encoding="utf-8")
        written.append((c["title"], c["cardId"], path))
    print("wrote", len(written), "to", OUT)
    index = OUT / "index.tsv"
    index.write_text(
        "\n".join(f"{uid}\t{title}\t{path.name}" for title, uid, path in written) + "\n",
        encoding="utf-8",
    )
    alias_rows = []
    occupied = {c["title"] for c in chars}
    for title, uid, _path in written:
        for alias in aliases_for(title):
            if alias and alias not in occupied:
                alias_rows.append((alias, title))
                occupied.add(alias)
    # Tooex (hand-written 1_1) uses the same parenthetical pattern.
    for alias in aliases_for("2X-3KPR (Tooex)"):
        if alias and alias not in occupied:
            alias_rows.append((alias, "2X-3KPR (Tooex)"))
            occupied.add(alias)
    (OUT / "aliases.tsv").write_text(
        "\n".join(f"{alias}\t{dest}" for alias, dest in alias_rows) + "\n",
        encoding="utf-8",
    )
    print("aliases", len(alias_rows))


if __name__ == "__main__":
    main()
