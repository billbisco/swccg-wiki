#!/usr/bin/env python3
"""2026 World Championship: hub + 132 deck pages from the PC's official GEMP files (forum t=87042),
cross-checked against the PC per-deck posts. Same layout as the 2026 BWC/Nationals pages.

python3 gen_w26.py  -> out/pages/*.wiki, out/gemp/*.txt, out/all.tsv, out/report.txt
"""
import json, re, sys, html, glob, pathlib, collections, urllib.request, urllib.parse, time
HERE = pathlib.Path(__file__).parent
sys.path.insert(0, "/home/claude/sw2/authoring/pc-pdf-scans")
sys.path.insert(0, "/home/claude/sw2/authoring/pc-posts")
import resolve_wiki as R
import parse_posts as P

RAW = HERE / "raw"
OUT = HERE / "out"; (OUT / "pages").mkdir(parents=True, exist_ok=True); (OUT / "gemp").mkdir(exist_ok=True)
DB = {r["cardId"]: r for r in json.load(open("/home/claude/playerscommittee/gemp-swccg-public/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json")) if "cardId" in r}
API = "https://wiki.swccg.com/api.php"
EVENT = "2026 World Championship"
PC_HUB = "https://www.starwarsccg.org/2026-11-swccg-world-championship-bloomington-minnesota-oct-23-25-2026/"
FORUM = "https://forum.starwarsccg.org/viewforum.php?f=1598"
GEMP_TOPIC = "https://forum.starwarsccg.org/viewtopic.php?t=87042"
T8_TOPIC = "https://forum.starwarsccg.org/viewtopic.php?t=87037"
PAIR_TOPIC = "https://forum.starwarsccg.org/viewtopic.php?t=87035"
rep = []

def q(**k):
    k.update(format="json", formatversion=2)
    for a in range(6):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(API, data=urllib.parse.urlencode(k).encode(),
                             headers={"User-Agent": "HolocronClaude-w26"}), timeout=90))
        except Exception:
            time.sleep(4)
    raise RuntimeError("api")

# ---------- players / standings
D1 = []
hub = open(RAW / "w26" / "_hub.html", encoding="utf-8").read()
txt = html.unescape(re.sub(r"<[^>]+>", "\n", hub))
for m in re.finditer(r"^\s*(\d+)\.\s+([^\n–]+?)\s+–", txt, re.M):
    D1.append((int(m.group(1)), m.group(2).strip()))
D1 = [p for _n, p in sorted(dict(D1).items())] if False else [p for n, p in sorted({n: p for n, p in D1}.items())]
assert len(D1) == 58, len(D1)
T8 = ["Brian Fred", "Justin Desai", "Greg Shaw", "Drew Lichtenstein", "Joe Horbey", "Joe Olson", "Dennis Reinhardt", "Bryan Mischke"]
TOK = {"Kelly": "Tom Kelly", "CKelly": "Chris Kelly", "JOlson": "Joe Olson", "SOlson": "Sam Olson", "Johnson": "Patrick Johnson",
       "Russel": "Nathan Russell", "Wishniewski": "Joe Wisniewski", "Nava De Santiago": "Larry Nava De Santiago"}
for p in D1:
    TOK.setdefault(p.split()[-1], p)

# ---------- GEMP files
files = {}
for f in sorted(glob.glob(str(RAW / "gemp" / "**" / "*.txt"), recursive=True)):
    name = pathlib.Path(f).name
    m = re.match(r"26Worlds (T8 )?(.+?) (DS|LS) (.+)\.txt$", name)
    t8, tok, side, arch = bool(m.group(1)), m.group(2), m.group(3), m.group(4)
    player = TOK[tok]
    key = (player, t8, side)
    if key in files and "Worlds Lists" in f:   # the corrected Kramer file at the zip root wins
        continue
    files[key] = (f, name, arch)
assert len(files) == 132, len(files)

def norm_arch(a):
    a = re.sub(r"\s*\((?:v|V)\)$", "v", a)
    a = re.sub(r"(?<=[a-z])V$", "v", a)
    return a

