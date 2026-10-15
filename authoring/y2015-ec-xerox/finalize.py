#!/usr/bin/env python3
"""Finalize generated 2015 EC Xerox pages for apply.

- Keep the existing stub title (hub/player pages link it); log sheet-vs-title mismatches.
- Keep the stub's sourced lines (PC list + Preserved copy) and add PDF citations with Wayback copies.
- Card links whose target page does not exist on the wiki print as plain text (Bill: print as written).

Writes final/<safe>.wiki, final/titles.tsv (title<TAB>file), final/report.txt
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

E = Path(__file__).resolve().parent
GEN = E / "final" / "gen"
OUT = E / "final" / "pages"
API = "https://wiki.swccg.com/api.php"
OUT.mkdir(parents=True, exist_ok=True)

PDF = {
    "01-17": ("https://res.starwarsccg.org/wp/wp-content/uploads/SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf",
              "https://web.archive.org/web/20170705061358/http://www.starwarsccg.org/wp/wp-content/uploads/SW-EC-2015-Day-2-Deck-Lists-Place-01-17.pdf"),
    "18-35": ("https://res.starwarsccg.org/wp/wp-content/uploads/SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf",
              "https://web.archive.org/web/20170710081541/http://www.starwarsccg.org/wp/wp-content/uploads/SW-EC-2015-Day-2-Deck-Lists-Place-18-35.pdf"),
}


def api(**kw):
    kw["format"] = "json"
    for _ in range(4):
        try:
            return json.load(urllib.request.urlopen(API + "?" + urllib.parse.urlencode(kw), timeout=60))
        except Exception:
            time.sleep(3)
    raise SystemExit("api failed")


def stub_text(title):
    r = api(action="query", titles=title, prop="revisions", rvprop="content", rvslots="main")
    p = list(r["query"]["pages"].values())[0]
    return None if "missing" in p else p["revisions"][0]["slots"]["main"]["*"]


_exists = {}


def exists_many(titles):
    todo = [t for t in titles if t not in _exists]
    for i in range(0, len(todo), 40):
        chunk = todo[i:i + 40]
        r = api(action="query", titles="|".join(chunk), redirects=1)
        norm = {n["from"]: n["to"] for n in r["query"].get("normalized", [])}
        red = {n["from"]: n["to"] for n in r["query"].get("redirects", [])}
        ok = {p["title"] for p in r["query"]["pages"].values() if "missing" not in p and "invalid" not in p}
        for t in chunk:
            t2 = norm.get(t, t)
            t3 = red.get(t2, t2)
            _exists[t] = t3 in ok
        time.sleep(0.3)


pagemap = [l.split("\t") for l in (E / "pagemap.tsv").read_text().splitlines()[1:] if l.strip()]
pagemap.append(["1", "Joe Olson", "a", "2", "4",
                "2015 European Championship Day 2 Joe Olson DS Endor Operations",
                "2015 European Championship Day 2 Joe Olson LS Watch Your Step"])
by_ps = {}
for pl, player, pdf, dsp, lsp, dst, lst in pagemap:
    by_ps[(player, "DS")] = (dst, pdf)
    by_ps[(player, "LS")] = (lst, pdf)

rows = [l.split("\t") for l in (GEN / "y2015-ec-xerox-titles.tsv").read_text(encoding="utf-8").splitlines() if l]
report, titles_out = [], []
link_re = re.compile(r"\[\[([^\]|#]+)(?:\|([^\]]*))?\]\]")
for gen_title, rel in rows:
    m = re.match(r"2015 European Championship Day 2 (.+?) (DS|LS) (.+)$", gen_title)
    player, side, label = m.groups()
    want, pdf = by_ps[(player, side)]
    text = (GEN / rel).read_text(encoding="utf-8")
    if want != gen_title:
        report.append(f"TITLE kept existing: {want!r}  (sheet starts {label!r})")
    text = text.replace(f"'''{gen_title}'''", f"'''{want}'''", 1)

    if "'''Side:'''" not in text:
        side_word = "Dark" if side == "DS" else "Light"
        info = (f"* '''Player:''' [[{player}]]\n* '''Event:''' [[2015 European Championship]]\n"
                f"* '''Side:''' [[{side_word}]]\n")
        text = text.replace("== Deck info ==\n\n", "== Deck info ==\n\n" + info, 1)
    stub = stub_text(want) or ""
    src = re.search(r"^\* '''Source:''' .*$", stub, re.M)
    if src and "'''Source:'''" not in text:
        text = re.sub(r"(^\* '''Stage:''' .*$)", lambda mm: mm.group(1) + "\n" + src.group(0), text, count=1, flags=re.M)

    key = "01-17" if pdf == "a" else "18-35"
    url, wb = PDF[key]
    other = PDF["18-35" if key == "01-17" else "01-17"][0]
    place_lbl = "Place 1-17" if key == "01-17" else "Place 18-35"
    text = re.sub(r"^\* \[" + re.escape(url) + r" [^\]]*\], res\.starwarsccg\.org$",
                  f"* [{url} {place_lbl} PDF], res.starwarsccg.org. Preserved copy: [{wb} Internet Archive]", text, flags=re.M)
    text = re.sub(r"^\* \[" + re.escape(other) + r" [^\]]*\], res\.starwarsccg\.org\n", "", text, flags=re.M)
    wrap = re.search(r"^\* \[https://www\.starwarsccg\.org/2015-european-championships/ [^\n]*Preserved copy:[^\n]*$", stub, re.M)
    if wrap:
        text = re.sub(r"^\* \[https://www\.starwarsccg\.org/2015-european-championships/ [^\]]*\], starwarsccg\.org$",
                      lambda mm: wrap.group(0), text, flags=re.M)

    # plain links in the decklist body -> plain text when the page doesn't exist
    head, sep, rest = text.partition("== Decklist ==")
    body, sep2, tail = rest.partition("== See also ==")
    targets = {mm.group(1).strip() for mm in link_re.finditer(body) if not mm.group(1).startswith(("File:", "Category:", ":"))}
    exists_many(sorted(targets))
    printed = []

    def fix(mm):
        t = mm.group(1).strip()
        if t.startswith(("File:", "Category:", ":")) or _exists.get(t, True):
            return mm.group(0)
        printed.append(t)
        return mm.group(2) or t

    body = link_re.sub(fix, body)
    text = head + sep + body + sep2 + tail
    if printed:
        report.append(f"PLAIN TEXT on {want}: {sorted(set(printed))}")
    fn = re.sub(r"[^\w.-]+", "_", want) + ".wiki"
    (OUT / fn).write_text(text, encoding="utf-8")
    titles_out.append(f"{want}\tpages/{fn}")

(E / "final" / "titles.tsv").write_text("\n".join(titles_out) + "\n", encoding="utf-8")
(E / "final" / "report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
print(len(titles_out), "pages;", sum(r.startswith("TITLE") for r in report), "title notes;",
      sum(r.startswith("PLAIN") for r in report), "pages with plain-text cards")
