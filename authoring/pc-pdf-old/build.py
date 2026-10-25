"""build.py <events.json> <names.tsv> <final_dir>
New decklist pages + event hubs from helper JSONs in out/G*/ (old PC deck-sheet PDFs, never on the wiki).
names.tsv: stem<TAB>page_key<TAB>side<TAB>name_written<TAB>username<TAB>player (canonical; "SKIP" to leave out)
events.json: {stem: {hub, stage, title_stage, date, iso, site, format, pdf_file, sources:[[url,label]], day1_stem}}"""
import json, re, sys, pathlib, collections, glob
sys.path.insert(0, "/home/claude/sw2/authoring/pc-pdf-scans")
import resolve_wiki as R

HERE = pathlib.Path(__file__).parent
events = json.load(open(sys.argv[1]))
OVR = json.load(open(HERE / "event_overrides.json")) if (HERE / "event_overrides.json").exists() else {}
final = pathlib.Path(sys.argv[3]); (final / "pages").mkdir(parents=True, exist_ok=True)
names = {}
for l in open(sys.argv[2], encoding="utf-8"):
    if not l.strip() or l.startswith("stem\t"): continue
    f = l.rstrip("\n").split("\t")
    names[(f[0], f[1])] = f[5].strip()

LEFT = ["Objective", "Character", "Effect", "Interrupt", "Epic Event", "Admiral's Order", "Jedi Test", "Podracer"]
RIGHT = ["Location", "Starship", "Vehicle", "Weapon", "Device", "Creature", "Defensive Shield", "Not identified"]
def norm_type(t):
    t = (t or "").strip()
    if t.lower().startswith("admiral"): return "Admiral's Order"
    return t if t in LEFT + RIGHT else (t or "Not identified")
def label(t):
    return re.sub(r"( \((?!V\))[^()]*\))+$", "", t.replace("•", ""))
def cardlink(i):
    t = i["title"]; lab = label(t)
    s = "{{CardLink|" + t + "|" + i["image"]
    if lab != t: s += "|label=" + lab
    return s + "}}"

def _norm(s):
    s = s.replace("•", "").replace("’", "'").replace("“", '"').replace("”", '"').replace('"', "'")
    return re.sub(r"[^a-z0-9]", "", s.lower())
def _base(t):
    return re.sub(r"( \([^()]*\))+$", "", t)
def rawprefix(q):
    k = "raw:" + q
    if k not in R._c["prefix"]:
        r = R._q(action="query", list="prefixsearch", pssearch=q, pslimit=40)
        R._c["prefix"][k] = [p["title"] for p in r["query"]["prefixsearch"]]
    return R._c["prefix"][k]
def norm_resolve(name, v, side, ep1, shield, original=False):
    """Fallback: titles whose base equals the name ignoring punctuation (Run Luke, Run!; Romas 'Lock' Navander),
    and cards the wiki has only as (V) pages (Galen, Secret Apprentice (V) (Virtual Set 17: ...))."""
    nn = _norm(name)
    cands = set()
    for q in {name, name[:14], re.split(r"[\"'!?,]", name)[0].strip()}:
        if len(q) >= 3:
            try: cands.update(rawprefix(q))
            except Exception: pass
    cands = [t for t in cands if _norm(_base(t.replace(" (V)", ""))) == nn or _norm(_base(t)) == nn]
    if not cands: return None
    R.fetch(cands)
    ok = {}
    for t in cands:
        i = R._c["pages"].get(t)
        if i and i["card"] and not i["dis"] and i["side"] == side and "(AI)" not in i["title"]:
            if shield and i["type"] != "Defensive Shield": continue
            ok.setdefault(i["title"], i)
    ok = list(ok.values())
    if not ok: return None
    plain = [i for i in ok if "(V)" not in i["title"]]
    virt = [i for i in ok if "(V)" in i["title"]]
    pool = (virt or plain) if v else (plain or virt)
    if ep1:
        e = [i for i in pool if "(Coruscant)" in i["title"]]
        pool = e or pool
    else:
        e = [i for i in pool if "(Coruscant)" not in i["title"]]
        pool = e or pool
    if original and v:
        e = [i for i in pool if "(Virtual Set" in i["title"]]
        if e: pool = e
    pool.sort(key=lambda i: ((("(Virtual Set" in i["title"]) != bool(original and v)), len(i["title"]), i["title"]))
    return pool[0]