# ---------- PC posts
posts = {}
for f in glob.glob(str(RAW / "w26" / "2026-*.html")):
    raw = open(f, encoding="utf-8", errors="replace").read()
    t = html.unescape(re.search(r"<title>(.*?)</title>", raw, re.S).group(1)).split(" - Star Wars")[0].strip()
    t2 = re.sub(r"(?i)^(2026 World Championship (?:Top 8 )?)(.*)$", lambda mm: mm.group(1) + mm.group(2), t)
    m = re.match(r"2026 World Championship (Top 8 )?(.+?) (DS|LS) ", t2 + " ")
    if not m:
        NS = {"Hayes Hunter Luke Saga": ("Hayes Hunter", "LS"), "Hayes Hunter Hunt Down (V)": ("Hayes Hunter", "DS"),
              "William Ament TDIGWATT (V)": ("William Ament", "DS"), "Tom Kelly Mind What You Have Learned (V)": ("Tom Kelly", "LS")}
        k2 = t2.replace("2026 World Championship ", "")
        if k2 in NS:
            posts[(NS[k2][0], False, NS[k2][1])] = ("https://www.starwarsccg.org/" + pathlib.Path(f).stem + "/", t, pathlib.Path(f)); continue
    if not m:
        rep.append(f"POST-UNPARSED {t}"); continue
    pl = m.group(2).strip(); pl = {"Pat Johnson": "Patrick Johnson", "Joe Wishniewski": "Joe Wisniewski",
        "Matthew Harrison-Trainer": "Matthew Harrison-Trainor"}.get(pl, pl)
    pl = next((x for x in D1 if x.lower() == pl.lower()), pl)
    if pl not in D1:
        cand = [p for p in D1 if p.split()[-1] == pl.split()[-1]]
        if len(cand) == 1: pl = cand[0]
        else: rep.append(f"POST-PLAYER? {t}"); continue
    sd = "LS" if pathlib.Path(f).stem == "2026-world-championship-justin-desai-ds-luke-saga" else m.group(3)
    if sd != m.group(3): rep.append(f"POST-SIDE {t}: deck is Luke Saga (LS); filed as LS")
    posts[(pl, bool(m.group(1)), sd)] = ("https://www.starwarsccg.org/" + pathlib.Path(f).stem + "/", t, pathlib.Path(f))

# ---------- Set 27 pages (not in the public GEMP database yet)
S27 = {}
r = q(action="query", list="categorymembers", cmtitle="Category:Virtual Set 27", cmlimit=200)
for x in r["query"]["categorymembers"]:
    t = x["title"]
    base = re.sub(r" \((?:V|ALT|Virtual Set 27|\d)\)", "", t.replace("•", "")).split(" / ")[0].strip()
    S27.setdefault(base, []).append(t)
    S27.setdefault(re.sub(r" \([^()]*\)$", "", base), []).append(t)
R.fetch([t for v in S27.values() for t in v])

def setno(cid): return int(re.match(r"\d+", cid).group(0))

def wiki_for(cid, title, side):
    """Wiki card page for a GEMP card: the printing whose image set matches the blueprint set."""
    sideW = "Dark" if side == "DS" else "Light"
    title = title.replace("&amp;", "&")
    s = setno(cid)
    if s == 227:
        c = [R._c["pages"].get(t) for t in S27.get(title, [])]
        c = [i for i in c if i and i["card"] and i["side"] == sideW and "(ALT)" not in i["title"]]
        c.sort(key=lambda i: ("(Virtual Set 27)" in i["title"], len(i["title"])))
        return c[0] if c else None
    names = R.prefix(title) + [title]
    if " / " not in title:
        for k in (title + " /", title + " (V) /"):
            if "raw:" + k not in R._c["prefix"]:
                rr = R._q(action="query", list="prefixsearch", pssearch=k, pslimit=40)
                R._c["prefix"]["raw:" + k] = [x["title"] for x in rr["query"]["prefixsearch"]]
            names += R._c["prefix"]["raw:" + k]
    rx = re.compile(re.escape(title).replace("&", "&\\s*•?") + r"( \(V\))?( / .*)?( \([^()]+\))*$")
    cand = [t for t in dict.fromkeys(names) if rx.match(t.replace("•", "")) or rx.match(t)]
    R.fetch(cand)
    ok = [R._c["pages"][t] for t in cand if R._c["pages"].get(t) and R._c["pages"][t]["card"] and not R._c["pages"][t]["dis"]
          and R._c["pages"][t]["side"] == sideW and "(AI)" not in R._c["pages"][t]["title"] and "(ALT)" not in R._c["pages"][t]["title"]]
    seen = {}
    for i in ok: seen.setdefault(i["title"], i)
    ok = list(seen.values())
    if not ok:
        i = R.resolve(title, s >= 200, sideW) or R.resolve(title, False, sideW)
        tc = " ".join(w[:1].upper() + w[1:] for w in title.split(" "))
        if not i and tc != title:
            return wiki_for(cid, tc, side)
        return i
    if s >= 200:
        pre = f"V{s - 200}-"
        hit = [i for i in ok if i["image"].startswith(pre)]
        if hit:
            hit.sort(key=lambda i: ("(Virtual Set" in i["title"], "(V)" not in i["title"], len(i["title"])))
            return hit[0]
    if s < 200:
        plain = [i for i in ok if "(V)" not in i["title"] and not re.match(r"(V\d|VB|VSh|OVS|PS\d)", i["image"])]
        if plain:
            plain.sort(key=lambda i: ("(Virtual Set" in i["title"], len(i["title"])))
            return plain[0]
    ok.sort(key=lambda i: ("(Virtual Set" in i["title"], len(i["title"])))
    return ok[0]

