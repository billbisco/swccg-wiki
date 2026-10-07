#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

docker exec swccg_wiki mkdir -p /tmp/gpn-wars
docker cp "$ROOT/gpn-wars-media/." swccg_wiki:/tmp/gpn-wars/ || true
docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="Game Players Network and WARS TCG history" /tmp/gpn-wars || true

python3 - <<'PY'
from pathlib import Path
p=Path("pages")
rows=[
    ("Game Players Network", "pages/Game_Players_Network.wiki"),
    ("Game Player's Network", "pages/Game_Player's_Network.wiki"),
    ("WARS TCG", "pages/WARS_TCG.wiki"),
    ("WARS Trading Card Game", "pages/WARS_Trading_Card_Game.wiki"),
    ("Wars TCG", "pages/wars-tcg-redirect.wiki"),
    ("History of the Players Committee", "pages/History_of_the_Players_Committee.wiki"),
    ("Players Committee", "pages/Players_Committee.wiki"),
]
Path("gpn-wars-titles.tsv").write_text("\n".join(f"{t}\t{r}" for t,r in rows)+"\n", encoding="utf-8")
print("titles", len(rows))
PY

n=0
while IFS=$'\t' read -r title rel; do
  [ -z "${title:-}" ] && continue
  f="$ROOT/$rel"
  [ -f "$f" ] || continue
  n=$((n+1))
  echo "== edit $n $title =="
  python3 - "$f" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1])
raw=p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw=raw[3:]
p.write_text(raw.decode("utf-8").replace("\r\n","\n").replace("\r","\n"), encoding="utf-8", newline="\n")
PY
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Game Players Network and WARS TCG history" "$title" < "$f"
done < "$ROOT/gpn-wars-titles.tsv"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
Game Players Network
WARS TCG
History of the Players Committee
Players Committee
EOF
echo DONE gpn-wars n=$n
