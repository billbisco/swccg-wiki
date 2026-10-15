#!/usr/bin/env python3
"""Finalize generated pages for decks transcribed from PC decklist PDF scans.

python3 finalize_pdf.py <gen_dir> <decks-canon.json> <out_dir>
- Player/Event/Side (+ Username) in Deck info; keeps the stub's PC-list Source line.
- Scan section: the sheet image(s) File:<Event> <Player> <DS|LS>.png with a page ref to the PDF on the wiki.
- Sources: the PDF (original URL + Wayback copy) + the stub's own source lines.
- Decks not fully identified (blank or UNSURE lines) get the sheet's numbered list instead of the grouped list
  (Bill's phases 1-3); unidentified lines print as written. Missing card pages print as plain text.
Writes out/pages/*.wiki, out/titles.tsv, out/scans.tsv (file name<TAB>pdf<TAB>pages), out/report.txt
"""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path

API = "https://wiki.swccg.com/api.php"
PDFS = {  # local name -> (wiki file name, original url, wayback copy)
    "2016-worlds-day2.pdf": ("2016 World Championship Day 2 Decklists.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=4896",
                             "https://web.archive.org/web/20170717182557/http://www.starwarsccg.org/forums/download/file.php?id=4896"),
    "2016-worlds-day3.pdf": ("2016 World Championship Day 3 Decklists.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=4891",
                             "https://web.archive.org/web/20170717230049/http://www.starwarsccg.org/forums/download/file.php?id=4891"),
    "2016-ec-day2-a.pdf": ("2016 European Championship Day 2 Decklists 01-18.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=4974",
                           "https://web.archive.org/web/2017/http://www.starwarsccg.org/forums/download/file.php?id=4974"),
    "2016-ec-day2-b.pdf": ("2016 European Championship Day 2 Decklists 19-37.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=4975",
                           "https://web.archive.org/web/2017/http://www.starwarsccg.org/forums/download/file.php?id=4975"),
    "2016-ec-day3.pdf": ("2016 European Championship Day 3 Decklists.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=4982",
                         "https://web.archive.org/web/2017/http://www.starwarsccg.org/forums/download/file.php?id=4982"),
    "2016-tmw-day1.pdf": ("2016 Texas Mini Worlds Day 1 Decklists.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=5059",
                          "https://web.archive.org/web/2017/http://www.starwarsccg.org/forums/download/file.php?id=5059"),
    "2016-tmw-day2.pdf": ("2016 Texas Mini Worlds Day 2 Decklists.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=5058",
                          "https://web.archive.org/web/2017/http://www.starwarsccg.org/forums/download/file.php?id=5058"),
    "2016-egp-day1.pdf": ("2016 Endor Grand Prix Day 1 Decklists.pdf", "https://res.starwarsccg.org/wp/wp-content/uploads/Endor-Grand-Prix-Saturday-Decklists.pdf",
                          "https://web.archive.org/web/2017/http://www.starwarsccg.org/wp/wp-content/uploads/Endor-Grand-Prix-Saturday-Decklists.pdf"),
    "2017-egp-day1.pdf": ("2017 Endor Grand Prix Day 1 Decklists.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=5796",
                          "https://web.archive.org/web/2017/http://www.starwarsccg.org/forums/download/file.php?id=5796"),
    "2017-egp-day2.pdf": ("2017 Endor Grand Prix Day 2 Decklists.pdf", "http://www.starwarsccg.org/forums/download/file.php?id=5861",
                          "https://web.archive.org/web/2017/http://www.starwarsccg.org/forums/download/file.php?id=5861"),
}

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
        q = api(action="query", titles="|".join(ch), redirects=1)["query"]
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


def full_objective(t):
    if " / " in t:
        return t
    r = api(action="query", list="allpages", apprefix=t + " / ", aplimit=10)["query"]["allpages"]
    full = [p["title"] for p in r if not re.search(r"\((?:Virtual|AI|Errata|Original|PC Errata|Dark)", p["title"])]
    return full[0] if full else None


