#!/usr/bin/env python3
"""Virtual set hubs + Template:Card pages from PC cardlists + scomp.

Current virtual (2014 Reset onward) uses scomp gametext when present.
Legacy blocks are not in scomp — pages use the PC card image, title, type,
and rarity; game text is not invented.

Virtual Master is the union of Blocks 1–9 + Virtual Shields, so it is not
imported as a second copy of those cards.
"""
from __future__ import annotations

import html as htmlmod
import json
import re
import sys
import urllib.request
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from xml.sax.saxutils import escape as xml_escape

sys.path.insert(0, str(Path(__file__).resolve().parent))
import generate_remaining_cards as grc
import generate_set_lists as gsl
import premiere_extras as extras

ROOT = Path(__file__).resolve().parent
ART = ROOT / "set-card-art"
BANNERS = ROOT / "set-art-virtual"
CACHE = ROOT / "pc-cardlists"
OUT_PAGES = ROOT / "pages" / "virtual"
OUT_HUBS = ROOT / "pages" / "set-hubs"
OUT_LISTS = ROOT / "pages" / "set-lists"
MAP_PATH = ROOT / "card_title_map.json"
UA = {"User-Agent": "SWCCGWiki/1.0"}
CARDLIST = "https://res.starwarsccg.org/cardlists/{slug}Type.html"
SCOMP_UI = "https://scomp.starwarsccg.org"
SLIPS = "https://www.starwarsccg.org/resources/virtual-slips/"
COLLECTING = "https://www.starwarsccg.org/collecting/"

TYPE_FROM_HEADING = {
    "CHARACTER": "Character",
    "CREATURE": "Creature",
    "DEVICE": "Device",
    "EFFECT": "Effect",
    "INTERRUPT": "Interrupt",
    "LOCATION": "Location",
    "STARSHIP": "Starship",
    "VEHICLE": "Vehicle",
    "WEAPON": "Weapon",
    "OBJECTIVE": "Objective",
    "EPIC EVENT": "Epic Event",
    "JEDI TEST": "Jedi Test",
    "ADMIRAL'S ORDER": "Admiral's Order",
    "ADMIRALS ORDER": "Admiral's Order",
    "PODRACER": "Podracer",
    "DEFENSIVE SHIELD": "Defensive Shield",
    "MISSION": "Mission",
}
LOC_SUB = {"Site": "Site", "System": "System", "Sector": "Sector"}
CHAR_SUB = {
    "Rebel", "Imperial", "Alien", "Droid", "Republic", "Sith",
    "Jedi Master", "Dark Jedi Master", "New Republic", "Separatist",
}
SKIP_SET_ICONS = {f"Set {n}" for n in range(0, 28)} | {
    "Set D", "Set P", "Premium", "Virtual",
}

