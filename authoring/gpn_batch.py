#!/usr/bin/env python3
"""Game Players Network decks as data files (2026-10-10, Claude) — same flow as decktech_batch.py.

    python3 gpn_batch.py draft IDS...          # gpn-decks/id-N.html -> decktech-decks/gpn-N.json (suggestions)
    (finish each file: /home/claude/finish.py finish("gpn-N", rows, ...) — every card exact)
    python3 gpn_batch.py build BATCH IDS...    # pages, player pages, hub rows, GEMP files, TSV/tar, apply script
    python3 gpn_batch.py check TSV IDS...      # FlaggedRevs + red links, ledger gpn-live.json, learn nicknames

Pages match the layout of the earlier GPN pages (generate_gpn_decks.py, listing pages 63-13).
Original-era virtual cards dest to "X (V) (Virtual Set N)" pages chosen by post date (wiki_cardlink.ovs_pick).
"""
from __future__ import annotations

import json
import re
import sys
import tarfile
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import decktech_batch as b  # noqa: E402
import gemp_importable as gi  # noqa: E402
import generate_decktech as gd  # noqa: E402
import generate_gpn_decks as g  # noqa: E402
import wiki_cardlink as cl  # noqa: E402

DECKS = ROOT / "decktech-decks"
LIVE = ROOT / "gpn-live.json"
GEMP_OUT = ROOT / "gemp-import-gpn-data"
HUB = "Game Players Network decks"
PAGES_FILE = ROOT / "gpn-pages.json"  # id -> listing page (pages 12..1, Claude's captures)


def iso(posted: str) -> str:
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", posted or "")
    return f"{int(m.group(3)):04d}-{int(m.group(1)):02d}-{int(m.group(2)):02d}" if m else ""


def page_of(did: int) -> int:
    pages = json.loads(PAGES_FILE.read_text()) if PAGES_FILE.exists() else {}
    return int(pages.get(str(did), g.ID_TO_PAGE.get(did, 0)))


# ---------------------------------------------------------------- draft

def suggest_gpn(name: str, side: str, date_iso: str) -> tuple[str, str]:
    st, card = b.suggest(name, side)
    if re.search(r"(?i)\(v\)|virtual|\bv-?card\b", name) or (card.endswith("(V)") and st != "exact"):
        base = re.sub(r"(?i)\s*\((?:v|virtual|vsc?)\)|\s*virtual|\s*v-?card", "", name).strip()
        st2, c2 = b.suggest(base, side)
        page, _ = cl.ovs_pick(c2 or base, date_iso)
        if page:
            return "ovs", page
    return st, card


def cmd_draft(ids: list[str]) -> None:
    for did in map(int, ids):
        path = g.CACHE / f"id-{did}.html"
        if not path.exists():
            print("NOFILE", did)
            continue
        rec = g.parse_deck_html(path)
        side_u = g.infer_side(rec["rows"], rec["title"], rec["description"])
        side = "Dark" if side_u == "DARK" else "Light"
        d_iso = iso(rec["posted"])
        cards = []
        for q, n in rec["rows"]:
            if n.casefold() == rec["title"].casefold():
                continue
            st, card = suggest_gpn(n, side, d_iso)
            t = card if st in ("exact", "nickname", "ovs") else f"?? {n}"
            cards.append([q, t, b.card_type(card) if card else "?", f"posted: {n} ({st})"])
        handle = rec["author"]
        player = g.player_dest(handle)
        d = {
            "id": f"gpn-{did}", "gpn_id": did, "source": "gpn", "page": page_of(did),
            "posted": rec["posted"], "date": d_iso, "byline": handle, "player": player,
            "player_page": "existing" if b.live_text(player) is not None else "new",
            "published_title": rec["title"], "use_published_title": did not in g.WITHHELD_TITLE,
            "category": rec["category"], "url": rec["url"], "side": side,
            "description": rec["description"], "strategy": rec["strategy"],
            "starting": {"card": None, "interrupt": None, "effect": None},
            "cards": cards, "shields": [], "shields_note": None, "notes": [],
        }
        out = DECKS / f"gpn-{did}.json"
        if out.exists():
            print("EXISTS", out.name, "(edit it instead)")
            continue
        out.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        bad = sum(1 for c in cards if c[1].startswith("??"))
        print(f"DRAFT gpn-{did} pg{d['page']} {side} {handle!r} {rec['title'][:50]!r} rows={len(cards)} qty={sum(c[0] for c in cards)} unresolved={bad}")


# ---------------------------------------------------------------- build

