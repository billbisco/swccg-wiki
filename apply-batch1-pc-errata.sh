#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch1-gifs

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
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name "'"$HT_FILE"'" | head -1); if [ -n "$f" ]; then sha1sum "$f" | awk "{print \$1}"; else echo MISSING; fi'
}

ARCHIVES=(
  Dagobah-D-4lomsconcussionrifle-decipher-archive.gif
  Premiere-D-5d6ra7-decipher-archive.gif
  JP-L-8d8-decipher-archive.gif
)
HT_FILES=(
  Dagobah-D-4lomsconcussionrifle.gif
  Premiere-D-5d6ra7.gif
  JP-L-8d8.gif
)

echo "== Holotable BEFORE =="
declare -a HT_BEFORE
for ht in "${HT_FILES[@]}"; do
  h=$(ht_hex "$ht")
  echo "ht_before $ht=$h"
  test -n "$h" && test "$h" != "MISSING"
  HT_BEFORE+=("$h")
done

echo "== SAFETY: stage archives only =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
for a in "${ARCHIVES[@]}"; do
  test -f "$ROOT/set-card-art/$a"
  cp -f "$ROOT/set-card-art/$a" "$STAGE/$a"
done
for ht in "${HT_FILES[@]}"; do
  if [ -f "$STAGE/$ht" ]; then echo "REFUSING Holotable in stage: $ht" >&2; exit 1; fi
done
ls -la "$STAGE"

echo "== importImages archive Originals =="
docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch1-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch1-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch1-gifs/
COMMENT='Decipher.com cardlists archive faces for PC Errata batch1 (4-LOM concussion rifle, 5D6-RA-7, 8D8); flush crop + pads bleached #FFFFFF (~350x490). DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch1-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch1-gifs
fi

echo "== edit File descriptions =="
edit "File:Dagobah-D-4lomsconcussionrifle-decipher-archive.gif" "$PAGES/File_Dagobah-D-4lomsconcussionrifle-decipher-archive.gif.wiki" "File page: Decipher Dagobah archive Original for 4-LOM's Concussion Rifle PC Errata"
edit "File:Premiere-D-5d6ra7-decipher-archive.gif" "$PAGES/File_Premiere-D-5d6ra7-decipher-archive.gif.wiki" "File page: Decipher Premiere archive Original for 5D6-RA-7 PC Errata"
edit "File:JP-L-8d8-decipher-archive.gif" "$PAGES/File_JP-L-8d8-decipher-archive.gif.wiki" "File page: Decipher Jabba's Palace archive Original for 8D8 PC Errata"

echo "== edit card pages =="
edit "4-LOM's Concussion Rifle (Original)" "$PAGES/4-LOM's_Concussion_Rifle_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "4-LOM's Concussion Rifle (PC Errata)" "$PAGES/4-LOM's_Concussion_Rifle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable face"
edit "4-LOM's Concussion Rifle" "$PAGES/4-LOM's_Concussion_Rifle.wiki" "Restore Decipher printed game text; archive face; link PC Errata"

edit "5D6-RA-7 (Fivedesix) (Original)" "$PAGES/5D6-RA-7_(Fivedesix)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "5D6-RA-7 (Fivedesix) (PC Errata)" "$PAGES/5D6-RA-7_(Fivedesix)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable face"
edit "5D6-RA-7 (Fivedesix)" "$PAGES/5D6-RA-7_(Fivedesix).wiki" "Restore Decipher printed game text; archive face; link PC Errata"

edit "8D8 (Original)" "$PAGES/8D8_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "8D8 (PC Errata)" "$PAGES/8D8_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable face"
edit "8D8" "$PAGES/8D8.wiki" "Restore Decipher printed game text; archive face; link PC Errata"

edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add 4-LOM's Concussion Rifle, 5D6-RA-7, 8D8 rows"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index PC-only Appendix A seeds: 4-LOM, 5D6-RA-7, 8D8"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -25 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -25 \
  || true

purge() {
  echo "purge $1"
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null \
    || true
}
for t in \
  "4-LOM's Concussion Rifle" "4-LOM's Concussion Rifle (Original)" "4-LOM's Concussion Rifle (PC Errata)" \
  "5D6-RA-7 (Fivedesix)" "5D6-RA-7 (Fivedesix) (Original)" "5D6-RA-7 (Fivedesix) (PC Errata)" \
  "8D8" "8D8 (Original)" "8D8 (PC Errata)" \
  "Errata" "PC Errata" \
  "File:Dagobah-D-4lomsconcussionrifle-decipher-archive.gif" \
  "File:Premiere-D-5d6ra7-decipher-archive.gif" \
  "File:JP-L-8d8-decipher-archive.gif" \
  "File:Dagobah-D-4lomsconcussionrifle.gif" \
  "File:Premiere-D-5d6ra7.gif" \
  "File:JP-L-8d8.gif"
do
  purge "$t"
done

echo "== Holotable AFTER =="
i=0
for ht in "${HT_FILES[@]}"; do
  h=$(ht_hex "$ht")
  echo "ht_after $ht=$h"
  test "$h" = "${HT_BEFORE[$i]}"
  i=$((i+1))
done
echo "HOLOTABLE_OK"
echo "DONE_APPLY_BATCH1_PC_ERRATA"
