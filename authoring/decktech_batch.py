#!/usr/bin/env python3
"""Data-driven DeckTech dests: one JSON file per deck, one renderer, batched applies.

Replaces "hand-write a new block in generate_decktech.py per deck". Each deck is
`decktech-decks/<id>.json`; this script renders the deck page, the player page,
and adds rows to [[DeckTech decks]] and the format page on top of what
generate_decktech.py already produces. Decks dested before 2026-10-10 stay in
generate_decktech.py; only new decks use data files.

Workflow (see SKILL swccg-wiki § DeckTech):

    python decktech_batch.py fetch 22698 22685 ...     # posts + cleaned txt + card suggestions
    python decktech_batch.py wayback 22698 22685 ...   # run in background; fills decktech-wayback.json
    python decktech_batch.py draft 22698                # skeleton decktech-decks/22698.json to finish by hand
    python decktech_batch.py build dt-batch-01 22698 22685 ...   # pages/ + y-dt-batch-01.tsv + tar
    python decktech_batch.py check y-dt-batch-01.tsv 22698 22685 ...  # after apply: reviewed, red links; records ids in decktech-live.json

Apply on the VPS exactly like other batches: scp the tar + apply-tsv.sh, run
`apply-tsv.sh y-dt-<batch>.tsv "<summary>"`.
"""
from __future__ import annotations

import difflib
import html
import json
import re
import ssl
import sys
import tarfile
import time
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))

import gemp_importable as gi  # noqa: E402
import generate_decktech as gd  # noqa: E402
import wiki_cardlink as cl  # noqa: E402

# Original-era (2002) Virtual slips not yet in generate_decktech.ORIGINAL_VS.
# Posted "X (V)" in a 2002 deck dests the original slip page, not current virtual.
EXTRA_ORIGINAL_VS = {
    "Assault Rifle (V)": ("Assault Rifle (V) (Virtual Set 1)", "VS1O-07-Assault Rifle.png"),
    "Gold 1 (V)": ("Gold 1 (V) (Virtual Set 1)", "VS1O-03-Gold 1.png"),
    "Fusion Generator Supply Tanks (V) (Light)": ("Fusion Generator Supply Tanks (V) (Light) (Virtual Set 1)", "VS1O-02-Fusion Generator Supply Tanks.png"),
    "Fusion Generator Supply Tanks (V) (Dark)": ("Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1)", "VS1O-11-Fusion Generator Supply Tanks.png"),
}
for _k, _v in EXTRA_ORIGINAL_VS.items():
    gd.ORIGINAL_VS.setdefault(_k, _v)

DECKS = ROOT / "decktech-decks"
POSTS = ROOT / "decktech-posts"
WAYBACK_FILE = ROOT / "decktech-wayback.json"
LIVE_FILE = ROOT / "decktech-live.json"  # ids verified live by `check`; hub/format pages always include them
NICKNAMES = ROOT / "card_nicknames.json"
API = "https://wiki.swccg.com/api.php"
UA = {"User-Agent": "swccg-wiki-dest/1.0 (wiki.swccg.com historian)"}
CTX = ssl.create_default_context()

# Where a format page lists its pool-by-legal-day sentences. New sentences are
# inserted at the start of that paragraph (we dest backward in time). Add an
# anchor here when the work reaches a new format.
FORMAT_ANCHORS = {
    "Premiere - Original VS1": re.compile(r"^(?=\[\[[^\]]+\]\] (?:is printed Decipher through|dests \[\[))", re.M),
}

HEADER_WORDS = {"starting", "start", "location", "site", "character", "starship", "ship", "vehicle", "weapon",
                "device", "effect", "interrupt", "interupt", "interrrupt", "inturrupt", "interuppt", "racer", "podracer",
                "admiral", "ao", "epic", "epice", "creature", "shield", "green", "blue"}
TYPE_HEADERS = {
    "objective": "OBJECTIVE", "location": "LOCATION", "site": "LOCATION", "system": "LOCATION",
    "character": "CHARACTER", "starship": "STARSHIP", "ship": "STARSHIP", "vehicle": "VEHICLE",
    "weapon": "WEAPON", "device": "DEVICE", "effect": "EFFECT", "interrupt": "INTERRUPT",
    "admiral": "ADMIRALS_ORDER", "ao": "ADMIRALS_ORDER", "epic": "EPIC_EVENT", "creature": "CREATURE",
    "jedi test": "JEDI_TEST", "podracer": "PODRACER", "shield": "DEFENSIVE_SHIELD",
}


# ---------------------------------------------------------------- helpers

def http_get(url: str, timeout: int = 60) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, context=CTX, timeout=timeout) as r:
        return r.read()


def api(**kw) -> dict:
    kw.update(format="json", formatversion="2")
    return json.loads(http_get(API + "?" + urllib.parse.urlencode(kw)))


def live_text(title: str) -> str | None:
    d = api(action="query", prop="revisions", rvprop="content", rvslots="main", titles=title)
    p = d["query"]["pages"][0]
    if p.get("missing"):
        return None
    return p["revisions"][0]["slots"]["main"]["content"]


REF3 = "Reflections III: A Collector's Bounty"
_SHIELD_PAGES: dict[str, str | None] = {}


