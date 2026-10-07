#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG_SRC="$ROOT/set-card-art/CC-D-projectivetelepathy-decipher-archive.gif"
STAGE=$(mktemp -d)

echo "== importImages cropped PT Decipher archive face =="
if [ ! -f "$IMG_SRC" ]; then
  echo "MISSING image $IMG_SRC" >&2
  exit 1
fi
cp -f "$IMG_SRC" "$STAGE/CC-D-projectivetelepathy-decipher-archive.gif"
docker exec swccg_wiki mkdir -p /tmp/pt-archive-crop
docker cp "$STAGE/." swccg_wiki:/tmp/pt-archive-crop/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Crop white pad/drop-shadow from Decipher archive face; tight corner pad to match Holotable Errata size on Errata hub" \
  --overwrite \
  /tmp/pt-archive-crop
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Crop white pad/drop-shadow from Decipher archive face; tight corner pad to match Holotable Errata size on Errata hub" \
    /tmp/pt-archive-crop || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
rm -rf "$STAGE"

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

# Bust thumbs + page cache for faces that use this file
purge "File:CC-D-projectivetelepathy-decipher-archive.gif"
purge "Errata"
purge "Projective Telepathy (Original)"
purge "Projective Telepathy"

echo "== DONE pt-archive-crop =="
