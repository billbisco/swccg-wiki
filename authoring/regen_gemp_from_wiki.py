#!/usr/bin/env python3
"""Regenerate GEMP importable decklists from the LIVE deck pages, through gemp_map (Bill 2026-10-17).

Works on any deck page that has a `* '''GEMP Importable deck:''' [[Media:NAME.txt|Download]]` line, whoever made it
(DeckTech, GPN, tournament dests). Reads the page's `== Decklist ==` CardLink rows and its Side / Format, resolves each
wiki title to a swccg-gemp blueprint id, writes NAME.txt, and compares it to the file on the wiki.

  python3 regen_gemp_from_wiki.py --category "Game Players Network" --out regen-gpn
  python3 regen_gemp_from_wiki.py --titles-file titles.txt --out regen-x

Output dir: NAME.txt files that differ from the wiki, pages/*.wiki for pages whose GEMP line changes, a TSV for
wiki_api_apply (pages), and report.tsv (one row per page: title, file, status, omitted, changed ids).
Rules:
  * Cards outside the 60 (`== Defensive Shields ==`, "outside the 60" sections) are left out.
  * In a "Premiere - Original VS*" deck a "(V)" title is an Original Virtual slip: left out (swccg-gemp has not coded the
    Original Virtual cards yet; mapping it would land on a PC "(V)" or printed card).
  * Only ids swccg-gemp has go in the file; the rest are named in the GEMP line "(omits …: not in GEMP)".
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sys
import time
from collections import Counter
import urllib.parse
import urllib.request
from pathlib import Path

import gemp_importable as gi
import gemp_map

API = "https://wiki.swccg.com/api.php"
GEMP_LINE = re.compile(r"^\* '''GEMP Importable deck:''' \[\[Media:([^|\]]+?)\s*\|Download\]\].*$", re.M)


def api(**k):
    k.update(format="json", formatversion=2)
    for i in range(4):
        try:
            data = urllib.parse.urlencode(k).encode()
            return json.load(urllib.request.urlopen(urllib.request.Request(API, data=data), timeout=60))
        except Exception:
            if i == 3:
                raise
            time.sleep(2 + 3 * i)


def category_titles(cat: str) -> list[str]:
    out, cont = [], {}
    while True:
        r = api(action="query", list="categorymembers", cmtitle="Category:" + cat, cmlimit=500, cmnamespace=0, **cont)
        out += [m["title"] for m in r["query"]["categorymembers"]]
        if "continue" not in r:
            return out
        cont = r["continue"]


def page_texts(titles: list[str]) -> dict[str, str]:
    out = {}
    for i in range(0, len(titles), 50):
        r = api(action="query", titles="|".join(titles[i:i + 50]), prop="revisions", rvprop="content", rvslots="main")
        for p in r["query"]["pages"]:
            if p.get("revisions"):
                out[p["title"]] = p["revisions"][0]["slots"]["main"]["content"]
    return out


def file_sha1(names: list[str]) -> dict[str, str | None]:
    out = {}
    for i in range(0, len(names), 50):
        r = api(action="query", titles="|".join("File:" + n for n in names[i:i + 50]), prop="imageinfo", iiprop="sha1")
        norm = {n["to"]: n["from"] for n in r["query"].get("normalized", [])}
        for p in r["query"]["pages"]:
            t = norm.get(p["title"], p["title"])[5:]
            out[t] = (p.get("imageinfo") or [{}])[0].get("sha1")
    return out


def live_file(name: str) -> str:
    r = api(action="query", titles="File:" + name, prop="imageinfo", iiprop="url")
    ii = r["query"]["pages"][0].get("imageinfo")
    return urllib.request.urlopen(ii[0]["url"], timeout=60).read().decode("utf-8", "replace") if ii else ""


def decklist_rows(text: str) -> list[tuple[int, str]]:
    m = re.search(r"^== Decklist ==\s*$(.*?)(?=^== (?!Decklist))", text, re.M | re.S)
    body = m.group(1) if m else ""
    rows = []
    for q, title, _hint in gi.parse_wiki_cards(body):
        rows.append((q, title))
    return rows


def side_of(text: str) -> str | None:
    m = re.search(r"^\* '''Side:''' \[\[(Light|Dark)\]\]", text, re.M)
    return m.group(1) if m else None


def format_of(text: str) -> str:
    m = re.search(r"^\* '''Format:''' \[\[([^\]|]+)", text, re.M)
    return m.group(1) if m else ""


def build(text: str) -> tuple[str | None, list[str], list[str]]:
    side, fmt = side_of(text), format_of(text)
    if not side:
        return None, [], ["no Side"]
    original_vs = "Original VS" in fmt
    cards, omitted = [], []
    for q, t in decklist_rows(text):
        t = t.replace("•", "").strip()
        if (original_vs and re.search(r"\(V\)", t)) or "(Virtual Set" in t:
            omitted.append(t)
            continue
        card, _ = gemp_map.resolve(t, side)
        if not card and t.endswith(" (Dark)"):
            card, _ = gemp_map.resolve(t[:-7], side)
        if not card or not gemp_map.in_target(card["cardId"]):
            omitted.append(t)
            continue
        cards += [card] * q
    if not cards:
        return None, omitted, ["no importable cards"]
    lines = ['<?xml version="1.0" encoding="UTF-8" standalone="no"?>', "<deck>"]
    for c in cards:
        hz = "true" if (c.get("cardSubtype") or "").upper() == "SITE" else "false"
        title = gemp_map.db_title(c["cardId"]) or c["title"]
        lines.append(f'    <card blueprintId="{gi.escape(c["cardId"])}" horizontal="{hz}" '
                     f'title="{gi.escape(title, {chr(34): "&quot;"})}"/>')
    return "\n".join(lines + ["</deck>", ""]), list(dict.fromkeys(omitted)), []


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--category")
    ap.add_argument("--titles-file")
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    titles = category_titles(a.category) if a.category else [l.strip() for l in open(a.titles_file) if l.strip()]
    out = Path(a.out)
    (out / "files").mkdir(parents=True, exist_ok=True)
    (out / "pages").mkdir(exist_ok=True)
    texts = page_texts(titles)
    have = {t: GEMP_LINE.search(x) for t, x in texts.items()}
    names = [m.group(1).strip() for m in have.values() if m]
    shas = file_sha1(names)
    rep, tsv = [], []
    for t, x in sorted(texts.items()):
        m = have[t]
        if not m:
            continue
        fn = m.group(1).strip()
        xml, omitted, err = build(x)
        if err:
            rep.append([t, fn, "skip: " + "; ".join(err), ", ".join(omitted)])
            continue
        data = xml.encode("utf-8")
        file_changed = hashlib.sha1(data).hexdigest() != shas.get(fn)
        if file_changed and shas.get(fn):  # same cards in another order or title spelling is not worth a re-upload
            file_changed = Counter(re.findall(r'blueprintId="([^"]+)"', live_file(fn))) != Counter(
                re.findall(r'blueprintId="([^"]+)"', xml))
        if file_changed:
            (out / "files" / fn).write_bytes(data)
        line = m.group(0)[: m.group(0).index("|Download]]") + len("|Download]]")]  # keep the page's own link text
        if omitted:
            line += " (omits " + ", ".join(omitted) + ": not in GEMP)"
        mo = re.search(r"\(omits (.*): (?:no GEMP blueprint|not in GEMP)\)", m.group(0))
        if set((mo.group(1).split(", ") if mo else [])) == set(omitted):
            line = m.group(0)  # same omissions: leave the page alone
        new = x[:m.start()] + line + x[m.end():]
        page_changed = new != x
        if page_changed:
            p = out / "pages" / (re.sub(r'[\\/:*?"<>|]', "_", t.replace(" ", "_")) + ".wiki")
            p.write_text(new, encoding="utf-8")
            tsv.append(f"{t}\tpages/{p.name}\n")
        rep.append([t, fn, ("file+page" if file_changed and page_changed else "file" if file_changed else
                            "page" if page_changed else "same"), ", ".join(omitted)])
    (out / f"{out.name}.tsv").write_text("".join(tsv), encoding="utf-8")
    with (out / "report.tsv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["page", "file", "status", "omitted"])
        w.writerows(rep)

    print(Counter(r[2].split(":")[0] for r in rep), "pages", len(texts), "with GEMP line", len(names))
    return 0


if __name__ == "__main__":
    sys.exit(main())
