#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG_DIR="$ROOT/set-card-art"
STAGE=$(mktemp -d)

ARCHIVES=(
  CC-D-projectivetelepathy-decipher-archive.gif
  ANH-L-attackrun-decipher-archive.gif
  Premiere-D-limitedresources-decipher-archive.gif
  Premiere-L-berustew-decipher-archive.gif
  Premiere-L-spaceportspeeders-decipher-archive.gif
)

echo "== importImages: bleach exterior corner pads to #FFFFFF on Decipher archives =="
for f in "${ARCHIVES[@]}"; do
  if [ ! -f "$IMG_DIR/$f" ]; then
    echo "MISSING $IMG_DIR/$f" >&2
    exit 1
  fi
  cp -f "$IMG_DIR/$f" "$STAGE/$f"
done
docker exec swccg_wiki mkdir -p /tmp/errata-archives-white-corners
docker cp "$STAGE/." swccg_wiki:/tmp/errata-archives-white-corners/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Bleach soft gray drop-shadow dither in exterior corner pads to pure #FFFFFF on Decipher archive faces (Errata hub); black border and card face untouched" \
  --overwrite \
  /tmp/errata-archives-white-corners
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Bleach soft gray drop-shadow dither in exterior corner pads to pure #FFFFFF on Decipher archive faces (Errata hub); black border and card face untouched" \
    /tmp/errata-archives-white-corners || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
rm -rf "$STAGE"

# Do NOT edit Errata.wiki — Original|353px| Errata|350px| five-column layout stays locked

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

for f in "${ARCHIVES[@]}"; do
  purge "File:$f"
done
purge "Errata"
purge "Projective Telepathy (Original)"
purge "Attack Run (Original)"
purge "Limited Resources (Original)"
purge "Beru Stew (Original)"
purge "Spaceport Speeders (Original)"

echo "== DONE errata-archives-white-corners =="
