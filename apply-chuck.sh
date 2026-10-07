#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Chuck Kallenbach' \
  < "$ROOT/pages/Chuck_Kallenbach.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Squadron Members' \
  < "$ROOT/pages/Squadron_Members.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Chuck Kallenbach' || true
docker exec swccg_wiki php maintenance/run.php purgePage 'Squadron Members' || true
echo DONE chuck
