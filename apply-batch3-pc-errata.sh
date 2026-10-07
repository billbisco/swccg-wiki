#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch3-gifs

ARCHIVES=(
  CC-D-alltooeasy-decipher-archive.gif
  JP-D-allwrappedup-decipher-archive.gif
  JP-D-antipersonnellasercannon-decipher-archive.gif
  ANH-L-alternativestofighting-decipher-archive.gif
  CC-L-armedanddangerous-decipher-archive.gif
)
HT_FILES=(
  CC-D-alltooeasy.gif
  JP-D-allwrappedup.gif
  JP-D-antipersonnellasercannon.gif
  ANH-L-alternativestofighting.gif
  CC-L-armedanddangerous.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch3-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch3-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch3-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch3 (All Too Easy, All Wrapped Up, Antipersonnel Laser Cannon, Alternatives To Fighting, Armed And Dangerous); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch3-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch3-gifs
fi

edit "File:CC-D-alltooeasy-decipher-archive.gif" "$PAGES/File_CC-D-alltooeasy-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original All Too Easy"
edit "File:JP-D-allwrappedup-decipher-archive.gif" "$PAGES/File_JP-D-allwrappedup-decipher-archive.gif.wiki" "File: Decipher Jabba archive Original All Wrapped Up"
edit "File:JP-D-antipersonnellasercannon-decipher-archive.gif" "$PAGES/File_JP-D-antipersonnellasercannon-decipher-archive.gif.wiki" "File: Decipher Jabba archive Original Antipersonnel Laser Cannon"
edit "File:ANH-L-alternativestofighting-decipher-archive.gif" "$PAGES/File_ANH-L-alternativestofighting-decipher-archive.gif.wiki" "File: Decipher ANH archive Original Alternatives To Fighting"
edit "File:CC-L-armedanddangerous-decipher-archive.gif" "$PAGES/File_CC-L-armedanddangerous-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Armed And Dangerous"

edit "All Too Easy (Original)" "$PAGES/All_Too_Easy_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "All Too Easy (PC Errata)" "$PAGES/All_Too_Easy_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "All Too Easy" "$PAGES/All_Too_Easy.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "All Wrapped Up (Original)" "$PAGES/All_Wrapped_Up_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "All Wrapped Up (PC Errata)" "$PAGES/All_Wrapped_Up_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "All Wrapped Up" "$PAGES/All_Wrapped_Up.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Antipersonnel Laser Cannon (Original)" "$PAGES/Antipersonnel_Laser_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Antipersonnel Laser Cannon (PC Errata)" "$PAGES/Antipersonnel_Laser_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Antipersonnel Laser Cannon" "$PAGES/Antipersonnel_Laser_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Alternatives To Fighting (Original)" "$PAGES/Alternatives_To_Fighting_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Alternatives To Fighting (PC Errata)" "$PAGES/Alternatives_To_Fighting_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Alternatives To Fighting" "$PAGES/Alternatives_To_Fighting.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Armed And Dangerous (Original)" "$PAGES/Armed_And_Dangerous_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Armed And Dangerous (PC Errata)" "$PAGES/Armed_And_Dangerous_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Armed And Dangerous" "$PAGES/Armed_And_Dangerous.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add All Too Easy, All Wrapped Up, Antipersonnel Laser Cannon, Alternatives To Fighting, Armed And Dangerous"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch3 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "All Too Easy" "All Too Easy (Original)" "All Too Easy (PC Errata)" \
  "All Wrapped Up" "All Wrapped Up (Original)" "All Wrapped Up (PC Errata)" \
  "Antipersonnel Laser Cannon" "Antipersonnel Laser Cannon (Original)" "Antipersonnel Laser Cannon (PC Errata)" \
  "Alternatives To Fighting" "Alternatives To Fighting (Original)" "Alternatives To Fighting (PC Errata)" \
  "Armed And Dangerous" "Armed And Dangerous (Original)" "Armed And Dangerous (PC Errata)" \
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
echo DONE_APPLY_BATCH3_PC_ERRATA
