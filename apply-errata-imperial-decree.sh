#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/errata-imperial-decree-gifs

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

echo "== SAFETY: refuse to import Holotable CC-D-imperialdecree.gif =="
# Only archive in STAGE
mkdir -p "$STAGE"
rm -f "$STAGE"/*
ARCHIVE=CC-D-imperialdecree-decipher-archive.gif
src="$ROOT/set-card-art/$ARCHIVE"
if [ ! -f "$src" ]; then echo "MISSING $src" >&2; exit 1; fi
# Stage ONLY the archive. Holotable may already exist under set-card-art from prior
# wiki art sync — that is fine; we never copy/import it.
cp -f "$src" "$STAGE/$ARCHIVE"
# Explicitly ensure Holotable is not in STAGE even if present on disk
rm -f "$STAGE/CC-D-imperialdecree.gif"
# Double-check STAGE contents
ls -la "$STAGE"
if ls "$STAGE"/CC-D-imperialdecree.gif >/dev/null 2>&1; then
  echo "REFUSING: Holotable gif in STAGE" >&2
  exit 1
fi
n=$(find "$STAGE" -maxdepth 1 -type f -name '*.gif' | wc -l)
if [ "$n" -ne 1 ]; then
  echo "REFUSING: expected exactly 1 gif in STAGE, got $n" >&2
  exit 1
fi

echo "== importImages Imperial Decree Decipher archive ONLY =="
docker exec swccg_wiki mkdir -p /tmp/errata-imperial-decree-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/errata-imperial-decree-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/errata-imperial-decree-gifs/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com Cloud City Dark face archive (Wayback 2001-08); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Imperial Decree). DO NOT touch Holotable CC-D-imperialdecree.gif." \
  --overwrite \
  /tmp/errata-imperial-decree-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com Cloud City Dark face archive (Wayback 2001-08); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Imperial Decree). DO NOT touch Holotable CC-D-imperialdecree.gif." \
    /tmp/errata-imperial-decree-gifs || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Imperial Decree (Original)" "$PAGES/Imperial_Decree_(Original).wiki" \
  "New: printed Cloud City face (…Force drain bonuses everywhere are ignored.); Gloss Supp sibling"
edit "Imperial Decree (Errata)" "$PAGES/Imperial_Decree_(Errata).wiki" \
  "New: Gloss Supp last-part Force drain bonuses canceled; card_uid 5_120-DE"
edit "Imperial Decree" "$PAGES/Imperial_Decree.wiki" \
  "Default=Gloss Supp wording; hatnotes/printings to Original+Errata; Errata hub"
edit "Errata" "$PAGES/Errata.wiki" \
  "Add Imperial Decree row (Gloss Supp 29 Jan 2002); Original 353px / Errata 350px; Holotable untouched"

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
purge "Imperial Decree"
purge "Imperial Decree (Original)"
purge "Imperial Decree (Errata)"
purge "File:CC-D-imperialdecree-decipher-archive.gif"
# Do NOT purge Holotable as a re-import; optional purge of page cache only is fine
purge "File:CC-D-imperialdecree.gif"

echo "== DONE errata-imperial-decree (archive only; Holotable untouched) =="
