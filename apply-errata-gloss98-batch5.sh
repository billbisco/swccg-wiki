#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/errata-gloss98-batch5-gifs

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

echo "== importImages Glossary 1998 face-delta batch5 Decipher archive faces =="
mkdir -p "$STAGE"
ARCHIVES=(
  Dagobah-L-asteroidsanctuary-decipher-archive.gif
  Premiere-L-lukeskywalker-decipher-archive.gif
  ANH-L-lukescape-decipher-archive.gif
  Premiere-D-tallonroll-decipher-archive.gif
  ANH-L-undercover-decipher-archive.gif
)
for f in "${ARCHIVES[@]}"; do
  src="$ROOT/set-card-art/$f"
  if [ ! -f "$src" ]; then echo "MISSING $src" >&2; exit 1; fi
  cp -f "$src" "$STAGE/$f"
done
docker exec swccg_wiki mkdir -p /tmp/errata-gloss98-batch5-gifs
docker cp "$STAGE/." swccg_wiki:/tmp/errata-gloss98-batch5-gifs/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com cardlists face archives (Wayback); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Asteroid Sanctuary / Luke Skywalker / Luke's Cape / Tallon Roll / Undercover)" \
  --overwrite \
  /tmp/errata-gloss98-batch5-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com cardlists face archives (Wayback); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Asteroid Sanctuary / Luke Skywalker / Luke's Cape / Tallon Roll / Undercover)" \
    /tmp/errata-gloss98-batch5-gifs || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Asteroid Sanctuary (Original)" "$PAGES/Asteroid_Sanctuary_(Original).wiki" \
  "New: Dagobah Decipher cardlists archive face; Glossary 1998 Errata sibling (exchange note)"
edit "Asteroid Sanctuary (Errata)" "$PAGES/Asteroid_Sanctuary_(Errata).wiki" \
  "New: Glossary Version 2.0 Errata text; card_uid 4_17-DE"
edit "Asteroid Sanctuary" "$PAGES/Asteroid_Sanctuary.wiki" \
  "Default=Glossary Version 2.0 Errata wording; hatnotes/printings to Original+Errata; Errata hub"

edit "Luke Skywalker (Original)" "$PAGES/Luke_Skywalker_(Original).wiki" \
  "New: Premiere printed Decipher cardlists face (non-Tatooine location / starship); Glossary 1998 sibling"
edit "Luke Skywalker (Errata)" "$PAGES/Luke_Skywalker_(Errata).wiki" \
  "New: Glossary Version 2.0 Errata text; card_uid 1_19-DE"
edit "Luke Skywalker" "$PAGES/Luke_Skywalker.wiki" \
  "Default=Glossary Version 2.0 Errata wording; hatnotes/printings to Original+Errata; Errata hub"

edit "Luke's Cape (Original)" "$PAGES/Luke's_Cape_(Original).wiki" \
  "New: ANH printed Decipher cardlists face; Glossary 1998 sibling"
edit "Luke's Cape (Errata)" "$PAGES/Luke's_Cape_(Errata).wiki" \
  "New: Glossary Version 2.0 Errata text; card_uid 2_35-DE"
edit "Luke's Cape" "$PAGES/Luke's_Cape.wiki" \
  "Default=Glossary Version 2.0 Errata wording; hatnotes/printings to Original+Errata; Errata hub"

edit "Tallon Roll (Original)" "$PAGES/Tallon_Roll_(Original).wiki" \
  "New: Premiere printed Decipher cardlists face (one Rebel, one Imperial); Glossary 1998 sibling"
edit "Tallon Roll (Errata)" "$PAGES/Tallon_Roll_(Errata).wiki" \
  "New: Glossary Version 2.0 Errata text; card_uid 1_270-DE"
edit "Tallon Roll" "$PAGES/Tallon_Roll.wiki" \
  "Default=Glossary Version 2.0 Errata wording; hatnotes/printings to Original+Errata; Errata hub"

edit "Undercover (Original)" "$PAGES/Undercover_(Original).wiki" \
  "New: ANH printed Decipher cardlists face (no Immune to Alter); Glossary 1998 sibling"
edit "Undercover (Errata)" "$PAGES/Undercover_(Errata).wiki" \
  "New: Glossary Version 2.0 Errata text; card_uid 2_40-DE"
edit "Undercover" "$PAGES/Undercover.wiki" \
  "Default=Glossary Version 2.0 Errata wording; hatnotes/printings to Original+Errata; Errata hub"

edit "Errata" "$PAGES/Errata.wiki" \
  "Add Asteroid Sanctuary, Luke Skywalker, Luke's Cape, Tallon Roll, Undercover rows (Glossary Version 2.0 Nov 1998); Original 353px / Errata 350px"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20

purge() {
  local title="$1"
  echo "purge $title"
  docker exec swccg_wiki php maintenance/run.php purgePage "$title" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$title" 2>/dev/null \
    || true
}

purge "Errata"
for t in \
  "Asteroid Sanctuary" "Asteroid Sanctuary (Original)" "Asteroid Sanctuary (Errata)" \
  "Luke Skywalker" "Luke Skywalker (Original)" "Luke Skywalker (Errata)" \
  "Luke's Cape" "Luke's Cape (Original)" "Luke's Cape (Errata)" \
  "Tallon Roll" "Tallon Roll (Original)" "Tallon Roll (Errata)" \
  "Undercover" "Undercover (Original)" "Undercover (Errata)"
do
  purge "$t"
done
for f in "${ARCHIVES[@]}"; do
  purge "File:$f"
done

echo "== DONE errata-gloss98-batch5 =="
