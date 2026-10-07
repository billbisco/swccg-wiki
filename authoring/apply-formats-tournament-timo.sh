#!/bin/bash
# Apply Formats hub expansion, Premiere-Death Star II format, Retro GEMPC tournament + Timo deck, CardLink + Common.js.
# VPS only; no git remote. Never prints /opt/swccg-wiki/.env
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

for f in \
  Formats.wiki \
  Premiere_-_Death_Star_II.wiki \
  Premiere_to_DSII.wiki \
  Template_CardLink.wiki \
  MediaWiki_Common.js.wiki
 do
  if [ ! -s "$PAGES/$f" ]; then echo "ERROR: missing $PAGES/$f" >&2; exit 1; fi
done
TOURNEY="$PAGES/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki"
DECK="$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations.wiki"
if [ ! -s "$TOURNEY" ] || [ ! -s "$DECK" ]; then echo "ERROR: missing tourney/deck" >&2; exit 1; fi

edit() {
  local title="$1"; local file="$2"; local summary="$3"
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

edit "Formats" "$PAGES/Formats.wiki" "Formats: add GEMP environments + Premiere-Death Star II; link Retro GEMPC"
edit "Premiere - Death Star II" "$PAGES/Premiere_-_Death_Star_II.wiki" "GEMP format stub Premiere - Death Star II (premiere_ds2); cite PC Retro GEMPC"
edit "Premiere to DSII" "$PAGES/Premiere_to_DSII.wiki" "redirect Premiere to DSII -> Premiere - Death Star II"
edit "2026 Retro GEMP Match Play Championship (Premiere to DSII)" "$TOURNEY" "Tournament article: 2026 Retro GEMP Match Play Championship Premiere to DSII; cite PC news"
edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations" "$DECK" "Decklist: Timo Dusel DS Ralltiir Operations from Retro GEMPC; CardLink hover"
edit "Template:CardLink" "$PAGES/Template_CardLink.wiki" "Template:CardLink for wiki card hover preview via Common.js"
edit "MediaWiki:Common.js" "$PAGES/MediaWiki_Common.js.wiki" "Common.js: bind swccg-card-link hover to existing card-zoom popup"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
printf '%s\n' \
  'Formats' \
  'Premiere - Death Star II' \
  'Premiere to DSII' \
  '2026 Retro GEMP Match Play Championship (Premiere to DSII)' \
  '2026 Retro GEMPC Timo Dusel DS Ralltiir Operations' \
  'Template:CardLink' \
  'MediaWiki:Common.js' \
  'Main Page' \
  | docker exec -i swccg_wiki php maintenance/run.php purgePage || true

echo formats-tournament-timo applied
