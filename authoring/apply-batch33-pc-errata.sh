#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch33-gifs

ARCHIVES=(
  Premiere-D-tuskenraider-decipher-archive.gif
  ANH-D-u3po-decipher-archive.gif
  Premiere-D-ubrikkian9000z001-decipher-archive.gif
  Dagobah-D-uncertainisthefuture-decipher-archive.gif
  Hoth-L-underattack-decipher-archive.gif
  ANH-L-undercover-decipher-archive.gif
  ANH-D-undercover-decipher-archive.gif
  ANH-D-urorrurrrshuntingrifle-decipher-archive.gif
  CloudCity-D-vadersbounty-decipher-archive.gif
  Premiere-D-vaderslightsaber-decipher-archive.gif
  Hoth-L-vehiclemine-decipher-archive.gif
  Hoth-D-vehiclemine-decipher-archive.gif
)
HT_FILES=(
  Premiere-D-tuskenraider.gif
  ANH-D-u3po.gif
  Premiere-D-ubrikkian9000z001.gif
  Dagobah-D-uncertainisthefuture.gif
  Hoth-L-underattack.gif
  ANH-L-undercover.gif
  ANH-D-undercover.gif
  ANH-D-urorrurrrshuntingrifle.gif
  CC-D-vadersbounty.gif
  Premiere-D-vaderslightsaber.gif
  Hoth-L-vehiclemine.gif
  Hoth-D-vehiclemine.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch33-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch33-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch33-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch33 (Tusken Raider through Vehicle Mine Dark); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch33-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch33-gifs
fi

edit "File:Premiere-D-tuskenraider-decipher-archive.gif" "$PAGES/File_Premiere-D-tuskenraider-decipher-archive.gif.wiki" "File: Decipher archive Original Tusken Raider"
edit "File:ANH-D-u3po-decipher-archive.gif" "$PAGES/File_ANH-D-u3po-decipher-archive.gif.wiki" "File: Decipher archive Original U-3PO (Yoo-Threepio)"
edit "File:Premiere-D-ubrikkian9000z001-decipher-archive.gif" "$PAGES/File_Premiere-D-ubrikkian9000z001-decipher-archive.gif.wiki" "File: Decipher archive Original Ubrikkian 9000 Z001"
edit "File:Dagobah-D-uncertainisthefuture-decipher-archive.gif" "$PAGES/File_Dagobah-D-uncertainisthefuture-decipher-archive.gif.wiki" "File: Decipher archive Original Uncertain Is The Future"
edit "File:Hoth-L-underattack-decipher-archive.gif" "$PAGES/File_Hoth-L-underattack-decipher-archive.gif.wiki" "File: Decipher archive Original Under Attack"
edit "File:ANH-L-undercover-decipher-archive.gif" "$PAGES/File_ANH-L-undercover-decipher-archive.gif.wiki" "File: Decipher archive Original Undercover"
edit "File:ANH-D-undercover-decipher-archive.gif" "$PAGES/File_ANH-D-undercover-decipher-archive.gif.wiki" "File: Decipher archive Original Undercover (Dark)"
edit "File:ANH-D-urorrurrrshuntingrifle-decipher-archive.gif" "$PAGES/File_ANH-D-urorrurrrshuntingrifle-decipher-archive.gif.wiki" "File: Decipher archive Original URoRRuR'R'R's Hunting Rifle"
edit "File:CloudCity-D-vadersbounty-decipher-archive.gif" "$PAGES/File_CloudCity-D-vadersbounty-decipher-archive.gif.wiki" "File: Decipher archive Original Vader's Bounty"
edit "File:Premiere-D-vaderslightsaber-decipher-archive.gif" "$PAGES/File_Premiere-D-vaderslightsaber-decipher-archive.gif.wiki" "File: Decipher archive Original Vader's Lightsaber"
edit "File:Hoth-L-vehiclemine-decipher-archive.gif" "$PAGES/File_Hoth-L-vehiclemine-decipher-archive.gif.wiki" "File: Decipher archive Original Vehicle Mine"
edit "File:Hoth-D-vehiclemine-decipher-archive.gif" "$PAGES/File_Hoth-D-vehiclemine-decipher-archive.gif.wiki" "File: Decipher archive Original Vehicle Mine (Dark)"

edit "Tusken Raider (Original)" "$PAGES/Tusken_Raider_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tusken Raider (PC Errata)" "$PAGES/Tusken_Raider_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tusken Raider" "$PAGES/Tusken_Raider.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "U-3PO (Yoo-Threepio) (Original)" "$PAGES/U-3PO_(Yoo-Threepio)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "U-3PO (Yoo-Threepio) (PC Errata)" "$PAGES/U-3PO_(Yoo-Threepio)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "U-3PO (Yoo-Threepio)" "$PAGES/U-3PO_(Yoo-Threepio).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Ubrikkian 9000 Z001 (Original)" "$PAGES/Ubrikkian_9000_Z001_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ubrikkian 9000 Z001 (PC Errata)" "$PAGES/Ubrikkian_9000_Z001_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ubrikkian 9000 Z001" "$PAGES/Ubrikkian_9000_Z001.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Uncertain Is The Future (Original)" "$PAGES/Uncertain_Is_The_Future_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Uncertain Is The Future (PC Errata)" "$PAGES/Uncertain_Is_The_Future_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Uncertain Is The Future" "$PAGES/Uncertain_Is_The_Future.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Under Attack (Original)" "$PAGES/Under_Attack_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Under Attack (PC Errata)" "$PAGES/Under_Attack_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Under Attack" "$PAGES/Under_Attack.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Undercover (Original)" "$PAGES/Undercover_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Undercover (PC Errata)" "$PAGES/Undercover_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Undercover" "$PAGES/Undercover.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Undercover (Dark) (Original)" "$PAGES/Undercover_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Undercover (Dark) (PC Errata)" "$PAGES/Undercover_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Undercover (Dark)" "$PAGES/Undercover_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "URoRRuR'R'R's Hunting Rifle (Original)" "$PAGES/URoRRuR'R'R's_Hunting_Rifle_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "URoRRuR'R'R's Hunting Rifle (PC Errata)" "$PAGES/URoRRuR'R'R's_Hunting_Rifle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "URoRRuR'R'R's Hunting Rifle" "$PAGES/URoRRuR'R'R's_Hunting_Rifle.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Vader's Bounty (Original)" "$PAGES/Vader's_Bounty_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vader's Bounty (PC Errata)" "$PAGES/Vader's_Bounty_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vader's Bounty" "$PAGES/Vader's_Bounty.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Vader's Lightsaber (Original)" "$PAGES/Vader's_Lightsaber_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vader's Lightsaber (PC Errata)" "$PAGES/Vader's_Lightsaber_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vader's Lightsaber" "$PAGES/Vader's_Lightsaber.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Vehicle Mine (Original)" "$PAGES/Vehicle_Mine_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vehicle Mine (PC Errata)" "$PAGES/Vehicle_Mine_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vehicle Mine" "$PAGES/Vehicle_Mine.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Vehicle Mine (Dark) (Original)" "$PAGES/Vehicle_Mine_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Vehicle Mine (Dark) (PC Errata)" "$PAGES/Vehicle_Mine_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Vehicle Mine (Dark)" "$PAGES/Vehicle_Mine_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch33 (Tusken Raider through Vehicle Mine Dark)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch33 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Tusken Raider" \
  "Tusken Raider (Original)" \
  "Tusken Raider (PC Errata)" \
  "U-3PO (Yoo-Threepio)" \
  "U-3PO (Yoo-Threepio) (Original)" \
  "U-3PO (Yoo-Threepio) (PC Errata)" \
  "Ubrikkian 9000 Z001" \
  "Ubrikkian 9000 Z001 (Original)" \
  "Ubrikkian 9000 Z001 (PC Errata)" \
  "Uncertain Is The Future" \
  "Uncertain Is The Future (Original)" \
  "Uncertain Is The Future (PC Errata)" \
  "Under Attack" \
  "Under Attack (Original)" \
  "Under Attack (PC Errata)" \
  "Undercover" \
  "Undercover (Original)" \
  "Undercover (PC Errata)" \
  "Undercover (Dark)" \
  "Undercover (Dark) (Original)" \
  "Undercover (Dark) (PC Errata)" \
  "URoRRuR'R'R's Hunting Rifle" \
  "URoRRuR'R'R's Hunting Rifle (Original)" \
  "URoRRuR'R'R's Hunting Rifle (PC Errata)" \
  "Vader's Bounty" \
  "Vader's Bounty (Original)" \
  "Vader's Bounty (PC Errata)" \
  "Vader's Lightsaber" \
  "Vader's Lightsaber (Original)" \
  "Vader's Lightsaber (PC Errata)" \
  "Vehicle Mine" \
  "Vehicle Mine (Original)" \
  "Vehicle Mine (PC Errata)" \
  "Vehicle Mine (Dark)" \
  "Vehicle Mine (Dark) (Original)" \
  "Vehicle Mine (Dark) (PC Errata)" \
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
echo DONE_APPLY_BATCH33_PC_ERRATA
