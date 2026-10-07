#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch32-gifs

ARCHIVES=(
  Premiere-D-thecircleisnowcomplete-decipher-archive.gif
  CloudCity-D-theemperorsprize-decipher-archive.gif
  ANH-L-theyreondantooine-decipher-archive.gif
  Dagobah-D-tieavenger-decipher-archive.gif
  ANH-D-tievanguard-decipher-archive.gif
  ANH-L-tiree-decipher-archive.gif
  Premiere-D-tonnikasisters-decipher-archive.gif
  Hoth-L-torynfarr-decipher-archive.gif
  ANH-D-tractorbeam-decipher-archive.gif
  Hoth-D-trample-decipher-archive.gif
  CloudCity-L-trevahorme-decipher-archive.gif
  Premiere-D-turbolaserbattery-decipher-archive.gif
  CloudCity-D-restrictedaccess-decipher-archive.gif
)
HT_FILES=(
  Premiere-D-thecircleisnowcomplete.gif
  CC-D-theemperorsprize.gif
  ANH-L-theyreondantooine.gif
  Dagobah-D-tieavenger.gif
  ANH-D-tievanguard.gif
  ANH-L-tiree.gif
  Premiere-D-tonnikasisters.gif
  Hoth-L-torynfarr.gif
  ANH-D-tractorbeam.gif
  Hoth-D-trample.gif
  CC-L-trevahorme.gif
  Premiere-D-turbolaserbattery.gif
  CC-D-restrictedaccess.gif
)

strip_bom() {
  python3 - "$1" <<'INNER'
from pathlib import Path
import sys, re
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
m = re.search(r"\|notes=(.*?)(\n\|[a-z_]+=|\n\}\})", text, re.S)
if m and re.search(r"\[\[File:[^\]]*\.gif", m.group(1), re.I):
    raise SystemExit(f"FATAL: gif File embed in notes of {p.name}")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
INNER
}
edit() {
  local title="$1" file="$2" summary="$3"
  strip_bom "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}
ht_hex() {
  local HT_FILE="$1"
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -type f -name "'"$HT_FILE"'" | head -1); if [ -n "$f" ]; then sha1sum "$f" | awk "{print \$1}"; else echo MISSING; fi'
}

echo "== Holotable BEFORE =="
declare -a HT_BEFORE
for ht in "${HT_FILES[@]}"; do
  h=$(ht_hex "$ht"); echo "ht_before $ht=$h"
  test -n "$h" && test "$h" != "MISSING"
  HT_BEFORE+=("$h")
done

