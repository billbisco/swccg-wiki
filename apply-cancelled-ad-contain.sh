#!/bin/bash
# Main Page: contain Cancelled Expansions SoTE ad float; shrink thumb 280->160.
# Never prints /opt/swccg-wiki/.env
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"
MP="$PAGES/Main_Page.wiki"
if [ ! -s "$MP" ]; then echo "ERROR: missing $MP" >&2; exit 1; fi
if ! grep -q 'overflow:auto' "$MP" || ! grep -q '160px' "$MP"; then
  echo "ERROR: worktree Main_Page.wiki missing overflow/160px fix" >&2
  exit 1
fi
echo "== edit Main Page (Cancelled ad contain) =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Main Page: Cancelled Expansions ad thumb 160px + clear float before Virtual Legacy" \
  "Main Page" < "$MP"
echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
echo "== purge Main Page =="
printf '%s\n' 'Main Page' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo "== verify raw =="
curl -sL "https://wiki.swccg.com/wiki/Main_Page?action=raw" | sed -n '/Cancelled Expansions/,/Virtual Legacy/p' | head -30
if curl -sL "https://wiki.swccg.com/wiki/Main_Page?action=raw" | grep -q 'thumb|right|160px' && curl -sL "https://wiki.swccg.com/wiki/Main_Page?action=raw" | grep -q 'overflow:auto'; then
  echo "OK: 160px + overflow live"
else
  echo "WARN: expected markers missing on live raw" >&2
  exit 2
fi
if curl -sL "https://wiki.swccg.com/wiki/Main_Page?action=raw" | grep -q '280px'; then
  echo "WARN: 280px still present" >&2
  exit 3
fi
echo DONE