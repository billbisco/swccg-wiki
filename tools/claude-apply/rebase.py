#!/usr/bin/env python3
"""rebase.py OUTDIR GROUPDIR...  : for every editconflict row in GROUPDIR/applied.jsonl (not later done),
3-way merge (base revision -> draft) onto the live text with git merge-file. Clean merges go to OUTDIR
(apply.tsv, base_revids.json = live revid, .wiki); conflicts are listed in OUTDIR/unmerged.tsv."""
import json, os, subprocess, sys, tempfile, urllib.parse, urllib.request
API = "https://swccg.com/wiki/api.php"
def q(**p):
    p.update(format="json", formatversion=2)
    return json.load(urllib.request.urlopen(urllib.request.Request(API, urllib.parse.urlencode(p).encode()), timeout=120))
out = sys.argv[1]; os.makedirs(out, exist_ok=True)
rows, base, bad = [], {}, []
for g in sys.argv[2:]:
    b = json.load(open(os.path.join(g, "base_revids.json")))
    files = dict(l.rstrip("\n").split("\t")[:2] for l in open(os.path.join(g, "apply.tsv")) if l.strip())
    res = {}
    for l in open(os.path.join(g, "applied.jsonl")):
        j = json.loads(l); res[j["title"]] = j["result"]
    for t, r in res.items():
        if not r.startswith("ERROR editconflict"): continue
        draft = open(os.path.join(g, os.path.basename(files[t])), encoding="utf-8").read()
        old = q(action="query", revids=str(b[t]), prop="revisions", rvprop="content", rvslots="main")["query"]["pages"][0]["revisions"][0]["slots"]["main"]["content"]
        lp = q(action="query", titles=t, prop="revisions", rvprop="content|ids", rvslots="main")["query"]["pages"][0]["revisions"][0]
        live, lrev = lp["slots"]["main"]["content"], lp["revid"]
        with tempfile.TemporaryDirectory() as td:
            for n, s in (("live", live), ("old", old), ("draft", draft)):
                open(os.path.join(td, n), "w", encoding="utf-8").write(s if s.endswith("\n") else s + "\n")
            rc = subprocess.run(["git", "merge-file", "-p", os.path.join(td, "live"), os.path.join(td, "old"), os.path.join(td, "draft")], capture_output=True, text=True)
        if rc.returncode != 0:
            bad.append((t, g)); continue
        m = rc.stdout
        if not live.endswith("\n") and m.endswith("\n"): m = m[:-1]
        fn = t.replace("/", "%2F") + ".wiki"
        open(os.path.join(out, fn), "w", encoding="utf-8").write(m)
        rows.append((t, fn)); base[t] = lrev
open(os.path.join(out, "apply.tsv"), "w").write("".join(f"{t}\t{f}\n" for t, f in rows))
json.dump(base, open(os.path.join(out, "base_revids.json"), "w"))
open(os.path.join(out, "unmerged.tsv"), "w").write("".join(f"{t}\t{g}\n" for t, g in bad))
print("merged", len(rows), "unmerged", len(bad))
