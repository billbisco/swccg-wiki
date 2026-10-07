#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch22-gifs

ARCHIVES=(
  CloudCity-D-landocalrissian-decipher-archive.gif
  Premiere-D-lonewarrior-decipher-archive.gif
  Premiere-L-linv8k-decipher-archive.gif
  Premiere-D-linv8m-decipher-archive.gif
  Hoth-D-lieutenantcabbel-decipher-archive.gif
  Premiere-D-lieutenanttanbris-decipher-archive.gif
  DeathStarII-L-lieutenanttelsij-decipher-archive.gif
  ANH-D-lirincarn-decipher-archive.gif
  Premiere-D-lightrepeatingblasterrifle-decipher-archive.gif
  Premiere-D-lonepilot-decipher-archive.gif
  Dagobah-D-lostinspace-decipher-archive.gif
  JabbasPalace-L-leslomytacema-decipher-archive.gif
  Premiere-D-localtrouble-decipher-archive.gif
)
HT_FILES=(
  CC-D-landocalrissian.gif
  Premiere-D-lonewarrior.gif
  Premiere-L-linv8k.gif
  Premiere-D-linv8m.gif
  Hoth-D-lieutenantcabbel.gif
  Premiere-D-lieutenanttanbris.gif
  DS2-L-lieutenanttelsij.gif
  ANH-D-lirincarn.gif
  Premiere-D-lightrepeatingblasterrifle.gif
  Premiere-D-lonepilot.gif
  Dagobah-D-lostinspace.gif
  JP-L-leslomytacema.gif
  Premiere-D-localtrouble.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch22-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch22-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch22-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch22 (Lando Calrissian Dark through Local Trouble); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch22-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch22-gifs
fi

edit "File:CloudCity-D-landocalrissian-decipher-archive.gif" "$PAGES/File_CloudCity-D-landocalrissian-decipher-archive.gif.wiki" "File: Decipher archive Original Lando Calrissian (Dark)"
edit "File:Premiere-D-lonewarrior-decipher-archive.gif" "$PAGES/File_Premiere-D-lonewarrior-decipher-archive.gif.wiki" "File: Decipher archive Original Lone Warrior"
edit "File:Premiere-L-linv8k-decipher-archive.gif" "$PAGES/File_Premiere-L-linv8k-decipher-archive.gif.wiki" "File: Decipher archive Original LIN-V8K (Elleyein-Veeatekay)"
edit "File:Premiere-D-linv8m-decipher-archive.gif" "$PAGES/File_Premiere-D-linv8m-decipher-archive.gif.wiki" "File: Decipher archive Original LIN-V8M (Elleyein-Veeateemm)"
edit "File:Hoth-D-lieutenantcabbel-decipher-archive.gif" "$PAGES/File_Hoth-D-lieutenantcabbel-decipher-archive.gif.wiki" "File: Decipher archive Original Lieutenant Cabbel"
edit "File:Premiere-D-lieutenanttanbris-decipher-archive.gif" "$PAGES/File_Premiere-D-lieutenanttanbris-decipher-archive.gif.wiki" "File: Decipher archive Original Lieutenant Tanbris"
edit "File:DeathStarII-L-lieutenanttelsij-decipher-archive.gif" "$PAGES/File_DeathStarII-L-lieutenanttelsij-decipher-archive.gif.wiki" "File: Decipher archive Original Lieutenant Telsij"
edit "File:ANH-D-lirincarn-decipher-archive.gif" "$PAGES/File_ANH-D-lirincarn-decipher-archive.gif.wiki" "File: Decipher archive Original Lirin Car'n"
edit "File:Premiere-D-lightrepeatingblasterrifle-decipher-archive.gif" "$PAGES/File_Premiere-D-lightrepeatingblasterrifle-decipher-archive.gif.wiki" "File: Decipher archive Original Light Repeating Blaster Rifle"
edit "File:Premiere-D-lonepilot-decipher-archive.gif" "$PAGES/File_Premiere-D-lonepilot-decipher-archive.gif.wiki" "File: Decipher archive Original Lone Pilot"
edit "File:Dagobah-D-lostinspace-decipher-archive.gif" "$PAGES/File_Dagobah-D-lostinspace-decipher-archive.gif.wiki" "File: Decipher archive Original Lost In Space"
edit "File:JabbasPalace-L-leslomytacema-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-leslomytacema-decipher-archive.gif.wiki" "File: Decipher archive Original Leslomy Tacema"
edit "File:Premiere-D-localtrouble-decipher-archive.gif" "$PAGES/File_Premiere-D-localtrouble-decipher-archive.gif.wiki" "File: Decipher archive Original Local Trouble"
edit "Lando Calrissian (Dark) (Original)" "$PAGES/Lando_Calrissian_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lando Calrissian (Dark) (PC Errata)" "$PAGES/Lando_Calrissian_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lando Calrissian (Dark)" "$PAGES/Lando_Calrissian_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lone Warrior (Original)" "$PAGES/Lone_Warrior_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lone Warrior (PC Errata)" "$PAGES/Lone_Warrior_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lone Warrior" "$PAGES/Lone_Warrior.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "LIN-V8K (Elleyein-Veeatekay) (Original)" "$PAGES/LIN-V8K_(Elleyein-Veeatekay)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "LIN-V8K (Elleyein-Veeatekay) (PC Errata)" "$PAGES/LIN-V8K_(Elleyein-Veeatekay)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "LIN-V8K (Elleyein-Veeatekay)" "$PAGES/LIN-V8K_(Elleyein-Veeatekay).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "LIN-V8M (Elleyein-Veeateemm) (Original)" "$PAGES/LIN-V8M_(Elleyein-Veeateemm)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "LIN-V8M (Elleyein-Veeateemm) (PC Errata)" "$PAGES/LIN-V8M_(Elleyein-Veeateemm)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "LIN-V8M (Elleyein-Veeateemm)" "$PAGES/LIN-V8M_(Elleyein-Veeateemm).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lieutenant Cabbel (Original)" "$PAGES/Lieutenant_Cabbel_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lieutenant Cabbel (PC Errata)" "$PAGES/Lieutenant_Cabbel_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lieutenant Cabbel" "$PAGES/Lieutenant_Cabbel.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lieutenant Tanbris (Original)" "$PAGES/Lieutenant_Tanbris_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lieutenant Tanbris (PC Errata)" "$PAGES/Lieutenant_Tanbris_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lieutenant Tanbris" "$PAGES/Lieutenant_Tanbris.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lieutenant Telsij (Original)" "$PAGES/Lieutenant_Telsij_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lieutenant Telsij (PC Errata)" "$PAGES/Lieutenant_Telsij_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lieutenant Telsij" "$PAGES/Lieutenant_Telsij.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lirin Car'n (Original)" "$PAGES/Lirin_Car'n_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lirin Car'n (PC Errata)" "$PAGES/Lirin_Car'n_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lirin Car'n" "$PAGES/Lirin_Car'n.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Light Repeating Blaster Rifle (Original)" "$PAGES/Light_Repeating_Blaster_Rifle_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Light Repeating Blaster Rifle (PC Errata)" "$PAGES/Light_Repeating_Blaster_Rifle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Light Repeating Blaster Rifle" "$PAGES/Light_Repeating_Blaster_Rifle.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lone Pilot (Original)" "$PAGES/Lone_Pilot_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lone Pilot (PC Errata)" "$PAGES/Lone_Pilot_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lone Pilot" "$PAGES/Lone_Pilot.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lost In Space (Original)" "$PAGES/Lost_In_Space_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lost In Space (PC Errata)" "$PAGES/Lost_In_Space_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lost In Space" "$PAGES/Lost_In_Space.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Leslomy Tacema (Original)" "$PAGES/Leslomy_Tacema_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Leslomy Tacema (PC Errata)" "$PAGES/Leslomy_Tacema_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Leslomy Tacema" "$PAGES/Leslomy_Tacema.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Local Trouble (Original)" "$PAGES/Local_Trouble_(Original).wiki" "PC Errata seed: printed Decipher archive Original (create)"
edit "Local Trouble (PC Errata)" "$PAGES/Local_Trouble_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable (create)"
edit "Local Trouble" "$PAGES/Local_Trouble.wiki" "Create bare + Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch22 (Lando Calrissian Dark through Local Trouble)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch22 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Lando Calrissian (Dark)" \
  "Lando Calrissian (Dark) (Original)" \
  "Lando Calrissian (Dark) (PC Errata)" \
  "Lone Warrior" \
  "Lone Warrior (Original)" \
  "Lone Warrior (PC Errata)" \
  "LIN-V8K (Elleyein-Veeatekay)" \
  "LIN-V8K (Elleyein-Veeatekay) (Original)" \
  "LIN-V8K (Elleyein-Veeatekay) (PC Errata)" \
  "LIN-V8M (Elleyein-Veeateemm)" \
  "LIN-V8M (Elleyein-Veeateemm) (Original)" \
  "LIN-V8M (Elleyein-Veeateemm) (PC Errata)" \
  "Lieutenant Cabbel" \
  "Lieutenant Cabbel (Original)" \
  "Lieutenant Cabbel (PC Errata)" \
  "Lieutenant Tanbris" \
  "Lieutenant Tanbris (Original)" \
  "Lieutenant Tanbris (PC Errata)" \
  "Lieutenant Telsij" \
  "Lieutenant Telsij (Original)" \
  "Lieutenant Telsij (PC Errata)" \
  "Lirin Car'n" \
  "Lirin Car'n (Original)" \
  "Lirin Car'n (PC Errata)" \
  "Light Repeating Blaster Rifle" \
  "Light Repeating Blaster Rifle (Original)" \
  "Light Repeating Blaster Rifle (PC Errata)" \
  "Lone Pilot" \
  "Lone Pilot (Original)" \
  "Lone Pilot (PC Errata)" \
  "Lost In Space" \
  "Lost In Space (Original)" \
  "Lost In Space (PC Errata)" \
  "Leslomy Tacema" \
  "Leslomy Tacema (Original)" \
  "Leslomy Tacema (PC Errata)" \
  "Local Trouble" \
  "Local Trouble (Original)" \
  "Local Trouble (PC Errata)" \
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
echo DONE_APPLY_BATCH22_PC_ERRATA
