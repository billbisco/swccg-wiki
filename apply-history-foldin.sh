#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES=$ROOT/pages
strip() {
  python3 - <<PY
from pathlib import Path
p = Path("$1")
b = p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"):
    b = b[3:]
# refuse if mojibake markers already present in source? just strip BOM
p.write_bytes(b)
# report non-ascii
t = b.decode("utf-8")
n = sum(1 for c in t if ord(c) > 127)
print(f"source {p.name} nonascii={n}")
PY
}
edit() {
  local title="$1" file="$2" summary="$3"
  strip "$file"
  echo "edit $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}
edit "Virtual Sets (2002-2009)" "$PAGES/Virtual_Sets_(2002-2009).wiki" "ASCII-safe punctuation; Alpha1 HTML strengthens on VS rows; Shields cite"
edit "History of the Players Committee" "$PAGES/History_of_the_Players_Committee.wiki" "ASCII-safe punctuation; host forward / Mercenaries note"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -2
docker exec -i swccg_wiki php maintenance/run.php purgePage <<EOF
Virtual Sets (2002-2009)
History of the Players Committee
Pre-reorg Virtual Sets
EOF
docker exec swccg_wiki php maintenance/run.php getText "Virtual Sets (2002-2009)" > /tmp/vs_live.txt
docker exec swccg_wiki php maintenance/run.php getText "History of the Players Committee" > /tmp/hist_live.txt
python3 - <<'PY'
from pathlib import Path
for name in ['/tmp/vs_live.txt','/tmp/hist_live.txt']:
  t=Path(name).read_text(encoding='utf-8')
  non=[c for c in t if ord(c)>127]
  print(name, 'nonascii', len(non), 'mojibake', any(x in t for x in ['â€','Â·','Ã¢']))
  for needle in ['CardVault','22 Sep 2002','12 Dec 2004','8 June 2009','27 Mar 2004','18 Apr 2009','7 Aug 2008','reorganized into Blocks','Luke (V)','403','5 July 2009','Mercenaries']:
    if needle in t:
      print('  HAS', needle)
print('LIVE CHECK OK')
PY