CURRENT = [
    ("200", "Virtual Set 0", "V0", "24 September 2014", "Set0", "SET0_title.gif"),
    ("setd", "Virtual Set D", "VD", "24 September 2014", "SetD", "SETD_title.gif"),
    ("201", "Virtual Set 1", "V1", "27 March 2015", "Set1", "SET1_title.gif"),
    ("202", "Virtual Set 2", "V2", "17 July 2015", "Set2", "SET2_title.gif"),
    ("203", "Virtual Set 3", "V3", "4 December 2015", "Set3", "SET3_title.gif"),
    ("204", "Virtual Set 4", "V4", "29 June 2016", "Set4", "SET4_title.gif"),
    ("205", "Virtual Set 5", "V5", "23 November 2016", "Set5", "SET5_title.gif"),
    ("301", "Virtual Set P", "VP", "24 February 2017", "SetP", "SETP_title.gif"),
    ("206", "Virtual Set 6", "V6", "14 April 2017", "Set6", "SET6_title.gif"),
    ("207", "Virtual Set 7", "V7", "13 July 2017", "Set7", "SET7_title.gif"),
    ("208", "Virtual Set 8", "V8", "30 November 2017", "Set8", "SET8_title.gif"),
    ("209", "Virtual Set 9", "V9", "6 July 2018", "Set9", "SET9_title.gif"),
    ("210", "Virtual Set 10", "V10", "8 January 2019", "Set10", "SET10_title.gif"),
    ("211", "Virtual Set 11", "V11", "2 August 2019", "Set11", "SET11_title.gif"),
    ("212", "Virtual Set 12", "V12", "22 March 2020", "Set12", "SET12_title.gif"),
    ("213", "Virtual Set 13", "V13", "9 November 2020", "Set13", "SET13_title.gif"),
    ("214", "Virtual Set 14", "V14", "18 March 2021", "Set14", "SET14_title.gif"),
    ("215", "Virtual Set 15", "V15", "23 June 2021", "Set15", "SET15_title.gif"),
    ("216", "Virtual Set 16", "V16", "3 September 2021", "Set16", "SET16_title.gif"),
    ("217", "Virtual Set 17", "V17", "20 December 2021", "Set17", "SET17_title.gif"),
    ("218", "Virtual Set 18", "V18", "21 April 2022", "Set18", "SET18_title.gif"),
    ("219", "Virtual Set 19", "V19", "15 August 2022", "Set19", "SET19_title.gif"),
    ("220", "Virtual Set 20", "V20", "12 December 2022", "Set20", "SET20_title.gif"),
    ("221", "Virtual Set 21", "V21", "18 June 2023", "Set21", "SET21_title.gif"),
    ("222", "Virtual Set 22", "V22", "2 October 2023", "Set22", "SET22_title.gif"),
    ("223", "Virtual Set 23", "V23", "22 July 2024", "Set23", "SET23_title.gif"),
    ("224", "Virtual Set 24", "V24", "30 December 2024", "Set24", "SET24_title.gif"),
    ("225", "Virtual Set 25", "V25", "8 August 2025", "Set25", "SET25_title.gif"),
    ("226", "Virtual Set 26", "V26", "8 December 2025", "Set26", "SET26_title.gif"),
    ("227", "Virtual Set 27", "V27", "24 August 2026", "Set27", "SET27_title.gif"),
]
LEGACY = [
    ("vb1", "Virtual Block 1", "VB1", "2002–2014", "VBlock1", "v1-title.jpg"),
    ("vb2", "Virtual Block 2", "VB2", "2002–2014", "VBlock2", "v2-title.jpg"),
    ("vb3", "Virtual Block 3", "VB3", "2002–2014", "VBlock3", "v3-title.jpg"),
    ("vb4", "Virtual Block 4", "VB4", "2002–2014", "VBlock4", "v4-title.jpg"),
    ("vb5", "Virtual Block 5", "VB5", "2002–2014", "VBlock5", "v5-title.jpg"),
    ("vb6", "Virtual Block 6", "VB6", "2002–2014", "VBlock6", "v6-title.jpg"),
    ("vb7", "Virtual Block 7", "VB7", "2002–2014", "VBlock7", "v7-title.jpg"),
    ("vb8", "Virtual Block 8", "VB8", "2002–2014", "VBlock8", "v8-title.jpg"),
    ("vb9", "Virtual Block 9", "VB9", "2002–2014", "VBlock9", "v9-title.jpg"),
    ("vsh", "Virtual Shields", "VSh", "2002–2014", "VShields", "vd_title.jpg"),
]
ALL_SETS = CURRENT + LEGACY
SET_NAME = {sid: name for sid, name, *_ in ALL_SETS}
SET_PREFIX = {sid: pref for sid, _n, pref, *_ in ALL_SETS}
SET_DATE = {sid: date for sid, _n, _p, date, *_ in ALL_SETS}
SET_SLUG = {sid: slug for sid, _n, _p, _d, slug, *_ in ALL_SETS}
SET_BANNER = {sid: ban for sid, *_rest, ban in ALL_SETS}
CURRENT_IDS = {sid for sid, *_ in CURRENT}
LEGACY_IDS = {sid for sid, *_ in LEGACY}

TYPE_ORDER = list(gsl.TYPE_ORDER) + ["Mission"]
gsl.TYPE_PAGE.setdefault("Mission", "Mission")


