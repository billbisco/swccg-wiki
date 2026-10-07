#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

echo "== Template:Card image2_layout=right (side-by-side) =="
edit "Template:Card" "$PAGES/Template_Card.wiki" \
  "Optional |image2_layout=right side-by-side portraits; omit/stack = stacked (default)"

echo "== MediaWiki:Common.css card-portraits-row + card-rail-dual =="
edit "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki" \
  "card-portraits-row flex side-by-side; card-rail-dual 580px for Objective sample"

echo "== SYCFA sample: image2_layout=right =="
edit "Set Your Course For Alderaan / The Ultimate Power In The Universe" \
  "$PAGES/Set_Your_Course_For_Alderaan___The_Ultimate_Power_In_The_Universe.wiki" \
  "Sample: |image2_layout=right — 0 left, 7 right in portrait rail"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

purge "Template:Card"
purge "MediaWiki:Common.css"
purge "Set Your Course For Alderaan / The Ultimate Power In The Universe"
purge "HoloNet Transmission"
purge "Attack Run"

echo "== bump \$wgCacheEpoch + restart wiki (CSS) =="
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

echo "== DONE obj-sidebyside-sample =="