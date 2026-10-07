#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch38-gifs

ARCHIVES=(
  ESBIntroductoryTwoPlayerGame-L-lonerogue-decipher-archive.gif
)
HT_FILES=(
  ESB2P-L-lonerogue.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch38-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch38-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch38-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch38 (Lone Rogue through Lone Rogue); flush crop + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch38-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch38-gifs
fi

edit "File:ESBIntroductoryTwoPlayerGame-L-lonerogue-decipher-archive.gif" "$PAGES/File_ESBIntroductoryTwoPlayerGame-L-lonerogue-decipher-archive.gif.wiki" "File: Decipher archive Original Lone Rogue"

edit "Lone Rogue (Original)" "$PAGES/Lone_Rogue_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Lone Rogue (PC Errata)" "$PAGES/Lone_Rogue_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Lone Rogue" "$PAGES/Lone_Rogue.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch38 (Lone Rogue through Lone Rogue)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch38 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Lone Rogue" \
  "Lone Rogue (Original)" \
  "Lone Rogue (PC Errata)" \
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
echo DONE_APPLY_BATCH38_PC_ERRATA
