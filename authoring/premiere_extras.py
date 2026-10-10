#!/usr/bin/env python3
"""Scomp rulings + Decipher starred strategy notes for every Decipher set."""
from __future__ import annotations

import json
import re
import time
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
UA = {"User-Agent": "Mozilla/5.0 SWCCGWiki/1.0"}
SCOMP_GH = "https://github.com/swccgpc/swccg-scomp"
SCOMP_JSON = "https://github.com/swccgpc/swccg-card-json"
ARCHIVE_LS = "https://web.archive.org/web/20020611184117/http://www.decipher.com/starwars/cardlists/premiere/light/"
ARCHIVE_DS = "https://web.archive.org/web/20020611184117/http://www.decipher.com/starwars/cardlists/premiere/dark/"

_CACHE = None


def wiki_escape(s: str) -> str:
    s = s.replace("&nbsp;", " ")
    s = re.sub(r"<u>(.*?)</u>", r"''\1''", s, flags=re.I | re.S)
    s = re.sub(r"<[^>]+>", "", s)
    s = s.replace("|", "{{!}}")
    # Remaining "<" is game text ("attrition < 5"), not HTML. Do this after
    # tag strip; "&lt;" has no "<" character so it is not double-encoded.
    s = s.replace("<", "&lt;")
    s = re.sub(r"[ \t]+", " ", s)
    return s.strip()


CONCEPT_PAGES = {
    "Interrupt",
    "Used Interrupt",
    "Lost Interrupt",
    "Effect",
    "Utinni Effect",
    "Character",
    "Device",
    "Weapon",
    "Starship",
    "Vehicle",
    "Location",
    "Site",
    "System",
    "Light",
    "Dark",
    "Rebel",
    "Imperial",
    "Alien",
    "Droid",
}

NICK_STOP = {
    "force",
    "station",
    "interrupt",
    "effect",
    "field",
    "deck",
    "site",
    "system",
    "starship",
    "fighter",
    "trooper",
    "farm",
    "mine",
    "tube",
    "cannon",
    "rifle",
    "blaster",
    "droid",
    "guard",
    "pilot",
    "scout",
    "crew",
    "barrier",
    "assault",
    "maneuvers",
    "resources",
    "terminal",
    "conversation",
    "damage",
    "weapon",
    "device",
    "location",
    "character",
    "vehicle",
    "the",
    "of",
    "and",
}

# Colloquial Decipher-extra names → printed title. Side-specific dest is
# resolved later (Sense vs Sense (Dark)).
EXPLICIT_NICKS = {
    "Tarkin": "Grand Moff Tarkin",
    "Vader": "Darth Vader",
    "Luke": "Luke Skywalker",
    "Leia": "Leia Organa",
    "Han": "Han Solo",
    "Chewie": "Chewbacca",
    "Kenobi": "Obi-Wan Kenobi",
    "Obi-Wan": "Obi-Wan Kenobi",
    "Falcon": "Millennium Falcon",
    "Tooex": "2X-3KPR (Tooex)",
    "Artoo": "R2-D2",
    "Threepio": "C-3PO",
    "Cantina": "Tatooine: Cantina",
}

# Scomp list fields that name cards (not nicknames/characteristics).
LINK_FIELDS = {
    "combos",
    "rulings",
    "pulled_by",
    "pulls",
    "canceled_by",
    "cancels",
    "matching",
    "matching_weapon",
    "counterpart",
    "underlying_card_for",
}


def _printed_title(card: dict) -> str:
    t = ((card.get("front") or {}).get("title") or "")
    return re.sub(r"^[•*]+", "", t).strip()


def _load_scomp():
    by_id = {}
    by_img = {}
    records = []
    for side in ("Light", "Dark"):
        p = ROOT / f"scomp-{side}.json"
        data = json.loads(p.read_text(encoding="utf-8"))
        cards = data["cards"] if isinstance(data, dict) else data
        for c in cards:
            front = c.get("front") or {}
            printed = re.sub(r"^[•*]+", "", (front.get("title") or "")).strip()
            records.append(
                {
                    "printed": printed,
                    "side": c.get("side") or side,
                    "set": str(c.get("set") or ""),
                    "type": front.get("type") or "",
                    "uniqueness": front.get("uniqueness") or "",
                }
            )
            gid = c.get("gempId") or ""
            if gid:
                by_id[gid] = c
            if str(c.get("set")) != "1":
                continue
            img = (front.get("imageUrl") or "")
            stem = Path(urllib.parse.urlparse(img).path).stem.lower()
            if stem:
                by_img[stem] = c
    return by_id, by_img, records


