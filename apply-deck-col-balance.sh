#!/bin/bash
# Apply dynamic two-column decklist balance for all 2026 Retro GEMPC decks. VPS only.
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  if [ ! -s "$file" ]; then echo "ERROR: missing $file" >&2; exit 1; fi
  strip_bom "$file"
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

SUMMARY='Dynamic two-column decklist balance: whole type blocks assigned to minimize |left_lines-right_lines|'

shopt -s nullglob
files=("$PAGES"/2026_Retro_GEMPC_*.wiki)
# Exclude layout-suffix companions if present in pages/
count=0
for f in "${files[@]}"; do
  base=$(basename "$f")
  case "$base" in
    *'(two-column'*|*'two-column_layout'*|*'(picture'*|*'picture_layout'*|*'(single'*) continue ;;
  esac
  # Only edit files we staged for this apply (presence is enough; pages/ holds the new content)
  title=${base%.wiki}
  title=${title//_/ }
  edit "$title" "$f" "$SUMMARY"
  count=$((count+1))
done
echo "== edited $count pages =="

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin

echo "== purgePage batch =="
{
  for f in "${files[@]}"; do
    base=$(basename "$f")
    case "$base" in
      *'(two-column'*|*'two-column_layout'*|*'(picture'*|*'picture_layout'*|*'(single'*) continue ;;
    esac
    title=${base%.wiki}
    title=${title//_/ }
    printf '%s\n' "$title"
  done
} | docker exec -i swccg_wiki php maintenance/run.php purgePage

echo "== DONE apply-deck-col-balance =="