def load(did) -> dict:
    return json.loads((DECKS / f"gpn-{did}.json").read_text(encoding="utf-8"))


def title_of(d: dict) -> str:
    if not d.get("use_published_title", True):
        return g.WITHHELD_TITLE.get(d["gpn_id"]) or f"{d['player']} {'DS' if d['side'] == 'Dark' else 'LS'}"
    return g.wiki_title_for(d["byline"], d["published_title"], d["gpn_id"])


def fmt_of(d: dict) -> str:
    vs = [cl.ovs_set(r[1]) for r in d["cards"] if "(Virtual Set" in r[1]]
    vs += [int(m.group(1)) for r in d["cards"] for m in [re.search(r"Virtual Set (\d+)", gd.ORIGINAL_VS.get(r[1], ("",))[0])] if m]
    if vs:
        return f"Premiere - Original VS{max(vs)}"
    nums = []
    for r in d["cards"]:
        try:
            c = gi.lookup(r[1], d["side"], None)
            n = gi.set_num(c["cardId"])
            if n <= 20:
                nums.append(n)
        except KeyError:
            pass
    hi = max(nums) if nums else 9
    for threshold, wiki_fmt, _code in g.SET_FORMAT:
        if hi >= threshold:
            return wiki_fmt
    return "Premiere - Death Star II"


def gemp(d: dict, fmt: str, taken: set[str]) -> tuple[str | None, list[str]]:
    rows, omitted = [], []
    allowed = gi.load_format_sets().get("open_no_virtual")
    for r in d["cards"]:
        q, t = int(r[0]), r[1]
        if t in gd.ORIGINAL_VS or "(Virtual Set" in t or r[2] in ("DEFENSIVE_SHIELD", "UNKNOWN"):
            omitted.append(re.sub(r" \(Virtual Set \d+\)$", "", t))
            continue
        try:
            gi.lookup(t, d["side"], allowed)
            rows.append((q, t, None))
        except KeyError:
            omitted.append(t)
    if not rows:
        return None, omitted
    xml, _ = gi.xml_for(rows, d["side"], "open_no_virtual")
    st = (d.get("starting") or {}).get("card") or d["published_title"]
    who = d["byline"]
    last = who.split()[-1] if who.split() else who
    if last.isdigit() or len(last) <= 2:
        who = re.sub(r'["*?<>#\[\]{}\s]+', "", who)
    fn = gi.safe_deck_filename(gi.deck_name(fmt, b._arch(st), who, d["side"], d["date"][:4], "GPN")) + ".txt"
    fn = re.sub(r"\s+", " ", fn.replace("_", " "))
    prior = re.search(r"\[\[Media:([^|\]]+?\.txt) ?\|", b.live_text(title_of(d)) or "")
    if prior:
        fn = prior.group(1).strip()
    elif fn.lower() in taken or b.file_exists(fn):
        fn = gi.safe_deck_filename(fn[:-4].rsplit(" GPN", 1)[0] + f" {d['gpn_id']}") + ".txt"
    taken.add(fn.lower())
    GEMP_OUT.mkdir(exist_ok=True)
    (GEMP_OUT / fn).write_text(xml, encoding="utf-8", newline="\n")
    return fn, omitted


