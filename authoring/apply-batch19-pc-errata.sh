#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch19-gifs

ARCHIVES=(
  ANewHope-D-imontheleader-decipher-archive.gif
  Premiere-L-ivegotabadfeelingaboutthis-decipher-archive.gif
  Premiere-D-ivegotaproblemhere-decipher-archive.gif
  Premiere-D-ivelostartoo-decipher-archive.gif
  CloudCity-D-ihadnochoice-decipher-archive.gif
  Hoth-L-ithoughttheysmelledbad-decipher-archive.gif
  Premiere-D-imperialtrooperguard-decipher-archive.gif
  SpecialEdition-D-inrange-decipher-archive.gif
  Hoth-L-infantrymine-decipher-archive.gif
  Hoth-D-infantrymine-decipher-archive.gif
  Premiere-D-ioncannon-decipher-archive.gif
  CloudCity-L-innocentscoundrel-decipher-archive.gif
)
HT_FILES=(
  ANH-D-imontheleader.gif
  Premiere-L-ivegotabadfeelingaboutthis.gif
  Premiere-D-ivegotaproblemhere.gif
  Premiere-D-ivelostartoo.gif
  CC-D-ihadnochoice.gif
  Hoth-L-ithoughttheysmelledbadontheoutside.gif
  Premiere-D-imperialtrooperguard.gif
  SE-D-inrange.gif
  Hoth-L-infantrymine.gif
  Hoth-D-infantrymine.gif
  Premiere-D-ioncannon.gif
  CC-L-innocentscoundrel.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch19-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch19-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch19-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch19 (Im On The Leader through Innocent Scoundrel; Infantry Mine dual); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch19-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch19-gifs
fi

edit "File:ANewHope-D-imontheleader-decipher-archive.gif" "$PAGES/File_ANewHope-D-imontheleader-decipher-archive.gif.wiki" "File: Decipher archive Original I'm On The Leader"
edit "File:Premiere-L-ivegotabadfeelingaboutthis-decipher-archive.gif" "$PAGES/File_Premiere-L-ivegotabadfeelingaboutthis-decipher-archive.gif.wiki" "File: Decipher archive Original I've Got A Bad Feeling About This"
edit "File:Premiere-D-ivegotaproblemhere-decipher-archive.gif" "$PAGES/File_Premiere-D-ivegotaproblemhere-decipher-archive.gif.wiki" "File: Decipher archive Original I've Got A Problem Here"
edit "File:Premiere-D-ivelostartoo-decipher-archive.gif" "$PAGES/File_Premiere-D-ivelostartoo-decipher-archive.gif.wiki" "File: Decipher archive Original I've Lost Artoo!"
edit "File:CloudCity-D-ihadnochoice-decipher-archive.gif" "$PAGES/File_CloudCity-D-ihadnochoice-decipher-archive.gif.wiki" "File: Decipher archive Original I Had No Choice"
edit "File:Hoth-L-ithoughttheysmelledbad-decipher-archive.gif" "$PAGES/File_Hoth-L-ithoughttheysmelledbad-decipher-archive.gif.wiki" "File: Decipher archive Original I Thought They Smelled Bad On The Outside"
edit "File:Premiere-D-imperialtrooperguard-decipher-archive.gif" "$PAGES/File_Premiere-D-imperialtrooperguard-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Trooper Guard"
edit "File:SpecialEdition-D-inrange-decipher-archive.gif" "$PAGES/File_SpecialEdition-D-inrange-decipher-archive.gif.wiki" "File: Decipher archive Original In Range"
edit "File:Hoth-L-infantrymine-decipher-archive.gif" "$PAGES/File_Hoth-L-infantrymine-decipher-archive.gif.wiki" "File: Decipher archive Original Infantry Mine"
edit "File:Hoth-D-infantrymine-decipher-archive.gif" "$PAGES/File_Hoth-D-infantrymine-decipher-archive.gif.wiki" "File: Decipher archive Original Infantry Mine (Dark)"
edit "File:Premiere-D-ioncannon-decipher-archive.gif" "$PAGES/File_Premiere-D-ioncannon-decipher-archive.gif.wiki" "File: Decipher archive Original Ion Cannon"
edit "File:CloudCity-L-innocentscoundrel-decipher-archive.gif" "$PAGES/File_CloudCity-L-innocentscoundrel-decipher-archive.gif.wiki" "File: Decipher archive Original Innocent Scoundrel"
edit "I'm On The Leader (Original)" "$PAGES/I'm_On_The_Leader_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I'm On The Leader (PC Errata)" "$PAGES/I'm_On_The_Leader_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I'm On The Leader" "$PAGES/I'm_On_The_Leader.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "I've Got A Bad Feeling About This (Original)" "$PAGES/I've_Got_A_Bad_Feeling_About_This_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I've Got A Bad Feeling About This (PC Errata)" "$PAGES/I've_Got_A_Bad_Feeling_About_This_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I've Got A Bad Feeling About This" "$PAGES/I've_Got_A_Bad_Feeling_About_This.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "I've Got A Problem Here (Original)" "$PAGES/I've_Got_A_Problem_Here_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I've Got A Problem Here (PC Errata)" "$PAGES/I've_Got_A_Problem_Here_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I've Got A Problem Here" "$PAGES/I've_Got_A_Problem_Here.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "I've Lost Artoo! (Original)" "$PAGES/I've_Lost_Artoo!_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I've Lost Artoo! (PC Errata)" "$PAGES/I've_Lost_Artoo!_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I've Lost Artoo!" "$PAGES/I've_Lost_Artoo!.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "I Had No Choice (Original)" "$PAGES/I_Had_No_Choice_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I Had No Choice (PC Errata)" "$PAGES/I_Had_No_Choice_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I Had No Choice" "$PAGES/I_Had_No_Choice.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "I Thought They Smelled Bad On The Outside (Original)" "$PAGES/I_Thought_They_Smelled_Bad_On_The_Outside_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "I Thought They Smelled Bad On The Outside (PC Errata)" "$PAGES/I_Thought_They_Smelled_Bad_On_The_Outside_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "I Thought They Smelled Bad On The Outside" "$PAGES/I_Thought_They_Smelled_Bad_On_The_Outside.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Imperial Trooper Guard (Original)" "$PAGES/Imperial_Trooper_Guard_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Trooper Guard (PC Errata)" "$PAGES/Imperial_Trooper_Guard_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Trooper Guard" "$PAGES/Imperial_Trooper_Guard.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "In Range (Original)" "$PAGES/In_Range_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "In Range (PC Errata)" "$PAGES/In_Range_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "In Range" "$PAGES/In_Range.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Infantry Mine (Original)" "$PAGES/Infantry_Mine_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Infantry Mine (PC Errata)" "$PAGES/Infantry_Mine_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Infantry Mine" "$PAGES/Infantry_Mine.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Infantry Mine (Dark) (Original)" "$PAGES/Infantry_Mine_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Infantry Mine (Dark) (PC Errata)" "$PAGES/Infantry_Mine_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Infantry Mine (Dark)" "$PAGES/Infantry_Mine_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Ion Cannon (Original)" "$PAGES/Ion_Cannon_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ion Cannon (PC Errata)" "$PAGES/Ion_Cannon_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ion Cannon" "$PAGES/Ion_Cannon.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Innocent Scoundrel (Original)" "$PAGES/Innocent_Scoundrel_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Innocent Scoundrel (PC Errata)" "$PAGES/Innocent_Scoundrel_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Innocent Scoundrel" "$PAGES/Innocent_Scoundrel.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch19 (Im On The Leader through Innocent Scoundrel; Infantry Mine dual)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch19 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "I'm On The Leader" \
  "I'm On The Leader (Original)" \
  "I'm On The Leader (PC Errata)" \
  "I've Got A Bad Feeling About This" \
  "I've Got A Bad Feeling About This (Original)" \
  "I've Got A Bad Feeling About This (PC Errata)" \
  "I've Got A Problem Here" \
  "I've Got A Problem Here (Original)" \
  "I've Got A Problem Here (PC Errata)" \
  "I've Lost Artoo!" \
  "I've Lost Artoo! (Original)" \
  "I've Lost Artoo! (PC Errata)" \
  "I Had No Choice" \
  "I Had No Choice (Original)" \
  "I Had No Choice (PC Errata)" \
  "I Thought They Smelled Bad On The Outside" \
  "I Thought They Smelled Bad On The Outside (Original)" \
  "I Thought They Smelled Bad On The Outside (PC Errata)" \
  "Imperial Trooper Guard" \
  "Imperial Trooper Guard (Original)" \
  "Imperial Trooper Guard (PC Errata)" \
  "In Range" \
  "In Range (Original)" \
  "In Range (PC Errata)" \
  "Infantry Mine" \
  "Infantry Mine (Original)" \
  "Infantry Mine (PC Errata)" \
  "Infantry Mine (Dark)" \
  "Infantry Mine (Dark) (Original)" \
  "Infantry Mine (Dark) (PC Errata)" \
  "Ion Cannon" \
  "Ion Cannon (Original)" \
  "Ion Cannon (PC Errata)" \
  "Innocent Scoundrel" \
  "Innocent Scoundrel (Original)" \
  "Innocent Scoundrel (PC Errata)" \
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
echo DONE_APPLY_BATCH19_PC_ERRATA
