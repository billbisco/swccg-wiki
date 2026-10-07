#!/bin/bash
set -euo pipefail
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Cite refs; split Scomp sections; strategy byline" "Template:Card" < /opt/swccg-wiki/pages/Template_Card.wiki
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="POC: citations, byline, combos not in rulings" "Darth Vader" < /opt/swccg-wiki/pages/ds-cards/1_168.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Template:Card' 'Darth Vader' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo vader poc done
