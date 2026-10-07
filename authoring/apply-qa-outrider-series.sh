#!/bin/bash
# Apply Outrider Cup series hub + Team Europe dest-link fix.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
bash "$ROOT/apply-tsv.sh" "$ROOT/qa-outrider-series-titles.tsv" "Outrider Cup series hub; Team Europe dual-title dests"
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Outrider Cup
Team USA
Team Europe
Category:Teams
EOF
echo "APPLY-QA-OUTRIDER-SERIES-DONE"
