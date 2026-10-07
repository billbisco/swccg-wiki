#!/bin/bash
# Apply Retro GEMPC remaining (#9-#50) sample decks + standings links. VPS only.
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
MEDIA_STAGE=/tmp/retro-gempc-media-remaining
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
cp -f "$ROOT/retro-gempc-media-remaining/"*.txt "$MEDIA_STAGE/"
ls "$MEDIA_STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/retro-gempc-media-remaining
docker cp "$MEDIA_STAGE/." swccg_wiki:/tmp/retro-gempc-media-remaining/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="GEMP import from 2026 Retro Gempc Fixed.zip (forum t=86979) #9-#50" \
  --overwrite \
  /tmp/retro-gempc-media-remaining
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo "== edit File description pages =="
edit "File:26RMPC Garcia DS HD.txt" "$PAGES/File_26RMPC_Garcia_DS_HD.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Garcia LS TRM.txt" "$PAGES/File_26RMPC_Garcia_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Horbey DS SYCFA.txt" "$PAGES/File_26RMPC_Horbey_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Horbey LS TRM.txt" "$PAGES/File_26RMPC_Horbey_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Coupland DS BHBM.txt" "$PAGES/File_26RMPC_Coupland_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Coupland LS HB.txt" "$PAGES/File_26RMPC_Coupland_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Prodoehl DS HD.txt" "$PAGES/File_26RMPC_Prodoehl_DS_HD.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Prodoehl LS MWYHL.txt" "$PAGES/File_26RMPC_Prodoehl_LS_MWYHL.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Bethell DS ROps.txt" "$PAGES/File_26RMPC_Bethell_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Bethell LS TIGIH.txt" "$PAGES/File_26RMPC_Bethell_LS_TIGIH.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Ford DS SYCFA.txt" "$PAGES/File_26RMPC_Ford_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Ford LS HB.txt" "$PAGES/File_26RMPC_Ford_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Larson DS ROps.txt" "$PAGES/File_26RMPC_Larson_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Larson LS TRM.txt" "$PAGES/File_26RMPC_Larson_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Madaio DS ROps.txt" "$PAGES/File_26RMPC_Madaio_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Madaio LS EBO.txt" "$PAGES/File_26RMPC_Madaio_LS_EBO.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC PJohnson DS ROps.txt" "$PAGES/File_26RMPC_PJohnson_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC PJohnson LS HB.txt" "$PAGES/File_26RMPC_PJohnson_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Halman DS BHBM.txt" "$PAGES/File_26RMPC_Halman_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Halman LS TRM.txt" "$PAGES/File_26RMPC_Halman_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Petersson DS HD.txt" "$PAGES/File_26RMPC_Petersson_DS_HD.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Petersson LS HB.txt" "$PAGES/File_26RMPC_Petersson_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Hickey DS SYCFA.txt" "$PAGES/File_26RMPC_Hickey_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Hickey LS Profit.txt" "$PAGES/File_26RMPC_Hickey_LS_Profit.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Simpson DS Court.txt" "$PAGES/File_26RMPC_Simpson_DS_Court.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Simpson LS Operatives.txt" "$PAGES/File_26RMPC_Simpson_LS_Operatives.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Anderson DS SYCFA.txt" "$PAGES/File_26RMPC_Anderson_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Anderson LS HB.txt" "$PAGES/File_26RMPC_Anderson_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Lindstrom DS Court.txt" "$PAGES/File_26RMPC_Lindstrom_DS_Court.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Lindstrom LS MBO.txt" "$PAGES/File_26RMPC_Lindstrom_LS_MBO.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Mikulka DS ISB.txt" "$PAGES/File_26RMPC_Mikulka_DS_ISB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Mikulka LS TIGIH.txt" "$PAGES/File_26RMPC_Mikulka_LS_TIGIH.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Waldron DS SYCFA.txt" "$PAGES/File_26RMPC_Waldron_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Waldron LS HB.txt" "$PAGES/File_26RMPC_Waldron_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Ja McBride DS BHBM.txt" "$PAGES/File_26RMPC_Ja_McBride_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Ja McBride LS TRM.txt" "$PAGES/File_26RMPC_Ja_McBride_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Wargo DS BHBM.txt" "$PAGES/File_26RMPC_Wargo_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Wargo LS MWYHL.txt" "$PAGES/File_26RMPC_Wargo_LS_MWYHL.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Radic DS Clouds.txt" "$PAGES/File_26RMPC_Radic_DS_Clouds.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Radic LS RST.txt" "$PAGES/File_26RMPC_Radic_LS_RST.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Butler DS BHBM.txt" "$PAGES/File_26RMPC_Butler_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Butler LS TRM.txt" "$PAGES/File_26RMPC_Butler_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Clark DS ISB.txt" "$PAGES/File_26RMPC_Clark_DS_ISB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Clark LS TRM.txt" "$PAGES/File_26RMPC_Clark_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC RScott DS BHBM.txt" "$PAGES/File_26RMPC_RScott_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC RScott LS TRM.txt" "$PAGES/File_26RMPC_RScott_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Sanders DS BHBM.txt" "$PAGES/File_26RMPC_Sanders_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Sanders LS TIGIH.txt" "$PAGES/File_26RMPC_Sanders_LS_TIGIH.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Deibler DS ISB.txt" "$PAGES/File_26RMPC_Deibler_DS_ISB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Deibler LS Profit.txt" "$PAGES/File_26RMPC_Deibler_LS_Profit.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Lingrell DS HD.txt" "$PAGES/File_26RMPC_Lingrell_DS_HD.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Lingrell LS TRM.txt" "$PAGES/File_26RMPC_Lingrell_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Behm DS ROps.txt" "$PAGES/File_26RMPC_Behm_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Behm LS Profit.txt" "$PAGES/File_26RMPC_Behm_LS_Profit.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Tennyson DS ROps.txt" "$PAGES/File_26RMPC_Tennyson_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Tennyson LS TIGIH.txt" "$PAGES/File_26RMPC_Tennyson_LS_TIGIH.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Jasper DS BHBM.txt" "$PAGES/File_26RMPC_Jasper_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Jasper LS HB.txt" "$PAGES/File_26RMPC_Jasper_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Adamson DS BHBM.txt" "$PAGES/File_26RMPC_Adamson_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Adamson LS Profit.txt" "$PAGES/File_26RMPC_Adamson_LS_Profit.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Price DS ISB.txt" "$PAGES/File_26RMPC_Price_DS_ISB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Price LS RST.txt" "$PAGES/File_26RMPC_Price_LS_RST.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Heft DS Court.txt" "$PAGES/File_26RMPC_Heft_DS_Court.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Heft LS EBO.txt" "$PAGES/File_26RMPC_Heft_LS_EBO.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Gravel DS BHBM.txt" "$PAGES/File_26RMPC_Gravel_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Gravel LS HB.txt" "$PAGES/File_26RMPC_Gravel_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Perugini DS HD.txt" "$PAGES/File_26RMPC_Perugini_DS_HD.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Perugini LS TRM.txt" "$PAGES/File_26RMPC_Perugini_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Vencill DS TIEs.txt" "$PAGES/File_26RMPC_Vencill_DS_TIEs.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Vencill LS HB.txt" "$PAGES/File_26RMPC_Vencill_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Nguyen DS ROps.txt" "$PAGES/File_26RMPC_Nguyen_DS_ROps.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Nguyen LS HB.txt" "$PAGES/File_26RMPC_Nguyen_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Blackstock DS BHBM.txt" "$PAGES/File_26RMPC_Blackstock_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Blackstock LS QMC.txt" "$PAGES/File_26RMPC_Blackstock_LS_QMC.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Amore DS SYCFA.txt" "$PAGES/File_26RMPC_Amore_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Amore LS HB.txt" "$PAGES/File_26RMPC_Amore_LS_HB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Winter DS SYCFA.txt" "$PAGES/File_26RMPC_Winter_DS_SYCFA.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Winter LS Beg Canyon.txt" "$PAGES/File_26RMPC_Winter_LS_Beg_Canyon.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Parco DS ISB.txt" "$PAGES/File_26RMPC_Parco_DS_ISB.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Parco LS MWYHL.txt" "$PAGES/File_26RMPC_Parco_LS_MWYHL.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC CJohnson DS BHBM.txt" "$PAGES/File_26RMPC_CJohnson_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC CJohnson LS Profit.txt" "$PAGES/File_26RMPC_CJohnson_LS_Profit.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Ju McBride DS BHBM.txt" "$PAGES/File_26RMPC_Ju_McBride_DS_BHBM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"
edit "File:26RMPC Ju McBride LS TRM.txt" "$PAGES/File_26RMPC_Ju_McBride_LS_TRM.txt.wiki" "GEMP import summary: 2026 Retro Gempc Fixed.zip #9-#50"

