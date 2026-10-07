#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/errata-gloss98-remain-gifs

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

echo "== importImages Glossary 1998 remain face-delta Decipher archive faces =="
mkdir -p "$STAGE"
ARCHIVES=(
  ANH-D-advosze-decipher-archive.gif
  Premiere-L-electrobinoculars-decipher-archive.gif
  Hoth-D-idjustassoonkissawookiee-decipher-archive.gif
  Hoth-L-itcanwait-decipher-archive.gif
  Premiere-L-wioslea-decipher-archive.gif
  Hoth-D-responsibilityofcommand-decipher-archive.gif
  Hoth-D-atatcannon-decipher-archive.gif
  Hoth-L-mediumrepeatingblastercannon-decipher-archive.gif
)
for f in "${ARCHIVES[@]}"; do
  src="$ROOT/set-card-art/$f"
  if [ ! -f "$src" ]; then echo "MISSING $src" >&2; exit 1; fi
  cp -f "$src" "$STAGE/$f"
done
docker exec swccg_wiki mkdir -p /tmp/errata-gloss98-remain-gifs
docker cp "$STAGE/." swccg_wiki:/tmp/errata-gloss98-remain-gifs/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com cardlists face archives (Wayback); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Advosze / Electrobinoculars / I'd Just As Soon Kiss A Wookiee / It Can Wait / Wioslea / Responsibility Of Command / AT-AT Cannon / Medium Repeating Blaster Cannon)" \
  --overwrite \
  /tmp/errata-gloss98-remain-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com cardlists face archives (Wayback); cropped flush to black border, exterior corner pads bleached #FFFFFF; Errata hub Original column (Glossary 1998 remain batch)" \
    /tmp/errata-gloss98-remain-gifs || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit_card() {
  local title="$1" base="$2"
  edit "$title (Original)" "$PAGES/${base}_(Original).wiki" \
    "New: Decipher cardlists archive face; Glossary 1998 Errata sibling"
  edit "$title (Errata)" "$PAGES/${base}_(Errata).wiki" \
    "New: Glossary Version 2.0 Errata text"
  edit "$title" "$PAGES/${base}.wiki" \
    "Default=Glossary Version 2.0 Errata wording; hatnotes/printings to Original+Errata; Errata hub"
}

edit_card "Advosze" "Advosze"
edit_card "Electrobinoculars" "Electrobinoculars"
# apostrophe titles: files use I'd_
edit "I'd Just As Soon Kiss A Wookiee (Original)" "$PAGES/I'd_Just_As_Soon_Kiss_A_Wookiee_(Original).wiki" \
  "New: Hoth printed Decipher cardlists face; Glossary 1998 sibling"
edit "I'd Just As Soon Kiss A Wookiee (Errata)" "$PAGES/I'd_Just_As_Soon_Kiss_A_Wookiee_(Errata).wiki" \
  "New: Glossary Version 2.0 Errata text; card_uid 3_127-DE"
edit "I'd Just As Soon Kiss A Wookiee" "$PAGES/I'd_Just_As_Soon_Kiss_A_Wookiee.wiki" \
  "Default=Glossary Version 2.0 Errata wording; hatnotes/printings to Original+Errata; Errata hub"

edit_card "It Can Wait" "It_Can_Wait"
edit_card "Wioslea" "Wioslea"
edit_card "Responsibility Of Command" "Responsibility_Of_Command"
edit_card "AT-AT Cannon" "AT-AT_Cannon"
edit_card "Medium Repeating Blaster Cannon" "Medium_Repeating_Blaster_Cannon"

edit "Errata" "$PAGES/Errata.wiki" \
  "Add Advosze, Electrobinoculars, I'd Just As Soon Kiss A Wookiee, It Can Wait, Wioslea, Responsibility Of Command, AT-AT Cannon, Medium Repeating Blaster Cannon (Glossary Version 2.0 Nov 1998); Original 353px / Errata 350px"

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
  "Advosze" "Advosze (Original)" "Advosze (Errata)" \
  "Electrobinoculars" "Electrobinoculars (Original)" "Electrobinoculars (Errata)" \
  "I'd Just As Soon Kiss A Wookiee" "I'd Just As Soon Kiss A Wookiee (Original)" "I'd Just As Soon Kiss A Wookiee (Errata)" \
  "It Can Wait" "It Can Wait (Original)" "It Can Wait (Errata)" \
  "Wioslea" "Wioslea (Original)" "Wioslea (Errata)" \
  "Responsibility Of Command" "Responsibility Of Command (Original)" "Responsibility Of Command (Errata)" \
  "AT-AT Cannon" "AT-AT Cannon (Original)" "AT-AT Cannon (Errata)" \
  "Medium Repeating Blaster Cannon" "Medium Repeating Blaster Cannon (Original)" "Medium Repeating Blaster Cannon (Errata)"
do
  purge "$t"
done
for f in "${ARCHIVES[@]}"; do
  purge "File:$f"
done

echo "== DONE errata-gloss98-remain =="
