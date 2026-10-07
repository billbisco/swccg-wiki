#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch31-gifs

ARCHIVES=(
  OTSD-D-stormtroopercadet-decipher-archive.gif
  ANH-D-stunningleader-decipher-archive.gif
  Hoth-L-surfacedefensecannon-decipher-archive.gif
  ANH-L-sw4ioncannon-decipher-archive.gif
  ANH-D-swillacorey-decipher-archive.gif
  Premiere-D-tallonroll-decipher-archive.gif
  Premiere-L-taggeseeker-decipher-archive.gif
  Premiere-L-tarkinseeker-decipher-archive.gif
  SE-D-tarkinsbounty-decipher-archive.gif
  Hoth-L-tauntaun-decipher-archive.gif
  Hoth-L-tauntaunhandler-decipher-archive.gif
  Hoth-D-thatsittherebelsarethere-decipher-archive.gif
)
HT_FILES=(
  OTSD-D-stormtroopercadet.gif
  ANH-D-stunningleader.gif
  Hoth-L-surfacedefensecannon.gif
  ANH-L-sw4ioncannon.gif
  ANH-D-swillacorey.gif
  Premiere-D-tallonroll.gif
  Premiere-L-taggeseeker.gif
  Premiere-L-tarkinseeker.gif
  SE-D-tarkinsbounty.gif
  Hoth-L-tauntaun.gif
  Hoth-L-tauntaunhandler.gif
  Hoth-D-thatsittherebelsarethere.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch31-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch31-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch31-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch31 (Stormtrooper Cadet through That'\''s It, The Rebels Are There!); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch31-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch31-gifs
fi

edit "File:OTSD-D-stormtroopercadet-decipher-archive.gif" "$PAGES/File_OTSD-D-stormtroopercadet-decipher-archive.gif.wiki" "File: Decipher archive Original Stormtrooper Cadet"
edit "File:ANH-D-stunningleader-decipher-archive.gif" "$PAGES/File_ANH-D-stunningleader-decipher-archive.gif.wiki" "File: Decipher archive Original Stunning Leader"
edit "File:Hoth-L-surfacedefensecannon-decipher-archive.gif" "$PAGES/File_Hoth-L-surfacedefensecannon-decipher-archive.gif.wiki" "File: Decipher archive Original Surface Defense Cannon"
edit "File:ANH-L-sw4ioncannon-decipher-archive.gif" "$PAGES/File_ANH-L-sw4ioncannon-decipher-archive.gif.wiki" "File: Decipher archive Original SW-4 Ion Cannon"
edit "File:ANH-D-swillacorey-decipher-archive.gif" "$PAGES/File_ANH-D-swillacorey-decipher-archive.gif.wiki" "File: Decipher archive Original Swilla Corey"
edit "File:Premiere-D-tallonroll-decipher-archive.gif" "$PAGES/File_Premiere-D-tallonroll-decipher-archive.gif.wiki" "File: Decipher archive Original Tallon Roll"
edit "File:Premiere-L-taggeseeker-decipher-archive.gif" "$PAGES/File_Premiere-L-taggeseeker-decipher-archive.gif.wiki" "File: Decipher archive Original Tagge Seeker"
edit "File:Premiere-L-tarkinseeker-decipher-archive.gif" "$PAGES/File_Premiere-L-tarkinseeker-decipher-archive.gif.wiki" "File: Decipher archive Original Tarkin Seeker"
edit "File:SE-D-tarkinsbounty-decipher-archive.gif" "$PAGES/File_SE-D-tarkinsbounty-decipher-archive.gif.wiki" "File: Decipher archive Original Tarkin's Bounty"
edit "File:Hoth-L-tauntaun-decipher-archive.gif" "$PAGES/File_Hoth-L-tauntaun-decipher-archive.gif.wiki" "File: Decipher archive Original Tauntaun"
edit "File:Hoth-L-tauntaunhandler-decipher-archive.gif" "$PAGES/File_Hoth-L-tauntaunhandler-decipher-archive.gif.wiki" "File: Decipher archive Original Tauntaun Handler"
edit "File:Hoth-D-thatsittherebelsarethere-decipher-archive.gif" "$PAGES/File_Hoth-D-thatsittherebelsarethere-decipher-archive.gif.wiki" "File: Decipher archive Original That's It, The Rebels Are There!"

edit "Stormtrooper Cadet (Original)" "$PAGES/Stormtrooper_Cadet_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Stormtrooper Cadet (PC Errata)" "$PAGES/Stormtrooper_Cadet_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Stormtrooper Cadet" "$PAGES/Stormtrooper_Cadet.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Stunning Leader (Original)" "$PAGES/Stunning_Leader_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Stunning Leader (PC Errata)" "$PAGES/Stunning_Leader_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Stunning Leader" "$PAGES/Stunning_Leader.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Surface Defense Cannon (Original)" "$PAGES/Surface_Defense_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Surface Defense Cannon (PC Errata)" "$PAGES/Surface_Defense_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Surface Defense Cannon" "$PAGES/Surface_Defense_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "SW-4 Ion Cannon (Original)" "$PAGES/SW-4_Ion_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "SW-4 Ion Cannon (PC Errata)" "$PAGES/SW-4_Ion_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "SW-4 Ion Cannon" "$PAGES/SW-4_Ion_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Swilla Corey (Original)" "$PAGES/Swilla_Corey_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Swilla Corey (PC Errata)" "$PAGES/Swilla_Corey_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Swilla Corey" "$PAGES/Swilla_Corey.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tallon Roll (Original)" "$PAGES/Tallon_Roll_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tallon Roll (PC Errata)" "$PAGES/Tallon_Roll_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tallon Roll" "$PAGES/Tallon_Roll.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tagge Seeker (Original)" "$PAGES/Tagge_Seeker_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tagge Seeker (PC Errata)" "$PAGES/Tagge_Seeker_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tagge Seeker" "$PAGES/Tagge_Seeker.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tarkin Seeker (Original)" "$PAGES/Tarkin_Seeker_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tarkin Seeker (PC Errata)" "$PAGES/Tarkin_Seeker_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tarkin Seeker" "$PAGES/Tarkin_Seeker.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tarkin's Bounty (Original)" "$PAGES/Tarkin's_Bounty_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tarkin's Bounty (PC Errata)" "$PAGES/Tarkin's_Bounty_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tarkin's Bounty" "$PAGES/Tarkin's_Bounty.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tauntaun (Original)" "$PAGES/Tauntaun_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tauntaun (PC Errata)" "$PAGES/Tauntaun_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tauntaun" "$PAGES/Tauntaun.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Tauntaun Handler (Original)" "$PAGES/Tauntaun_Handler_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Tauntaun Handler (PC Errata)" "$PAGES/Tauntaun_Handler_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Tauntaun Handler" "$PAGES/Tauntaun_Handler.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "That's It, The Rebels Are There! (Original)" "$PAGES/That's_It,_The_Rebels_Are_There!_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "That's It, The Rebels Are There! (PC Errata)" "$PAGES/That's_It,_The_Rebels_Are_There!_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "That's It, The Rebels Are There!" "$PAGES/That's_It,_The_Rebels_Are_There!.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch31 (Stormtrooper Cadet through That's It, The Rebels Are There!)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch31 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Stormtrooper Cadet" \
  "Stormtrooper Cadet (Original)" \
  "Stormtrooper Cadet (PC Errata)" \
  "Stunning Leader" \
  "Stunning Leader (Original)" \
  "Stunning Leader (PC Errata)" \
  "Surface Defense Cannon" \
  "Surface Defense Cannon (Original)" \
  "Surface Defense Cannon (PC Errata)" \
  "SW-4 Ion Cannon" \
  "SW-4 Ion Cannon (Original)" \
  "SW-4 Ion Cannon (PC Errata)" \
  "Swilla Corey" \
  "Swilla Corey (Original)" \
  "Swilla Corey (PC Errata)" \
  "Tallon Roll" \
  "Tallon Roll (Original)" \
  "Tallon Roll (PC Errata)" \
  "Tagge Seeker" \
  "Tagge Seeker (Original)" \
  "Tagge Seeker (PC Errata)" \
  "Tarkin Seeker" \
  "Tarkin Seeker (Original)" \
  "Tarkin Seeker (PC Errata)" \
  "Tarkin's Bounty" \
  "Tarkin's Bounty (Original)" \
  "Tarkin's Bounty (PC Errata)" \
  "Tauntaun" \
  "Tauntaun (Original)" \
  "Tauntaun (PC Errata)" \
  "Tauntaun Handler" \
  "Tauntaun Handler (Original)" \
  "Tauntaun Handler (PC Errata)" \
  "That's It, The Rebels Are There!" \
  "That's It, The Rebels Are There! (Original)" \
  "That's It, The Rebels Are There! (PC Errata)" \
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
echo DONE_APPLY_BATCH31_PC_ERRATA