def starred_slugs(side: str) -> list[str]:
    html = (ROOT / f"decipher-premiere-{side}.html").read_text(encoding="utf-8")
    slugs = []
    for tr in re.split(r"<tr", html, flags=re.I):
        if "cardstrategy.gif" not in tr:
            continue
        m = re.search(r'href="small/([^"]+)\.html"', tr)
        if m:
            slugs.append(m.group(1).lower())
    return slugs


def _strategy_original(folder: str, side: str, slug: str, split: bool, subdir: str) -> str:
    mid = f"{folder}/{side}" if split and side in ("light", "dark") else folder
    return f"http://www.decipher.com/starwars/cardlists/{mid}/{subdir}/{slug}.html"


def fetch_strategy_html(
    side: str,
    slug: str,
    folder: str | None = None,
    split: bool = True,
    subdir: str = "small",
) -> str:
    folder = folder or "premiere"
    subdir = subdir or "small"
    # List side and scomp side can disagree (same title both sides, or a
    # combined Reflections list). Try every cached side folder for this slug.
    candidates = []
    for s in (side, "light", "dark", "both"):
        candidates.append(ROOT / "decipher-strategy" / folder / s / f"{slug}.html")
    candidates.append(ROOT / "decipher-strategy" / side / f"{slug}.html")
    for cache in candidates:
        if cache.exists() and cache.stat().st_size > 500:
            return cache.read_text(encoding="utf-8", errors="replace")
    cache.parent.mkdir(parents=True, exist_ok=True)
    original = _strategy_original(folder, side, slug, split, subdir)
    # Prefetch fills the cache. One polite id_ snapshot if a starred card
    # is missing; do not blast multiple calendar URLs (Wayback 429).
    url = f"https://web.archive.org/web/2004id_/{original}"
    h = ""
    req = urllib.request.Request(url, headers=UA)
    try:
        h = urllib.request.urlopen(req, timeout=60).read().decode("latin-1", "replace")
    except Exception as e:
        print("fail", folder, side, slug, e)
        h = ""
    if h and ("card strategy" in h.lower() or "BeginEditable" in h or "<b>" in h):
        cache.write_text(h, encoding="utf-8")
        time.sleep(0.8)
        return h
    return ""


def _archive_mailto(href: str) -> str:
    m = re.search(r"mailto:([^\"'\s]+)", href or "")
    return f"mailto:{m.group(1)}" if m else href


def _unwrap_paragraphs(text: str) -> str:
    """Keep paragraph breaks; join 1990s HTML hard-wraps inside a paragraph.

    Decipher extras are ~70-column HTML. A leftover wrap like a line that is
    only ' Add' must not stay as its own wikitext line: a leading space is
    MediaWiki preformatted text.
    """
    text = "\n".join(line.strip() for line in text.splitlines())
    paras = []
    for p in re.split(r"\n\s*\n", text):
        line = re.sub(r"\s*\n\s*", " ", p).strip()
        if line:
            paras.append(line)
    return "\n\n".join(paras)


def _format_byline(raw: str) -> str:
    mail_m = re.search(r"mailto:([^\"'\s>]+)", raw or "", re.I)
    mail = mail_m.group(1) if mail_m else ""
    vis = re.sub(r"<br\s*/?>", " ", raw or "", flags=re.I)
    vis = re.sub(r"<[^>]+>", "", vis)
    vis = re.sub(r"\s+", " ", vis).strip(" ,")
    while True:
        nxt = re.sub(r"^(By:?|From:?)\s+", "", vis, flags=re.I).strip(" ,")
        if nxt == vis:
            break
        vis = nxt
    if mail:
        vis = re.sub(r"\s*\(" + re.escape(mail) + r"\)", "", vis, flags=re.I)
        vis = vis.strip(" ,")
    rest = ""
    rm = re.search(r",?\s*((?:Gold|Red|Black|White)\s+\d+)\s*$", vis, re.I)
    if rm:
        rest = rm.group(1)
        vis = vis[: rm.start()].strip(" ,")
    name = vis.strip(" ,")
    if mail and name:
        by = f"By [mailto:{mail} {name}]"
    elif name:
        by = f"By {name}"
    elif mail:
        by = f"By [mailto:{mail} {mail}]"
    else:
        return ""
    if rest:
        by += f", {rest}"
    return by


