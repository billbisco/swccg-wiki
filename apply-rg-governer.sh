#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec swccg_wiki mkdir -p /tmp/rg-tarkin
docker cp "$ROOT/encyclopedia/upload/RG-C1-Governer-Tarkin.jpg" swccg_wiki:/tmp/rg-tarkin/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Category One original photo of printed playtest Governer Tarkin" \
  /tmp/rg-tarkin || true
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Category One original of Governer Tarkin playtest sticker" \
  "File:RG-C1-Governer-Tarkin.jpg" < "$ROOT/pages/File_RG-C1-Governer-Tarkin.jpg.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Official playtest title Governer Tarkin; drop Remastered column (no unique-only rows)" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold"
docker exec swccg_wiki php maintenance/run.php purgePage "File:RG-C1-Governer-Tarkin.jpg"
echo DONE rg-governer
