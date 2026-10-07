#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

echo "== importImages remaster =="
docker exec swccg_wiki mkdir -p /tmp/rg-r
docker cp "$ROOT/encyclopedia/upload/." swccg_wiki:/tmp/rg-r/
# only RG-R-*
docker exec swccg_wiki bash -lc 'mkdir -p /tmp/rg-r-only; cp /tmp/rg-r/RG-R-* /tmp/rg-r-only/ 2>/dev/null || true'
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Reflections Gold remastered reconstruction (Google Doc; not Decipher print)" \
  /tmp/rg-r-only || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

echo "== edit hub =="
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Remastered column from Reflections Gold Remastered Google Doc" \
  "Reflections Gold" < "$ROOT/pages/Reflections_Gold.wiki"

python3 - <<'PY'
from pathlib import Path
rows=[]
for p in sorted(Path("/opt/swccg-wiki/pages").glob("File_RG-R-*")):
    # File_RG-R-2-1B_jpg.wiki -> File:RG-R-2-1B.jpg
    name=p.stem  # File_RG-R-2-1B_jpg
    rest=name[len("File_"):]
    if rest.endswith("_jpg"):
        title="File:"+rest[:-4]+".jpg"
    elif rest.endswith("_png"):
        title="File:"+rest[:-4]+".png"
    else:
        continue
    rows.append((title, str(p)))
Path("/opt/swccg-wiki/rg-r-files.tsv").write_text(
    "\n".join(f"{t}\t{r}" for t,r in rows)+"\n", encoding="utf-8"
)
print("file pages", len(rows))
PY

n=0
while IFS=$'\t' read -r title rel; do
  [ -z "${title:-}" ] && continue
  n=$((n+1))
  echo "== edit $n $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
    --summary="Reflections Gold remastered file description" \
    "$title" < "$rel"
done < "$ROOT/rg-r-files.tsv"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
docker exec swccg_wiki php maintenance/run.php purgePage "Reflections Gold" || true
echo DONE refgold-remaster n=$n
