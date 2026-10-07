#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
docker exec swccg_wiki bash -lc 'rm -rf /tmp/rg-t; mkdir -p /tmp/rg-t'
docker cp "$ROOT/rg-t.tgz" swccg_wiki:/tmp/rg-t.tgz
docker exec swccg_wiki bash -lc 'tar xzf /tmp/rg-t.tgz -C /tmp/rg-t && ls /tmp/rg-t | wc -l'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Hi-res Reflections Gold reconstructions from Andy Talaga Drive" \
  /tmp/rg-t || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Talaga Drive hi-res column on Reflections Gold card list" \
  "Reflections Gold" < pages/Reflections_Gold.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
echo DONE talaga-rg
