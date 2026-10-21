#!/bin/bash
# Apply Main Page empty-cell / Cancelled Expansions + mobile Common.css fixes.
# Does NOT touch Set-VB* art or V16/V27 crops. Never prints /opt/swccg-wiki/.env
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
        if e.code not in (429, 503) or i == 6:
            raise
        ra = (e.headers.get("Retry-After") or "").strip()
        time.sleep(float(ra) if ra.isdigit() else min(2 * 2 ** i, 60))
p = (d.get("query") or {}).get("pages", [{}])[0]
if p.get("revisions"):
    sys.stdout.write(p["revisions"][0]["slots"]["main"].get("content", ""))
' "$1"
}
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

MP="$PAGES/Main_Page.wiki"
CSS="$PAGES/MediaWiki_Common.css.wiki"
if [ ! -s "$MP" ] || [ ! -s "$CSS" ]; then
  echo "ERROR: missing Main_Page or Common.css source" >&2
  exit 1
fi

echo "== edit Main Page =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Main Page: single-cell header tables; Cancelled Expansions thumb right" \
  "Main Page" < "$MP"

echo "== edit MediaWiki:Common.css =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="mobile: static search/personal; Main Page wikitable fixed; mw-head clip" \
  "MediaWiki:Common.css" < "$CSS"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge Main Page + Common.css =="
printf '%s\n' \
  'Main Page' \
  'MediaWiki:Common.css' \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true

echo "== bump wgCacheEpoch + restart wiki =="
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import re
p = Path("/opt/swccg-wiki/extra-settings.php")
t = p.read_text()
new = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
pat = re.compile(r"\$wgCacheEpoch\s*=\s*'[^']*';")
if pat.search(t):
    p.write_text(pat.sub(f"$wgCacheEpoch = '{new}';", t, count=1))
    print(f"epoch bumped to {new}")
else:
    print("WARNING: $wgCacheEpoch line not found; skip bump")
PY

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d wiki
sleep 4

echo "== verify live raw =="
wiki_raw "Main_Page" | head -n 80 | tee /tmp/main-page-raw-check.txt
if grep -F "| '''[https://play.swccg.com/ Play Star Wars CCG online for free on GEMP]'''" /tmp/main-page-raw-check.txt; then
  echo "OK: GEMP single-cell line present"
else
  echo "WARN: expected GEMP single-cell line missing" >&2
fi
if grep -F 'link=Cancelled Expansions' /tmp/main-page-raw-check.txt; then
  echo "WARN: Cancelled Expansions still linked from file" >&2
else
  echo "OK: no link=Cancelled Expansions on ad"
fi
if grep -F 'thumb|right|280px' /tmp/main-page-raw-check.txt; then
  echo "OK: thumb|right present"
fi

echo "== apply-main-mobile done =="