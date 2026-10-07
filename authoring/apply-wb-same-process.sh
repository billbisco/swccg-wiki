#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
GIF="$ROOT/set-card-art/ANH-L-attackrun-wb-decipher.gif"
FILE_WIKI="$ROOT/pages/File_ANH-L-attackrun-wb-decipher.gif.wiki"
HT_EXPECTED=3a3ee5afcd96a081a9ae73b683a4001c93ad862c
NEW_EXPECTED_SHA=2e4d370c81b9f2e5b9c6fb2b192e019a13b2697d

ht_hex() {
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name ANH-L-attackrun.gif | head -1); sha1sum "$f" | awk "{print \$1}"'
}

echo "== Holotable sha1 BEFORE =="
HT_BEFORE=$(ht_hex)
echo "ht_before=$HT_BEFORE"
echo "$HT_BEFORE" > /tmp/ht-sha1-before-wb-same.txt
if [ "$HT_BEFORE" != "$HT_EXPECTED" ]; then
  echo "FATAL: Holotable sha1 mismatch before=$HT_BEFORE expected=$HT_EXPECTED" >&2
  exit 1
fi

test -f "$GIF"
test -f "$FILE_WIKI"
echo "== local gif =="
ls -la "$GIF"
sha1sum "$GIF"
LOC_SHA=$(sha1sum "$GIF" | awk '{print $1}')
test "$LOC_SHA" = "$NEW_EXPECTED_SHA"
python3 - <<PY
from PIL import Image
im=Image.open("$GIF")
print("dims", im.size)
assert im.size == (350, 490), im.size
PY

# Normalize File wiki to LF UTF-8 (no BOM) — NEVER use sed s/\r$// via Windows (strips trailing r)
python3 - "$FILE_WIKI" <<'PY'
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

echo "== SAFETY: stage WB only =="
STAGE=/tmp/wb-same-process-stage
rm -rf "$STAGE"
mkdir -p "$STAGE"
cp -f "$GIF" "$STAGE/ANH-L-attackrun-wb-decipher.gif"
n=$(find "$STAGE" -maxdepth 1 -type f -name '*.gif' | wc -l)
test "$n" -eq 1
ls -la "$STAGE"

echo "== importImages overwrite (WB only) =="
docker exec swccg_wiki mkdir -p /tmp/wb-same-process-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/wb-same-process-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/wb-same-process-gifs/
COMMENT='Attack Run WB same-process (Chief/Bill): Errata archive-faces flush to white-border outer silhouette; bleach exterior corner pads + BR gray #FFFFFF; 350x490; NOT cite-only; DO NOT touch Holotable ANH-L-attackrun.gif.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="$COMMENT" \
  --overwrite \
  /tmp/wb-same-process-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "overwrite failed; retry without overwrite" >&2
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="$COMMENT" \
    /tmp/wb-same-process-gifs
fi

echo "== edit File description =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="WB File summary: same Errata archive-faces process; flush white-border silhouette 350x490; baseline Errata face; Holotable on PC Errata only" \
  "File:ANH-L-attackrun-wb-decipher.gif" < "$FILE_WIKI"

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
echo "$HT_AFTER" > /tmp/ht-sha1-after-wb-same.txt
if [ "$HT_AFTER" != "$HT_EXPECTED" ]; then
  echo "FATAL: Holotable changed!" >&2
  exit 1
fi
echo "HOLOTABLE_OK"

echo "== on-disk WB probe =="
docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name ANH-L-attackrun-wb-decipher.gif | head -1); ls -la "$f"; sha1sum "$f"; python3 -c "from PIL import Image; im=Image.open(\"$f\"); print(im.size)"'

echo "DONE_APPLY_WB_SAME_PROCESS"
