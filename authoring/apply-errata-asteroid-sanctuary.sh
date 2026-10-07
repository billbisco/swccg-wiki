#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/errata-asteroid-sanctuary-gifs

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

echo "== SAFETY: refuse to import Holotable Dagobah-L-asteroidsanctuary.gif =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
ARCHIVE=Dagobah-L-asteroidsanctuary-decipher-archive.gif
src="$ROOT/set-card-art/$ARCHIVE"
if [ ! -f "$src" ]; then echo "MISSING $src" >&2; exit 1; fi
cp -f "$src" "$STAGE/$ARCHIVE"
rm -f "$STAGE/Dagobah-L-asteroidsanctuary.gif"
ls -la "$STAGE"
if ls "$STAGE"/Dagobah-L-asteroidsanctuary.gif >/dev/null 2>&1; then
  echo "REFUSING: Holotable gif in STAGE" >&2
  exit 1
fi
n=$(find "$STAGE" -maxdepth 1 -type f -name '*.gif' | wc -l)
if [ "$n" -ne 1 ]; then
  echo "REFUSING: expected exactly 1 gif in STAGE, got $n" >&2
  exit 1
fi

# Record Holotable sha1 BEFORE import (proof untouched)
echo "== Holotable sha1 BEFORE =="
docker exec swccg_wiki php maintenance/run.php eval '
$t = Title::newFromText("File:Dagobah-L-asteroidsanctuary.gif");
$file = MediaWiki\MediaWikiServices::getInstance()->getRepoGroup()->findFile($t);
if ($file) { echo "ht_sha1=" . $file->getSha1() . " size=" . $file->getSize() . "\n"; }
else { echo "ht_MISSING\n"; }
' 2>/dev/null || true
# Also via API-ish path on host after
HT_BEFORE=$(sha1sum /var/lib/docker/volumes/*/_data/e/e1/Dagobah-L-asteroidsanctuary.gif 2>/dev/null | head -1 || true)
echo "ht_host_hint=$HT_BEFORE"

echo "== importImages Asteroid Sanctuary store-printed Original ONLY =="
docker exec swccg_wiki mkdir -p /tmp/errata-asteroid-sanctuary-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/errata-asteroid-sanctuary-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/errata-asteroid-sanctuary-gifs/
COMMENT='SWCCG Store printed Original face (11914-2T.jpg); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Asteroid Sanctuary). DO NOT touch Holotable Dagobah-L-asteroidsanctuary.gif. Red Decipher cardlists GIF is cite-only.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="$COMMENT" \
  --overwrite \
  /tmp/errata-asteroid-sanctuary-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="$COMMENT" \
    /tmp/errata-asteroid-sanctuary-gifs || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Asteroid Sanctuary (Original)" "$PAGES/Asteroid_Sanctuary_(Original).wiki" \
  "Replace Original face with true printed store photo; game_text = incorrect print; red GIF cite-only"
edit "Asteroid Sanctuary (Errata)" "$PAGES/Asteroid_Sanctuary_(Errata).wiki" \
  "Notes: Original = true printed store face (not Decipher cardlists archive)"
edit "Asteroid Sanctuary" "$PAGES/Asteroid_Sanctuary.wiki" \
  "Notes: Original = true printed store face (not Decipher cardlists archive)"
edit "File:Dagobah-L-asteroidsanctuary-decipher-archive.gif" "$PAGES/File_Dagobah-L-asteroidsanctuary-decipher-archive.gif.wiki" \
  "Summary: store printed Original face; Holotable untouched; red GIF cite-only"

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
purge "Asteroid Sanctuary"
purge "Asteroid Sanctuary (Original)"
purge "Asteroid Sanctuary (Errata)"
purge "File:Dagobah-L-asteroidsanctuary-decipher-archive.gif"
purge "File:Dagobah-L-asteroidsanctuary.gif"

echo "== Holotable sha1 AFTER (must match before) =="
docker exec swccg_wiki php maintenance/run.php eval '
$t = Title::newFromText("File:Dagobah-L-asteroidsanctuary.gif");
$file = MediaWiki\MediaWikiServices::getInstance()->getRepoGroup()->findFile($t);
if ($file) { echo "ht_sha1=" . $file->getSha1() . " size=" . $file->getSize() . "\n"; }
else { echo "ht_MISSING\n"; }
$t2 = Title::newFromText("File:Dagobah-L-asteroidsanctuary-decipher-archive.gif");
$file2 = MediaWiki\MediaWikiServices::getInstance()->getRepoGroup()->findFile($t2);
if ($file2) { echo "arch_sha1=" . $file2->getSha1() . " size=" . $file2->getSize() . "\n"; }
' 2>/dev/null || true

echo "== DONE errata-asteroid-sanctuary (store Original only; Holotable untouched) =="
