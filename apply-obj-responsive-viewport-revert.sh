#!/bin/bash
# REVERT site-wide device-width viewport; KEEP card-device-narrow Objective stack.
# Never prints /opt/swccg-wiki/.env
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

CSS="$PAGES/MediaWiki_Common.css.wiki"
JS="$PAGES/MediaWiki_Common.js.wiki"
test -s "$CSS"
test -s "$JS"
test -s "$ROOT/SwccgChrome.php"
test -s "$ROOT/extra-settings.php"

# Must NOT force device-width anymore
if grep -q 'onOutputPageAfterGetHeadLinksArray' "$ROOT/SwccgChrome.php"; then
  echo "FAIL: SwccgChrome still has OutputPageAfterGetHeadLinksArray" >&2
  exit 1
fi
if grep -q 'onOutputPageAfterGetHeadLinksArray' "$ROOT/extra-settings.php"; then
  echo "FAIL: extra-settings still registers viewport rewrite hook" >&2
  exit 1
fi
if grep -q 'wgVectorResponsive' "$ROOT/extra-settings.php"; then
  echo "FAIL: extra-settings still has wgVectorResponsive" >&2
  exit 1
fi
# Must KEEP dual-portrait phone stack path
grep -q 'card-device-narrow' "$CSS"
grep -q 'card-device-narrow' "$JS"
grep -q 'screen.width' "$JS"

echo "== revert Vector legacy skin.json responsive:true -> false =="
docker exec -i swccg_wiki python3 - <<'PY'
from pathlib import Path
import re
p = Path("/var/www/html/skins/Vector/skin.json")
t = p.read_text()
# Count before
print("before false=", t.count('"responsive": false'), "true=", t.count('"responsive": true'))
# Legacy vector skin should be responsive:false. Prior fix flipped the only false->true.
# Vector-2022 already has true. We need exactly one false for legacy.
# Strategy: find the legacy "name": "vector" block and ensure its responsive is false.
# Simpler reliable approach used previously: the FIRST '"responsive": true' after patch
# that replaced the only false — but now we may have two trues.
# Safest: locate '"name": "vector"' (legacy, not vector-2022) and set responsive false nearby.

idx = t.find('"name": "vector"')
if idx < 0:
    raise SystemExit("vector skin name not found")
# Prefer the bare "vector" skin entry; vector-2022 is '"name": "vector-2022"'
# find('"name": "vector"') may hit vector-2022 first if that string is a prefix... 
# '"name": "vector"' is NOT a prefix of vector-2022 because of the closing quote.
# Actually '"name": "vector"' appears ONLY for legacy; vector-2022 has longer name.

# Within ~800 chars after name, set responsive false if currently true
chunk = t[idx:idx+1200]
m = re.search(r'"responsive":\s*(true|false)', chunk)
if not m:
    raise SystemExit("responsive key not found near legacy vector name")
print("legacy responsive currently:", m.group(1))
if m.group(1) == "true":
    abs_start = idx + m.start()
    abs_end = idx + m.end()
    t = t[:abs_start] + '"responsive": false' + t[abs_end:]
    p.write_text(t)
    print("patched legacy responsive -> false")
else:
    print("already false; no change")
t2 = p.read_text()
print("after false=", t2.count('"responsive": false'), "true=", t2.count('"responsive": true'))
# Sanity: must have at least one false
if t2.count('"responsive": false') < 1:
    raise SystemExit("expected at least one responsive:false after revert")
PY

echo "== edit MediaWiki:Common.css (keep card-device-narrow) =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="revert viewport: keep card-device-narrow Objective stack; no site-wide device-width" \
  "MediaWiki:Common.css" < "$CSS"

echo "== edit MediaWiki:Common.js (keep screen.width path) =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="revert viewport: keep html.card-device-narrow from screen.width; chrome restored via width=1120" \
  "MediaWiki:Common.js" < "$JS"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

echo "== purge key pages =="
printf '%s\n' \
  'MediaWiki:Common.css' \
  'MediaWiki:Common.js' \
  'Main Page' \
  'HoloNet Transmission' \
  'Set Your Course For Alderaan / The Ultimate Power In The Universe' \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true

echo "== bump wgCacheEpoch =="
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import re
p = Path("/opt/swccg-wiki/extra-settings.php")
t = p.read_text()
new = datetime.now(timezone.utc).strftime("%Y%m%d%H%M%S")
pat = re.compile(r"\$wgCacheEpoch\s*=\s*'[^']*';")
if not pat.search(t):
    raise SystemExit("no wgCacheEpoch")
p.write_text(pat.sub(f"$wgCacheEpoch = '{new}';", t, count=1))
print(f"epoch bumped to {new}")
PY

echo "== restart wiki (pick up SwccgChrome/extra-settings + skin.json) =="
docker compose -f docker-compose.yml -f docker-compose.localsettings.yml restart wiki
sleep 12

echo "== apply-obj-responsive-viewport-revert done =="
