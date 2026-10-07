#!/bin/bash
# Apply Hoth Limited infobox 260px box + packaging markup.
set -euo pipefail
ROOT=/opt/swccg-wiki

echo "== edit Hoth Limited =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin 'Hoth Limited' \
  < "$ROOT/pages/set-hubs/Hoth.wiki"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
for t in 'Hoth Limited' 'Hoth'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done

echo "DONE Hoth Limited infobox size"
