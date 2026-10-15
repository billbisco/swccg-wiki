#!/usr/bin/env python3
"""Match parsed PC posts to existing stub pages.  python3 match.py <parsed.json> <stubs.json> <decks_out.json>"""
import json, re, sys, unicodedata
from collections import defaultdict

EVENTS = [("2015-worlds-", "2015 World Championship"), ("2015-mpc-", "2015 Match Play Championship"),
          ("2015-san-diego-grand-prix-", "2015 San Diego Grand Prix"),
          ("2016-world-championships-", "2016 World Championship"), ("2016-mpc-", "2016 Match Play Championship"),
          ("2016-endor-grand-prix-", "2016 Endor Grand Prix"), ("2015-texas-mini-worlds-", "2015 Texas Mini Worlds"),
          ("2017-us-nationals-", "2017 U.S. National Championship"),
          ("2016-european-championships-", "2016 European Championship"),
          ("2016-texas-mini-worlds-", "2016 Texas Mini Worlds")]


def norm(s):
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z]+", " ", s).strip()


posts = json.load(open(sys.argv[1]))
import os
SLUGEV = json.load(open(os.environ["SLUG_EVENT"])) if os.environ.get("SLUG_EVENT") else {}  # slug -> event (wave 3: per-event folders)
_DB = json.load(open("/home/claude/swccg-gemp/src/gemp-swccg-cards/src/main/resources/card_blueprint_database.json"))
_SIDE = {}
for _r in _DB:
    _SIDE.setdefault(norm(_r["title"]), set()).add(_r.get("side"))


def infer_side(p):
    dk = lt = 0
    for _q, n, _v in p["cards"] + p["shields"]:
        sides = _SIDE.get(norm(re.sub(r"\s*\(v\)\s*$", "", n, flags=re.I)), set())
        if sides == {"DARK"}: dk += 1
        elif sides == {"LIGHT"}: lt += 1
    return "DS" if dk > lt * 2 else "LS" if lt > dk * 2 else None
ALIAS = {'charles-alderson': 'charles-arlandson', 'grand-prix-harpster': 'grand-prix-steve-harpster', 'barry-apelstien': 'barry-alperstein', 'jon-bauer': 'jonathan-bauer'}
for _p in posts:
    _p['slug_m'] = _p['slug']
    for a, b in ALIAS.items():
        _p['slug_m'] = _p['slug_m'].replace(a, b)
stubs = json.load(open(sys.argv[2]))
by_key = defaultdict(list)
for s in stubs:
    by_key[(s["event"], s["side"])].append(s)

out, unmatched, used = [], [], set()
queue = list(posts)
for PASS in (1, 2):
  todo, queue = queue, []
  for p in todo:
    ev = SLUGEV.get(p["slug"]) or next((e for pre, e in EVENTS if p["slug"].startswith(pre)), None)
    side = p["side"] or ("DS" if re.search(r"-ds(-|$)", p["slug"]) else "LS" if re.search(r"-ls(-|$)", p["slug"]) else None) or infer_side(p)
    slug = norm(p.get("slug_m", p["slug"]).replace("-", " "))
    _d = re.search(r"day-(\d)", p["slug"])
    stage = f"Day {_d.group(1)}" if _d else None
    cands = []
    for s in by_key.get((ev, side), []):
        if s["title"] in used:
            continue
        pn = norm(s["player"])
        if pn and (f" {pn} " in f" {slug} " or f" {pn} " in f" {norm(p['post_title'])} "):
            if stage and (s["stage"] or s.get("stage_line")) and (s["stage"] or s.get("stage_line")) != stage:
                continue
            cands.append(s)
    if len(cands) > 1:  # same player twice (e.g. Day 2 and Day 3 or Top 4): prefer stage match / objective words
        st = [c for c in cands if stage and c["stage"] == stage] or cands
        words = set(norm(p["slug"]).split())
        st.sort(key=lambda c: -len(words & set(norm(c["title"]).split())))
        cands = st[:1]
    if not cands and PASS == 1:
        queue.append(p); continue
    if not cands:  # fuzzy: spelling variants (Bolletino/Bollentino, Aesen/Aasen, Caldred/Cal Aldred)
        import difflib
        toks = norm(p["slug"].replace("-", " ") + " " + p["post_title"]).split()
        sides = [side] if side else ["DS", "LS"]
        best = []
        for sd in sides:
            for s2 in by_key.get((ev, sd), []):
                if s2["title"] in used or (stage and (s2["stage"] or s2.get("stage_line")) and (s2["stage"] or s2.get("stage_line")) != stage):
                    continue
                nt = norm(s2["player"]).split()
                if not nt:
                    continue
                last = max(difflib.SequenceMatcher(None, nt[-1], t).ratio() for t in toks)
                first = max(difflib.SequenceMatcher(None, nt[0], t).ratio() for t in toks)
                joined = max(difflib.SequenceMatcher(None, "".join(nt), "".join(toks[i:i+k])).ratio()
                             for k in (1, 2, 3) for i in range(len(toks)))
                if last < 0.75 and joined < 0.85:
                    continue
                best.append((max(min(last, first) * 0.5 + last * 0.5, joined), sd, s2))
        best.sort(key=lambda b: -b[0])
        if best and best[0][0] >= 0.8 and (len(best) == 1 or best[0][0] - best[1][0] >= 0.08):
            sc, sd, s2 = best[0]
            if not side:
                words = set(norm(p["slug"]).split())
                if len([b for b in best[:3] if b[2]["player"] == s2["player"]]) > 1:  # both sides of same player
                    pick = max([b for b in best if b[2]["player"] == s2["player"]],
                               key=lambda b: len(words & set(norm(b[2]["title"]).split())))
                    sc, sd, s2 = pick
                side = sd
            cands = [s2]
            print("  FUZZY", p["slug"], "->", s2["title"], round(sc, 2))
    if not cands:
        unmatched.append((p["slug"], ev, side)); continue
    s = cands[0]; used.add(s["title"])
    st_cards = p.get("starting") or []
    start = next((c[1] for c in st_cards if " / " in c[1]), "")
    if not start:
        lab = norm(re.sub(r"\s*\(V\)\s*$", "", s["title"].split(f" {side} ", 1)[-1]))
        start = next((c[1] for c in st_cards if norm(c[1]).startswith(lab) or lab.startswith(norm(c[1]))), "")
    if not start:
        start = next((c[1] for c in st_cards if norm(c[1]) not in ("knowledge and defense", "anger fear aggression")), "")
    out.append(dict(title=s["title"], player=s["player"], side=side, event=ev, stage=s.get("stage_line") or s["stage"] or "Day 1",
                    format_link=s["fmt"] or "[[Open]]", start=start, cards=p["cards"], shields=p["shields"],
                    url=p["url"], wayback=p["wayback"], post_title=p["post_title"], slug=p["slug"]))
json.dump(out, open(sys.argv[3], "w"), ensure_ascii=False, indent=0)
left = [s["title"] for s in stubs if s["title"] not in used]
print("matched", len(out), "unmatched posts", len(unmatched), "stubs without post", len(left))
for u in unmatched: print("  POST?", u)
for t in left[:40]: print("  STUB?", t)
