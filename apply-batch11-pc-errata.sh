#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch11-gifs

ARCHIVES=(
  Premiere-L-disarmed-decipher-archive.gif
  Premiere-D-disarmed-decipher-archive.gif
  JP-D-doublelasercannon-decipher-archive.gif
  Premiere-D-drevazan-decipher-archive.gif
  Premiere-L-dontgetcocky-decipher-archive.gif
  ANH-L-doubleagent-decipher-archive.gif
  Premiere-D-ds612-decipher-archive.gif
  Premiere-D-ds613-decipher-archive.gif
  ANH-D-ds614-decipher-archive.gif
  Premiere-L-dutch-decipher-archive.gif
  Premiere-D-droiddetector-decipher-archive.gif
  SE-L-droidmerchant-decipher-archive.gif
  Premiere-L-droidshutdown-decipher-archive.gif
  Premiere-D-dantooinedark-decipher-archive.gif
  SE-D-dagobah-decipher-archive.gif
)
HT_FILES=(
  Premiere-L-disarmed.gif
  Premiere-D-disarmed.gif
  JP-D-doublelasercannon.gif
  Premiere-D-drevazan.gif
  Premiere-L-dontgetcocky.gif
  ANH-L-doubleagent.gif
  Premiere-D-ds612.gif
  Premiere-D-ds613.gif
  ANH-D-ds614.gif
  Premiere-L-dutch.gif
  Premiere-D-droiddetector.gif
  SE-L-droidmerchant.gif
  Premiere-L-droidshutdown.gif
  Premiere-D-dantooine.gif
  SE-D-dagobah.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch11-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch11-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch11-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch11 (Disarmed L/D, Double Laser Cannon, Dr. Evazan, Don't Get Cocky, Double Agent, DS-61-2/3/4, Dutch, Droid Detector, Droid Merchant, Droid Shutdown, Dantooine Dark, Dagobah Dark); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch11-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch11-gifs
fi

edit "File:Premiere-L-disarmed-decipher-archive.gif" "$PAGES/File_Premiere-L-disarmed-decipher-archive.gif.wiki" "File: Decipher archive Original Disarmed"
edit "File:Premiere-D-disarmed-decipher-archive.gif" "$PAGES/File_Premiere-D-disarmed-decipher-archive.gif.wiki" "File: Decipher archive Original Disarmed (Dark)"
edit "File:JP-D-doublelasercannon-decipher-archive.gif" "$PAGES/File_JP-D-doublelasercannon-decipher-archive.gif.wiki" "File: Decipher archive Original Double Laser Cannon"
edit "File:Premiere-D-drevazan-decipher-archive.gif" "$PAGES/File_Premiere-D-drevazan-decipher-archive.gif.wiki" "File: Decipher archive Original Dr. Evazan"
edit "File:Premiere-L-dontgetcocky-decipher-archive.gif" "$PAGES/File_Premiere-L-dontgetcocky-decipher-archive.gif.wiki" "File: Decipher archive Original Don't Get Cocky"
edit "File:ANH-L-doubleagent-decipher-archive.gif" "$PAGES/File_ANH-L-doubleagent-decipher-archive.gif.wiki" "File: Decipher archive Original Double Agent"
edit "File:Premiere-D-ds612-decipher-archive.gif" "$PAGES/File_Premiere-D-ds612-decipher-archive.gif.wiki" "File: Decipher archive Original DS-61-2"
edit "File:Premiere-D-ds613-decipher-archive.gif" "$PAGES/File_Premiere-D-ds613-decipher-archive.gif.wiki" "File: Decipher archive Original DS-61-3"
edit "File:ANH-D-ds614-decipher-archive.gif" "$PAGES/File_ANH-D-ds614-decipher-archive.gif.wiki" "File: Decipher archive Original DS-61-4"
edit "File:Premiere-L-dutch-decipher-archive.gif" "$PAGES/File_Premiere-L-dutch-decipher-archive.gif.wiki" "File: Decipher archive Original Dutch"
edit "File:Premiere-D-droiddetector-decipher-archive.gif" "$PAGES/File_Premiere-D-droiddetector-decipher-archive.gif.wiki" "File: Decipher archive Original Droid Detector"
edit "File:SE-L-droidmerchant-decipher-archive.gif" "$PAGES/File_SE-L-droidmerchant-decipher-archive.gif.wiki" "File: Decipher archive Original Droid Merchant"
edit "File:Premiere-L-droidshutdown-decipher-archive.gif" "$PAGES/File_Premiere-L-droidshutdown-decipher-archive.gif.wiki" "File: Decipher archive Original Droid Shutdown"
edit "File:Premiere-D-dantooinedark-decipher-archive.gif" "$PAGES/File_Premiere-D-dantooinedark-decipher-archive.gif.wiki" "File: Decipher archive Original Dantooine (Dark)"
edit "File:SE-D-dagobah-decipher-archive.gif" "$PAGES/File_SE-D-dagobah-decipher-archive.gif.wiki" "File: Decipher archive Original Dagobah (Dark)"

edit "Disarmed (Original)" "$PAGES/Disarmed_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Disarmed (PC Errata)" "$PAGES/Disarmed_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Disarmed" "$PAGES/Disarmed.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Disarmed (Dark) (Original)" "$PAGES/Disarmed_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Disarmed (Dark) (PC Errata)" "$PAGES/Disarmed_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Disarmed (Dark)" "$PAGES/Disarmed_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Double Laser Cannon (Original)" "$PAGES/Double_Laser_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Double Laser Cannon (PC Errata)" "$PAGES/Double_Laser_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Double Laser Cannon" "$PAGES/Double_Laser_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dr. Evazan (Original)" "$PAGES/Dr._Evazan_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dr. Evazan (PC Errata)" "$PAGES/Dr._Evazan_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dr. Evazan" "$PAGES/Dr._Evazan.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Don't Get Cocky (Original)" "$PAGES/Don't_Get_Cocky_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Don't Get Cocky (PC Errata)" "$PAGES/Don't_Get_Cocky_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Don't Get Cocky" "$PAGES/Don't_Get_Cocky.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Double Agent (Original)" "$PAGES/Double_Agent_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Double Agent (PC Errata)" "$PAGES/Double_Agent_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Double Agent" "$PAGES/Double_Agent.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "DS-61-2 (Original)" "$PAGES/DS-61-2_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "DS-61-2 (PC Errata)" "$PAGES/DS-61-2_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "DS-61-2" "$PAGES/DS-61-2.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "DS-61-3 (Original)" "$PAGES/DS-61-3_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "DS-61-3 (PC Errata)" "$PAGES/DS-61-3_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "DS-61-3" "$PAGES/DS-61-3.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "DS-61-4 (Original)" "$PAGES/DS-61-4_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "DS-61-4 (PC Errata)" "$PAGES/DS-61-4_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "DS-61-4" "$PAGES/DS-61-4.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dutch (Original)" "$PAGES/Dutch_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dutch (PC Errata)" "$PAGES/Dutch_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dutch" "$PAGES/Dutch.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Droid Detector (Original)" "$PAGES/Droid_Detector_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Droid Detector (PC Errata)" "$PAGES/Droid_Detector_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Droid Detector" "$PAGES/Droid_Detector.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Droid Merchant (Original)" "$PAGES/Droid_Merchant_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Droid Merchant (PC Errata)" "$PAGES/Droid_Merchant_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Droid Merchant" "$PAGES/Droid_Merchant.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Droid Shutdown (Original)" "$PAGES/Droid_Shutdown_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Droid Shutdown (PC Errata)" "$PAGES/Droid_Shutdown_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Droid Shutdown" "$PAGES/Droid_Shutdown.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dantooine (Dark) (Original)" "$PAGES/Dantooine_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dantooine (Dark) (PC Errata)" "$PAGES/Dantooine_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dantooine (Dark)" "$PAGES/Dantooine_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dagobah (Dark) (Original)" "$PAGES/Dagobah_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dagobah (Dark) (PC Errata)" "$PAGES/Dagobah_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dagobah (Dark)" "$PAGES/Dagobah_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch11 (Disarmed through Dagobah Dark)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch11 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Disarmed" \
  "Disarmed (Original)" \
  "Disarmed (PC Errata)" \
  "Disarmed (Dark)" \
  "Disarmed (Dark) (Original)" \
  "Disarmed (Dark) (PC Errata)" \
  "Double Laser Cannon" \
  "Double Laser Cannon (Original)" \
  "Double Laser Cannon (PC Errata)" \
  "Dr. Evazan" \
  "Dr. Evazan (Original)" \
  "Dr. Evazan (PC Errata)" \
  "Don't Get Cocky" \
  "Don't Get Cocky (Original)" \
  "Don't Get Cocky (PC Errata)" \
  "Double Agent" \
  "Double Agent (Original)" \
  "Double Agent (PC Errata)" \
  "DS-61-2" \
  "DS-61-2 (Original)" \
  "DS-61-2 (PC Errata)" \
  "DS-61-3" \
  "DS-61-3 (Original)" \
  "DS-61-3 (PC Errata)" \
  "DS-61-4" \
  "DS-61-4 (Original)" \
  "DS-61-4 (PC Errata)" \
  "Dutch" \
  "Dutch (Original)" \
  "Dutch (PC Errata)" \
  "Droid Detector" \
  "Droid Detector (Original)" \
  "Droid Detector (PC Errata)" \
  "Droid Merchant" \
  "Droid Merchant (Original)" \
  "Droid Merchant (PC Errata)" \
  "Droid Shutdown" \
  "Droid Shutdown (Original)" \
  "Droid Shutdown (PC Errata)" \
  "Dantooine (Dark)" \
  "Dantooine (Dark) (Original)" \
  "Dantooine (Dark) (PC Errata)" \
  "Dagobah (Dark)" \
  "Dagobah (Dark) (Original)" \
  "Dagobah (Dark) (PC Errata)" \
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
echo DONE_APPLY_BATCH11_PC_ERRATA
