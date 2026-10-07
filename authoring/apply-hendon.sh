#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Hendon start: Kashyyyk: Chewie's Hut (deploys only as starting location)" \
  "2026 GEMPC Robbie Hendon LS LTWW(V)" < "$ROOT/pages/2026_GEMPC_Robbie_Hendon_LS_LTWW(V).wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Hendon start inferred from Chewie's Hut deploy-only text" \
  "2026 Tenth Annual GEMPC" < "$ROOT/pages/2026_Tenth_Annual_GEMPC.wiki"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin >/tmp/fr.out || true
tail -3 /tmp/fr.out
docker exec swccg_wiki php maintenance/run.php purgePage "2026 GEMPC Robbie Hendon LS LTWW(V)" || true
docker exec swccg_wiki php maintenance/run.php purgePage "2026 Tenth Annual GEMPC" || true
echo DONE hendon
