#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
edit() {
  local title="$1" file="$2" summary="$3"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}
edit "Scott Lingrell" "$ROOT/pages/Scott_Lingrell.wiki" \
  "GEMP handle advocate; current Head/Lead Advocate; CRingwell"
edit "Advocate" "$ROOT/pages/Advocate.wiki" \
  "PC office; current Head/Lead Advocate is Scott Lingrell (GEMP advocate)"
edit "Players Committee advocates" "$ROOT/pages/Players_Committee_advocates.wiki" \
  "PC is an organization of Advocates; current Head/Lead is Scott Lingrell (GEMP advocate)"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Scott Lingrell"
docker exec swccg_wiki php maintenance/run.php purgePage "Advocate"
docker exec swccg_wiki php maintenance/run.php purgePage "Players Committee advocates"
docker exec swccg_wiki php maintenance/run.php purgePage "crngwell"
echo DONE advocate-handle
