#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGE="$ROOT/pages/Timo_Dusel.wiki"
SUMMARY='Tournament Results table; remove Decklists (sample for Bill)'

if [ ! -s "$PAGE" ]; then
  echo "ERROR: missing $PAGE" >&2
  exit 1
fi
python3 - <<'PY'
from pathlib import Path
p = Path('/opt/swccg-wiki/pages/Timo_Dusel.wiki')
raw = p.read_bytes()
if raw.startswith(b'\xef\xbb\xbf'):
    raw = raw[3:]
text = raw.decode('utf-8').replace('\r\n', '\n').replace('\r', '\n')
p.write_text(text, encoding='utf-8', newline='\n')
PY

echo '== edit Timo Dusel =='
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$SUMMARY" 'Timo Dusel' < "$PAGE"

echo '== FlaggedRevs reviewAllPages =='
review_rc=0
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || review_rc=$?
echo "reviewAllPages exit=$review_rc (continued to purge)"

echo '== purge Timo Dusel =='
printf '%s\n' 'Timo Dusel' | docker exec -i swccg_wiki php maintenance/run.php purgePage

echo '== live getText verification =='
docker exec swccg_wiki php maintenance/run.php getText 'Timo Dusel'