def _extract_byline(chunk: str) -> tuple[str, str]:
    """Pull the credit line after the bold title; leave the article body."""
    tm = re.search(r"<b>.*?</b>\s*(?:<br\s*/?>)?", chunk, re.I | re.S)
    rest = chunk[tm.end() :] if tm else chunk
    # Premiere extras use <br><br> after the credit. Later sets (Tatooine)
    # wrap title+byline in <p>…</p> (`by Name <i>(email)</i>`).
    cm = re.search(
        r"^\s*((?:By:?|From)\b.*?)(?:<br\s*/?>\s*<br\s*/?>|</p>|<p\b)",
        rest,
        re.I | re.S,
    )
    if not cm:
        return "", chunk
    byline = _format_byline(cm.group(1))
    kept = rest[cm.end() :]
    if tm:
        kept = chunk[: tm.start()] + kept
    return byline, kept


def parse_strategy(html: str) -> tuple[str, str]:
    """Return (byline_wikitext, body). Byline includes name, email, and Gold #."""
    m = re.search(
        r'<!--\s*#BeginEditable\s+"cardstrategy"\s*-->(.*)<!--\s*#EndEditable\s*-->',
        html,
        re.S | re.I,
    )
    chunk = m.group(1) if m else ""
    if not chunk:
        m2 = re.search(
            r"click to enlarge(.*?)(?:TM\s*&(?:amp;)?\s*©|TERMS OF USAGE)",
            html,
            re.S | re.I,
        )
        chunk = m2.group(1) if m2 else ""
    if not chunk:
        return "", ""
    byline, chunk = _extract_byline(chunk)
    text = re.sub(r"<br\s*/?>\s*<br\s*/?>", "\n\n", chunk, flags=re.I)
    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</p>", "\n\n", text, flags=re.I)
    text = re.sub(r"<p[^>]*>", "", text, flags=re.I)
    text = re.sub(r"</blockquote>", "", text, flags=re.I)
    text = re.sub(r"<blockquote[^>]*>", "", text, flags=re.I)
    text = re.sub(r"<a [^>]*>.*?</a>", "", text, flags=re.I | re.S)
    text = re.sub(r"<b>.*?</b>", "", text, flags=re.I | re.S)
    text = re.sub(r"(?im)^(By:?|From)\s+\S.*$", "", text)
    text = wiki_escape(text)
    text = _unwrap_paragraphs(text)
    text = re.sub(r"(?m)^[ \t]+", "", text)
    return byline, text


def strategy_archive_url(
    html: str,
    side: str,
    slug: str,
    folder: str = "premiere",
    split: bool = True,
    subdir: str = "small",
) -> str:
    subdir = subdir or "small"
    m = re.search(
        r'__wm\.wombat\("https?://www\.decipher\.com[^"]*(?:small|extras)/'
        + re.escape(slug)
        + r'\.html","(\d+)"',
        html,
    )
    original = _strategy_original(folder, side, slug, split, subdir)
    if m:
        return f"https://web.archive.org/web/{m.group(1)}/{original}"
    if folder == "premiere" and subdir == "small":
        base = ARCHIVE_LS if side == "light" else ARCHIVE_DS
        return base + f"small/{slug}.html"
    return f"https://web.archive.org/web/20040811123219/{original}"


def scomp_url(card: dict) -> str:
    title = (card.get("front") or {}).get("title") or ""
    title = re.sub(r"^[•*]+", "", title).strip()
    return "https://scomp.starwarsccg.org/?s=" + urllib.parse.quote(title)


def ref_tag(url: str, name: str | None = None, reuse: bool = False) -> str:
    if reuse and name:
        return f'<ref name="{name}" />'
    if name:
        return f'<ref name="{name}">{url}</ref>'
    return f"<ref>{url}</ref>"


