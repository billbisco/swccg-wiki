#!/usr/bin/env python3
"""Backfill GEMP Importable deck downloads for deck pages that are already live (2026-10-10).

Reads each live page, takes the cards from its '== Decklist ==' section only (never Defensive
Shields or the quoted post), builds the GEMP .txt, and writes the page with a download line.
Original-era (V) slips (no GEMP blueprint) are omitted and named on the page, as for new decks.

    python3 gemp_backfill.py build TITLES.json OUTDIR      # -> OUTDIR/{pages/*.wiki, gemp/*.txt, apply.tsv}

TITLES.json: [[page title, decktech id or null], ...]. Results are also recorded in
gemp-backfill.json (page title -> file name) so generate_decktech.py keeps the line on rebuilds.
"""
from __future__ import annotations

import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import gemp_importable as gi  # noqa: E402

API = "https://wiki.swccg.com/api.php"
UA = {"User-Agent": "swccg-wiki-dest/1.0 (GEMP backfill)"}
LEDGER = ROOT / "gemp-backfill.json"


def api(**p) -> dict:
    q = {"format": "json", "formatversion": "2", **p}
    req = urllib.request.Request(API + "?" + urllib.parse.urlencode(q), headers=UA)
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.loads(r.read().decode("utf-8"))


def live(titles: list[str]) -> dict[str, str]:
    out = {}
    for i in range(0, len(titles), 50):
        d = api(action="query", titles="|".join(titles[i:i + 50]), prop="revisions", rvprop="content", rvslots="main")
        for p in d["query"]["pages"]:
            if not p.get("missing"):
                out[p["title"]] = p["revisions"][0]["slots"]["main"]["content"]
    return out


def file_exists(fn: str) -> bool:
    p = api(action="query", titles="File:" + fn)["query"]["pages"][0]
    return not p.get("missing")


def decklist_section(text: str) -> str:
    m = re.search(r"^== *Decklist *==[ \t]*$", text, re.M)
    if not m:
        return ""
    nxt = re.search(r"^==[^=]", text[m.end():], re.M)
    return text[m.end(): m.end() + (nxt.start() if nxt else len(text))]


def field(text: str, name: str) -> str:
    m = re.search(rf"^\* '''{re.escape(name)}:'''\s*(.+)$", text, re.M)
    if not m:
        return ""
    v = re.sub(r"\{\{CardLink\|([^}|]+)\|[^}|]+(?:\|label=[^}]+)?\}\}", r"\1", m.group(1))
    return re.sub(r"\[\[([^\]|]+)(?:\|[^\]]+)?\]\]", r"\1", v).strip()


def arch_of(start: str) -> str:
    face = (start or "").split(" / ")[0]
    if face in gi.ARCHETYPE_ABBR or len(face) <= 10:
        return face
    return "".join(w[0] for w in re.findall(r"[A-Za-z0-9']+", face) if w[0].isalnum()).upper()


def format_key(fmt: str) -> str:
    sets = gi.load_format_sets()
    if fmt in sets:
        return fmt
    return "open_no_virtual"  # Original VS-era pools: printed Decipher cards; (V) slips have no blueprint


def resolve(title: str, side: str, fmt: str) -> dict:
    """GEMP blueprint for a wiki dest title. Falls back from 'Alter (Coruscant)' /
    'Proton Torpedoes (Theed Palace)' style disambiguated titles to the card of that set."""
    allowed = gi.load_format_sets().get(format_key(fmt))
    try:
        return gi.lookup(title, side, allowed)
    except KeyError:
        pass
    m = re.match(r"^(.+?)((?: \([^)]*\))+)$", title)
    if not m:
        raise KeyError(title)
    base = m.group(1)
    tags = [t.strip("() ").upper().replace(" ", "_").replace("'", "") for t in re.findall(r"\([^)]*\)", m.group(2))]
    cands = [c for c in gi.load_cards() if c["title"] == base and c["side"] == side.upper()]
    for c in cands:
        if c.get("expansionSet") in tags:
            return c
    if cands:
        return gi.lookup(base, side, allowed)
    raise KeyError(title)


def xml_from(cards: list[tuple[int, dict]]) -> str:
    from xml.sax.saxutils import escape
    lines = ['<?xml version="1.0" encoding="UTF-8" standalone="no"?>', "<deck>"]
    for q, c in cards:
        hid = "true" if gi.is_horizontal(c) else "false"
        lines += [f'    <card blueprintId="{escape(c["cardId"])}" horizontal="{hid}" title="{escape(c["title"])}"/>'] * q
    return "\n".join(lines + ["</deck>", ""])


