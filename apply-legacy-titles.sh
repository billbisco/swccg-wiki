#!/bin/bash
# Apply Legacy Virtual title banner crops (VB1-9 + VSh) ? official PC cardlist titles.
# Replaces collage thumbnails with same File: names.
set -euo pipefail
ROOT=/opt/swccg-wiki
SRC="$ROOT/set-art-virtual-cropped"
STAGE=/tmp/legacy-title-crops

mkdir -p "$STAGE"
rm -f "$STAGE"/*
for n in 1 2 3 4 5 6 7 8 9; do
  cp -f "$SRC/Set-VB${n}-title.jpg" "$STAGE/"
done
cp -f "$SRC/Set-VSh-title.jpg" "$STAGE/"

ls -la "$STAGE"

docker exec swccg_wiki mkdir -p /tmp/legacy-title-crops
docker cp "$STAGE/." swccg_wiki:/tmp/legacy-title-crops/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Legacy Virtual titles: official PC cardlist banner crops (replace collages)" \
  --overwrite \
  /tmp/legacy-title-crops

docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images
docker exec swccg_wiki php maintenance/run.php refreshImageMetadata --force || true

# FlaggedRevs review (file pages / any pending)
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

# Purge Main Page + hubs + file pages so tiles refresh
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Main Page
Virtual Block 1
Virtual Block 2
Virtual Block 3
Virtual Block 4
Virtual Block 5
Virtual Block 6
Virtual Block 7
Virtual Block 8
Virtual Block 9
Virtual Shields
File:Set-VB1-title.jpg
File:Set-VB2-title.jpg
File:Set-VB3-title.jpg
File:Set-VB4-title.jpg
File:Set-VB5-title.jpg
File:Set-VB6-title.jpg
File:Set-VB7-title.jpg
File:Set-VB8-title.jpg
File:Set-VB9-title.jpg
File:Set-VSh-title.jpg
EOF

echo "legacy title crops applied"
# Spot-check hashed image headers (sizes should match local crops)
for f in Set-VB1-title.jpg Set-VB7-title.jpg Set-VSh-title.jpg; do
  echo "---- $f"
  docker exec swccg_wiki bash -c "find /var/www/html/images -name '$f' -printf '%p %s\n' 2>/dev/null | head -5"
done
