#!/usr/bin/env python3
"""2001-2006 typed decklists (PC forms on theforce.net, DeckTech/Wayback posts) -> deck pages, hubs, person rows.
python3 gen_typed.py -> final/pages/*.wiki, final/all.tsv, final/report.txt"""
import json, re, sys, glob, pathlib, collections, urllib.request, urllib.parse, time
HERE = pathlib.Path(__file__).parent
OLD = HERE.parent / "old"
sys.path.insert(0, "/home/claude/sw2/authoring/pc-pdf-scans")
import resolve_wiki as R
b = open(OLD / "build.py").read()
defs = b[b.index("LEFT = ["):b.index("# ---- load decks")] + "\n" + re.search(r"^def esc.*$", b, re.M).group(0)
B = {"R": R, "re": re, "json": json}
exec(compile(defs, "build", "exec"), B)
LEFT, RIGHT, cardlink, esc, norm_type, resolve_line, norm_resolve = (B[k] for k in ("LEFT", "RIGHT", "cardlink", "esc", "norm_type", "resolve_line", "norm_resolve"))
F = HERE / "final"; (F / "pages").mkdir(parents=True, exist_ok=True)
rep = []
API = "https://wiki.swccg.com/api.php"
def q(**k):
    k.update(format="json", formatversion=2)
    for a in range(6):
        try:
            return json.load(urllib.request.urlopen(urllib.request.Request(API, data=urllib.parse.urlencode(k).encode(), headers={"User-Agent": "HolocronClaude-typed"}), timeout=90))
        except Exception:
            time.sleep(4)
def live(t):
    p = q(action="query", titles=t, prop="revisions", rvprop="content", rvslots="main", redirects=1)["query"]["pages"][0]
    return (p["title"], p["revisions"][0]["slots"]["main"]["content"]) if p.get("revisions") else (t, None)

PLAYER = {"Jonathan Chu": "Jonny Chu", "Joseph Giannetti": "Joe Giannetti", "Bobby Hilbun": "Bobby Hilburn"}
# event -> (dates text, iso, site, format) for events that have no hub yet
VS = [("2002-06-01", "Premiere - Original VS1"), ("2002-09-20", "Premiere - Original VS2"), ("2003-02-05", "Premiere - Original VS3"),
      ("2003-06-01", "Premiere - Original VS4"), ("2004-01-12", "Premiere - Original VS5"), ("2006-12-04", "Premiere - Original VS6")]
def pool(iso):
    for lim, f in VS:
        if iso < lim: return f
    return "Premiere - Original VS11"
EV = {
 "2003 DPC Atlanta": ("February 2003", "2003-02-01", "Atlanta, Georgia"),
 "2003 DPC Chicago": ("12 April 2003", "2003-04-12", "Chicago, Illinois"),
 "2003 MegaCon": ("1 March 2003", "2003-03-01", "Orlando, Florida"),
 "2003 Maryland State Championship": ("April 2003", "2003-04-01", "Maryland"),
 "2003 Georgia State Championship": ("May 2003", "2003-05-01", "Georgia"),
 "2003 Chandrila State Championship": ("June 2003", "2003-06-01", "Italy"),
 "2003 Minnesota State Championship": ("2003", "2003-06-01", "Minnesota"),
 "2003 Florida State Championship": ("2003", "2003-08-01", "Florida"),
 "2003 Origins": ("June 2003", "2003-06-26", "Columbus, Ohio"),
 "2004 DPC Atlanta": ("2004", "2004-02-01", "Atlanta, Georgia"),
 "2004 Washington State Championship": ("2004", "2004-05-01", "Washington"),
 "2004 Illinois State Championship": ("2004", "2004-06-01", "Illinois"),
 "2004 Origins": ("July 2004", "2004-07-01", "Columbus, Ohio"),
 "2004 Mystic Visions": ("July 2004", "2004-07-15", None),
 "2004 European Championship": ("2004", "2004-07-01", None),
 "2004 German Open (Ralltiir)": ("2004", "2004-06-01", "Germany"),
 "2005 Corellia Regional": ("9 January 2005", "2005-01-09", None),
 "2005 Michigan Mini-Open": ("12 March 2005", "2005-03-12", "Michigan"),
 "2005 Ohio State Championship": ("April 2005", "2005-04-01", "Ohio"),
 "2005 Norwegian National Championship": ("April 2005", "2005-04-01", "Norway"),
 "2005 U.S. National Championship": ("July 2005 (Origins)", "2005-07-01", "Columbus, Ohio"),
 "2005 New York State Championship": ("July 2005", "2005-07-01", "New York"),
 "2006 Yavin IV Regional": ("1 April 2006", "2006-04-01", None),
 "2006 Bespin Regional": ("April 2006", "2006-04-15", None),
 "2006 Tennessee DPC": ("10 June 2006", "2006-06-10", "Tennessee"),
 "2006 Rhode Island State Championship": ("2 July 2006", "2006-07-02", "Rhode Island"),
 "2006 Massachusetts State Championship": ("1 July 2006", "2006-07-01", "Massachusetts"),
 "2006 Minnesota State Championship": ("July 2006", "2006-07-15", "Minnesota"),
}
EXIST = {"2001 Washington State Championship": "2001-04-21", "2002 NYC Mini-Open": "2002-06-01", "2002 Origins Open": "2002-07-04",
         "2002 World Championship": "2002-11-01", "2003 World Championship": "2003-08-29", "2004 World Championship": "2004-08-01",
         "2005 World Championship": "2005-08-18", "2006 World Championship": "2006-10-19"}
