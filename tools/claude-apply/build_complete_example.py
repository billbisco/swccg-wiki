"""#1347 navigator drafts (navgen render_template/member_edit reused verbatim)."""
import sys, json, os, re, collections
sys.path.insert(0, "/home/claude/navgen"); import navgen
C = navgen.load_census_module("/home/claude/census1325")
OUT = "/home/claude/r1347"
VO3 = "(Virtual Set 3: Revolution)"
# (template name, existing?, [(title, label, edition-override or None)]) ; order = render order
F = collections.OrderedDict()
ESB = "The Empire Strikes Back Introductory Two-Player Game"
F["Chewie [Light character]"] = ("Chewie", True, [
    ("Chewie", "Original", None), ("Chewie (Japanese ESB Two-Player)", "Japanese", ESB),
    ("Chewie (V) (Virtual Set 10: Fourth Anthology) (Original 2005)", "Original (2005)", None),
    ("Chewie (V) (Virtual Set 10: Fourth Anthology) (Original)", "Remastered (2006)", None),
    ("Chewie (V) (Virtual Block 2)", "Original", None),
    ("Chewie (V)", "Original", None), ("Chewie (V) (Errata)", "Errata", None)])
F["Dark Forces [Dark effect]"] = ("Dark Forces", True, [
    ("Dark Forces", "Original", None),
    (f"Dark Forces (V) {VO3} (Original)", "Original", None), (f"Dark Forces (V) {VO3} (Remastered 2006)", "Remastered (2006)", None),
    ("Dark Forces (V)", "Original", None)])
F["Faithful Service [Light effect]"] = ("Faithful Service", True, [
    ("Faithful Service", "Original", None),
    ("Faithful Service (V) (Virtual Set 12: Martyrs & Magistrates) (Original)", "Original", None),
    ("Faithful Service (V)", "Original", None), ("Faithful Service (V) (Errata)", "Errata", None),
    ("Faithful Service (V) (Errata 2)", "Errata 2", None), ("Faithful Service (V) (Errata 3)", "Errata 3", None)])
F["For Luck [Light effect]"] = ("For Luck", True, [
    ("For Luck", "Original", None), ("For Luck (Errata)", "Decipher Errata", None),
    (f"For Luck (V) {VO3} (Original)", "Original", None), (f"For Luck (V) {VO3} (Remastered 2006)", "Remastered (2006)", None),
    ("For Luck (V) (Virtual Block 1)", "Original", None),
    ("For Luck (V)", "Original", None), ("For Luck (V) (Errata)", "Errata", None)])
F["Forced Servitude [Dark effect]"] = ("Forced Servitude", True, [
    ("Forced Servitude", "Original", None),
    ("Forced Servitude (V) (Virtual Set 12: Martyrs & Magistrates) (Original)", "Original", None),
    ("Forced Servitude (V)", "Original", None), ("Forced Servitude (V) (Errata)", "Errata", None),
    ("Forced Servitude (V) (Errata 2)", "Errata 2", None), ("Forced Servitude (V) (Errata 3)", "Errata 3", None)])
F["Han [Light character]"] = ("Han", True, [
    ("Han", "Original", None),
    (f"Han (V) {VO3} (Original)", "Original", None), (f"Han (V) {VO3} (Remastered 2006)", "Remastered (2006)", None),
    ("Han (V) (Virtual Block 3)", "Original", None),
    ("Han (V)", "Original", None), ("Han (V) (Errata)", "Errata", None)])
F["Motti [Dark character]"] = ("Motti", True, [
    ("Motti", "Original", None),
    (f"Motti (V) {VO3} (Original)", "Original", None), (f"Motti (V) {VO3} (Remastered 2006)", "Remastered (2006)", None)])
F["Veers [Dark character]"] = ("Veers", True, [
    ("Veers", "Original", None), ("Veers (Japanese ESB Two-Player)", "Japanese", ESB),
    ("Veers (V) (Virtual Set 10: Fourth Anthology) (Original)", "Original", None),
    ("Veers (V) (Virtual Block 2)", "Original", None),
    ("Veers (V)", "Original", None), ("Veers (V) (Errata)", "Errata", None),
    ("Veers (V) (Errata 2)", "Errata 2", None), ("Veers (V) (Errata 3)", "Errata 3", None)])