echo "== edit deck pages =="
edit "2026 Retro GEMPC David Garcia DS Hunt Down And Destroy The Jedi" "$PAGES/2026_Retro_GEMPC_David_Garcia_DS_Hunt_Down_And_Destroy_The_Jedi.wiki" "Create: #9 David Garcia Dark Hunt Down two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC David Garcia LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_David_Garcia_LS_Throne_Room_Mains.wiki" "Create: #9 David Garcia Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Joe Horbey DS Set Your Course For Alderaan" "$PAGES/2026_Retro_GEMPC_Joe_Horbey_DS_Set_Your_Course_For_Alderaan.wiki" "Create: #10 Joe Horbey Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Joe Horbey LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Joe_Horbey_LS_Throne_Room_Mains.wiki" "Create: #10 Joe Horbey Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Evan Coupland DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Evan_Coupland_DS_Bring_Him_Before_Me.wiki" "Create: #11 Evan Coupland Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Evan Coupland LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Evan_Coupland_LS_Hidden_Base.wiki" "Create: #11 Evan Coupland Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Alex Prodoehl DS Hunt Down And Destroy The Jedi" "$PAGES/2026_Retro_GEMPC_Alex_Prodoehl_DS_Hunt_Down_And_Destroy_The_Jedi.wiki" "Create: #12 Alex Prodoehl Dark Hunt Down two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Alex Prodoehl LS Mind What You Have Learned" "$PAGES/2026_Retro_GEMPC_Alex_Prodoehl_LS_Mind_What_You_Have_Learned.wiki" "Create: #12 Alex Prodoehl Light MWYHL two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Andrew Bethell DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Andrew_Bethell_DS_Ralltiir_Operations.wiki" "Create: #13 Andrew Bethell Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Andrew Bethell LS There Is Good In Him" "$PAGES/2026_Retro_GEMPC_Andrew_Bethell_LS_There_Is_Good_In_Him.wiki" "Create: #13 Andrew Bethell Light TIGIH two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Matthew Ford DS Set Your Course For Alderaan" "$PAGES/2026_Retro_GEMPC_Matthew_Ford_DS_Set_Your_Course_For_Alderaan.wiki" "Create: #14 Matthew Ford Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Matthew Ford LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Matthew_Ford_LS_Hidden_Base.wiki" "Create: #14 Matthew Ford Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Garrett Larson DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Garrett_Larson_DS_Ralltiir_Operations.wiki" "Create: #15 Garrett Larson Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Garrett Larson LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Garrett_Larson_LS_Throne_Room_Mains.wiki" "Create: #15 Garrett Larson Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Chris Madaio DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Chris_Madaio_DS_Ralltiir_Operations.wiki" "Create: #16 Chris Madaio Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Chris Madaio LS Echo Base Operations" "$PAGES/2026_Retro_GEMPC_Chris_Madaio_LS_Echo_Base_Operations.wiki" "Create: #16 Chris Madaio Light EBO two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Patrick Johnson DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Patrick_Johnson_DS_Ralltiir_Operations.wiki" "Create: #17 Patrick Johnson Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Patrick Johnson LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Patrick_Johnson_LS_Hidden_Base.wiki" "Create: #17 Patrick Johnson Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Kendall Halman DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Kendall_Halman_DS_Bring_Him_Before_Me.wiki" "Create: #18 Kendall Halman Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Kendall Halman LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Kendall_Halman_LS_Throne_Room_Mains.wiki" "Create: #18 Kendall Halman Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Tony Petersson DS Hunt Down And Destroy The Jedi" "$PAGES/2026_Retro_GEMPC_Tony_Petersson_DS_Hunt_Down_And_Destroy_The_Jedi.wiki" "Create: #19 Tony Petersson Dark Hunt Down two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Tony Petersson LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Tony_Petersson_LS_Hidden_Base.wiki" "Create: #19 Tony Petersson Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Charlie Hickey DS Set Your Course For Alderaan" "$PAGES/2026_Retro_GEMPC_Charlie_Hickey_DS_Set_Your_Course_For_Alderaan.wiki" "Create: #20 Charlie Hickey Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Charlie Hickey LS You Can Either Profit By This..." "$PAGES/2026_Retro_GEMPC_Charlie_Hickey_LS_You_Can_Either_Profit_By_This....wiki" "Create: #20 Charlie Hickey Light Profit two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Matt Simpson DS Court Of The Vile Gangster" "$PAGES/2026_Retro_GEMPC_Matt_Simpson_DS_Court_Of_The_Vile_Gangster.wiki" "Create: #21 Matt Simpson Dark Court two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Matt Simpson LS Local Uprising" "$PAGES/2026_Retro_GEMPC_Matt_Simpson_LS_Local_Uprising.wiki" "Create: #21 Matt Simpson Light Local Uprising two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Jeff Anderson DS Set Your Course For Alderaan" "$PAGES/2026_Retro_GEMPC_Jeff_Anderson_DS_Set_Your_Course_For_Alderaan.wiki" "Create: #22 Jeff Anderson Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Jeff Anderson LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Jeff_Anderson_LS_Hidden_Base.wiki" "Create: #22 Jeff Anderson Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Ben Lindstrom DS Court Of The Vile Gangster" "$PAGES/2026_Retro_GEMPC_Ben_Lindstrom_DS_Court_Of_The_Vile_Gangster.wiki" "Create: #23 Ben Lindstrom Dark Court two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Ben Lindstrom LS Massassi Base Operations" "$PAGES/2026_Retro_GEMPC_Ben_Lindstrom_LS_Massassi_Base_Operations.wiki" "Create: #23 Ben Lindstrom Light MBO two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Geoffrey Mikulka DS ISB Operations" "$PAGES/2026_Retro_GEMPC_Geoffrey_Mikulka_DS_ISB_Operations.wiki" "Create: #24 Geoffrey Mikulka Dark ISB two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Geoffrey Mikulka LS There Is Good In Him" "$PAGES/2026_Retro_GEMPC_Geoffrey_Mikulka_LS_There_Is_Good_In_Him.wiki" "Create: #24 Geoffrey Mikulka Light TIGIH two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Robert Waldon DS Set Your Course For Alderaan" "$PAGES/2026_Retro_GEMPC_Robert_Waldon_DS_Set_Your_Course_For_Alderaan.wiki" "Create: #25 Robert Waldon Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Robert Waldon LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Robert_Waldon_LS_Hidden_Base.wiki" "Create: #25 Robert Waldon Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Jarrett McBride DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Jarrett_McBride_DS_Bring_Him_Before_Me.wiki" "Create: #26 Jarrett McBride Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Jarrett McBride LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Jarrett_McBride_LS_Throne_Room_Mains.wiki" "Create: #26 Jarrett McBride Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Brandon Wargo DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Brandon_Wargo_DS_Bring_Him_Before_Me.wiki" "Create: #27 Brandon Wargo Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Brandon Wargo LS Mind What You Have Learned" "$PAGES/2026_Retro_GEMPC_Brandon_Wargo_LS_Mind_What_You_Have_Learned.wiki" "Create: #27 Brandon Wargo Light MWYHL two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Adam Radic DS Imperial Occupation" "$PAGES/2026_Retro_GEMPC_Adam_Radic_DS_Imperial_Occupation.wiki" "Create: #28 Adam Radic Dark Imperial Occupation two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Adam Radic LS Rebel Strike Team" "$PAGES/2026_Retro_GEMPC_Adam_Radic_LS_Rebel_Strike_Team.wiki" "Create: #28 Adam Radic Light RST two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Michael Butler DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Michael_Butler_DS_Bring_Him_Before_Me.wiki" "Create: #29 Michael Butler Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Michael Butler LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Michael_Butler_LS_Throne_Room_Mains.wiki" "Create: #29 Michael Butler Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Phil Clark DS ISB Operations" "$PAGES/2026_Retro_GEMPC_Phil_Clark_DS_ISB_Operations.wiki" "Create: #30 Phil Clark Dark ISB two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Phil Clark LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Phil_Clark_LS_Throne_Room_Mains.wiki" "Create: #30 Phil Clark Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Randy Scott DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Randy_Scott_DS_Bring_Him_Before_Me.wiki" "Create: #31 Randy Scott Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Randy Scott LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Randy_Scott_LS_Throne_Room_Mains.wiki" "Create: #31 Randy Scott Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Steve Sanders DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Steve_Sanders_DS_Bring_Him_Before_Me.wiki" "Create: #32 Steve Sanders Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Steve Sanders LS There Is Good In Him" "$PAGES/2026_Retro_GEMPC_Steve_Sanders_LS_There_Is_Good_In_Him.wiki" "Create: #32 Steve Sanders Light TIGIH two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Christian Deibler DS ISB Operations" "$PAGES/2026_Retro_GEMPC_Christian_Deibler_DS_ISB_Operations.wiki" "Create: #33 Christian Deibler Dark ISB two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Christian Deibler LS You Can Either Profit By This..." "$PAGES/2026_Retro_GEMPC_Christian_Deibler_LS_You_Can_Either_Profit_By_This....wiki" "Create: #33 Christian Deibler Light Profit two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Scott Lingrell DS Hunt Down And Destroy The Jedi" "$PAGES/2026_Retro_GEMPC_Scott_Lingrell_DS_Hunt_Down_And_Destroy_The_Jedi.wiki" "Create: #34 Scott Lingrell Dark Hunt Down two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Scott Lingrell LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Scott_Lingrell_LS_Throne_Room_Mains.wiki" "Create: #34 Scott Lingrell Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Zachary Behm DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Zachary_Behm_DS_Ralltiir_Operations.wiki" "Create: #35 Zachary Behm Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Zachary Behm LS You Can Either Profit By This..." "$PAGES/2026_Retro_GEMPC_Zachary_Behm_LS_You_Can_Either_Profit_By_This....wiki" "Create: #35 Zachary Behm Light Profit two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Matthew Tennyson DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Matthew_Tennyson_DS_Ralltiir_Operations.wiki" "Create: #36 Matthew Tennyson Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Matthew Tennyson LS There Is Good In Him" "$PAGES/2026_Retro_GEMPC_Matthew_Tennyson_LS_There_Is_Good_In_Him.wiki" "Create: #36 Matthew Tennyson Light TIGIH two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Phil Jasper DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Phil_Jasper_DS_Bring_Him_Before_Me.wiki" "Create: #37 Phil Jasper Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Phil Jasper LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Phil_Jasper_LS_Hidden_Base.wiki" "Create: #37 Phil Jasper Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Mike Adamson DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Mike_Adamson_DS_Bring_Him_Before_Me.wiki" "Create: #38 Mike Adamson Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Mike Adamson LS You Can Either Profit By This..." "$PAGES/2026_Retro_GEMPC_Mike_Adamson_LS_You_Can_Either_Profit_By_This....wiki" "Create: #38 Mike Adamson Light Profit two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Brandon Price DS ISB Operations" "$PAGES/2026_Retro_GEMPC_Brandon_Price_DS_ISB_Operations.wiki" "Create: #39 Brandon Price Dark ISB two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Brandon Price LS Rebel Strike Team" "$PAGES/2026_Retro_GEMPC_Brandon_Price_LS_Rebel_Strike_Team.wiki" "Create: #39 Brandon Price Light RST two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC John Heft DS Court Of The Vile Gangster" "$PAGES/2026_Retro_GEMPC_John_Heft_DS_Court_Of_The_Vile_Gangster.wiki" "Create: #40 John Heft Dark Court two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC John Heft LS Echo Base Operations" "$PAGES/2026_Retro_GEMPC_John_Heft_LS_Echo_Base_Operations.wiki" "Create: #40 John Heft Light EBO two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Robert Gravel DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Robert_Gravel_DS_Bring_Him_Before_Me.wiki" "Create: #41 Robert Gravel Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Robert Gravel LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Robert_Gravel_LS_Hidden_Base.wiki" "Create: #41 Robert Gravel Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Cedric Perugini DS Hunt Down And Destroy The Jedi" "$PAGES/2026_Retro_GEMPC_Cedric_Perugini_DS_Hunt_Down_And_Destroy_The_Jedi.wiki" "Create: #42 Cedric Perugini Dark Hunt Down two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Cedric Perugini LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Cedric_Perugini_LS_Throne_Room_Mains.wiki" "Create: #42 Cedric Perugini Light TRM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Carter Vencill DS Imperial Occupation" "$PAGES/2026_Retro_GEMPC_Carter_Vencill_DS_Imperial_Occupation.wiki" "Create: #43 Carter Vencill Dark Imperial Occupation two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Carter Vencill LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Carter_Vencill_LS_Hidden_Base.wiki" "Create: #43 Carter Vencill Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Thomas Nguyen DS Ralltiir Operations" "$PAGES/2026_Retro_GEMPC_Thomas_Nguyen_DS_Ralltiir_Operations.wiki" "Create: #44 Thomas Nguyen Dark ROps two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Thomas Nguyen LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Thomas_Nguyen_LS_Hidden_Base.wiki" "Create: #44 Thomas Nguyen Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Matt Blackstock DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Matt_Blackstock_DS_Bring_Him_Before_Me.wiki" "Create: #45 Matt Blackstock Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Matt Blackstock LS Quiet Mining Colony" "$PAGES/2026_Retro_GEMPC_Matt_Blackstock_LS_Quiet_Mining_Colony.wiki" "Create: #45 Matt Blackstock Light QMC two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Frank Amore DS Set Your Course For Alderaan" "$PAGES/2026_Retro_GEMPC_Frank_Amore_DS_Set_Your_Course_For_Alderaan.wiki" "Create: #46 Frank Amore Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Frank Amore LS Hidden Base" "$PAGES/2026_Retro_GEMPC_Frank_Amore_LS_Hidden_Base.wiki" "Create: #46 Frank Amore Light Hidden Base two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Kurt Winter DS Set Your Course For Alderaan" "$PAGES/2026_Retro_GEMPC_Kurt_Winter_DS_Set_Your_Course_For_Alderaan.wiki" "Create: #47 Kurt Winter Dark SYCFA two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Kurt Winter LS Beggars Canyon" "$PAGES/2026_Retro_GEMPC_Kurt_Winter_LS_Beggars_Canyon.wiki" "Create: #47 Kurt Winter Light Beggars Canyon two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Joshua Parco DS ISB Operations" "$PAGES/2026_Retro_GEMPC_Joshua_Parco_DS_ISB_Operations.wiki" "Create: #48 Joshua Parco Dark ISB two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Joshua Parco LS Mind What You Have Learned" "$PAGES/2026_Retro_GEMPC_Joshua_Parco_LS_Mind_What_You_Have_Learned.wiki" "Create: #48 Joshua Parco Light MWYHL two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Casey Johnson DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Casey_Johnson_DS_Bring_Him_Before_Me.wiki" "Create: #49 Casey Johnson Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Casey Johnson LS You Can Either Profit By This..." "$PAGES/2026_Retro_GEMPC_Casey_Johnson_LS_You_Can_Either_Profit_By_This....wiki" "Create: #49 Casey Johnson Light Profit two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Justin McBride DS Bring Him Before Me" "$PAGES/2026_Retro_GEMPC_Justin_McBride_DS_Bring_Him_Before_Me.wiki" "Create: #50 Justin McBride Dark BHBM two-column from GEMP Fixed zip"
edit "2026 Retro GEMPC Justin McBride LS Throne Room Mains" "$PAGES/2026_Retro_GEMPC_Justin_McBride_LS_Throne_Room_Mains.wiki" "Create: #50 Justin McBride Light TRM two-column from GEMP Fixed zip"

