#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Corellian Engineering Corporation (fan site)' \
  < "$ROOT/pages/Corellian_Engineering_Corporation_(fan_site).wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Category:Decipher' \
  < "$ROOT/pages/Category_Decipher.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Category:History' \
  < "$ROOT/pages/Category_History.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
for t in 'Corellian Engineering Corporation (fan site)' 'Category:Decipher' 'Category:History' 'Squadron Members' 'Sandy Wible'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done
echo DONE cats
