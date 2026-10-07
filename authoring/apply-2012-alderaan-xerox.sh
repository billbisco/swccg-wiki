#!/bin/bash
# Apply 2012 Alderaan Regionals leftover Xerox. ReviewTitles TSV titles only.
# Default is the delta TSV + y2012-alderaan-media-delta when present.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2012-alderaan-xerox.tgz" ]; then
  tar xzf "$ROOT/y2012-alderaan-xerox.tgz" -C "$ROOT"
fi

if [ -s "$ROOT/y2012-alderaan-xerox-delta.tsv" ]; then
  DEFAULT_TSV="$ROOT/y2012-alderaan-xerox-delta.tsv"
else
  DEFAULT_TSV="$ROOT/y2012-alderaan-xerox-titles.tsv"
fi
TSV="${1:-$DEFAULT_TSV}"
SUMMARY="${2:-2012 Alderaan Regionals leftover Xerox}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" apply-2012-alderaan-xerox.sh 2>/dev/null || true
chmod +x apply-tsv.sh apply-2012-alderaan-xerox.sh || true

if [ -d "$ROOT/y2012-alderaan-media-delta" ]; then
  MEDIA_DIR="$ROOT/y2012-alderaan-media-delta"
else
  MEDIA_DIR="$ROOT/y2012-alderaan-media"
fi

echo "== importImages from $MEDIA_DIR =="
docker exec swccg_wiki bash -c 'rm -rf /tmp/y2012-alderaan-xerox; mkdir -p /tmp/y2012-alderaan-xerox'
if [ -d "$MEDIA_DIR" ]; then
  for f in "$MEDIA_DIR"/*; do
    [ -f "$f" ] || continue
    docker cp "$f" "swccg_wiki:/tmp/y2012-alderaan-xerox/$(basename "$f")"
  done
fi
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2012 Alderaan Regionals leftover Xerox PDFs" \
  --extensions=pdf \
  /tmp/y2012-alderaan-xerox > /tmp/y2012-alderaan-xerox-import.log 2>&1 || true
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2012 Alderaan Regionals leftover Xerox page scans" \
  --extensions=png \
  /tmp/y2012-alderaan-xerox >> /tmp/y2012-alderaan-xerox-import.log 2>&1 || true
grep -E 'Found|Added|Skipped|imported' /tmp/y2012-alderaan-xerox-import.log | tail -20 || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
{
  cut -f1 "$TSV"
  printf '%s\n' "2012 Alderaan Regionals" "Category:2012"
} | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo APPLY-2012-ALDERAAN-XEROX-DONE