def shield_link(name: str, side: str) -> str | None:
    """Decipher's Defensive Shields were printed in Reflections III; same-named older cards are Effects.
    Link the Reflections III shield page (titled "X (Reflections III: ...)" or "X (Dark|Light)") with its own image."""
    for page in (f"{name} ({REF3})", f"{name} ({side})", name):
        if page not in _SHIELD_PAGES:
            txt = live_text(page) or ""
            ok = "type=Defensive Shield" in txt and f"side={side}" in txt and f"set={REF3}" in txt
            m = re.search(r"^\|image=(.+)$", txt, re.M)
            _SHIELD_PAGES[page] = m.group(1).strip() if ok and m else None
        if _SHIELD_PAGES[page]:
            return gd.cl.cardlink(page, _SHIELD_PAGES[page], name)
    return None


def long_date(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.day} {d.strftime('%B')} {d.year}"


def short_date(iso: str) -> str:
    d = date.fromisoformat(iso)
    return f"{d.month}/{d.day}/{d.strftime('%y')}"


def inventory() -> dict[str, dict]:
    inv = json.loads((ROOT / "decktech-inventory.json").read_text(encoding="utf-8"))
    return {str(p["id"]): p for p in inv["posts"]}


def yaml_path(pid: str) -> str:
    iso = date_of(pid)
    return f"https://raw.githubusercontent.com/stevetotheizz0/decktech_archives/master/_posts/{iso}-{pid}.md"


def date_of(pid: str) -> str:
    raw = inventory()[pid]["date"]  # "Apr 9, 2002"
    return time.strftime("%Y-%m-%d", time.strptime(raw, "%b %d, %Y"))


# ---------------------------------------------------------------- card resolution

_CANON: dict[str, set[str]] | None = None
_TYPES: dict[str, str] = {}
INDEX_TYPE = {
    "Character": "CHARACTER", "Interrupt": "INTERRUPT", "Effect": "EFFECT", "Location": "LOCATION",
    "Starship": "STARSHIP", "Weapon": "WEAPON", "Objective": "OBJECTIVE", "Vehicle": "VEHICLE",
    "Device": "DEVICE", "Defensive Shield": "DEFENSIVE_SHIELD", "Epic Event": "EPIC_EVENT",
    "Creature": "CREATURE", "Admiral's Order": "ADMIRALS_ORDER", "Podracer": "PODRACER",
}


def card_type(title: str) -> str:
    canon()
    t = _TYPES.get(title, "")
    return "JEDI_TEST" if t.startswith("Jedi Test") else INDEX_TYPE.get(t, "")
_NICK: dict[str, dict] | None = None


def canon() -> dict[str, set[str]]:
    global _CANON
    if _CANON is None:
        _CANON = {}
        for (side, key), cards in cl._load_index().items():
            for c in cards:
                f = c.get("front") or {}
                t = cl.strip_uniqueness(f.get("title") or "")
                if t:
                    _CANON.setdefault(f"{side}|{key}", set()).add(t)
                    _TYPES.setdefault(t, f.get("type") or "")
    return _CANON


def nicknames() -> dict[str, dict]:
    global _NICK
    if _NICK is None:
        raw = json.loads(NICKNAMES.read_text(encoding="utf-8")) if NICKNAMES.exists() else {}
        _NICK = {k.casefold(): v for k, v in raw.items()}
    return _NICK


def suggest(posted: str, side: str) -> tuple[str, str]:
    """(status, card) where status is exact | nickname | fuzzy | ? ."""
    name = re.sub(r"\s+", " ", posted).strip(" -*•")
    c = canon()
    key = f"{side}|{cl.lookup_key(name).casefold()}"
    if key in c:
        return "exact", sorted(c[key])[0]
    nk = nicknames().get(name.casefold())
    if nk and "card" in nk:
        return "nickname", nk["card"]
    titles = sorted({t for k, ts in c.items() if k.startswith(side + "|") for t in ts})
    hit = difflib.get_close_matches(name, titles, n=1, cutoff=0.72)
    if hit:
        return "fuzzy", hit[0]
    return "?", ""


QTY_PATTERNS = [
    re.compile(r"^[\[(](\d+)[\])}]\s*(.+)$"),  # [3] Name / (2) Name / [2} Name
    re.compile(r"^(\d+)\s*x\s*(?![-\d])(.+)$", re.I),  # not "2X-3KPR"
    re.compile(r"^(.+?)\s+[x×]\s*(\d+)\s*\([^)]*\)$", re.I),  # "2X-3KPR x3 (Nighttime Droid)"
    re.compile(r"^(.+?)\s*[x×]\s*(\d+)$", re.I),
    re.compile(r"^(.+?)\s*\((\d+)\)$"),
]


