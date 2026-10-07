#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
edit() { docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin "$1" < "$2"; }
edit 'Squadron Members' "$ROOT/pages/Squadron_Members.wiki"
edit 'Corellian Engineering Corporation (fan site)' "$ROOT/pages/Corellian_Engineering_Corporation_(fan_site).wiki"
edit 'Jeff Hansen' "$ROOT/pages/people/Jeff_Hansen.wiki"
edit 'John Sarnecki' "$ROOT/pages/people/John_Sarnecki.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
for t in 'Squadron Members' 'Corellian Engineering Corporation (fan site)' 'Jeff Hansen' 'John Sarnecki'; do
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" || true
done
echo DONE wayback notes