def label_of(i, gemp_title):
    t = i["title"]
    lab = re.sub(r"( \((?!V\))[^()]*\))+$", "", t).replace("•", "")
    if " / " in lab and " / " not in gemp_title:
        lab = lab.split(" / ")[0] + (" (V)" if "(V)" in t and "(V)" not in lab.split(" / ")[0] else "")
    return lab

def link(i, gemp_title):
    lab = label_of(i, gemp_title)
    return f"[[{i['title']}]]" if lab == i["title"] else f"[[{i['title']}|{lab}]]"

CAT = {"CHARACTER": "Character", "DEVICE": "Device", "EFFECT": "Effect", "EPIC_EVENT": "Epic Event", "LOCATION": "Location",
       "OBJECTIVE": "Objective", "JEDI_TEST": "Jedi Test", "PODRACER": "Podracer", "STARSHIP": "Starship", "VEHICLE": "Vehicle",
       "WEAPON": "Weapon", "INTERRUPT": "Interrupt", "DEFENSIVE_SHIELD": "Defensive Shield", "ADMIRALS_ORDER": "Admiral's Order",
       "CREATURE": "Creature"}
LEFT = ["Character", "Device", "Effect", "Epic Event", "Location", "Objective", "Jedi Test", "Podracer", "Creature"]
RIGHT = ["Starship", "Vehicle", "Weapon", "Interrupt", "Admiral's Order", "Defensive Shield"]
_text = {}
def page_text(t):
    if t not in _text:
        r = q(action="query", prop="revisions", rvprop="content", rvslots="main", titles=t)
        p = r["query"]["pages"][0]
        _text[t] = p["revisions"][0]["slots"]["main"]["content"] if p.get("revisions") else ""
    return _text[t]

def deck_title(player, t8, side, arch):
    return f"2026 Worlds {'Top 8 ' if t8 else ''}{player} {side} {norm_arch(arch)}"