def as_list(val) -> list:
    if not val:
        return []
    if isinstance(val, list):
        return val
    return [val]


def item_title(item) -> str:
    if isinstance(item, dict):
        t = item.get("title") or ""
    else:
        t = str(item)
    return re.sub(r"^[•*]+", "", t).strip()


class CardLinker:
    """Wiki-link printed titles and colloquial names (Tarkin → Grand Moff Tarkin)."""

    def __init__(self, records: list[dict]):
        light_prem = {
            r["printed"]
            for r in records
            if r["set"] == "1" and r["side"] == "Light" and r["printed"]
        }
        self.light_prem = light_prem
        # alias lower -> list of (alias, dest, side, premiere)
        buckets: dict[str, list[tuple[str, str, str, bool]]] = {}
        exact_lower = set()

        def add(alias: str, dest: str, side: str, premiere: bool = False):
            a = (alias or "").strip()
            if not a or not dest:
                return
            buckets.setdefault(a.lower(), []).append((a, dest, side, premiere))

        title_map = {}
        mp = ROOT / "card_title_map.json"
        if mp.exists():
            try:
                title_map = json.loads(mp.read_text(encoding="utf-8"))
            except Exception:
                title_map = {}

        def wiki_dest(printed: str, side: str, set_id: str) -> str:
            mapped = title_map.get(f"{set_id}|{side}|{printed}")
            if mapped:
                return mapped
            if set_id == "1" and side == "Dark" and (
                printed in light_prem or printed in CONCEPT_PAGES
            ):
                return f"{printed} (Dark)"
            return printed

        last_word: dict[str, list[tuple[str, str]]] = {}
        for r in records:
            printed = r["printed"]
            if not printed:
                continue
            dest = wiki_dest(printed, r["side"], r["set"])
            prem = r["set"] == "1"
            add(printed, dest, r["side"], prem)
            # Scomp "Title (EP1)" is the Coruscant printing, not Premiere.
            if r["set"] == "12":
                add(f"{printed} (EP1)", dest, r["side"], False)
            exact_lower.add(printed.lower())
            if " / " in printed:
                front_n, back_n = printed.split(" / ", 1)
                add(front_n, dest, r["side"], prem)
                add(back_n, dest, r["side"], prem)
                add(printed.replace(" / ", "/"), dest, r["side"], prem)
            m = re.match(r"^(.+?) \((.+)\)$", printed)
            if m:
                inner = m.group(2).strip()
                head = m.group(1).strip()
                if inner not in ("V", "AI", "Dark", "Light", "EP1"):
                    add(head, dest, r["side"], prem)
                    add(inner, dest, r["side"], prem)
            if (
                r["set"] == "1"
                and r["type"] == "Character"
                and r["uniqueness"] == "*"
            ):
                parts = re.split(r"[\s']+", printed)
                if len(parts) >= 2:
                    lw = parts[-1]
                    if lw.lower() not in NICK_STOP and len(lw) >= 4:
                        last_word.setdefault(lw.lower(), []).append((lw, dest))

        for key, pairs in last_word.items():
            dests = {d for _a, d in pairs}
            if len(dests) != 1:
                continue
            alias, dest = pairs[0]
            add(alias, dest, "*", True)

        for nick, printed in EXPLICIT_NICKS.items():
            cands = buckets.get(printed.lower()) or []
            prem_cands = [c for c in cands if c[3]]
            use = prem_cands or cands
            if not use:
                add(nick, printed, "*", True)
                continue
            for _a, dest, sd, prem in use:
                add(nick, dest, sd, prem)

        # Longest alias first so "Vader's Cape" wins over "Vader" / "Cape".
        items = []
        seen = set()
        for _k, lst in buckets.items():
            for alias, dest, sd, prem in lst:
                sig = (alias.lower(), dest, sd, prem)
                if sig in seen:
                    continue
                seen.add(sig)
                items.append((alias, dest, sd, prem))
        items.sort(key=lambda x: len(x[0]), reverse=True)
        self.items = items
        by_alias: dict[str, list[tuple[str, str, bool]]] = {}
        ordered = []
        seen_a = set()
        for alias, dest, sd, prem in items:
            by_alias.setdefault(alias.lower(), []).append((dest, sd, prem))
            if alias.lower() not in seen_a and alias:
                seen_a.add(alias.lower())
                ordered.append(alias)
        self.by_alias = by_alias
        if ordered:
            self.pattern = re.compile(
                r"(?<![A-Za-z0-9])("
                + "|".join(re.escape(a) for a in ordered)
                + r")(?![A-Za-z0-9])"
            )
        else:
            self.pattern = None

    def dest_for(self, alias: str, side: str) -> str | None:
        hits = self.by_alias.get(alias.lower()) or []
        if not hits:
            return None
        for pred in (
            lambda d, s, p: p and s == side,
            lambda d, s, p: p and s == "*",
            lambda d, s, p: p,
            lambda d, s, p: s == side,
            lambda d, s, p: s == "*",
            lambda d, s, p: True,
        ):
            for d, s, p in hits:
                if pred(d, s, p):
                    return d
        return None

    def wikilink(self, dest: str, visible: str) -> str:
        if visible == dest:
            return f"[[{dest}]]"
        return f"[[{dest}{{{{!}}}}{visible}]]"

    def link_text(self, text: str, side: str) -> str:
        if not text:
            return text
        held: list[str] = []

        def hold(m: re.Match) -> str:
            held.append(m.group(0))
            return f"\x00{len(held) - 1}\x00"

        if not self.pattern:
            return text

        def protect(s: str) -> str:
            s = re.sub(r"\[\[[^\]]+\]\]", hold, s)
            s = re.sub(r"<ref\b[^>]*/>", hold, s, flags=re.I)
            s = re.sub(r"<ref\b[^>]*>.*?</ref>", hold, s, flags=re.I | re.S)
            s = re.sub(r"\[mailto:[^\]]+\]", hold, s)
            s = re.sub(r"https?://[^\s\]<]+", hold, s)
            return s

        work = protect(text)
        work = self.pattern.sub(
            lambda m: self.wikilink(self.dest_for(m.group(1), side) or m.group(1), m.group(0)),
            work,
        )
        return re.sub(r"\x00(\d+)\x00", lambda m: held[int(m.group(1))], work)


