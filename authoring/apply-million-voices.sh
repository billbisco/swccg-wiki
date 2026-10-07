#!/bin/bash
set -euo pipefail
PAGE="A Million Voices Crying Out"
FILE=/opt/swccg-wiki/pages/remaining/11_68.wiki
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Decipher starred strategy" "$PAGE" < "$FILE"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
echo "$PAGE" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo million voices strategy applied
