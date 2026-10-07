#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
STAGE=/tmp/pc-logos
mkdir -p "$STAGE"
cp -f "$ROOT/images/pc-logos/PC_logo_former.png" "$STAGE/"
cp -f "$ROOT/images/pc-logos/PC_logo_modern.png" "$STAGE/"

# Prefer HTML-entity-safe: ensure History page is UTF-8 without inventing content
python3 - <<'PY'
from pathlib import Path
p = Path("/opt/swccg-wiki/pages/History_of_the_Players_Committee.wiki")
b = p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"):
    b = b[3:]
    p.write_bytes(b)
text = b.decode("utf-8")
assert "PC_logo_former.png" in text and "PC_logo_modern.png" in text
assert "== Logos ==" in text
print("history page ok", len(text), "nonascii", sum(1 for c in text if ord(c) > 127))
PY

docker exec swccg_wiki mkdir -p /tmp/pc-logos
docker cp "$STAGE/." swccg_wiki:/tmp/pc-logos/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="PC logos: former GPN rulesupdate.pdf oval; modern GitHub org avatar (u/25210454); cite avatars.githubusercontent.com" \
  --overwrite \
  /tmp/pc-logos
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "import overwrite failed; retry without overwrite after delete"
  docker exec swccg_wiki php maintenance/run.php delete --user=Admin "File:PC_logo_former.png" --reason="replace" 2>/dev/null || true
  docker exec swccg_wiki php maintenance/run.php delete --user=Admin "File:PC_logo_modern.png" --reason="replace" 2>/dev/null || true
  docker exec -u root swccg_wiki bash -lc 'find /var/www/html/images -iname "*PC_logo_*" -print -delete' || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="PC logos: former GPN rulesupdate.pdf oval; modern GitHub org avatar (u/25210454); cite avatars.githubusercontent.com" \
    /tmp/pc-logos
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo "edit History of the Players Committee"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Logos: former GPN oval + modern site header (cited); Wikipedia-style side-by-side" \
  "History of the Players Committee" < "$ROOT/pages/History_of_the_Players_Committee.wiki"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -3
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
History of the Players Committee
File:PC_logo_former.png
File:PC_logo_modern.png
EOF

python3 - <<'PY'
import urllib.request
for u in [
 "https://wiki.swccg.com/wiki/History_of_the_Players_Committee",
 "https://wiki.swccg.com/wiki/File:PC_logo_former.png",
 "https://wiki.swccg.com/wiki/File:PC_logo_modern.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/PC_logo_former.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/PC_logo_modern.png",
]:
  try:
    r = urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=25)
    print(u, r.status, r.headers.get("Content-Type","")[:40])
  except Exception as e:
    print(u, e)
print("DONE")
PY