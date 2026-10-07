#!/bin/bash
# Apply Retro GEMPC decklist normalize + Timo LS + Jonny Chu DS/LS. VPS only.
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
MEDIA_STAGE=/tmp/retro-gempc-media
cd "$ROOT"

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
  if [ ! -s "$file" ]; then echo "ERROR: missing $file" >&2; exit 1; fi
  strip_bom "$file"
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

echo "== importImages GEMP txt =="
rm -rf "$MEDIA_STAGE"
mkdir -p "$MEDIA_STAGE"
cp -f "$ROOT/retro-gempc-media/"*.txt "$MEDIA_STAGE/"
ls -la "$MEDIA_STAGE"
docker exec swccg_wiki mkdir -p /tmp/retro-gempc-media
docker cp "$MEDIA_STAGE/." swccg_wiki:/tmp/retro-gempc-media/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="GEMP import from 2026 Retro Gempc Fixed.zip (forum t=86979)" \
  --overwrite \
  /tmp/retro-gempc-media
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo "== edit File description pages =="
edit "File:26RMPC Dusel LS HB.txt" "$PAGES/File_26RMPC_Dusel_LS_HB.txt.wiki" \
  "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC JChu DS ROps.txt" "$PAGES/File_26RMPC_JChu_DS_ROps.txt.wiki" \
  "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC JChu LS TRM.txt" "$PAGES/File_26RMPC_JChu_LS_TRM.txt.wiki" \
  "GEMP import summary: 2026 Retro Gempc Fixed.zip"

echo "== edit deck + hub pages =="
edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations" \
  "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations.wiki" \
  "Canonical two-column decklist (standard layout); companion LS link"

edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)" \
  "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations_(two-column_layout).wiki" \
  "Redirect to bare canonical title; two-column is now the standard"

edit "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)" \
  "$PAGES/2026_Retro_GEMPC_Timo_Dusel_DS_Ralltiir_Operations_(picture_layout).wiki" \
  "Redirect to bare canonical title; remove alternate layout"

edit "2026 Retro GEMPC Timo Dusel LS Hidden Base" \
  "$PAGES/2026_Retro_GEMPC_Timo_Dusel_LS_Hidden_Base.wiki" \
  "Create: Timo #1 Light Hidden Base two-column decklist from GEMP Fixed zip"

edit "2026 Retro GEMPC Jonny Chu DS Ralltiir Operations" \
  "$PAGES/2026_Retro_GEMPC_Jonny_Chu_DS_Ralltiir_Operations.wiki" \
  "Create: Jonny Chu #2 Dark ROps two-column decklist from GEMP Fixed zip"

edit "2026 Retro GEMPC Jonny Chu LS Throne Room Mains" \
  "$PAGES/2026_Retro_GEMPC_Jonny_Chu_LS_Throne_Room_Mains.wiki" \
  "Create: Jonny Chu #2 Light TRM (Throne Room Mains) two-column from GEMP Fixed zip"

edit "2026 Retro GEMP Match Play Championship (Premiere to DSII)" \
  "$PAGES/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki" \
  "Decklists: canonical bare titles for Timo DS+LS and Jonny Chu DS+LS; drop layout alternates"

edit "Timo Dusel" \
  "$PAGES/Timo_Dusel.wiki" \
  "Link canonical DS ROps + LS Hidden Base decklists"

edit "Jonny Chu" \
  "$PAGES/Jonny_Chu.wiki" \
  "Link canonical DS ROps + LS Throne Room Mains (TRM) decklists"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20

echo "== purgePage =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
2026 Retro GEMPC Timo Dusel DS Ralltiir Operations
2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)
2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)
2026 Retro GEMPC Timo Dusel LS Hidden Base
2026 Retro GEMPC Jonny Chu DS Ralltiir Operations
2026 Retro GEMPC Jonny Chu LS Throne Room Mains
2026 Retro GEMP Match Play Championship (Premiere to DSII)
Timo Dusel
Jonny Chu
File:26RMPC Dusel LS HB.txt
File:26RMPC JChu DS ROps.txt
File:26RMPC JChu LS TRM.txt
Main Page
EOFPURGE

echo "== side-scan verify =="
python3 <<'PY'
import subprocess
checks = [
  ("2026 Retro GEMPC Timo Dusel DS Ralltiir Operations", "Dark"),
  ("2026 Retro GEMPC Timo Dusel LS Hidden Base", "Light"),
  ("2026 Retro GEMPC Jonny Chu DS Ralltiir Operations", "Dark"),
  ("2026 Retro GEMPC Jonny Chu LS Throne Room Mains", "Light"),
]
for title, side in checks:
    text = subprocess.check_output(
        ["docker", "exec", "swccg_wiki", "php", "maintenance/run.php", "getText", title],
        text=True, errors="replace")
    L = text.count("-L-"); D = text.count("-D-")
    dark = text.count("(Dark)")
    print(f"{title}: side={side} L={L} D={D} (Dark)={dark} redirect={'#REDIRECT' in text[:80]}")
    if side == "Dark" and L:
        raise SystemExit(f"FAIL -L- on Dark: {title}")
    if side == "Light" and (D or dark):
        raise SystemExit(f"FAIL Dark art/paren on Light: {title}")
print("side-scan OK")
PY

echo "== redirect verify =="
for t in \
  "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (two-column layout)" \
  "2026 Retro GEMPC Timo Dusel DS Ralltiir Operations (picture layout)"
do
  echo "---- $t ----"
  docker exec swccg_wiki php maintenance/run.php getText "$t" | head -3
done

echo retro-gempc-decks applied
