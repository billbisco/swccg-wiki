#!/usr/bin/env python3
"""Wave 6: split a build into batch A (named from the player's own page at the same event — safe to publish)
and batch B (event-sibling naming, other-event words in the slug, odd player names — needs review).

python3 split.py builddir outA planB.json
"""
import json, re, sys, shutil, pathlib

OTHER = ['retro', 'charity', 'league', 'jawa', 'gempc', 'ocs', 'sealed', 'draft', 'classic', 'legacy', 'cube']
b = pathlib.Path(sys.argv[1]); outA = pathlib.Path(sys.argv[2])
plan = json.load(open(b / "plan.json"))
evs = {l.split()[1].rstrip(":") for l in open(b / "report.txt") if l.startswith("EVENT-SIBLING")}


def fn(t): return re.sub(r"[^A-Za-z0-9 ._()-]", "_", t) + ".wiki"


A, B = [], []
for p in plan:
    if p["status"] != "built" or p["slug"] in evs:
        B.append(p); continue
    s = p["slug"].lower(); t = (p["sibling"] + " " + p["title"]).lower()
    if any(w in s and w not in t for w in OTHER) or re.search(r"\d|nats|nationals", p["player"] or "") or len((p["player"] or "").split()) < 2:
        B.append(p); continue
    A.append(p)
if outA.exists(): shutil.rmtree(outA)
(outA / "pages").mkdir(parents=True); (outA / "gemp").mkdir()
for p in A:
    shutil.copy(b / "pages" / fn(p["title"]), outA / "pages" / fn(p["title"]))
    if p.get("gemp"): shutil.copy(b / "gemp" / p["gemp"], outA / "gemp" / p["gemp"])
json.dump(A, open(outA / "plan.json", "w"), indent=1, ensure_ascii=False)
(outA / "apply.tsv").write_text("".join(f"{p['title']}\tpages/{fn(p['title'])}\n" for p in A), encoding="utf-8")
json.dump(B, open(sys.argv[3], "w"), indent=1, ensure_ascii=False)
print("A", len(A), "B", len(B))
