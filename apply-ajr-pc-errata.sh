#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-ajr-gifs
ARCHIVE=Tat-L-ajedisresilience-decipher-archive.gif
HT_FILE=Tat-L-ajedisresilience.gif

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
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -type f -name '"$HT_FILE"' | head -1); sha1sum "$f" | awk "{print \$1}"'
}

echo "== Holotable BEFORE =="
HT_BEFORE=$(ht_hex)
echo "ht_before=$HT_BEFORE"
test -n "$HT_BEFORE"

mkdir -p "$STAGE"; rm -f "$STAGE"/*
test -f "$ROOT/set-card-art/$ARCHIVE"
cp -f "$ROOT/set-card-art/$ARCHIVE" "$STAGE/$ARCHIVE"
if [ -f "$STAGE/$HT_FILE" ]; then echo REFUSING; exit 1; fi

docker exec swccg_wiki mkdir -p /tmp/pc-errata-ajr-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-ajr-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-ajr-gifs/
COMMENT='Decipher Tatooine archive Original for A Jedi'\''s Resilience PC Errata; flush crop + pads #FFFFFF (~350x490). DO NOT replace Holotable.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-ajr-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-ajr-gifs
fi

edit "File:$ARCHIVE" "$PAGES/File_Tat-L-ajedisresilience-decipher-archive.gif.wiki" "File page: Decipher Tatooine archive Original for A Jedi's Resilience"
edit "A Jedi's Resilience (Original)" "$PAGES/A_Jedi's_Resilience_(Original).wiki" "PC Errata seed: printed Decipher archive Original"
edit "A Jedi's Resilience (PC Errata)" "$PAGES/A_Jedi's_Resilience_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A + Holotable face"
edit "A Jedi's Resilience" "$PAGES/A_Jedi's_Resilience.wiki" "Restore Decipher printed game text; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: add A Jedi's Resilience row"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index A Jedi's Resilience (PC Errata)"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -15 \
  || docker exec swccg_wiki php maintenance/run.php reviewAllPages --username=Admin 2>&1 | tail -15 \
  || true

purge() {
  docker exec swccg_wiki php maintenance/run.php purgePage "$1" 2>/dev/null \
    || docker exec swccg_wiki php maintenance/purgePage.php "$1" 2>/dev/null || true
}
for t in "A Jedi's Resilience" "A Jedi's Resilience (Original)" "A Jedi's Resilience (PC Errata)" \
  Errata "PC Errata" "File:$ARCHIVE" "File:$HT_FILE"; do
  echo "purge $t"; purge "$t"
done

HT_AFTER=$(ht_hex)
echo "ht_after=$HT_AFTER"
test "$HT_AFTER" = "$HT_BEFORE"
echo HOLOTABLE_OK
echo DONE_APPLY_AJR_PC_ERRATA
