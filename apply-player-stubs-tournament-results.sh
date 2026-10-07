#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
STUBS="$ROOT/pages/player-stubs"
SUMMARY='Tournament Results table (Event|Format|Finish|Dark|Light); remove Decklists; match Timo standard'

if [ ! -d "$STUBS" ]; then
  echo "ERROR: missing $STUBS" >&2
  exit 1
fi

# Normalize newlines / strip BOM
python3 - <<'PY'
from pathlib import Path
d = Path('/opt/swccg-wiki/pages/player-stubs')
for p in sorted(d.glob('*.wiki')):
    raw = p.read_bytes()
    if raw.startswith(b'\xef\xbb\xbf'):
        raw = raw[3:]
    text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
    if not text.endswith('\n'):
        text += '\n'
    p.write_text(text, encoding='utf-8', newline='\n')
print('normalized', len(list(d.glob("*.wiki"))), 'wiki files')
PY

mapfile -t FILES < <(ls "$STUBS"/*.wiki | sort)
echo "Editing ${#FILES[@]} player stubs..."
ok=0
fail=0
for f in "${FILES[@]}"; do
  base=$(basename "$f" .wiki)
  title="${base//_/ }"
  if docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$SUMMARY" "$title" < "$f"; then
    ok=$((ok+1))
    echo "OK $title"
  else
    fail=$((fail+1))
    echo "FAIL $title" >&2
  fi
done
echo "EDIT_DONE ok=$ok fail=$fail"

echo '== FlaggedRevs reviewAllPages =='
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo '== purge touched titles =='
for f in "${FILES[@]}"; do
  base=$(basename "$f" .wiki)
  title="${base//_/ }"
  printf '%s\n' "$title" | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
done

echo '== spot-check getText =='
for t in 'Timo Dusel' 'Jonny Chu' 'Bill Bisco' 'David Garcia'; do
  echo "----- $t -----"
  docker exec swccg_wiki php maintenance/run.php getText "$t" | head -40
done
