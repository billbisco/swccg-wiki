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

edit "Virtual Sets (2002-2009)" "$PAGES/Virtual_Sets_(2002-2009).wiki" "pre-reorg Virtual Sets overview with citations"
edit "Pre-reorg Virtual Sets" "$PAGES/Pre-reorg_Virtual_Sets.wiki" "redirect to Virtual Sets (2002-2009)"
edit "History of the Players Committee" "$PAGES/History_of_the_Players_Committee.wiki" "PC history timeline with citations and era layers"
edit "Players Committee" "$PAGES/Players_Committee.wiki" "link history and pre-reorg overview"
edit "Category:Virtual Legacy sets" "$PAGES/Category_Virtual_Legacy_sets.wiki" "point to pre-reorg overview; Blocks vs Sets"
edit "Main Page" "$PAGES/Main_Page.wiki" "Legacy band intro links to pre-reorg sets and PC history"
edit "Formats" "$PAGES/Formats.wiki" "see also PC history and pre-reorg Virtual Sets"
edit "Rulebooks" "$PAGES/Rulebooks.wiki" "Legacy Virtual band links to history and pre-reorg sets"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<EOF || true
Virtual Sets (2002-2009)
Pre-reorg Virtual Sets
History of the Players Committee
Players Committee
Category:Virtual Legacy sets
Main Page
Formats
Rulebooks
EOF

echo VERIFY
docker exec swccg_wiki php maintenance/run.php getText "Virtual Sets (2002-2009)" | head -12
echo ----
docker exec swccg_wiki php maintenance/run.php getText "History of the Players Committee" | head -12
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Pre-reorg Virtual Sets"
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Main Page" | grep -n "Virtual Legacy\|pre-reorg\|History of the Players" | head -10
echo history pages apply done