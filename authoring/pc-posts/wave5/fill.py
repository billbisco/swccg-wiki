#!/usr/bin/env python3
"""Fill empty 2015-2018 decklist stubs from the PC per-deck posts fetched via FlareSolverr.

python3 fill.py  -> out/pages/<title>.wiki, out/all.tsv, out/report.txt
"""
import json, re, sys, pathlib, collections, urllib.request, urllib.parse
HERE = pathlib.Path(__file__).parent
OLD = HERE.parent / "old"
sys.path.insert(0, "/home/claude/sw2/authoring/pc-posts")
sys.path.insert(0, "/home/claude/sw2/authoring/pc-pdf-scans")
import parse_posts as P
import resolve_wiki as R

# canon.py helpers (module body without its __main__-style tail)
src = open("/home/claude/sw2/authoring/pc-posts/canon.py").read().split("decks = json.load(open(sys.argv[1]))")[0]
src = src.replace("/home/claude/swccg-gemp/", "/home/claude/playerscommittee/gemp-swccg-public/")
C = {"__file__": "/home/claude/sw2/authoring/pc-posts/canon.py"}
exec(compile(src, "canon", "exec"), C)

# build.py resolution/render helpers (defs only)
b = open(OLD / "build.py").read()
defs = b[b.index("LEFT = ["):b.index("# ---- load decks")]
B = {"R": R, "re": re, "json": json}
exec(compile(defs + "\n" + re.search(r"^def esc.*$", b, re.M).group(0), "build", "exec"), B)
LEFT, RIGHT, cardlink, esc, norm_type = B["LEFT"], B["RIGHT"], B["cardlink"], B["esc"], B["norm_type"]

API = "https://wiki.swccg.com/api.php"
def live(title):
    import time
    for a in range(6):
        try: return _live(title)
        except Exception: time.sleep(5)
    return _live(title)
def _live(title):
    r = json.load(urllib.request.urlopen(API + "?" + urllib.parse.urlencode(dict(action="query", prop="revisions",
        rvprop="content|timestamp", rvslots="main", titles=title, format="json", formatversion=2)), timeout=60))
    p = r["query"]["pages"][0]
    return p["revisions"][0]["slots"]["main"]["content"], p["revisions"][0]["timestamp"]

def modern_fix(i, side, shield):
    """Post-2014 deck: an unmarked line must not land on a Legacy (VB/VSh/OVS) printing when an original page exists."""
    if not i or not re.match(r"(VB|VSh|OVS)", i["image"]) or "(V)" in i["title"]:
        return i
    return i

EXTRA = {("DS", "endor landining platform"): "Endor: Landing Platform (Docking Bay)", ("DS", "endor bunker"): "Endor: Bunker",
         ("DS", "opressive"): "Oppressive Enforcement", ("DS", "ychf"): "You Cannot Hide Forever",
         ("DS", "ychf (v)"): "You Cannot Hide Forever (V)", ("DS", "dr evazan & ponda baba"): "Dr. Evazan & Ponda Baba",
         ("DS", "short-range fighters & watch your back!"): "Short Range Fighters & Watch Your Back!",
         ("LS", "boussh"): "Boushh", ("DS", "imbalance and kintan strider"): "Imbalance & Kintan Strider", ("LS", "obi-wan kenobi with lightsaber"): "Obi-Wan With Lightsaber", ("LS", "artoo detoo in red 5"): "Artoo-Detoo In Red 5",
         ("LS", "spaceport: docking bay"): "Spaceport Docking Bay", ("LS", "sense (premiere)"): "Sense (Light) (Premiere)"}
