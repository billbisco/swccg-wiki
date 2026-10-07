#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/errata-innocent-scoundrel-gifs

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

echo "== SAFETY: refuse Holotable CC-L-innocentscoundrel.gif =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
ARCHIVE=CC-L-innocentscoundrel-decipher-archive.gif
src="$ROOT/set-card-art/$ARCHIVE"
if [ ! -f "$src" ]; then echo "MISSING $src" >&2; exit 1; fi
cp -f "$src" "$STAGE/$ARCHIVE"
rm -f "$STAGE/CC-L-innocentscoundrel.gif"
ls -la "$STAGE"
if ls "$STAGE"/CC-L-innocentscoundrel.gif >/dev/null 2>&1; then
  echo "REFUSING: Holotable gif in STAGE" >&2
  exit 1
fi
n=$(find "$STAGE" -maxdepth 1 -type f -name '*.gif' | wc -l)
if [ "$n" -ne 1 ]; then
  echo "REFUSING: expected exactly 1 gif in STAGE, got $n" >&2
  exit 1
fi

echo "== importImages Innocent Scoundrel Decipher archive ONLY =="
docker exec swccg_wiki mkdir -p /tmp/errata-innocent-scoundrel-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/errata-innocent-scoundrel-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/errata-innocent-scoundrel-gifs/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com Cloud City Light face archive (Wayback 2001-08-28); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Innocent Scoundrel). DO NOT touch Holotable CC-L-innocentscoundrel.gif." \
  --overwrite \
  /tmp/errata-innocent-scoundrel-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com Cloud City Light face archive (Wayback 2001-08-28); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Innocent Scoundrel). DO NOT touch Holotable CC-L-innocentscoundrel.gif." \
    /tmp/errata-innocent-scoundrel-gifs || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Innocent Scoundrel (Original)" "$PAGES/Innocent_Scoundrel_(Original).wiki" \
  "New: printed Cloud City face (title without •); Gloss Supp sibling"
edit "Innocent Scoundrel (Errata)" "$PAGES/Innocent_Scoundrel_(Errata).wiki" \
  "New: Gloss Supp Erratum unique (•); card_uid 5_53-DE"
edit "Innocent Scoundrel" "$PAGES/Innocent_Scoundrel.wiki" \
  "Default=Gloss Supp unique (•); hatnotes/printings to Original+Errata; Errata hub"
edit "Errata" "$PAGES/Errata.wiki" \
  "Add Innocent Scoundrel row (Gloss Supp 29 Jan 2002); Original 353px / Errata 350px; Holotable untouched"

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
purge "Innocent Scoundrel"
purge "Innocent Scoundrel (Original)"
purge "Innocent Scoundrel (Errata)"
purge "File:CC-L-innocentscoundrel-decipher-archive.gif"
purge "File:CC-L-innocentscoundrel.gif"

echo "== DONE errata-innocent-scoundrel (archive only; Holotable untouched) =="