def page_body(d: dict, title: str, fmt: str, fn: str | None, omitted: list[str]) -> str:
    side_u = d["side"].upper()
    st = d.get("starting") or {}
    start = st.get("card")
    start_field = gd.wiki_card(start, side_u) if start else "—"
    vis = (start or d["published_title"]).split(" / ")[0]
    rows = b.rows_of(d)
    n = sum(q for q, _, _ in rows) + sum(int(r[0]) for r in d["cards"] if r[2] == "UNKNOWN")
    intro_bits = [d["description"].strip()] if d.get("description", "").strip() else []
    if n != 60:
        intro_bits.append(f"The published list has {n} cards.")
    intro_sec = "== Introduction ==\n\n" + "\n\n".join(intro_bits) + "\n\n" if intro_bits else ""
    strat = (d.get("strategy") or "").strip()
    after_sec = f"\n== Strategy ==\n\n{strat}\n" if strat else ""
    download = ""
    if fn:
        download = gi.wiki_download_line(fn)
        if omitted:
            download += " (omits " + ", ".join(dict.fromkeys(omitted)) + ": no GEMP blueprint)"
    info = [f"* '''Player:''' {g.player_link(d['byline'])}", f"* '''Published:''' {g.display_date(d['posted'])} (Game Players Network)",
            f"* '''GPN category:''' {d['category']}", f"* '''Format:''' [[{fmt}]]", f"* '''Side:''' [[{d['side']}]]",
            f"* '''Starting Card:''' {start_field}"]
    for k, lab in (("interrupt", "Starting Interrupt"), ("effect", "Starting Effect")):
        if st.get(k):
            info.append(f"* '''{lab}:''' {gd.wiki_card(st[k], side_u)}")
    info.append(f"* '''Strategy:''' {vis}")
    if download:
        info.append(download)
    shields = ""
    if d.get("shields"):
        sh = "\n".join(f"* {q}x {b.shield_link(nm, d['side']) or gd.wiki_card(nm, side_u)}" for q, nm, _ in b.rows_of(d, "shields"))
        shields = f"\n== Defensive Shields ==\n\nThese cards were posted as Defensive Shields outside the deck.\n\n{sh}\n"
    shnote = f"\n{d['shields_note']}\n" if d.get("shields_note") else ""
    notes = ""
    if d.get("notes"):
        notes = "\n== Notes ==\n\n" + "\n".join(f"* {x}" for x in d["notes"]) + "\n"
    withheld = " The published title is not used as the page title; it is kept in the source citation." if not d.get("use_published_title", True) else ""
    year = d["date"][:4] or "2003"
    pg = d.get("page") or 0
    return f"""'''{title}''' is a [[{d['side']}]] constructed list published on [[Game Players Network]].{withheld}

== Deck info ==
{chr(10).join(info)}

{intro_sec}== Decklist ==

{gd.table_from_rows(rows, side_u)}
{b.unknown_note(d)}{shields}{shnote}{notes}{after_sec}
== See also ==

* [[Game Players Network decks]]
* {g.player_link(d['byline'])}
* [[Game Players Network]]
{"* [[GEMP importable decklist]]" if fn else ""}

== Sources ==

* [{d['url']} {d['published_title']}] (Wayback, {g.DETAIL_TS})
* [{g.listing_url(pg)} GPN Star Wars Decks page {pg}] (Wayback, {g.INDEX_TS})

{g.CATS}[[Category:Decklists]]
[[Category:{year}]]
[[Category:Game Players Network]]
"""


def player_text(d: dict, title: str, current: str | None) -> str:
    dest = g.player_dest(d["byline"])
    bit = f"* [[{title}]] ({d['side'][0]}S, {g.display_date(d['posted'])})"
    if current is None:
        note = g.HANDLE_NOTE.get(d["byline"], "")
        lead = f" {note.rstrip('.')}." if note else ""
        hat = f" For the card of that name, see [[{d['byline']}]]." if dest.endswith(" (GPN)") and dest != d["byline"] else ""
        return (f"'''{d['byline']}''' published constructed lists on [[Game Players Network]].{lead}{hat}\n\n== Decklists ==\n\n{bit}\n\n"
                f"== See also ==\n\n* [[Game Players Network decks]]\n* [[Decklists]]\n\n{g.CATS}[[Category:Players]]\n")
    if f"[[{title}]]" in current:
        return current
    if "== Decklists ==" in current:
        i = current.index("== Decklists ==")
        nxt = re.search(r"^==[^=]", current[i + 15:], re.M)
        at = i + 15 + (nxt.start() if nxt else len(current) - i - 15)
        return current[:at].rstrip("\n") + "\n" + bit + "\n\n" + current[at:].lstrip("\n")
    if "== See also ==" in current:
        return current.replace("== See also ==", f"== Decklists ==\n\n{bit}\n\n== See also ==", 1)
    cat = re.search(r"^\[\[Category:", current, re.M)
    at = cat.start() if cat else len(current)
    return current[:at].rstrip("\n") + f"\n\n== Decklists ==\n\n{bit}\n\n" + current[at:]


def hub_text(current: str, new_rows: list[tuple[tuple, str]], pages: set[int]) -> str:
    start = current.index('{| class="wikitable sortable"')
    end = current.index("\n|}", start)
    body = current[start:end]
    head, _, rest = body.partition("\n|-\n")
    rows = [r for r in rest.split("\n|-\n") if r.strip()]
    have = {r for r in rows}

    def key(r: str):
        m = re.match(r"\| (\d{1,2}) (\w+) (\d{4})", r)
        if not m:
            return (0, 0, 0)
        mon = [k for k, v in enumerate(g.MONTHS) if v == m.group(2)]
        return (int(m.group(3)), mon[0] if mon else 0, int(m.group(1)))
    for _k, r in new_rows:
        if r not in have:
            rows.append(r)
    rows.sort(key=key)
    table = head + "\n|-\n" + "\n|-\n".join(rows)
    text = current[:start] + table + current[end:]
    for pg in sorted(pages, reverse=True):
        line = f"* [{g.listing_url(pg)} GPN Star Wars Decks page {pg}] (Wayback, 30 April 2005)"
        if line not in text and f"pg={pg}]" not in text and f"pg={pg} " not in text:
            anchor = text.find("* [https://web.archive.org/web/20050327114018/")
            text = text[:anchor] + line + "\n" + text[anchor:] if anchor >= 0 else text
    return text