def parse_card_list(cards: str) -> list[tuple[int, str, str]]:
    rows: list[tuple[int, str, str]] = []
    kind = ""
    for raw in cards.splitlines():
        line = raw.strip().strip("'`").strip()
        if not line:
            continue
        line = re.sub(r"^(.+?)\s*\(\s*[x×]\s*(\d+)\b[^)]*\)$", r"\1 x\2", line, flags=re.I)  # "Shmi Skywalker(x2)", "(x4, best card ever)"
        line = re.sub(r"^\(([A-Za-z' ]+)\)\s*-?\s*(\d*)$", lambda m: f"{m.group(1)} ({m.group(2)})" if m.group(2) else m.group(1), line)  # "(Inturrupts)-16"
        line = re.sub(r"^([A-Za-z]+) & [A-Za-z]+$", lambda m: m.group(1) if m.group(1).lower().rstrip("s") in HEADER_WORDS else m.group(0), line)  # "Starships & Vehicles"
        line = re.sub(r"^([A-Za-z'/ ]+?)\s+-\s*(\d+)$", r"\1 (\2)", line)  # "CHARACTERS -19"
        line = re.sub(r"^[-=\s(]+([A-Za-z' ]+?)[-=\s)]+$", r"\1", line)  # "-STARTING-", "((( STARTING )))"
        line = re.sub(r"^([A-Za-z']+)-\s*\((\d+)\)$", r"\1 (\2)", line)  # "Starships- (5)"
        line = re.sub(r"^([A-Za-z']+)-$", r"\1", line)  # "Effects-"
        line = re.sub(r"^([A-Za-z']+) ?(\d+)$", lambda m: f"{m.group(1)} ({m.group(2)})" if m.group(1).lower().rstrip("s") in HEADER_WORDS - {"green", "blue"} else m.group(0), line)  # "starting6", "Locations 7"
        head = re.match(r"^([A-Za-z'/ ]+?)\s*(?:\([^)]*\))?\s*:?$", line)
        counted = bool(re.search(r"\([^)]*\)\s*:?$|:$", line)) and not re.search(r"\(\d+\)$", line) or bool(re.search(r"\(\d+\)\s*:?$", line)) and len(line.split()) <= 3
        if head and (counted or len(head.group(1).split()) == 1 or head.group(1).strip().lower() in ("admirals order", "admirals orders", "admiral's order", "admiral's orders", "weapons/devices", "starting cards")):
            word = head.group(1).strip().lower().split("/")[0].split()[0] if head.group(1).strip() else ""
            word = word.rstrip("s")
            hit = difflib.get_close_matches(word, list(TYPE_HEADERS), n=1, cutoff=0.8)  # 0.75 read 'Shmi' as 'ship'
            if word in ("green", "blue", "racer", "epice"):  # joke / short headers seen in posts
                kind = {"green": "WEAPON", "blue": "STARSHIP", "racer": "PODRACER", "epice": "EPIC_EVENT"}[word]
                continue
            if word in ("starting", "start"):
                kind = "STARTING"
                continue
            if hit:
                kind = TYPE_HEADERS[hit[0]]
                continue
        line = re.sub(r"\s*\(S\b[^)]*\)\s*$", "", line, flags=re.I)  # starting marker "(S)"
        qty, name = 1, line
        for pat in QTY_PATTERNS:
            m = pat.match(line)
            if m:
                a, b = m.groups()
                qty, name = (int(a), b) if a.isdigit() else (int(b), a)
                break
        rows.append((qty, name.strip(), kind or "?"))
    return rows


# ---------------------------------------------------------------- commands

def cmd_fetch(ids: list[str]) -> None:
    POSTS.mkdir(exist_ok=True)
    for pid in ids:
        urls = {
            f"{pid}.yaml.md": yaml_path(pid),
            f"{pid}.skilton.html": f"https://www.stephenskilton.com/decktech_archives/{pid}/",
            f"{pid}.live.html": f"http://www.decktech.net/starwarsccg/deck/{pid}",
        }
        for name, url in urls.items():
            try:
                (POSTS / name).write_bytes(http_get(url, 45))
            except Exception as e:  # noqa: BLE001
                print("FAIL", pid, name, type(e).__name__, e)
        write_clean_txt(pid)
        post = gd.split_dt_post(int(pid))
        side = guess_side(post.get("cards", ""))
        print(f"\n=== {pid} {post.get('title')!r} by {post.get('author')!r} ({date_of(pid)}) side≈{side}")
        for qty, name, kind in parse_card_list(post.get("cards", "")):
            st, card = suggest(name, side)
            flag = "  " if st in ("exact", "nickname") else "!!"
            print(f"{flag} {qty}x {name!r:45} {kind:15} -> {st}: {card}")


def guess_side(cards: str) -> str:
    dark = len(re.findall(r"vader|imperial|emperor|executor|stormtrooper|walker|tie\b|fett|jabba", cards, re.I))
    light = len(re.findall(r"luke|leia|han\b|rebel|x-wing|jedi|obi|yoda|chewie|falcon|senate", cards, re.I))
    return "Dark" if dark >= light else "Light"


