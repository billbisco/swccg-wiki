#!/bin/bash
# Apply viewport fix: SwccgChrome rewrite + Vector skin.json + Common.css/js belt.
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
grep -q 'onOutputPageAfterGetHeadLinksArray' "$ROOT/SwccgChrome.php"
grep -q 'onOutputPageAfterGetHeadLinksArray' "$ROOT/extra-settings.php"
grep -q 'card-device-narrow' "$CSS"
grep -q 'card-device-narrow' "$JS"

echo "== patch Vector legacy skin.json responsive:false -> true =="
# Source fix: Skin::isResponsive() then emits device-width viewport itself.
# SwccgChrome hook still rewrites width=1120 if this patch is lost on recreate.
SKIN_JSON=/var/www/html/skins/Vector/skin.json
docker exec -i swccg_wiki python3 - <<'PY'
from pathlib import Path
import re
p = Path("/var/www/html/skins/Vector/skin.json")
t = p.read_text()
# Only flip the legacy "vector" skin block's responsive:false (first false after "name": "vector")
# Safer: replace the specific pattern that appears once for legacy.
old = '"name": "vector"'
idx = t.find(old)
if idx < 0:
    raise SystemExit("vector skin name not found")
# find responsive in the legacy args block (before next skin or end)
# The legacy block has '"responsive": false,' once.
# vector-2022 has '"responsive": true,' ? leave that alone.
count_false = t.count('"responsive": false')
count_true = t.count('"responsive": true')
print(f"before responsive false={count_false} true={count_true}")
if count_false == 0:
    print("already patched (no responsive false)")
else:
    # Replace only the first '"responsive": false' which is the legacy vector skin
    # (vector-2022 appears first in skin.json with true; legacy is the false one)
    t2, n = re.subn(r'"responsive":\s*false', '"responsive": true', t, count=1)
    if n != 1:
        raise SystemExit(f"expected 1 replacement, got {n}")
    p.write_text(t2)
    print("patched legacy responsive -> true")
print("after false=", p.read_text().count('"responsive": false'), "true=", p.read_text().count('"responsive": true'))
PY

echo "== edit MediaWiki:Common.css =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="viewport/phone: card-device-narrow belt for Objective responsive portraits" \
  "MediaWiki:Common.css" < "$CSS"

echo "== edit MediaWiki:Common.js =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="viewport/phone: toggle html.card-device-narrow from screen.width<=720" \
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

echo "== apply-obj-responsive-viewport done =="
