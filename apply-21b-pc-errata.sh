#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
STAGE=/tmp/pc-errata-21b-gifs
ARCHIVE=Hoth-L-21btooonebee-decipher-archive.gif
HT_FILE=Hoth-L-21btooonebee.gif

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys, re
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
# refuse gif File embeds in |notes=
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
  docker exec swccg_wiki bash -c 'f=$(find /var/www/html/images -name '"$HT_FILE"' | head -1); sha1sum "$f" | awk "{print \$1}"'
}

echo "== Holotable BEFORE =="
HT_BEFORE=$(ht_hex)
echo "ht_before=$HT_BEFORE"
test -n "$HT_BEFORE"

echo "== SAFETY: stage archive only =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
test -f "$ROOT/set-card-art/$ARCHIVE"
cp -f "$ROOT/set-card-art/$ARCHIVE" "$STAGE/$ARCHIVE"
# refuse Holotable in stage
if [ -f "$STAGE/$HT_FILE" ]; then echo "REFUSING Holotable in stage" >&2; exit 1; fi
ls -la "$STAGE"

echo "== importImages archive Original =="
docker exec swccg_wiki mkdir -p /tmp/pc-errata-21b-gifs
docker exec swccg_wiki bash -c 'rm -rf /tmp/pc-errata-21b-gifs/*'
docker cp "$STAGE/." swccg_wiki:/tmp/pc-errata-21b-gifs/
COMMENT='Decipher.com Hoth Light cardlists archive face for 2-1B (Too-Onebee) (Wayback); flush crop + exterior corner pads bleached #FFFFFF (~350x490). Original column on Errata PC Errata. DO NOT replace Holotable Hoth-L-21btooonebee.gif.'
set +e
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" --overwrite /tmp/pc-errata-21b-gifs
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="$COMMENT" /tmp/pc-errata-21b-gifs
fi

echo "== edit File description =="
edit "File:$ARCHIVE" "$PAGES/File_Hoth-L-21btooonebee-decipher-archive.gif.wiki" "File page: Decipher Hoth archive Original for 2-1B PC Errata seed"

echo "== edit card pages =="
edit "2-1B (Too-Onebee) (Original)" "$PAGES/2-1B_(Too-Onebee)_(Original).wiki" "PC Errata seed: printed Decipher archive Original for 2-1B"
edit "2-1B (Too-Onebee) (PC Errata)" "$PAGES/2-1B_(Too-Onebee)_(PC_Errata).wiki" "PC Errata seed: AR 2023 Appendix A game text + Holotable face"
edit "2-1B (Too-Onebee)" "$PAGES/2-1B_(Too-Onebee).wiki" "Restore Decipher printed game text; archive face; link PC Errata"
edit "Errata" "$PAGES/Errata.wiki" "PC Errata section: first row 2-1B (archive Original + Holotable PC)"
edit "PC Errata" "$PAGES/PC_Errata.wiki" "Index first PC-only Appendix A seed: 2-1B (Too-Onebee) (PC Errata)"

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
purge "2-1B (Too-Onebee)"
purge "2-1B (Too-Onebee) (Original)"
purge "2-1B (Too-Onebee) (PC Errata)"
purge "Errata"
purge "PC Errata"
purge "File:$ARCHIVE"
purge "File:$HT_FILE"

echo "== Holotable AFTER =="
HT_AFTER=$(ht_hex)
echo "ht_after=$HT_AFTER"
test "$HT_AFTER" = "$HT_BEFORE"
echo "HOLOTABLE_OK"
echo "DONE_APPLY_21B_PC_ERRATA"
