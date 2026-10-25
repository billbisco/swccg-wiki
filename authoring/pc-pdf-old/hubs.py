"""hubs.py <events.json> <final_dir> : event hub pages, person page edits/new stubs, List of SWCCG tournaments rows.
Reads final/decks-built.json (from build.py). Fetches live person pages / the tournament list."""
import json, re, sys, pathlib, collections
sys.path.insert(0, "/home/claude/sw2/authoring/pc-pdf-scans")
import resolve_wiki as R
events = json.load(open(sys.argv[1])); final = pathlib.Path(sys.argv[2])
decks = json.load(open(final / "decks-built.json"))
out = final / "pages"; rows = []
def live(title):
    r = R._q(action="query", titles=title, prop="revisions", rvprop="content", rvslots="main")
    p = r["query"]["pages"][0]
    return p["revisions"][0]["slots"]["main"]["content"] if p.get("revisions") else None
def fn(t): return re.sub(r"[^\w.-]+", "_", t) + ".wiki"
def put(t, text):
    (out / fn(t)).write_text(text, encoding="utf-8"); rows.append(f"{t}\tpages/{fn(t)}")
for d in decks: rows.append(f"{d['title']}\tpages/{d['_fn']}")

hubs = collections.OrderedDict()
for stem, ev in events.items():
    hubs.setdefault(ev["hub"], []).append(stem)
def surname_key(p): return (p.split()[-1].lower() if " " in p else p.lower(), p.lower())
def esc(s): return (s or "").replace("[", "&#91;").replace("]", "&#93;")

for hub, stems in hubs.items():
    ev0 = events[stems[0]]
    stages = []
    for st in stems:
        ev = events[st]; lab = ev.get("stage") or ev.get("section", "Decklists")
        if lab not in [s[0] for s in stages]: stages.append((lab, st))
    secs = []
    for lab, _ in sorted(stages, key=lambda s: s[0], reverse=True):
        ds = [d for d in decks if events[d["evkey"]]["hub"] == hub and (events[d["evkey"]].get("stage") or events[d["evkey"]].get("section", "Decklists")) == lab]
        bypl = collections.OrderedDict()
        for d in sorted(ds, key=lambda d: surname_key(d["player"])):
            bypl.setdefault(d["player"], {})[d["side"]] = d
        t = ["{| class=\"wikitable sortable\"", "! Player !! Dark !! Light"]
        for p, s in bypl.items():
            cell = lambda x: f"[[{x['title']}|{x['_deckname']}]]" if x else "—"
            t += ["|-", f"| [[{p}]] || {cell(s.get('DS'))} || {cell(s.get('LS'))}"]
        t.append("|}")
        secs.append(f"== {lab} ==\n\n" + "\n".join(t))
    srcs = []
    for st in stems:
        for u, l in events[st]["sources"]:
            line = f"* [{u} {l}]"
            if line not in srcs: srcs.append(line)
    stand = ""
    if ev0.get("results"):
        import difflib
        R0 = json.load(open(pathlib.Path(__file__).parent / ev0["results"]))
        evpl = sorted({d["player"] for d in decks if events[d["evkey"]]["hub"] == hub})
        rows_ = ["{| class=\"wikitable\"", "! Place !! Player !! Record"]
        for r in R0["rows"]:
            nw = re.sub(r'\s*\(.*?\)|"[^"]*"', "", r["name_written"]).strip()
            m = [p for p in evpl if p.lower() == nw.lower()] or difflib.get_close_matches(nw, evpl, n=1, cutoff=0.75) \
                or [p for p in evpl if p.split()[0].lower() == nw.split()[0].lower() and len(nw.split()) == 1]
            who = f"[[{m[0]}]]" if m else esc(r["name_written"])
            rows_ += ["|-", f"| {r['place']} || {who} || {esc(r.get('record', ''))}"]
        rows_.append("|}")
        stand = "== Standings ==\n\nStandings as given in the PDF.\n\n" + "\n".join(rows_) + "\n\n"
    pdfs = ", ".join(f"[[:File:{events[s]['pdf_file']}]]" for s in stems)
    win = ev0.get("winner")
    text = f"""'''{hub}''' was a Players Committee {ev0.get('kind', 'constructed event')}, {ev0['date']}, using the pre-reset virtual pool ([[{ev0['format']}]]). The deck sheets below are transcribed from the Players Committee's scanned decklist PDF{'s' if len(stems) > 1 else ''} ({pdfs}).{(' ' + ev0['note']) if ev0.get('note') else ''}

== Format ==

* '''Environment:''' [[{ev0['format']}]]
* '''Site:''' {ev0.get('site') or '—'}
* '''Dates:''' {ev0['date']}
* '''Winner:''' {('[[' + win + ']]') if win else '—'}

{stand}{chr(10).join(s + chr(10) for s in secs)}
== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [[{ev0['format']}]]

== Sources ==

{chr(10).join(srcs)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:{ev0['iso'][:4]}]]
"""
    put(hub, text)

