#!/usr/bin/env python3
"""Generate remaining Premiere Light Side card pages (non-character) from the Tooex template."""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "pages" / "ls-rest"
JSON_PATHS = [
    ROOT / "premiere-cards.json",
    ROOT.parent / "src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json",
]
THUMBS = ROOT / "premiere-thumbs.wiki"

DECIPHER_LS = "https://web.archive.org/web/20020611184117/http://www.decipher.com/starwars/cardlists/premiere/light/index.html"
DECIPHER_DS = "https://web.archive.org/web/20020611184117/http://www.decipher.com/starwars/cardlists/premiere/dark/index.html"
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
TYPE_LABEL = {
    "CHARACTER": "Character",
    "DEVICE": "Device",
    "EFFECT": "Effect",
    "INTERRUPT": "Interrupt",
    "LOCATION": "Location",
    "STARSHIP": "Starship",
    "VEHICLE": "Vehicle",
    "WEAPON": "Weapon",
}
SUBTYPE_LABEL = {
    "USED": "Used Interrupt",
    "LOST": "Lost Interrupt",
    "USED_OR_LOST": "Used or Lost Interrupt",
    "UTINNI": "Utinni Effect",
    "SITE": "Site",
    "SYSTEM": "System",
    "STARFIGHTER": "Starfighter",
    "CAPITAL": "Capital",
    "TRANSPORT": "Transport",
    "CREATURE": "Creature",
    "CHARACTER": "Character",
    "STARSHIP": "Starship",
    "AUTOMATED": "Automated",
    "VEHICLE": "Vehicle",
    "ARTILLERY": "Artillery",
}

# (cardCategory, CardSubtype) → (visible label, wiki page). Label matches
# the printed gold bar; the page is disambiguated when the same word is
# also a card category (Character weapon ≠ Character card).
SUBTYPE_PAGE = {
    ("WEAPON", "CHARACTER"): ("Character", "Character Weapon"),
    ("WEAPON", "STARSHIP"): ("Starship", "Starship Weapon"),
    ("WEAPON", "AUTOMATED"): ("Automated", "Automated Weapon"),
    ("WEAPON", "ARTILLERY"): ("Artillery", "Artillery Weapon"),
    ("WEAPON", "VEHICLE"): ("Vehicle", "Vehicle Weapon"),
    ("INTERRUPT", "USED"): ("Used Interrupt", "Used Interrupt"),
    ("INTERRUPT", "LOST"): ("Lost Interrupt", "Lost Interrupt"),
    ("INTERRUPT", "USED_OR_LOST"): ("Used or Lost Interrupt", "Used or Lost Interrupt"),
    ("EFFECT", "UTINNI"): ("Utinni Effect", "Utinni Effect"),
    ("VEHICLE", "CREATURE"): ("Creature", "Creature Vehicle"),
    ("VEHICLE", "TRANSPORT"): ("Transport", "Transport"),
    ("VEHICLE", "COMBAT"): ("Combat", "Combat Vehicle"),
    ("STARSHIP", "STARFIGHTER"): ("Starfighter", "Starfighter"),
    ("STARSHIP", "CAPITAL"): ("Capital", "Capital"),
    ("STARSHIP", "SHUTTLE"): ("Shuttle", "Shuttle"),
    ("STARSHIP", "SQUADRON"): ("Squadron", "Squadron"),
    ("LOCATION", "SITE"): ("Site", "Site"),
    ("LOCATION", "SYSTEM"): ("System", "System"),
    ("LOCATION", "SECTOR"): ("Sector", "Sector"),
}

AFFILIATION_PAGE = {
    "DROID": "Droid",
    "REBEL": "Rebel",
    "IMPERIAL": "Imperial",
    "ALIEN": "Alien",
    "REPUBLIC": "Republic",
    "SITH": "Sith",
    "JEDI_MASTER": "Jedi Master",
    "DARK_JEDI_MASTER": "Dark Jedi Master",
    "NEW_REPUBLIC": "New Republic",
    "RESISTANCE": "Resistance",
    "FIRST_ORDER": "First Order",
}


