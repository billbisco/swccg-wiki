#!/usr/bin/env python3
"""Wave 6: render a PC per-deck post (raw HTML) into a wiki decklist table + facts.

Library used by build.py. Reuses parse_posts (post parsing), canon.py (name fixes) and pc-pdf-old/build.py
(card resolution + CardLink rendering), the same machinery as wave5/fill.py.
"""
import json, re, sys, pathlib, collections

HERE = pathlib.Path(__file__).resolve().parent
PCP = HERE.parent
AUTH = PCP.parent
sys.path.insert(0, str(PCP))
sys.path.insert(0, str(AUTH / "pc-pdf-scans"))
import parse_posts as P          # noqa: E402
import resolve_wiki as R         # noqa: E402

src = open(PCP / "canon.py").read().split("decks = json.load(open(sys.argv[1]))")[0]
src = src.replace("/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json",
                  str(AUTH / "gemp-data" / "card_blueprint_database.json"))
C = {"__file__": str(PCP / "canon.py")}
exec(compile(src, "canon", "exec"), C)

b = open(AUTH / "pc-pdf-old" / "build.py").read()
defs = b[b.index("LEFT = ["):b.index("# ---- load decks")]
B = {"R": R, "re": re, "json": json}
exec(compile(defs + "\n" + re.search(r"^def esc.*$", b, re.M).group(0), "build", "exec"), B)
LEFT, RIGHT, cardlink, esc, norm_type = B["LEFT"], B["RIGHT"], B["cardlink"], B["esc"], B["norm_type"]

EXTRA = {("DS", "endor landining platform"): "Endor: Landing Platform (Docking Bay)", ("DS", "endor bunker"): "Endor: Bunker",
         ("DS", "opressive"): "Oppressive Enforcement", ("DS", "ychf"): "You Cannot Hide Forever",
         ("DS", "ychf (v)"): "You Cannot Hide Forever (V)", ("DS", "dr evazan & ponda baba"): "Dr. Evazan & Ponda Baba",
         ("DS", "short-range fighters & watch your back!"): "Short Range Fighters & Watch Your Back!",
         ("LS", "boussh"): "Boushh", ("DS", "imbalance and kintan strider"): "Imbalance & Kintan Strider",
         ("LS", "obi-wan kenobi with lightsaber"): "Obi-Wan With Lightsaber", ("LS", "artoo detoo in red 5"): "Artoo-Detoo In Red 5",
         ("LS", "spaceport: docking bay"): "Spaceport Docking Bay", ("LS", "sense (premiere)"): "Sense (Light) (Premiere)"}


def render(html_path, sd):
    """sd = 'DS'|'LS'. Returns dict(body, total, shields, unresolved, objective, starting, titles, post_title, rep)."""
    f = pathlib.Path(html_path)
    d = P.parse(f)
    _t, lines = P.post_body(f.read_text(encoding="utf-8", errors="replace"))
    rep = []
    pre = []
    for l in lines:
        if P.HEAD.match(l) or re.match(r"^[\[{]\s*([A-Za-z' &/-]+?)\s*[\]}]\s*$", l) or \
                re.sub(r"\s*\([^)]*\)\s*$", "", l).strip().lower() in P.BARE_HEADS:
            break
        pre.append(l)
    tot0 = sum(c[0] for c in d["cards"])
    if pre and tot0 < 60 and len(pre) <= 12 and not any(
            re.search(r"\b20\d\d\b|\d(?:st|nd|rd|th) place|day \d|record", l, re.I) for l in pre):
        d["cards"] = [list(P.split_item(l)) for l in pre] + d["cards"]
        d["starting"] = [list(P.split_item(l)) for l in pre] + d.get("starting", [])
        rep.append(f"PRE-HEAD {len(pre)} unheaded opening lines taken as starting cards")
    side = "Dark" if sd == "DS" else "Light"
    if d["side"] and d["side"] != sd:
        rep.append(f"SIDE-WORD post title says {d['side']}")
    groups = collections.OrderedDict(); unres = []; unres_cards = []; resolved = {}

    def resolve(name, v, shield):
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
            j = R.resolve(re.sub(r"^(.*?)(?: / .*)? \((Virtual Block|Dark|Light)[^()]*\)$", r"\1", info["title"]),
                          "(V)" in info["title"], side)
            if j and not re.match(r"(VB|VSh|OVS)", j["image"]): info = j
        if info and v and "(V)" not in info["title"]:
            rep.append(f"V-LOST {name0} (V) -> {info['title']}")
        return info

    cardlist = []

    def add(q, name, v, shield):
        info = resolve(name, v, shield)
        cardlist.append((q, info["title"] if info else None, name, v, shield))
        if info is None:
            key = ("Defensive Shield" if shield else "Not identified", "TEXT:" + name + (" (V)" if v else ""))
            unres.append(name + (" (V)" if v else ""))
            if not shield: unres_cards.append(name)
        else:
            typ = "Defensive Shield" if shield and info["type"] == "Defensive Shield" else norm_type(info["type"])
            key = (typ, info["title"])
            resolved[(name, v)] = info
        g = groups.setdefault(key[0], collections.OrderedDict())
        g[key[1]] = (g.get(key[1], (0, info))[0] + q, info)

    for q, n, v in d["cards"]: add(q, n, v, False)
    for q, n, v in d["shields"]: add(q, n, v, True)
    total = sum(q for q, _n, _v in d["cards"])
    nsh = sum(q for q, _n, _v in d["shields"])
    if total != 60: rep.append(f"COUNT {total} cards + {nsh} shields")
    if unres: rep.append("UNRESOLVED " + "; ".join(unres))

    def col(hs):
        o = []
        for h in hs:
            if h not in groups: continue
            o.append(f"'''{h}'''")
            for k, (q, info) in groups[h].items():
                o.append("* " + (f"{q}x " if q > 1 else "") + (cardlink(info) if info else esc(k[5:])))
            o.append("")
        return "\n".join(o).rstrip("\n")
    intro = ("Cards the post names that could not be matched to a card page are printed as written under "
             "'''Not identified'''.\n\n") if unres_cards else ""
    body = (intro + '{| class="wikitable" style="width:100%;"\n|-\n| style="width:50%; vertical-align:top;" |\n'
            + col(LEFT) + '\n| style="width:50%; vertical-align:top;" |\n' + col(RIGHT) + "\n|}\n")
    objective = next((info for q, info in groups.get("Objective", {}).values() if info), None)
    start_int = None
    for q, n, v in d.get("starting", []):
        i = resolved.get((n, v))
        if i and norm_type(i["type"]) == "Interrupt":
            start_int = i; break
    start_loc = None
    for q, n, v in d.get("starting", []):
        i = resolved.get((n, v))
        if i and norm_type(i["type"]) == "Location":
            start_loc = i; break
    titles = collections.Counter()
    for h, g in groups.items():
        for k, (q, info) in g.items():
            if info and h != "Defensive Shield": titles[info["title"]] += q
    return dict(body=body, total=total, shields=nsh, unresolved=unres, objective=objective, start_int=start_int,
                titles=titles, post_title=d["post_title"], rep=rep, cardlist=cardlist, start_loc=start_loc)


if __name__ == "__main__":
    r = render(sys.argv[1], sys.argv[2])
    print(r["post_title"], r["total"], r["shields"], r["objective"] and r["objective"]["title"],
          r["start_int"] and r["start_int"]["title"]); print("\n".join(r["rep"])); print(r["body"][:1500])