rows = [l.split("\t") for l in (gen / "titles.tsv").read_text(encoding="utf-8").splitlines() if l]
stubs = stub_texts([t for t, _ in rows])
link_re = re.compile(r"\[\[([^\]|#]+)(?:\|([^\]]*))?\]\]")
cl_re = re.compile(r"\{\{CardLink\|([^|}]+)\|[^}]*\}\}")
report, outrows, scans = [], [], []
for title, fn in rows:
    d = decks[title]
    text = (gen / fn).read_text(encoding="utf-8")
    side_word = "Dark" if d["side"] == "DS" else "Light"
    info = f"* '''Player:''' [[{d['player']}]]\n* '''Event:''' [[{d['event']}]]\n* '''Side:''' [[{side_word}]]\n"
    text = text.replace("== Deck info ==\n\n", "== Deck info ==\n\n" + info, 1)
    if d.get("username"):
        text = re.sub(r"(^\* '''Format:''' )", f"* '''Username:''' {d['username']}\n\\1", text, count=1, flags=re.M)
    stub = stubs.get(title, "")
    src = re.search(r"^\* '''Source:''' .*$", stub, re.M)
    if src:
        text = re.sub(r"(^\* '''Stage:''' .*$)", lambda m: m.group(1) + "\n" + src.group(0), text, count=1, flags=re.M)

    # numbered sheet list for decks not fully identified
    if not d.get("verified"):
        ren = {}
        for f in d.get("fixes", []):
            m = re.match(r"Posted (.+) dested (.+)\.$", f)
            if m:
                ren[m.group(1)] = re.sub(r" \(V\)$", "", m.group(2))

        uns_l, uns_s = set(), set()
        for nt in d.get("notes", []):
            if nt.upper().startswith(("UNSURE", "ILLEGIBLE")):
                for kind, a, b in re.findall(r"\b(line|shield)s? (\d+)(?:\s*[-–]\s*(\d+))?", nt, re.I):
                    rng = range(int(a), int(b or a) + 1)
                    (uns_s if kind.lower() == "shield" else uns_l).update(rng)

        prev = {"out": ""}

        def item(l, sh=False):
            r = _item(l, sh)
            t = (l.get("text") or "").strip()
            if re.fullmatch(r"[\"\u201c\u201d\u3003\u2033'`~-]*|(?i:same|ditto|do\.?)", t) and l.get("n") in (uns_s if sh else uns_l):
                r = prev["out"] or r   # ditto of the line above
            prev["out"] = r
            return r

        def _item(l, sh=False):
            if l.get("n") in (uns_s if sh else uns_l):  # unverified reading: print as written, unlinked
                return ((l.get("text") or "").strip() or "&nbsp;") + (" (V)" if l.get("v") else "")
            c = (l.get("card") or "").strip()
            c = ren.get(c, c)
            if not c:
                return (l.get("text") or "").strip() or "&nbsp;"
            lab = c + (" (V)" if l.get("v") and not c.endswith("(V)") else "")
            return f"[[{lab}]]"

        L = d["lines"]
        prev["out"] = ""
        col1 = "".join(f"<li>{item(l)}</li>\n" for l in L[:30])
        col2 = "".join(f"<li>{item(l)}</li>\n" for l in L[30:])
        prev["out"] = ""
        sh = "".join(f"<li>{item(l, True)}</li>\n" for l in d.get("shield_lines", []))
        body = ("\nAs listed on the deck sheet (numbered lines). Not every card has been verified yet.\n\n"
                "{| class=\"wikitable\" style=\"width:100%;\"\n|-\n| style=\"width:50%; vertical-align:top;\" |\n"
                f"<ol>\n{col1}</ol>\n| style=\"width:50%; vertical-align:top;\" |\n"
                f"<ol start=\"31\">\n{col2}</ol>\n" + (f"'''Defensive Shields'''\n<ol>\n{sh}</ol>\n" if sh else "") + "|}\n\n")
        text = re.sub(r"(== Decklist ==\n)[\s\S]*?(?=\n== Scan ==)", lambda m: m.group(1) + body, text, count=1)
        # starting card: objective / location by name
        st = d.get("start") or ""
        if st:
            full = full_objective(st) if " / " not in st else st
            tgt = full or st
            text = re.sub(r"^\* '''Starting Card:''' .*$", f"* '''Starting Card:''' [[{tgt}|{st.split(' / ')[0]}]]",
                          text, count=1, flags=re.M)
        report.append(f"NUMBERED {title}")

    # scan
    wikipdf, url, wb = PDFS[d["pdf"]]
    scan = f"{d['event']} {d['stage']} {d['player']} {d['side']}.png"
    pages = d.get("pages") or [d["page"]]
    pg = f"Page {pages[0]}" if len(pages) == 1 else f"Pages {pages[0]}–{pages[-1]}"
    scan_sec = ("== Scan ==\n\n{| style=\"margin:0 auto;border:0;border-collapse:collapse;background:transparent\"\n|-\n"
                f"| style=\"vertical-align:top;border:0;padding:0\" | [[File:{scan}|800px]]\n"
                f"| style=\"vertical-align:top;border:0;padding:0 0 0 0.2em;line-height:1\" | <ref>{pg} of [[:File:{wikipdf}]].</ref>\n|}}\n")
    text = re.sub(r"== Scan ==\n\n[^\n]*\n", lambda m: scan_sec, text, count=1)
    scans.append(f"{scan}\t{d['pdf']}\t{','.join(map(str, pages))}")
    # sources
    lines = [f"* [{url} {wikipdf[:-4]}], starwarsccg.org forum. Preserved copy: [{wb} Internet Archive]"]
    for l in re.findall(r"^\* \[https?://[^\n]*$", stub.split("== Sources ==")[-1] if "== Sources ==" in stub else "", re.M):
        if l not in lines:
            lines.append(l)
    text = re.sub(r"== Sources ==\n\n", "== Sources ==\n\n" + "\n".join(lines) + "\n", text, count=1)
    if "<references />" not in text:
        text = text.replace("[[Category:Decklists]]", "{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}\n\n[[Category:Decklists]]", 1)

    # red links -> full objective title or plain text
    head, sep, rest = text.partition("== Decklist ==")
    body, sep2, tail = rest.partition("== See also ==")
    exists_many(sorted({m.group(1).strip() for m in cl_re.finditer(head + body)} |
                       {m.group(1).strip() for m in link_re.finditer(head + body) if not m.group(1).startswith(("File:", "Category:", ":"))}))
    printed = []

    def fix_cl(m):
        t = m.group(1).strip()
        if _ex.get(t, True):
            return m.group(0)
        full = full_objective(t)
        if full:
            return m.group(0).replace("CardLink|" + m.group(1) + "|", "CardLink|" + full + "|", 1)
        printed.append(t)
        return t

    def fix(m):
        t = m.group(1).strip()
        if t.startswith(("File:", "Category:", ":")) or _ex.get(t, True):
            return m.group(0)
        if t.endswith(" (V)"):
            b = t[:-4]
            exists_many([b])
            if _ex.get(b):
                return f"[[{b}|{m.group(2) or t}]]"
        full = full_objective(t)
        if full:
            return f"[[{full}|{m.group(2) or t}]]"
        printed.append(t)
        return m.group(2) or t

    head = link_re.sub(fix, cl_re.sub(fix_cl, head))
    body = link_re.sub(fix, cl_re.sub(fix_cl, body))
    text = head + sep + body + sep2 + tail
    if printed:
        report.append(f"PLAIN {title}: {sorted(set(printed))}")
    n = sum(q for q, *_ in d["cards"])
    if n != 60:
        report.append(f"COUNT {title}: {n} identified cards")
    (out / "pages" / fn).write_text(text, encoding="utf-8")
    outrows.append(f"{title}\tpages/{fn}")
(out / "titles.tsv").write_text("\n".join(outrows) + "\n", encoding="utf-8")
(out / "scans.tsv").write_text("\n".join(scans) + "\n", encoding="utf-8")
(out / "report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
print(len(outrows), "pages;", sum(r.startswith("NUMBERED") for r in report), "numbered;",
      sum(r.startswith("PLAIN") for r in report), "with plain text")
