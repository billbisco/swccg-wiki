#!/bin/bash
set -euo pipefail
PAGES=/opt/swccg-wiki/pages
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="card-rail floats left by default" "Template:Card" < "$PAGES/Template_Card.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="card-rail left default" "MediaWiki:Common.css" < "$PAGES/MediaWiki_Common.css.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="left is default; drop rail=left" "Darth Vader" < "$PAGES/ds-cards/1_168.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Template:Card' 'MediaWiki:Common.css' 'Darth Vader' 'Djas Puhr' 'Luke Skywalker' '2X-3KPR (Tooex)' 'Alter' 'Sense' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo left-rail default done
