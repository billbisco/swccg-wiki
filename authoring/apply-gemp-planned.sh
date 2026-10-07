#!/bin/bash
# Apply GEMP planned-features dests, redirects, and hub links.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
sed -i 's/\r$//' apply-tsv.sh gemp-planned-titles.tsv apply-gemp-planned.sh || true
chmod +x apply-tsv.sh
bash "$ROOT/apply-tsv.sh" "$ROOT/gemp-planned-titles.tsv" "GEMP planned features: Anything Goes follow-ups, True Sabacc, later tournament types"
echo "== extra hub purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
GEMP planned features
Anything Goes
True Sabacc
Planned GEMP features
GEMP roadmap
True Sabacc Game Mode
GEMP
Main Page
Formats
Tournaments
EOF
echo APPLY-GEMP-PLANNED-DONE
