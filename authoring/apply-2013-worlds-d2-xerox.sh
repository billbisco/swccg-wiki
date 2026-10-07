#!/bin/bash
# Apply 2013 Worlds leftover Xerox: Day 2 Justin Desai Light p31.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-worlds-d2-xerox.tgz" ]; then
  tar xzf "$ROOT/y2013-worlds-d2-xerox.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-worlds-d2-xerox-titles.tsv}"
SUMMARY="${2:-2013 Worlds leftover Xerox Justin Desai Light p31}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
docker exec swccg_wiki bash -c 'rm -rf /tmp/y2013-worlds-d2-xerox; mkdir -p /tmp/y2013-worlds-d2-xerox'
for f in \
  "2013 Worlds Day 2 p31 Justin Desai LS.png"
do
  if [ -f "$ROOT/y2013-worlds-media/$f" ]; then
    docker cp "$ROOT/y2013-worlds-media/$f" "swccg_wiki:/tmp/y2013-worlds-d2-xerox/$f"
  fi
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2013 World Championship leftover Xerox page scans" \
  --extensions=png \
  /tmp/y2013-worlds-d2-xerox > /tmp/y2013-import.log 2>&1 || true
grep -E 'Found|Added|Skipped|imported' /tmp/y2013-import.log | tail -8 || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 World Championship
Category:2013
Justin Desai
Legacy Open
EOF
echo APPLY-2013-WORLDS-D2-XEROX-DONE