_LINKER = None


def card_linker() -> CardLinker:
    global _LINKER
    if _LINKER is None:
        _LINKER = CardLinker(_scomp()[2])
    return _LINKER


def characteristics_of(card: dict) -> list[str]:
    """Printed extraText first, then Scomp characteristic tags. De-dupe."""
    front = card.get("front") or {}
    out = []
    seen = set()
    for src in (front.get("extraText"), front.get("characteristics")):
        for item in as_list(src):
            t = item_title(item)
            key = t.lower()
            if t and key not in seen:
                seen.add(key)
                out.append(t)
    return out


def extras_fields(gemp_id: str) -> dict:
    """Template params for Scomp + Decipher strategy. Combos never go in rulings."""
    by_id, _by_img, _rec = _scomp()
    card = by_id.get(gemp_id)
    smap = starred_map()
    linker = card_linker()
    side = ((card or {}).get("side") or (smap.get(gemp_id) or {}).get("side") or "Light")
    if isinstance(side, str):
        side = "Dark" if side.lower().startswith("d") else "Light"
    out = {
        "strategy": "",
        "combos": "",
        "rulings": "",
        "pulled_by": "",
        "pulls": "",
        "canceled_by": "",
        "cancels": "",
        "matching": "",
        "matching_weapon": "",
        "also_known_as": "",
        "personas": "",
        "characteristics": "",
        "counterpart": "",
        "underlying_card_for": "",
        "has_refs": "",
    }
    used_ref = False
    if card:
        s_url = scomp_url(card)
        s_first = ref_tag(s_url, name="scomp")
        s_again = ref_tag(s_url, name="scomp", reuse=True)

        def blist(items, cite: str = "", link: bool = False, link_side: str | None = None) -> str:
            lines = []
            for i, item in enumerate(as_list(items)):
                t = item_title(item)
                if not t:
                    continue
                body = wiki_escape(t)
                if link:
                    body = linker.link_text(body, link_side or side)
                lines.append("* " + body + (cite if i == 0 else ""))
            return "\n".join(lines)

        scomp_sections = [
            ("combos", card.get("combo")),
            ("rulings", card.get("rulings")),
            ("pulled_by", card.get("pulledBy")),
            ("pulls", card.get("pulls")),
            ("canceled_by", card.get("canceledBy")),
            ("cancels", card.get("cancels")),
            ("matching", card.get("matching")),
            ("matching_weapon", card.get("matchingWeapon")),
            ("also_known_as", card.get("abbr")),
            ("personas", card.get("personas")),
            ("characteristics", characteristics_of(card)),
            ("counterpart", card.get("counterpart")),
            ("underlying_card_for", card.get("underlyingCardFor")),
        ]
        # Cite verbatim Combos/Rulings. If a card has neither, cite the first
        # Scomp section so References still lists scomp.starwarsccg.org.
        cite_on = set()
        if card.get("combo"):
            cite_on.add("combos")
        if card.get("rulings"):
            cite_on.add("rulings")
        if not cite_on:
            for field, items in scomp_sections:
                if as_list(items):
                    cite_on.add(field)
                    break

        defined = False
        for field, items in scomp_sections:
            if not as_list(items):
                continue
            cite = ""
            if field in cite_on:
                used_ref = True
                cite = s_first if not defined else s_again
                defined = True
            other = "Dark" if side == "Light" else "Light"
            out[field] = blist(
                items,
                cite=cite,
                link=field in LINK_FIELDS,
                link_side=other if field == "counterpart" else side,
            )

    star = smap.get(gemp_id)
    if star:
        html = fetch_strategy_html(
            star["side"],
            star["slug"],
            folder=star.get("folder") or "premiere",
            split=star.get("split", True),
            subdir=star.get("subdir") or "small",
        )
        byline, body = parse_strategy(html) if html else ("", "")
        if byline or body:
            src = strategy_archive_url(
                html,
                star["side"],
                star["slug"],
                folder=star.get("folder") or "premiere",
                split=star.get("split", True),
                subdir=star.get("subdir") or "small",
            )
            used_ref = True
            cite = ref_tag(src, name="decipher-strategy")
            parts = []
            if byline:
                parts.append(byline + cite)
            elif body:
                body = body + cite
            if body:
                parts.append(linker.link_text(body, side))
            out["strategy"] = "\n\n".join(parts)
    if used_ref:
        out["has_refs"] = "1"
    return out


