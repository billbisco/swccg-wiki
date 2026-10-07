#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch24-gifs

ARCHIVES=(
  ANH-D-mobqueta1deluxefloater-decipher-archive.gif
  Premiere-D-momentoftriumph-decipher-archive.gif
  Premiere-D-mse6mousedroid-decipher-archive.gif
  ANH-D-mosep-decipher-archive.gif
  ANH-L-mottiseeker-decipher-archive.gif
  Premiere-L-movealong-decipher-archive.gif
  Dagobah-L-movingtoattackposition-decipher-archive.gif
  Premiere-L-nabrunleids-decipher-archive.gif
  Premiere-L-obiwankenobi-decipher-archive.gif
  Premiere-L-obiwanslightsaber-decipher-archive.gif
  JPSD-D-mercenarypilot-decipher-archive.gif
  CloudCity-D-imperialtrooperguarddainsom-decipher-archive.gif
)
HT_FILES=(
  ANH-D-mobqueta1deluxefloater.gif
  Premiere-D-momentoftriumph.gif
  Premiere-D-mse6mousedroid.gif
  ANH-D-mosep.gif
  ANH-L-mottiseeker.gif
  Premiere-L-movealong.gif
  Dagobah-L-movingtoattackposition.gif
  Premiere-L-nabrunleids.gif
  Premiere-L-obiwankenobi.gif
  Premiere-L-obiwanslightsaber.gif
  JPSD-D-mercenarypilot.gif
  CC-D-imperialtrooperguarddainsom.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch24-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch24-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch24-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch24 (Mobquet A-1 Deluxe Floater through Imperial Trooper Guard Dainsom); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch24-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch24-gifs
fi

edit "File:ANH-D-mobqueta1deluxefloater-decipher-archive.gif" "$PAGES/File_ANH-D-mobqueta1deluxefloater-decipher-archive.gif.wiki" "File: Decipher archive Original Mobquet A-1 Deluxe Floater"
edit "File:Premiere-D-momentoftriumph-decipher-archive.gif" "$PAGES/File_Premiere-D-momentoftriumph-decipher-archive.gif.wiki" "File: Decipher archive Original Moment Of Triumph"
edit "File:Premiere-D-mse6mousedroid-decipher-archive.gif" "$PAGES/File_Premiere-D-mse6mousedroid-decipher-archive.gif.wiki" "File: Decipher archive Original MSE-6 'Mouse' Droid"
edit "File:ANH-D-mosep-decipher-archive.gif" "$PAGES/File_ANH-D-mosep-decipher-archive.gif.wiki" "File: Decipher archive Original Mosep"
edit "File:ANH-L-mottiseeker-decipher-archive.gif" "$PAGES/File_ANH-L-mottiseeker-decipher-archive.gif.wiki" "File: Decipher archive Original Motti Seeker"
edit "File:Premiere-L-movealong-decipher-archive.gif" "$PAGES/File_Premiere-L-movealong-decipher-archive.gif.wiki" "File: Decipher archive Original Move Along..."
edit "File:Dagobah-L-movingtoattackposition-decipher-archive.gif" "$PAGES/File_Dagobah-L-movingtoattackposition-decipher-archive.gif.wiki" "File: Decipher archive Original Moving To Attack Position"
edit "File:Premiere-L-nabrunleids-decipher-archive.gif" "$PAGES/File_Premiere-L-nabrunleids-decipher-archive.gif.wiki" "File: Decipher archive Original Nabrun Leids"
edit "File:Premiere-L-obiwankenobi-decipher-archive.gif" "$PAGES/File_Premiere-L-obiwankenobi-decipher-archive.gif.wiki" "File: Decipher archive Original Obi-Wan Kenobi"
edit "File:Premiere-L-obiwanslightsaber-decipher-archive.gif" "$PAGES/File_Premiere-L-obiwanslightsaber-decipher-archive.gif.wiki" "File: Decipher archive Original Obi-Wan's Lightsaber"
edit "File:JPSD-D-mercenarypilot-decipher-archive.gif" "$PAGES/File_JPSD-D-mercenarypilot-decipher-archive.gif.wiki" "File: Decipher archive Original Mercenary Pilot"
edit "File:CloudCity-D-imperialtrooperguarddainsom-decipher-archive.gif" "$PAGES/File_CloudCity-D-imperialtrooperguarddainsom-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Trooper Guard Dainsom"
edit "Mobquet A-1 Deluxe Floater (Original)" "$PAGES/Mobquet_A-1_Deluxe_Floater_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Mobquet A-1 Deluxe Floater (PC Errata)" "$PAGES/Mobquet_A-1_Deluxe_Floater_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Mobquet A-1 Deluxe Floater" "$PAGES/Mobquet_A-1_Deluxe_Floater.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Moment Of Triumph (Original)" "$PAGES/Moment_Of_Triumph_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Moment Of Triumph (PC Errata)" "$PAGES/Moment_Of_Triumph_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Moment Of Triumph" "$PAGES/Moment_Of_Triumph.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "MSE-6 'Mouse' Droid (Original)" "$PAGES/MSE-6_'Mouse'_Droid_(Original).wiki" "PC Errata seed: printed Decipher archive Original (create)"
edit "MSE-6 'Mouse' Droid (PC Errata)" "$PAGES/MSE-6_'Mouse'_Droid_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable (create)"
edit "MSE-6 'Mouse' Droid" "$PAGES/MSE-6_'Mouse'_Droid.wiki" "Create bare + Decipher print; archive face; link PC Errata"
edit "Mosep (Original)" "$PAGES/Mosep_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Mosep (PC Errata)" "$PAGES/Mosep_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Mosep" "$PAGES/Mosep.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Motti Seeker (Original)" "$PAGES/Motti_Seeker_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Motti Seeker (PC Errata)" "$PAGES/Motti_Seeker_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Motti Seeker" "$PAGES/Motti_Seeker.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Move Along... (Original)" "$PAGES/Move_Along..._(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Move Along... (PC Errata)" "$PAGES/Move_Along..._(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Move Along..." "$PAGES/Move_Along....wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Moving To Attack Position (Original)" "$PAGES/Moving_To_Attack_Position_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Moving To Attack Position (PC Errata)" "$PAGES/Moving_To_Attack_Position_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Moving To Attack Position" "$PAGES/Moving_To_Attack_Position.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Nabrun Leids (Original)" "$PAGES/Nabrun_Leids_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Nabrun Leids (PC Errata)" "$PAGES/Nabrun_Leids_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Nabrun Leids" "$PAGES/Nabrun_Leids.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Obi-Wan Kenobi (Original)" "$PAGES/Obi-Wan_Kenobi_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Obi-Wan Kenobi (PC Errata)" "$PAGES/Obi-Wan_Kenobi_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Obi-Wan Kenobi" "$PAGES/Obi-Wan_Kenobi.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Obi-Wan's Lightsaber (Original)" "$PAGES/Obi-Wan's_Lightsaber_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Obi-Wan's Lightsaber (PC Errata)" "$PAGES/Obi-Wan's_Lightsaber_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Obi-Wan's Lightsaber" "$PAGES/Obi-Wan's_Lightsaber.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Mercenary Pilot (Original)" "$PAGES/Mercenary_Pilot_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Mercenary Pilot (PC Errata)" "$PAGES/Mercenary_Pilot_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Mercenary Pilot" "$PAGES/Mercenary_Pilot.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Imperial Trooper Guard Dainsom (Original)" "$PAGES/Imperial_Trooper_Guard_Dainsom_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Trooper Guard Dainsom (PC Errata)" "$PAGES/Imperial_Trooper_Guard_Dainsom_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Trooper Guard Dainsom" "$PAGES/Imperial_Trooper_Guard_Dainsom.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch24 (Mobquet A-1 Deluxe Floater through Imperial Trooper Guard Dainsom)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch24 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Mobquet A-1 Deluxe Floater" \
  "Mobquet A-1 Deluxe Floater (Original)" \
  "Mobquet A-1 Deluxe Floater (PC Errata)" \
  "Moment Of Triumph" \
  "Moment Of Triumph (Original)" \
  "Moment Of Triumph (PC Errata)" \
  "MSE-6 'Mouse' Droid" \
  "MSE-6 'Mouse' Droid (Original)" \
  "MSE-6 'Mouse' Droid (PC Errata)" \
  "Mosep" \
  "Mosep (Original)" \
  "Mosep (PC Errata)" \
  "Motti Seeker" \
  "Motti Seeker (Original)" \
  "Motti Seeker (PC Errata)" \
  "Move Along..." \
  "Move Along... (Original)" \
  "Move Along... (PC Errata)" \
  "Moving To Attack Position" \
  "Moving To Attack Position (Original)" \
  "Moving To Attack Position (PC Errata)" \
  "Nabrun Leids" \
  "Nabrun Leids (Original)" \
  "Nabrun Leids (PC Errata)" \
  "Obi-Wan Kenobi" \
  "Obi-Wan Kenobi (Original)" \
  "Obi-Wan Kenobi (PC Errata)" \
  "Obi-Wan's Lightsaber" \
  "Obi-Wan's Lightsaber (Original)" \
  "Obi-Wan's Lightsaber (PC Errata)" \
  "Mercenary Pilot" \
  "Mercenary Pilot (Original)" \
  "Mercenary Pilot (PC Errata)" \
  "Imperial Trooper Guard Dainsom" \
  "Imperial Trooper Guard Dainsom (Original)" \
  "Imperial Trooper Guard Dainsom (PC Errata)" \
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
echo DONE_APPLY_BATCH24_PC_ERRATA
