"""pkg.py : final-all -> pkg/ (pages, file description pages, media, pdf, all.tsv) for the PC apply."""
import json, pathlib, shutil, re
H = pathlib.Path(__file__).parent
F = H / "final-all"; P = H / "pkg"
if P.exists(): shutil.rmtree(P)
(P / "pages").mkdir(parents=True); (P / "media").mkdir(); (P / "pdf").mkdir()
events = json.load(open(H / "events-all.json"))
canon = json.load(open(F / "decks-canon.json"))
built = {d["title"]: d for d in json.load(open(F / "decks-built.json"))}
rows = [l for l in (F / "all.tsv").read_text(encoding="utf-8").splitlines() if "\t" in l]
for l in rows:
    t, rel = l.split("\t"); shutil.copy(F / rel, P / rel)
def fn(t): return re.sub(r"[^\w.-]+", "_", t) + ".wiki"
extra = []
# format page
shutil.copy(H / "extra" / "Premiere_-_Original_VS12.wiki", P / "pages" / "Premiere_-_Original_VS12.wiki")
extra.append("Premiere - Original VS12\tpages/Premiere_-_Original_VS12.wiki")
# PDFs
done_pdf = set()
for stem, ev in events.items():
    name = ev["pdf_file"]
    if name in done_pdf: continue
    done_pdf.add(name)
    src = H / "pdf" / (stem.split("#")[0] + ".pdf")
    note = ""
    if stem == "2010_Regional_Dagobah":
        src = H / "pdf" / "2010_Regional_Dagobah_recovered.pdf"
        note = (" The copy on res.starwarsccg.org (and its Internet Archive copy) is cut off after page 13 of 22; this file holds"
                " the 13 page scans recovered from it.")
    shutil.copy(src, P / "pdf" / name)
    hubs = sorted({e["hub"] for e in events.values() if e["pdf_file"] == name})
    srcs = "\n".join(f"* [{u} {l}]" for u, l in ev["sources"])
    txt = (f"== Summary ==\nPlayers Committee scanned deck sheets: {', '.join('[[' + h + ']]' for h in hubs)}"
           f"{' ' + ev['stage'] if ev.get('stage') else ''}.{note}\n\n== Source ==\n{srcs}\n")
    t = "File:" + name
    (P / "pages" / fn(t)).write_text(txt, encoding="utf-8"); extra.append(f"{t}\tpages/{fn(t)}")
# scans
for d in canon:
    m = H / "media" / d["scan"]
    if not m.exists(): print("NO SCAN", d["scan"]); continue
    shutil.copy(m, P / "media" / d["scan"])
    b = built[d["title"]]; ev = events[b["evkey"]]
    pg = f"page {d['pages'][0]}" if len(d["pages"]) == 1 else f"pages {d['pages'][0]}–{d['pages'][-1]}"
    txt = (f"== Summary ==\nDeck sheet of [[{d['player']}]] ({'Dark' if d['side'] == 'DS' else 'Light'} Side) at [[{ev['hub']}]]"
           f"{' (' + ev['stage'] + ')' if ev.get('stage') else ''}: {pg} of [[:File:{ev['pdf_file']}]]. Decklist: [[{d['title']}]].\n")
    t = "File:" + d["scan"]
    (P / "pages" / fn(t)).write_text(txt, encoding="utf-8"); extra.append(f"{t}\tpages/{fn(t)}")
# order: format page, file pages first (after upload), then hubs/decks/persons
(P / "all.tsv").write_text("\n".join(extra + rows) + "\n", encoding="utf-8")
shutil.copy(H / "ap.py", P / "ap.py"); shutil.copy(F / "since.txt", P / "since.txt")
print(len(extra + rows), "pages;", len(list((P / "media").iterdir())), "scans;", len(done_pdf), "pdfs")