def cmd_build(batch: str, ids: list[str]) -> None:
    pages_dir = ROOT / "pages"
    pages_dir.mkdir(exist_ok=True)
    titles: list[tuple[str, str]] = []
    taken: set[str] = set()
    files = []
    hub_rows = []
    players: dict[str, str] = {}
    pgs = set()
    for did in ids:
        d = load(did)
        bad = [r for r in d["cards"] if r[2] == "?" or r[1].startswith("??")]
        if bad:
            raise SystemExit(f"gpn-{did}: unresolved {bad}")
        fmt = fmt_of(d)
        title = title_of(d)
        fn, omitted = gemp(d, fmt, taken)
        if fn:
            files.append(fn)
        path = gd.write_page(title, page_body(d, title, fmt, fn, omitted))
        titles.append((title, f"pages/{path.name}"))
        dest = g.player_dest(d["byline"])
        cur = players.get(dest)
        if cur is None:
            cur = b.live_text(dest)
        players[dest] = player_text(d, title, cur)
        disp = d["published_title"].replace("|", "/").replace("’", "'").replace("‘", "'")
        cell = f"[[{title}]]" if not d.get("use_published_title", True) else f"[[{title}|{disp}]]"
        hub_rows.append(((), f"| {g.display_date(d['posted'])}\n| [[{fmt}]]\n| {cell}\n| [[{d['side']}]]\n| {g.player_link(d['byline'])}"))
        pgs.add(d.get("page") or 0)
        print(f"BUILT gpn-{did} {title!r} {fmt} qty={sum(int(r[0]) for r in d['cards'])} gemp={fn}")
    for dest, text in players.items():
        p = gd.write_page(dest, text)
        titles.append((dest, f"pages/{p.name}"))
    hub = hub_text(b.live_text(HUB), hub_rows, pgs)
    p = gd.write_page(HUB, hub)
    titles.append((HUB, f"pages/{p.name}"))
    tsv = ROOT / f"y-{batch}.tsv"
    tsv.write_text("".join(f"{t}\t{r}\n" for t, r in titles), encoding="utf-8")
    sh = ROOT / f"apply-{batch}.sh"
    sh.write_text(b.APPLY_TEMPLATE.format(batch=batch).replace("DeckTech", "GPN"), encoding="utf-8", newline="\n")
    tar = ROOT / f"y-{batch}.tar"
    with tarfile.open(tar, "w") as tf:
        tf.add(tsv, arcname=tsv.name)
        tf.add(sh, arcname=sh.name)
        for fn in files:
            tf.add(GEMP_OUT / fn, arcname=f"gemp-import-{batch}/{fn}")
        for _, rel in titles:
            tf.add(ROOT / rel, arcname=rel)
    print("TSV", tsv.name, "n", len(titles), "GEMP", len(files), "TAR", tar.name)


def cmd_check(tsv: str, ids: list[str]) -> None:
    titles = [l.split("\t")[0] for l in (ROOT / tsv).read_text(encoding="utf-8").splitlines() if "\t" in l]
    bad = 0
    for i in range(0, len(titles), 50):
        d = b.api(action="query", titles="|".join(titles[i:i + 50]), prop="flagged")
        for p in d["query"]["pages"]:
            f = p.get("flagged")
            if p.get("missing") or not f or f.get("pending_since"):
                bad += 1
                print("NOT REVIEWED", p["title"])
    live = set(json.loads(LIVE.read_text())) if LIVE.exists() else set()
    live |= {int(x) for x in ids}
    LIVE.write_text(json.dumps(sorted(live)) + "\n")
    print("checked", len(titles), "not reviewed", bad, "gpn live", len(live))
    b.cmd_learn([f"gpn-{x}" for x in ids])


if __name__ == "__main__":
    cmd, args = sys.argv[1], sys.argv[2:]
    {"draft": cmd_draft, "build": lambda a: cmd_build(a[0], a[1:]), "check": lambda a: cmd_check(a[0], a[1:])}[cmd](args)
