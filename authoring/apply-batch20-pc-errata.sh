#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch20-gifs

ARCHIVES=(
  ANewHope-D-ito-decipher-archive.gif
  Hoth-L-itcanwait-decipher-archive.gif
  JabbasPalace-D-jabbathehutt-decipher-archive.gif
  JabbasPalace-D-jabbassailbarge-decipher-archive.gif
  ANewHope-D-jawablaster-decipher-archive.gif
  ANewHope-L-jawaiongun-decipher-archive.gif
  Premiere-L-jekporkins-decipher-archive.gif
  Hoth-L-jeroenwebb-decipher-archive.gif
  Premiere-L-jedilightsaber-decipher-archive.gif
  CloudCity-L-intotheventilationshaftlefty-decipher-archive.gif
)
HT_FILES=(
  ANH-D-ito.gif
  Hoth-L-itcanwait.gif
  JP-D-jabbathehutt.gif
  JP-D-jabbassailbarge.gif
  ANH-D-jawablaster.gif
  ANH-L-jawaiongun.gif
  Premiere-L-jekporkins.gif
  Hoth-L-jeroenwebb.gif
  Premiere-L-jedilightsaber.gif
  CC-L-intotheventilationshaftlefty.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch20-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch20-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch20-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch20 (IT-O through Into The Ventilation Shaft, Lefty); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch20-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch20-gifs
fi

edit "File:ANewHope-D-ito-decipher-archive.gif" "$PAGES/File_ANewHope-D-ito-decipher-archive.gif.wiki" "File: Decipher archive Original IT-O (Eyetee-Oh)"
edit "File:Hoth-L-itcanwait-decipher-archive.gif" "$PAGES/File_Hoth-L-itcanwait-decipher-archive.gif.wiki" "File: Decipher archive Original It Can Wait"
edit "File:JabbasPalace-D-jabbathehutt-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-jabbathehutt-decipher-archive.gif.wiki" "File: Decipher archive Original Jabba The Hutt"
edit "File:JabbasPalace-D-jabbassailbarge-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-jabbassailbarge-decipher-archive.gif.wiki" "File: Decipher archive Original Jabba's Sail Barge"
edit "File:ANewHope-D-jawablaster-decipher-archive.gif" "$PAGES/File_ANewHope-D-jawablaster-decipher-archive.gif.wiki" "File: Decipher archive Original Jawa Blaster"
edit "File:ANewHope-L-jawaiongun-decipher-archive.gif" "$PAGES/File_ANewHope-L-jawaiongun-decipher-archive.gif.wiki" "File: Decipher archive Original Jawa Ion Gun"
edit "File:Premiere-L-jekporkins-decipher-archive.gif" "$PAGES/File_Premiere-L-jekporkins-decipher-archive.gif.wiki" "File: Decipher archive Original Jek Porkins"
edit "File:Hoth-L-jeroenwebb-decipher-archive.gif" "$PAGES/File_Hoth-L-jeroenwebb-decipher-archive.gif.wiki" "File: Decipher archive Original Jeroen Webb"
edit "File:Premiere-L-jedilightsaber-decipher-archive.gif" "$PAGES/File_Premiere-L-jedilightsaber-decipher-archive.gif.wiki" "File: Decipher archive Original Jedi Lightsaber"
edit "File:CloudCity-L-intotheventilationshaftlefty-decipher-archive.gif" "$PAGES/File_CloudCity-L-intotheventilationshaftlefty-decipher-archive.gif.wiki" "File: Decipher archive Original Into The Ventilation Shaft, Lefty"
edit "IT-O (Eyetee-Oh) (Original)" "$PAGES/IT-O_(Eyetee-Oh)_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "IT-O (Eyetee-Oh) (PC Errata)" "$PAGES/IT-O_(Eyetee-Oh)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "IT-O (Eyetee-Oh)" "$PAGES/IT-O_(Eyetee-Oh).wiki" "Restore Decipher print; archive face; link PC Errata"
edit "It Can Wait (Original)" "$PAGES/It_Can_Wait_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "It Can Wait (PC Errata)" "$PAGES/It_Can_Wait_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "It Can Wait" "$PAGES/It_Can_Wait.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Jabba The Hutt (Original)" "$PAGES/Jabba_The_Hutt_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Jabba The Hutt (PC Errata)" "$PAGES/Jabba_The_Hutt_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Jabba The Hutt" "$PAGES/Jabba_The_Hutt.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Jabba's Sail Barge (Original)" "$PAGES/Jabba's_Sail_Barge_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Jabba's Sail Barge (PC Errata)" "$PAGES/Jabba's_Sail_Barge_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Jabba's Sail Barge" "$PAGES/Jabba's_Sail_Barge.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Jawa Blaster (Original)" "$PAGES/Jawa_Blaster_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Jawa Blaster (PC Errata)" "$PAGES/Jawa_Blaster_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Jawa Blaster" "$PAGES/Jawa_Blaster.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Jawa Ion Gun (Original)" "$PAGES/Jawa_Ion_Gun_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Jawa Ion Gun (PC Errata)" "$PAGES/Jawa_Ion_Gun_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Jawa Ion Gun" "$PAGES/Jawa_Ion_Gun.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Jek Porkins (Original)" "$PAGES/Jek_Porkins_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Jek Porkins (PC Errata)" "$PAGES/Jek_Porkins_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Jek Porkins" "$PAGES/Jek_Porkins.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Jeroen Webb (Original)" "$PAGES/Jeroen_Webb_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Jeroen Webb (PC Errata)" "$PAGES/Jeroen_Webb_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Jeroen Webb" "$PAGES/Jeroen_Webb.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Jedi Lightsaber (Original)" "$PAGES/Jedi_Lightsaber_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Jedi Lightsaber (PC Errata)" "$PAGES/Jedi_Lightsaber_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Jedi Lightsaber" "$PAGES/Jedi_Lightsaber.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Into The Ventilation Shaft, Lefty (Original)" "$PAGES/Into_The_Ventilation_Shaft,_Lefty_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Into The Ventilation Shaft, Lefty (PC Errata)" "$PAGES/Into_The_Ventilation_Shaft,_Lefty_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Into The Ventilation Shaft, Lefty" "$PAGES/Into_The_Ventilation_Shaft,_Lefty.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch20 (IT-O through Into The Ventilation Shaft, Lefty)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch20 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "IT-O (Eyetee-Oh)" \
  "IT-O (Eyetee-Oh) (Original)" \
  "IT-O (Eyetee-Oh) (PC Errata)" \
  "It Can Wait" \
  "It Can Wait (Original)" \
  "It Can Wait (PC Errata)" \
  "Jabba The Hutt" \
  "Jabba The Hutt (Original)" \
  "Jabba The Hutt (PC Errata)" \
  "Jabba's Sail Barge" \
  "Jabba's Sail Barge (Original)" \
  "Jabba's Sail Barge (PC Errata)" \
  "Jawa Blaster" \
  "Jawa Blaster (Original)" \
  "Jawa Blaster (PC Errata)" \
  "Jawa Ion Gun" \
  "Jawa Ion Gun (Original)" \
  "Jawa Ion Gun (PC Errata)" \
  "Jek Porkins" \
  "Jek Porkins (Original)" \
  "Jek Porkins (PC Errata)" \
  "Jeroen Webb" \
  "Jeroen Webb (Original)" \
  "Jeroen Webb (PC Errata)" \
  "Jedi Lightsaber" \
  "Jedi Lightsaber (Original)" \
  "Jedi Lightsaber (PC Errata)" \
  "Into The Ventilation Shaft, Lefty" \
  "Into The Ventilation Shaft, Lefty (Original)" \
  "Into The Ventilation Shaft, Lefty (PC Errata)" \
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
echo DONE_APPLY_BATCH20_PC_ERRATA
