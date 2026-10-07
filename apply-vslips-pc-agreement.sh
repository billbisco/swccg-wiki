#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"

strip_bom() {
  python3 - <<PY
from pathlib import Path
p = Path("$1")
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
p.write_bytes(raw)
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "V-slips" "$PAGES/V-slips.wiki" "new: V-slips / Virtual slips overview with citations"
edit "Virtual slips" "$PAGES/Virtual_slips.wiki" "redirect to V-slips"
edit "Virtual Slips" "$PAGES/Virtual_Slips.wiki" "redirect to V-slips"
edit "Players Committee-Lucasfilm agreement" "$PAGES/Players_Committee-Lucasfilm_agreement.wiki" "new: PC-Lucasfilm agreement (cited; Disney gap labeled)"
edit "Players Committee Lucasfilm agreement" "$PAGES/Players_Committee_Lucasfilm_agreement.wiki" "redirect to Players Committee-Lucasfilm agreement"
edit "Players Committee" "$PAGES/Players_Committee.wiki" "link agreement + V-slips"
edit "Main Page" "$PAGES/Main_Page.wiki" "cross-links: History, PC-Lucasfilm agreement, V-slips"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<EOF || true
V-slips
Virtual slips
Virtual Slips
Players Committee-Lucasfilm agreement
Players Committee Lucasfilm agreement
Players Committee
Main Page
EOF

echo VERIFY
docker exec swccg_wiki php maintenance/run.php getText "V-slips" | head -15
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Players Committee-Lucasfilm agreement" | head -15
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Virtual slips"
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Main Page" | grep -n "V-slips\|Lucasfilm agreement\|History of the Players" | head -15
echo vslips-pc-agreement apply done
