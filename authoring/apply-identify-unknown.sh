#!/bin/bash
# Apply facing-page dests + informed-identity merges.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/identify-unknown.tgz" ]; then
  tar xzf "$ROOT/identify-unknown.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/identify-unknown-titles.tsv}"
SUMMARY="${2:-Facing-page dests and informed-identity player merges}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Unknown players
Unknown Player
2014 World Championship
2013 Match Play Championship
2013 World Championship
Vinayum Bari
Mike Stirling
Brian Terwilliger
Matt Sokol
Steve Harpster
Kevin Shannon
Chris Wirfs
Chris Gogolen
Mike Pistone
Mark Walseth
Matt Schmaltz
List of SWCCG tournaments
Championships
Category:2013
Category:2014
EOF
echo APPLY-IDENTIFY-UNKNOWN-DONE