# ---------- build decks
built = {}
for (player, t8, side), (f, fname, arch) in sorted(files.items()):
    xml = open(f, encoding="utf-8").read()
    cards = [(re.sub(r"[*^]+$", "", c), html.unescape(t), tag) for tag, c, t in
             re.findall(r'<(card|cardOutsideDeck) blueprintId="([^"]+)"[^>]*title="([^"]*)"', xml)]
    groups = collections.defaultdict(collections.Counter); info = {}; unres = []
    obj = epic = None; ints = []; locs = []
    for cid, t, tag in cards:
        i = wiki_for(cid, t, side)
        row = DB.get(cid, {})
        cat = "Defensive Shield" if tag == "cardOutsideDeck" else CAT.get(row.get("cardCategory", ""), None) or (i["type"] if i else "Not identified")
        if cat == "Admiral's Order" or (cat or "").lower().startswith("admiral"): cat = "Admiral's Order"
        key = i["title"] if i else "TEXT:" + t
        groups[cat][key] += 1; info[key] = (i, t)
        if not i: unres.append(t)
        if tag != "card": continue
        gt = (row.get("gameText") or "")
        if not row and i and cat == "Interrupt":
            gt = page_text(i["title"])
        if cat == "Objective" and not obj: obj = (i, t)
        elif cat == "Epic Event" and not epic and ("only at start of game" in gt.lower() or "deploy on table" in gt.lower()): epic = (i, t)
        elif cat == "Interrupt" and "STARTING" in gt and key not in [k for k, _ in ints]: ints.append((key, (i, t)))
        if cat == "Location": locs.append((cid, t, i))
    n_main = sum(n for c, g in groups.items() if c != "Defensive Shield" for n in g.values())
    def col(heads):
        o = []
        for h in heads:
            if h not in groups: continue
            o.append(f"'''{h}'''")
            for key, n in sorted(groups[h].items(), key=lambda kv: label_of(info[kv[0]][0], info[kv[0]][1]).lower() if info[kv[0]][0] else kv[0][5:].lower()):
                i, t = info[key]
                o.append(f"* {n}x " + (link(i, t) if i else t))
            o.append("")
        return "\n".join(o).rstrip()
    extra = [h for h in groups if h not in LEFT + RIGHT]
    left, right = col(LEFT), col(RIGHT)
    if extra: right = (right + "\n\n" + col(extra)).strip()
    # starting card
    start_bits = []
    ltww = any(k.startswith("Let The Wookiee Win") and "(V)" in k for k, _ in ints)
    if ltww and not obj:
        two = [(t, i) for cid, t, i in locs if not (t == "Kashyyyk" or t.startswith("Kashyyyk:"))
               and sum((x.get("count") or 0) for x in (DB.get(cid, {}).get("icons") or []) if x.get("icon") == "LIGHT_FORCE") == 2]
        two = list({t: (t, i) for t, i in two}.values())
        if len(two) == 1:
            start_bits.append(link(two[0][1], two[0][0]) + " <small>(inferred: Let The Wookiee Win (V) requires a starting location with exactly two [Light]; Kashyyyk locations are deployed by that interrupt)</small>")
    if obj: start_bits.append(link(obj[0], obj[1]) if obj[0] else obj[1])
    elif epic: start_bits.append(link(epic[0], epic[1]) if epic[0] else epic[1])
    start_line = "* '''Starting Card:''' " + (" · ".join(start_bits) if start_bits else "—")
    int_line = "* '''Starting Interrupt:''' " + (" · ".join(link(i, t) if i else t for _k, (i, t) in ints) if ints else "—")
    if obj and obj[0]:
        hub_label = label_of(obj[0], obj[1])
    elif epic and epic[0]:
        hub_label = label_of(epic[0], epic[1])
    else:
        strat = [(k, it) for k, it in ints if not re.match(r"(Prepared Defenses|Heading For The Medical Frigate|Any Methods Necessary|Combat Readiness|Surface Defense|Operational As Planned)", k)]
        hub_label = label_of(strat[0][1][0], strat[0][1][1]) if strat and strat[0][1][0] else norm_arch(arch)
    title = deck_title(player, t8, side, arch)
    gfile = fname
    post = posts.get((player, t8, side))
    # cross-check against the post
    note = ""
    if post:
        d = P.parse(post[2]); tot = sum(c[0] for c in d["cards"])
        if tot and tot != n_main:
            rep.append(f"COUNT {title}: GEMP {n_main} main-deck cards, post {tot}")
    else:
        rep.append(f"NO-POST {title}")
    if n_main != 60:
        rep.append(f"GEMP-COUNT {title}: {n_main}")
    if unres: rep.append(f"UNRESOLVED {title}: {unres}")
    built[(player, t8, side)] = dict(title=title, hub_label=hub_label, start=start_line, ints=int_line, left=left, right=right,
                                     gfile=gfile, src=f, post=post, n=n_main)

# Emmett Armstrong DS: the GEMP file lacks 2x The Ebb Of Battle (not coded in GEMP); the post lists them.
EBB_NOTE = {}
for k, b in built.items():
    if k[0] == "Emmett Armstrong" and k[2] == "DS" and b["n"] == 58:
        EBB_NOTE[k] = True

companion = {}
for (p, t8, s), b in built.items():
    o = built.get((p, t8, "LS" if s == "DS" else "DS"))
    companion[(p, t8, s)] = o["title"] if o else ""

rows = []
for k, b in built.items():
    player, t8, side = k
    sw = "Dark" if side == "DS" else "Light"
    srcs = []
    if b["post"]:
        srcs.append(f"* [{b['post'][0]} {b['post'][1]}], starwarsccg.org")
    srcs.append(f"* [{GEMP_TOPIC} Decklist Files for the 2026 World Championships], forum.starwarsccg.org (GEMP file: {b['gfile']})")
    srcs.append(f"* [{PC_HUB} 2026-11 SWCCG World Championship – Bloomington, Minnesota (Oct. 23-25, 2026)], starwarsccg.org")
    extra_note = ""
    if k in EBB_NOTE:
        extra_note = ("\nThe list as posted has 60 cards, including 2x '''The Ebb Of Battle''' (Interrupt), a new card GEMP has not coded yet; "
                      "the GEMP file leaves them out (58 cards).<ref name=\"gempzip\">[" + GEMP_TOPIC + " Decklist Files for the 2026 World Championships], forum.starwarsccg.org</ref>\n")
    body = f"""== Deck info ==
* '''Player:''' [[{player}]]
* '''Event:''' [[{EVENT}]]
* '''Stage:''' {'Top 8' if t8 else 'Day 1'}
* '''Format:''' [[Open]]
* '''Side:''' [[{sw}]]
{b['start']}
{b['ints']}
* '''GEMP Importable deck:''' [[Media:{b['gfile']}|Download]]

== Decklist ==
{extra_note}
{{| class="wikitable" style="width:100%;"
|-
| style="width:50%; vertical-align:top;" |
{b['left']}

| style="width:50%; vertical-align:top;" |
{b['right']}

|}}

== See also ==
* [[{EVENT}]]
* [[List of SWCCG tournaments]]
{('* [[' + companion[k] + ']]') if companion[k] else ''}

== Sources ==
{chr(10).join(srcs)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:Tournaments]]
[[Category:{sw} Side decks]]
[[Category:2026]]
"""
    fn = re.sub(r"[^A-Za-z0-9._()-]", "_", b["title"]) + ".wiki"
    (OUT / "pages" / fn).write_text(body, encoding="utf-8")
    rows.append(f"{b['title']}\tpages/{fn}")
    (OUT / "gemp" / b["gfile"]).write_bytes(open(b["src"], "rb").read())

