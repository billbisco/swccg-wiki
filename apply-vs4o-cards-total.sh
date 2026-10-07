#!/bin/bash
set -euo pipefail
HUB='/opt/swccg-wiki/pages/set-hubs/Virtual_Set_4_(Original).wiki'
TITLE='Virtual Set 4 (Original)'

python3 - <<'PY'
from pathlib import Path
p=Path('/opt/swccg-wiki/pages/set-hubs/Virtual_Set_4_(Original).wiki')
b=p.read_bytes()
if b.startswith(b'\xef\xbb\xbf'): b=b[3:]
p.write_bytes(b)
t=b.decode('utf-8')
assert 'Cards Total' in t
assert '|| 50 (Remaster slips 01' in t
n=sum(1 for c in t if ord(c)>127)
print(f'hub nonascii={n} len={len(t)}')
assert n==0, 'non-ascii in hub'
PY

echo "edit: $TITLE"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary='VS4 Original hub: set Cards Total=50 (soft gap close)' "$TITLE" < "$HUB"

echo '==== FlaggedRevs reviewAllPages ===='
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

echo '==== purge hub ===='
printf '%s\n' 'Virtual Set 4 (Original)' | docker exec -i swccg_wiki php maintenance/run.php purgePage

echo '==== verify getText ===='
docker exec swccg_wiki php maintenance/run.php getText "$TITLE" | python3 -c '
import sys
t=sys.stdin.read()
assert "Cards Total" in t
assert "|| 50 (Remaster slips 01" in t
i=t.index("Cards Total")
print(t[i-40:i+100])
print("VS4O_CARDS_TOTAL_APPLY_OK")
'