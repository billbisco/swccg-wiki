#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

python3 - <<'PY'
from pathlib import Path
pages = Path("pages")
rows = []
# fan / people
for title, rel in [
    ("Red 32's Star Wars CCG Site", "pages/Red_32_Star_Wars_CCG_Site.wiki"),
    ('Carl "Mike" Hardy', "pages/people/Carl_Mike_Hardy.wiki"),
    ("DeckTech", "pages/DeckTech.wiki"),
    ("Corellian Engineering Corporation (fan site)", "pages/Corellian_Engineering_Corporation_(fan_site).wiki"),
    ("2026 Tenth Annual GEMPC", "pages/2026_Tenth_Annual_GEMPC.wiki"),
]:
    rows.append((title, rel))
for p in sorted(pages.glob("2026_GEMPC*.wiki")):
    title = p.stem.replace("_", " ")
    rows.append((title, str(p).replace("\\", "/")))
Path("gempc-fan-titles.tsv").write_text(
    "\n".join(f"{t}\t{r}" for t, r in rows) + "\n", encoding="utf-8"
)
print("titles", len(rows))
PY

echo "== importImages GEMP txt =="
docker exec swccg_wiki mkdir -p /tmp/gempc-2026-media
docker cp "$ROOT/gempc-2026-media/." swccg_wiki:/tmp/gempc-2026-media/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="GEMP import from 2026 Gempc.zip / Top 8 (forum t=86845)" \
  /tmp/gempc-2026-media || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

n=0
while IFS=$'\t' read -r title rel; do
  [ -z "${title:-}" ] && continue
  f="$ROOT/$rel"
  if [ ! -f "$f" ]; then echo "MISSING $f" >&2; exit 1; fi
  n=$((n+1))
  echo "== edit $n $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="2026 Tenth Annual GEMPC decks + Red 32 fan site" "$title" < "$f"
done < "$ROOT/gempc-fan-titles.tsv"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec swccg_wiki php maintenance/run.php purgePage "2026 Tenth Annual GEMPC" || true
docker exec swccg_wiki php maintenance/run.php purgePage "Red 32's Star Wars CCG Site" || true
echo "DONE gempc-fan n=$n"