def build(titles_json: Path, outdir: Path) -> None:
    want = json.loads(titles_json.read_text(encoding="utf-8"))
    pages = live([t for t, _ in want])
    (outdir / "pages").mkdir(parents=True, exist_ok=True)
    (outdir / "gemp").mkdir(parents=True, exist_ok=True)
    ledger = json.loads(LEDGER.read_text(encoding="utf-8")) if LEDGER.exists() else {}
    taken: set[str] = set()
    tsv, report = [], []
    for title, pid in want:
        text = pages.get(title)
        if text is None:
            report.append(f"MISSING PAGE {title}")
            continue
        if "GEMP Importable deck" in text:
            report.append(f"SKIP already has GEMP: {title}")
            continue
        side = field(text, "Side") or "Light"
        fmt = field(text, "Format")
        rows = gi.parse_wiki_cards(decklist_section(text))
        keep, omitted, bad = [], [], []
        for q, t, hint in rows:
            if "(Virtual Set" in t or t.endswith("(V)") or "(V) (" in t:
                omitted.append(t.split(" (Virtual Set")[0])
                continue
            try:
                keep.append((q, resolve(t, hint or side, fmt)))
            except KeyError:
                bad.append(t)
        if bad:
            report.append(f"UNMATCHED {title}: {bad}")
        if not keep:
            report.append(f"EMPTY {title}")
            continue
        xml, notes = xml_from(keep), []
        year = (re.search(r"(\d{4})", field(text, "Published") or "") or [None, None])[1]
        player = field(text, "Player") or title.split()[0]
        base = gi.safe_deck_filename(gi.deck_name(fmt, arch_of(field(text, "Starting Card")), player, side, year, "DeckTech"))
        fn = base + ".txt"
        if fn.lower() in taken or file_exists(fn):
            fn = gi.safe_deck_filename(gi.deck_name(fmt, arch_of(field(text, "Starting Card")), player, side, year, str(pid or ""))) + ".txt"
        fn = re.sub(r"\s+", " ", fn.replace("_", " "))
        if fn.lower() in taken or file_exists(fn):
            report.append(f"NAME CLASH {title}: {fn}")
            continue
        taken.add(fn.lower())
        (outdir / "gemp" / fn).write_text(xml, encoding="utf-8", newline="\n")
        line = gi.wiki_download_line(fn)
        why = []
        if omitted:
            why.append(", ".join(dict.fromkeys(omitted)) + ": no GEMP blueprint")
        if bad:
            why.append(", ".join(dict.fromkeys(bad)) + f": not a {side} card GEMP knows; this list's dest needs checking")
        if why:
            line += " (omits " + "; ".join(why) + ")"
        if re.search(r"^\* '''Strategy:'''", text, re.M):
            new = re.sub(r"^(\* '''Strategy:''')", line.replace("\\", "\\\\") + r"\n\1", text, count=1, flags=re.M)
        else:
            new = re.sub(r"^(\* '''Side:'''[^\n]*)", r"\1\n" + line.replace("\\", "\\\\"), text, count=1, flags=re.M)
        if new == text:
            report.append(f"NO INSERT POINT {title}")
            continue
        safe = re.sub(r'[\\/:*?"<>|]', "_", title).replace(" ", "_") + ".wiki"
        (outdir / "pages" / safe).write_text(new, encoding="utf-8", newline="\n")
        tsv.append(f"{title}\tpages/{safe}")
        ledger[title] = {"file": fn, "line": line}
        qty = sum(q for q, _ in keep)
        report.append(f"OK {title}: {fn} ({qty} cards{'; ' + '; '.join(notes[:3]) if notes else ''})")
    (outdir / "apply.tsv").write_text("\n".join(tsv) + "\n", encoding="utf-8")
    LEDGER.write_text(json.dumps(ledger, indent=1, ensure_ascii=False, sort_keys=True) + "\n", encoding="utf-8")
    print("\n".join(report))
    print(f"pages {len(tsv)}, files {len(list((outdir / 'gemp').glob('*.txt')))}")


if __name__ == "__main__":
    if len(sys.argv) != 4 or sys.argv[1] != "build":
        raise SystemExit(__doc__)
    build(Path(sys.argv[2]), Path(sys.argv[3]))
