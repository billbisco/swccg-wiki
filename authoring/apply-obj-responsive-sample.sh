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

echo "== Template:Card image2_layout=responsive =="
edit "Template:Card" "$PAGES/Template_Card.wiki" \
  "Optional |image2_layout=responsive (wide side-by-side / narrow stack); keep right=force-side, stack=force-stack"

echo "== MediaWiki:Common.css responsive dual portraits @720px =="
edit "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki" \
  "card-rail-responsive / card-portraits-responsive: max-width 720px stacks dual Objective portraits"

echo "== SYCFA sample: image2_layout=responsive =="
edit "Set Your Course For Alderaan / The Ultimate Power In The Universe" \
  "$PAGES/Set_Your_Course_For_Alderaan___The_Ultimate_Power_In_The_Universe.wiki" \
  "Sample: |image2_layout=responsive — wide 0|7 side-by-side, narrow stacked"

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

echo "== bump \$wgCacheEpoch + restart wiki (CSS / site.styles) =="
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
sleep 6

echo "== DONE obj-responsive-sample =="
