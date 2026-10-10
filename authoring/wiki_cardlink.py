#!/usr/bin/env python3
"""Wiki decklist hover: {{CardLink|dest|File.gif}}.

Template:CardLink wraps span.swccg-card-link; MediaWiki:Common.js bindCardLinks
shows File: art on hover. That is wiki card-image hover, not Phase 3 GEMP hover.

Requires an existing File: for the image argument. Fall back to [[dest]] when
no File mapping exists.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

# Decipher unique-card File: prefixes (same as generate_remaining_cards.SET_PREFIX).
SET_PREFIX: dict[str, str] = {
    "1": "Premiere",
    "2": "ANH",
    "3": "Hoth",
    "4": "Dagobah",
    "5": "CC",
    "6": "JP",
    "7": "SE",
    "8": "Endor",
    "9": "DS2",
    "10": "Ref2",
    "11": "Tat",
    "12": "Cor",
    "13": "Ref3",
    "14": "Theed",
    "101": "P2P",
    "102": "Jedi",
    "103": "RL",
    "104": "ESB2P",
    "106": "OTSD",
    "108": "EP",
    "109": "ECC",
    "110": "EJP",
    "111": "TA",
    "112": "JPSD",
}
# Current virtual + Legacy Virtual Block (generate_virtual.SET_PREFIX).
for _sid, _pref in (
    ("200", "V0"),
    ("201", "V1"),
    ("202", "V2"),
    ("203", "V3"),
    ("204", "V4"),
    ("205", "V5"),
    ("206", "V6"),
    ("207", "V7"),
    ("208", "V8"),
    ("209", "V9"),
    ("210", "V10"),
    ("211", "V11"),
    ("212", "V12"),
    ("213", "V13"),
    ("214", "V14"),
    ("215", "V15"),
    ("216", "V16"),
    ("217", "V17"),
    ("218", "V18"),
    ("219", "V19"),
    ("220", "V20"),
    ("221", "V21"),
    ("222", "V22"),
    ("223", "V23"),
    ("224", "V24"),
    ("225", "V25"),
    ("226", "V26"),
    ("227", "V27"),
    ("vb1", "VB1"),
    ("vb2", "VB2"),
    ("vb3", "VB3"),
    ("vb4", "VB4"),
    ("vb5", "VB5"),
    ("vb6", "VB6"),
    ("vb7", "VB7"),
    ("vb8", "VB8"),
    ("vb9", "VB9"),
    ("vsh", "VSh"),
    ("setd", "VD"),
    ("301", "VP"),
):
    SET_PREFIX[_sid] = _pref

# PC Type.html slug → scomp-style set id (generate_virtual.ALL_SETS).
_PC_SLUG_SET = {
    "Set0": "200",
    "SetD": "setd",
    "SetP": "301",
    "VShields": "vsh",
}
for _n in range(1, 28):
    _PC_SLUG_SET[f"Set{_n}"] = str(200 + _n)
for _n in range(1, 10):
    _PC_SLUG_SET[f"VBlock{_n}"] = f"vb{_n}"

_UNI = re.compile(r"^[•♦○*<>]+\s*|[•♦○]")
_VB = re.compile(r" \(Virtual Block \d+\)$")
_VSH = re.compile(r" \(Virtual Shields\)$")
_DARK = re.compile(r" \(Dark\)$")
_CARDLINK = re.compile(
    r"\{\{CardLink\|([^}|]+)\|([^}|]+)(?:\|label=([^}]+))?\}\}"
)
_WIKILINK = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")

_INDEX: dict[tuple[str, str], list[dict]] | None = None


def norm_side(side: str) -> str:
    s = (side or "").strip().upper()
    if s in {"L", "LS", "LIGHT"}:
        return "Light"
    if s in {"D", "DS", "DARK"}:
        return "Dark"
    if s in {"LIGHT", "DARK"}:
        return s.title()
    if side in {"Light", "Dark"}:
        return side
    return side.title() if side else ""


def strip_uniqueness(title: str) -> str:
    return _UNI.sub("", title or "").strip()


def lookup_key(title: str) -> str:
    t = strip_uniqueness(title)
    t = _VB.sub("", t)
    t = _VSH.sub("", t)
    t = _DARK.sub("", t)
    t = re.sub(r"\s+", " ", t).strip()
    return t


def wiki_file_name(card: dict) -> str | None:
    front = card.get("front") or {}
    url = front.get("imageUrl") or ""
    if not url:
        return None
    stem = url.split("/")[-1].split("?")[0]
    if not stem:
        return None
    letter = "L" if card.get("side") == "Light" else "D"
    sid = str(card.get("set") or "")
    pref = SET_PREFIX.get(sid, "X")
    if sid == "1":
        return f"Premiere-{letter}-{stem}"
    if (pref.startswith("VB") or pref == "VSh") and stem.endswith(".gif") and not stem.endswith("-pre.gif"):
        stem = stem[:-4] + "-pre.gif"
    return f"{pref}-{letter}-{stem}"


def _index_card(out: dict[tuple[str, str], list[dict]], card: dict) -> None:
    side = card.get("side") or ""
    front = card.get("front") or {}
    title = strip_uniqueness(front.get("title") or "")
    if not title or not side:
        return
    keys = {title, lookup_key(title)}
    if " / " in title:
        keys.add(title.split(" / ", 1)[0])
    if "/" in title and " / " not in title:
        keys.add(title.split("/", 1)[0].strip())
    for k in keys:
        if not k:
            continue
        out.setdefault((side, k.casefold()), []).append(card)


def _pc_cardlists() -> list[dict]:
    """Virtual cards missing from scomp JSON (later sets + Virtual Blocks)."""
    cache = ROOT / "pc-cardlists"
    if not cache.is_dir():
        return []
    try:
        import generate_virtual as gv
    except Exception:
        return []
    out: list[dict] = []
    for sid, _n, _pref, _d, slug, *_ in gv.ALL_SETS:
        path = cache / f"{slug}Type.html"
        if not path.exists() or path.stat().st_size < 500:
            continue
        for row in gv.parse_cardlist(path.read_text(encoding="utf-8")):
            url = row.get("url") or ""
            title = row.get("title") or ""
            side = row.get("side") or ""
            if not url or not title or not side:
                continue
            out.append(
                {
                    "side": side,
                    "set": sid,
                    "legacy": bool(str(sid).startswith("vb") or sid == "vsh"),
                    "front": {"title": title, "imageUrl": url},
                }
            )
    return out


def _load_index() -> dict[tuple[str, str], list[dict]]:
    global _INDEX
    if _INDEX is not None:
        return _INDEX
    out: dict[tuple[str, str], list[dict]] = {}
    for name in ("scomp-Light.json", "scomp-Dark.json"):
        path = ROOT / name
        if not path.exists():
            continue
        blob = json.loads(path.read_text(encoding="utf-8"))
        cards = blob.get("cards") if isinstance(blob, dict) else blob
        for c in cards or []:
            _index_card(out, c)
    for c in _pc_cardlists():
        _index_card(out, c)
    _INDEX = out
    return _INDEX


def _set_num(sid: str) -> int:
    if sid.isdigit():
        return int(sid)
    return 10000


def _set_rank(card: dict, prefer_legacy: bool) -> tuple:
    sid = str(card.get("set") or "")
    n = _set_num(sid)
    legacy = bool(card.get("legacy"))
    vb = sid.startswith("vb") or sid == "vsh"
    virt_cur = n >= 200
    printed = sid.isdigit() and n < 200
    if prefer_legacy:
        return (0 if vb else 1, 0 if legacy else 1, 0 if printed else 1, n, sid)
    return (0 if printed else 1, 0 if (not virt_cur and not vb) else 1, 0 if not legacy else 1, n, sid)


def image_for(title: str, side: str, prefer_legacy: bool = False) -> str | None:
    """Return wiki File: basename for a printed/GEMP title on that side, or None."""
    side_n = norm_side(side)
    key = lookup_key(title)
    if not key or not side_n:
        return None
    idx = _load_index()
    cands = list(idx.get((side_n, key.casefold()), []))
    if not cands and " / " in key:
        cands = list(idx.get((side_n, key.split(" / ", 1)[0].casefold()), []))
    if not cands:
        return None
    cands.sort(key=lambda c: _set_rank(c, prefer_legacy))
    return wiki_file_name(cands[0])


def cardlink(dest: str, image: str | None, label: str | None = None) -> str:
    dest = (dest or "").strip()
    if not dest:
        return "—"
    vis = (label or "").strip()
    if not image:
        if vis and vis != dest:
            return f"[[{dest}|{vis}]]"
        return f"[[{dest}]]"
    if not vis or vis == dest:
        return f"{{{{CardLink|{dest}|{image}}}}}"
    return f"{{{{CardLink|{dest}|{image}|label={vis}}}}}"


def wrap(title: str, side: str, dest: str | None = None, label: str | None = None) -> str:
    """Emit CardLink for a GEMP/wiki printed title."""
    dest_s = (dest or title or "").strip()
    vis = label
    if vis is None and dest_s and " / " in dest_s and dest_s != title:
        vis = dest_s.split(" / ", 1)[0]
    prefer = "Virtual Block" in dest_s or "Virtual Shields" in dest_s
    img = image_for(title or dest_s, side, prefer_legacy=prefer)
    if not img and dest_s != title:
        img = image_for(dest_s, side, prefer_legacy=prefer)
    return cardlink(dest_s, img, vis)


def strip_markup_title(text: str) -> str:
    """Visible/dest title from CardLink or [[link]] wikitext."""
    text = (text or "").strip()
    m = _CARDLINK.search(text)
    if m:
        return (m.group(3) or m.group(1)).strip()
    m = _WIKILINK.search(text)
    if m:
        return (m.group(2) or m.group(1)).strip()
    return text


def _alt_titles(title: str) -> list[str]:
    t = lookup_key(title)
    out = [t]
    if "Wan " in t or t.startswith("Obi Wan"):
        out.append(t.replace("Obi Wan", "Obi-Wan"))
    if t.endswith("!"):
        out.append(t.rstrip("!").strip())
    # Title-case particles that GEMP stores capitalized.
    if " to " in t or " of " in t or " is " in t:
        out.append(
            t.replace(" to ", " To ")
            .replace(" of ", " Of ")
            .replace(" is ", " Is ")
            .replace(" with ", " With ")
            .replace(" the ", " The ")
        )
    if "Millenium" in t:
        out.append(t.replace("Millenium", "Millennium"))
    if "Nar Shadaa" in t:
        out.append(t.replace("Nar Shadaa", "Nar Shaddaa"))
    if t == "Professor (V)":
        out.append("The Professor (V)")
    if t == "Jabba's Prize (V)":
        out.append("Jabba's Prize")
    if t == "Yavin 4: War Room (V)":
        out.append("Yavin 4: Massassi War Room (V)")
    seen = []
    for x in out:
        if x and x not in seen:
            seen.append(x)
    return seen


def lookup_image(title: str, side: str, prefer_legacy: bool = False) -> str | None:
    img = image_for(title, side, prefer_legacy=prefer_legacy)
    if img:
        return img
    for alt in _alt_titles(title):
        if alt == lookup_key(title):
            continue
        img = image_for(alt, side, prefer_legacy=prefer_legacy)
        if img:
            return img
    other = "Dark" if norm_side(side) == "Light" else "Light"
    img = image_for(title, other, prefer_legacy=prefer_legacy)
    if img:
        return img
    for alt in _alt_titles(title):
        img = image_for(alt, other, prefer_legacy=prefer_legacy)
        if img:
            return img
    return None


def replace_wikilink(match: re.Match, side: str, prefer_legacy: bool = False) -> str:
    dest = (match.group(1) or "").strip()
    label = (match.group(2) or "").strip() or None
    if dest.startswith("File:") or dest.startswith("Media:") or dest.startswith("Category:"):
        return match.group(0)
    if dest.startswith(":") or dest.startswith("*"):
        return match.group(0)
    prefer = (
        prefer_legacy
        or "Virtual Block" in dest
        or "Virtual Shields" in dest
    )
    img = lookup_image(dest, side, prefer_legacy=prefer)
    if not img and label:
        img = lookup_image(label, side, prefer_legacy=prefer)
    if not img:
        return match.group(0)
    return cardlink(dest, img, label)


def convert_deck_wikitext(text: str, side: str, prefer_legacy: bool | None = None) -> str:
    """Rewrite Starting Card + Decklist [[links]] to CardLink. Leave other sections."""
    if prefer_legacy is None:
        prefer_legacy = "[[Legacy Open]]" in text or "Virtual Block" in text

    def convert_chunk(chunk: str) -> str:
        return _WIKILINK.sub(
            lambda m: replace_wikilink(m, side, prefer_legacy=prefer_legacy),
            chunk,
        )

    out = text
    out = re.sub(
        r"^(\* '''Starting Card:''' )(.+)$",
        lambda m: m.group(1) + convert_chunk(m.group(2)),
        out,
        count=1,
        flags=re.M,
    )
    m = re.search(r"(== Decklist ==\n)(.*?)(?=\n== |\Z)", out, flags=re.S)
    if m:
        body = convert_chunk(m.group(2))
        out = out[: m.start(2)] + body + out[m.end(2) :]
    return out


def infer_side_from_page(text: str, title: str = "") -> str:
    m = re.search(r"\* '''Side:'''\s*\[\[(Light|Dark)\]\]", text)
    if m:
        return m.group(1)
    if title.endswith(" LS") or title.endswith("_LS") or " LS " in title:
        return "Light"
    if title.endswith(" DS") or title.endswith("_DS") or " DS " in title:
        return "Dark"
    if re.search(r"\bLight Side\b", text[:400]):
        return "Light"
    if re.search(r"\bDark Side\b", text[:400]):
        return "Dark"
    return ""


# ---------------------------------------------------------------- Defensive Shields (2026-10-10)
# Decipher printed Defensive Shields only in Reflections III. Most share a name with an older
# Effect (Battle Plan, Aim High, Your Insight Serves You Well, Resistance, ...), and the plain-name
# wiki page is that older card. A "Defensive Shields" section must link the shield page, which the
# wiki titles "X (Reflections III: A Collector's Bounty)" or "X (Light|Dark)"; shields printed only
# in Reflections III keep the plain name. Looked up live (cached) so new pages are found.
REF3 = "Reflections III: A Collector's Bounty"
_SHIELD_CACHE: dict[str, str | None] = {}


def _wiki_raw(title: str) -> str:
    import urllib.parse
    import urllib.request
    url = "https://wiki.swccg.com/index.php?" + urllib.parse.urlencode({"title": title, "action": "raw"})
    req = urllib.request.Request(url, headers={"User-Agent": "swccg-wiki-dest/1.0 (shield links)"})
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            return r.read().decode("utf-8")
    except Exception:  # noqa: BLE001 - missing page = 404
        return ""


def shield_page(name: str, side: str) -> tuple[str, str] | None:
    """(page title, image) of the Reflections III Defensive Shield `name` for side Light|Dark."""
    side = "Dark" if side.upper().startswith("D") else "Light"
    for page in (f"{name} ({REF3})", f"{name} ({side})", name):
        if page not in _SHIELD_CACHE:
            txt = _wiki_raw(page)
            ok = "type=Defensive Shield" in txt and f"side={side}" in txt and f"set={REF3}" in txt
            m = re.search(r"^\|image=(.+)$", txt, re.M)
            _SHIELD_CACHE[page] = m.group(1).strip() if ok and m else None
        if _SHIELD_CACHE[page]:
            return page, _SHIELD_CACHE[page]
    return None


def fix_shield_section(text: str) -> str:
    """Point every card link inside a 'Defensive Shields' section ({{CardLink}} or [[link]]) at the
    Reflections III shield page. Other sections are untouched."""
    out, pos = [], 0
    for m in re.finditer(r"^(=+) *Defensive Shields *\1[ \t]*$", text, re.M):
        if m.start() < pos:
            continue
        level = len(m.group(1))
        nxt = re.search(rf"^={{1,{level}}}[^=]", text[m.end():], re.M)
        stop = m.end() + (nxt.start() if nxt else len(text) - m.end())
        out.append(text[pos:m.end()])
        out.append(_fix_shields_in(text[m.end():stop]))
        pos = stop
    out.append(text[pos:])
    return "".join(out)


def _shield_any_side(name: str, side_hint: str | None) -> tuple[str, str] | None:
    if side_hint:
        return shield_page(name, side_hint)
    hits = [h for h in (shield_page(name, "Light"), shield_page(name, "Dark")) if h]
    return hits[0] if len(hits) == 1 else None


def _fix_shields_in(section: str) -> str:
    def card(cm: re.Match) -> str:
        dest, img, label = cm.group(1).strip(), cm.group(2).strip(), (cm.group(3) or "").strip()
        name = label or dest
        if "(V)" in name or REF3 in dest:
            return cm.group(0)
        hit = _shield_any_side(name, "Dark" if "-D-" in img else "Light" if "-L-" in img else None)
        return cardlink(hit[0], hit[1], name) if hit and hit[0] != dest else cm.group(0)

    def link(lm: re.Match) -> str:
        dest, label = lm.group(1).strip(), (lm.group(2) or "").strip()
        if dest.startswith(("File:", "Category:", ":")) or "(V)" in dest or REF3 in dest:
            return lm.group(0)
        hit = _shield_any_side(dest, None)
        return f"[[{hit[0]}|{label or dest}]]" if hit and hit[0] != dest else lm.group(0)

    section = re.sub(r"\{\{CardLink\|([^|}]+)\|([^|}]+)(?:\|label=([^}]+))?\}\}", card, section)
    return re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", link, section)
