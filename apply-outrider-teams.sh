#!/bin/bash
# Apply Outrider team hubs + player Finish rows + Friday team winner lines.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/outrider-teams.tgz" ]; then
  tar xzf "$ROOT/outrider-teams.tgz" -C "$ROOT"
fi
bash "$ROOT/apply-tsv.sh" "$ROOT/outrider-teams-titles.tsv" "Outrider Cups as team events: rosters, matches, team winners"
echo "== extra hub purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
2019 Outrider Cup
2021 Outrider Cup
2023 Outrider Cup III
2026 Outrider Cup IV
List of SWCCG tournaments
Joe Olson
Bastian Winkelhaus
Chris Kelly
Jared Napolitano
Mike Kessling
2024 World Championship
2023 World Championship
2023 Endor Grand Prix
2025 World Championship
EOF
echo APPLY-OUTRIDER-DONE
