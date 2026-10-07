#!/bin/bash
set -euo pipefail
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Unwrap Decipher strategy wraps; Cite refs; Scomp sections" "Djas Puhr" < /opt/swccg-wiki/pages/ds-cards/1_171.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf '%s\n' 'Djas Puhr' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo djas extras done