EXIST_FMT = {"2001 Washington State Championship": "Premiere - Reflections II"}
CRUDE = {"DіCK HAT", "SYCF(A)UCK MegaCon Undefeated 3rd Place"}

decks = [json.load(open(f)) for f in sorted(glob.glob(str(HERE / "out" / "*.json")))]
for d in decks:
    d["player"] = PLAYER.get(d["player"], d["player"])
    iso = EXIST.get(d["event"]) or EV[d["event"]][1]
    d["_iso"] = iso
    d["_fmt"] = EXIST_FMT.get(d["event"]) or pool(iso)
    if d["stage"] == "6 V-Card Tournament": d["_fmt"] = None
    side = "Dark" if d["side"] == "DS" else "Light"
    st = d.get("start") or ""
    si = None
    if st:
        sv = any(x.get("v") and (x.get("card") or "").split(" / ")[0] == st.split(" / ")[0] for x in d["lines"])
        si = resolve_line(st, sv, side, False, False, "original") or R.resolve(st, False, side)
    d["_start"] = si
    name = B["label"](si["title"].split(" / ")[0]) if si else (st.split(" / ")[0] if st else "")
    if si and "(V)" in si["title"] and "(V)" not in name: name += " (V)"
    d["_deckname"] = name or "Deck"
    stg = f" {d['stage']}" if d.get("stage") and d["stage"] not in ("",) else ""
    d["title"] = f"{d['event']}{stg} {d['player']} {d['side']} {d['_deckname']}".replace("  ", " ")
c = collections.Counter(d["title"] for d in decks)
for d in decks:
    if c[d["title"]] > 1:
        d["title"] += f" ({re.sub(r'[^A-Za-z0-9 ]', '', d['deck_name'])[:40].strip()})"
        rep.append(f"DUP-TITLE -> {d['title']}")

rows = []
def fn(t): return re.sub(r"[^\w.-]+", "_", t) + ".wiki"
def put(t, text):
    (F / "pages" / fn(t)).write_text(text, encoding="utf-8"); rows.append(f"{t}\tpages/{fn(t)}")