mp = json.load(open(HERE / "map.json"))
out = HERE / "out"; (out / "pages").mkdir(parents=True, exist_ok=True)
rep, rows = [], []
for title, url in mp.items():
    slug = url.rstrip("/").split("/")[-1]
    f = HERE / "raw" / "posts" / f"{slug}.html"
    d = P.parse(f)
    _t, lines = P.post_body(f.read_text(encoding="utf-8", errors="replace"))
    pre = []
    for l in lines:
        if P.HEAD.match(l) or re.match(r"^[\[{]\s*([A-Za-z' &/-]+?)\s*[\]}]\s*$", l) or re.sub(r"\s*\([^)]*\)\s*$", "", l).strip().lower() in P.BARE_HEADS:
            break
        pre.append(l)
    tot0 = sum(c[0] for c in d["cards"])
    if pre and tot0 < 60 and len(pre) <= 12 and not any(re.search(r"\b20\d\d\b|\d(?:st|nd|rd|th) place|day \d|record", l, re.I) for l in pre):
        add_pre = [list(P.split_item(l)) for l in pre]
        d["cards"] = add_pre + d["cards"]
        rep.append(f"PRE-HEAD {title}: {len(pre)} unheaded opening lines taken as starting cards ({tot0} -> {sum(c[0] for c in d['cards'])})")
    sd = "DS" if " DS " in f" {title} " else "LS"
    side = "Dark" if sd == "DS" else "Light"
    if d["side"] and d["side"] != sd:
        rep.append(f"SIDE-WORD {title}: post title says {d['side']} ({d['post_title']})")
    groups = collections.OrderedDict(); unres = []; unres_cards = []
    def add(q, name, v, shield):
        name0 = name
        m = re.search(r"\s+V$", name)
        if m: name, v = name[:m.start()], True
        name = EXTRA.get((sd, name.lower()), name)
        tc = " ".join(w[:1].upper() + w[1:] for w in name.split(" "))
        C["wiki_has"]([name, tc, tc + " (V)", name + " (V)"])
        n2, v2, _fx = C["fix"](name, v, sd)
        if n2 == name and tc != name: n2, v2, _fx = C["fix"](tc, v, sd)
        n2 = C["objective_fix"](n2, v2) if " / " in n2 else n2
        ep1 = bool(re.search(r"\(Coruscant\)", n2))
        info = B["_resolve_line"](n2, v2, side, ep1, shield) or B["norm_resolve"](n2, v2, side, ep1, shield)
        if info is None and n2 != name:
            info = B["_resolve_line"](name, v, side, False, shield)
        if info is None and tc != name:
            info = B["_resolve_line"](tc, v, side, False, shield) or B["norm_resolve"](tc, v, side, False, shield)
        if info and re.search(r" \((Virtual Block|Dark|Light)[^()]*\)$", info["title"]) and not shield:
            j = R.resolve(re.sub(r"^(.*?)(?: / .*)? \((Virtual Block|Dark|Light)[^()]*\)$", r"\1", info["title"]), "(V)" in info["title"], side)
            if j and not re.match(r"(VB|VSh|OVS)", j["image"]): info = j
        name = name0
        if info is None:
            key = ("Defensive Shield" if shield else "Not identified", "TEXT:" + name + (" (V)" if v else ""))
            unres.append(name + (" (V)" if v else "")); 
            if not shield: unres_cards.append(name)
        else:
            typ = "Defensive Shield" if shield and info["type"] == "Defensive Shield" else norm_type(info["type"])
            if v and "(V)" not in info["title"]:
                rep.append(f"V-LOST {title}: {name} (V) -> {info['title']}")
            key = (typ, info["title"])
        g = groups.setdefault(key[0], collections.OrderedDict())
        g[key[1]] = (g.get(key[1], (0, info))[0] + q, info)
    for q, n, v in d["cards"]: add(q, n, v, False)
    for q, n, v in d["shields"]: add(q, n, v, True)
    total = sum(q for q, _n, _v in d["cards"])
    if total != 60:
        rep.append(f"COUNT {title}: {total} cards + {sum(q for q,_n,_v in d['shields'])} shields")
    if unres:
        rep.append(f"UNRESOLVED {title}: " + "; ".join(unres))
    def col(hs):
        o = []
        for h in hs:
            if h not in groups: continue
            o.append(f"'''{h}'''")
            for k, (q, info) in groups[h].items():
                o.append("* " + (f"{q}x " if q > 1 else "") + (cardlink(info) if info else esc(k[5:])))
            o.append("")
        return "\n".join(o).rstrip("\n")
    intro = "Cards the post names that could not be matched to a card page are printed as written under '''Not identified'''.\n\n" if unres_cards else ""
    body = (intro + '{| class="wikitable" style="width:100%;"\n|-\n| style="width:50%; vertical-align:top;" |\n'
            + col(LEFT) + '\n| style="width:50%; vertical-align:top;" |\n' + col(RIGHT) + "\n|}\n")
    txt, ts = live(title)
    if "== Decklist ==" in txt:
        rep.append(f"SKIP-HAS-LIST {title}"); continue
    if "== See also ==" not in txt:
        rep.append(f"NO-SEEALSO {title}"); continue
    txt = txt.replace("== See also ==", "== Decklist ==\n\n" + body + "\n== See also ==", 1)
    clean_url = url.replace("starwarsccg.org/wp/", "starwarsccg.org/")
    srcline = f"* [{clean_url} {esc(d['post_title'])}], starwarsccg.org (deck post)."
    txt = re.sub(r"(== Sources ==\n\n)", r"\1" + srcline.replace("\\", "\\\\") + "\n", txt, count=1)
    fn = re.sub(r"[^A-Za-z0-9 ._()-]", "_", title) + ".wiki"
    (out / "pages" / fn).write_text(txt, encoding="utf-8")
    rows.append(f"{title}\tpages/{fn}\t{ts}")
    rep.append(f"OK {title} <- {d['post_title']} ({total}+{sum(q for q,_n,_v in d['shields'])})")
(out / "all.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
(out / "report.txt").write_text("\n".join(rep) + "\n", encoding="utf-8")
print(len(rows), "pages"); print("\n".join(r for r in rep if not r.startswith("OK")))
