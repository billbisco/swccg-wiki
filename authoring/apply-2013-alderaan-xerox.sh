#!/bin/bash
# Apply 2013 Alderaan leftover Xerox: Tom / Shannon / Schoenthal / Nathan.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-alderaan-xerox.tgz" ]; then
  tar xzf "$ROOT/y2013-alderaan-xerox.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-alderaan-xerox-titles.tsv}"
SUMMARY="${2:-2013 Alderaan leftover Xerox Tom Shannon Schoenthal Nathan}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
docker exec swccg_wiki bash -c 'rm -rf /tmp/y2013-alderaan-xerox; mkdir -p /tmp/y2013-alderaan-xerox'
for f in \
  "2013 Alderaan Regionals p03 Tom LS.png" \
  "2013 Alderaan Regionals p04 Tom DS.png" \
  "2013 Alderaan Regionals p07 Kevin Shannon DS.png" \
  "2013 Alderaan Regionals p08 Kevin Shannon LS.png" \
  "2013 Alderaan Regionals p21 Chris Schoenthal LS.png" \
  "2013 Alderaan Regionals p22 Chris Schoenthal DS.png" \
  "2013 Alderaan Regionals p25 Nathan DS.png" \
  "2013 Alderaan Regionals p26 Nathan LS.png"
do
  if [ -f "$ROOT/y2013-alderaan-media/$f" ]; then
    docker cp "$ROOT/y2013-alderaan-media/$f" "swccg_wiki:/tmp/y2013-alderaan-xerox/$f"
  fi
done
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2013 Alderaan Regionals leftover Xerox page scans" \
  --extensions=png \
  /tmp/y2013-alderaan-xerox > /tmp/y2013-alderaan-import.log 2>&1 || true
grep -E 'Found|Added|Skipped|imported' /tmp/y2013-alderaan-import.log | tail -12 || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 Alderaan Regionals
Category:2013
Tom
Kevin Shannon
Chris Schoenthal
Nathan
Legacy Open
EOF
echo APPLY-2013-ALDERAAN-XEROX-DONE
