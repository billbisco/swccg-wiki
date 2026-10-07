#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -d "$ROOT/2025-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/vm-media
  docker cp "$ROOT/2025-media/." swccg_wiki:/tmp/vm-media/ || true
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="2025 Vegas/Morristown GEMP" /tmp/vm-media || true
fi
python3 - <<'PY'
from pathlib import Path
rows = [
    ("2025 Online Championship Series Playoffs", "pages/2025_Online_Championship_Series_Playoffs.wiki"),
    ("2025 European Championship", "pages/2025_European_Championship.wiki"),
    ("2025 Las Vegas Grand Prix", "pages/2025_Las_Vegas_Grand_Prix.wiki"),
    ("2025 Morristown Melee", "pages/2025_Morristown_Melee.wiki"),
    ("2026 Jawa Cup", "pages/2026_Jawa_Cup.wiki"),
    ("2026 Retro U.S. Nationals", "pages/2026_Retro_U.S._Nationals.wiki"),
    ("2025 Regional Championships", "pages/2025_Regional_Championships.wiki"),
    ("2026 Regional Championships", "pages/2026_Regional_Championships.wiki"),
]
pages = Path("pages")
for pat in (
    "2025_European_Championship*.wiki",
    "2025_OCS*.wiki",
    "2025_LVGP*.wiki",
    "2025_Morristown*.wiki",
    "2026_Jawa_Cup*.wiki",
    "2026_Retro_U.S._Nationals*.wiki",
    "2025_*Regionals*.wiki",
    "2026_*Regionals*.wiki",
):
    for p in sorted(pages.glob(pat)):
        if p.name in {
            "2025_European_Championship.wiki",
            "2026_Jawa_Cup.wiki",
            "2026_Retro_U.S._Nationals.wiki",
        }:
            continue
        rows.append((p.stem.replace("_", " "), str(p).replace("\\", "/")))
seen = {}
for t, r in rows:
    seen[t] = r
Path("missing-decks-titles.tsv").write_text("\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8")
print("titles", len(seen))
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
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Add missing 2025/2026 tournament decklists" "$title" < "$f"
done < "$ROOT/missing-decks-titles.tsv"
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
2025 Online Championship Series Playoffs
2025 European Championship
2025 Las Vegas Grand Prix
2025 Morristown Melee
2026 Jawa Cup
2026 Retro U.S. Nationals
2025 Regional Championships
2026 Regional Championships
EOF
echo DONE missing n=$n
