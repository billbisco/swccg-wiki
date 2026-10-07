#!/bin/bash
# Apply Main Page empty-cell / Cancelled Expansions + mobile Common.css fixes.
# Does NOT touch Set-VB* art or V16/V27 crops. Never prints /opt/swccg-wiki/.env
set -euo pipefail
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
curl -sL "https://wiki.swccg.com/wiki/Main_Page?action=raw" | head -n 80 | tee /tmp/main-page-raw-check.txt
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