PREF = {"legacy": ("VB", "VSh", "OVS"), "original": ("OVS", "VSh")}
def era_pick(name, side, shield, era):
    """A ticked (V) line in a pre-2014 deck: the period's virtual printing, by card-image prefix
    (Legacy Virtual Block = VB…, Defensive Shields = VSh…, original Virtual Sets = OVS…), not the post-2014 V0/VS page."""
    base = name.replace(" (V)", "").strip(); nn = _norm(base)
    cands = set()
    for q in {base + " (V)", base[:14]}:
        try: cands.update(rawprefix(q))
        except Exception: pass
    cands = [t for t in cands if "(V)" in t and _norm(_base(t.replace(" (V)", ""))) == nn]
    if not cands: return None
    R.fetch(cands)
    ok = {}
    for t in cands:
        i = R._c["pages"].get(t)
        if i and i["card"] and not i["dis"] and i["side"] == side and "(AI)" not in i["title"]:
            if shield and i["type"] != "Defensive Shield": continue
            ok.setdefault(i["title"], i)
    for pre in PREF[era]:
        hit = sorted([i for i in ok.values() if i["image"].startswith(pre)], key=lambda i: (len(i["title"]), i["title"]))
        if hit: return hit[0]
    return None

def era_fix(i, side, shield, era):
    """A pre-2014 deck must not link a post-2014 printing (V0…/VS… art) when the wiki has the period page
    (Probot (Dark) = VB6, Overseer (Virtual Block 6), …)."""
    if not i or era not in PREF or not re.match(r"(V0|VS\d*)-", i["image"]): return i
    want_v = "(V)" in i["title"]; base = _base(i["title"].replace(" (V)", "")); nn = _norm(base)
    cands = [t for t in rawprefix(base) if _norm(_base(t.replace(" (V)", ""))) == nn and (("(V)" in t) == want_v)]
    R.fetch(cands)
    ok = [R._c["pages"][t] for t in cands if R._c["pages"].get(t) and R._c["pages"][t]["card"] and not R._c["pages"][t]["dis"]
          and R._c["pages"][t]["side"] == side and "(AI)" not in R._c["pages"][t]["title"] and "(ALT)" not in R._c["pages"][t]["title"]
          and (not shield or R._c["pages"][t]["type"] == "Defensive Shield")]
    for pre in PREF[era]:
        hit = sorted([x for x in ok if x["image"].startswith(pre)], key=lambda x: (len(x["title"]), x["title"]))
        if hit: return hit[0]
    return i

def resolve_line(name, v, side, ep1, shield, era=""):
    if not name: return None
    if v and era in PREF:
        i = era_pick(name, side, shield, era)
        if i: return i
    r = _resolve_line(name, v, side, ep1, shield)
    return era_fix(r or norm_resolve(name, v, side, ep1, shield, era == "original"), side, shield, era)

def _resolve_line(name, v, side, ep1, shield):
    if not name: return None
    if shield:
        i = R.resolve_shield(name, v, side)
        if i: return i
    i = R.resolve(name, bool(v), side, ep1)
    if i and (not shield or i["type"] == "Defensive Shield"): return i
    if not v:
        # Legacy-era virtual cards that the wiki only has as a "(V)" page whose art is a Virtual Block card
        j = R.resolve(name, True, side, ep1)
        if j and j["image"].startswith("VB") and (not shield or j["type"] == "Defensive Shield"): return j
    else:
        j = R.resolve(name, False, side, ep1)
        if j and (not shield or j["type"] == "Defensive Shield"): return j
    if shield:
        i = R.resolve(name, bool(v), side, ep1)
        return i
    return None

