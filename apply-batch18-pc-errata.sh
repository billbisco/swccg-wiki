#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch18-gifs

ARCHIVES=(
  Hoth-D-imperialgunner-decipher-archive.gif
  Dagobah-D-imperialhelmsman-decipher-archive.gif
  Premiere-D-imperialpilot-decipher-archive.gif
  Premiere-D-imperialblaster-decipher-archive.gif
  Premiere-D-imperialreinforcements-decipher-archive.gif
  ANewHope-D-imperialsquadleader-decipher-archive.gif
  Hoth-D-idjustassoonkissawookiee-decipher-archive.gif
  Premiere-D-ifindyourlackoffaith-decipher-archive.gif
  Dagobah-D-ig88-decipher-archive.gif
  Dagobah-D-ig2000-decipher-archive.gif
  Dagobah-D-ig88spulsecannon-decipher-archive.gif
  ANewHope-L-imheretorescueyou-decipher-archive.gif
)
HT_FILES=(
  Hoth-D-imperialgunner.gif
  Dagobah-D-imperialhelmsman.gif
  Premiere-D-imperialpilot.gif
  Premiere-D-imperialblaster.gif
  Premiere-D-imperialreinforcements.gif
  ANH-D-imperialsquadleader.gif
  Hoth-D-idjustassoonkissawookiee.gif
  Premiere-D-ifindyourlackoffaithdisturbing.gif
  Dagobah-D-ig88.gif
  Dagobah-D-ig2000.gif
  Dagobah-D-ig88spulsecannon.gif
  ANH-L-imheretorescueyou.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch18-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch18-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch18-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch18 (Imperial Gunner through Im Here To Rescue You); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch18-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch18-gifs
fi

edit "File:Hoth-D-imperialgunner-decipher-archive.gif" "$PAGES/File_Hoth-D-imperialgunner-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Gunner"
edit "File:Dagobah-D-imperialhelmsman-decipher-archive.gif" "$PAGES/File_Dagobah-D-imperialhelmsman-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Helmsman"
edit "File:Premiere-D-imperialpilot-decipher-archive.gif" "$PAGES/File_Premiere-D-imperialpilot-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Pilot"
edit "File:Premiere-D-imperialblaster-decipher-archive.gif" "$PAGES/File_Premiere-D-imperialblaster-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Blaster"
edit "File:Premiere-D-imperialreinforcements-decipher-archive.gif" "$PAGES/File_Premiere-D-imperialreinforcements-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Reinforcements"
edit "File:ANewHope-D-imperialsquadleader-decipher-archive.gif" "$PAGES/File_ANewHope-D-imperialsquadleader-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Squad Leader"
edit "File:Hoth-D-idjustassoonkissawookiee-decipher-archive.gif" "$PAGES/File_Hoth-D-idjustassoonkissawookiee-decipher-archive.gif.wiki" "File: Decipher archive Original I'd Just As Soon Kiss A Wookiee"
edit "File:Premiere-D-ifindyourlackoffaith-decipher-archive.gif" "$PAGES/File_Premiere-D-ifindyourlackoffaith-decipher-archive.gif.wiki" "File: Decipher archive Original I Find Your Lack Of Faith Disturbing"
edit "File:Dagobah-D-ig88-decipher-archive.gif" "$PAGES/File_Dagobah-D-ig88-decipher-archive.gif.wiki" "File: Decipher archive Original IG-88"
edit "File:Dagobah-D-ig2000-decipher-archive.gif" "$PAGES/File_Dagobah-D-ig2000-decipher-archive.gif.wiki" "File: Decipher archive Original IG-2000"
edit "File:Dagobah-D-ig88spulsecannon-decipher-archive.gif" "$PAGES/File_Dagobah-D-ig88spulsecannon-decipher-archive.gif.wiki" "File: Decipher archive Original IG-88's Pulse Cannon"
edit "File:ANewHope-L-imheretorescueyou-decipher-archive.gif" "$PAGES/File_ANewHope-L-imheretorescueyou-decipher-archive.gif.wiki" "File: Decipher archive Original I'm Here To Rescue You"
edit "Imperial Gunner (Original)" "$PAGES/Imperial_Gunner_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Gunner (PC Errata)" "$PAGES/Imperial_Gunner_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Gunner" "$PAGES/Imperial_Gunner.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Imperial Helmsman (Original)" "$PAGES/Imperial_Helmsman_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Helmsman (PC Errata)" "$PAGES/Imperial_Helmsman_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Helmsman" "$PAGES/Imperial_Helmsman.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Imperial Pilot (Original)" "$PAGES/Imperial_Pilot_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Pilot (PC Errata)" "$PAGES/Imperial_Pilot_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Pilot" "$PAGES/Imperial_Pilot.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Imperial Blaster (Original)" "$PAGES/Imperial_Blaster_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Blaster (PC Errata)" "$PAGES/Imperial_Blaster_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Blaster" "$PAGES/Imperial_Blaster.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Imperial Reinforcements (Original)" "$PAGES/Imperial_Reinforcements_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Reinforcements (PC Errata)" "$PAGES/Imperial_Reinforcements_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Reinforcements" "$PAGES/Imperial_Reinforcements.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Imperial Squad Leader (Original)" "$PAGES/Imperial_Squad_Leader_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Squad Leader (PC Errata)" "$PAGES/Imperial_Squad_Leader_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Squad Leader" "$PAGES/Imperial_Squad_Leader.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "I'd Just As Soon Kiss A Wookiee (Original)" "$PAGES/I'd_Just_As_Soon_Kiss_A_Wookiee_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I'd Just As Soon Kiss A Wookiee (PC Errata)" "$PAGES/I'd_Just_As_Soon_Kiss_A_Wookiee_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I'd Just As Soon Kiss A Wookiee" "$PAGES/I'd_Just_As_Soon_Kiss_A_Wookiee.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "I Find Your Lack Of Faith Disturbing (Original)" "$PAGES/I_Find_Your_Lack_Of_Faith_Disturbing_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I Find Your Lack Of Faith Disturbing (PC Errata)" "$PAGES/I_Find_Your_Lack_Of_Faith_Disturbing_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I Find Your Lack Of Faith Disturbing" "$PAGES/I_Find_Your_Lack_Of_Faith_Disturbing.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "IG-88 (Original)" "$PAGES/IG-88_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "IG-88 (PC Errata)" "$PAGES/IG-88_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "IG-88" "$PAGES/IG-88.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "IG-2000 (Original)" "$PAGES/IG-2000_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "IG-2000 (PC Errata)" "$PAGES/IG-2000_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "IG-2000" "$PAGES/IG-2000.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "IG-88's Pulse Cannon (Original)" "$PAGES/IG-88's_Pulse_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "IG-88's Pulse Cannon (PC Errata)" "$PAGES/IG-88's_Pulse_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "IG-88's Pulse Cannon" "$PAGES/IG-88's_Pulse_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "I'm Here To Rescue You (Original)" "$PAGES/I'm_Here_To_Rescue_You_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I'm Here To Rescue You (PC Errata)" "$PAGES/I'm_Here_To_Rescue_You_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I'm Here To Rescue You" "$PAGES/I'm_Here_To_Rescue_You.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch18 (Imperial Gunner through Im Here To Rescue You)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch18 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Imperial Gunner" \
  "Imperial Gunner (Original)" \
  "Imperial Gunner (PC Errata)" \
  "Imperial Helmsman" \
  "Imperial Helmsman (Original)" \
  "Imperial Helmsman (PC Errata)" \
  "Imperial Pilot" \
  "Imperial Pilot (Original)" \
  "Imperial Pilot (PC Errata)" \
  "Imperial Blaster" \
  "Imperial Blaster (Original)" \
  "Imperial Blaster (PC Errata)" \
  "Imperial Reinforcements" \
  "Imperial Reinforcements (Original)" \
  "Imperial Reinforcements (PC Errata)" \
  "Imperial Squad Leader" \
  "Imperial Squad Leader (Original)" \
  "Imperial Squad Leader (PC Errata)" \
  "I'd Just As Soon Kiss A Wookiee" \
  "I'd Just As Soon Kiss A Wookiee (Original)" \
  "I'd Just As Soon Kiss A Wookiee (PC Errata)" \
  "I Find Your Lack Of Faith Disturbing" \
  "I Find Your Lack Of Faith Disturbing (Original)" \
  "I Find Your Lack Of Faith Disturbing (PC Errata)" \
  "IG-88" \
  "IG-88 (Original)" \
  "IG-88 (PC Errata)" \
  "IG-2000" \
  "IG-2000 (Original)" \
  "IG-2000 (PC Errata)" \
  "IG-88's Pulse Cannon" \
  "IG-88's Pulse Cannon (Original)" \
  "IG-88's Pulse Cannon (PC Errata)" \
  "I'm Here To Rescue You" \
  "I'm Here To Rescue You (Original)" \
  "I'm Here To Rescue You (PC Errata)" \
  "Errata" "PC Errata"
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
echo DONE_APPLY_BATCH18_PC_ERRATA