def write_clean_txt(pid: str) -> None:
    raw = (POSTS / f"{pid}.yaml.md").read_text(encoding="utf-8")
    raw = html.unescape(raw)
    for a, b in (("\u0092", "'"), ("’", "'"), ("‘", "'"), ("�", "'")):
        raw = raw.replace(a, b)

    def val(name: str) -> str:
        m = re.search(rf"^{name}:\s*(.+)$", raw, re.M)
        v = (m.group(1).strip() if m else "").lstrip("!").strip()
        if len(v) > 1 and v[0] == v[-1] and v[0] in "\"'":
            v = v[1:-1]
        return v.strip()

    lower = raw.lower()
    ca, sa = lower.find("cards:"), lower.find("strategy:")
    cards = raw[ca + 6:sa].strip().strip("'‘’`").strip()
    strategy = re.sub(r"\s*\*+\s*$", "", raw[sa + 9:].strip().strip("'‘’`").strip(), flags=re.M)
    tags = val("tags") or val("tag")
    if not tags:
        m = re.search(r"^tags:\s*\n((?:- .+\n)+)", raw, re.M)
        tags = m.group(1).strip().replace("\n", " ") if m else ""
    out = (
        f"{val('title')}\n\nTitle: {val('title')}\nAuthor: {val('author')}\n"
        f"Date: {_us_date(pid)}\n"
        f"Rating: {val('rating')}\nTags: {tags}\n\nDescription: {val('description')}\n\n"
        f"Cards: \n\n{cards}\n\nStrategy: \n\n{strategy}\n"
    )
    (POSTS / f"{pid}.txt").write_text(out, encoding="utf-8", newline="\n")


def _us_date(pid: str) -> str:
    d = date.fromisoformat(date_of(pid))
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def live_url(pid) -> str:
    return f"http://www.decktech.net/starwarsccg/deck/{pid}"


WB_QUEUE = ROOT.parent / "ops" / "wayback" / "queue.txt"
WB_DONE = ROOT.parent / "ops" / "wayback" / "done.json"


def cmd_wayback(ids: list[str]) -> None:
    """Queue the decktech.net page of each deck for a Wayback save (Bill 2026-10-10: the original
    decktech.net link is the one to preserve; Skilton/GitHub Pages copies are cited, not re-saved).

    Appends to ops/wayback/queue.txt; commit + push it and the VPS worker (ops/wayback_worker.py)
    saves them one at a time. Until that worker runs, Bill's PC can run
    claude-agent/wbq.py STATE ID:live ... instead and its results go in decktech-wayback.json.
    """
    have = WB_QUEUE.read_text(encoding="utf-8").splitlines() if WB_QUEUE.exists() else []
    new = [live_url(p) for p in ids if live_url(p) not in have]
    WB_QUEUE.parent.mkdir(parents=True, exist_ok=True)
    with WB_QUEUE.open("a", encoding="utf-8") as fh:
        fh.writelines(u + "\n" for u in new)
    print(f"queued {len(new)} URLs in {WB_QUEUE.relative_to(ROOT.parent)}; commit + push it")


