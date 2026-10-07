#!/bin/bash
# Apply 2013 SoCal leftover Xerox: Day 1 Jan Westergard p43 Light / p44 Dark.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-socal-xerox.tgz" ]; then
  tar xzf "$ROOT/y2013-socal-xerox.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-socal-xerox-titles.tsv}"
SUMMARY="${2:-2013 SoCal leftover Xerox Jan Westergard p43-p44 Watch Your Step / Invasion}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
docker exec swccg_wiki bash -c 'rm -rf /tmp/y2013-socal-xerox; mkdir -p /tmp/y2013-socal-xerox'
for f in \
  "2013 SoCal Grand Prix Day 1 p43 Jan Westergard LS.png" \
  "2013 SoCal Grand Prix Day 1 p44 Jan Westergard DS.png"
do
  if [ -f "$ROOT/y2013-socal-media/$f" ]; then
    docker cp "$ROOT/y2013-socal-media/$f" "swccg_wiki:/tmp/y2013-socal-xerox/$f"
  fi
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2013 SoCal Grand Prix leftover Xerox page scans" \
  --extensions=png \
  /tmp/y2013-socal-xerox > /tmp/y2013-socal-import.log 2>&1 || true
grep -E 'Found|Added|Skipped|imported' /tmp/y2013-socal-import.log | tail -8 || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 SoCal Grand Prix
Category:2013
Jan Westergard
Legacy Open
EOF
echo APPLY-2013-SOCAL-XEROX-DONE