# ---- person pages
per = collections.defaultdict(list)
for d in decks: per[d["player"]].append(d)
newp, edited = [], []
for p, ds in sorted(per.items()):
    txt = live(p)
    # one row per event+stage
    rws = collections.OrderedDict()
    for d in ds:
        ev = events[d["evkey"]]
        k = (ev["hub"], ev.get("stage", ""))
        rws.setdefault(k, {"ev": ev, "s": {}})["s"][d["side"]] = d
    def row(k, v):
        ev = v["ev"]; c = lambda x: f"[[{x['title']}|{x['_deckname']}]]" if x else "—"
        stg = f" ({ev['stage']})" if ev.get("stage") else ""
        return f"| {ev['date']} || [[{ev['hub']}]]{stg} || [[{ev['format']}]] || — || {c(v['s'].get('DS'))} || {c(v['s'].get('LS'))}"
    newrows = [(v["ev"]["iso"], k, row(k, v)) for k, v in rws.items()]
    if txt is None:
        hubsl = sorted({k[0] for _, k, _ in newrows})
        body = "\n|-\n".join(r for _, _, r in sorted(newrows, reverse=True))
        cats = sorted({v["ev"]["iso"][:4] for v in rws.values()})
        text = f"""'''{p}''' played the {', '.join('[[' + h + ']]' for h in hubsl)}.

== Tournament Results ==

{{| class="wikitable"
|-
! Date !! Event !! Format !! Finish !! Dark !! Light
|-
{body}
|}}

== See also ==

{chr(10).join('* [[' + h + ']]' for h in hubsl)}
* [[List of SWCCG tournaments]]
* [[Championships]]

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Players]]
{chr(10).join('[[Category:' + c + ']]' for c in cats)}
"""
        put(p, text); newp.append(p); continue
    if re.match(r"#REDIRECT", txt, re.I):
        print("REDIRECT person", p); continue
    t = txt
    for iso, k, r in sorted(newrows, reverse=True):
        anyt = [x for x in ds if events[x["evkey"]]["hub"] == k[0]]
        if any(f"[[{x['title']}|" in t for x in anyt): continue
        m = re.search(r"(== Tournament Results ==\s*\{\| class=\"wikitable\"[^\n]*\n(?:\|-\n)?! Date[^\n]*\n)(.*?)(\n\|\})", t, re.S)
        if not m:
            tbl = "\n\n{| class=\"wikitable\"\n|-\n! Date !! Event !! Format !! Finish !! Dark !! Light\n|-\n" + r + "\n|}\n"
            if "== See also ==" in t: t = t.replace("== See also ==", "== Tournament Results ==" + tbl + "\n== See also ==", 1)
            else: t += "\n== Tournament Results ==" + tbl
            continue
        # insert sorted by ISO date found in each row (rows may lack ISO; use year)
        body = m.group(2)
        parts = re.split(r"\n\|-\n", "\n" + body.strip("\n")) if body.strip() else []
        parts = [x.strip("\n") for x in parts if x.strip() and x.strip() != "|-"]
        def yr(x):
            y = re.findall(r"\b(19|20)(\d\d)\b", x.split("||")[0])
            return int(y[-1][0] + y[-1][1]) if y else 0
        idx = len(parts)
        for i, x in enumerate(parts):
            if yr(x) and yr(x) < int(iso[:4]): idx = i; break
        parts.insert(idx, r)
        t = t[:m.start(2)] + "|-\n" + "\n|-\n".join(parts) + t[m.end(2):]
    for k in {k for _, k, _ in newrows}:
        if f"* [[{k[0]}]]" not in t and "== See also ==" in t:
            t = t.replace("== See also ==\n\n", f"== See also ==\n\n* [[{k[0]}]]\n", 1)
    for c in sorted({v["ev"]["iso"][:4] for v in rws.values()}):
        if f"[[Category:{c}]]" not in t: t = t.rstrip("\n") + f"\n[[Category:{c}]]\n"
    if t != txt:
        put(p, t); edited.append(p)

# ---- List of SWCCG tournaments
lt = live("List of SWCCG tournaments")
t = lt
for hub, stems in hubs.items():
    ev = events[stems[0]]; yr = ev["iso"][:4]
    if f"[[{hub}|" in t: continue
    short = hub[5:]
    r = f"| {ev['iso']} || [[{hub}|{short}]] || {ev['date']} || {ev.get('site') or '—'} || [[{ev['format']}]] || {('[[' + ev['winner'] + ']]') if ev.get('winner') else '—'}"
    m = re.search(r"(== " + yr + r" ==\s*\{\| class=\"wikitable sortable\"\n\|-\n! Tag[^\n]*\n)(.*?)(\n\|\})", t, re.S)
    if not m:
        print("NO YEAR SECTION", yr); continue
    parts = [x.strip("\n") for x in re.split(r"\n\|-\n", "\n" + m.group(2).strip("\n")) if x.strip() and x.strip() != "|-"]
    idx = len(parts)
    for i, x in enumerate(parts):
        tag = x.split("||")[0].strip("| ").strip()
        if tag < ev["iso"]: idx = i; break
    parts.insert(idx, r)
    t = t[:m.start(2)] + "|-\n" + "\n|-\n".join(parts) + t[m.end(2):]
if t != lt: put("List of SWCCG tournaments", t)
(final / "all.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
print("hubs", len(hubs), "new persons", len(newp), "edited persons", len(edited), "rows", len(rows))
json.dump({"new": newp, "edited": edited}, open(final / "persons.json", "w"), indent=1)
