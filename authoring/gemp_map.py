#!/usr/bin/env python3
"""Wiki card title -> GEMP blueprint (title + id), with an audit of whether the id really exists in GEMP.

Bill 2026-10-17: every GEMP importable decklist must only use blueprint ids that our GEMP (billbisco/swccg-gemp) actually
has, and there should be one table mapping each transcribed card to its wiki article, GEMP card name and GEMP card id.
swccg-gemp is the target; PC GEMP compatibility (same ids, no conflicts) is kept where reasonable but is secondary.

Resolution order for a deck row (side + wiki page title):
  1. gemp-card-overrides.tsv (side, wiki title -> gemp id) for the few titles that can't be derived.
  2. The wiki title as-is, then with "•", "(Dark)"/"(Light)" and trailing set disambiguators stripped
     ("Tatooine (Light) (Coruscant)" -> "Tatooine", preferring the CORUSCANT printing).
  3. gemp_importable.lookup as the last resort (aliases, prefix matches).

Existence is checked against the Java card classes of billbisco/swccg-gemp (the target) and, for the compatibility column,
PlayersCommittee/gemp-swccg-public, when those clones are present, else against the blueprint JSON only.
"""
from __future__ import annotations

import csv
import glob
import json
import os
import re
import sys
from pathlib import Path

import gemp_importable as gi

ROOT = Path(__file__).resolve().parent
OVERRIDES = ROOT / "gemp-card-overrides.tsv"
MAP_TSV = ROOT / "gemp-card-map.tsv"
UPSTREAM = Path(os.environ.get("GEMP_UPSTREAM", "/home/claude/playerscommittee/gemp-swccg-public"))
FORK = Path(os.environ.get("GEMP_FORK", "/home/claude/billbisco/swccg-gemp"))

# wiki set disambiguator -> GEMP set number (the part of the blueprint id before "_")
SET_HINT = {
    "Premiere": 1, "A New Hope": 2, "Hoth": 3, "Dagobah": 4, "Cloud City": 5, "Jabba's Palace": 6,
    "Special Edition": 7, "Endor": 8, "Death Star II": 9, "Reflections II": 10, "Tatooine": 11, "Coruscant": 12,
    "Reflections III": 13, "Reflections III: A Collector's Bounty": 13, "Theed Palace": 14,
    "Jedi Pack": 102, "Rebel Leader Pack": 103, "First Anthology": 105, "Official Tournament Sealed Deck": 106,
    "Second Anthology": 107, "Enhanced Premiere": 108, "Enhanced Cloud City": 109, "Enhanced Jabba's Palace": 110,
    "Third Anthology": 111, "Jabba's Palace Sealed Deck": 112,
}
SIDE_WORDS = {"Dark", "Light"}

_JAVA: dict[str, set[str]] | None = None


def _java_ids(root: Path) -> set[str]:
    out = set()
    for p in glob.glob(str(root / "**" / "Card*_*.java"), recursive=True):
        m = re.match(r"^Card(\d+)_0*(\d+)$", os.path.basename(p)[:-5])
        if m:
            out.add(f"{m.group(1)}_{m.group(2)}")
    return out


_JIDX: list[dict] | None = None


def java_index() -> list[dict]:
    """Every card class in public GEMP and Bill's fork: cardId, title, side, cardSubtype, source."""
    global _JIDX
    if _JIDX is None:
        seen: dict[str, dict] = {}
        for src, root in (("gemp", UPSTREAM), ("fork-only", FORK)):
            if not root.exists():
                continue
            for p in glob.glob(str(root / "**" / "Card*_*.java"), recursive=True):
                m = re.match(r"^Card(\d+)_0*(\d+)$", os.path.basename(p)[:-5])
                if not m:
                    continue
                cid = f"{m.group(1)}_{m.group(2)}"
                if cid in seen:
                    continue
                head = open(p, encoding="utf-8", errors="replace").read(4000)
                t = re.search(r"^\s*\* Title: (.+)$", head, re.M)
                if not t:
                    continue
                side = "DARK" if "/dark/" in p.replace(os.sep, "/") else "LIGHT" if "/light/" in p.replace(os.sep, "/") else (
                    "DARK" if "Side.DARK" in head else "LIGHT")
                sub = re.search(r"^\s*\* Subtype: (.+)$", head, re.M)
                typ = re.search(r"^\s*\* Type: (.+)$", head, re.M)
                seen[cid] = {"cardId": cid, "title": t.group(1).strip(), "side": side, "source": src,
                             "cardSubtype": (sub.group(1).strip().upper() if sub else ""),
                             "cardCategory": (typ.group(1).strip().upper().replace(" ", "_") if typ else "")}
        _JIDX = list(seen.values())
    return _JIDX