built = []
for d in decks:
    side = "Dark" if d["side"] == "DS" else "Light"
    groups = collections.OrderedDict(); unres = []
    def add(x, shield):
        name = (x.get("card") or "").strip()
        info = resolve_line(name, x.get("v"), side, x.get("ep1"), shield, "original") if name else None
        if info is None and name: info = norm_resolve(name, x.get("v"), side, False, shield, True)
        n = int(x.get("qty") or 1)
        if info is None:
            key = ("Defensive Shield" if shield else "Not identified", "TEXT:" + (x.get("text") or name))
            unres.append(x.get("text") or name)
        else:
            typ = "Defensive Shield" if shield else norm_type(info["type"])
            if shield and info["type"] != "Defensive Shield": typ = "Defensive Shield"
            key = (typ, info["title"])
        g = groups.setdefault(key[0], collections.OrderedDict()); g[key[1]] = (g.get(key[1], (0, info))[0] + n, info)
    for x in d["lines"]: add(x, False)
    for x in d.get("shields", []): add(x, True)
    if unres: rep.append(f"UNRESOLVED {d['title']}: {unres}")
    def col(hs):
        o = []
        for h in hs:
            if h not in groups: continue
            o.append(f"'''{h}'''")
            for k, (n, info) in groups[h].items():
                o.append("* " + (f"{n}x " if n > 1 else "") + (cardlink(info) if info else esc(k[5:])))
            o.append("")
        return "\n".join(o).rstrip("\n")
    intro = ""
    if "Not identified" in groups or any(k.startswith("TEXT:") for k in groups.get("Defensive Shield", {})):
        intro = "Lines that could not be matched to a card page are printed as written.\n\n"
    body = intro + '{| class="wikitable" style="width:100%;"\n|-\n| style="width:50%; vertical-align:top;" |\n' + col(LEFT) + '\n| style="width:50%; vertical-align:top;" |\n' + col(RIGHT) + "\n|}\n"
    src = d["source_url"]; wb = d.get("wayback_url") or ""
    is_pdf = src.lower().endswith(".pdf")
    by = d.get("posted_by") or ""
    if is_pdf:
        how = "from the official Players Committee decklist form"
    else:
        how = f"as posted on DeckTech{(' by ' + esc(by)) if by else ''}{(' (' + esc(d['posted_date']) + ')') if d.get('posted_date') else ''}"
    ref = f'<ref name="src">[{src} {esc(d.get("source_title") or d["deck_name"])}]' + (f". Preserved copy: [{wb} Internet Archive]" if wb else "") + "</ref>"
    stage = d.get("stage") or ""
    place = d.get("place") or ""
    lead = (f"'''{d['title']}''' was the {side} Side constructed list played by [[{d['player']}]] at [[{d['event']}]]"
            f"{(' (' + stage + ')') if stage else ''}{(', finishing ' + place) if place else ''}; the list below is {how}.{ref}")
    info_lines = [f"* '''Player:''' [[{d['player']}]]", f"* '''Event:''' [[{d['event']}]]"]
    if stage: info_lines.append(f"* '''Stage:''' {stage}")
    if place: info_lines.append(f"* '''Finish:''' {place}")
    info_lines.append(f"* '''Side:''' [[{side}]]")
    if d["_start"]: info_lines.append("* '''Starting Card:''' " + cardlink(d["_start"]))
    elif d.get("start"): info_lines.append("* '''Starting Card:''' " + esc(d["start"]))
    if d.get("deck_name") and d["deck_name"] not in CRUDE: info_lines.append("* '''Deck name:''' " + esc(d["deck_name"]))
    if d["_fmt"]: info_lines.append(f"* '''Format:''' [[{d['_fmt']}]]")
    info_lines.append(f"* '''Source:''' [{src} {'PC decklist form' if is_pdf else 'DeckTech post'}]" + (f" (preserved copy: [{wb} Internet Archive])" if wb else ""))
    note = f"\n'''Note:''' {esc(d['flag'])}<ref name=\"src\" />\n" if d.get("flag") else ""
    text = f"""{lead}
{note}
== Deck info ==

{chr(10).join(info_lines)}

== Decklist ==

{body}
== See also ==

* [[{d['event']}]]
* [[{d['player']}]]
* [[List of SWCCG tournaments]]

== Sources ==

* [{src} {esc(d.get('source_title') or d['deck_name'])}]{(' — [' + wb + ' Internet Archive copy]') if wb else ''}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:{d['_iso'][:4]}]]
"""
    put(d["title"], text)
    built.append(d)

# ---------- hubs
byev = collections.defaultdict(list)
for d in built: byev[d["event"]].append(d)
def table(ds):
    by = collections.OrderedDict()
    for d in sorted(ds, key=lambda d: (d.get("stage") or "", d["player"].split()[-1])):
        by.setdefault((d.get("stage") or "", d["player"]), {})[d["side"]] = d
    t = ['{| class="wikitable sortable"', "! Stage !! Finish !! Player !! Dark !! Light"]
    for (stg, p), s in by.items():
        fin = (s.get("DS") or s.get("LS")).get("place") or ""
        cell = lambda x: f"[[{x['title']}|{x['_deckname']}]]" if x else "—"
        t += ["|-", f"| {stg or '—'} || {esc(fin) or '—'} || [[{p}]] || {cell(s.get('DS'))} || {cell(s.get('LS'))}"]
    t.append("|}")
    return "\n".join(t)
