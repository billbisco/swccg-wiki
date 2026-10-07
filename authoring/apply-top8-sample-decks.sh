#!/bin/bash
# Apply Retro GEMPC top8 (#3-#8) sample decks + standings links. VPS only.
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
MEDIA_STAGE=/tmp/retro-gempc-media-top8
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
cp -f "$ROOT/retro-gempc-media-top8/"*.txt "$MEDIA_STAGE/"
ls -la "$MEDIA_STAGE"
docker exec swccg_wiki mkdir -p /tmp/retro-gempc-media-top8
docker cp "$MEDIA_STAGE/." swccg_wiki:/tmp/retro-gempc-media-top8/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="GEMP import from 2026 Retro Gempc Fixed.zip (forum t=86979)" \
  --overwrite \
  /tmp/retro-gempc-media-top8
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo "== edit File description pages =="
edit "File:26RMPC Christoffel DS SYCFA.txt" "$PAGES/File_26RMPC_Christoffel_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Christoffel LS EBO.txt" "$PAGES/File_26RMPC_Christoffel_LS_EBO.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Bing DS ROps.txt" "$PAGES/File_26RMPC_Bing_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Bing LS Profit.txt" "$PAGES/File_26RMPC_Bing_LS_Profit.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Monteith DS ROps.txt" "$PAGES/File_26RMPC_Monteith_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Monteith LS Operatives.txt" "$PAGES/File_26RMPC_Monteith_LS_Operatives.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Bisco DS SYCFA.txt" "$PAGES/File_26RMPC_Bisco_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Bisco LS Operatives.txt" "$PAGES/File_26RMPC_Bisco_LS_Operatives.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Kippel DS ROps.txt" "$PAGES/File_26RMPC_Kippel_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Kippel LS TRM.txt" "$PAGES/File_26RMPC_Kippel_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Tarbox DS HD.txt" "$PAGES/File_26RMPC_Tarbox_DS_HD.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"
edit "File:26RMPC Tarbox LS HB.txt" "$PAGES/File_26RMPC_Tarbox_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip"

echo "== edit deck pages =="
edit "2026 Retro GEMPC Jeremy Christoffel DS Set Your Course For Alderaan" \
  "$PAGES/2026_Retro_GEMPC_Jeremy_Christoffel_DS_Set_Your_Course_For_Alderaan.wiki" \
  "Create: #3 Jeremy Christoffel Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Jeremy Christoffel LS Echo Base Operations" \
  "$PAGES/2026_Retro_GEMPC_Jeremy_Christoffel_LS_Echo_Base_Operations.wiki" \
  "Create: #3 Jeremy Christoffel Light EBO two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Kevin Bing DS Ralltiir Operations" \
  "$PAGES/2026_Retro_GEMPC_Kevin_Bing_DS_Ralltiir_Operations.wiki" \
  "Create: #4 Kevin Bing Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Kevin Bing LS You Can Either Profit By This..." \
  "$PAGES/2026_Retro_GEMPC_Kevin_Bing_LS_Profit.wiki" \
  "Create: #4 Kevin Bing Light Profit two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Ian Monteith DS Ralltiir Operations" \
  "$PAGES/2026_Retro_GEMPC_Ian_Monteith_DS_Ralltiir_Operations.wiki" \
  "Create: #5 Ian Monteith Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Ian Monteith LS Local Uprising" \
  "$PAGES/2026_Retro_GEMPC_Ian_Monteith_LS_Local_Uprising.wiki" \
  "Create: #5 Ian Monteith Light Local Uprising two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Bill Bisco DS Set Your Course For Alderaan" \
  "$PAGES/2026_Retro_GEMPC_Bill_Bisco_DS_Set_Your_Course_For_Alderaan.wiki" \
  "Create: #6 Bill Bisco Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Bill Bisco LS Local Uprising" \
  "$PAGES/2026_Retro_GEMPC_Bill_Bisco_LS_Local_Uprising.wiki" \
  "Create: #6 Bill Bisco Light Local Uprising two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Brad Kippel DS Ralltiir Operations" \
  "$PAGES/2026_Retro_GEMPC_Brad_Kippel_DS_Ralltiir_Operations.wiki" \
  "Create: #7 Brad Kippel Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Brad Kippel LS Throne Room Mains" \
  "$PAGES/2026_Retro_GEMPC_Brad_Kippel_LS_Throne_Room_Mains.wiki" \
  "Create: #7 Brad Kippel Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Will Tarbox DS Hunt Down And Destroy The Jedi" \
  "$PAGES/2026_Retro_GEMPC_Will_Tarbox_DS_Hunt_Down_And_Destroy_The_Jedi.wiki" \
  "Create: #8 Will Tarbox Dark Hunt Down two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Will Tarbox LS Hidden Base" \
  "$PAGES/2026_Retro_GEMPC_Will_Tarbox_LS_Hidden_Base.wiki" \
  "Create: #8 Will Tarbox Light Hidden Base two-column from GEMP Fixed zip"

echo "== edit championship + player stubs =="
edit "2026 Retro GEMP Match Play Championship (Premiere to DSII)" \
  "$PAGES/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki" \
  "Standings #3-#8 Dark/Light cells link to sample deck pages; no Decklists section"

