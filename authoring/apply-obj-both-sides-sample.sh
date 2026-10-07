#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

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

echo "== Template:Card optional image2 (stacked portrait) =="
edit "Template:Card" "$PAGES/Template_Card.wiki" \
  "Optional |image2= second portrait stacked under |image= (Objectives 0/7); omit = unchanged"

echo "== SYCFA sample: add image2 7-side =="
edit "Set Your Course For Alderaan / The Ultimate Power In The Universe" \
  "$PAGES/Set_Your_Course_For_Alderaan___The_Ultimate_Power_In_The_Universe.wiki" \
  "Sample: show 7-side via |image2=TA-D-theultimatepowerintheuniverse.gif under 0-side portrait"

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
purge "Set Your Course For Alderaan / The Ultimate Power In The Universe"
# Spot-check singles still one portrait after template change
purge "HoloNet Transmission"
purge "Attack Run"

echo "== DONE obj-both-sides-sample =="