# ---- load decks
decks = []
for f in sorted(glob.glob(str(HERE / "out" / "G*" / "*.json"))):
    if f.endswith("results.json"): continue
    d = json.load(open(f))
    stem = d["pdf"]; key = pathlib.Path(f).stem.split("-p", 1)[1] if "-p" in pathlib.Path(f).stem else str(d["pages"][0])
    d["_key"] = "p" + key; d["_file"] = f
    d["evkey"] = OVR.get(f"{stem}|{d['_key']}", stem)
    pl = names.get((stem, d["_key"]))
    if pl is None:
        print("NO NAME ROW", stem, d["_key"], d.get("name_written")); continue
    if pl == "SKIP": continue
    d["player"] = pl
    d["side"] = "DS" if d["side"].upper().startswith("D") else "LS"
    for fld in ("lines", "shields"):
        ex = []
        for x in d.get(fld, []):
            n = x.get("count") or 1
            try: n = int(n)
            except Exception: n = 1
            ex += [dict(x, count=1) for _ in range(max(1, n))]
        d[fld] = ex
    for x in d["lines"] + d.get("shields", []) + [c for c in d.get("additional", []) if isinstance(c, dict)]:
        tx = (x.get("text") or ""); tl = tx.lower(); c = x.get("card") or ""
        if "eject" in tl and ("atroc" in tl or " ia" in tl or "combo" in tl or "+" in tl or "&" in tl):
            x["card"] = ""          # "Eject! Eject! & Imperial Atrocity": no card page anywhere; print as written
        elif "cyborg" in tl and "commander" in tl:
            x["card"] = ""
        elif "galen" in tl and "secret" in tl:
            x["card"] = "Galen, Secret Apprentice"
        elif re.sub(r"\s*\(v\)\s*$", "", tl).strip() in ("fallen jedi", "black leader", "blind jedi", "galen's fighter"):
            x["card"] = re.sub(r"\s*\((v|V)\)\s*$", "", tx).strip().title().replace("'S", "'s")   # the 2009 TFU cards as titled then
        elif not c and re.match(r"^\s*(IC|2L|11|TL|IL|1L)\s*-?\s*19\b", tx, re.I) and d["side"] == "LS":
            x["card"] = "IL-19"
        elif not c and re.match(r"^\s*(the )?emperor'?s reach\s*$", tl) and d["side"] == "DS":
            x["card"] = "Maarek Stele, The Emperor's Reach"
    decks.append(d)

report = []
byk = {(events[d["evkey"]]["hub"], events[d["evkey"]].get("stage", ""), d["player"], d["side"]): d for d in decks}

# ---- apply "same as yesterday"
for d in decks:
    if not d.get("same_as"): continue
    ev = events[d["evkey"]]; d1 = events.get(ev.get("day1_stem", ""), {})
    src = byk.get((d1.get("hub", ev["hub"]), d1.get("stage", ""), d["player"], d["side"]))
    if not src:
        report.append(f"SAMEAS-NOSRC {d['pdf']} {d['_key']} {d['player']} {d['side']}"); d["_nosrc"] = True; continue
    lines = [dict(x) for x in src["lines"]]; shields = [dict(x) for x in src.get("shields", [])]
    applied = []
    for c in d.get("changes", []):
        tgt = shields if c.get("shield") else lines
        if c.get("out"):
            for k, x in enumerate(tgt):
                if (x.get("card") or x.get("text") or "").lower() == c["out"].lower():
                    del tgt[k]; break
            else:
                report.append(f"SAMEAS-OUT-MISSING {d['pdf']} {d['_key']} {c['out']}")
        if c.get("in"):
            tgt.append({"n": 0, "text": c.get("in"), "card": c.get("in"), "v": bool(c.get("v_in"))})
        applied.append(c.get("text") or f"-{c.get('out')} +{c.get('in')}")
    d["_day1"] = src; d["_applied"] = applied
    d["lines"] = lines; d["shields"] = shields
    if not d.get("start"): d["start"] = src.get("start", "")

# ---- titles
def front(t):
    return label(t.split(" / ")[0].strip())
