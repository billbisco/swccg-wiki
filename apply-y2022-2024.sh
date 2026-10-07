#!/bin/bash
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"

if [ -d "$ROOT/y2022-2024-media" ]; then
  echo "== import GEMP media =="
  docker exec swccg_wiki mkdir -p /tmp/y2022-2024-media
  docker cp "$ROOT/y2022-2024-media/." swccg_wiki:/tmp/y2022-2024-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="GEMP import 2022-2024 tournament decks" \
    /tmp/y2022-2024-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

python3 /opt/swccg-wiki/_fix_tsv_cr.py "$ROOT/y2022-2024-titles.tsv" 2>/dev/null || python3 - "$ROOT/y2022-2024-titles.tsv" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
text = p.read_text(encoding="utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print("stripped cr", p)
PY

bash "$ROOT/apply-tsv.sh" "$ROOT/y2022-2024-titles.tsv" "2022-2024 tournament hubs, decks, and player stubs"