mkdir -p "$STAGE"; rm -f "$STAGE"/*
for a in "${ARCHIVES[@]}"; do
  test -f "$ROOT/set-card-art/$a"
  cp -f "$ROOT/set-card-art/$a" "$STAGE/$a"
done
for ht in "${HT_FILES[@]}"; do
  if [ -f "$STAGE/$ht" ]; then echo "REFUSING Holotable $ht"; exit 1; fi
done

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch32-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch32-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch32-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch32 (The Circle Is Now Complete through Restricted Access); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch32-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch32-gifs
fi

edit "File:Premiere-D-thecircleisnowcomplete-decipher-archive.gif" "$PAGES/File_Premiere-D-thecircleisnowcomplete-decipher-archive.gif.wiki" "File: Decipher archive Original The Circle Is Now Complete"
edit "File:CloudCity-D-theemperorsprize-decipher-archive.gif" "$PAGES/File_CloudCity-D-theemperorsprize-decipher-archive.gif.wiki" "File: Decipher archive Original The Emperor's Prize"
edit "File:ANH-L-theyreondantooine-decipher-archive.gif" "$PAGES/File_ANH-L-theyreondantooine-decipher-archive.gif.wiki" "File: Decipher archive Original They're On Dantooine"
edit "File:Dagobah-D-tieavenger-decipher-archive.gif" "$PAGES/File_Dagobah-D-tieavenger-decipher-archive.gif.wiki" "File: Decipher archive Original TIE Avenger"
edit "File:ANH-D-tievanguard-decipher-archive.gif" "$PAGES/File_ANH-D-tievanguard-decipher-archive.gif.wiki" "File: Decipher archive Original TIE Vanguard"
edit "File:ANH-L-tiree-decipher-archive.gif" "$PAGES/File_ANH-L-tiree-decipher-archive.gif.wiki" "File: Decipher archive Original Tiree"
edit "File:Premiere-D-tonnikasisters-decipher-archive.gif" "$PAGES/File_Premiere-D-tonnikasisters-decipher-archive.gif.wiki" "File: Decipher archive Original Tonnika Sisters"
edit "File:Hoth-L-torynfarr-decipher-archive.gif" "$PAGES/File_Hoth-L-torynfarr-decipher-archive.gif.wiki" "File: Decipher archive Original Toryn Farr"
edit "File:ANH-D-tractorbeam-decipher-archive.gif" "$PAGES/File_ANH-D-tractorbeam-decipher-archive.gif.wiki" "File: Decipher archive Original Tractor Beam"
edit "File:Hoth-D-trample-decipher-archive.gif" "$PAGES/File_Hoth-D-trample-decipher-archive.gif.wiki" "File: Decipher archive Original Trample"
edit "File:CloudCity-L-trevahorme-decipher-archive.gif" "$PAGES/File_CloudCity-L-trevahorme-decipher-archive.gif.wiki" "File: Decipher archive Original Treva Horme"
edit "File:Premiere-D-turbolaserbattery-decipher-archive.gif" "$PAGES/File_Premiere-D-turbolaserbattery-decipher-archive.gif.wiki" "File: Decipher archive Original Turbolaser Battery"
edit "File:CloudCity-D-restrictedaccess-decipher-archive.gif" "$PAGES/File_CloudCity-D-restrictedaccess-decipher-archive.gif.wiki" "File: Decipher archive Original Restricted Access"

edit "The Circle Is Now Complete (Original)" "$PAGES/The_Circle_Is_Now_Complete_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "The Circle Is Now Complete (PC Errata)" "$PAGES/The_Circle_Is_Now_Complete_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "The Circle Is Now Complete" "$PAGES/The_Circle_Is_Now_Complete.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "The Emperor's Prize (Original)" "$PAGES/The_Emperor's_Prize_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "The Emperor's Prize (PC Errata)" "$PAGES/The_Emperor's_Prize_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "The Emperor's Prize" "$PAGES/The_Emperor's_Prize.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "They're On Dantooine (Original)" "$PAGES/They're_On_Dantooine_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "They're On Dantooine (PC Errata)" "$PAGES/They're_On_Dantooine_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "They're On Dantooine" "$PAGES/They're_On_Dantooine.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "TIE Avenger (Original)" "$PAGES/TIE_Avenger_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "TIE Avenger (PC Errata)" "$PAGES/TIE_Avenger_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "TIE Avenger" "$PAGES/TIE_Avenger.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "TIE Vanguard (Original)" "$PAGES/TIE_Vanguard_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "TIE Vanguard (PC Errata)" "$PAGES/TIE_Vanguard_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "TIE Vanguard" "$PAGES/TIE_Vanguard.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tiree (Original)" "$PAGES/Tiree_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tiree (PC Errata)" "$PAGES/Tiree_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tiree" "$PAGES/Tiree.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tonnika Sisters (Original)" "$PAGES/Tonnika_Sisters_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tonnika Sisters (PC Errata)" "$PAGES/Tonnika_Sisters_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tonnika Sisters" "$PAGES/Tonnika_Sisters.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Toryn Farr (Original)" "$PAGES/Toryn_Farr_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Toryn Farr (PC Errata)" "$PAGES/Toryn_Farr_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Toryn Farr" "$PAGES/Toryn_Farr.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tractor Beam (Original)" "$PAGES/Tractor_Beam_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tractor Beam (PC Errata)" "$PAGES/Tractor_Beam_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tractor Beam" "$PAGES/Tractor_Beam.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Trample (Original)" "$PAGES/Trample_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Trample (PC Errata)" "$PAGES/Trample_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Trample" "$PAGES/Trample.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Treva Horme (Original)" "$PAGES/Treva_Horme_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Treva Horme (PC Errata)" "$PAGES/Treva_Horme_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Treva Horme" "$PAGES/Treva_Horme.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Turbolaser Battery (Original)" "$PAGES/Turbolaser_Battery_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Turbolaser Battery (PC Errata)" "$PAGES/Turbolaser_Battery_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Turbolaser Battery" "$PAGES/Turbolaser_Battery.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Restricted Access (Original)" "$PAGES/Restricted_Access_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Restricted Access (PC Errata)" "$PAGES/Restricted_Access_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Restricted Access" "$PAGES/Restricted_Access.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch32 (The Circle Is Now Complete through Restricted Access)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch32 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "The Circle Is Now Complete" \
  "The Circle Is Now Complete (Original)" \
  "The Circle Is Now Complete (PC Errata)" \
  "The Emperor's Prize" \
  "The Emperor's Prize (Original)" \
  "The Emperor's Prize (PC Errata)" \
  "They're On Dantooine" \
  "They're On Dantooine (Original)" \
  "They're On Dantooine (PC Errata)" \
  "TIE Avenger" \
  "TIE Avenger (Original)" \
  "TIE Avenger (PC Errata)" \
  "TIE Vanguard" \
  "TIE Vanguard (Original)" \
  "TIE Vanguard (PC Errata)" \
  "Tiree" \
  "Tiree (Original)" \
  "Tiree (PC Errata)" \
  "Tonnika Sisters" \
  "Tonnika Sisters (Original)" \
  "Tonnika Sisters (PC Errata)" \
  "Toryn Farr" \
  "Toryn Farr (Original)" \
  "Toryn Farr (PC Errata)" \
  "Tractor Beam" \
  "Tractor Beam (Original)" \
  "Tractor Beam (PC Errata)" \
  "Trample" \
  "Trample (Original)" \
  "Trample (PC Errata)" \
  "Treva Horme" \
  "Treva Horme (Original)" \
  "Treva Horme (PC Errata)" \
  "Turbolaser Battery" \
  "Turbolaser Battery (Original)" \
  "Turbolaser Battery (PC Errata)" \
  "Restricted Access" \
  "Restricted Access (Original)" \
  "Restricted Access (PC Errata)" \
  "Errata" \
  "PC Errata"
do
  echo "purge $t"; purge "$t"
done
for a in "${ARCHIVES[@]}"; do purge "File:$a"; done
for ht in "${HT_FILES[@]}"; do purge "File:$ht"; done

echo "== Holotable AFTER =="
i=0
for ht in "${HT_FILES[@]}"; do
  h=$(ht_hex "$ht"); echo "ht_after $ht=$h"
  test "$h" = "${HT_BEFORE[$i]}"
  i=$((i+1))
done
echo HOLOTABLE_OK
echo DONE_APPLY_BATCH32_PC_ERRATA