def subtype_fields(c) -> tuple[str, str]:
    cat = c.get("cardCategory") or ""
    raw_sub = c.get("cardSubtype") or ""
    if cat == "CHARACTER":
        types = c.get("cardTypes") or []
        raw = types[0] if types else ""
        label = AFFILIATION_PAGE.get(raw, pretty_enum(raw, {}))
        return label, label
    if raw_sub in ("", "NORMAL"):
        return "", ""
    if (cat, raw_sub) in SUBTYPE_PAGE:
        return SUBTYPE_PAGE[(cat, raw_sub)]
    label = pretty_enum(raw_sub, SUBTYPE_LABEL)
    return label, label


ICON_LABEL = {
    "LIGHT_FORCE": "Light Force",
    "DARK_FORCE": "Dark Force",
    "INTERIOR_SITE": "Interior Site",
    "EXTERIOR_SITE": "Exterior Site",
    "PLANET": "Planet",
    "SPACE": "Space",
    "MOBILE": "Mobile",
    "NAV_COMPUTER": "Nav Computer",
    "SCOMP_LINK": "Scomp Link",
    "STARSHIP": "Starship",
    "VEHICLE": "Vehicle",
    "WEAPON": "Weapon",
    "DEVICE": "Device",
    "EFFECT": "Effect",
    "INTERRUPT": "Interrupt",
    "CREATURE": "Creature",
    "PILOT": "Pilot",
    "WARRIOR": "Warrior",
    "REBEL": "Rebel",
    "IMPERIAL": "Imperial",
    "ALIEN": "Alien",
    "DROID": "Droid",
}
CONCEPT_LINKS = [
    "Utinni Effect",
    "Used or Lost Interrupt",
    "Used Interrupt",
    "Lost Interrupt",
    "Interrupt",
    "Effect",
    "Device",
    "Weapon",
    "Starship",
    "Vehicle",
    "Location",
]
EXTRA_LINKS = [
    "R2-D2",
    "Chewbacca",
    "Chewie",
    "Lando",
    "Falcon",
    "Red 5",
    "Red 6",
    "Death Star",
    "Nighttime conditions",
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


def pretty_enum(raw: str, table: dict) -> str:
    if not raw:
        return ""
    if raw in table:
        return table[raw]
    return raw.replace("_", " ").title()


ICON_ORDER = [
    "DARK_FORCE",
    "LIGHT_FORCE",
    "INTERIOR_SITE",
    "EXTERIOR_SITE",
    "PLANET",
    "SPACE",
    "MOBILE",
    "VEHICLE",
    "STARSHIP",
    "SCOMP_LINK",
    "CREATURE",
]


def format_icon(code: str, count: int) -> str:
    name = pretty_enum(code, ICON_LABEL)
    if count > 1:
        return f"[[{name}]] ×{count}"
    return f"[[{name}]]"


def icon_links(icons) -> str:
    if not icons:
        return ""
    parts = []
    for ic in icons:
        parts.append(format_icon(ic.get("icon") or "", ic.get("count") or 1))
    return " ".join(parts)


def location_icon_rows(icons) -> tuple[str, str]:
    """Split location icons into Dark Side / Light Side, with shared site icons on both."""
    by = {}
    for ic in icons or []:
        code = ic.get("icon") or ""
        if code:
            by[code] = ic.get("count") or 1
    shared_codes = [c for c in by if c not in ("DARK_FORCE", "LIGHT_FORCE")]
    shared_codes.sort(
        key=lambda c: ICON_ORDER.index(c) if c in ICON_ORDER else 100 + len(c)
    )
    shared = [format_icon(c, by[c]) for c in shared_codes]
    dark = []
    if "DARK_FORCE" in by:
        dark.append(format_icon("DARK_FORCE", by["DARK_FORCE"]))
    dark.extend(shared)
    light = []
    if "LIGHT_FORCE" in by:
        light.append(format_icon("LIGHT_FORCE", by["LIGHT_FORCE"]))
    light.extend(shared)
    return " ".join(dark), " ".join(light)


def rarity_link(r: str) -> str:
    if not r:
        return "Rarity"
    return RARITY_LINK.get(r[0], "Rarity")


def is_self_name(n: str, title: str) -> bool:
    if n == title:
        return True
    return title.startswith(n + " (") or title.startswith(n + " ")


def aliases_for(title: str) -> list[str]:
    out = []
    m = re.match(r"^(.+?) \((.+)\)$", title)
    if m:
        out.append(m.group(1).strip())
        out.append(m.group(2).strip())
    m2 = re.match(r"^([A-Z0-9]+(?:-[A-Z0-9]+)+) ", title)
    if m2:
        head = m2.group(1)
        if head not in out and head != title:
            out.append(head)
    return out


class Linker:
    def __init__(self, titles: list[str]):
        names = list(titles) + [n for n in EXTRA_LINKS + CONCEPT_LINKS if n not in titles]
        self.names = sorted(set(names), key=len, reverse=True)

    def link_text(self, text: str) -> str:
        out = text
        for n in self.names:
            out = re.sub(rf"(?<!\[\[){re.escape(n)}(?!\]\])", f"[[{n}]]", out)
        return out

    def see_also(self, text: str, title: str) -> str:
        items = []
        for n in self.names:
            if is_self_name(n, title):
                continue
            if n in EXTRA_LINKS and n not in text:
                continue
            if n in text and n not in items:
                items.append(n)
        return "\n".join(f"* [[{x}]]" for x in items)

    def wiki_safe(self, gtext: str, title: str = "") -> str:
        escaped = tpl_escape(gtext)
        if gtext.startswith(("*", "#", ":", ";")):
            escaped = "<nowiki>" + escaped[0] + "</nowiki>" + escaped[1:]
        linked = self.link_text(escaped)
        if title:
            linked = linked.replace(f"[[{title}]]", title)
        return linked


def stat(c, key):
    v = c.get(key)
    if v is None:
        return ""
    return str(v)


def game_text_for(c, linker: Linker) -> str:
    if c.get("cardCategory") == "LOCATION":
        parts = []
        ls = c.get("locationLightSideGameText") or ""
        ds = c.get("locationDarkSideGameText") or ""
        if ls:
            parts.append("'''Light Side:''' " + linker.wiki_safe(ls, c.get("title") or ""))
        if ds:
            parts.append("'''Dark Side:''' " + linker.wiki_safe(ds, c.get("title") or ""))
        return "\n\n".join(parts)
    return linker.wiki_safe(c.get("gameText") or "", c.get("title") or "")


def page_for(c, prev_title, next_title, img, linker: Linker, ds_titles=None, side="Light", list_url=None, hatnote=""):
    title = c["title"]
    uid = c["cardId"]
    cat = c.get("cardCategory") or ""
    type_label = TYPE_LABEL.get(cat, cat.title() if cat else "Card")
    subtype, subtype_link = subtype_fields(c)
    models = c.get("modelTypes") or []
    model = pretty_enum(models[0], {}) if models else ""
    lore = c.get("lore") or ""
    uni = UNI.get(c.get("uniqueness") or "", c.get("uniqueness") or "")
    r = c.get("rarity") or ""
    deploy = c.get("deployCost")
    if deploy is None:
        g = c.get("gameText") or ""
        deploy_s = "*" if g.lstrip().startswith("*") else ""
    else:
        deploy_s = str(deploy)
    gtext = game_text_for(c, linker)
    also_txt = linker.see_also((c.get("gameText") or "") + " " + lore + " " + (c.get("locationLightSideGameText") or "") + " " + (c.get("locationDarkSideGameText") or ""), title)
    printings = (
        "'''Premiere Limited''' (1995, black border) — this page<br />"
        "'''Premiere Unlimited''' (1995/96, white border) — same art and text<br />"
        "Japanese Takara Premiere"
    )
    if list_url is None:
        list_url = DECIPHER_LS if side == "Light" else DECIPHER_DS
    sources = (
        f"* [{list_url} Premiere {side} Side card list] at Decipher.com (archive, 11 June 2002)\n"
        f"* [{DECIPHER_INDEX} Star Wars CCG cardlists index] at Decipher.com (archive, 25 December 2008)\n"
        f"* [{DECIPHER_PDF} Complete Card List] (Decipher PDF, archive 28 September 2007) — {side} {type_label}: {title}, Premiere, {r}"
    )
    fields = {
        "title": title,
        "card_uid": uid,
        "image": img,
        "side": side,
        "type": type_label,
        "subtype": subtype,
        "subtype_link": subtype_link,
        "model": model,
        "set": "Premiere Limited",
        "rarity": r,
        "rarity_link": rarity_link(r),
        "uniqueness": uni,
        "destiny": stat(c, "destiny"),
        "power": stat(c, "power"),
        "ability": stat(c, "ability"),
        "deploy": deploy_s,
        "forfeit": stat(c, "forfeit"),
        "armor": stat(c, "armor"),
        "maneuver": stat(c, "maneuver"),
        "hyperspeed": stat(c, "hyperspeed"),
        "landspeed": stat(c, "landspeed"),
        "icons": "",
        "dark_icons": "",
        "light_icons": "",
        "version_label": "printed",
        "set_band": "Decipher",
        "prev": prev_title or "",
        "next": next_title or "",
        "lore": tpl_escape(lore),
        "game_text": gtext,
        "printings": printings,
        "notes": "",
        "see_also": also_txt,
        "sources": sources,
        "strategy": "",
        "rulings": "",
        "hatnote": hatnote
        or (
            f"For the Dark Side card, see [[{title} (Dark)]]."
            if ds_titles and title in ds_titles
            else ""
        ),
    }
    if cat == "LOCATION":
        dark, light = location_icon_rows(c.get("icons"))
        fields["dark_icons"] = dark
        fields["light_icons"] = light
    else:
        fields["icons"] = icon_links(c.get("icons"))
    try:
        from premiere_extras import extras_fields

        fields.update(extras_fields(uid))
    except Exception:
        pass
    skip_empty = {
        "model",
        "prev",
        "next",
        "deploy",
        "notes",
        "game_text_note",
        "power",
        "ability",
        "forfeit",
        "armor",
        "maneuver",
        "hyperspeed",
        "landspeed",
        "icons",
        "dark_icons",
        "light_icons",
        "subtype",
        "subtype_link",
        "see_also",
        "lore",
        "hatnote",
        "strategy",
        "combos",
        "rulings",
        "pulled_by",
        "pulls",
        "canceled_by",
        "cancels",
        "matching",
        "matching_weapon",
        "also_known_as",
        "personas",
        "characteristics",
        "counterpart",
        "underlying_card_for",
        "has_refs",
    }
    lines = ["{{Card"]
    for k, v in fields.items():
        if v == "" and k in skip_empty:
            continue
        lines.append(f"|{k}={v}")
    lines.append("}}")
    return "\n".join(lines) + "\n"


def main():
    db = load_db()
    imgs = image_map()
    all_ls = [
        c
        for c in db
        if c.get("side") == "LIGHT"
    ]
    all_ls.sort(key=lambda c: int(c["cardId"].split("_")[1]))
    titles = [c["title"] for c in all_ls]
    linker = Linker(titles)
    ds_titles = {c["title"] for c in db if c.get("side") == "DARK"}
    rest = [c for c in all_ls if c.get("cardCategory") != "CHARACTER"]
    OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for i, c in enumerate(rest):
        if i == 0:
            prev_t = "Wioslea"
        else:
            prev_t = rest[i - 1]["title"]
        next_t = rest[i + 1]["title"] if i + 1 < len(rest) else ""
        img = imgs.get(c["cardId"], "")
        text = page_for(c, prev_t, next_t, img, linker, ds_titles)
        path = OUT / f"{c['cardId']}.wiki"
        path.write_text(text, encoding="utf-8")
        written.append((c["title"], c["cardId"], path))
    print("wrote", len(written), "to", OUT)
    (OUT / "index.tsv").write_text(
        "\n".join(f"{uid}\t{title}\t{path.name}" for title, uid, path in written) + "\n",
        encoding="utf-8",
    )
    occupied = {c["title"] for c in all_ls}
    occupied.update({"2X-3KPR (Tooex)", "Tooex", "2X-3KPR"})
    alias_rows = []
    for title, uid, _path in written:
        for alias in aliases_for(title):
            if alias and alias not in occupied:
                alias_rows.append((alias, title))
                occupied.add(alias)
    (OUT / "aliases.tsv").write_text(
        "\n".join(f"{alias}\t{dest}" for alias, dest in alias_rows) + "\n",
        encoding="utf-8",
    )
    print("aliases", len(alias_rows))


if __name__ == "__main__":
    main()
