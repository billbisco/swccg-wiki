#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch6-gifs

ARCHIVES=(
  CC-D-carbonitechamberconsole-decipher-archive.gif
  JP-D-caneadiss-decipher-archive.gif
  Dagobah-D-captainneeda-decipher-archive.gif
  Dagobah-D-bossk-decipher-archive.gif
  CC-D-bounty-decipher-archive.gif
  ANH-L-bowcaster-decipher-archive.gif
  CC-D-bobafettsblasterrifle-decipher-archive.gif
  ANH-D-besieged-decipher-archive.gif
  Premiere-D-boostedtiecannon-decipher-archive.gif
  ANH-D-captainkhurgee-decipher-archive.gif
  Hoth-D-captainlennox-decipher-archive.gif
  Hoth-D-captainpiett-decipher-archive.gif
)
HT_FILES=(
  CC-D-carbonitechamberconsole.gif
  JP-D-caneadiss.gif
  Dagobah-D-captainneeda.gif
  Dagobah-D-bossk.gif
  CC-D-bounty.gif
  ANH-L-bowcaster.gif
  CC-D-bobafettsblasterrifle.gif
  ANH-D-besieged.gif
  Premiere-D-boostedtiecannon.gif
  ANH-D-captainkhurgee.gif
  Hoth-D-captainlennox.gif
  Hoth-D-captainpiett.gif
)

