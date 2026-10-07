#!/bin/bash
set -euo pipefail
HUBS=/opt/swccg-wiki/pages/set-hubs
strip() {
  python3 - <<PY
from pathlib import Path
p=Path("$1")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"): b=b[3:]
p.write_bytes(b)
n=sum(1 for c in b.decode("utf-8") if ord(c)>127)
print(f"{p.name} nonascii={n}")
assert n==0
PY
}
edit() {
  strip "$2"
  echo "edit $1"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$3" "$1" < "$2"
}
edit "Virtual Shields (Original)" "$HUBS/Virtual_Shields_(Original).wiki" "Sources: vshields.pdf + Shields-Decipher.pdf (RIII only); soften Premium label"
edit "Virtual Shields" "$HUBS/Virtual_Shields.wiki" "Sources: add vshields.pdf; soften Premium Set 1 wording"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -2
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Virtual Shields (Original)
Virtual Shields
Virtual Shields (Legacy)
EOF
python3 - <<'PY'
import subprocess
for title in ["Virtual Shields (Original)", "Virtual Shields"]:
  t=subprocess.check_output(["docker","exec","swccg_wiki","php","maintenance/run.php","getText",title],text=True,errors="replace")
  non=sum(1 for c in t if ord(c)>127)
  moj=any(x in t for x in ["â€","Â·","Ã¢"])
  print(f"{title}: nonascii={non} mojibake={moj}")
  for n in ["vshields.pdf","Shields-Decipher.pdf","soft/historical","NOT FOUND","DSShields.indd","Reflections III"]:
    if n in t: print(f"  HAS {n}")
print("SHIELDS SOURCES OK")
PY