echo "== edit championship =="
edit "2026 Retro GEMP Match Play Championship (Premiere to DSII)" "$PAGES/2026_Retro_GEMP_Match_Play_Championship_(Premiere_to_DSII).wiki" "Standings #9-#50 Dark/Light cells link to sample deck pages; no Decklists section"

echo "== edit player stubs =="
edit "David Garcia" "$PAGES/players/David_Garcia.wiki" "Link #9 Dark/Light sample decklists; Tournament Results Date range"
edit "Joe Horbey" "$PAGES/players/Joe_Horbey.wiki" "Link #10 Dark/Light sample decklists; Tournament Results Date range"
edit "Evan Coupland" "$PAGES/players/Evan_Coupland.wiki" "Link #11 Dark/Light sample decklists; Tournament Results Date range"
edit "Alex Prodoehl" "$PAGES/players/Alex_Prodoehl.wiki" "Link #12 Dark/Light sample decklists; Tournament Results Date range"
edit "Andrew Bethell" "$PAGES/players/Andrew_Bethell.wiki" "Link #13 Dark/Light sample decklists; Tournament Results Date range"
edit "Matthew Ford" "$PAGES/players/Matthew_Ford.wiki" "Link #14 Dark/Light sample decklists; Tournament Results Date range"
edit "Garrett Larson" "$PAGES/players/Garrett_Larson.wiki" "Link #15 Dark/Light sample decklists; Tournament Results Date range"
edit "Chris Madaio" "$PAGES/players/Chris_Madaio.wiki" "Link #16 Dark/Light sample decklists; Tournament Results Date range"
edit "Patrick Johnson" "$PAGES/players/Patrick_Johnson.wiki" "Link #17 Dark/Light sample decklists; Tournament Results Date range"
edit "Kendall Halman" "$PAGES/players/Kendall_Halman.wiki" "Link #18 Dark/Light sample decklists; Tournament Results Date range"
edit "Tony Petersson" "$PAGES/players/Tony_Petersson.wiki" "Link #19 Dark/Light sample decklists; Tournament Results Date range"
edit "Charlie Hickey" "$PAGES/players/Charlie_Hickey.wiki" "Link #20 Dark/Light sample decklists; Tournament Results Date range"
edit "Matt Simpson" "$PAGES/players/Matt_Simpson.wiki" "Link #21 Dark/Light sample decklists; Tournament Results Date range"
edit "Jeff Anderson" "$PAGES/players/Jeff_Anderson.wiki" "Link #22 Dark/Light sample decklists; Tournament Results Date range"
edit "Ben Lindstrom" "$PAGES/players/Ben_Lindstrom.wiki" "Link #23 Dark/Light sample decklists; Tournament Results Date range"
edit "Geoffrey Mikulka" "$PAGES/players/Geoffrey_Mikulka.wiki" "Link #24 Dark/Light sample decklists; Tournament Results Date range"
edit "Robert Waldon" "$PAGES/players/Robert_Waldon.wiki" "Link #25 Dark/Light sample decklists; Tournament Results Date range"
edit "Jarrett McBride" "$PAGES/players/Jarrett_McBride.wiki" "Link #26 Dark/Light sample decklists; Tournament Results Date range"
edit "Brandon Wargo" "$PAGES/players/Brandon_Wargo.wiki" "Link #27 Dark/Light sample decklists; Tournament Results Date range"
edit "Adam Radic" "$PAGES/players/Adam_Radic.wiki" "Link #28 Dark/Light sample decklists; Tournament Results Date range"
edit "Michael Butler" "$PAGES/players/Michael_Butler.wiki" "Link #29 Dark/Light sample decklists; Tournament Results Date range"
edit "Phil Clark" "$PAGES/players/Phil_Clark.wiki" "Link #30 Dark/Light sample decklists; Tournament Results Date range"
edit "Randy Scott" "$PAGES/players/Randy_Scott.wiki" "Link #31 Dark/Light sample decklists; Tournament Results Date range"
edit "Steve Sanders" "$PAGES/players/Steve_Sanders.wiki" "Link #32 Dark/Light sample decklists; Tournament Results Date range"
edit "Christian Deibler" "$PAGES/players/Christian_Deibler.wiki" "Link #33 Dark/Light sample decklists; Tournament Results Date range"
edit "Scott Lingrell" "$PAGES/players/Scott_Lingrell.wiki" "Link #34 Dark/Light sample decklists; Tournament Results Date range"
edit "Zachary Behm" "$PAGES/players/Zachary_Behm.wiki" "Link #35 Dark/Light sample decklists; Tournament Results Date range"
edit "Matthew Tennyson" "$PAGES/players/Matthew_Tennyson.wiki" "Link #36 Dark/Light sample decklists; Tournament Results Date range"
edit "Phil Jasper" "$PAGES/players/Phil_Jasper.wiki" "Link #37 Dark/Light sample decklists; Tournament Results Date range"
edit "Mike Adamson" "$PAGES/players/Mike_Adamson.wiki" "Link #38 Dark/Light sample decklists; Tournament Results Date range"
edit "Brandon Price" "$PAGES/players/Brandon_Price.wiki" "Link #39 Dark/Light sample decklists; Tournament Results Date range"
edit "John Heft" "$PAGES/players/John_Heft.wiki" "Link #40 Dark/Light sample decklists; Tournament Results Date range"
edit "Robert Gravel" "$PAGES/players/Robert_Gravel.wiki" "Link #41 Dark/Light sample decklists; Tournament Results Date range"
edit "Cedric Perugini" "$PAGES/players/Cedric_Perugini.wiki" "Link #42 Dark/Light sample decklists; Tournament Results Date range"
edit "Carter Vencill" "$PAGES/players/Carter_Vencill.wiki" "Link #43 Dark/Light sample decklists; Tournament Results Date range"
edit "Thomas Nguyen" "$PAGES/players/Thomas_Nguyen.wiki" "Link #44 Dark/Light sample decklists; Tournament Results Date range"
edit "Matt Blackstock" "$PAGES/players/Matt_Blackstock.wiki" "Link #45 Dark/Light sample decklists; Tournament Results Date range"
edit "Frank Amore" "$PAGES/players/Frank_Amore.wiki" "Link #46 Dark/Light sample decklists; Tournament Results Date range"
edit "Kurt Winter" "$PAGES/players/Kurt_Winter.wiki" "Link #47 Dark/Light sample decklists; Tournament Results Date range"
edit "Joshua Parco" "$PAGES/players/Joshua_Parco.wiki" "Link #48 Dark/Light sample decklists; Tournament Results Date range"
edit "Casey Johnson" "$PAGES/players/Casey_Johnson.wiki" "Link #49 Dark/Light sample decklists; Tournament Results Date range"
edit "Justin McBride" "$PAGES/players/Justin_McBride.wiki" "Link #50 Dark/Light sample decklists; Tournament Results Date range"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -40

