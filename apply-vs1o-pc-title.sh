#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
STAGE=/tmp/vs1o-title
mkdir -p "$STAGE"
cp -f "$ROOT/images/original-vs1/Set-VS1O-title.png" "$STAGE/"
# try overwrite first
docker exec swccg_wiki mkdir -p /tmp/vs1o-title
docker cp "$STAGE/." swccg_wiki:/tmp/vs1o-title/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="VS1 Original hub title: PC symbol from GPN rulesupdate.pdf + Virtual Set 1 text (placeholder, not pack art)" \
  --overwrite \
  /tmp/vs1o-title
rc=$?
set -e
if [ "$rc" -ne 0 ]; then
  echo "overwrite failed; delete File page and retry"
  # delete wiki file page
  echo "y" | docker exec -i swccg_wiki php maintenance/run.php deleteBatch --user=Admin <<'EOF' || true
File:Set-VS1O-title.png
EOF
  # also try delete.php
  docker exec swccg_wiki php maintenance/run.php delete --user=Admin "File:Set-VS1O-title.png" --reason="replace placeholder title" 2>/dev/null || \
  docker exec swccg_wiki php maintenance/run.php deleteBatch --u Admin /dev/stdin <<'EOF' || true
File:Set-VS1O-title.png
EOF
  # find and remove hashed files
  docker exec -u root swccg_wiki bash -lc 'find /var/www/html/images -iname "*Set-VS1O-title*" -print -delete' || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="VS1 Original hub title: PC symbol from GPN rulesupdate.pdf + Virtual Set 1 text (placeholder, not pack art)" \
    /tmp/vs1o-title
fi
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

python3 - <<'PY'
from pathlib import Path
p=Path("/opt/swccg-wiki/pages/set-hubs/Virtual_Set_1_(Original).wiki")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"): b=b[3:]
p.write_bytes(b)
assert sum(1 for c in b.decode("utf-8") if ord(c)>127)==0
PY
echo "edit hub"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="hub title: PC symbol placeholder from GPN rulesupdate.pdf; cite IA" \
  "Virtual Set 1 (Original)" < /opt/swccg-wiki/pages/set-hubs/Virtual_Set_1_\(Original\).wiki

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -2
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Virtual Set 1 (Original)
Main Page
File:Set-VS1O-title.png
EOF
# bump cache? purge should be enough for file
python3 - <<'PY'
import subprocess, urllib.request
t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText","Virtual Set 1 (Original)"],text=True)
print("hub nonascii", sum(1 for c in t if ord(c)>127), "rulesupdate", "rulesupdate.pdf" in t, "creative" in t.lower())
for u in [
 "https://wiki.swccg.com/wiki/File:Set-VS1O-title.png",
 "https://wiki.swccg.com/wiki/Special:FilePath/Set-VS1O-title.png",
 "https://wiki.swccg.com/wiki/Virtual_Set_1_(Original)",
]:
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method='HEAD'), timeout=20)
    print(u, r.status, r.headers.get('Content-Length'), r.headers.get('Content-Type','')[:40])
  except Exception as e:
    print(u, e)
print("DONE")
PY