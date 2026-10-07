#!/bin/bash
# Apply 2014 Alderaan leftover Xerox. ReviewTitles TSV titles only.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-alderaan-xerox.tgz" ]; then
  tar xzf "$ROOT/y2014-alderaan-xerox.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-alderaan-xerox-titles.tsv}"
SUMMARY="${2:-2014 Alderaan leftover Xerox}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
docker exec swccg_wiki bash -c 'rm -rf /tmp/y2014-alderaan-xerox; mkdir -p /tmp/y2014-alderaan-xerox'
if [ -d "$ROOT/y2014-alderaan-xerox-media" ]; then
  for f in "$ROOT/y2014-alderaan-xerox-media"/*; do
    [ -f "$f" ] || continue
    docker cp "$f" "swccg_wiki:/tmp/y2014-alderaan-xerox/$(basename "$f")"
  done
fi
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2014 Alderaan leftover Xerox PDFs" \
  --extensions=pdf \
  /tmp/y2014-alderaan-xerox > /tmp/y2014-alderaan-xerox-import.log 2>&1 || true
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2014 Alderaan leftover Xerox page scans" \
  --extensions=png \
  /tmp/y2014-alderaan-xerox >> /tmp/y2014-alderaan-xerox-import.log 2>&1 || true
grep -E 'Found|Added|Skipped|imported' /tmp/y2014-alderaan-xerox-import.log | tail -20 || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2014 Alderaan Regionals
Category:2014
Nathan
Steve
Gabe
Jeffrey W
Adam K
Legacy Open
EOF
echo APPLY-2014-ALDERAAN-XEROX-DONE
