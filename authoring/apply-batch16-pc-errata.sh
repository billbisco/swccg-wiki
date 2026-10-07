#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch16-gifs

ARCHIVES=(
  Dagobah-D-frustration-decipher-archive.gif
  Premiere-L-fusiongeneratorsupplytank-decipher-archive.gif
  Premiere-D-fusiongeneratorsupplydark-decipher-archive.gif
  CloudCity-L-gamblersluck-decipher-archive.gif
  Premiere-D-grandmofftarkin-decipher-archive.gif
  Premiere-D-gaderffiistick-decipher-archive.gif
  ANewHope-L-grimtaash-decipher-archive.gif
  SpecialEdition-L-grondornmuse-decipher-archive.gif
  Premiere-L-hansolo-decipher-archive.gif
  Dagobah-L-hanstoolkit-decipher-archive.gif
  CloudCity-L-haven-decipher-archive.gif
  Premiere-L-hearmebabyholdtogether-decipher-archive.gif
  Premiere-L-hyperescape-decipher-archive.gif
)
HT_FILES=(
  Dagobah-D-frustration.gif
  Premiere-L-fusiongeneratorsupplytanks.gif
  Premiere-D-fusiongeneratorsupplytanks.gif
  CC-L-gamblersluck.gif
  Premiere-D-grandmofftarkin.gif
  Premiere-D-gaderffiistick.gif
  ANH-L-grimtaash.gif
  SE-L-grondornmuse.gif
  Premiere-L-hansolo.gif
  Dagobah-L-hanstoolkit.gif
  CC-L-haven.gif
  Premiere-L-hearmebabyholdtogether.gif
  Premiere-L-hyperescape.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch16-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch16-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch16-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch16 (Frustration through Hyper Escape; Fusion dual); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch16-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch16-gifs
fi

edit "File:Dagobah-D-frustration-decipher-archive.gif" "$PAGES/File_Dagobah-D-frustration-decipher-archive.gif.wiki" "File: Decipher archive Original Frustration"
edit "File:Premiere-L-fusiongeneratorsupplytank-decipher-archive.gif" "$PAGES/File_Premiere-L-fusiongeneratorsupplytank-decipher-archive.gif.wiki" "File: Decipher archive Original Fusion Generator Supply Tanks"
edit "File:Premiere-D-fusiongeneratorsupplydark-decipher-archive.gif" "$PAGES/File_Premiere-D-fusiongeneratorsupplydark-decipher-archive.gif.wiki" "File: Decipher archive Original Fusion Generator Supply Tanks (Dark)"
edit "File:CloudCity-L-gamblersluck-decipher-archive.gif" "$PAGES/File_CloudCity-L-gamblersluck-decipher-archive.gif.wiki" "File: Decipher archive Original Gambler's Luck"
edit "File:Premiere-D-grandmofftarkin-decipher-archive.gif" "$PAGES/File_Premiere-D-grandmofftarkin-decipher-archive.gif.wiki" "File: Decipher archive Original Grand Moff Tarkin"
edit "File:Premiere-D-gaderffiistick-decipher-archive.gif" "$PAGES/File_Premiere-D-gaderffiistick-decipher-archive.gif.wiki" "File: Decipher archive Original Gaderffii Stick"
edit "File:ANewHope-L-grimtaash-decipher-archive.gif" "$PAGES/File_ANewHope-L-grimtaash-decipher-archive.gif.wiki" "File: Decipher archive Original Grimtaash"
edit "File:SpecialEdition-L-grondornmuse-decipher-archive.gif" "$PAGES/File_SpecialEdition-L-grondornmuse-decipher-archive.gif.wiki" "File: Decipher archive Original Grondorn Muse"
edit "File:Premiere-L-hansolo-decipher-archive.gif" "$PAGES/File_Premiere-L-hansolo-decipher-archive.gif.wiki" "File: Decipher archive Original Han Solo"
edit "File:Dagobah-L-hanstoolkit-decipher-archive.gif" "$PAGES/File_Dagobah-L-hanstoolkit-decipher-archive.gif.wiki" "File: Decipher archive Original Han's Toolkit"
edit "File:CloudCity-L-haven-decipher-archive.gif" "$PAGES/File_CloudCity-L-haven-decipher-archive.gif.wiki" "File: Decipher archive Original Haven"
edit "File:Premiere-L-hearmebabyholdtogether-decipher-archive.gif" "$PAGES/File_Premiere-L-hearmebabyholdtogether-decipher-archive.gif.wiki" "File: Decipher archive Original Hear Me Baby, Hold Together"
edit "File:Premiere-L-hyperescape-decipher-archive.gif" "$PAGES/File_Premiere-L-hyperescape-decipher-archive.gif.wiki" "File: Decipher archive Original Hyper Escape"

edit "Frustration (Original)" "$PAGES/Frustration_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Frustration (PC Errata)" "$PAGES/Frustration_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Frustration" "$PAGES/Frustration.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Fusion Generator Supply Tanks (Original)" "$PAGES/Fusion_Generator_Supply_Tanks_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Fusion Generator Supply Tanks (PC Errata)" "$PAGES/Fusion_Generator_Supply_Tanks_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Fusion Generator Supply Tanks" "$PAGES/Fusion_Generator_Supply_Tanks.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Fusion Generator Supply Tanks (Dark) (Original)" "$PAGES/Fusion_Generator_Supply_Tanks_(Dark)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Fusion Generator Supply Tanks (Dark) (PC Errata)" "$PAGES/Fusion_Generator_Supply_Tanks_(Dark)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Fusion Generator Supply Tanks (Dark)" "$PAGES/Fusion_Generator_Supply_Tanks_(Dark).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Gambler's Luck (Original)" "$PAGES/Gambler's_Luck_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Gambler's Luck (PC Errata)" "$PAGES/Gambler's_Luck_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Gambler's Luck" "$PAGES/Gambler's_Luck.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Grand Moff Tarkin (Original)" "$PAGES/Grand_Moff_Tarkin_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Grand Moff Tarkin (PC Errata)" "$PAGES/Grand_Moff_Tarkin_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Grand Moff Tarkin" "$PAGES/Grand_Moff_Tarkin.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Gaderffii Stick (Original)" "$PAGES/Gaderffii_Stick_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Gaderffii Stick (PC Errata)" "$PAGES/Gaderffii_Stick_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Gaderffii Stick" "$PAGES/Gaderffii_Stick.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Grimtaash (Original)" "$PAGES/Grimtaash_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Grimtaash (PC Errata)" "$PAGES/Grimtaash_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Grimtaash" "$PAGES/Grimtaash.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Grondorn Muse (Original)" "$PAGES/Grondorn_Muse_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Grondorn Muse (PC Errata)" "$PAGES/Grondorn_Muse_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Grondorn Muse" "$PAGES/Grondorn_Muse.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Han Solo (Original)" "$PAGES/Han_Solo_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Han Solo (PC Errata)" "$PAGES/Han_Solo_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Han Solo" "$PAGES/Han_Solo.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Han's Toolkit (Original)" "$PAGES/Han's_Toolkit_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Han's Toolkit (PC Errata)" "$PAGES/Han's_Toolkit_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Han's Toolkit" "$PAGES/Han's_Toolkit.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Haven (Original)" "$PAGES/Haven_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Haven (PC Errata)" "$PAGES/Haven_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Haven" "$PAGES/Haven.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Hear Me Baby, Hold Together (Original)" "$PAGES/Hear_Me_Baby,_Hold_Together_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Hear Me Baby, Hold Together (PC Errata)" "$PAGES/Hear_Me_Baby,_Hold_Together_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Hear Me Baby, Hold Together" "$PAGES/Hear_Me_Baby,_Hold_Together.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Hyper Escape (Original)" "$PAGES/Hyper_Escape_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Hyper Escape (PC Errata)" "$PAGES/Hyper_Escape_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Hyper Escape" "$PAGES/Hyper_Escape.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch16 (Frustration through Hyper Escape; Fusion dual)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch16 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "Frustration" "Frustration (Original)" "Frustration (PC Errata)" \
  "Fusion Generator Supply Tanks" "Fusion Generator Supply Tanks (Original)" "Fusion Generator Supply Tanks (PC Errata)" \
  "Fusion Generator Supply Tanks (Dark)" "Fusion Generator Supply Tanks (Dark) (Original)" "Fusion Generator Supply Tanks (Dark) (PC Errata)" \
  "Gambler's Luck" "Gambler's Luck (Original)" "Gambler's Luck (PC Errata)" \
  "Grand Moff Tarkin" "Grand Moff Tarkin (Original)" "Grand Moff Tarkin (PC Errata)" \
  "Gaderffii Stick" "Gaderffii Stick (Original)" "Gaderffii Stick (PC Errata)" \
  "Grimtaash" "Grimtaash (Original)" "Grimtaash (PC Errata)" \
  "Grondorn Muse" "Grondorn Muse (Original)" "Grondorn Muse (PC Errata)" \
  "Han Solo" "Han Solo (Original)" "Han Solo (PC Errata)" \
  "Han's Toolkit" "Han's Toolkit (Original)" "Han's Toolkit (PC Errata)" \
  "Haven" "Haven (Original)" "Haven (PC Errata)" \
  "Hear Me Baby, Hold Together" "Hear Me Baby, Hold Together (Original)" "Hear Me Baby, Hold Together (PC Errata)" \
  "Hyper Escape" "Hyper Escape (Original)" "Hyper Escape (PC Errata)" \
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
echo DONE_APPLY_BATCH16_PC_ERRATA
