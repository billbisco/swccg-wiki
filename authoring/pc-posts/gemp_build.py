#!/usr/bin/env python3
"""Build GEMP-importable deck files for a finalized batch and add the download line to each page.

python3 gemp_build.py <decks-canon.json> <final_dir> <event_token_map.json or ''>
Writes <final_dir>/gemp/<file>.txt, patches <final_dir>/pages/*.wiki (Deck info line), and
<final_dir>/gemp-report.txt (omitted cards per deck). Cards GEMP has no blueprint for are left out and named.
"""
import json, re, sys, pathlib
sys.path.insert(0, "/home/claude/swccg-wiki/authoring")
import gemp_importable as gi

gi.CARD_DB = pathlib.Path("/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json")
gi.FORMATS_JSON = pathlib.Path("/home/claude/swccg-gemp/src/gemp-swccg-server/src/main/resources/swccgFormats.json")

TOKEN = {"World Championship": "Worlds", "Match Play Championship": "MPC", "San Diego Grand Prix": "SDGP",
         "European Championship": "EC", "Texas Mini Worlds": "TMW", "Endor Grand Prix": "EGP",
         "U.S. National Championship": "Nats"}

decks = json.load(open(sys.argv[1]))
final = pathlib.Path(sys.argv[2])
out = final / "gemp"; out.mkdir(exist_ok=True)
rows_tsv = {l.split("\t")[0]: l.split("\t")[1] for l in (final / "titles.tsv").read_text(encoding="utf-8").splitlines() if l}
import unicodedata
def _nk(t):
    t = unicodedata.normalize("NFKD", t).encode("ascii", "ignore").decode().lower().replace("&", " and ")
    return re.sub(r"[^a-z0-9]+", "", t)
_NK = {}
for _r in json.load(open(gi.CARD_DB)):
    _NK.setdefault((_r.get("side"), _nk(_r["title"])), _r["title"])
allowed = None  # historical decks: full card pool (2015-era shields were later retired from Open)
taken, report, n_ok = set(), [], 0
import os
if os.environ.get("GEMP_TAKEN"):  # filenames already used by other batches on the wiki
    taken |= {l.strip().lower() for l in open(os.environ["GEMP_TAKEN"], encoding="utf-8") if l.strip()}
for d in decks:
    side = "DARK" if d["side"] == "DS" else "LIGHT"
    keep, omitted = [], []
    for q, name, v in d["cards"] + d.get("shields", []):
        title = f"{name} (V)" if v and not name.endswith("(V)") else name
        hint = None
        if title.endswith(" (Dark)") or " (Dark) (" in title:
            hint = "DARK"
        found = None
        base = re.sub(r"\s*\((?:Coruscant|Premiere|Dark|Special Edition)\)", "", name).replace("*", "").strip()
        if "(Dark)" in name:
            hint = "DARK"
        for t in dict.fromkeys((title, name, base, f"{base} (V)" if v else base)):
            try:
                gi.lookup(t, hint or side, allowed); found = t; break
            except KeyError:
                continue
        if not found:
            for t in (title, base, name, name.split(" / ")[0]):
                hit = _NK.get((hint or side, _nk(t)))
                if hit:
                    try:
                        gi.lookup(hit, hint or side, allowed); found = hit; break
                    except KeyError:
                        pass
        if found:
            keep.append((q, found, hint))
        else:
            omitted.append(name)
    shield_names = {n for _q, n, _v in d.get("shields", [])}
    main_missing = [n for n in omitted if n not in shield_names]
    if main_missing:
        report.append(f"SKIP {d['title']}: main-deck cards not in GEMP {main_missing}"); continue
    try:
        xml, notes = gi.xml_for(keep, side, "all")
    except KeyError as e:
        report.append(f"NOGEMP {d['title']}: {e}"); continue
    year = d["event"][:4]
    tok = next((v for k, v in TOKEN.items() if k in d["event"]), "PC")
    arch = d["title"].split(f" {d['side']} ", 1)[-1]
    base = gi.safe_deck_filename(gi.deck_name("Open", arch, d["player"], d["side"], year, tok))
    clean = lambda f: re.sub(r"\s+", " ", f.replace("_", " "))
    fn = clean(base + ".txt")
    i = 2
    while fn.lower() in taken:
        fn = clean(f"{base[:36]} {i}.txt"); i += 1
    taken.add(fn.lower())
    (out / fn).write_text(xml, encoding="utf-8", newline="\n")
    page = final / rows_tsv[d["title"]]
    text = page.read_text(encoding="utf-8")
    line = gi.wiki_download_line(fn)
    if "GEMP Importable deck:" in text:
        text = re.sub(r"\* '''GEMP Importable deck:'''[^\n]+", line, text, count=1)
    else:
        text = re.sub(r"(\* '''Starting Card:'''[^\n]+)", lambda m: m.group(1) + "\n" + line, text, count=1)
    page.write_text(text, encoding="utf-8")
    n_ok += 1
    if omitted:
        report.append(f"OMITTED {d['title']} -> {fn}: {omitted}")
(final / "gemp-report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
print("skipped (main deck not fully in GEMP)", sum(r.startswith("SKIP") for r in report))
print("gemp files", n_ok, "decks with omitted cards", sum(r.startswith("OMITTED") for r in report),
      "no file", sum(r.startswith("NOGEMP") for r in report))
