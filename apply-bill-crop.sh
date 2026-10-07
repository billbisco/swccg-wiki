#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
GIF="$ROOT/set-card-art/ANH-L-attackrun-wb-decipher.gif"
FILE_WIKI="$ROOT/pages/File_ANH-L-attackrun-wb-decipher.gif.wiki"
ANH_WIKI="$ROOT/pages/A_New_Hope.wiki"
HT_EXPECTED=3a3ee5afcd96a081a9ae73b683a4001c93ad862c
NEW_EXPECTED_SHA=a7876aae9073a0cbaf78219ee7e539ba7f1e36c1

ht_hex() {
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name ANH-L-attackrun.gif | head -1); sha1sum "$f" | awk "{print \$1}"'
}

echo "== Holotable sha1 BEFORE =="
HT_BEFORE=$(ht_hex)
echo "ht_before=$HT_BEFORE"
echo "$HT_BEFORE" > /tmp/ht-sha1-before-bill-crop.txt
if [ "$HT_BEFORE" != "$HT_EXPECTED" ]; then
  echo "FATAL: Holotable sha1 mismatch before=$HT_BEFORE expected=$HT_EXPECTED" >&2
  exit 1
fi

test -f "$GIF"
test -f "$FILE_WIKI"
test -f "$ANH_WIKI"
echo "== local gif (Bill hand-crop — do not alter) =="
ls -la "$GIF"
sha1sum "$GIF"
LOC_SHA=$(sha1sum "$GIF" | awk '{print $1}')
test "$LOC_SHA" = "$NEW_EXPECTED_SHA"
# dims via identify if available, else skip PIL
if command -v identify >/dev/null 2>&1; then
  identify "$GIF"
fi

normalize() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PY
}
normalize "$FILE_WIKI"
normalize "$ANH_WIKI"
grep -n 'ANH-L-attackrun-wb-decipher.gif|200px|link=Attack Run' "$ANH_WIKI"
grep -n 'ANH-L-attackrun.gif|200px|link=Attack Run' "$ANH_WIKI" && { echo "FATAL: Holotable still Attack Run thumb"; exit 1; } || echo "ANH thumb OK (no Holotable Attack Run thumb)"

echo "== SAFETY: stage WB only =="
STAGE=/tmp/bill-crop-stage
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -f "$GIF" "$STAGE/ANH-L-attackrun-wb-decipher.gif"
n=$(find "$STAGE" -maxdepth 1 -type f -name '*.gif' | wc -l)
test "$n" -eq 1
ls -la "$STAGE"

echo "== importImages overwrite (WB only — Bill crop) =="
docker exec swccg_wiki mkdir -p /tmp/bill-crop-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/bill-crop-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/bill-crop-gifs/
COMMENT='Attack Run WB: Bill hand-crop 350x490 (sha1 a7876aae9073a0cbaf78219ee7e539ba7f1e36c1); Errata/baseline face; do not re-crop; DO NOT touch Holotable ANH-L-attackrun.gif.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="$COMMENT" \
  --overwrite \
  /tmp/bill-crop-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="$COMMENT" \
    /tmp/bill-crop-gifs
fi

echo "== edit File description =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="WB File: Bill hand-crop 350x490 baseline/Errata face; Holotable on PC Errata only" \
  "File:ANH-L-attackrun-wb-decipher.gif" < "$FILE_WIKI"

echo "== edit A New Hope — Attack Run thumb to WB File =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="A New Hope list: Attack Run thumb = WB Decipher File (not Holotable)" \
  "A New Hope" < "$ANH_WIKI"

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
purge "A New Hope"
purge "File:ANH-L-attackrun.gif"

echo "== Holotable sha1 AFTER =="
HT_AFTER=$(ht_hex)
echo "ht_after=$HT_AFTER"
echo "$HT_AFTER" > /tmp/ht-sha1-after-bill-crop.txt
if [ "$HT_AFTER" != "$HT_EXPECTED" ]; then
  echo "FATAL: Holotable changed!" >&2
  exit 1
fi
echo "HOLOTABLE_OK"

echo "== on-disk WB probe =="
docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name ANH-L-attackrun-wb-decipher.gif | head -1); ls -la "$f"; sha1sum "$f"'
echo "DONE_APPLY_BILL_CROP"