edit "Jeremy Christoffel" "$PAGES/Jeremy_Christoffel.wiki" "Link #3 SYCFA + EBO sample decklists"
edit "Kevin Bing" "$PAGES/Kevin_Bing.wiki" "Link #4 ROps + Profit sample decklists"
edit "Ian Monteith" "$PAGES/Ian_Monteith.wiki" "Link #5 ROps + Local Uprising sample decklists"
edit "Bill Bisco" "$PAGES/Bill_Bisco.wiki" "Link #6 SYCFA + Local Uprising sample decklists"
edit "Brad Kippel" "$PAGES/Brad_Kippel.wiki" "Link #7 ROps + TRM sample decklists"
edit "Will Tarbox" "$PAGES/Will_Tarbox.wiki" "Link #8 Hunt Down + Hidden Base sample decklists"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -30

echo "== purgePage =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
2026 Retro GEMPC Jeremy Christoffel DS Set Your Course For Alderaan
2026 Retro GEMPC Jeremy Christoffel LS Echo Base Operations
2026 Retro GEMPC Kevin Bing DS Ralltiir Operations
2026 Retro GEMPC Kevin Bing LS You Can Either Profit By This...
2026 Retro GEMPC Ian Monteith DS Ralltiir Operations
2026 Retro GEMPC Ian Monteith LS Local Uprising
2026 Retro GEMPC Bill Bisco DS Set Your Course For Alderaan
2026 Retro GEMPC Bill Bisco LS Local Uprising
2026 Retro GEMPC Brad Kippel DS Ralltiir Operations
2026 Retro GEMPC Brad Kippel LS Throne Room Mains
2026 Retro GEMPC Will Tarbox DS Hunt Down And Destroy The Jedi
2026 Retro GEMPC Will Tarbox LS Hidden Base
2026 Retro GEMP Match Play Championship (Premiere to DSII)
Jeremy Christoffel
Kevin Bing
Ian Monteith
Bill Bisco
Brad Kippel
Will Tarbox
File:26RMPC Christoffel DS SYCFA.txt
File:26RMPC Christoffel LS EBO.txt
File:26RMPC Bing DS ROps.txt
File:26RMPC Bing LS Profit.txt
File:26RMPC Monteith DS ROps.txt
File:26RMPC Monteith LS Operatives.txt
File:26RMPC Bisco DS SYCFA.txt
File:26RMPC Bisco LS Operatives.txt
File:26RMPC Kippel DS ROps.txt
File:26RMPC Kippel LS TRM.txt
File:26RMPC Tarbox DS HD.txt
File:26RMPC Tarbox LS HB.txt
Main Page
EOFPURGE

echo "== side-scan verify =="
python3 <<'PY'
import subprocess
checks = [
  ("2026 Retro GEMPC Jeremy Christoffel DS Set Your Course For Alderaan", "Dark"),
  ("2026 Retro GEMPC Jeremy Christoffel LS Echo Base Operations", "Light"),
  ("2026 Retro GEMPC Kevin Bing DS Ralltiir Operations", "Dark"),
  ("2026 Retro GEMPC Kevin Bing LS You Can Either Profit By This...", "Light"),
  ("2026 Retro GEMPC Ian Monteith DS Ralltiir Operations", "Dark"),
  ("2026 Retro GEMPC Ian Monteith LS Local Uprising", "Light"),
  ("2026 Retro GEMPC Bill Bisco DS Set Your Course For Alderaan", "Dark"),
  ("2026 Retro GEMPC Bill Bisco LS Local Uprising", "Light"),
  ("2026 Retro GEMPC Brad Kippel DS Ralltiir Operations", "Dark"),
  ("2026 Retro GEMPC Brad Kippel LS Throne Room Mains", "Light"),
  ("2026 Retro GEMPC Will Tarbox DS Hunt Down And Destroy The Jedi", "Dark"),
  ("2026 Retro GEMPC Will Tarbox LS Hidden Base", "Light"),
]
for title, side in checks:
    text = subprocess.check_output(
        ["docker", "exec", "swccg_wiki", "php", "maintenance/run.php", "getText", title],
        text=True, errors="replace")
    L = text.count("-L-"); D = text.count("-D-")
    dark = text.count("(Dark)")
    print(f"{title}: side={side} L={L} D={D} (Dark)={dark}")
    if side == "Dark" and L:
        raise SystemExit(f"FAIL -L- on Dark: {title}")
    if side == "Light" and (D or dark):
        raise SystemExit(f"FAIL Dark art/paren on Light: {title}")
print("side-scan OK")
PY

echo "== championship cells verify =="
docker exec swccg_wiki php maintenance/run.php getText "2026 Retro GEMP Match Play Championship (Premiere to DSII)" \
  | python3 -c "import sys; t=sys.stdin.read();
assert '== Decklists ==' not in t
for s in ['Jeremy Christoffel DS Set Your Course','Kevin Bing DS Ralltiir','Ian Monteith LS Local','Bill Bisco DS Set Your','Brad Kippel LS Throne','Will Tarbox DS Hunt Down']:
  assert s in t, s
print('championship links OK; no Decklists section')"

echo top8-sample-decks applied
