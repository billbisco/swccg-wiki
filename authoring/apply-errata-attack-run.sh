#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
IMG_SRC="$ROOT/set-card-art/ANH-L-attackrun-decipher-archive.gif"
STAGE=/tmp/ar-archive-gif

strip_bom() {
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

edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

echo "== importImages Attack Run Decipher archive face =="
if [ ! -f "$IMG_SRC" ]; then
  echo "MISSING image $IMG_SRC" >&2
  exit 1
fi
mkdir -p "$STAGE"
cp -f "$IMG_SRC" "$STAGE/ANH-L-attackrun-decipher-archive.gif"
docker exec swccg_wiki mkdir -p /tmp/ar-archive-gif
docker cp "$STAGE/." swccg_wiki:/tmp/ar-archive-gif/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com A New Hope Light face archive (Wayback 2008-12-25); printed Original Attack Run" \
  --overwrite \
  /tmp/ar-archive-gif
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com A New Hope Light face archive (Wayback 2008-12-25); printed Original Attack Run" \
    /tmp/ar-archive-gif || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Attack Run (Original)" "$PAGES/Attack_Run_(Original).wiki" \
  "New: printed ANH face (*Immune to Overload during Attack Run.); Decipher archive GIF"

edit "Attack Run (Errata)" "$PAGES/Attack_Run_(Errata).wiki" \
  "New: Gloss Supp last-line Proton Torpedoes immunity; card_uid 2_42-DE"

edit "Attack Run" "$PAGES/Attack_Run.wiki" \
  "Default=Gloss Supp wording; hatnotes/printings to Original+Errata; point to Errata hub"

edit "Errata" "$PAGES/Errata.wiki" \
  "Add Attack Run row; equal 350x490 faces; [1] Gloss Supp beside Errata (shared named ref)"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

purge "Errata"
purge "Attack Run"
purge "Attack Run (Original)"
purge "Attack Run (Errata)"

echo "== DONE =="