_ALL: list[dict] | None = None


def all_cards() -> list[dict]:
    """Blueprint JSON cards plus card classes the JSON lacks (Java headers)."""
    global _ALL
    if _ALL is None:
        db = gi.load_cards()
        jx = {c["cardId"]: c for c in java_index()}
        merged = []
        for c in db:  # the Java header title is the server's own (it keeps "(AI)"/"(V)" that the JSON drops)
            j = jx.get(c["cardId"])
            merged.append({**c, "title": j["title"]} if j else c)
        have = {c["cardId"] for c in db}
        _ALL = merged + [c for c in jx.values() if c["cardId"] not in have]
    return _ALL


_DBT: dict[str, str] | None = None


def db_title(card_id: str) -> str | None:
    global _DBT
    if _DBT is None:
        _DBT = {c["cardId"]: c["title"] for c in gi.load_cards()}
    return _DBT.get(card_id)


def java_ids() -> dict[str, set[str]]:
    global _JAVA
    if _JAVA is None:
        _JAVA = {"upstream": _java_ids(UPSTREAM) if UPSTREAM.exists() else set(),
                 "fork": _java_ids(FORK) if FORK.exists() else set()}
    return _JAVA


def status_of(card_id: str) -> str:
    """Bill 2026-10-17: the target GEMP is billbisco/swccg-gemp; PC GEMP compatibility is secondary.
    'both' = swccg-gemp and PC GEMP have the card class; 'swccg-gemp' = only ours (PC hasn't coded it);
    'pc-only' = only PC GEMP (swccg-gemp should catch up); 'missing' = neither has it (a swccg-gemp coding to-do)."""
    j = java_ids()
    if not j["fork"] and not j["upstream"]:
        return "both" if any(c["cardId"] == card_id for c in gi.load_cards()) else "missing"
    f, u = card_id in j["fork"], card_id in j["upstream"]
    return "both" if f and u else "swccg-gemp" if f else "pc-only" if u else "missing"


def in_target(card_id: str) -> bool:
    """True when swccg-gemp (our GEMP) has the card, so the id may go in an importable file."""
    return status_of(card_id) in ("both", "swccg-gemp")


def _norm(t: str) -> str:
    t = t.replace("•", "").replace("’", "'").replace("“", '"').replace("”", '"')
    return re.sub(r"\s+", " ", t).strip().casefold()


def _norm_q(t: str) -> str:
    return _norm(t).replace('"', "'")


def overrides() -> dict[tuple[str, str], str]:
    out = {}
    if OVERRIDES.exists():
        for row in csv.DictReader(OVERRIDES.open(encoding="utf-8"), delimiter="\t"):
            out[(row["side"].upper(), row["wiki_title"])] = row["gemp_id"]
    return out


def strip_title(title: str) -> tuple[list[str], list[str]]:
    """Return candidate GEMP titles (most specific first) and the set hints found."""
    t = title.replace("•", "").strip()
    cands, hints = [t], []
    while True:
        m = re.match(r"^(.*\S) \(([^()]+)\)$", t)
        if not m:
            break
        t, tag = m.group(1), m.group(2)
        if tag in SET_HINT:
            hints.append(SET_HINT[tag])
        elif tag not in SIDE_WORDS:
            # a real part of the card title, e.g. "(Docking Bay)", "(Leebo)": keep trying shorter forms too
            pass
        cands.append(t)
    for c in list(cands):
        if " / " in c:
            cands.append(c.split(" / ", 1)[0])
        if c in gi.TITLE_ALIAS:
            cands.append(gi.TITLE_ALIAS[c])
    return list(dict.fromkeys(cands)), hints


