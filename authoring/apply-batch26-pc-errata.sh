#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch26-gifs

ARCHIVES=(
  Premiere-L-oldben-decipher-archive.gif
  Hoth-L-onemorepass-decipher-archive.gif
  Hoth-L-ordmantell-decipher-archive.gif
  Premiere-L-outofnowhere-decipher-archive.gif
  Endor-D-outflank-decipher-archive.gif
  Premiere-L-owenlars-decipher-archive.gif
  JabbasPalace-L-palejoreshad-decipher-archive.gif
  Premiere-L-panic-decipher-archive.gif
  Premiere-L-pops-decipher-archive.gif
  Premiere-L-plastoidarmor-decipher-archive.gif
  Premiere-D-pondababa-decipher-archive.gif
  CloudCity-L-princessleia-decipher-archive.gif
)
HT_FILES=(
  Premiere-L-oldben.gif
  Hoth-L-onemorepass.gif
  Hoth-L-ordmantell.gif
  Premiere-L-outofnowhere.gif
  Endor-D-outflank.gif
  Premiere-L-owenlars.gif
  JP-L-palejoreshad.gif
  Premiere-L-panic.gif
  Premiere-L-pops.gif
  Premiere-L-plastoidarmor.gif
  Premiere-D-pondababa.gif
  CC-L-princessleia.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch26-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch26-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch26-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch26 (Old Ben through Princess Leia); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch26-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch26-gifs
fi

edit "File:Premiere-L-oldben-decipher-archive.gif" "$PAGES/File_Premiere-L-oldben-decipher-archive.gif.wiki" "File: Decipher archive Original Old Ben"
edit "File:Hoth-L-onemorepass-decipher-archive.gif" "$PAGES/File_Hoth-L-onemorepass-decipher-archive.gif.wiki" "File: Decipher archive Original One More Pass"
edit "File:Hoth-L-ordmantell-decipher-archive.gif" "$PAGES/File_Hoth-L-ordmantell-decipher-archive.gif.wiki" "File: Decipher archive Original Ord Mantell"
edit "File:Premiere-L-outofnowhere-decipher-archive.gif" "$PAGES/File_Premiere-L-outofnowhere-decipher-archive.gif.wiki" "File: Decipher archive Original Out Of Nowhere"
edit "File:Endor-D-outflank-decipher-archive.gif" "$PAGES/File_Endor-D-outflank-decipher-archive.gif.wiki" "File: Decipher archive Original Outflank"
edit "File:Premiere-L-owenlars-decipher-archive.gif" "$PAGES/File_Premiere-L-owenlars-decipher-archive.gif.wiki" "File: Decipher archive Original Owen Lars"
edit "File:JabbasPalace-L-palejoreshad-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-palejoreshad-decipher-archive.gif.wiki" "File: Decipher archive Original Palejo Reshad"
edit "File:Premiere-L-panic-decipher-archive.gif" "$PAGES/File_Premiere-L-panic-decipher-archive.gif.wiki" "File: Decipher archive Original Panic"
edit "File:Premiere-L-pops-decipher-archive.gif" "$PAGES/File_Premiere-L-pops-decipher-archive.gif.wiki" "File: Decipher archive Original Pops"
edit "File:Premiere-L-plastoidarmor-decipher-archive.gif" "$PAGES/File_Premiere-L-plastoidarmor-decipher-archive.gif.wiki" "File: Decipher archive Original Plastoid Armor"
edit "File:Premiere-D-pondababa-decipher-archive.gif" "$PAGES/File_Premiere-D-pondababa-decipher-archive.gif.wiki" "File: Decipher archive Original Ponda Baba"
edit "File:CloudCity-L-princessleia-decipher-archive.gif" "$PAGES/File_CloudCity-L-princessleia-decipher-archive.gif.wiki" "File: Decipher archive Original Princess Leia"

edit "Old Ben (Original)" "$PAGES/Old_Ben_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Old Ben (PC Errata)" "$PAGES/Old_Ben_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Old Ben" "$PAGES/Old_Ben.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "One More Pass (Original)" "$PAGES/One_More_Pass_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "One More Pass (PC Errata)" "$PAGES/One_More_Pass_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "One More Pass" "$PAGES/One_More_Pass.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Ord Mantell (Original)" "$PAGES/Ord_Mantell_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ord Mantell (PC Errata)" "$PAGES/Ord_Mantell_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ord Mantell" "$PAGES/Ord_Mantell.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Out Of Nowhere (Original)" "$PAGES/Out_Of_Nowhere_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Out Of Nowhere (PC Errata)" "$PAGES/Out_Of_Nowhere_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Out Of Nowhere" "$PAGES/Out_Of_Nowhere.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Outflank (Original)" "$PAGES/Outflank_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Outflank (PC Errata)" "$PAGES/Outflank_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Outflank" "$PAGES/Outflank.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Owen Lars (Original)" "$PAGES/Owen_Lars_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Owen Lars (PC Errata)" "$PAGES/Owen_Lars_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Owen Lars" "$PAGES/Owen_Lars.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Palejo Reshad (Original)" "$PAGES/Palejo_Reshad_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Palejo Reshad (PC Errata)" "$PAGES/Palejo_Reshad_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Palejo Reshad" "$PAGES/Palejo_Reshad.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Panic (Original)" "$PAGES/Panic_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Panic (PC Errata)" "$PAGES/Panic_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Panic" "$PAGES/Panic.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Pops (Original)" "$PAGES/Pops_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Pops (PC Errata)" "$PAGES/Pops_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Pops" "$PAGES/Pops.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Plastoid Armor (Original)" "$PAGES/Plastoid_Armor_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Plastoid Armor (PC Errata)" "$PAGES/Plastoid_Armor_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Plastoid Armor" "$PAGES/Plastoid_Armor.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Ponda Baba (Original)" "$PAGES/Ponda_Baba_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ponda Baba (PC Errata)" "$PAGES/Ponda_Baba_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ponda Baba" "$PAGES/Ponda_Baba.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Princess Leia (Original)" "$PAGES/Princess_Leia_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Princess Leia (PC Errata)" "$PAGES/Princess_Leia_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Princess Leia" "$PAGES/Princess_Leia.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch26 (Old Ben through Princess Leia)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch26 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}

for t in \
  "Old Ben" \
  "Old Ben (Original)" \
  "Old Ben (PC Errata)" \
  "One More Pass" \
  "One More Pass (Original)" \
  "One More Pass (PC Errata)" \
  "Ord Mantell" \
  "Ord Mantell (Original)" \
  "Ord Mantell (PC Errata)" \
  "Out Of Nowhere" \
  "Out Of Nowhere (Original)" \
  "Out Of Nowhere (PC Errata)" \
  "Outflank" \
  "Outflank (Original)" \
  "Outflank (PC Errata)" \
  "Owen Lars" \
  "Owen Lars (Original)" \
  "Owen Lars (PC Errata)" \
  "Palejo Reshad" \
  "Palejo Reshad (Original)" \
  "Palejo Reshad (PC Errata)" \
  "Panic" \
  "Panic (Original)" \
  "Panic (PC Errata)" \
  "Pops" \
  "Pops (Original)" \
  "Pops (PC Errata)" \
  "Plastoid Armor" \
  "Plastoid Armor (Original)" \
  "Plastoid Armor (PC Errata)" \
  "Ponda Baba" \
  "Ponda Baba (Original)" \
  "Ponda Baba (PC Errata)" \
  "Princess Leia" \
  "Princess Leia (Original)" \
  "Princess Leia (PC Errata)" \
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
echo DONE_APPLY_BATCH26_PC_ERRATA
