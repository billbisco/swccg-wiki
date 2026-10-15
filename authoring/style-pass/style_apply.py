#!/usr/bin/env python3
"""Apply style-pass drafts as Holocron Claude, skipping pages edited since the snapshot.

usage: style_apply.py manifest.json [--limit N]
manifest: [{title, ts (snapshot revision timestamp), text, talk (optional), summary}]
Progress is kept in done.json next to the manifest, so reruns skip finished titles.
"""
import json, os, sys, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wiki_api_apply import Wiki

man_path = sys.argv[1]
limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 10**9
deadline = time.time() + 150
man = json.load(open(man_path))
done_path = os.path.join(os.path.dirname(os.path.abspath(man_path)), "done.json")
done = json.load(open(done_path)) if os.path.exists(done_path) else {}
w = Wiki()
n = 0
for it in man:
    t = it["title"]
    if t in done or n >= limit or time.time() > deadline:
        continue
    r = w.get(action="query", titles=t, prop="revisions", rvprop="timestamp|user", rvslots="main")
    p = r["query"]["pages"][0]
    cur = p["revisions"][0]["timestamp"] if "revisions" in p else None
    if cur != it["ts"]:
        done[t] = f"SKIP changed since snapshot ({p['revisions'][0]['user'] if cur else 'missing'} {cur})"
    else:
        res = w.edit(t, it["text"], it["summary"])
        if it.get("talk"):
            tt = "Talk:" + t
            r2 = w.get(action="query", titles=tt, prop="revisions", rvprop="content", rvslots="main")
            p2 = r2["query"]["pages"][0]
            old = p2["revisions"][0]["slots"]["main"]["content"] if "revisions" in p2 else ""
            res += " | talk " + w.edit(tt, (old.rstrip() + "\n\n" if old.strip() else "") + it["talk"].strip() + "\n",
                                        "Style pass: moved notes and cuts from the article")
        done[t] = res
    n += 1
    json.dump(done, open(done_path, "w"), indent=0)
    print(t, "->", done[t], flush=True)
left = sum(1 for it in man if it["title"] not in done)
print("remaining", left)
