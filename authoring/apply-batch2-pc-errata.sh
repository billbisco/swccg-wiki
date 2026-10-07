#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch2-gifs

ARCHIVES=(
  Premiere-L-affectmind-decipher-archive.gif
  CC-D-abilityabilityability-decipher-archive.gif
  Premiere-D-adisturbanceintheforce-decipher-archive.gif
  Premiere-L-atremorintheforce-decipher-archive.gif
  CC-L-advantage-decipher-archive.gif
  Hoth-D-admiralozzel-decipher-archive.gif
)
HT_FILES=(
  Premiere-L-affectmind.gif
  CC-D-abilityabilityability.gif
  Premiere-D-adisturbanceintheforce.gif
  Premiere-L-atremorintheforce.gif
  CC-L-advantage.gif
  Hoth-D-admiralozzel.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch2-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch2-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch2-gifs/
COMMENT='Decipher.com archive Originals for PC Errata batch2 (Affect Mind, Ability Ability Ability, Disturbance, Tremor, Advantage, Admiral Ozzel); flush [3:493,3:353] + flood bleach #FFF. DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch2-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch2-gifs
fi

edit "File:Premiere-L-affectmind-decipher-archive.gif" "$PAGES/File_Premiere-L-affectmind-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original Affect Mind"
edit "File:CC-D-abilityabilityability-decipher-archive.gif" "$PAGES/File_CC-D-abilityabilityability-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Ability Ability Ability"
edit "File:Premiere-D-adisturbanceintheforce-decipher-archive.gif" "$PAGES/File_Premiere-D-adisturbanceintheforce-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original A Disturbance In The Force"
edit "File:Premiere-L-atremorintheforce-decipher-archive.gif" "$PAGES/File_Premiere-L-atremorintheforce-decipher-archive.gif.wiki" "File: Decipher Premiere archive Original A Tremor In The Force"
edit "File:CC-L-advantage-decipher-archive.gif" "$PAGES/File_CC-L-advantage-decipher-archive.gif.wiki" "File: Decipher Cloud City archive Original Advantage"
edit "File:Hoth-D-admiralozzel-decipher-archive.gif" "$PAGES/File_Hoth-D-admiralozzel-decipher-archive.gif.wiki" "File: Decipher Hoth archive Original Admiral Ozzel"

edit "Affect Mind (Original)" "$PAGES/Affect_Mind_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Affect Mind (PC Errata)" "$PAGES/Affect_Mind_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Affect Mind" "$PAGES/Affect_Mind.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Ability, Ability, Ability (Original)" "$PAGES/Ability,_Ability,_Ability_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Ability, Ability, Ability (PC Errata)" "$PAGES/Ability,_Ability,_Ability_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Ability, Ability, Ability" "$PAGES/Ability,_Ability,_Ability.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "A Disturbance In The Force (Original)" "$PAGES/A_Disturbance_In_The_Force_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "A Disturbance In The Force (PC Errata)" "$PAGES/A_Disturbance_In_The_Force_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "A Disturbance In The Force" "$PAGES/A_Disturbance_In_The_Force.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "A Tremor In The Force (Original)" "$PAGES/A_Tremor_In_The_Force_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "A Tremor In The Force (PC Errata)" "$PAGES/A_Tremor_In_The_Force_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "A Tremor In The Force" "$PAGES/A_Tremor_In_The_Force.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Advantage (Original)" "$PAGES/Advantage_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Advantage (PC Errata)" "$PAGES/Advantage_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Advantage" "$PAGES/Advantage.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Admiral Ozzel (Original)" "$PAGES/Admiral_Ozzel_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Admiral Ozzel (PC Errata)" "$PAGES/Admiral_Ozzel_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Admiral Ozzel" "$PAGES/Admiral_Ozzel.wiki" "Restore Decipher print; archive face; link PC Errata"

edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add Affect Mind, Ability Ability Ability, Disturbance, Tremor, Advantage, Admiral Ozzel"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch2 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Affect Mind" "Affect Mind (Original)" "Affect Mind (PC Errata)" \
  "Ability, Ability, Ability" "Ability, Ability, Ability (Original)" "Ability, Ability, Ability (PC Errata)" \
  "A Disturbance In The Force" "A Disturbance In The Force (Original)" "A Disturbance In The Force (PC Errata)" \
  "A Tremor In The Force" "A Tremor In The Force (Original)" "A Tremor In The Force (PC Errata)" \
  "Advantage" "Advantage (Original)" "Advantage (PC Errata)" \
  "Admiral Ozzel" "Admiral Ozzel (Original)" "Admiral Ozzel (PC Errata)" \
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
echo DONE_APPLY_BATCH2_PC_ERRATA
