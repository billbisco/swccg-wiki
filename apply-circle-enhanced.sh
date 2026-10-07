#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec swccg_wiki mkdir -p /tmp/rg-circle-e
docker cp "$ROOT/encyclopedia/upload/RG-T-The-Circle-Is-Now-Complete-v3.png" swccg_wiki:/tmp/rg-circle-e/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Enhanced Circle-only reconstruction (The Circle Is Now Complete.png)" \
  /tmp/rg-circle-e || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Talaga standalone Circle: Enhanced The Circle Is Now Complete.png" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
echo DONE circle-enhanced