for d in decks:
    ev = events[d["evkey"]]; side = "Dark" if d["side"] == "DS" else "Light"
    st = d.get("start") or ""
    sv = "(V)" in st or any(x.get("v") and (x.get("card") or "").split(" / ")[0] == st.split(" / ")[0] for x in d["lines"])
    si = resolve_line(st.replace(" (V)", ""), sv, side, False, False, ev.get("era", "")) if st else None
    if st and not si: si = R.resolve(st.replace(" (V)", ""), False, side) or R.resolve(st.replace(" (V)", ""), True, side)
    if not st:
        # no objective: the deck is named by its first location (the starting location is normally listed first)
        for x in d["lines"]:
            if x.get("card"):
                i = R.resolve(x["card"], bool(x.get("v")), side, x.get("ep1"))
                if i and i["type"] == "Location":
                    si = i; d["_start_from_loc"] = True; break
    d["_start"] = si
    name = front(si["title"]) if si else (front(st) if st else "")
    if si and "(V)" in si["title"] and "(V)" not in name: name += " (V)"
    d["_deckname"] = name or "Deck"
    pre = ev["hub"] + (" " + ev["title_stage"] if ev.get("title_stage") else "")
    d["title"] = f"{pre} {d['player']} {d['side']} {d['_deckname']}".replace("  ", " ")
seen = collections.Counter(d["title"] for d in decks)
for t, n in seen.items():
    if n > 1: report.append(f"DUP-TITLE {t} x{n}")

def esc(s): return (s or "").replace("[", "&#91;").replace("]", "&#93;").replace("{", "&#123;").replace("}", "&#125;").replace("|", "&#124;")

