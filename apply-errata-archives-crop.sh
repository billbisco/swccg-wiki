#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
IMG_DIR="$ROOT/set-card-art"
STAGE=$(mktemp -d)

ARCHIVES=(
  CC-D-projectivetelepathy-decipher-archive.gif
  ANH-L-attackrun-decipher-archive.gif
  Premiere-D-limitedresources-decipher-archive.gif
  Premiere-L-berustew-decipher-archive.gif
  Premiere-L-spaceportspeeders-decipher-archive.gif
)

echo "== importImages: 5 cropped Decipher archive faces =="
for f in "${ARCHIVES[@]}"; do
  if [ ! -f "$IMG_DIR/$f" ]; then
    echo "MISSING $IMG_DIR/$f" >&2
    exit 1
  fi
  cp -f "$IMG_DIR/$f" "$STAGE/$f"
done
docker exec swccg_wiki mkdir -p /tmp/errata-archives-crop
docker cp "$STAGE/." swccg_wiki:/tmp/errata-archives-crop/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Crop white pad/drop-shadow from Decipher archive faces; flush to black card border for Errata hub 350px columns" \
  --overwrite \
  /tmp/errata-archives-crop
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Crop white pad/drop-shadow from Decipher archive faces; flush to black card border for Errata hub 350px columns" \
    /tmp/errata-archives-crop || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
rm -rf "$STAGE"

echo "== edit Errata page (both columns 350px) =="
python3 - "$PAGES/Errata.wiki" <<'PY'
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
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Errata hub: crop Decipher archives flush to black border; both Original and Errata columns at 350px; update caption" \
  "Errata" < "$PAGES/Errata.wiki"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

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

echo "== DONE errata-archives-crop =="
