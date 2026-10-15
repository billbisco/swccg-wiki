#!/usr/bin/env python3
"""Finalize generated pages for PC-post-sourced decks.

python3 finalize_pc.py <gen_dir> <decks.json> <out_dir>
- Adds Player/Event/Side to Deck info; keeps the stub's PC-list Source line (+ Preserved copy).
- Replaces the Scan placeholder with an "Original post" section is NOT done: typed posts have no scan, so the section is dropped.
- Sources: the deck post (live URL) + its Wayback capture, plus the stub's existing source lines.
- Card links whose target page doesn't exist print as plain text (Bill: print as written).
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

API = "https://wiki.swccg.com/api.php"
gen, decks_path, out = Path(sys.argv[1]), Path(sys.argv[2]), Path(sys.argv[3])
(out / "pages").mkdir(parents=True, exist_ok=True)
decks = {d["title"]: d for d in json.loads(decks_path.read_text(encoding="utf-8"))}


def api(**kw):
    kw["format"] = "json"
    for _ in range(5):
        try:
            return json.load(urllib.request.urlopen(API + "?" + urllib.parse.urlencode(kw), timeout=60))
        except Exception:
            time.sleep(3)
    raise SystemExit("api failed")


_ex = {}


def exists_many(ts):
    todo = [t for t in ts if t not in _ex]
    for i in range(0, len(todo), 45):
        ch = todo[i:i + 45]
        r = api(action="query", titles="|".join(ch), redirects=1)
        q = r["query"]
        norm = {n["from"]: n["to"] for n in q.get("normalized", [])}
        red = {n["from"]: n["to"] for n in q.get("redirects", [])}
        ok = {p["title"] for p in q["pages"].values() if "missing" not in p and "invalid" not in p}
        for t in ch:
            t2 = norm.get(t, t)
            _ex[t] = red.get(t2, t2) in ok
        time.sleep(0.25)


def stub_texts(titles):
    res = {}
    for i in range(0, len(titles), 40):
        r = api(action="query", titles="|".join(titles[i:i + 40]), prop="revisions", rvprop="content", rvslots="main")
        for p in r["query"]["pages"].values():
            if "revisions" in p:
                res[p["title"]] = p["revisions"][0]["slots"]["main"]["*"]
        time.sleep(0.25)
    return res


rows = [l.split("\t") for l in (gen / "titles.tsv").read_text(encoding="utf-8").splitlines() if l]
stubs = stub_texts([t for t, _ in rows])
link_re = re.compile(r"\[\[([^\]|#]+)(?:\|([^\]]*))?\]\]")
report, outrows = [], []
for title, fn in rows:
    d = decks[title]
    text = (gen / fn).read_text(encoding="utf-8")
    side_word = "Dark" if d["side"] == "DS" else "Light"
    info = (f"* '''Player:''' [[{d['player']}]]\n* '''Event:''' [[{d['event']}]]\n* '''Side:''' [[{side_word}]]\n")
    text = text.replace("== Deck info ==\n\n", "== Deck info ==\n\n" + info, 1)
    stub = stubs.get(title, "")
    src = re.search(r"^\* '''Source:''' .*$", stub, re.M)
    if src:
        text = re.sub(r"(^\* '''Stage:''' .*$)", lambda m: m.group(1) + "\n" + src.group(0), text, count=1, flags=re.M)
    # drop the Scan placeholder section (typed post: no sheet)
    text = re.sub(r"\n== Scan ==\n\n[^\n]*\n", "\n", text)
    # Sources
    post = d.get("url", "")
    wb = d.get("wayback", "")
    lines = []
    if post:
        lines.append(f"* [{post} {d.get('post_title') or 'Deck post'}], starwarsccg.org"
                     + (f". Preserved copy: [{wb} Internet Archive]" if wb else ""))
    for l in re.findall(r"^\* \[https?://[^\n]*$", stub.split("== Sources ==")[-1] if "== Sources ==" in stub else "", re.M):
        if l not in lines:
            lines.append(l)
    text = re.sub(r"== Sources ==\n\n", "== Sources ==\n\n" + "\n".join(lines) + "\n", text, count=1)
    # plain text for missing card pages
    head, sep, rest = text.partition("== Decklist ==")
    body, sep2, tail = rest.partition("== See also ==")
    tg = {m.group(1).strip() for m in link_re.finditer(body) if not m.group(1).startswith(("File:", "Category:", ":"))}
    exists_many(sorted(tg))
    printed = []

    def fix(m):
        t = m.group(1).strip()
        if t.startswith(("File:", "Category:", ":")) or _ex.get(t, True):
            return m.group(0)
        printed.append(t)
        return m.group(2) or t

    body = link_re.sub(fix, body)
    # {{CardLink|Target|img...}}: front-only objective names -> full "Front / Back" title; else plain text
    cl_re = re.compile(r"\{\{CardLink\|([^|}]+)\|[^}]*\}\}")
    exists_many(sorted({m.group(1).strip() for m in cl_re.finditer(body)}))

    def fix_cl(m):
        t = m.group(1).strip()
        if _ex.get(t, True):
            return m.group(0)
        if " / " not in t:
            r = api(action="query", list="allpages", apprefix=t + " / ", aplimit=10)["query"]["allpages"]
            full = [p["title"] for p in r if not re.search(r"\((?:Virtual|AI|Errata|Original|PC Errata|Dark)", p["title"])]
            if full:
                return m.group(0).replace("CardLink|" + m.group(1) + "|", "CardLink|" + full[0] + "|", 1)
        printed.append(t)
        return t
    body = cl_re.sub(fix_cl, body)
    text = head + sep + body + sep2 + tail
    if printed:
        report.append(f"PLAIN {title}: {sorted(set(printed))}")
    n = sum(q for q, *_ in d["cards"])
    if n != 60:
        report.append(f"COUNT {title}: {n} cards as posted")
    (out / "pages" / fn).write_text(text, encoding="utf-8")
    outrows.append(f"{title}\tpages/{fn}")
(out / "titles.tsv").write_text("\n".join(outrows) + "\n", encoding="utf-8")
(out / "report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
print(len(outrows), "pages;", sum(r.startswith("PLAIN") for r in report), "with plain text;",
      sum(r.startswith("COUNT") for r in report), "not 60")
