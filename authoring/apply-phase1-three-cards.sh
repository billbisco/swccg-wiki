#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-phase1-gifs
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
# Errata hub Notes column safety
if p.name == "Errata.wiki":
    for line in text.splitlines():
        if line.startswith("| [[Players Committee Advanced Rulebook]]") and re.search(r"\[\[File:[^\]]*\.gif", line, re.I):
            raise SystemExit("FATAL: gif File embed in Errata Notes column")
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
  local f="$1"
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -type f -name '"$f"' | head -1); test -n "$f" && sha1sum "$f" | awk "{print \$1}"'
}

echo "== Phase1: 4-LOM / 5D6 / 8D8 PC Errata seed =="
echo "== Holotable BEFORE =="
declare -A HT_BEFORE
for ht in "${HT_FILES[@]}"; do
  h=$(ht_hex "$ht")
  echo "ht_before $ht=$h"
  test -n "$h"
  HT_BEFORE[$ht]=$h
done

echo "== SAFETY: stage archive only =="
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
docker exec swccg_wiki mkdir -p /tmp/pc-errata-phase1-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-phase1-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-phase1-gifs/
COMMENT='Decipher.com cardlists archive faces for PC Errata Original columns (4-LOM concussion rifle, 5D6-RA-7, 8D8); flush crop + exterior corner pads bleached #FFFFFF (~350x490). DO NOT replace Holotable gifs.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-phase1-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-phase1-gifs
fi

echo "== edit File descriptions =="
edit "File:Dagobah-D-4lomsconcussionrifle-decipher-archive.gif" "$PAGES/File_Dagobah-D-4lomsconcussionrifle-decipher-archive.gif.wiki" "File page: Decipher Dagobah archive Original for 4-LOM's Concussion Rifle PC Errata seed"
edit "File:Premiere-D-5d6ra7-decipher-archive.gif" "$PAGES/File_Premiere-D-5d6ra7-decipher-archive.gif.wiki" "File page: Decipher Premiere archive Original for 5D6-RA-7 PC Errata seed"
edit "File:JP-L-8d8-decipher-archive.gif" "$PAGES/File_JP-L-8d8-decipher-archive.gif.wiki" "File page: Decipher JP archive Original for 8D8 PC Errata seed"

echo "== edit card pages (4-LOM) =="
edit "4-LOM's Concussion Rifle (Original)" "$PAGES/4-LOM's_Concussion_Rifle_(Original).wiki" "PC Errata seed: printed Decipher archive Original for 4-LOM's Concussion Rifle"
edit "4-LOM's Concussion Rifle (PC Errata)" "$PAGES/4-LOM's_Concussion_Rifle_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A game text + Holotable face"
edit "4-LOM's Concussion Rifle" "$PAGES/4-LOM's_Concussion_Rifle.wiki" "Restore Decipher printed game text; archive face; card_uid 4_174o; link PC Errata"

echo "== edit card pages (5D6) =="
edit "5D6-RA-7 (Fivedesix) (Original)" "$PAGES/5D6-RA-7_(Fivedesix)_(Original).wiki" "PC Errata seed: printed Decipher archive Original for 5D6-RA-7"
edit "5D6-RA-7 (Fivedesix) (PC Errata)" "$PAGES/5D6-RA-7_(Fivedesix)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A game text + Holotable face"
edit "5D6-RA-7 (Fivedesix)" "$PAGES/5D6-RA-7_(Fivedesix).wiki" "Restore Decipher printed game text; archive face; card_uid 1_163o; link PC Errata"

echo "== edit card pages (8D8) =="
edit "8D8 (Original)" "$PAGES/8D8_(Original).wiki" "PC Errata seed: printed Decipher archive Original for 8D8"
edit "8D8 (PC Errata)" "$PAGES/8D8_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A game text + Holotable face"
edit "8D8" "$PAGES/8D8.wiki" "Restore Decipher printed game text; archive face; card_uid 6_1o; link PC Errata"

echo "== edit hubs (serialize Errata) =="
edit "Errata" "$PAGES/Errata.wiki" "PC Errata: add 4-LOM's Concussion Rifle, 5D6-RA-7, 8D8 rows (AR-linked Notes)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index Appendix A walk seeds: 4-LOM, 5D6-RA-7, 8D8"

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
purge "4-LOM's Concussion Rifle"
purge "4-LOM's Concussion Rifle (Original)"
purge "4-LOM's Concussion Rifle (PC Errata)"
purge "5D6-RA-7 (Fivedesix)"
purge "5D6-RA-7 (Fivedesix) (Original)"
purge "5D6-RA-7 (Fivedesix) (PC Errata)"
purge "8D8"
purge "8D8 (Original)"
purge "8D8 (PC Errata)"
purge "Errata"
purge "PC Errata"
for a in "${ARCHIVES[@]}"; do purge "File:$a"; done
for ht in "${HT_FILES[@]}"; do purge "File:$ht"; done

echo "== Holotable AFTER =="
for ht in "${HT_FILES[@]}"; do
  h=$(ht_hex "$ht")
  echo "ht_after $ht=$h"
  test "$h" = "${HT_BEFORE[$ht]}"
done
echo "HOLOTABLE_OK"
echo "DONE_APPLY_PHASE1_THREE_CARDS"
