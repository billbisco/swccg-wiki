#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
GIF="$ROOT/set-card-art/ANH-L-attackrun-wb-decipher.gif"
HT_EXPECTED=3a3ee5afcd96a081a9ae73b683a4001c93ad862c

ht_hex() {
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name ANH-L-attackrun.gif | head -1); sha1sum "$f" | awk "{print \$1}"'
}

echo "== Holotable sha1 BEFORE =="
HT_BEFORE=$(ht_hex)
echo "ht_before=$HT_BEFORE"
echo "$HT_BEFORE" > /tmp/ht-sha1-before-wb-recrop.txt
if [ "$HT_BEFORE" != "$HT_EXPECTED" ]; then
  echo "FATAL: Holotable sha1 mismatch before=$HT_BEFORE expected=$HT_EXPECTED" >&2
  exit 1
fi

test -f "$GIF"
echo "== local gif =="
ls -la "$GIF"
sha1sum "$GIF"
python3 - <<PY
from PIL import Image
im=Image.open("$GIF")
print("dims", im.size)
assert im.size == (348, 488), im.size
PY

echo "== SAFETY: stage WB only =="
STAGE=/tmp/wb-recrop-stage
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -f "$GIF" "$STAGE/ANH-L-attackrun-wb-decipher.gif"
rm -f "$STAGE/ANH-L-attackrun.gif" || true
n=$(find "$STAGE" -maxdepth 1 -type f -name '*.gif' | wc -l)
test "$n" -eq 1
ls -la "$STAGE"

echo "== importImages overwrite (WB only) =="
docker exec swccg_wiki mkdir -p /tmp/wb-recrop-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/wb-recrop-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/wb-recrop-gifs/
COMMENT='Attack Run WB recrop (Bill): crop flush to outer white-border corners; bleach BR gray on white border to #FFFFFF; do NOT purple-flush; do NOT replace Holotable ANH-L-attackrun.gif.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="$COMMENT" \
  --overwrite \
  /tmp/wb-recrop-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "overwrite failed; retry without overwrite" >&2
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="$COMMENT" \
    /tmp/wb-recrop-gifs
fi

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}
purge "File:ANH-L-attackrun-wb-decipher.gif"
purge "Attack Run"
purge "Attack Run (Errata)"
purge "Attack Run (Original)"
purge "Attack Run (PC Errata)"
purge "Errata"
purge "File:ANH-L-attackrun.gif"

echo "== Holotable sha1 AFTER =="
HT_AFTER=$(ht_hex)
echo "ht_after=$HT_AFTER"
echo "$HT_AFTER" > /tmp/ht-sha1-after-wb-recrop.txt
if [ "$HT_AFTER" != "$HT_EXPECTED" ]; then
  echo "FATAL: Holotable changed!" >&2
  exit 1
fi
echo "HOLOTABLE_OK"

echo "== on-disk WB probe =="
docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name ANH-L-attackrun-wb-decipher.gif | head -1); ls -la "$f"; sha1sum "$f"; python3 -c "from PIL import Image; im=Image.open(\"$f\"); print(im.size)"'

echo "DONE_APPLY_WB_RECROP"
