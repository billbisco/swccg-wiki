#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
for pair in \
  "Patrick Johnson|pages/player-stubs/Patrick_Johnson.wiki" \
  "Timo Dusel|pages/player-stubs/Timo_Dusel.wiki" \
  "Brad Kippel|pages/player-stubs/Brad_Kippel.wiki" \
  "Joe Horbey|pages/player-stubs/Joe_Horbey.wiki" \
  "Alex Prodoehl|pages/player-stubs/Alex_Prodoehl.wiki" \
  "Matthew Ford|pages/player-stubs/Matthew_Ford.wiki" \
  "Garrett Larson|pages/player-stubs/Garrett_Larson.wiki" \
  "Kendall Halman|pages/player-stubs/Kendall_Halman.wiki" \
  "Charlie Hickey|pages/player-stubs/Charlie_Hickey.wiki" \
  "Randy Scott|pages/player-stubs/Randy_Scott.wiki" \
  "Casey Johnson|pages/player-stubs/Casey_Johnson.wiki"
do
  title="${pair%%|*}"
  f="$ROOT/${pair#*|}"
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="Sources: real URLs not leftover numbered refs" "$title" < "$f"
done
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Patrick Johnson
Timo Dusel
Charlie Hickey
EOF
echo DONE stub-sources
