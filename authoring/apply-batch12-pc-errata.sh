#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch12-gifs

ARCHIVES=(
  Hoth-L-duallasercannon-decipher-archive.gif
  Hoth-L-echotrooperbackpack-decipher-archive.gif
  Dagobah-L-effectiverepairs-decipher-archive.gif
  Premiere-D-eg6-decipher-archive.gif
  Dagobah-L-egregiouspiloterror-decipher-archive.gif
  ANH-L-ejecteject-decipher-archive.gif
  Premiere-D-elishelrot-decipher-archive.gif
  Premiere-L-ellorrsmadak-decipher-archive.gif
  JP-L-elom-decipher-archive.gif
  Premiere-D-emergencydeployment-decipher-archive.gif
  CC-D-endthisdestructiveconflict-decipher-archive.gif
  ANH-D-enhancedtielasercannon-decipher-archive.gif
  Premiere-L-escapepod-decipher-archive.gif
  Hoth-L-evacuationcontrol-decipher-archive.gif
  ANH-D-evader-decipher-archive.gif
  Dagobah-D-executorholotheatre-decipher-archive.gif
)
HT_FILES=(
  Hoth-L-duallasercannon.gif
  Hoth-L-echotrooperbackpack.gif
  Dagobah-L-effectiverepairs.gif
  Premiere-D-eg6.gif
  Dagobah-L-egregiouspiloterror.gif
  ANH-L-ejecteject.gif
  Premiere-D-elishelrot.gif
  Premiere-L-ellorrsmadak.gif
  JP-L-elom.gif
  Premiere-D-emergencydeployment.gif
  CC-D-endthisdestructiveconflict.gif
  ANH-D-enhancedtielasercannon.gif
  Premiere-L-escapepod.gif
  Hoth-L-evacuationcontrol.gif
  ANH-D-evader.gif
  Dagobah-D-executorholotheatre.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch12-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch12-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch12-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch12 (Dual Laser Cannon through Executor: Holotheatre); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch12-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch12-gifs
fi

edit "File:Hoth-L-duallasercannon-decipher-archive.gif" "$PAGES/File_Hoth-L-duallasercannon-decipher-archive.gif.wiki" "File: Decipher archive Original Dual Laser Cannon"
edit "File:Hoth-L-echotrooperbackpack-decipher-archive.gif" "$PAGES/File_Hoth-L-echotrooperbackpack-decipher-archive.gif.wiki" "File: Decipher archive Original Echo Trooper Backpack"
edit "File:Dagobah-L-effectiverepairs-decipher-archive.gif" "$PAGES/File_Dagobah-L-effectiverepairs-decipher-archive.gif.wiki" "File: Decipher archive Original Effective Repairs"
edit "File:Premiere-D-eg6-decipher-archive.gif" "$PAGES/File_Premiere-D-eg6-decipher-archive.gif.wiki" "File: Decipher archive Original EG-6 (Eegee-Six)"
edit "File:Dagobah-L-egregiouspiloterror-decipher-archive.gif" "$PAGES/File_Dagobah-L-egregiouspiloterror-decipher-archive.gif.wiki" "File: Decipher archive Original Egregious Pilot Error"
edit "File:ANH-L-ejecteject-decipher-archive.gif" "$PAGES/File_ANH-L-ejecteject-decipher-archive.gif.wiki" "File: Decipher archive Original Eject! Eject!"
edit "File:Premiere-D-elishelrot-decipher-archive.gif" "$PAGES/File_Premiere-D-elishelrot-decipher-archive.gif.wiki" "File: Decipher archive Original Elis Helrot"
edit "File:Premiere-L-ellorrsmadak-decipher-archive.gif" "$PAGES/File_Premiere-L-ellorrsmadak-decipher-archive.gif.wiki" "File: Decipher archive Original Ellorrs Madak"
edit "File:JP-L-elom-decipher-archive.gif" "$PAGES/File_JP-L-elom-decipher-archive.gif.wiki" "File: Decipher archive Original Elom"
edit "File:Premiere-D-emergencydeployment-decipher-archive.gif" "$PAGES/File_Premiere-D-emergencydeployment-decipher-archive.gif.wiki" "File: Decipher archive Original Emergency Deployment"
edit "File:CC-D-endthisdestructiveconflict-decipher-archive.gif" "$PAGES/File_CC-D-endthisdestructiveconflict-decipher-archive.gif.wiki" "File: Decipher archive Original End This Destructive Conflict"
edit "File:ANH-D-enhancedtielasercannon-decipher-archive.gif" "$PAGES/File_ANH-D-enhancedtielasercannon-decipher-archive.gif.wiki" "File: Decipher archive Original Enhanced TIE Laser Cannon"
edit "File:Premiere-L-escapepod-decipher-archive.gif" "$PAGES/File_Premiere-L-escapepod-decipher-archive.gif.wiki" "File: Decipher archive Original Escape Pod"
edit "File:Hoth-L-evacuationcontrol-decipher-archive.gif" "$PAGES/File_Hoth-L-evacuationcontrol-decipher-archive.gif.wiki" "File: Decipher archive Original Evacuation Control"
edit "File:ANH-D-evader-decipher-archive.gif" "$PAGES/File_ANH-D-evader-decipher-archive.gif.wiki" "File: Decipher archive Original Evader"
edit "File:Dagobah-D-executorholotheatre-decipher-archive.gif" "$PAGES/File_Dagobah-D-executorholotheatre-decipher-archive.gif.wiki" "File: Decipher archive Original Executor: Holotheatre"

edit "Dual Laser Cannon (Original)" "$PAGES/Dual_Laser_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dual Laser Cannon (PC Errata)" "$PAGES/Dual_Laser_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dual Laser Cannon" "$PAGES/Dual_Laser_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Echo Trooper Backpack (Original)" "$PAGES/Echo_Trooper_Backpack_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Echo Trooper Backpack (PC Errata)" "$PAGES/Echo_Trooper_Backpack_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Echo Trooper Backpack" "$PAGES/Echo_Trooper_Backpack.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Effective Repairs (Original)" "$PAGES/Effective_Repairs_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Effective Repairs (PC Errata)" "$PAGES/Effective_Repairs_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Effective Repairs" "$PAGES/Effective_Repairs.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "EG-6 (Eegee-Six) (Original)" "$PAGES/EG-6_(Eegee-Six)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "EG-6 (Eegee-Six) (PC Errata)" "$PAGES/EG-6_(Eegee-Six)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "EG-6 (Eegee-Six)" "$PAGES/EG-6_(Eegee-Six).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Egregious Pilot Error (Original)" "$PAGES/Egregious_Pilot_Error_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Egregious Pilot Error (PC Errata)" "$PAGES/Egregious_Pilot_Error_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Egregious Pilot Error" "$PAGES/Egregious_Pilot_Error.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Eject! Eject! (Original)" "$PAGES/Eject!_Eject!_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Eject! Eject! (PC Errata)" "$PAGES/Eject!_Eject!_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Eject! Eject!" "$PAGES/Eject!_Eject!.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Elis Helrot (Original)" "$PAGES/Elis_Helrot_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Elis Helrot (PC Errata)" "$PAGES/Elis_Helrot_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Elis Helrot" "$PAGES/Elis_Helrot.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Ellorrs Madak (Original)" "$PAGES/Ellorrs_Madak_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ellorrs Madak (PC Errata)" "$PAGES/Ellorrs_Madak_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ellorrs Madak" "$PAGES/Ellorrs_Madak.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Elom (Original)" "$PAGES/Elom_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Elom (PC Errata)" "$PAGES/Elom_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Elom" "$PAGES/Elom.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Emergency Deployment (Original)" "$PAGES/Emergency_Deployment_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Emergency Deployment (PC Errata)" "$PAGES/Emergency_Deployment_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Emergency Deployment" "$PAGES/Emergency_Deployment.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "End This Destructive Conflict (Original)" "$PAGES/End_This_Destructive_Conflict_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "End This Destructive Conflict (PC Errata)" "$PAGES/End_This_Destructive_Conflict_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "End This Destructive Conflict" "$PAGES/End_This_Destructive_Conflict.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Enhanced TIE Laser Cannon (Original)" "$PAGES/Enhanced_TIE_Laser_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Enhanced TIE Laser Cannon (PC Errata)" "$PAGES/Enhanced_TIE_Laser_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Enhanced TIE Laser Cannon" "$PAGES/Enhanced_TIE_Laser_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Escape Pod (Original)" "$PAGES/Escape_Pod_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Escape Pod (PC Errata)" "$PAGES/Escape_Pod_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Escape Pod" "$PAGES/Escape_Pod.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Evacuation Control (Original)" "$PAGES/Evacuation_Control_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Evacuation Control (PC Errata)" "$PAGES/Evacuation_Control_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Evacuation Control" "$PAGES/Evacuation_Control.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Evader (Original)" "$PAGES/Evader_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Evader (PC Errata)" "$PAGES/Evader_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Evader" "$PAGES/Evader.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Executor: Holotheatre (Original)" "$PAGES/Executor:_Holotheatre_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Executor: Holotheatre (PC Errata)" "$PAGES/Executor:_Holotheatre_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Executor: Holotheatre" "$PAGES/Executor:_Holotheatre.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch12 (Dual Laser Cannon through Executor: Holotheatre)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch12 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Dual Laser Cannon"
  "Dual Laser Cannon (Original)"
  "Dual Laser Cannon (PC Errata)"
  "Echo Trooper Backpack"
  "Echo Trooper Backpack (Original)"
  "Echo Trooper Backpack (PC Errata)"
  "Effective Repairs"
  "Effective Repairs (Original)"
  "Effective Repairs (PC Errata)"
  "EG-6 (Eegee-Six)"
  "EG-6 (Eegee-Six) (Original)"
  "EG-6 (Eegee-Six) (PC Errata)"
  "Egregious Pilot Error"
  "Egregious Pilot Error (Original)"
  "Egregious Pilot Error (PC Errata)"
  "Eject! Eject!"
  "Eject! Eject! (Original)"
  "Eject! Eject! (PC Errata)"
  "Elis Helrot"
  "Elis Helrot (Original)"
  "Elis Helrot (PC Errata)"
  "Ellorrs Madak"
  "Ellorrs Madak (Original)"
  "Ellorrs Madak (PC Errata)"
  "Elom"
  "Elom (Original)"
  "Elom (PC Errata)"
  "Emergency Deployment"
  "Emergency Deployment (Original)"
  "Emergency Deployment (PC Errata)"
  "End This Destructive Conflict"
  "End This Destructive Conflict (Original)"
  "End This Destructive Conflict (PC Errata)"
  "Enhanced TIE Laser Cannon"
  "Enhanced TIE Laser Cannon (Original)"
  "Enhanced TIE Laser Cannon (PC Errata)"
  "Escape Pod"
  "Escape Pod (Original)"
  "Escape Pod (PC Errata)"
  "Evacuation Control"
  "Evacuation Control (Original)"
  "Evacuation Control (PC Errata)"
  "Evader"
  "Evader (Original)"
  "Evader (PC Errata)"
  "Executor: Holotheatre"
  "Executor: Holotheatre (Original)"
  "Executor: Holotheatre (PC Errata)"
  "Errata"
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
echo DONE_APPLY_BATCH12_PC_ERRATA