echo "== purgePage =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
2026 Retro GEMPC David Garcia DS Hunt Down And Destroy The Jedi
2026 Retro GEMPC David Garcia LS Throne Room Mains
2026 Retro GEMPC Joe Horbey DS Set Your Course For Alderaan
2026 Retro GEMPC Joe Horbey LS Throne Room Mains
2026 Retro GEMPC Evan Coupland DS Bring Him Before Me
2026 Retro GEMPC Evan Coupland LS Hidden Base
2026 Retro GEMPC Alex Prodoehl DS Hunt Down And Destroy The Jedi
2026 Retro GEMPC Alex Prodoehl LS Mind What You Have Learned
2026 Retro GEMPC Andrew Bethell DS Ralltiir Operations
2026 Retro GEMPC Andrew Bethell LS There Is Good In Him
2026 Retro GEMPC Matthew Ford DS Set Your Course For Alderaan
2026 Retro GEMPC Matthew Ford LS Hidden Base
2026 Retro GEMPC Garrett Larson DS Ralltiir Operations
2026 Retro GEMPC Garrett Larson LS Throne Room Mains
2026 Retro GEMPC Chris Madaio DS Ralltiir Operations
2026 Retro GEMPC Chris Madaio LS Echo Base Operations
2026 Retro GEMPC Patrick Johnson DS Ralltiir Operations
2026 Retro GEMPC Patrick Johnson LS Hidden Base
2026 Retro GEMPC Kendall Halman DS Bring Him Before Me
2026 Retro GEMPC Kendall Halman LS Throne Room Mains
2026 Retro GEMPC Tony Petersson DS Hunt Down And Destroy The Jedi
2026 Retro GEMPC Tony Petersson LS Hidden Base
2026 Retro GEMPC Charlie Hickey DS Set Your Course For Alderaan
2026 Retro GEMPC Charlie Hickey LS You Can Either Profit By This...
2026 Retro GEMPC Matt Simpson DS Court Of The Vile Gangster
2026 Retro GEMPC Matt Simpson LS Local Uprising
2026 Retro GEMPC Jeff Anderson DS Set Your Course For Alderaan
2026 Retro GEMPC Jeff Anderson LS Hidden Base
2026 Retro GEMPC Ben Lindstrom DS Court Of The Vile Gangster
2026 Retro GEMPC Ben Lindstrom LS Massassi Base Operations
2026 Retro GEMPC Geoffrey Mikulka DS ISB Operations
2026 Retro GEMPC Geoffrey Mikulka LS There Is Good In Him
2026 Retro GEMPC Robert Waldon DS Set Your Course For Alderaan
2026 Retro GEMPC Robert Waldon LS Hidden Base
2026 Retro GEMPC Jarrett McBride DS Bring Him Before Me
2026 Retro GEMPC Jarrett McBride LS Throne Room Mains
2026 Retro GEMPC Brandon Wargo DS Bring Him Before Me
2026 Retro GEMPC Brandon Wargo LS Mind What You Have Learned
2026 Retro GEMPC Adam Radic DS Imperial Occupation
2026 Retro GEMPC Adam Radic LS Rebel Strike Team
2026 Retro GEMPC Michael Butler DS Bring Him Before Me
2026 Retro GEMPC Michael Butler LS Throne Room Mains
2026 Retro GEMPC Phil Clark DS ISB Operations
2026 Retro GEMPC Phil Clark LS Throne Room Mains
2026 Retro GEMPC Randy Scott DS Bring Him Before Me
2026 Retro GEMPC Randy Scott LS Throne Room Mains
2026 Retro GEMPC Steve Sanders DS Bring Him Before Me
2026 Retro GEMPC Steve Sanders LS There Is Good In Him
2026 Retro GEMPC Christian Deibler DS ISB Operations
2026 Retro GEMPC Christian Deibler LS You Can Either Profit By This...
2026 Retro GEMPC Scott Lingrell DS Hunt Down And Destroy The Jedi
2026 Retro GEMPC Scott Lingrell LS Throne Room Mains
2026 Retro GEMPC Zachary Behm DS Ralltiir Operations
2026 Retro GEMPC Zachary Behm LS You Can Either Profit By This...
2026 Retro GEMPC Matthew Tennyson DS Ralltiir Operations
2026 Retro GEMPC Matthew Tennyson LS There Is Good In Him
2026 Retro GEMPC Phil Jasper DS Bring Him Before Me
2026 Retro GEMPC Phil Jasper LS Hidden Base
2026 Retro GEMPC Mike Adamson DS Bring Him Before Me
2026 Retro GEMPC Mike Adamson LS You Can Either Profit By This...
2026 Retro GEMPC Brandon Price DS ISB Operations
2026 Retro GEMPC Brandon Price LS Rebel Strike Team
2026 Retro GEMPC John Heft DS Court Of The Vile Gangster
2026 Retro GEMPC John Heft LS Echo Base Operations
2026 Retro GEMPC Robert Gravel DS Bring Him Before Me
2026 Retro GEMPC Robert Gravel LS Hidden Base
2026 Retro GEMPC Cedric Perugini DS Hunt Down And Destroy The Jedi
2026 Retro GEMPC Cedric Perugini LS Throne Room Mains
2026 Retro GEMPC Carter Vencill DS Imperial Occupation
2026 Retro GEMPC Carter Vencill LS Hidden Base
2026 Retro GEMPC Thomas Nguyen DS Ralltiir Operations
2026 Retro GEMPC Thomas Nguyen LS Hidden Base
2026 Retro GEMPC Matt Blackstock DS Bring Him Before Me
2026 Retro GEMPC Matt Blackstock LS Quiet Mining Colony
2026 Retro GEMPC Frank Amore DS Set Your Course For Alderaan
2026 Retro GEMPC Frank Amore LS Hidden Base
2026 Retro GEMPC Kurt Winter DS Set Your Course For Alderaan
2026 Retro GEMPC Kurt Winter LS Beggars Canyon
2026 Retro GEMPC Joshua Parco DS ISB Operations
2026 Retro GEMPC Joshua Parco LS Mind What You Have Learned
2026 Retro GEMPC Casey Johnson DS Bring Him Before Me
2026 Retro GEMPC Casey Johnson LS You Can Either Profit By This...
2026 Retro GEMPC Justin McBride DS Bring Him Before Me
2026 Retro GEMPC Justin McBride LS Throne Room Mains
2026 Retro GEMP Match Play Championship (Premiere to DSII)
David Garcia
Joe Horbey
Evan Coupland
Alex Prodoehl
Andrew Bethell
Matthew Ford
Garrett Larson
Chris Madaio
Patrick Johnson
Kendall Halman
Tony Petersson
Charlie Hickey
Matt Simpson
Jeff Anderson
Ben Lindstrom
Geoffrey Mikulka
Robert Waldon
Jarrett McBride
Brandon Wargo
Adam Radic
Michael Butler
Phil Clark
Randy Scott
Steve Sanders
Christian Deibler
Scott Lingrell
Zachary Behm
Matthew Tennyson
Phil Jasper
Mike Adamson
Brandon Price
John Heft
Robert Gravel
Cedric Perugini
Carter Vencill
Thomas Nguyen
Matt Blackstock
Frank Amore
Kurt Winter
Joshua Parco
Casey Johnson
Justin McBride
File:26RMPC Garcia DS HD.txt
File:26RMPC Garcia LS TRM.txt
File:26RMPC Horbey DS SYCFA.txt
File:26RMPC Horbey LS TRM.txt
File:26RMPC Coupland DS BHBM.txt
File:26RMPC Coupland LS HB.txt
File:26RMPC Prodoehl DS HD.txt
File:26RMPC Prodoehl LS MWYHL.txt
File:26RMPC Bethell DS ROps.txt
File:26RMPC Bethell LS TIGIH.txt
File:26RMPC Ford DS SYCFA.txt
File:26RMPC Ford LS HB.txt
File:26RMPC Larson DS ROps.txt
File:26RMPC Larson LS TRM.txt
File:26RMPC Madaio DS ROps.txt
File:26RMPC Madaio LS EBO.txt
File:26RMPC PJohnson DS ROps.txt
File:26RMPC PJohnson LS HB.txt
File:26RMPC Halman DS BHBM.txt
File:26RMPC Halman LS TRM.txt
File:26RMPC Petersson DS HD.txt
File:26RMPC Petersson LS HB.txt
File:26RMPC Hickey DS SYCFA.txt
File:26RMPC Hickey LS Profit.txt
File:26RMPC Simpson DS Court.txt
File:26RMPC Simpson LS Operatives.txt
File:26RMPC Anderson DS SYCFA.txt
File:26RMPC Anderson LS HB.txt
File:26RMPC Lindstrom DS Court.txt
File:26RMPC Lindstrom LS MBO.txt
File:26RMPC Mikulka DS ISB.txt
File:26RMPC Mikulka LS TIGIH.txt
File:26RMPC Waldron DS SYCFA.txt
File:26RMPC Waldron LS HB.txt
File:26RMPC Ja McBride DS BHBM.txt
File:26RMPC Ja McBride LS TRM.txt
File:26RMPC Wargo DS BHBM.txt
File:26RMPC Wargo LS MWYHL.txt
File:26RMPC Radic DS Clouds.txt
File:26RMPC Radic LS RST.txt
File:26RMPC Butler DS BHBM.txt
File:26RMPC Butler LS TRM.txt
File:26RMPC Clark DS ISB.txt
File:26RMPC Clark LS TRM.txt
File:26RMPC RScott DS BHBM.txt
File:26RMPC RScott LS TRM.txt
File:26RMPC Sanders DS BHBM.txt
File:26RMPC Sanders LS TIGIH.txt
File:26RMPC Deibler DS ISB.txt
File:26RMPC Deibler LS Profit.txt
File:26RMPC Lingrell DS HD.txt
File:26RMPC Lingrell LS TRM.txt
File:26RMPC Behm DS ROps.txt
File:26RMPC Behm LS Profit.txt
File:26RMPC Tennyson DS ROps.txt
File:26RMPC Tennyson LS TIGIH.txt
File:26RMPC Jasper DS BHBM.txt
File:26RMPC Jasper LS HB.txt
File:26RMPC Adamson DS BHBM.txt
File:26RMPC Adamson LS Profit.txt
File:26RMPC Price DS ISB.txt
File:26RMPC Price LS RST.txt
File:26RMPC Heft DS Court.txt
File:26RMPC Heft LS EBO.txt
File:26RMPC Gravel DS BHBM.txt
File:26RMPC Gravel LS HB.txt
File:26RMPC Perugini DS HD.txt
File:26RMPC Perugini LS TRM.txt
File:26RMPC Vencill DS TIEs.txt
File:26RMPC Vencill LS HB.txt
File:26RMPC Nguyen DS ROps.txt
File:26RMPC Nguyen LS HB.txt
File:26RMPC Blackstock DS BHBM.txt
File:26RMPC Blackstock LS QMC.txt
File:26RMPC Amore DS SYCFA.txt
File:26RMPC Amore LS HB.txt
File:26RMPC Winter DS SYCFA.txt
File:26RMPC Winter LS Beg Canyon.txt
File:26RMPC Parco DS ISB.txt
File:26RMPC Parco LS MWYHL.txt
File:26RMPC CJohnson DS BHBM.txt
File:26RMPC CJohnson LS Profit.txt
File:26RMPC Ju McBride DS BHBM.txt
File:26RMPC Ju McBride LS TRM.txt
Main Page
EOFPURGE

