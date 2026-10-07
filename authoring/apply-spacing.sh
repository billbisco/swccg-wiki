#!/bin/bash
set -euo pipefail
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="protect spaces before subtype/model in #if" "Template:Card" < /opt/swccg-wiki/pages/Template_Card.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Template:Card' 'Alter' "Vader's Lightsaber" '2X-3KPR (Tooex)' 'Luke Skywalker' 'Millennium Falcon' 'Death Star Plans' 'Darth Vader' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo spacing done