strip_bom() {
  python3 - "$1" <<'PY'
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
PY
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch6-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch6-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch6-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch6 (Carbonite Chamber Console, Cane Adiss, Captain Needa, Bossk, Bounty, Bowcaster, Boba Fetts Blaster Rifle, Besieged, Boosted TIE Cannon, Captain Khurgee, Captain Lennox, Captain Piett); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch6-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch6-gifs
fi

edit "File:CC-D-carbonitechamberconsole-decipher-archive.gif" "$PAGES/File_CC-D-carbonitechamberconsole-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Carbonite Chamber Console"
edit "File:JP-D-caneadiss-decipher-archive.gif" "$PAGES/File_JP-D-caneadiss-decipher-archive.gif.wiki" "File: Decipher Jabba archive Original Cane Adiss"
edit "File:Dagobah-D-captainneeda-decipher-archive.gif" "$PAGES/File_Dagobah-D-captainneeda-decipher-archive.gif.wiki" "File: Decipher Dagobah archive Original Captain Needa"
edit "File:Dagobah-D-bossk-decipher-archive.gif" "$PAGES/File_Dagobah-D-bossk-decipher-archive.gif.wiki" "File: Decipher Dagobah archive Original Bossk"
edit "File:CC-D-bounty-decipher-archive.gif" "$PAGES/File_CC-D-bounty-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Bounty"
edit "File:ANH-L-bowcaster-decipher-archive.gif" "$PAGES/File_ANH-L-bowcaster-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Bowcaster"
edit "File:CC-D-bobafettsblasterrifle-decipher-archive.gif" "$PAGES/File_CC-D-bobafettsblasterrifle-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Boba Fett's Blaster Rifle"
edit "File:ANH-D-besieged-decipher-archive.gif" "$PAGES/File_ANH-D-besieged-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Besieged"
edit "File:Premiere-D-boostedtiecannon-decipher-archive.gif" "$PAGES/File_Premiere-D-boostedtiecannon-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Boosted TIE Cannon"
edit "File:ANH-D-captainkhurgee-decipher-archive.gif" "$PAGES/File_ANH-D-captainkhurgee-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Captain Khurgee"
edit "File:Hoth-D-captainlennox-decipher-archive.gif" "$PAGES/File_Hoth-D-captainlennox-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Captain Lennox"
edit "File:Hoth-D-captainpiett-decipher-archive.gif" "$PAGES/File_Hoth-D-captainpiett-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Captain Piett"

edit "Carbonite Chamber Console (Original)" "$PAGES/Carbonite_Chamber_Console_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Carbonite Chamber Console (PC Errata)" "$PAGES/Carbonite_Chamber_Console_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Carbonite Chamber Console" "$PAGES/Carbonite_Chamber_Console.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Cane Adiss (Original)" "$PAGES/Cane_Adiss_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Cane Adiss (PC Errata)" "$PAGES/Cane_Adiss_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Cane Adiss" "$PAGES/Cane_Adiss.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Captain Needa (Original)" "$PAGES/Captain_Needa_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Captain Needa (PC Errata)" "$PAGES/Captain_Needa_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Captain Needa" "$PAGES/Captain_Needa.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Bossk (Original)" "$PAGES/Bossk_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Bossk (PC Errata)" "$PAGES/Bossk_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Bossk" "$PAGES/Bossk.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Bounty (Original)" "$PAGES/Bounty_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Bounty (PC Errata)" "$PAGES/Bounty_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Bounty" "$PAGES/Bounty.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Bowcaster (Original)" "$PAGES/Bowcaster_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Bowcaster (PC Errata)" "$PAGES/Bowcaster_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Bowcaster" "$PAGES/Bowcaster.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Boba Fett's Blaster Rifle (Original)" "$PAGES/Boba_Fett's_Blaster_Rifle_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Boba Fett's Blaster Rifle (PC Errata)" "$PAGES/Boba_Fett's_Blaster_Rifle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Boba Fett's Blaster Rifle" "$PAGES/Boba_Fett's_Blaster_Rifle.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Besieged (Original)" "$PAGES/Besieged_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Besieged (PC Errata)" "$PAGES/Besieged_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Besieged" "$PAGES/Besieged.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Boosted TIE Cannon (Original)" "$PAGES/Boosted_TIE_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Boosted TIE Cannon (PC Errata)" "$PAGES/Boosted_TIE_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Boosted TIE Cannon" "$PAGES/Boosted_TIE_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Captain Khurgee (Original)" "$PAGES/Captain_Khurgee_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Captain Khurgee (PC Errata)" "$PAGES/Captain_Khurgee_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Captain Khurgee" "$PAGES/Captain_Khurgee.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Captain Lennox (Original)" "$PAGES/Captain_Lennox_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Captain Lennox (PC Errata)" "$PAGES/Captain_Lennox_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Captain Lennox" "$PAGES/Captain_Lennox.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Captain Piett (Original)" "$PAGES/Captain_Piett_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Captain Piett (PC Errata)" "$PAGES/Captain_Piett_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Captain Piett" "$PAGES/Captain_Piett.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch6 (Carbonite Chamber Console through Captain Piett)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch6 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Carbonite Chamber Console" "Carbonite Chamber Console (Original)" "Carbonite Chamber Console (PC Errata)" \
  "Cane Adiss" "Cane Adiss (Original)" "Cane Adiss (PC Errata)" \
  "Captain Needa" "Captain Needa (Original)" "Captain Needa (PC Errata)" \
  "Bossk" "Bossk (Original)" "Bossk (PC Errata)" \
  "Bounty" "Bounty (Original)" "Bounty (PC Errata)" \
  "Bowcaster" "Bowcaster (Original)" "Bowcaster (PC Errata)" \
  "Boba Fett's Blaster Rifle" "Boba Fett's Blaster Rifle (Original)" "Boba Fett's Blaster Rifle (PC Errata)" \
  "Besieged" "Besieged (Original)" "Besieged (PC Errata)" \
  "Boosted TIE Cannon" "Boosted TIE Cannon (Original)" "Boosted TIE Cannon (PC Errata)" \
  "Captain Khurgee" "Captain Khurgee (Original)" "Captain Khurgee (PC Errata)" \
  "Captain Lennox" "Captain Lennox (Original)" "Captain Lennox (PC Errata)" \
  "Captain Piett" "Captain Piett (Original)" "Captain Piett (PC Errata)" \
  Errata "PC Errata"
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
echo DONE_APPLY_BATCH6_PC_ERRATA
