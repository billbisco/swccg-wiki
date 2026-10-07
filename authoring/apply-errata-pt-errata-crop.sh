#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG_SRC="$ROOT/set-card-art/CC-D-projectivetelepathy.gif"
STAGE=$(mktemp -d)

echo "== importImages cropped PT Errata/Holotable face =="
if [ ! -f "$IMG_SRC" ]; then
  echo "MISSING image $IMG_SRC" >&2
  exit 1
fi
cp -f "$IMG_SRC" "$STAGE/CC-D-projectivetelepathy.gif"
docker exec swccg_wiki mkdir -p /tmp/pt-errata-crop
docker cp "$STAGE/." swccg_wiki:/tmp/pt-errata-crop/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Crop Holotable black pad; opaque GIF (no transparency halo on white page); match Original size on Errata hub" \
  --overwrite \
  /tmp/pt-errata-crop
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Crop Holotable black pad; opaque GIF; match Original size on Errata hub" \
    /tmp/pt-errata-crop || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
# Delete stale thumbs so MediaWiki regenerates
docker exec -u root swccg_wiki bash -lc 'rm -rf /var/www/html/images/thumb/6/69/CC-D-projectivetelepathy.gif || true'
rm -rf "$STAGE"

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

purge "File:CC-D-projectivetelepathy.gif"
purge "Errata"
purge "Projective Telepathy (Errata)"
purge "Projective Telepathy"

echo "== DONE pt-errata-crop =="
