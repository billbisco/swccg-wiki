#!/bin/bash
set -euo pipefail
# Current wikitext via api.php (anonymous index.php?action=raw is rate-limited by nginx: 429).
# Prints nothing for a missing page, as `curl ...?action=raw` did. Title may use _ or %-escapes.
wiki_raw() {
  python3 -c '
import json, sys, time, urllib.error, urllib.parse, urllib.request
t = urllib.parse.unquote(sys.argv[1]).replace("_", " ")
u = "https://wiki.swccg.com/api.php?" + urllib.parse.urlencode({"action": "query", "prop": "revisions", "rvprop": "content", "rvslots": "main", "titles": t, "format": "json", "formatversion": "2"})
ua = "SWCCGWikiTools/1.0 (https://wiki.swccg.com/wiki/User:Comlink_Cursor; wikitext reader)"
for i in range(7):
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": ua}), timeout=60))
        break
    except urllib.error.HTTPError as e:
        if e.code not in (429, 502, 503, 504) or i == 6:
            raise
        ra = (e.headers.get("Retry-After") or "").strip()
        time.sleep(float(ra) if ra.isdigit() else min(2 * 2 ** i, 60))
p = (d.get("query") or {}).get("pages", [{}])[0]
if p.get("revisions"):
    sys.stdout.write(p["revisions"][0]["slots"]["main"].get("content", ""))
' "$1"
}
echo "== LS =="
wiki_raw "2013_Worlds_Day_3_Justin_Desai_LS_It_Is_The_Future_You_See_(V)" | head -n 10
echo "== DS =="
wiki_raw "2013_Worlds_Day_3_Justin_Desai_DS_Imperial_Occupation" | head -n 10
echo "== HUB =="
wiki_raw "2013_World_Championship" | grep -n "Justin Desai" || true
echo "== PLAYER =="
wiki_raw "Justin_Desai" | grep "2013 World Championship" || true
echo QA-D3-DESAI-DONE
