#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch15-gifs

ARCHIVES=(
  Premiere-D-gravelstorm-decipher-archive.gif
  JediPack-D-gravityshadow-decipher-archive.gif
  Tatooine-L-greatshotkid-decipher-archive.gif
  Dagobah-L-greatwarrior-decipher-archive.gif
  Premiere-L-hansheavyblasterpistol-decipher-archive.gif
  Hoth-L-golanlaserbattery-decipher-archive.gif
  ANH-L-gold2-decipher-archive.gif
  ANH-D-ghhhk-decipher-archive.gif
  ANH-L-garouflafoe-decipher-archive.gif
  Premiere-D-feltiperntrevagg-decipher-archive.gif
  ReflectionsIII-D-darkrage-decipher-archive.gif
  ReflectionsIII-L-coloclawfish-decipher-archive.gif
  ReflectionsIII-D-coloclawfish-decipher-archive.gif
)
HT_FILES=(
  Premiere-D-gravelstorm.gif
  Jedi-D-gravityshadow.gif
  Tat-L-greatshotkid.gif
  Dagobah-L-greatwarrior.gif
  Premiere-L-hansheavyblasterpistol.gif
  Hoth-L-golanlaserbattery.gif
  ANH-L-gold2.gif
  ANH-D-ghhhk.gif
  ANH-L-garouflafoe.gif
  Premiere-D-feltiperntrevagg.gif
  Ref3-D-darkrage.gif
  Ref3-L-coloclawfish.gif
  Ref3-D-coloclawfish.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch15-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch15-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch15-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch15 (Gravel Storm through Colo Claw Fish dual); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch15-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch15-gifs
fi

edit "File:Premiere-D-gravelstorm-decipher-archive.gif" "$PAGES/File_Premiere-D-gravelstorm-decipher-archive.gif.wiki" "File: Decipher archive Original Gravel Storm"
edit "File:JediPack-D-gravityshadow-decipher-archive.gif" "$PAGES/File_JediPack-D-gravityshadow-decipher-archive.gif.wiki" "File: Decipher archive Original Gravity Shadow"
edit "File:Tatooine-L-greatshotkid-decipher-archive.gif" "$PAGES/File_Tatooine-L-greatshotkid-decipher-archive.gif.wiki" "File: Decipher archive Original Great Shot, Kid!"
edit "File:Dagobah-L-greatwarrior-decipher-archive.gif" "$PAGES/File_Dagobah-L-greatwarrior-decipher-archive.gif.wiki" "File: Decipher archive Original Great Warrior"
edit "File:Premiere-L-hansheavyblasterpistol-decipher-archive.gif" "$PAGES/File_Premiere-L-hansheavyblasterpistol-decipher-archive.gif.wiki" "File: Decipher archive Original Han's Heavy Blaster Pistol"
edit "File:Hoth-L-golanlaserbattery-decipher-archive.gif" "$PAGES/File_Hoth-L-golanlaserbattery-decipher-archive.gif.wiki" "File: Decipher archive Original Golan Laser Battery"
edit "File:ANH-L-gold2-decipher-archive.gif" "$PAGES/File_ANH-L-gold2-decipher-archive.gif.wiki" "File: Decipher archive Original Gold 2"
edit "File:ANH-D-ghhhk-decipher-archive.gif" "$PAGES/File_ANH-D-ghhhk-decipher-archive.gif.wiki" "File: Decipher archive Original Ghhhk"
edit "File:ANH-L-garouflafoe-decipher-archive.gif" "$PAGES/File_ANH-L-garouflafoe-decipher-archive.gif.wiki" "File: Decipher archive Original Garouf Lafoe"
edit "File:Premiere-D-feltiperntrevagg-decipher-archive.gif" "$PAGES/File_Premiere-D-feltiperntrevagg-decipher-archive.gif.wiki" "File: Decipher archive Original Feltipern Trevagg"
edit "File:ReflectionsIII-D-darkrage-decipher-archive.gif" "$PAGES/File_ReflectionsIII-D-darkrage-decipher-archive.gif.wiki" "File: Decipher archive Original Dark Rage"
edit "File:ReflectionsIII-L-coloclawfish-decipher-archive.gif" "$PAGES/File_ReflectionsIII-L-coloclawfish-decipher-archive.gif.wiki" "File: Decipher archive Original Colo Claw Fish"
edit "File:ReflectionsIII-D-coloclawfish-decipher-archive.gif" "$PAGES/File_ReflectionsIII-D-coloclawfish-decipher-archive.gif.wiki" "File: Decipher archive Original Colo Claw Fish (Dark)"

edit "Gravel Storm (Original)" "$PAGES/Gravel_Storm_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Gravel Storm (PC Errata)" "$PAGES/Gravel_Storm_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Gravel Storm" "$PAGES/Gravel_Storm.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Gravity Shadow (Original)" "$PAGES/Gravity_Shadow_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Gravity Shadow (PC Errata)" "$PAGES/Gravity_Shadow_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Gravity Shadow" "$PAGES/Gravity_Shadow.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Great Shot, Kid! (Original)" "$PAGES/Great_Shot,_Kid!_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Great Shot, Kid! (PC Errata)" "$PAGES/Great_Shot,_Kid!_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Great Shot, Kid!" "$PAGES/Great_Shot,_Kid!.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Great Warrior (Original)" "$PAGES/Great_Warrior_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Great Warrior (PC Errata)" "$PAGES/Great_Warrior_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Great Warrior" "$PAGES/Great_Warrior.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Han's Heavy Blaster Pistol (Original)" "$PAGES/Han's_Heavy_Blaster_Pistol_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Han's Heavy Blaster Pistol (PC Errata)" "$PAGES/Han's_Heavy_Blaster_Pistol_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Han's Heavy Blaster Pistol" "$PAGES/Han's_Heavy_Blaster_Pistol.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Golan Laser Battery (Original)" "$PAGES/Golan_Laser_Battery_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Golan Laser Battery (PC Errata)" "$PAGES/Golan_Laser_Battery_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Golan Laser Battery" "$PAGES/Golan_Laser_Battery.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Gold 2 (Original)" "$PAGES/Gold_2_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Gold 2 (PC Errata)" "$PAGES/Gold_2_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Gold 2" "$PAGES/Gold_2.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Ghhhk (Original)" "$PAGES/Ghhhk_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ghhhk (PC Errata)" "$PAGES/Ghhhk_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ghhhk" "$PAGES/Ghhhk.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Garouf Lafoe (Original)" "$PAGES/Garouf_Lafoe_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Garouf Lafoe (PC Errata)" "$PAGES/Garouf_Lafoe_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Garouf Lafoe" "$PAGES/Garouf_Lafoe.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Feltipern Trevagg (Original)" "$PAGES/Feltipern_Trevagg_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Feltipern Trevagg (PC Errata)" "$PAGES/Feltipern_Trevagg_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Feltipern Trevagg" "$PAGES/Feltipern_Trevagg.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Dark Rage (Original)" "$PAGES/Dark_Rage_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Dark Rage (PC Errata)" "$PAGES/Dark_Rage_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Dark Rage" "$PAGES/Dark_Rage.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Colo Claw Fish (Original)" "$PAGES/Colo_Claw_Fish_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Colo Claw Fish (PC Errata)" "$PAGES/Colo_Claw_Fish_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Colo Claw Fish" "$PAGES/Colo_Claw_Fish.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Colo Claw Fish (Dark) (Original)" "$PAGES/Colo_Claw_Fish_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Colo Claw Fish (Dark) (PC Errata)" "$PAGES/Colo_Claw_Fish_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Colo Claw Fish (Dark)" "$PAGES/Colo_Claw_Fish_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch15 (Gravel Storm through Colo Claw Fish dual)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch15 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Gravel Storm" "Gravel Storm (Original)" "Gravel Storm (PC Errata)" "Gravity Shadow" "Gravity Shadow (Original)" "Gravity Shadow (PC Errata)" "Great Shot, Kid!" "Great Shot, Kid! (Original)" "Great Shot, Kid! (PC Errata)" "Great Warrior" "Great Warrior (Original)" "Great Warrior (PC Errata)" "Han's Heavy Blaster Pistol" "Han's Heavy Blaster Pistol (Original)" "Han's Heavy Blaster Pistol (PC Errata)" "Golan Laser Battery" "Golan Laser Battery (Original)" "Golan Laser Battery (PC Errata)" "Gold 2" "Gold 2 (Original)" "Gold 2 (PC Errata)" "Ghhhk" "Ghhhk (Original)" "Ghhhk (PC Errata)" "Garouf Lafoe" "Garouf Lafoe (Original)" "Garouf Lafoe (PC Errata)" "Feltipern Trevagg" "Feltipern Trevagg (Original)" "Feltipern Trevagg (PC Errata)" "Dark Rage" "Dark Rage (Original)" "Dark Rage (PC Errata)" "Colo Claw Fish" "Colo Claw Fish (Original)" "Colo Claw Fish (PC Errata)" "Colo Claw Fish (Dark)" "Colo Claw Fish (Dark) (Original)" "Colo Claw Fish (Dark) (PC Errata)" \
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
echo DONE_APPLY_BATCH15_PC_ERRATA
