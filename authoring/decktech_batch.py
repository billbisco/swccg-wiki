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
    python decktech_batch.py check y-dt-batch-01.tsv    # after apply: reviewed + no new red links

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

import generate_decktech as gd  # noqa: E402
import wiki_cardlink as cl  # noqa: E402

# Original-era (2002) Virtual slips not yet in generate_decktech.ORIGINAL_VS.
# Posted "X (V)" in a 2002 deck dests the original slip page, not current virtual.
EXTRA_ORIGINAL_VS = {
    "Assault Rifle (V)": ("Assault Rifle (V) (Virtual Set 1)", "VS1O-07-Assault Rifle.png"),
}
for _k, _v in EXTRA_ORIGINAL_VS.items():
    gd.ORIGINAL_VS.setdefault(_k, _v)

DECKS = ROOT / "decktech-decks"
POSTS = ROOT / "decktech-posts"
WAYBACK_FILE = ROOT / "decktech-wayback.json"
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
    re.compile(r"^(\d+)\s*x\s*(.+)$", re.I),
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
        head = re.match(r"^([A-Za-z'/ ]+?)\s*(?:\([^)]*\))?\s*:?$", line)
        counted = bool(re.search(r"\([^)]*\)\s*:?$|:$", line)) and not re.search(r"\(\d+\)$", line) or bool(re.search(r"\(\d+\)\s*:?$", line)) and len(line.split()) <= 3
        if head and (counted or len(head.group(1).split()) == 1 or head.group(1).strip().lower() in ("admirals order", "admiral's order", "weapons/devices", "starting cards")):
            word = head.group(1).strip().lower().split("/")[0].split()[0] if head.group(1).strip() else ""
            word = word.rstrip("s")
            hit = difflib.get_close_matches(word, list(TYPE_HEADERS), n=1, cutoff=0.75)
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


def cmd_wayback(ids: list[str]) -> None:
    """Save live + Skilton copies to the Wayback Machine, all in parallel (~2 min per batch).

    web.archive.org/save is blocked from some cloud sandboxes; run this where it works
    (e.g. Bill's PC shell). Results merge into decktech-wayback.json.
    """
    from concurrent.futures import ThreadPoolExecutor
    data = json.loads(WAYBACK_FILE.read_text(encoding="utf-8")) if WAYBACK_FILE.exists() else {}
    jobs = [(pid, kind, url) for pid in ids for kind, url in (
        ("live", f"http://www.decktech.net/starwarsccg/deck/{pid}"),
        ("skilton", f"https://www.stephenskilton.com/decktech_archives/{pid}/"),
    ) if not data.get(pid, {}).get(kind)]

    def save(job):
        pid, kind, url = job
        try:
            req = urllib.request.Request("https://web.archive.org/save/" + url, headers=UA)
            with urllib.request.urlopen(req, context=CTX, timeout=240) as r:
                m = re.search(r"/web/(\d{14})/", r.geturl())
            return pid, kind, (f"https://web.archive.org/web/{m.group(1)}/{url.rstrip('/')}/" if m else None)
        except Exception as e:  # noqa: BLE001
            print("FAIL", pid, kind, type(e).__name__, e, flush=True)
            return pid, kind, None

    with ThreadPoolExecutor(max_workers=8) as ex:
        for pid, kind, url in ex.map(save, jobs):
            if url:
                data.setdefault(pid, {})[kind] = url
                print("SAVED", pid, kind, url, flush=True)
    WAYBACK_FILE.write_text(json.dumps(data, indent=1, sort_keys=True) + "\n", encoding="utf-8")


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
    bad = [r for r in d["cards"] if str(r[1]).startswith("??") or r[2] == "?"]
    if bad:
        raise SystemExit(f"{pid}: unresolved cards {bad[:5]}")
    return d


def dest_title(d: dict) -> str:
    if d.get("dest_title"):
        return d["dest_title"]
    tail = d["published_title"] if d.get("use_published_title") else ("DS" if d["side"] == "Dark" else "LS")
    pre = f"{d['event']} " if d.get("kind") == "tournament" else ""
    return f"{pre}{d['player']} {tail}"


def label(d: dict) -> str:
    return d["published_title"] if d.get("use_published_title") else f"DeckTech post {d['id']}"


def register_wayback(d: dict) -> None:
    wb = json.loads(WAYBACK_FILE.read_text(encoding="utf-8")) if WAYBACK_FILE.exists() else {}
    for kind, url in {**wb.get(str(d["id"]), {}), **d.get("wayback", {})}.items():
        gd.WAYBACK[(kind, d["id"])] = url


def rows_of(d: dict, key: str = "cards") -> list[tuple[int, str, str]]:
    return [(int(r[0]), r[1], r[2]) for r in d.get(key, [])]


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
    if d.get("description"):
        info.append(f"* '''Strategy:''' {d['description']}")
    shields = ""
    if d.get("shields"):
        sh = "\n".join(f"* {q}x {wc(n)}" for q, n, _ in rows_of(d, "shields"))
        shields = f"\n== Defensive Shields ==\n\nThese cards were posted as Defensive Shields outside the 60. They do not count toward the 60.\n\n{sh}\n"
    note = f"\n{d['shields_note']}\n" if d.get("shields_note") else ""
    see = ([] if d.get("player_page") == "none" else [f"* [[{d['player']}]]"]) + ([f"* [[{d['event']}]]"] if d.get("event") else []) + [
        "* [[DeckTech decks]]", "* [[Decklists]]", f"* [[{d['format']}]]"]
    return f"""{intro}{gd.post_ref(f"dt-{pid}", pid, lbl, byline)}

== Deck info ==
{chr(10).join(info)}

== Decklist ==

{gd.table_from_rows(rows_of(d), side_u)}
{shields}{note}
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
    text = gd.add_misc_row(current, player_row(d))
    text = gd.add_see_also(text, f"* [[{dest_title(d)}]]")
    text = gd.add_source_line(text, gd.post_source_bullets(pid, lbl))
    return gd.add_category(text, d["date"][:4])


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

    for d in decks:
        qty = sum(int(r[0]) for r in d["cards"])
        print(f"{d['id']} {dest_title(d)} qty={qty}")
        gd.print_lookups(rows_of(d), d["side"].upper())
        emit(dest_title(d), deck_page(d))
        if d.get("player_page") == "none":
            continue
        cur = None if d.get("player_page") == "new" else live_text(d["player"])
        if d.get("player_page") == "new" and live_text(d["player"]) is not None:
            raise SystemExit(f"{d['player']} already exists on the wiki; set player_page to existing")
        emit(d["player"], player_page(d, cur))
    emit("DeckTech decks", insert_hub_rows(gd.decktech_decks(), decks))
    for fmt in sorted({d["format"] for d in decks}):
        base = getattr(gd, FORMAT_BUILDERS[fmt])()
        emit(fmt, insert_format_sentences(base, fmt, [d for d in decks if d["format"] == fmt]))
    seen, lines = set(), []
    for t, rel in titles:
        if t not in seen:
            seen.add(t)
            lines.append(f"{t}\t{rel}")
    tsv = ROOT / f"y-{batch}.tsv"
    tsv.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    tar = ROOT / f"y-{batch}.tar"
    with tarfile.open(tar, "w") as tf:
        tf.add(tsv, arcname=tsv.name)
        for _, rel in [l.split("\t") for l in lines]:
            tf.add(ROOT / rel, arcname=rel)
    print("TSV", tsv.name, "n", len(lines), "TAR", tar.name)


def cmd_check(tsv: str) -> None:
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
        cmd_check(args[0])
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main(sys.argv)