def cmd_draft(pid: str) -> None:
    DECKS.mkdir(exist_ok=True)
    post = gd.split_dt_post(int(pid))
    side = guess_side(post.get("cards", ""))
    rows = []
    for qty, name, kind in parse_card_list(post.get("cards", "")):
        st, card = suggest(name, side)
        kind = card_type(card) or kind if card else kind
        rows.append([qty, card or f"?? {name}", kind, f"posted: {name} ({st})"])
    author = post.get("author", "")
    player = re.sub(r'\s*"[^"]*"\s*', " ", author).strip()
    skel = {
        "id": int(pid),
        "date": date_of(pid),
        "published_title": post.get("title", ""),
        "use_published_title": True,
        "byline": author,
        "player": player,
        "player_page": "new",
        "player_intro": f"posted a [[{side}]] list on DeckTech.",
        "side": side,
        "format": "Premiere - Original VS1",
        "kind": "general",
        "event": None,
        "finish": None,
        "starting": {"card": None, "interrupt": None, "effect": None},
        "description": gd._field((POSTS / f"{pid}.txt").read_text(encoding="utf-8"), "Description"),
        "cards": rows,
        "shields": [],
        "shields_note": None,
        "notes": [],
    }
    out = DECKS / f"{pid}.json"
    if out.exists():
        raise SystemExit(f"{out} exists; edit it instead")
    out.write_text(json.dumps(skel, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("DRAFT", out)


# ---------------------------------------------------------------- rendering

def load_deck(pid: str) -> dict:
    d = json.loads((DECKS / f"{pid}.json").read_text(encoding="utf-8"))
    bad = [r for r in d["cards"] if str(r[1]).startswith("??") or r[2] == "?"]  # UNKNOWN is allowed (explicit)
    if bad:
        raise SystemExit(f"{pid}: unresolved cards {bad[:5]}")
    return d


def dest_title(d: dict) -> str:
    if d.get("dest_title"):
        return d["dest_title"]
    tail = d["published_title"] if d.get("use_published_title") else ("DS" if d["side"] == "Dark" else "LS")
    pre = f"{d['event']} " if d.get("kind") == "tournament" else ""
    return " ".join(f"{pre}{d['player']} {tail}".split())  # MediaWiki collapses runs of spaces


def label(d: dict) -> str:
    return d["published_title"] if d.get("use_published_title") else f"DeckTech post {d['id']}"


def register_wayback(d: dict) -> None:
    wb = json.loads(WAYBACK_FILE.read_text(encoding="utf-8")) if WAYBACK_FILE.exists() else {}
    found = dict(wb.get(str(d["id"]), {}))
    if WB_DONE.exists():  # VPS queue results (status ok = capture confirmed)
        e = json.loads(WB_DONE.read_text(encoding="utf-8")).get(live_url(d["id"]))
        if e and e.get("status") == "ok":
            found.setdefault("live", e["capture"])
    for kind, url in {**found, **d.get("wayback", {})}.items():
        gd.WAYBACK[(kind, d["id"])] = url


def rows_of(d: dict, key: str = "cards") -> list[tuple[int, str, str]]:
    """Table rows. Type UNKNOWN = a posted name that matches no card; shown as text, never guessed."""
    return [(int(r[0]), r[1], r[2]) for r in d.get(key, []) if r[2] != "UNKNOWN"]


def unknown_note(d: dict) -> str:
    unk = [f"{int(r[0])}x {r[1]}" for r in d.get("cards", []) if r[2] == "UNKNOWN"]
    if not unk:
        return ""
    return ("\nThe post also lists " + ", ".join(unk) + ", which matches no known card; it is shown as posted "
            "and counted in the published total.\n")


def plink(d: dict) -> str:
    """Player link, or plain text when the post's name is not a person to page (player_page: none)."""
    return d["player"] if d.get("player_page") == "none" else f"[[{d['player']}]]"


def deck_page(d: dict) -> str:
    side_u = d["side"].upper()
    t, pid, lbl = dest_title(d), d["id"], label(d)
    byline = f"{d['byline']}, {long_date(d['date'])}"
    wc = lambda name: gd.wiki_card(name, side_u)  # noqa: E731
    intro = f"'''{t}''' is the [[{d['side']}]] constructed list {plink(d)} posted on DeckTech"
    if d.get("kind") == "tournament":
        intro += f" after finishing {d['finish']} at [[{d['event']}]]"
    intro += "."
    if d.get("player_note"):
        intro += " " + d["player_note"]
    if not d.get("use_published_title"):
        intro += " The published title is not used as the page title; it appears in the original post below."
    info = [f"* '''Player:''' {plink(d)}"]
    if d.get("kind") == "tournament":
        info += [f"* '''Event:''' [[{d['event']}]]", f"* '''Finish:''' {d['finish']}"]
    info.append(f"* '''Published:''' {long_date(d['date'])} (DeckTech)")
    if d.get("use_published_title"):
        info.append(f"* '''Published title:''' ''{d['published_title']}''")
    info += [f"* '''Format:''' [[{d['format']}]]", f"* '''Side:''' [[{d['side']}]]"]
    st = d.get("starting") or {}
    for k, lab in (("card", "Starting Card"), ("interrupt", "Starting Interrupt"), ("effect", "Starting Effect")):
        if st.get(k):
            info.append(f"* '''{lab}:''' {wc(st[k])}")
    if d.get("gemp_file"):
        line = gi.wiki_download_line(d["gemp_file"])
        if d.get("gemp_omitted"):
            line += " (omits " + ", ".join(dict.fromkeys(d["gemp_omitted"])) + ": no GEMP blueprint)"
        info.append(line)
    if d.get("description"):
        info.append(f"* '''Strategy:''' {d['description']}")
    shields = ""
    if d.get("shields"):
        sh = "\n".join(f"* {q}x {shield_link(n, d['side']) or wc(n)}" for q, n, _ in rows_of(d, "shields"))
        shields = f"\n== Defensive Shields ==\n\nThese cards were posted as Defensive Shields outside the 60. They do not count toward the 60.\n\n{sh}\n"
    note = f"\n{d['shields_note']}\n" if d.get("shields_note") else ""
    see = ([] if d.get("player_page") == "none" else [f"* [[{d['player']}]]"]) + ([f"* [[{d['event']}]]"] if d.get("event") else []) + [
        "* [[DeckTech decks]]", "* [[Decklists]]", f"* [[{d['format']}]]"]
    return f"""{intro}{gd.post_ref(f"dt-{pid}", pid, lbl, byline)}

== Deck info ==
{chr(10).join(info)}

== Decklist ==

{gd.table_from_rows(rows_of(d), side_u)}
{shields}{note}{unknown_note(d)}
{gd.formatted_original_post(pid, description=d.get("description", ""))}

== See also ==

{chr(10).join(see)}

== Sources ==

{gd.post_source_bullets(pid, lbl)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:{d['date'][:4]}]]
"""


def player_row(d: dict) -> str:
    return (f"| {long_date(d['date'])} || [[{d['format']}]] || "
            f"[[{dest_title(d)}{'|' + d['published_title'] if d.get('use_published_title') else ''}]] || [[{d['side']}]]")


def player_page(d: dict, current: str | None) -> str:
    pid, lbl = d["id"], label(d)
    if current is None:
        ref = gd.post_ref(f"dt-{pid}", pid, lbl, f"{d['byline']}, {long_date(d['date'])}")
        return f"""'''{d['player']}'''{ref} {d['player_intro']}

== Miscellaneous decklists ==

{{| class="wikitable"
|-
! Date !! Format !! Title !! Side
|-
{player_row(d)}
|}}

== See also ==

* [[{dest_title(d)}]]
* [[DeckTech decks]]
* [[Decklists]]

== Sources ==

{gd.post_source_bullets(pid, lbl)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:People]]
[[Category:{d['date'][:4]}]]
"""
    text = current
    note = d.get("player_page_note")
    if note and note not in text:
        cut = text.find("\n\n== ")
        text = text[:cut] + " " + note + text[cut:] if cut > 0 else text
    text = sort_misc_rows(gd.add_misc_row(text, player_row(d)))
    text = gd.add_see_also(text, f"* [[{dest_title(d)}]]")
    text = gd.add_source_line(text, gd.post_source_bullets(pid, lbl))
    return gd.add_category(text, d["date"][:4])


def sort_misc_rows(text: str) -> str:
    """Keep a player's Miscellaneous decklists table oldest-first."""
    i = text.find("== Miscellaneous decklists ==")
    if i < 0:
        return text
    head_end = text.find("|-\n|", i)
    end = text.find("\n|}", i)
    rows = [r.rstrip("\n") for r in text[head_end:end].split("|-\n") if r.strip()]

    def key(r: str):
        m = re.match(r"\|\s*(\d{1,2}) (\w+) (\d{4})", r)
        if not m:
            return (9999, 0, 0)
        return (int(m.group(3)), time.strptime(m.group(2), "%B").tm_mon, int(m.group(1)))
    rows.sort(key=key)
    return text[:head_end] + "".join(f"|-\n{r}\n" for r in rows).rstrip("\n") + text[end:]


def hub_row(d: dict) -> tuple[str, str]:
    t = dest_title(d)
    if d.get("kind") == "tournament":
        start = (d.get("starting") or {}).get("card") or d["published_title"]
        dark = f"[[{t}|{start}]]" if d["side"] == "Dark" else "—"
        light = f"[[{t}|{start}]]" if d["side"] == "Light" else "—"
        return "tournament", (f"| {short_date(d['date'])} || [[{d['format']}]] || [[{d['event']}]] || {d['finish']} || "
                              f"{plink(d)} || {dark} || {light}")
    shown = f"[[{t}|{d['published_title']}]]" if d.get("use_published_title") else f"[[{t}]]"
    return "general", f"| {short_date(d['date'])} || [[{d['format']}]] || {shown} || [[{d['side']}]] || {plink(d)}"


def _row_date(row: str) -> tuple:
    m = re.match(r"\|\s*(\d+)/(\d+)/(\d+)", row)
    return (int(m.group(3)), int(m.group(1)), int(m.group(2))) if m else (99, 99, 99)


def insert_hub_rows(hub: str, decks: list[dict]) -> str:
    """Add rows oldest-first. Same-day rows: new (older-id) posts go before existing ones,
    because dests run backward through the archive."""
    sections = {"tournament": "== Tournament lists ==", "general": "== General lists =="}
    for kind_name, header in sections.items():
        new = [(d["date"], d["id"], hub_row(d)[1]) for d in decks
               if hub_row(d)[0] == kind_name and f"[[{dest_title(d)}" not in hub]
        if not new:
            continue
        start = hub.find(header)
        table = hub.find("|-\n|", start)
        end = hub.find("\n|}", start)
        old = [r.rstrip("\n") for r in hub[table:end].split("|-\n") if r.strip()]
        keyed = [(_row_date(r), 1, 0, r) for r in old]
        keyed += [(_row_date(row), 0, pid, row) for _, pid, row in new]
        keyed.sort(key=lambda k: (k[0], k[1], k[2]))
        body = "".join(f"|-\n{r}\n" for *_, r in keyed).rstrip("\n")
        hub = hub[:table] + body + hub[end:]
    return hub


def insert_format_sentences(text: str, fmt: str, decks: list[dict]) -> str:
    anchor = FORMAT_ANCHORS.get(fmt)
    if not anchor:
        raise SystemExit(f"no FORMAT_ANCHORS entry for {fmt!r}; add one first")
    m = anchor.search(text)
    if not m:
        raise SystemExit(f"anchor not found on {fmt}")
    new = ""
    for d in sorted(decks, key=lambda x: (x["date"], x["id"])):
        t = dest_title(d)
        if f"[[{t}]] is printed" in text or f"[[{t}]] dests" in text:
            continue
        vs = [gd.ORIGINAL_VS[r[1]][0] for r in d["cards"] if r[1] in gd.ORIGINAL_VS]
        if d.get("format_sentence"):
            new += d["format_sentence"].rstrip() + " "
        elif vs:
            links = " and ".join(f"[[{v}]]" for v in dict.fromkeys(vs))
            new += f"[[{t}]] dests {links}. "
        else:
            new += (f"[[{t}]] is printed Decipher through [[Theed Palace]] (no original (V) cards); "
                    f"the format cell is still this pool by legal day ({long_date(d['date'])}). ")
    return text[:m.start()] + new + text[m.start():]


GEMP_OUT = ROOT / "gemp-import-dt"
GEMP_FORMAT = {  # wiki format -> GEMP format code (original-era Virtual slips have no blueprints)
    "Premiere - Original VS1": "open_no_virtual",
    "Premiere - Original VS2": "open_no_virtual",
    "Premiere - Original VS3": "open_no_virtual",
}


def _arch(start: str) -> str:
    face = (start or "").split(" / ")[0]
    if face in gi.ARCHETYPE_ABBR or len(face) <= 10:
        return face
    return "".join(w[0] for w in re.findall(r"[A-Za-z0-9']+", face) if w[0].isalnum()).upper()


def gemp_file(d: dict, taken: set[str]) -> tuple[str | None, list[str]]:
    """Write the GEMP importable decklist for a deck. Returns (filename, omitted cards)."""
    rows, omitted = [], []
    for r in d["cards"]:
        q, t = int(r[0]), r[1]
        if t in gd.ORIGINAL_VS or r[2] in ("DEFENSIVE_SHIELD", "UNKNOWN"):
            omitted.append(t)
            continue
        rows.append((q, t, None))
    code = GEMP_FORMAT.get(d["format"], "open_no_virtual")
    try:
        xml, notes = gi.xml_for(rows, d["side"], code)
    except KeyError as e:
        print(f"NOGEMP {d['id']}: {e}")
        return None, omitted
    start = (d.get("starting") or {}).get("card") or d.get("published_title") or ""
    arch = d.get("gemp_arch") or _arch(start)  # gemp_arch: the post's own archetype name when the start card says nothing
    base = gi.safe_deck_filename(gi.deck_name(d["format"], arch, d["player"], d["side"], d["date"][:4], "DeckTech"))
    fn = d.get("gemp_file_live") or base + ".txt"  # a deck already live keeps its uploaded file name
    if not d.get("gemp_file_live") and (fn.lower() in taken or file_exists(fn)):
        fn = gi.safe_deck_filename(gi.deck_name(d["format"], arch, d["player"], d["side"], d["date"][:4], str(d["id"]))) + ".txt"
    fn = re.sub(r"\s+", " ", fn.replace("_", " "))  # MediaWiki stores "_" as a space
    taken.add(fn.lower())
    GEMP_OUT.mkdir(exist_ok=True)
    (GEMP_OUT / fn).write_text(xml, encoding="utf-8", newline="\n")
    if notes:
        print("GEMP NOTES", d["id"], notes[:6])
    return fn, omitted


def file_exists(fn: str) -> bool:
    p = api(action="query", titles="File:" + fn)["query"]["pages"][0]
    return not p.get("missing")


FORMAT_BUILDERS = {"Premiere - Original VS1": "povs1_page", "Premiere - Original VS2": "povs2_page"}


def cmd_build(batch: str, ids: list[str]) -> None:
    decks = [load_deck(p) for p in ids]
    for d in decks:
        register_wayback(d)
        if not gd.WAYBACK.get(("live", d["id"])) and not gd.WAYBACK.get(("skilton", d["id"])):
            print(f"WARN {d['id']}: no Wayback yet (run wayback; mission = original + backup link)")
    titles: list[tuple[str, str]] = []

    def emit(title: str, body: str) -> None:
        path = gd.write_page(title, body)
        titles.append((title, f"pages/{path.name}"))

    taken: set[str] = set()
    gemp_files: list[str] = []
    for d in decks:
        if d.get("gemp", True):
            fn, omitted = gemp_file(d, taken)
            d["gemp_file"], d["gemp_omitted"] = fn, omitted
            if fn:
                gemp_files.append(fn)
    players: dict[str, str] = {}
    for d in decks:
        qty = sum(int(r[0]) for r in d["cards"])
        print(f"{d['id']} {dest_title(d)} qty={qty}")
        gd.print_lookups(rows_of(d), d["side"].upper())
        emit(dest_title(d), deck_page(d))
        if d.get("player_page") == "none":
            continue
        if d["player"] in players:  # several decks by one player in this batch
            cur = players[d["player"]]
        else:
            cur = None if d.get("player_page") == "new" else live_text(d["player"])
            if d.get("player_page") == "new" and live_text(d["player"]) is not None:
                raise SystemExit(f"{d['player']} already exists on the wiki; set player_page to existing")
        players[d["player"]] = player_page(d, cur)
    for name, body in players.items():
        emit(name, body)
    # Hub + format pages are rebuilt from generate_decktech.py, so they must carry every
    # data-file deck already live (ledger) plus this batch — not just this batch.
    live_ids = [str(i) for i in json.loads(LIVE_FILE.read_text(encoding="utf-8"))] if LIVE_FILE.exists() else []
    every = {str(d["id"]): d for d in [load_deck(i) for i in live_ids if i not in ids] + decks}
    for d in every.values():
        register_wayback(d)
    all_decks = list(every.values())
    emit("DeckTech decks", insert_hub_rows(gd.decktech_decks(), all_decks))
    for fmt in sorted({d["format"] for d in all_decks}):
        base = getattr(gd, FORMAT_BUILDERS[fmt])()
        emit(fmt, insert_format_sentences(base, fmt, [d for d in all_decks if d["format"] == fmt]))
    seen, lines = set(), []
    for t, rel in titles:
        if t not in seen:
            seen.add(t)
            lines.append(f"{t}\t{rel}")
    tsv = ROOT / f"y-{batch}.tsv"
    tsv.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    tar = ROOT / f"y-{batch}.tar"
    apply_sh = ROOT / f"apply-{batch}.sh"
    apply_sh.write_text(APPLY_TEMPLATE.format(batch=batch), encoding="utf-8", newline="\n")
    with tarfile.open(tar, "w") as tf:
        tf.add(tsv, arcname=tsv.name)
        tf.add(apply_sh, arcname=apply_sh.name)
        for fn in gemp_files:
            tf.add(GEMP_OUT / fn, arcname=f"gemp-import-{batch}/{fn}")
        for _, rel in [l.split("\t") for l in lines]:
            tf.add(ROOT / rel, arcname=rel)
    print("TSV", tsv.name, "n", len(lines), "TAR", tar.name)


APPLY_TEMPLATE = """#!/bin/bash
# DeckTech batch {batch}: upload GEMP importable decklists, then pages (apply-tsv.sh).
# Run on the VPS in /opt/swccg-wiki after: tar xf y-{batch}.tar
set -euo pipefail
export LANG=C.UTF-8
cd /opt/swccg-wiki
USER_NAME="${{EDIT_USER:-Admin}}"
if [ -d gemp-import-{batch} ] && ls gemp-import-{batch}/*.txt >/dev/null 2>&1; then
  docker exec swccg_wiki mkdir -p /tmp/gemp-import-{batch}
  docker cp gemp-import-{batch}/. swccg_wiki:/tmp/gemp-import-{batch}/
  docker exec swccg_wiki php maintenance/run.php importImages --user="$USER_NAME" \\
    --comment="DeckTech {batch} GEMP importable decklists" --extensions=txt --overwrite /tmp/gemp-import-{batch} || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi
bash apply-tsv.sh /opt/swccg-wiki/y-{batch}.tsv "DeckTech {batch}"
echo APPLY-{batch}-DONE
"""


def cmd_check(tsv: str, ids: list[str] | None = None) -> None:
    titles = [l.split("\t")[0] for l in Path(tsv).read_text(encoding="utf-8").splitlines() if l.strip()]
    bad = 0
    for i in range(0, len(titles), 40):
        for p in api(action="query", prop="info|flagged", titles="|".join(titles[i:i + 40]))["query"]["pages"]:
            ok = not p.get("missing") and (p.get("flagged") or {}).get("stable_revid") == p.get("lastrevid")
            if not ok:
                bad += 1
                print("NOT REVIEWED", p["title"])
    known_red = {"Category:2002"}
    for t in titles:
        p = api(action="parse", page=t, prop="links|categories")["parse"]
        red = [l["title"] for l in p["links"] if not l.get("exists") and l["title"] not in known_red and "&" not in l["title"]]
        if red:
            print("RED", t, red[:8])
    print(f"checked {len(titles)} not reviewed {bad}")
    if ids and not bad:
        for i in ids:  # once live: player page exists, GEMP file name is fixed
            f = DECKS / f"{i}.json"
            d = json.loads(f.read_text(encoding="utf-8"))
            if d.get("player_page") == "new":
                d["player_page"] = "existing"
            page = live_text(dest_title(d)) or ""
            m = re.search(r"GEMP Importable deck:\'\'\'\s*\[\[Media:([^|\]]+)", page)
            if m:
                d["gemp_file_live"] = m.group(1).strip()
            f.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        led = set(json.loads(LIVE_FILE.read_text(encoding="utf-8"))) if LIVE_FILE.exists() else set()
        led |= {int(i) for i in ids}
        LIVE_FILE.write_text(json.dumps(sorted(led)) + "\n", encoding="utf-8")
        print("LEDGER", sorted(led))


def cmd_learn(ids: list[str]) -> None:
    """Teach card_nicknames.json every posted-name -> card match confirmed in finished decks, so the
    next fetch resolves them automatically. A name already mapped to a different card is reported,
    never overwritten."""
    raw = json.loads(NICKNAMES.read_text(encoding="utf-8")) if NICKNAMES.exists() else {}
    by_key = {k.casefold(): k for k in raw}
    added, clash = 0, []
    for pid in ids:
        d = load_deck(pid)
        for r in d.get("cards", []) + d.get("shields", []):
            if len(r) < 4 or r[2] == "UNKNOWN" or not str(r[3]).startswith("posted: "):
                continue
            posted = re.sub(r"\s*\((?:fuzzy|exact|nickname|\?)\)$", "", r[3][8:]).strip()
            parsed = parse_card_list(posted)
            if len(parsed) != 1:
                continue
            name = parsed[0][1].strip()
            if not name or name.casefold() == r[1].casefold() or suggest(name, d["side"]) == ("exact", r[1]):
                continue
            k = by_key.get(name.casefold())
            if k is None:
                raw[name] = {"card": r[1], "seen": 1}
                by_key[name.casefold()] = name
                added += 1
            elif raw[k]["card"] == r[1]:
                raw[k]["seen"] = raw[k].get("seen", 1) + 1
            else:
                clash.append(f"{name!r}: has {raw[k]['card']!r}, deck {pid} says {r[1]!r}")
    NICKNAMES.write_text(json.dumps(dict(sorted(raw.items(), key=lambda kv: kv[0].casefold())), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"learned {added} new nicknames ({len(raw)} total)")
    for c in clash:
        print("CLASH", c)


def main(argv: list[str]) -> None:
    if len(argv) < 2:
        raise SystemExit(__doc__)
    cmd, args = argv[1], argv[2:]
    if cmd == "fetch":
        cmd_fetch(args)
    elif cmd == "wayback":
        cmd_wayback(args)
    elif cmd == "draft":
        for a in args:
            cmd_draft(a)
    elif cmd == "build":
        cmd_build(args[0], args[1:])
    elif cmd == "check":
        cmd_check(args[0], args[1:])
        cmd_learn(args[1:])  # live + verified: safe to learn from
    elif cmd == "learn":
        cmd_learn(args)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
