#!/bin/bash
# Apply 2013 TMW leftover Xerox: Day 1 Matt Wehner p40 Light / p41 Dark.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-tmw-xerox.tgz" ]; then
  tar xzf "$ROOT/y2013-tmw-xerox.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-tmw-xerox-titles.tsv}"
SUMMARY="${2:-2013 TMW leftover Xerox Matt Wehner p40-p41 MWYHL / SYCFA}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
docker exec swccg_wiki bash -c 'rm -rf /tmp/y2013-tmw-xerox; mkdir -p /tmp/y2013-tmw-xerox'
for f in \
  "2013 Texas Mini Worlds Day 1 p40 Matt Wehner LS.png" \
  "2013 Texas Mini Worlds Day 1 p41 Matt Wehner DS.png"
do
  if [ -f "$ROOT/y2013-tmw-media/$f" ]; then
    docker cp "$ROOT/y2013-tmw-media/$f" "swccg_wiki:/tmp/y2013-tmw-xerox/$f"
  fi
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2013 Texas Mini Worlds leftover Xerox page scans" \
  --extensions=png \
  /tmp/y2013-tmw-xerox > /tmp/y2013-tmw-import.log 2>&1 || true
grep -E 'Found|Added|Skipped|imported' /tmp/y2013-tmw-import.log | tail -8 || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 Texas Mini Worlds
Category:2013
Matt Wehner
Legacy Open
EOF
echo APPLY-2013-TMW-XEROX-DONE
