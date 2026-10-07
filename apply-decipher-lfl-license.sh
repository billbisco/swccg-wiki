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

edit "Decipher and the Star Wars CCG Lucasfilm license" "$PAGES/Decipher_and_the_Star_Wars_CCG_Lucasfilm_license.wiki" "new: Decipher LFL license fight / Dec 2001 loss / PC handoff (cited)"
edit "Loss of the Decipher Lucasfilm license" "$PAGES/Loss_of_the_Decipher_Lucasfilm_license.wiki" "redirect to Decipher and the Star Wars CCG Lucasfilm license"
edit "Decipher Lucasfilm license" "$PAGES/Decipher_Lucasfilm_license.wiki" "redirect to Decipher and the Star Wars CCG Lucasfilm license"
edit "Decipher" "$PAGES/Decipher.wiki" "cross-link Decipher LFL license article"
edit "Players Committee" "$PAGES/Players_Committee.wiki" "cross-link Decipher LFL license article"
edit "Players Committee-Lucasfilm agreement" "$PAGES/Players_Committee-Lucasfilm_agreement.wiki" "cross-link Decipher LFL license article"
edit "History of the Players Committee" "$PAGES/History_of_the_Players_Committee.wiki" "cross-link Decipher LFL license article"
edit "Main Page" "$PAGES/Main_Page.wiki" "cross-link Decipher LFL license article"

echo "FlaggedRevs reviewAllPages"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<EOF || true
Decipher and the Star Wars CCG Lucasfilm license
Loss of the Decipher Lucasfilm license
Decipher Lucasfilm license
Decipher
Players Committee
Players Committee-Lucasfilm agreement
History of the Players Committee
Main Page
EOF

echo VERIFY
docker exec swccg_wiki php maintenance/run.php getText "Decipher and the Star Wars CCG Lucasfilm license" | head -20
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Main Page" | grep -n "Lucasfilm license\|Players Committee-Lucasfilm" | head -10
echo ----
docker exec swccg_wiki php maintenance/run.php getText "Decipher" | grep -n "Lucasfilm license" | head -5
echo license-apply done