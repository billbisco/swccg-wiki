#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-batch17-gifs

ARCHIVES=(
  Hoth-D-highanxiety-decipher-archive.gif
  CloudCity-L-hindsight-decipher-archive.gif
  Dagobah-D-holonettransmission-decipher-archive.gif
  CloudCity-D-humanshield-decipher-archive.gif
  Premiere-L-hydroponicsstation-decipher-archive.gif
  JabbasPalace-L-hnemthe-decipher-archive.gif
  ANewHope-L-hetnkik-decipher-archive.gif
  ANewHope-L-houjix-decipher-archive.gif
  JabbasPalace-D-huttbounty-decipher-archive.gif
  CloudCity-L-higherground-decipher-archive.gif
  ANewHope-D-hypo-decipher-archive.gif
  CloudCity-D-imperialdecree-decipher-archive.gif

)
HT_FILES=(
  Hoth-D-highanxiety.gif
  CC-L-hindsight_readable.gif
  Dagobah-D-holonettransmission.gif
  CC-D-humanshield.gif
  Premiere-L-hydroponicsstation.gif
  JP-L-hnemthe.gif
  ANH-L-hetnkik.gif
  ANH-L-houjix.gif
  JP-D-huttbounty.gif
  CC-L-higherground.gif
  ANH-D-hypo.gif
  CC-D-imperialdecree.gif
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

docker exec swccg_wiki mkdir -p /tmp/pc-errata-batch17-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-batch17-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-batch17-gifs/
COMMENT="Decipher.com archive Originals for PC Errata batch17 (High Anxiety through Imperial Decree); flush crop + flood bleach #FFF. DO NOT replace Holotable."
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-batch17-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-batch17-gifs
fi

edit "File:Hoth-D-highanxiety-decipher-archive.gif" "$PAGES/File_Hoth-D-highanxiety-decipher-archive.gif.wiki" "File: Decipher archive Original High Anxiety"
edit "File:CloudCity-L-hindsight-decipher-archive.gif" "$PAGES/File_CloudCity-L-hindsight-decipher-archive.gif.wiki" "File: Decipher archive Original Hindsight"
edit "File:Dagobah-D-holonettransmission-decipher-archive.gif" "$PAGES/File_Dagobah-D-holonettransmission-decipher-archive.gif.wiki" "File: Decipher archive Original HoloNet Transmission"
edit "File:CloudCity-D-humanshield-decipher-archive.gif" "$PAGES/File_CloudCity-D-humanshield-decipher-archive.gif.wiki" "File: Decipher archive Original Human Shield"
edit "File:Premiere-L-hydroponicsstation-decipher-archive.gif" "$PAGES/File_Premiere-L-hydroponicsstation-decipher-archive.gif.wiki" "File: Decipher archive Original Hydroponics Station"
edit "File:JabbasPalace-L-hnemthe-decipher-archive.gif" "$PAGES/File_JabbasPalace-L-hnemthe-decipher-archive.gif.wiki" "File: Decipher archive Original H'nemthe"
edit "File:ANewHope-L-hetnkik-decipher-archive.gif" "$PAGES/File_ANewHope-L-hetnkik-decipher-archive.gif.wiki" "File: Decipher archive Original Het Nkik"
edit "File:ANewHope-L-houjix-decipher-archive.gif" "$PAGES/File_ANewHope-L-houjix-decipher-archive.gif.wiki" "File: Decipher archive Original Houjix"
edit "File:JabbasPalace-D-huttbounty-decipher-archive.gif" "$PAGES/File_JabbasPalace-D-huttbounty-decipher-archive.gif.wiki" "File: Decipher archive Original Hutt Bounty"
edit "File:CloudCity-L-higherground-decipher-archive.gif" "$PAGES/File_CloudCity-L-higherground-decipher-archive.gif.wiki" "File: Decipher archive Original Higher Ground"
edit "File:ANewHope-D-hypo-decipher-archive.gif" "$PAGES/File_ANewHope-D-hypo-decipher-archive.gif.wiki" "File: Decipher archive Original Hypo"
edit "File:CloudCity-D-imperialdecree-decipher-archive.gif" "$PAGES/File_CloudCity-D-imperialdecree-decipher-archive.gif.wiki" "File: Decipher archive Original Imperial Decree"
edit "High Anxiety (Original)" "$PAGES/High_Anxiety_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "High Anxiety (PC Errata)" "$PAGES/High_Anxiety_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "High Anxiety" "$PAGES/High_Anxiety.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Hindsight (Original)" "$PAGES/Hindsight_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Hindsight (PC Errata)" "$PAGES/Hindsight_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Hindsight" "$PAGES/Hindsight.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "HoloNet Transmission (Original)" "$PAGES/HoloNet_Transmission_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "HoloNet Transmission (PC Errata)" "$PAGES/HoloNet_Transmission_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "HoloNet Transmission" "$PAGES/HoloNet_Transmission.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Human Shield (Original)" "$PAGES/Human_Shield_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Human Shield (PC Errata)" "$PAGES/Human_Shield_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Human Shield" "$PAGES/Human_Shield.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Hydroponics Station (Original)" "$PAGES/Hydroponics_Station_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Hydroponics Station (PC Errata)" "$PAGES/Hydroponics_Station_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Hydroponics Station" "$PAGES/Hydroponics_Station.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "H'nemthe (Original)" "$PAGES/H'nemthe_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "H'nemthe (PC Errata)" "$PAGES/H'nemthe_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "H'nemthe" "$PAGES/H'nemthe.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Het Nkik (Original)" "$PAGES/Het_Nkik_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Het Nkik (PC Errata)" "$PAGES/Het_Nkik_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Het Nkik" "$PAGES/Het_Nkik.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Houjix (Original)" "$PAGES/Houjix_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Houjix (PC Errata)" "$PAGES/Houjix_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Houjix" "$PAGES/Houjix.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Hutt Bounty (Original)" "$PAGES/Hutt_Bounty_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Hutt Bounty (PC Errata)" "$PAGES/Hutt_Bounty_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Hutt Bounty" "$PAGES/Hutt_Bounty.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Higher Ground (Original)" "$PAGES/Higher_Ground_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Higher Ground (PC Errata)" "$PAGES/Higher_Ground_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Higher Ground" "$PAGES/Higher_Ground.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Hypo (Original)" "$PAGES/Hypo_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Hypo (PC Errata)" "$PAGES/Hypo_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Hypo" "$PAGES/Hypo.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Imperial Decree (Original)" "$PAGES/Imperial_Decree_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "Imperial Decree (PC Errata)" "$PAGES/Imperial_Decree_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable"
edit "Imperial Decree" "$PAGES/Imperial_Decree.wiki" "Restore Decipher print; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add batch17 (High Anxiety through Imperial Decree)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index batch17 PC Errata seeds"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -20 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -20 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in \
  "High Anxiety" \
  "High Anxiety (Original)" \
  "High Anxiety (PC Errata)" \
  "Hindsight" \
  "Hindsight (Original)" \
  "Hindsight (PC Errata)" \
  "HoloNet Transmission" \
  "HoloNet Transmission (Original)" \
  "HoloNet Transmission (PC Errata)" \
  "Human Shield" \
  "Human Shield (Original)" \
  "Human Shield (PC Errata)" \
  "Hydroponics Station" \
  "Hydroponics Station (Original)" \
  "Hydroponics Station (PC Errata)" \
  "H'nemthe" \
  "H'nemthe (Original)" \
  "H'nemthe (PC Errata)" \
  "Het Nkik" \
  "Het Nkik (Original)" \
  "Het Nkik (PC Errata)" \
  "Houjix" \
  "Houjix (Original)" \
  "Houjix (PC Errata)" \
  "Hutt Bounty" \
  "Hutt Bounty (Original)" \
  "Hutt Bounty (PC Errata)" \
  "Higher Ground" \
  "Higher Ground (Original)" \
  "Higher Ground (PC Errata)" \
  "Hypo" \
  "Hypo (Original)" \
  "Hypo (PC Errata)" \
  "Imperial Decree" \
  "Imperial Decree (Original)" \
  "Imperial Decree (PC Errata)" \
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
echo DONE_APPLY_BATCH17_PC_ERRATA
