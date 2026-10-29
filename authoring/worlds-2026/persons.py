#!/usr/bin/env python3
"""Add 2026 World Championship rows to player pages (newest first); create pages for new players."""
import json, re, pathlib, urllib.request, urllib.parse, time, html
HERE = pathlib.Path(__file__).parent
OUT = HERE / "out"
built = json.load(open(OUT / "built.json"))
D1 = []
hub = open(HERE / "raw" / "w26" / "_hub.html", encoding="utf-8").read()
txt = html.unescape(re.sub(r"<[^>]+>", "\n", hub))
for m in re.finditer(r"^\s*(\d+)\.\s+([^\n–]+?)\s+–", txt, re.M):
    D1.append((int(m.group(1)), m.group(2).strip()))
D1 = [p for n, p in sorted({n: p for n, p in D1}.items())]
T8 = ["Brian Fred", "Justin Desai", "Greg Shaw", "Drew Lichtenstein", "Joe Horbey", "Joe Olson", "Dennis Reinhardt", "Bryan Mischke"]
PC_HUB = "https://www.starwarsccg.org/2026-11-swccg-world-championship-bloomington-minnesota-oct-23-25-2026/"
EV = "2026 World Championship"
REF = f'<ref name="pc-w26">[{PC_HUB} 2026-11 SWCCG World Championship – Bloomington, Minnesota (Oct. 23-25, 2026)], starwarsccg.org</ref>'
API = "https://wiki.swccg.com/api.php"

def get(titles):
    r = json.load(urllib.request.urlopen(API + "?" + urllib.parse.urlencode(dict(action="query", prop="revisions",
        rvprop="content|timestamp", rvslots="main", titles="|".join(titles), redirects=1, format="json", formatversion=2)), timeout=90))
    red = {x["from"]: x["to"] for x in r["query"].get("redirects", [])}
    pg = {p["title"]: p for p in r["query"]["pages"]}
    out = {}
    for t in titles:
        p = pg.get(red.get(t, t))
        out[t] = (p["title"], p["revisions"][0]["slots"]["main"]["content"]) if p and p.get("revisions") else None
    return out

def cell(p, t8, s):
    b = built.get(f"{p}|{t8}|{s}")
    return f"[[{b['title']}|{b['hub_label']}]]" if b else "—"

pages = {}
for i in range(0, len(D1), 40):
    pages.update(get(D1[i:i + 40]))
rows_out, rep = [], []
(OUT / "persons").mkdir(exist_ok=True)
for p in D1:
    rows = []
    first = True
    def ev_cell(stage):
        global first
        r = f"[[{EV}]] ({stage})" + (REF if first else '<ref name="pc-w26" />')
        first = False
        return r
    if p in T8:
        rows.append(f"|-\n| 25 October 2026 || {ev_cell('Top 8')} || [[Open]] || #{T8.index(p) + 1} || {cell(p, True, 'DS')} || {cell(p, True, 'LS')}")
    rows.append(f"|-\n| 24 October 2026 || {ev_cell('Day 1')} || [[Open]] || #{D1.index(p) + 1} || {cell(p, False, 'DS')} || {cell(p, False, 'LS')}")
    got = pages.get(p)
    if got is None:
        body = f"""'''{p}''' is a Star Wars CCG player who played the [[{EV}]].<ref name="pc-w26">[{PC_HUB} 2026-11 SWCCG World Championship – Bloomington, Minnesota (Oct. 23-25, 2026)], starwarsccg.org</ref>

== Tournament Results ==

{{| class="wikitable"
! Date !! Event !! Format !! Finish !! Dark !! Light
{chr(10).join(r.replace(REF, '<ref name="pc-w26" />') for r in rows)}
|}}

== See also ==

* [[{EV}]]
* [[List of SWCCG tournaments]]

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
"""
        title = p
        rep.append(f"NEW {p}")
    else:
        title, body = got
        if EV in body:
            rep.append(f"ALREADY {title}"); continue
        m = re.search(r"== ?Tournament Results ?==\s*\n\s*\{\|[^\n]*\n(?:\|-\s*\n)?(!.*?\n)", body)
        if m:
            body = body[:m.end()] + "\n".join(rows) + "\n" + body[m.end():]
        else:
            sec = "== Tournament Results ==\n\n{| class=\"wikitable\"\n! Date !! Event !! Format !! Finish !! Dark !! Light\n" + "\n".join(rows) + "\n|}\n\n"
            k = body.find("== See also ==")
            if k < 0: k = body.find("{{#if:1")
            if k < 0: k = body.find("[[Category:")
            body = body[:k] + sec + body[k:] if k >= 0 else body + "\n\n" + sec
            rep.append(f"NEWTABLE {title}")
        if "<references" not in body and "{{Reflist" not in body.lower():
            body = body.replace("[[Category:", "{{#if:1|<nowiki />\n<h2>References</h2>\n<references />}}\n\n[[Category:", 1)
    fn = re.sub(r"[^A-Za-z0-9._()-]", "_", title) + ".wiki"
    (OUT / "persons" / fn).write_text(body, encoding="utf-8")
    rows_out.append(f"{title}\tpersons/{fn}")
(OUT / "persons.tsv").write_text("\n".join(rows_out) + "\n", encoding="utf-8")
print(len(rows_out)); print("\n".join(rep))
