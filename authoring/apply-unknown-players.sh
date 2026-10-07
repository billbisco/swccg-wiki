#!/bin/bash
# Apply Unknown Player dest + Unknown players index.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/unknown-players.tgz" ]; then
  tar xzf "$ROOT/unknown-players.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/unknown-players-titles.tsv}"
SUMMARY="${2:-Unknown Player dest and Unknown players index}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Unknown players
Unknown Player
Blank Player
unnamed
2014 World Championship
List of SWCCG tournaments
Tournaments
Championships
Category:2014
EOF
echo APPLY-UNKNOWN-PLAYERS-DONE