for ev, ds in byev.items():
    srcs = sorted({f"* [{d['source_url']} {esc(d.get('source_title') or d['deck_name'])}]" for d in ds})
    if ev in EXIST:
        t, txt = live(ev)
        if txt is None: rep.append(f"HUB-MISSING {ev}"); continue
        sec = "== Decklists from DeckTech and PC forms ==\n\nLists recovered in 2026 from DeckTech posts (Internet Archive copies) and Players Committee decklist forms.\n\n" + table(ds) + "\n\n"
        txt = re.sub(r"\n*Published 60s from this event are not on this wiki yet\.\n", "\n", txt)
        k = txt.find("== See also ==")
        txt = txt[:k] + sec + txt[k:] if k >= 0 else txt + "\n" + sec
        k2 = txt.find("== Sources ==")
        if k2 >= 0:
            j = txt.find("\n\n", k2 + 15)
            add = "\n".join(s for s in srcs if s.split(' ')[0][3:] not in txt)
            if add: txt = txt[:j] + "\n" + add + txt[j:]
        put(t, txt)
    else:
        dates, iso, site = EV[ev]
        fmt = pool(iso)
        kind = "regional" if "Regional" in ev else ("state championship" if "State Championship" in ev else ("national championship" if "National" in ev else "constructed tournament"))
        txt = f"""'''{ev}''' was a Star Wars CCG {kind}{(' in ' + site) if site else ''} ({dates}). It is known from the decklists below, recovered from DeckTech posts and Players Committee forms.

== Format ==

* '''Environment:''' [[{fmt}]] (from the card pool legal on the event date)
* '''Site:''' {site or '—'}
* '''Dates:''' {dates}

== Decklists ==

{table(ds)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Formats]]
* [[{fmt}]]

== Sources ==

{chr(10).join(srcs)}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Tournaments]]
[[Category:{iso[:4]}]]
"""
        put(ev, txt)

# ---------- persons (rows in Tournament Results; stub pages for new players)
per = collections.defaultdict(list)
for d in built: per[d["player"]].append(d)
for p, ds in sorted(per.items()):
    t, txt = live(p)
    rws = collections.OrderedDict()
    for d in ds: rws.setdefault((d["event"], d.get("stage") or ""), {})[d["side"]] = d
    lines = []
    for (ev, stg), s in rws.items():
        x = s.get("DS") or s.get("LS")
        date = EV[ev][0] if ev in EV else x["_iso"][:4]
        cell = lambda y: f"[[{y['title']}|{y['_deckname']}]]" if y else "—"
        fmt = f"[[{x['_fmt']}]]" if x["_fmt"] else "—"
        lines.append(f"|-\n| {date} || [[{ev}]]{(' (' + stg + ')') if stg else ''} || {fmt} || {esc(x.get('place') or '—')} || {cell(s.get('DS'))} || {cell(s.get('LS'))}")
    if txt is None:
        txt = f"""'''{p}''' is a Star Wars CCG player.

== Tournament Results ==

{{| class="wikitable"
! Date !! Event !! Format !! Finish !! Dark !! Light
{chr(10).join(lines)}
|}}

== See also ==

* [[List of SWCCG tournaments]]

[[Category:Players]]
"""
        rep.append(f"NEW PERSON {p}")
    else:
        if all(d["title"] in txt for d in ds): continue
        m = re.search(r"== ?Tournament Results ?==\s*\n\s*\{\|[^\n]*\n(?:\|-\s*\n)?(!.*?\n)", txt)
        if m:
            # append at the end of the table (older events go at the bottom; rows are newest first)
            end = txt.find("\n|}", m.end())
            txt = txt[:end] + "\n" + "\n".join(lines) + txt[end:]
        else:
            sec = "== Tournament Results ==\n\n{| class=\"wikitable\"\n! Date !! Event !! Format !! Finish !! Dark !! Light\n" + "\n".join(lines) + "\n|}\n\n"
            k = txt.find("== See also ==")
            if k < 0: k = txt.find("{{#if:1")
            if k < 0: k = txt.find("[[Category:")
            txt = txt[:k] + sec + txt[k:] if k >= 0 else txt + "\n\n" + sec
    put(t, txt)
(F / "all.tsv").write_text("\n".join(rows) + "\n", encoding="utf-8")
(F / "report.txt").write_text("\n".join(rep) + "\n", encoding="utf-8")
json.dump([{k: v for k, v in d.items() if not k.startswith("_") or k in ("_deckname",)} | {"title": d["title"]} for d in built], open(F / "built.json", "w"), ensure_ascii=False, indent=1)
print(len(rows), "pages"); print("\n".join(rep[:60]))
