#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch5-gifs

ARCHIVES=(
  CC-L-beldonseye-decipher-archive.gif
  JP-D-beedo-decipher-archive.gif
  ANH-D-black4-decipher-archive.gif
  ANH-L-blastthedoorkid-decipher-archive.gif
  CC-L-blasterproficiency-decipher-archive.gif
  Hoth-D-blizzard1-decipher-archive.gif
  Hoth-D-blizzard2-decipher-archive.gif
  JP-D-barada-decipher-archive.gif
  SE-L-benkenobi-decipher-archive.gif
  CC-D-blasteddroid-decipher-archive.gif
  ANH-L-chewbacca-decipher-archive.gif
  Premiere-D-chiefbast-decipher-archive.gif
)
HT_FILES=(
  CC-L-beldonseye.gif
  JP-D-beedo.gif
  ANH-D-black4.gif
  ANH-L-blastthedoorkid.gif
  CC-L-blasterproficiency.gif
  Hoth-D-blizzard1.gif
  Hoth-D-blizzard2.gif
  JP-D-barada.gif
  SE-L-benkenobi.gif
  CC-D-blasteddroid.gif
  ANH-L-chewbacca.gif
  Premiere-D-chiefbast.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch5-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch5-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch5-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch5 (Beldons Eye, Beedo, Black 4, Blast The Door Kid, Blaster Proficiency, Blizzard 1/2, Barada, Ben Kenobi, Blasted Droid, Chewbacca, Chief Bast); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch5-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch5-gifs
fi

edit "File:CC-L-beldonseye-decipher-archive.gif" "$PAGES/File_CC-L-beldonseye-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Beldon's Eye"
edit "File:JP-D-beedo-decipher-archive.gif" "$PAGES/File_JP-D-beedo-decipher-archive.gif.wiki" "File: Decipher Jabba archive Original Beedo"
edit "File:ANH-D-black4-decipher-archive.gif" "$PAGES/File_ANH-D-black4-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Black 4"
edit "File:ANH-L-blastthedoorkid-decipher-archive.gif" "$PAGES/File_ANH-L-blastthedoorkid-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Blast The Door Kid"
edit "File:CC-L-blasterproficiency-decipher-archive.gif" "$PAGES/File_CC-L-blasterproficiency-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Blaster Proficiency"
edit "File:Hoth-D-blizzard1-decipher-archive.gif" "$PAGES/File_Hoth-D-blizzard1-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Blizzard 1"
edit "File:Hoth-D-blizzard2-decipher-archive.gif" "$PAGES/File_Hoth-D-blizzard2-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Blizzard 2"
edit "File:JP-D-barada-decipher-archive.gif" "$PAGES/File_JP-D-barada-decipher-archive.gif.wiki" "File: Decipher Jabba archive Original Barada"
edit "File:SE-L-benkenobi-decipher-archive.gif" "$PAGES/File_SE-L-benkenobi-decipher-archive.gif.wiki" "File: Decipher Special Edition archive Original Ben Kenobi"
edit "File:CC-D-blasteddroid-decipher-archive.gif" "$PAGES/File_CC-D-blasteddroid-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Blasted Droid"
edit "File:ANH-L-chewbacca-decipher-archive.gif" "$PAGES/File_ANH-L-chewbacca-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Chewbacca"
edit "File:Premiere-D-chiefbast-decipher-archive.gif" "$PAGES/File_Premiere-D-chiefbast-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Chief Bast"

edit "Beldon's Eye (Original)" "$PAGES/Beldon's_Eye_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Beldon's Eye (PC Errata)" "$PAGES/Beldon's_Eye_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Beldon's Eye" "$PAGES/Beldon's_Eye.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Beedo (Original)" "$PAGES/Beedo_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Beedo (PC Errata)" "$PAGES/Beedo_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Beedo" "$PAGES/Beedo.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Black 4 (Original)" "$PAGES/Black_4_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Black 4 (PC Errata)" "$PAGES/Black_4_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Black 4" "$PAGES/Black_4.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Blast The Door, Kid! (Original)" "$PAGES/Blast_The_Door,_Kid!_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Blast The Door, Kid! (PC Errata)" "$PAGES/Blast_The_Door,_Kid!_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Blast The Door, Kid!" "$PAGES/Blast_The_Door,_Kid!.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Blaster Proficiency (Original)" "$PAGES/Blaster_Proficiency_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Blaster Proficiency (PC Errata)" "$PAGES/Blaster_Proficiency_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Blaster Proficiency" "$PAGES/Blaster_Proficiency.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Blizzard 1 (Original)" "$PAGES/Blizzard_1_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Blizzard 1 (PC Errata)" "$PAGES/Blizzard_1_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Blizzard 1" "$PAGES/Blizzard_1.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Blizzard 2 (Original)" "$PAGES/Blizzard_2_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Blizzard 2 (PC Errata)" "$PAGES/Blizzard_2_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Blizzard 2" "$PAGES/Blizzard_2.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Barada (Original)" "$PAGES/Barada_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Barada (PC Errata)" "$PAGES/Barada_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Barada" "$PAGES/Barada.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Ben Kenobi (Original)" "$PAGES/Ben_Kenobi_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ben Kenobi (PC Errata)" "$PAGES/Ben_Kenobi_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ben Kenobi" "$PAGES/Ben_Kenobi.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Blasted Droid (Original)" "$PAGES/Blasted_Droid_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Blasted Droid (PC Errata)" "$PAGES/Blasted_Droid_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Blasted Droid" "$PAGES/Blasted_Droid.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Chewbacca (Original)" "$PAGES/Chewbacca_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Chewbacca (PC Errata)" "$PAGES/Chewbacca_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Chewbacca" "$PAGES/Chewbacca.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Chief Bast (Original)" "$PAGES/Chief_Bast_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Chief Bast (PC Errata)" "$PAGES/Chief_Bast_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Chief Bast" "$PAGES/Chief_Bast.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch5 (Beldon's Eye through Chief Bast)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch5 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Beldon's Eye" "Beldon's Eye (Original)" "Beldon's Eye (PC Errata)" \
  "Beedo" "Beedo (Original)" "Beedo (PC Errata)" \
  "Black 4" "Black 4 (Original)" "Black 4 (PC Errata)" \
  "Blast The Door, Kid!" "Blast The Door, Kid! (Original)" "Blast The Door, Kid! (PC Errata)" \
  "Blaster Proficiency" "Blaster Proficiency (Original)" "Blaster Proficiency (PC Errata)" \
  "Blizzard 1" "Blizzard 1 (Original)" "Blizzard 1 (PC Errata)" \
  "Blizzard 2" "Blizzard 2 (Original)" "Blizzard 2 (PC Errata)" \
  "Barada" "Barada (Original)" "Barada (PC Errata)" \
  "Ben Kenobi" "Ben Kenobi (Original)" "Ben Kenobi (PC Errata)" \
  "Blasted Droid" "Blasted Droid (Original)" "Blasted Droid (PC Errata)" \
  "Chewbacca" "Chewbacca (Original)" "Chewbacca (PC Errata)" \
  "Chief Bast" "Chief Bast (Original)" "Chief Bast (PC Errata)" \
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
echo DONE_APPLY_BATCH5_PC_ERRATA