canon = []
SEEN_SCAN = set()
for d in decks:
    ev = events[d["evkey"]]; side = "Dark" if d["side"] == "DS" else "Light"
    groups = collections.OrderedDict(); cards = []; shields = []; unres = 0
    def add(line, is_shield):
        global unres
        name = (line.get("card") or "").strip()
        info = resolve_line(name, line.get("v"), side, line.get("ep1"), is_shield, ev.get("era", ""))
        tx = re.sub(r"\s*\((?:v|V)\)\s*$", "", (line.get("text") or "")).strip()
        if info is None and not name and len(tx) > 5 and not re.search(r"eject|cyborg", tx, re.I):
            info = norm_resolve(tx, line.get("v"), side, line.get("ep1"), is_shield, ev.get("era") == "original")  # exact title, ignoring punctuation only
        if info is None:
            key = ("Not identified", "TEXT:" + (line.get("text") or name or "?"))
            report.append(f"UNRESOLVED {d['title']} line {line.get('n')}: text={line.get('text')!r} card={name!r}")
        else:
            typ = "Defensive Shield" if is_shield and info["type"] == "Defensive Shield" else norm_type(info["type"])
            key = (typ, info["title"])
            (shields if typ == "Defensive Shield" else cards).append((name, "(V)" in info["title"]))
        groups.setdefault(key[0], collections.OrderedDict())
        g = groups[key[0]]; g[key[1]] = (g.get(key[1], (0, info))[0] + 1, info)
    lines = d["lines"] + [dict(x, n="A") for x in d.get("additional", []) if isinstance(x, dict)]
    for l in lines: add(l, False)
    for l in d.get("shields", []): add(l, True)
    def col(hs):
        out = []
        for h in hs:
            if h not in groups: continue
            out.append(f"'''{h}'''")
            for k, (q, info) in groups[h].items():
                pre = f"{q}x " if q > 1 else ""
                out.append("* " + pre + (cardlink(info) if info else esc(k[5:])))
            out.append("")
        return "\n".join(out).rstrip("\n")
    intro = ""
    if d.get("_day1"):
        t1 = d["_day1"]["title"]
        ch = "; ".join(esc(x) for x in d["_applied"])
        intro = (f"The sheet says the deck is the same as the player's [[{t1}|list from the day before]]"
                 + (f", with these changes: {ch}. The list below applies them.\n\n" if ch else ". The list below is that list.\n\n"))
    elif d.get("_nosrc"):
        intro = "The sheet says the deck is the same as the day before, but that list is not in the PDF. Only what the sheet itself lists is below.\n\n"
    if "Not identified" in groups:
        intro += "Lines the transcription could not identify are printed as written under '''Not identified'''.\n\n"
    body = (intro + '{| class="wikitable" style="width:100%;"\n|-\n| style="width:50%; vertical-align:top;" |\n'
            + col(LEFT) + '\n| style="width:50%; vertical-align:top;" |\n' + col(RIGHT) + "\n|}\n")
    sidew = "Dark Side" if d["side"] == "DS" else "Light Side"
    stage_txt = ev.get("stage") or ev.get("stage_label", "")
    info_lines = []
    if d["_start"] and not d.get("_start_from_loc"): info_lines.append("* '''Starting Card:''' " + cardlink(d["_start"]))
    elif d.get("start"): info_lines.append("* '''Starting Card:''' " + esc(d["start"]))
    nw = (d.get("name_written") or "").strip()
    if nw and re.sub(r"[^a-z]", "", nw.lower()) != re.sub(r"[^a-z]", "", d["player"].lower()):
        info_lines.append("* '''Name on sheet:''' " + esc(nw))
    if d.get("deck_name"): info_lines.append("* '''Deck name:''' " + esc(d["deck_name"]))
    if d.get("username"): info_lines.append("* '''Username:''' " + esc(d["username"]))
    info_lines.append(f"* '''Format:''' [[{ev['format']}]]")
    if stage_txt: info_lines.append(f"* '''Stage:''' {stage_txt}")
    pages = d["pages"]
    pg = f"Page {pages[0]}" if len(pages) == 1 else f"Pages {pages[0]}–{pages[-1]}"
    scanfile = f"{ev['hub']}{(' ' + ev['title_stage']) if ev.get('title_stage') else ''} {d['player']} {d['side']}.png"
    if scanfile in SEEN_SCAN: scanfile = scanfile[:-4] + f" (page {pages[0]}).png"
    SEEN_SCAN.add(scanfile)
    d["_scan"] = scanfile
    src_lines = "\n".join(f"* [{u} {esc(lab)}]" for u, lab in ev["sources"])
    stage_paren = f" ({stage_txt})" if stage_txt else ""
    text = f"""'''{d['title']}''' was the {sidew} constructed list played by [[{d['player']}]] at [[{ev['hub']}]]{stage_paren}.

== Deck info ==

{chr(10).join(info_lines)}

== Decklist ==

{body}

== Scan ==

{{| style="margin:0 auto;border:0;border-collapse:collapse;background:transparent"
|-
| style="vertical-align:top;border:0;padding:0" | [[File:{scanfile}|800px]]
| style="vertical-align:top;border:0;padding:0 0 0 0.2em;line-height:1" | <ref>{pg} of [[:File:{ev['pdf_file']}]].</ref>
|}}


== See also ==

* [[{ev['hub']}]]
* [[{d['player']}]]
* [[List of SWCCG tournaments]]

== Sources ==

{src_lines}

{{{{#if:1|<nowiki />
<h2>References</h2>
<references />}}}}

[[Category:Decklists]]
[[Category:{ev['iso'][:4]}]]
"""
    fn = re.sub(r"[^\w.-]+", "_", d["title"]) + ".wiki"
    (final / "pages" / fn).write_text(text, encoding="utf-8")
    d["_fn"] = fn
    canon.append({"title": d["title"], "player": d["player"], "side": d["side"], "event": ev["hub"],
                  "stage": ev.get("stage", ""), "cards": [[1, n, v] for n, v in cards],
                  "shields": [[1, n, v] for n, v in shields], "pdf": d["pdf"], "pages": d["pages"], "scan": scanfile})
json.dump(canon, open(final / "decks-canon.json", "w"), indent=1, ensure_ascii=False)
json.dump([{k: v for k, v in d.items() if not k.startswith("_") or k in ("_fn", "_scan", "_deckname")} for d in decks],
          open(final / "decks-built.json", "w"), indent=1, ensure_ascii=False)
(final / "report.txt").write_text("\n".join(report) + "\n", encoding="utf-8")
print(len(decks), "decks;", sum(r.startswith("UNRESOLVED") for r in report), "unresolved;",
      sum(not r.startswith("UNRESOLVED") for r in report), "other report lines")
