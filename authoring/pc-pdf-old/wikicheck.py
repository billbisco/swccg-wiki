"""wikicheck.py "<card name>" DS|LS : list wiki card pages whose title starts with the name (side, type, image)."""
import sys, json, urllib.request, urllib.parse
API = "https://wiki.swccg.com/api.php"
def q(p):
    p.update(format="json", formatversion=2)
    return json.load(urllib.request.urlopen(urllib.request.Request(API, data=urllib.parse.urlencode(p).encode()), timeout=60))
name, side = sys.argv[1], {"DS": "Dark", "LS": "Light"}.get(sys.argv[2].upper(), sys.argv[2]) if len(sys.argv) > 2 else ""
ts = [p["title"] for p in q(dict(action="query", list="prefixsearch", pssearch=name, pslimit=25))["query"]["prefixsearch"]]
if not ts:
    ts = [p["title"] for p in q(dict(action="query", list="search", srsearch=name, srwhat="title", srlimit=15))["query"]["search"]]
r = q(dict(action="query", titles="|".join(ts[:50]), prop="revisions", rvprop="content", rvslots="main", redirects=1))
import re
for p in r["query"]["pages"]:
    t = p["revisions"][0]["slots"]["main"]["content"] if p.get("revisions") else ""
    g = lambda f: (re.search(r"\|\s*" + f + r"\s*=\s*([^\n|]*)", t) or [None, ""])[1].strip()
    if "{{Card" not in t: continue
    s = g("side")
    if side and s != side: continue
    print(f"{p['title']}\t{s}\t{g('type')}\t{g('image')}")
