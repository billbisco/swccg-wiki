#!/bin/bash
# Apply a titles TSV (title<TAB>relpath) via docker edit + FlaggedRevs + purge.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
TSV="${1:-}"
SUMMARY="${2:-wiki tournament pages}"
if [ ! -s "$TSV" ]; then
  echo "ERROR: missing $TSV" >&2
  exit 1
fi

n=0
while IFS=$'\t' read -r title rel; do
  title="${title%$'\r'}"
  rel="${rel%$'\r'}"
  [ -z "${title:-}" ] && continue
  f="$ROOT/$rel"
  if [ ! -f "$f" ]; then
    echo "MISSING $f" >&2
    continue
  fi
  n=$((n+1))
  echo "== edit $n $title =="
  python3 - "$f" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
if not text.endswith("\n"):
    text += "\n"
p.write_text(text, encoding="utf-8", newline="\n")
PY
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="$SUMMARY" \
    "$title" < "$f" || echo "EDITFAIL $title" >&2
done < "$TSV"

echo "== FlaggedRevs ReviewTitles =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true

echo "== purge =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo DONE n=$n tsv=$TSV