F["Eriadu [Dark location]"] = ("Eriadu (Jedi Pack)", False, [("Eriadu", "Original", None), ("Eriadu (V)", "Original", None)])
F["Hoth: Mountains (6th Marker) [Dark location]"] = ("Hoth: Mountains (6th Marker) (%s)" % ESB, False, [
    ("Hoth: Mountains (6th Marker)", "Original", None), ("Hoth: Mountains (6th Marker) (Japanese ESB Two-Player)", "Japanese", ESB)])
F["Hyperoute Navigation Chart [Dark game aid]"] = ("Hyperoute Navigation Chart (Jedi Pack)", False, [
    ("Hyperoute Navigation Chart", "Original", None), ("Hyperoute Navigation Chart (V)", "Original", None)])
O = "Obsidian Squadron TIE"
F["Obsidian Squadron TIE [Dark starship]"] = (O + " (Official Tournament Sealed Deck)", False,
    [(O, "Original", None)] + [(f"{O} ({q})", q, None) for q in ["Decipher Errata 1998", "PC Errata 2013 slip",
     "PC Errata 2017 slip", "PC Errata 2018 E card", "PC Errata 2019 disc card", "PC 2025 D-E1 card"]])
for n, s in [("Rebel Trooper Recruit", "Light character"), ("Stormtrooper Cadet", "Dark character")]:
    F[f"{n} [{s}]"] = (n + " (Official Tournament Sealed Deck)", False,
        [(n, "Original", None), (f"{n} (PC Errata 2017 slip)", "PC Errata 2017 slip", None),
         (f"{n} (PC Errata 2018 E card)", "PC Errata 2018 E card", None)])
F["Tarkin's Orders [Dark interrupt]"] = ("Tarkin's Orders (Official Tournament Sealed Deck)", False, [
    ("Tarkin's Orders", "Original", None), ("Tarkin's Orders (V)", "Original", None)])

if __name__ == "__main__":
    allm = sorted({m for v in F.values() for m, _, _ in v[2]})
    tnames = ["Template:Card versions/" + v[0] for v in F.values()]
    live = navgen.live_pages(allm + tnames)
    json.dump(live, open("build_live.json", "w"))
    eds = set()
    for m in allm:
        assert not live[m]["missing"] and not live[m]["redirect"], m
    drafts = collections.OrderedDict(); rows = []; seen = set(); noop = []
    for fam, (tname, exists, order) in F.items():
        tfull = "Template:Card versions/" + tname
        assert live[tfull]["missing"] != exists, (tfull, exists)
        by_era = collections.OrderedDict(); keys = set(); fr = []
        for m, lab, edo in order:
            assert m not in seen, m; seen.add(m)
            tx = live[m]["text"]; inf = C.parse_infobox(tx)
            era = C.era_of(inf, m); ed = edo or C.strip_markup(inf.get("set") or "")
            assert era in navgen.ERA_ORDER, (m, era)
            keys.add((C.norm_side(inf.get("side", "")), C.norm_type(inf.get("type", ""))))
            by_era.setdefault(era, []).append(dict(title=m, label=lab, edition=ed))
            fr.append((m, lab, ed, era))
        assert len(keys) == 1, (fam, keys)
        eds |= {e for _, _, e, _ in fr}
        drafts[tfull] = (navgen.render_template(tname, by_era), live[tfull]["revid"])
        for m, _, _, _ in fr:
            nt, why = navgen.member_edit(live[m]["text"], tname)
            assert nt is not None, (m, why)
            if nt == live[m]["text"]:
                noop.append(m); continue
            drafts[m] = (nt, live[m]["revid"])
        rows.append((fam, tfull, "existing" if exists else "new", fr))
    res = navgen.live_resolve(sorted(eds))
    for e in eds: assert res[e][0], ("edition", e)
    for f in os.listdir(OUT):
        if f.endswith(".wiki"): os.remove(os.path.join(OUT, f))
    base = {}; ap = []
    for t in sorted(drafts, key=lambda x: (not x.startswith("Template:"), x)):
        tx, rev = drafts[t]
        open(os.path.join(OUT, navgen.fname(t)), "w").write(tx)
        ap.append(f"{t}\tdrafts/r1347/{navgen.fname(t)}"); base[t] = rev
    open(os.path.join(OUT, "apply.tsv"), "w").write("\n".join(ap) + "\n")
    json.dump(base, open(os.path.join(OUT, "base_revids.json"), "w"), ensure_ascii=False, indent=1)
    json.dump(rows, open("rows.json", "w"), indent=1)
    print(len(drafts), "drafts;", len(rows), "families; unchanged members:", noop)
