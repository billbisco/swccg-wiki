#!/usr/bin/env python3
"""Add the DeckTech post (title, author, date, rating, description, strategy, original card list) to the
2001-2006 typed deck pages, as on the 2002 DeckTech pages. Reads the live page text, writes post/pages + post/all.tsv."""
import json, re, html, glob, pathlib, urllib.request, urllib.parse, time
HERE = pathlib.Path(__file__).parent
S = HERE.parent
OUT = HERE / "post"; (OUT / "pages").mkdir(parents=True, exist_ok=True)
API = "https://wiki.swccg.com/api.php"

loc = {}
for g in ("gap/G1/found.json", "gap/G2/found.json", "gap/G1/extras_out_of_scope.json"):
    p = S / g
    if p.exists():
        for e in json.load(open(p)):
            if e.get("local_file"): loc.setdefault(e["source_url"], e["local_file"])

def text_of(f):
    raw = open(f, "rb").read().decode("utf-8", "replace")
    if raw.count("�") > 20: raw = open(f, "rb").read().decode("latin-1")
    t = re.sub(r"(?is)<script.*?</script>|<style.*?</style>|<!--.*?-->", "", raw)
    t = re.sub(r"(?i)<br\s*/?>|</p>|</tr>|</div>|</h\d>|</li>", "\n", t)
    t = html.unescape(re.sub(r"<[^>]+>", "", t)).replace("\r", "").replace("\xa0", " ")
    return re.sub(r"\n[ \t]*\n+", "\n", t)

def parse_decktech(t):
    m = re.search(r"\n([^\n]+)\n\s*Rating\s*\n?\s*\(([\d.]+)\)", t)
    if not m: return None
    d = {"title": m.group(1).strip(), "rating": m.group(2)}
    rest = t[m.end():]
    a = re.search(r"Author\s+(.+?)\s*(?:\(Subscribe|\n)", rest); d["author"] = a.group(1).strip() if a else ""
    de = re.search(r"\n\s*Description\s*\n(.*?)\n\s*Submitted\s+([^\n]+)", rest, re.S)
    d["description"] = de.group(1).strip() if de else ""
    d["submitted"] = de.group(2).strip() if de else ""
    c = re.search(r"\n\s*Cards\s*\n(.*?)\n\s*Strategy\s*\n", rest, re.S)
    d["cards"] = c.group(1).strip() if c else ""
    s = re.search(r"\n\s*Strategy\s*\n(.*?)(?:\n\s*Back to Decks Directory|\n\s*In order to review|\Z)", rest, re.S)
    d["strategy"] = s.group(1).strip() if s else ""
    return d

def parse_ess(t):
    m = re.search(r"Deck:\s*(.+?)\s*\((\d+) cards\)\s*\n\s*Description:\s*\n(.*?)\n\s*Quantity:", t, re.S)
    if not m: return None
    return {"title": m.group(1).strip(), "rating": "", "author": "mserisman (essentialswccg.com)", "submitted": "",
            "description": "", "strategy": m.group(3).strip(), "cards": ""}

def safe(line):
    line = line.replace("<", "&lt;").replace("[", "&#91;").replace("]", "&#93;").replace("{", "&#123;").replace("}", "&#125;").replace("|", "&#124;").replace("~~~", "&#126;~~")
    line = line.strip()
    if line[:1] in "*#:;=-" or line.startswith("----"): line = "<nowiki/>" + line
    if re.match(r"^https?://\S+$", line): pass
    return line

def para(text):
    return "\n\n".join(safe(l) for l in text.split("\n") if l.strip())

def q(**k):
    k.update(format="json", formatversion=2)
    for a in range(6):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(API, data=urllib.parse.urlencode(k).encode(), headers={"User-Agent": "HolocronClaude-post"}), timeout=90))
        except Exception:
            time.sleep(4)

built = json.load(open(HERE / "final" / "built.json"))
rows, rep = [], []
for b in built:
    src = b["source_url"]
    f = loc.get(src)
    if not f:
        rep.append(f"NOFILE {b['title']} ({src})"); continue
    if f.lower().endswith(".pdf"):
        rep.append(f"PDF-FORM {b['title']}"); continue
    t = text_of(f)
    d = parse_decktech(t) if "decktech" in src else parse_ess(t)
    if not d:
        rep.append(f"NOPARSE {b['title']} ({f})"); continue
    p = q(action="query", titles=b["title"], prop="revisions", rvprop="content", rvslots="main")["query"]["pages"][0]
    txt = p["revisions"][0]["slots"]["main"]["content"]
    if "== Original post ==" in txt:
        rep.append(f"HAS {b['title']}"); continue
    sec = [f"== Original post ==", "", f"'''{safe(d['title'])}'''"]
    if d["author"]: sec.append(f"* '''Author:''' {safe(d['author'])}")
    if d["submitted"]: sec.append(f"* '''Published:''' {safe(d['submitted'])}")
    if d["rating"]: sec.append(f"* '''Rating:''' {d['rating']}")
    if d["description"]: sec.append(f"* '''Description:''' {safe(' '.join(d['description'].split()))}")
    if d["strategy"]:
        sec += ["", "=== Strategy ===", "", para(d["strategy"])]
    if d["cards"]:
        cards = d["cards"].replace("</nowiki>", "").strip()
        sec += ["", "=== Original card list ===", "",
                '{| class="wikitable mw-collapsible mw-collapsed" style="width:100%" data-expandtext="Show" data-collapsetext="Hide"',
                "|+ As posted on DeckTech", "|-", '| <div style="white-space:pre-wrap"><nowiki>', cards, "</nowiki></div>", "|}"]
    block = "\n".join(sec) + "\n\n"
    k = txt.find("== See also ==")
    txt = txt[:k] + block + txt[k:]
    if d["description"] and "'''Description:'''" not in txt.split("== Decklist ==")[0]:
        txt = txt.replace("== Decklist ==", "", 0)
    fn = re.sub(r"[^\w.-]+", "_", b["title"]) + ".wiki"
    (OUT / "pages" / fn).write_text(txt, encoding="utf-8")
    rows.append(f"{b['title']}\tpages/{fn}")
    if not d["strategy"]: rep.append(f"NO-STRATEGY {b['title']}")
    if not d["description"]: rep.append(f"NO-DESCRIPTION {b['title']}")
(OUT / "all.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
(OUT / "report.txt").write_text("\n".join(rep) + "\n", encoding="utf-8")
print(len(rows), "pages"); print("\n".join(rep))
