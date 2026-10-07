#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/uniqueness-archive-gifs

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

echo "== importImages uniqueness Original archive faces =="
mkdir -p "$STAGE"
for f in Premiere-D-limitedresources-decipher-archive.gif \
         Premiere-L-berustew-decipher-archive.gif \
         Premiere-L-spaceportspeeders-decipher-archive.gif; do
  src="$ROOT/set-card-art/$f"
  if [ ! -f "$src" ]; then echo "MISSING $src" >&2; exit 1; fi
  cp -f "$src" "$STAGE/$f"
done
docker exec swccg_wiki mkdir -p /tmp/uniqueness-archive-gifs
docker cp "$STAGE/." swccg_wiki:/tmp/uniqueness-archive-gifs/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com Premiere face archives (Wayback 2008-12-25); Original printed titles without uniqueness/restriction bullets" \
  --overwrite \
  /tmp/uniqueness-archive-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com Premiere face archives (Wayback 2008-12-25); Original printed titles without uniqueness/restriction bullets" \
    /tmp/uniqueness-archive-gifs || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Limited Resources (Original)" "$PAGES/Limited_Resources_(Original).wiki" \
  "New: printed Premiere face (no •); Glossary 1998 uniqueness Errata sibling"
edit "Limited Resources (Errata)" "$PAGES/Limited_Resources_(Errata).wiki" \
  "New: •Limited Resources unique; Glossary 1998; card_uid 1_255-DE"
edit "Limited Resources" "$PAGES/Limited_Resources.wiki" \
  "Default=Gloss 1998 unique; hatnotes to Original/Errata; Errata hub"

edit "Beru Stew (Original)" "$PAGES/Beru_Stew_(Original).wiki" \
  "New: printed Premiere face (no •); Glossary 1998 uniqueness Errata sibling"
edit "Beru Stew (Errata)" "$PAGES/Beru_Stew_(Errata).wiki" \
  "New: •Beru Stew unique; Glossary 1998; card_uid 1_72-DE"
edit "Beru Stew" "$PAGES/Beru_Stew.wiki" \
  "Default=Gloss 1998 unique; hatnotes to Original/Errata; Errata hub"

edit "Spaceport Speeders (Original)" "$PAGES/Spaceport_Speeders_(Original).wiki" \
  "New: printed Premiere face (no •••); Gloss Supp restriction Errata sibling"
edit "Spaceport Speeders (Errata)" "$PAGES/Spaceport_Speeders_(Errata).wiki" \
  "New: •••Spaceport Speeders restricted; Gloss Supp; card_uid 1_112-DE"
edit "Spaceport Speeders" "$PAGES/Spaceport_Speeders.wiki" \
  "Default=Gloss Supp •••; hatnotes to Original/Errata; Errata hub"

edit "Errata" "$PAGES/Errata.wiki" \
  "Add Limited Resources/Beru Stew [2] Gloss 1998 + Spaceport Speeders [1] Gloss Supp; equal faces; cites beside Errata"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

purge() {
  echo "purge $1"
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null \
    || true
}
for t in Errata \
  "Limited Resources" "Limited Resources (Original)" "Limited Resources (Errata)" \
  "Beru Stew" "Beru Stew (Original)" "Beru Stew (Errata)" \
  "Spaceport Speeders" "Spaceport Speeders (Original)" "Spaceport Speeders (Errata)"; do
  purge "$t"
done
echo "== DONE =="
