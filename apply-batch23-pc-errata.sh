#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch23-gifs

ARCHIVES=(
  Premiere-D-lukeseeker-decipher-archive.gif
  CloudCity-L-lukesblasterpistol-decipher-archive.gif
  ANH-L-lukescape-decipher-archive.gif
  ANH-L-lukeshuntingrifle-decipher-archive.gif
  Premiere-L-lukesx34landspeeder-decipher-archive.gif
  ANH-D-ltpoltreidum-decipher-archive.gif
  ANH-L-magneticsuctiontube-decipher-archive.gif
  ANH-D-magneticsuctiontube-decipher-archive.gif
  Hoth-L-majorbrenderlin-decipher-archive.gif
  ANH-L-mercsunlet-decipher-archive.gif
  Premiere-D-miiyoomonith-decipher-archive.gif
  Dagobah-D-locationlocationlocation-decipher-archive.gif
  Hoth-L-mediumrepeatingblastercannon-decipher-archive.gif
)
HT_FILES=(
  Premiere-D-lukeseeker.gif
  CC-L-lukesblasterpistol.gif
  ANH-L-lukescape.gif
  ANH-L-lukeshuntingrifle.gif
  Premiere-L-lukesx34landspeeder.gif
  ANH-D-ltpoltreidum.gif
  ANH-L-magneticsuctiontube.gif
  ANH-D-magneticsuctiontube.gif
  Hoth-L-majorbrenderlin.gif
  ANH-L-mercsunlet.gif
  Premiere-D-miiyoomonith.gif
  Dagobah-D-locationlocationlocation.gif
  Hoth-L-mediumrepeatingblastercannon.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch23-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch23-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch23-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch23 (Luke Seeker through Medium Repeating Blaster Cannon); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch23-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch23-gifs
fi

edit "File:Premiere-D-lukeseeker-decipher-archive.gif" "$PAGES/File_Premiere-D-lukeseeker-decipher-archive.gif.wiki" "File: Decipher archive Original Luke Seeker"
edit "File:CloudCity-L-lukesblasterpistol-decipher-archive.gif" "$PAGES/File_CloudCity-L-lukesblasterpistol-decipher-archive.gif.wiki" "File: Decipher archive Original Luke's Blaster Pistol"
edit "File:ANH-L-lukescape-decipher-archive.gif" "$PAGES/File_ANH-L-lukescape-decipher-archive.gif.wiki" "File: Decipher archive Original Luke's Cape"
edit "File:ANH-L-lukeshuntingrifle-decipher-archive.gif" "$PAGES/File_ANH-L-lukeshuntingrifle-decipher-archive.gif.wiki" "File: Decipher archive Original Luke's Hunting Rifle"
edit "File:Premiere-L-lukesx34landspeeder-decipher-archive.gif" "$PAGES/File_Premiere-L-lukesx34landspeeder-decipher-archive.gif.wiki" "File: Decipher archive Original Luke's X-34 Landspeeder"
edit "File:ANH-D-ltpoltreidum-decipher-archive.gif" "$PAGES/File_ANH-D-ltpoltreidum-decipher-archive.gif.wiki" "File: Decipher archive Original Lt. Pol Treidum"
edit "File:ANH-L-magneticsuctiontube-decipher-archive.gif" "$PAGES/File_ANH-L-magneticsuctiontube-decipher-archive.gif.wiki" "File: Decipher archive Original Magnetic Suction Tube"
edit "File:ANH-D-magneticsuctiontube-decipher-archive.gif" "$PAGES/File_ANH-D-magneticsuctiontube-decipher-archive.gif.wiki" "File: Decipher archive Original Magnetic Suction Tube (Dark)"
edit "File:Hoth-L-majorbrenderlin-decipher-archive.gif" "$PAGES/File_Hoth-L-majorbrenderlin-decipher-archive.gif.wiki" "File: Decipher archive Original Major Bren Derlin"
edit "File:ANH-L-mercsunlet-decipher-archive.gif" "$PAGES/File_ANH-L-mercsunlet-decipher-archive.gif.wiki" "File: Decipher archive Original Merc Sunlet"
edit "File:Premiere-D-miiyoomonith-decipher-archive.gif" "$PAGES/File_Premiere-D-miiyoomonith-decipher-archive.gif.wiki" "File: Decipher archive Original M'iiyoom Onith"
edit "File:Dagobah-D-locationlocationlocation-decipher-archive.gif" "$PAGES/File_Dagobah-D-locationlocationlocation-decipher-archive.gif.wiki" "File: Decipher archive Original Location, Location, Location"
edit "File:Hoth-L-mediumrepeatingblastercannon-decipher-archive.gif" "$PAGES/File_Hoth-L-mediumrepeatingblastercannon-decipher-archive.gif.wiki" "File: Decipher archive Original Medium Repeating Blaster Cannon"
edit "Luke Seeker (Original)" "$PAGES/Luke_Seeker_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Luke Seeker (PC Errata)" "$PAGES/Luke_Seeker_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Luke Seeker" "$PAGES/Luke_Seeker.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Luke's Blaster Pistol (Original)" "$PAGES/Luke's_Blaster_Pistol_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Luke's Blaster Pistol (PC Errata)" "$PAGES/Luke's_Blaster_Pistol_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Luke's Blaster Pistol" "$PAGES/Luke's_Blaster_Pistol.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Luke's Cape (Original)" "$PAGES/Luke's_Cape_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Luke's Cape (PC Errata)" "$PAGES/Luke's_Cape_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Luke's Cape" "$PAGES/Luke's_Cape.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Luke's Hunting Rifle (Original)" "$PAGES/Luke's_Hunting_Rifle_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Luke's Hunting Rifle (PC Errata)" "$PAGES/Luke's_Hunting_Rifle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Luke's Hunting Rifle" "$PAGES/Luke's_Hunting_Rifle.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Luke's X-34 Landspeeder (Original)" "$PAGES/Luke's_X-34_Landspeeder_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Luke's X-34 Landspeeder (PC Errata)" "$PAGES/Luke's_X-34_Landspeeder_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Luke's X-34 Landspeeder" "$PAGES/Luke's_X-34_Landspeeder.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Lt. Pol Treidum (Original)" "$PAGES/Lt._Pol_Treidum_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lt. Pol Treidum (PC Errata)" "$PAGES/Lt._Pol_Treidum_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lt. Pol Treidum" "$PAGES/Lt._Pol_Treidum.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Magnetic Suction Tube (Original)" "$PAGES/Magnetic_Suction_Tube_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Magnetic Suction Tube (PC Errata)" "$PAGES/Magnetic_Suction_Tube_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Magnetic Suction Tube" "$PAGES/Magnetic_Suction_Tube.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Magnetic Suction Tube (Dark) (Original)" "$PAGES/Magnetic_Suction_Tube_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Magnetic Suction Tube (Dark) (PC Errata)" "$PAGES/Magnetic_Suction_Tube_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Magnetic Suction Tube (Dark)" "$PAGES/Magnetic_Suction_Tube_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Major Bren Derlin (Original)" "$PAGES/Major_Bren_Derlin_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Major Bren Derlin (PC Errata)" "$PAGES/Major_Bren_Derlin_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Major Bren Derlin" "$PAGES/Major_Bren_Derlin.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Merc Sunlet (Original)" "$PAGES/Merc_Sunlet_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Merc Sunlet (PC Errata)" "$PAGES/Merc_Sunlet_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Merc Sunlet" "$PAGES/Merc_Sunlet.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "M'iiyoom Onith (Original)" "$PAGES/M'iiyoom_Onith_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "M'iiyoom Onith (PC Errata)" "$PAGES/M'iiyoom_Onith_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "M'iiyoom Onith" "$PAGES/M'iiyoom_Onith.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Location, Location, Location (Original)" "$PAGES/Location,_Location,_Location_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Location, Location, Location (PC Errata)" "$PAGES/Location,_Location,_Location_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Location, Location, Location" "$PAGES/Location,_Location,_Location.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Medium Repeating Blaster Cannon (Original)" "$PAGES/Medium_Repeating_Blaster_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Medium Repeating Blaster Cannon (PC Errata)" "$PAGES/Medium_Repeating_Blaster_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Medium Repeating Blaster Cannon" "$PAGES/Medium_Repeating_Blaster_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch23 (Luke Seeker through Medium Repeating Blaster Cannon)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch23 PC Errata seeds"


docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Luke Seeker" \
  "Luke Seeker (Original)" \
  "Luke Seeker (PC Errata)" \
  "Luke's Blaster Pistol" \
  "Luke's Blaster Pistol (Original)" \
  "Luke's Blaster Pistol (PC Errata)" \
  "Luke's Cape" \
  "Luke's Cape (Original)" \
  "Luke's Cape (PC Errata)" \
  "Luke's Hunting Rifle" \
  "Luke's Hunting Rifle (Original)" \
  "Luke's Hunting Rifle (PC Errata)" \
  "Luke's X-34 Landspeeder" \
  "Luke's X-34 Landspeeder (Original)" \
  "Luke's X-34 Landspeeder (PC Errata)" \
  "Lt. Pol Treidum" \
  "Lt. Pol Treidum (Original)" \
  "Lt. Pol Treidum (PC Errata)" \
  "Magnetic Suction Tube" \
  "Magnetic Suction Tube (Original)" \
  "Magnetic Suction Tube (PC Errata)" \
  "Magnetic Suction Tube (Dark)" \
  "Magnetic Suction Tube (Dark) (Original)" \
  "Magnetic Suction Tube (Dark) (PC Errata)" \
  "Major Bren Derlin" \
  "Major Bren Derlin (Original)" \
  "Major Bren Derlin (PC Errata)" \
  "Merc Sunlet" \
  "Merc Sunlet (Original)" \
  "Merc Sunlet (PC Errata)" \
  "M'iiyoom Onith" \
  "M'iiyoom Onith (Original)" \
  "M'iiyoom Onith (PC Errata)" \
  "Location, Location, Location" \
  "Location, Location, Location (Original)" \
  "Location, Location, Location (PC Errata)" \
  "Medium Repeating Blaster Cannon" \
  "Medium Repeating Blaster Cannon (Original)" \
  "Medium Repeating Blaster Cannon (PC Errata)" \
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
echo DONE_APPLY_BATCH23_PC_ERRATA
