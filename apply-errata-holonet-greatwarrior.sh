#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/errata-holonet-gw-gifs

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

echo "== importImages HoloNet + Great Warrior Decipher archive faces =="
mkdir -p "$STAGE"
for f in Dagobah-D-holonettransmission-decipher-archive.gif \
         Dagobah-L-greatwarrior-decipher-archive.gif; do
  src="$ROOT/set-card-art/$f"
  if [ ! -f "$src" ]; then echo "MISSING $src" >&2; exit 1; fi
  cp -f "$src" "$STAGE/$f"
done
docker exec swccg_wiki mkdir -p /tmp/errata-holonet-gw-gifs
docker cp "$STAGE/." swccg_wiki:/tmp/errata-holonet-gw-gifs/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com Dagobah face archives (Wayback 2001-09); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (HoloNet Transmission / Great Warrior)" \
  --overwrite \
  /tmp/errata-holonet-gw-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com Dagobah face archives (Wayback 2001-09); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (HoloNet Transmission / Great Warrior)" \
    /tmp/errata-holonet-gw-gifs || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "HoloNet Transmission (Original)" "$PAGES/HoloNet_Transmission_(Original).wiki" \
  "New: printed Dagobah Decipher cardlists face (LOST Search…Shuffle, cut and replace.); Gloss Supp sibling"
edit "HoloNet Transmission (Errata)" "$PAGES/HoloNet_Transmission_(Errata).wiki" \
  "New: Gloss Supp USED/LOST correction (white-border reprint error); card_uid 4_143-DE"
edit "HoloNet Transmission" "$PAGES/HoloNet_Transmission.wiki" \
  "Default=Gloss Supp wording; hatnotes/printings to Original+Errata; Errata hub"

edit "Great Warrior (Original)" "$PAGES/Great_Warrior_(Original).wiki" \
  "New: printed Dagobah face (…everywhere are ignored.); Gloss Supp sibling"
edit "Great Warrior (Errata)" "$PAGES/Great_Warrior_(Errata).wiki" \
  "New: Gloss Supp last-line Force drain bonuses canceled; card_uid 4_77-DE"
edit "Great Warrior" "$PAGES/Great_Warrior.wiki" \
  "Default=Gloss Supp wording; hatnotes/printings to Original+Errata; Errata hub"

edit "Errata" "$PAGES/Errata.wiki" \
  "Add HoloNet Transmission + Great Warrior rows (Gloss Supp 29 Jan 2002); Original 353px / Errata 350px"

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
purge "HoloNet Transmission"
purge "HoloNet Transmission (Original)"
purge "HoloNet Transmission (Errata)"
purge "Great Warrior"
purge "Great Warrior (Original)"
purge "Great Warrior (Errata)"
purge "File:Dagobah-D-holonettransmission-decipher-archive.gif"
purge "File:Dagobah-L-greatwarrior-decipher-archive.gif"

echo "== DONE errata-holonet-greatwarrior =="