def fetch(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.read()


def fetch_text(url: str) -> str:
    return fetch(url).decode("utf-8", "replace")


def download(url: str, dest: Path) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists() and dest.stat().st_size > 400:
        return
    try:
        dest.write_bytes(fetch(url))
    except Exception as e:
        print("fail", url, e)


def prefetch_art(cards_by_set: dict[str, list[dict]]) -> None:
    jobs = []
    for sid, _name, pref, _date, _slug, banner in ALL_SETS:
        jobs.append(
            (
                f"https://res.starwarsccg.org/cardlists/images/{banner}",
                BANNERS / f"Set-{pref}-title.{banner.split('.')[-1]}",
            )
        )
        for c in cards_by_set.get(sid) or []:
            side = c.get("side") or "Light"
            for face in (c.get("front") or {}, c.get("back") or {}):
                url = face.get("imageUrl") or ""
                if not url:
                    continue
                jobs.append((url, ART / wiki_image(pref, side, url)))
    pending = [(u, d) for u, d in jobs if not (d.exists() and d.stat().st_size > 400)]
    print("art cached", len(jobs) - len(pending), "to fetch", len(pending), flush=True)
    if not pending:
        return
    done = 0
    with ThreadPoolExecutor(max_workers=12) as pool:
        futs = [pool.submit(download, u, d) for u, d in pending]
        for _ in as_completed(futs):
            done += 1
            if done % 100 == 0 or done == len(pending):
                print("art", done, "/", len(pending), flush=True)


def clean_title(raw: str) -> str:
    t = htmlmod.unescape(re.sub(r"<[^>]+>", "", raw or ""))
    t = t.replace("\xa0", " ").strip()
    t = re.sub(r"\s+", " ", t)
    return t


def printed_title(raw: str) -> str:
    return re.sub(r"^[•*<>]+", "", clean_title(raw)).strip()


def uniqueness_from_marks(raw: str) -> str:
    t = clean_title(raw).lstrip()
    if t.startswith("•••") or t.startswith("***"):
        return "***"
    if t.startswith("••") or t.startswith("**"):
        return "**"
    if t.startswith("•") or t.startswith("*"):
        return "*"
    if t.startswith("<>"):
        return "<>"
    return None


def stem_of(url: str) -> str:
    return url.split("/")[-1].split("?")[0]


def wiki_image(prefix: str, side: str, url: str) -> str:
    letter = "L" if side == "Light" else "D"
    stem = stem_of(url)
    if (prefix.startswith("VB") or prefix == "VSh") and stem.endswith(".gif") and not stem.endswith("-pre.gif"):
        stem = stem[:-4] + "-pre.gif"
    return f"{prefix}-{letter}-{stem}"


def parse_section(html: str, side: str) -> list[dict]:
    """Card rows from one Light or Dark half of a Type.html list."""
    rows = []
    typ = "Character"
    for m in re.finditer(r"<tr>(.*?)</tr>", html, re.S | re.I):
        cell = m.group(1)
        tcell = re.search(r"class=['\"]type['\"]>\s*([^<]+)", cell, re.I)
        if tcell:
            key = re.sub(r"\s+", " ", tcell.group(1)).strip().upper()
            typ = TYPE_FROM_HEADING.get(key, key.title())
            continue
        links = re.findall(
            r"<a href=['\"](https://res\.starwarsccg\.org/cards/[^'\"]+/large/[^'\"]+)['\"][^>]*>(.*?)</a>",
            cell,
            re.S | re.I,
        )
        if not links:
            continue
        rar = ""
        rds = re.findall(r"<td class=['\"]center['\"][^>]*>\s*([^<]*?)\s*</td>", cell, re.I)
        if rds:
            rar = rds[-1].strip()
        icon = ""
        im = re.search(r'title=["\']([^"\']+)["\']', cell)
        if im:
            icon = im.group(1).strip()
        titles = [clean_title(t) for _u, t in links]
        urls = [u for u, _t in links]
        if len(links) >= 2 and typ == "Objective":
            title = printed_title(titles[0]) + " / " + printed_title(titles[1])
            raw = titles[0]
            url = urls[0]
            back_url = urls[1]
        else:
            title_raw = titles[0]
            title = printed_title(title_raw)
            raw = titles[0]
            url = urls[0]
            back_url = urls[1] if len(urls) > 1 else ""
        if not title or not url:
            continue
        row_typ = typ
        if icon in TYPE_FROM_HEADING.values() or icon in {
            "Defensive Shield", "Objective", "Mission", "Epic Event",
            "Jedi Test", "Admiral's Order", "Podracer",
        }:
            row_typ = icon
        sub = ""
        if row_typ == "Location":
            sub = LOC_SUB.get(icon, icon if icon in ("Site", "System", "Sector") else "Site")
        elif row_typ == "Character":
            sub = icon if icon in CHAR_SUB or "/" in icon else icon
        elif row_typ == "Weapon":
            sub = icon if icon else ""
        rows.append(
            {
                "side": side,
                "type": row_typ,
                "subType": sub,
                "title_raw": raw,
                "title": title,
                "url": url,
                "back_url": back_url,
                "rarity": rar,
                "icon": icon,
                "uniqueness": uniqueness_from_marks(raw),
            }
        )
    return rows


def parse_cardlist(html: str) -> list[dict]:
    """Rows from a PC Type.html list."""
    parts = re.split(
        r"Card List\s*(?:&#8211;|–|&ndash;|-)\s*(Light|Dark) Side",
        html,
        flags=re.I,
    )
    rows = []
    i = 1
    while i + 1 < len(parts):
        side = "Light" if parts[i].lower().startswith("l") else "Dark"
        rows.extend(parse_section(parts[i + 1], side))
        i += 2
    return rows


def load_cardlist(slug: str) -> list[dict]:
    CACHE.mkdir(parents=True, exist_ok=True)
    path = CACHE / f"{slug}Type.html"
    if not path.exists() or path.stat().st_size < 500:
        path.write_text(fetch_text(CARDLIST.format(slug=slug)), encoding="utf-8")
    return parse_cardlist(path.read_text(encoding="utf-8"))


def load_scomp_virtual() -> list[dict]:
    out = []
    for side in ("Light", "Dark"):
        data = json.loads((ROOT / f"scomp-{side}.json").read_text(encoding="utf-8"))
        cards = data["cards"] if isinstance(data, dict) else data
        for c in cards:
            sid = str(c.get("set"))
            url = ((c.get("front") or {}).get("imageUrl") or "")
            if sid == "200d":
                if "ResetDS" in url:
                    c = dict(c)
                    c["set"] = "setd"
                    out.append(c)
                continue
            if sid in CURRENT_IDS:
                typ = ((c.get("front") or {}).get("type") or "")
                if typ == "Game Aid":
                    continue
                out.append(c)
    return out


def scomp_index(cards: list[dict]) -> tuple[dict, dict]:
    by_url = {}
    by_title = {}
    for c in cards:
        front = c.get("front") or {}
        url = front.get("imageUrl") or ""
        if url:
            by_url[url] = c
        t = printed_title(front.get("title") or "")
        side = c.get("side") or "Light"
        by_title[(str(c.get("set")), side, t.lower())] = c
    return by_url, by_title


def decipher_objective_bases() -> set[str]:
    """Decipher dual-title objectives, (V) stripped — used to mark VB reprints."""
    bases: set[str] = set()
    if not MAP_PATH.exists():
        return bases
    dests = json.loads(MAP_PATH.read_text(encoding="utf-8"))
    virt_ids = set(SET_NAME)
    for k, v in dests.items():
        sid = k.split("|", 1)[0]
        if sid in virt_ids:
            continue
        printed = k.split("|", 2)[2] if k.count("|") >= 2 else v
        if " / " in printed:
            bases.add(re.sub(r" \(V\)", "", printed))
    return bases


def legacy_objective_title(dual: str, bases: set[str]) -> str:
    """PC lists often put (V) only on the 7-side. Reprints print (V) on both faces."""
    parts = [p.strip() for p in dual.split(" / ")]
    if len(parts) < 2:
        return dual
    base = " / ".join(re.sub(r" \(V\)$", "", p) for p in parts)
    if base not in bases:
        return dual
    return " / ".join(p if p.endswith(" (V)") else f"{p} (V)" for p in parts)


def merge_set(sid: str, listed: list[dict], by_url: dict, by_title: dict) -> list[dict]:
    used = set()
    merged = []
    bases = decipher_objective_bases() if sid in LEGACY_IDS else set()
    for row in listed:
        obj_title = None
        if row.get("type") == "Objective" and " / " in (row.get("title") or ""):
            obj_title = row["title"]
            if sid in LEGACY_IDS:
                obj_title = legacy_objective_title(obj_title, bases)
        c = by_url.get(row["url"])
        if c is None and sid in CURRENT_IDS:
            c = by_title.get((sid, row["side"], row["title"].lower()))
        if c is not None:
            used.add(id(c))
            card = dict(c)
            card["set"] = sid
            card["side"] = row["side"]
            card["rarity"] = card.get("rarity") or row["rarity"]
            front = dict(card.get("front") or {})
            if obj_title:
                front["title"] = obj_title
            if not front.get("imageUrl"):
                front["imageUrl"] = row["url"]
            if not front.get("type"):
                front["type"] = row["type"]
            if not front.get("subType") and row["subType"]:
                front["subType"] = row["subType"]
            if row["back_url"] and not card.get("back"):
                card["back"] = {"imageUrl": row["back_url"]}
            card["front"] = front
            merged.append(card)
            continue
        front = {
            "title": obj_title if obj_title else (row["title_raw"] or row["title"]),
            "type": row["type"],
            "subType": row["subType"],
            "imageUrl": row["url"],
            "gametext": "",
            "lore": "",
            "uniqueness": row["uniqueness"],
            "icons": [],
        }
        card = {
            "gempId": f"pc|{sid}|{row['side']}|{stem_of(row['url'])}",
            "set": sid,
            "side": row["side"],
            "rarity": row["rarity"],
            "legacy": sid in LEGACY_IDS,
            "front": front,
        }
        if row["back_url"]:
            card["back"] = {"imageUrl": row["back_url"]}
        merged.append(card)
    for c in by_title.values():
        if str(c.get("set")) != sid:
            continue
        if id(c) in used:
            continue
        extra = dict(c)
        extra["set"] = sid
        merged.append(extra)
    return merged


def seed_occupied() -> set[str]:
    occ = set(grc.seed_occupied())
    if MAP_PATH.exists():
        dests = json.loads(MAP_PATH.read_text(encoding="utf-8"))
        virt_ids = set(SET_NAME)
        occ.update(
            v
            for k, v in dests.items()
            if k.split("|", 1)[0] not in virt_ids
        )
    remaining = ROOT / "pages" / "remaining" / "index.tsv"
    if remaining.exists():
        for line in remaining.read_text(encoding="utf-8").splitlines():
            if line.strip():
                parts = line.split("\t")
                if len(parts) >= 2:
                    occ.add(parts[1])
    occ.update(SET_NAME.values())
    occ.update(
        {
            "Cancelled Expansions",
            "Current Virtual Sets",
            "Virtual Legacy",
            "Virtual Master",
            "Set 0",
            "Set D",
            "Set P",
            "Mission",
        }
    )
    return occ


def assign_titles(cards_by_set: dict[str, list[dict]], dests: dict) -> dict[str, str]:
    occ = seed_occupied() | set(dests.values())
    gid_to_page = {}
    for sid, _name, *_ in ALL_SETS:
        bucket = list(cards_by_set.get(sid) or [])
        bucket.sort(key=lambda c: (0 if c.get("side") == "Light" else 1, printed_title((c.get("front") or {}).get("title") or "").lower()))
        for c in bucket:
            t = printed_title((c.get("front") or {}).get("title") or "")
            if not t:
                continue
            side = c.get("side") or "Light"
            uid = unique_id(c)
            page = t
            if t in occ:
                if side == "Dark":
                    cand = f"{t} (Dark)"
                    if cand not in occ:
                        page = cand
                    else:
                        page = f"{t} ({SET_NAME[sid]})"
                else:
                    page = f"{t} ({SET_NAME[sid]})"
            n = 2
            base = page
            while page in occ:
                page = f"{base} ({n})"
                n += 1
            occ.add(page)
            gid_to_page[uid] = page
            dests[f"{sid}|{side}|{t}"] = page
    return gid_to_page


def unique_id(c: dict) -> str:
    gid = c.get("gempId") or ""
    url = ((c.get("front") or {}).get("imageUrl") or "")
    stem = stem_of(url) if url else ""
    t = printed_title((c.get("front") or {}).get("title") or "")
    if gid and not gid.startswith("pc|"):
        return f"{gid}|{stem or t}"
    return gid or f"{c.get('set')}|{c.get('side')}|{stem or t}"


def strip_v_faces(t: str) -> str:
    """Strip a trailing (V) from each face of a dual-title objective."""
    return " / ".join(re.sub(r" \(V\)$", "", p.strip()) for p in t.split(" / "))


def virt_hatnote(c: dict, page: str, dests: dict) -> str:
    t = printed_title((c.get("front") or {}).get("title") or "")
    side = c.get("side") or "Light"
    sid = str(c.get("set"))
    notes = []
    other = "Dark" if side == "Light" else "Light"
    other_page = dests.get(f"{sid}|{other}|{t}")
    if other_page:
        notes.append(f"For the {other} Side card, see [[{other_page}]].")
    bare = strip_v_faces(t)
    for tag in (" (Holo AI)", " (C-Slip AI)", " (ALT)", " (AI)"):
        if bare.endswith(tag):
            bare = bare[: -len(tag)]
    decipher_dest = None
    current_dest = None
    for key, dest in dests.items():
        parts = key.split("|", 2)
        if len(parts) != 3:
            continue
        ksid, kside, kt = parts
        if kside != side or dest == page:
            continue
        kt_bare = strip_v_faces(kt)
        if kt_bare != bare and kt != bare:
            continue
        if ksid not in SET_NAME:
            if decipher_dest is None:
                decipher_dest = dest
        elif ksid in CURRENT_IDS and current_dest is None:
            current_dest = dest
    if decipher_dest:
        notes.append(f"For the Decipher card, see [[{decipher_dest}]].")
    if sid in LEGACY_IDS and current_dest:
        notes.append(f"For the current virtual card, see [[{current_dest}]].")
    return " ".join(notes)


def virt_sources(c: dict, set_name: str) -> str:
    sid = str(c.get("set"))
    slug = SET_SLUG[sid]
    t = printed_title((c.get("front") or {}).get("title") or "")
    side = c.get("side") or "Light"
    url = CARDLIST.format(slug=slug)
    lines = [
        f"* [{url} {set_name} card list] at res.starwarsccg.org",
        f"* [{SLIPS} Virtual slips] at starwarsccg.org — {side}: {t}",
    ]
    if c.get("gempId") and not str(c.get("gempId")).startswith("pc|"):
        q = urllib.request.quote(t)
        lines.append(f"* [{SCOMP_UI}/?s={q} Scomp Link Access]")
    return "\n".join(lines)


def prepare_grc() -> None:
    for sid, name, pref, *_ in ALL_SETS:
        grc.SET_NAME[sid] = name
        grc.SET_PREFIX[sid] = pref
    grc.SKIP_ICON.update(SKIP_SET_ICONS)


def card_table(cards: list[dict], prefix: str, fetch_art: bool) -> str:
    grouped = defaultdict(list)
    for c in cards:
        front = c.get("front") or {}
        title = printed_title(front.get("title") or "")
        if not title:
            continue
        side = c.get("side") or "Light"
        typ = gsl.norm_type(front.get("type") or "")
        sid = str(c.get("set") or "")
        dest = gsl.title_map().get(f"{sid}|{side}|{title}") or title
        if typ == "Objective":
            gtext = front.get("gametext") or ""
            labels = gsl.split_objective_sides(title, gtext or "")
            faces = [front]
            if c.get("back"):
                faces.append(c["back"])
            for i, face in enumerate(faces):
                url = face.get("imageUrl") or front.get("imageUrl") or ""
                fname = wiki_image(prefix, side, url) if url else ""
                if fetch_art and url and fname:
                    download(url, ART / fname)
                text = labels[i][1] if i < len(labels) else ""
                grouped[(side, typ)].append(
                    {
                        "title": title,
                        "wiki": dest,
                        "label": gsl.decipher_objective_name(title),
                        "file": fname,
                        "rarity": c.get("rarity") or "",
                        "destiny": face.get("destiny") or ("0" if i == 0 else "7"),
                        "gtext": gsl.wiki_escape(text),
                        "type": "Objective",
                    }
                )
            continue
        url = front.get("imageUrl") or ""
        fname = wiki_image(prefix, side, url) if url else ""
        if fetch_art and url and fname:
            download(url, ART / fname)
        grouped[(side, typ)].append(
            {
                "title": title,
                "wiki": dest,
                "label": title,
                "file": fname,
                "rarity": c.get("rarity") or "",
                "destiny": front.get("destiny") or "",
                "gtext": gsl.wiki_escape(front.get("gametext") or ""),
                "type": typ,
            }
        )
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
            page = gsl.TYPE_PAGE.get(t, t)
            lines.append(f"==== [[{page}]] ====")
            lines.append('{| class="wikitable card-thumbs"')
            lines.append("! Image !! Card !! Type !! Rarity !! Destiny !! Game text")
            for r in rows:
                dest = r.get("wiki") or r["title"]
                img = f"[[File:{r['file']}|200px|link={dest}]]" if r["file"] else ""
                label = r.get("label") or r["title"]
                card = f"[[{dest}|{label}]]" if label != dest else f"[[{dest}]]"
                page = gsl.TYPE_PAGE.get(r["type"], r["type"])
                lines.append("|-")
                lines.append(
                    f"| {img} || {card} || [[{page}|{r['type']}]] || {r['rarity']} || {r['destiny']} || {r['gtext']}"
                )
            lines.append("|}")
            lines.append("")
    return "\n".join(lines) + "\n"


def hub_page(sid: str, cards: list[dict], thumbs: str) -> str:
    name = SET_NAME[sid]
    date = SET_DATE[sid] or "Players Committee virtual era"
    banner = SET_BANNER[sid]
    ext = banner.split(".")[-1]
    image = f"Set-{SET_PREFIX[sid]}-title.{ext}"
    n = len(cards)
    slug = SET_SLUG[sid]
    list_url = CARDLIST.format(slug=slug)
    if sid in LEGACY_IDS:
        publisher = "Star Wars CCG Players Committee"
        lead = (
            f"'''{name}''' is a Players Committee '''legacy''' virtual expansion "
            f"(2002–2014). These cards are no longer valid for competitive play; "
            f"use the Decipher sets and the current virtual sets (2014 Reset onward)."
        )
        more = (
            "The Players Committee published virtual cards from 2002 until the 2014 Reset. "
            "After the Reset, the earlier cards were reorganized into Virtual Blocks 1–9 "
            "plus Virtual Shields. The combined legacy list is also published as "
            "Virtual Master on the Players Committee cardlists."
        )
        cat = "[[Category:Virtual Legacy sets]]"
    else:
        publisher = "Star Wars CCG Players Committee"
        released = f" It was released {date}." if SET_DATE[sid] else ""
        lead = (
            f"'''{name}''' is a Players Committee virtual expansion from the 2014 Reset onward."
            f"{released} These are not Decipher cards."
        )
        more = (
            "Current virtual cards are maintained by the Star Wars CCG Players Committee. "
            "Printable slips are published with each set."
        )
        cat = "[[Category:Current Virtual sets]]"
    infobox = f"""{{| class="wikitable expansion-infobox"
! colspan="2" | {name}
|-
| colspan="2" style="text-align:center;" | [[File:{image}|260px]]
|-
! Game/Set
| Star Wars CCG
|-
! Expansion
| {name}
|-
! Publisher
| {publisher}
|-
! Date
| {date}
|-
! Cards Total
| {n}
|-
! Card Size
| 63x88mm
|}}
"""
    return (
        infobox
        + f"""
{lead}

{more}

{thumbs}
== Sources ==
* [{list_url} {name} card list] at res.starwarsccg.org
* [{SLIPS} Virtual slips] at starwarsccg.org

{cat}
[[Category:Sets]]
"""
    )


def tile_line(sid: str, n: int) -> str:
    name = SET_NAME[sid]
    date = SET_DATE[sid]
    pref = SET_PREFIX[sid]
    banner = SET_BANNER[sid]
    ext = banner.split(".")[-1]
    image = f"Set-{pref}-title.{ext}"
    meta = f"{date} · {n}" if date else str(n)
    return (
        f'<div class="set-tile">[[File:{image}|142px|link={name}]]'
        f'<span class="set-name">[[{name}]]</span>'
        f'<span class="set-meta">{meta}</span></div>'
    )


def write_xml(pages: list[tuple[str, str]], dest: Path) -> None:
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
    dest.write_text("\n".join(parts), encoding="utf-8")


def main(fetch_art: bool = True):
    prepare_grc()
    extras._CACHE = None
    extras._LINKER = None
    extras._STAR_CACHE = None
    print("loading scomp virtual", flush=True)
    scomp = load_scomp_virtual()
    by_url, by_title = scomp_index(scomp)
    print("scomp virtual", len(scomp), flush=True)
    cards_by_set = {}
    for sid, name, pref, date, slug, banner in ALL_SETS:
        print("cardlist", slug, flush=True)
        listed = load_cardlist(slug)
        merged = merge_set(sid, listed, by_url, by_title)
        cards_by_set[sid] = merged
        print(" ", name, "listed", len(listed), "merged", len(merged), flush=True)

    if fetch_art:
        prefetch_art(cards_by_set)

    dests = {}
    if MAP_PATH.exists():
        raw_map = json.loads(MAP_PATH.read_text(encoding="utf-8"))
        virt_ids = set(SET_NAME)
        dests = {
            k: v
            for k, v in raw_map.items()
            if k.split("|", 1)[0] not in virt_ids
        }
    gid_pages = assign_titles(cards_by_set, dests)
    MAP_PATH.write_text(json.dumps(dests, indent=0, ensure_ascii=False), encoding="utf-8")
    gsl._TITLE_MAP = dests

    OUT_PAGES.mkdir(parents=True, exist_ok=True)
    OUT_HUBS.mkdir(parents=True, exist_ok=True)
    OUT_LISTS.mkdir(parents=True, exist_ok=True)

    xml_pages = []
    written = []
    occ_alias = seed_occupied() | set(gid_pages.values())
    index_rows = []
    used_gids = set()

    for sid, name, pref, date, slug, banner in ALL_SETS:
        cards = cards_by_set[sid]
        print("pages", name, len(cards), flush=True)
        thumbs = card_table(cards, pref, False)
        list_fn = re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_") + ".wiki"
        (OUT_LISTS / list_fn).write_text(thumbs, encoding="utf-8")
        hub = hub_page(sid, cards, thumbs)
        (OUT_HUBS / list_fn).write_text(hub, encoding="utf-8")
        xml_pages.append((name, hub))
        short = name.replace("Virtual ", "")
        if short != name and short not in occ_alias:
            xml_pages.append((short, f"#REDIRECT [[{name}]]\n"))
            occ_alias.add(short)

        by_side = defaultdict(list)
        for c in cards:
            by_side[c.get("side") or "Light"].append(c)
        for side in ("Light", "Dark"):
            group = by_side.get(side) or []
            group.sort(key=lambda c: printed_title((c.get("front") or {}).get("title") or "").lower())
            titles = [
                gid_pages.get(unique_id(c), printed_title((c.get("front") or {}).get("title") or ""))
                for c in group
            ]
            for i, c in enumerate(group):
                uid = unique_id(c)
                page = gid_pages.get(uid, printed_title((c.get("front") or {}).get("title") or ""))
                prev = titles[i - 1] if i else ""
                nxt = titles[i + 1] if i + 1 < len(titles) else ""
                sources = virt_sources(c, name)
                text = grc.page_for(
                    c,
                    page,
                    prev,
                    nxt,
                    dests,
                    set_band="Virtual",
                    sources=sources,
                    hatnote=virt_hatnote(c, page, dests),
                    version_label="virtual",
                )
                fn = re.sub(r"[^A-Za-z0-9._-]+", "_", uid) + ".wiki"
                (OUT_PAGES / fn).write_text(text, encoding="utf-8")
                xml_pages.append((page, text))
                gid = c.get("gempId") or ""
                tpage = printed_title((c.get("front") or {}).get("title") or "")
                variant = any(tag in tpage for tag in ("(AI)", "(ALT)", "(Holo AI)", "(C-Slip AI)"))
                if gid and not gid.startswith("pc|") and gid not in used_gids and not variant:
                    xml_pages.append((f"Card:{gid}", f"#REDIRECT [[{page}]]\n"))
                    used_gids.add(gid)
                written.append(page)
                index_rows.append(f"{uid}\t{page}\t{fn}\t{side}\t{sid}")

    (OUT_PAGES / "index.tsv").write_text("\n".join(index_rows) + "\n", encoding="utf-8")
    write_xml(xml_pages, ROOT / "virtual-cards.xml")

    # Main Page fragments
    legacy_tiles = "\n".join(tile_line(sid, len(cards_by_set[sid])) for sid, *_ in LEGACY)
    current_tiles = "\n".join(tile_line(sid, len(cards_by_set[sid])) for sid, *_ in CURRENT)
    (ROOT / "pages" / "main-virtual-legacy.wiki").write_text(legacy_tiles + "\n", encoding="utf-8")
    (ROOT / "pages" / "main-virtual-current.wiki").write_text(current_tiles + "\n", encoding="utf-8")
    main_path = ROOT / "pages" / "Main_Page.wiki"
    if main_path.exists():
        main = main_path.read_text(encoding="utf-8")
        main = main.replace("<!--VIRTUAL_LEGACY_TILES-->", legacy_tiles)
        main = main.replace("<!--VIRTUAL_CURRENT_TILES-->", current_tiles)
        main_path.write_text(main, encoding="utf-8")

    counts = {sid: len(cards_by_set[sid]) for sid, *_ in ALL_SETS}
    (ROOT / "virtual-set-counts.json").write_text(json.dumps(counts, indent=2), encoding="utf-8")
    print("wrote", len(written), "card pages")
    print("xml", (ROOT / "virtual-cards.xml").stat().st_size)
    print("art", len(list(ART.glob("V*.gif"))) if ART.exists() else 0)


if __name__ == "__main__":
    fetch_art = "--no-fetch" not in sys.argv
    main(fetch_art=fetch_art)
