#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
IMG_SRC="$ROOT/set-card-art/CC-D-projectivetelepathy.gif"
STAGE=$(mktemp -d)

echo "== restore Holotable PT Errata face (uncropped) =="
cp -f "$IMG_SRC" "$STAGE/CC-D-projectivetelepathy.gif"
docker exec swccg_wiki mkdir -p /tmp/pt-holo-restore
docker cp "$STAGE/." swccg_wiki:/tmp/pt-holo-restore/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Restore uncropped Holotable Errata face (keep rounded corners); sizing handled in Errata table markup" \
  --overwrite \
  /tmp/pt-holo-restore
docker exec -u root swccg_wiki bash -lc 'rm -rf /var/www/html/images/thumb/6/69/CC-D-projectivetelepathy.gif || true'
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
rm -rf "$STAGE"

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PY
}

echo "== edit Errata sizes: Original 316px, Errata 350px =="
strip_bom "$PAGES/Errata.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin \
  --summary="Restore Holotable PT face; size Original archive at 316px vs Errata 350px so faces match; keep cites on card name" \
  "Errata" < "$PAGES/Errata.wiki"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

for t in "Errata" "File:CC-D-projectivetelepathy.gif" "Projective Telepathy (Errata)"; do
  echo "purge $t"
  docker exec swccg_wiki php maintenance/run.php purgePage "$t" 2>/dev/null || true
done
echo "== DONE restore-holo-size =="