# ---------- hub
def cell(p, t8, s):
    b = built.get((p, t8, s))
    return f"[[{b['title']}|{b['hub_label']}]]" if b else "—"
t8rows = ['{| class="wikitable sortable"', "! Finish !! Player !! Dark !! Light"]
for i, p in enumerate(T8, 1):
    t8rows += ["|-", f"| {i} || [[{p}]] || {cell(p, True, 'DS')} || {cell(p, True, 'LS')}"]
t8rows.append("|}")
d1rows = ['{| class="wikitable sortable"', "! Day 1 !! Player !! Dark !! Light"]
for i, p in enumerate(D1, 1):
    d1rows += ["|-", f"| {i} || [[{p}]] || {cell(p, False, 'DS')} || {cell(p, False, 'LS')}"]
d1rows.append("|}")
hubtxt = f"""'''2026 World Championship''' was the 31st annual Players Committee World Championship, held in Bloomington, Minnesota, 23–25 October 2026 (constructed 24–25 October). [[Brian Fred]] defeated [[Justin Desai]] in the Final Confrontation.<ref name="pc">[{PC_HUB} 2026-11 SWCCG World Championship – Bloomington, Minnesota (Oct. 23-25, 2026)], starwarsccg.org</ref><ref name="t8">[{T8_TOPIC} 2026 World Championship Top 8], forum.starwarsccg.org</ref>

The main event is [[Open]] constructed: Day 1 Swiss (58 players, eight games, no drops), then Top 8. [[Bryan Mischke]] took the eighth Top 8 seat in a play-in game against [[Chris Wirfs]] (both 6–2).<ref name="t8" />

== Format ==

* '''Environment:''' [[Open]] (Virtual Set 27 legal)
* '''Site:''' Bloomington, Minnesota
* '''Dates:''' 23–25 October 2026
* '''Forum:''' [{FORUM} 2026 World Championship Forum]
* '''GEMP importable decks:''' [{GEMP_TOPIC} forum t=87042]
* '''Pairings and results:''' [{PAIR_TOPIC} forum t=87035]

== Top 8 ==

Day 2 finish as published.<ref name="pc" />

{chr(10).join(t8rows)}

== Day 1 ==

Day 1 standings and lists as published.<ref name="pc" />

{chr(10).join(d1rows)}

== See also ==

* [[2025 World Championship]]
* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]

== Sources ==

* [{PC_HUB} 2026-11 SWCCG World Championship – Bloomington, Minnesota (Oct. 23-25, 2026)], starwarsccg.org
* [{GEMP_TOPIC} Decklist Files for the 2026 World Championships], forum.starwarsccg.org
* [{T8_TOPIC} 2026 World Championship Top 8], forum.starwarsccg.org
* [{PAIR_TOPIC} 2026 World Championship Pairings & Results], forum.starwarsccg.org
* [{FORUM} 2026 World Championship Forum], forum.starwarsccg.org

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:2026]]
"""
(OUT / "pages" / "2026_World_Championship.wiki").write_text(hubtxt, encoding="utf-8")
rows.insert(0, f"{EVENT}\tpages/2026_World_Championship.wiki")
(OUT / "all.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
json.dump({f"{k[0]}|{k[1]}|{k[2]}": {x: v for x, v in b.items() if x in ("title", "hub_label", "gfile")} for k, b in built.items()},
          open(OUT / "built.json", "w"), ensure_ascii=False, indent=1)
(OUT / "report.txt").write_text("\n".join(rep) + "\n", encoding="utf-8")
print(len(rows), "pages"); print("\n".join(rep))
