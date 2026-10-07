#!/bin/bash
# Apply Formats stub (+ Format redirect). VPS apply only; no git remote.
# Never prints /opt/swccg-wiki/.env
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

for f in Formats.wiki Format.wiki; do
  if [ ! -s "$PAGES/$f" ]; then
    echo "ERROR: missing $PAGES/$f" >&2
    exit 1
  fi
done

echo "== edit Formats =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Formats stub: Standard/Legacy + sealed/cube index; cite AFG and PC site" \
  "Formats" < "$PAGES/Formats.wiki"

echo "== edit Format redirect =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="redirect Format → Formats" \
  "Format" < "$PAGES/Format.wiki"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
printf '%s\n' 'Formats' 'Format' 'Main Page' \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true

echo Formats stub applied