def resolve(title: str, side: str, allowed: set[int] | None = None) -> tuple[dict | None, str]:
    side_u = "LIGHT" if side.upper() in {"LS", "LIGHT"} else "DARK"
    ov = overrides().get((side_u, title))
    allc = all_cards()
    pool = [c for c in allc if (c.get("side") or "").upper() == side_u
            and "DEFENSIVE_SHIELD" not in (c.get("cardCategory") or "").upper()]
    if ov:
        hit = [c for c in allc if c["cardId"] == ov]
        return (hit[0] if hit else {"cardId": ov, "title": title, "side": side_u}), "override"
    cands, hints = strip_title(title)
    for cand in cands:
        for norm in (_norm, _norm_q):
            hit = [c for c in pool if norm(c.get("title") or "") == norm(cand)]
            if not hit:
                continue
            printed = [c for c in hit if gi.set_num(c["cardId"]) < 200]
            hit = printed or hit
            if hints:
                h = [c for c in hit if gi.set_num(c["cardId"]) in hints]
                if h:
                    hit = h
            if allowed:
                a = [c for c in hit if gi.set_num(c["cardId"]) in allowed]
                if a:
                    hit = a
            # ours first, then the id PC GEMP shares (cross-compatibility), then the lowest id
            hit.sort(key=lambda c: (not in_target(c["cardId"]), status_of(c["cardId"]) != "both") + tuple(gi.card_id_key(c["cardId"])))
            return hit[0], "title"
    try:  # aliases and prefix matches from the older importer
        c = gi.lookup(title.replace("•", ""), side_u, allowed)
        return c, "fallback"
    except KeyError:
        return None, "none"


def build_map(write: bool = True) -> list[dict]:
    """One row per (side, wiki title) used in any DeckTech deck."""
    import generate_decktech as gd
    rows: dict[tuple[str, str], dict] = {}
    for f in sorted(glob.glob(str(ROOT / "decktech-decks" / "*.json"))):
        d = json.load(open(f, encoding="utf-8"))
        side = d["side"].upper()
        for r in d["cards"] + d.get("shields", []):
            t, typ = r[1], r[2]
            key = (side, t)
            row = rows.setdefault(key, {"side": side.title(), "wiki_title": t, "type": typ, "posted": {}, "decks": set()})
            row["decks"].add(d["id"])
            if len(r) > 3 and str(r[3]).startswith("posted: "):
                p = re.sub(r"\s*\((?:fuzzy|exact|nickname|\?)\)$", "", r[3][8:]).strip()
                row["posted"][p] = row["posted"].get(p, 0) + 1
    out = []
    for (side, t), row in sorted(rows.items(), key=lambda kv: (kv[0][0], kv[0][1].casefold())):
        if row["type"] == "UNKNOWN":
            card, how, st = None, "unknown", "not-a-card"
        elif row["type"] == "DEFENSIVE_SHIELD":
            card, how, st = None, "shield", "not-in-60"
        elif t in gd.ORIGINAL_VS or "(Virtual Set" in t:
            card, how, st = None, "original-vs", "original-VS-slip"
        else:
            card, how = resolve(t, side)
            st = status_of(card["cardId"]) if card else "missing"
        out.append({
            "side": row["side"], "wiki_article": t, "gemp_card_name": card["title"] if card else "",
            "gemp_card_id": card["cardId"] if card else "", "gemp_status": st, "matched_by": how,
            "decks": len(row["decks"]),
            "transcribed_as": " | ".join(k for k, _ in sorted(row["posted"].items(), key=lambda kv: -kv[1])[:8]),
        })
    if write:
        cols = list(out[0].keys())
        with MAP_TSV.open("w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n")
            w.writeheader()
            w.writerows(out)
    return out


if __name__ == "__main__":
    rows = build_map()
    from collections import Counter
    print(Counter(r["gemp_status"] for r in rows))
    for r in rows:
        if r["gemp_status"] in ("missing", "swccg-gemp", "pc-only"):
            print(r["gemp_status"], r["side"], r["wiki_article"], "->", r["gemp_card_name"], r["gemp_card_id"], f"({r['decks']} decks)")
    sys.exit(0)