def extras_for(gemp_id: str, smap: dict | None = None) -> tuple[str, str]:
    """Back-compat: strategy, rulings only. Prefer extras_fields()."""
    f = extras_fields(gemp_id)
    return f.get("strategy") or "", f.get("rulings") or ""


def _scomp():
    global _CACHE
    if _CACHE is None:
        _CACHE = _load_scomp()
    return _CACHE


DARK_SLUG_ALIASES = {
    "lifttubeimp": "lifttube",
    "sensedark": "sense",
    "tatooinelarsmoisturedark": "tatooinelarsmoisturefarm",
    "timerminedark": "timermine",
}


_STAR_CACHE = None


def starred_map() -> dict:
    global _STAR_CACHE
    if _STAR_CACHE is not None:
        return _STAR_CACHE
    all_path = ROOT / "starred_all.json"
    if all_path.exists() and all_path.stat().st_size > 20:
        _STAR_CACHE = json.loads(all_path.read_text(encoding="utf-8"))
        return _STAR_CACHE
    by_id, by_img, _rec = _scomp()
    out = {}
    for side in ("light", "dark"):
        for slug in starred_slugs(side):
            key = slug
            if side == "dark":
                key = DARK_SLUG_ALIASES.get(slug, slug)
            card = by_img.get(key)
            if not card:
                continue
            gid = card.get("gempId")
            if gid:
                title = re.sub(r"^[•*]+", "", (card.get("front") or {}).get("title") or "").strip()
                out[gid] = {"side": side, "slug": slug, "title": title}
    _STAR_CACHE = out
    return out


def prefetch_starred():
    sm = starred_map()
    print("starred mapped", len(sm))
    for gid, info in sorted(sm.items(), key=lambda x: x[0]):
        print("fetch", info["side"], info["slug"])
        fetch_strategy_html(info["side"], info["slug"])
    return sm


if __name__ == "__main__":
    prefetch_starred()
    print("done prefetch")