echo "== side-scan verify sample =="
python3 <<'PY'
import subprocess
checks = [
  ('2026 Retro GEMPC David Garcia DS Hunt Down And Destroy The Jedi', 'Dark'),
  ('2026 Retro GEMPC David Garcia LS Throne Room Mains', 'Light'),
  ('2026 Retro GEMPC Joe Horbey DS Set Your Course For Alderaan', 'Dark'),
  ('2026 Retro GEMPC Joe Horbey LS Throne Room Mains', 'Light'),
  ('2026 Retro GEMPC Michael Butler DS Bring Him Before Me', 'Dark'),
  ('2026 Retro GEMPC Michael Butler LS Throne Room Mains', 'Light'),
  ('2026 Retro GEMPC Phil Clark DS ISB Operations', 'Dark'),
  ('2026 Retro GEMPC Phil Clark LS Throne Room Mains', 'Light'),
  ('2026 Retro GEMPC Casey Johnson DS Bring Him Before Me', 'Dark'),
  ('2026 Retro GEMPC Casey Johnson LS You Can Either Profit By This...', 'Light'),
  ('2026 Retro GEMPC Justin McBride DS Bring Him Before Me', 'Dark'),
  ('2026 Retro GEMPC Justin McBride LS Throne Room Mains', 'Light'),
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
print("side-scan sample OK")
PY

echo "== championship cells verify =="
docker exec swccg_wiki php maintenance/run.php getText "2026 Retro GEMP Match Play Championship (Premiere to DSII)"   | python3 -c "import sys; t=sys.stdin.read();
assert '== Decklists ==' not in t
for s in ['David Garcia DS Hunt Down','Kurt Winter LS Beggars','Adam Radic DS Imperial','Casey Johnson DS Bring','Justin McBride LS Throne']:
  assert s in t, s
print('championship links OK; no Decklists section')"

echo remaining-decks-applied
