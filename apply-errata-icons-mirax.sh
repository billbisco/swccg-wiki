#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/errata-icons-mirax-gifs

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

echo "== importImages Desperate Times Decipher archive Original =="
mkdir -p "$STAGE"
ARCHIVES=(Ref3-L-desperatetimes-decipher-archive.gif)
for f in "${ARCHIVES[@]}"; do
  src="$ROOT/set-card-art/$f"
  if [ ! -f "$src" ]; then echo "MISSING $src" >&2; exit 1; fi
  cp -f "$src" "$STAGE/$f"
done
docker exec swccg_wiki mkdir -p /tmp/errata-icons-mirax-gifs
docker cp "$STAGE/." swccg_wiki:/tmp/errata-icons-mirax-gifs/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Decipher.com Reflections III cardlists face archive (Wayback JPG→GIF); cropped flush to black border; Errata hub Original column (Desperate Times Episode I icon)" \
  --overwrite \
  /tmp/errata-icons-mirax-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "importImages overwrite failed; retry without overwrite"
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="Decipher.com Reflections III cardlists face archive (Wayback); Errata hub Original (Desperate Times)" \
    /tmp/errata-icons-mirax-gifs || true
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

# Byte-identical check: Holotable Errata must not have been staged
if [ -f "$STAGE/Ref3-L-desperatetimes.gif" ]; then
  echo "ERROR: Holotable Errata GIF was staged — abort" >&2
  exit 1
fi

edit "Desperate Times (Original)" "$PAGES/Desperate_Times_(Original).wiki" \
  "New: Reflections III Decipher cardlists face with Episode I icon; Gloss Supp sibling"
edit "Desperate Times (Errata)" "$PAGES/Desperate_Times_(Errata).wiki" \
  "New: Glossary Supplement Episode I icon stricken; card_uid 13_13-DE"
edit "Desperate Times" "$PAGES/Desperate_Times.wiki" \
  "Default=Gloss Supp Episode I stricken; hatnotes/printings to Original+Errata; Errata hub"
edit "Mirax Terrik" "$PAGES/Mirax_Terrik.wiki" \
  "Notes: Gloss Supp foil deploy-should-be-2; Errata hub row deferred pending verified misprint photo"
edit "Errata" "$PAGES/Errata.wiki" \
  "Add Desperate Times (Gloss Supp Jan 2002 Episode I icon stricken); Original 353px / Errata 350px"

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
  "Desperate Times" "Desperate Times (Original)" "Desperate Times (Errata)" \
  "Mirax Terrik" \
  "File:Ref3-L-desperatetimes-decipher-archive.gif" \
  "File:Ref3-L-desperatetimes.gif"
do
  purge "$t"
done

echo "== done icons-mirax (Desperate Times live; Docking/Mirax hub skipped) =="
