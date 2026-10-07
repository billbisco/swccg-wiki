#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
UP=/tmp/ar20-upload

echo "== importImages (PDF + diagrams) =="
docker exec swccg_wiki rm -rf /tmp/ar20-upload || true
docker cp "$UP" swccg_wiki:/tmp/ar20-upload
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Legacy Virtual AR 2.0 PDF + diagrams" \
  --overwrite \
  /tmp/ar20-upload \
  || docker exec swccg_wiki php maintenance/importImages.php --user=Admin --overwrite /tmp/ar20-upload || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit() {
  local title="$1"
  local file="$2"
  local summary="$3"
  echo "edit $title"
  # strip UTF-8 BOM if present
  python3 - <<PY
from pathlib import Path
p = Path("$file")
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
p.write_bytes(raw)
PY
  docker exec -i swccg_wiki php maintenance/run.php edit \
    --user=Admin \
    --summary="$summary" \
    "$title" < "$file"
}

edit "Players Committee Advanced Rulebook 2.0" \
  "$PAGES/Players_Committee_Advanced_Rulebook_2.0.wiki" \
  "Legacy Virtual-era PC Advanced Rulebook 2.0 transcription"

edit "Legacy Virtual Advanced Rulebook" \
  "$PAGES/Legacy_Virtual_Advanced_Rulebook.wiki" \
  "redirect to AR 2.0"

edit "Rulebooks" \
  "$PAGES/Rulebooks.wiki" \
  "chronological bands: Decipher / Legacy Virtual / Virtual current"

edit "Mission" \
  "$PAGES/concepts/Mission.wiki" \
  "Mission rules from Legacy Virtual AR 2.0 (cited)"

echo "== FlaggedRevs =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "== purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Players Committee Advanced Rulebook 2.0
Legacy Virtual Advanced Rulebook
Players Committee Advanced Rulebook
Rulebooks
Mission
File:AR-version-2-0-final.pdf
File:AR20-cover.png
File:AR20-force-circulation.png
Main Page
EOF

echo "== verify =="
docker exec swccg_wiki php maintenance/run.php getText "Players Committee Advanced Rulebook 2.0" | head -15
echo "----"
docker exec swccg_wiki php maintenance/run.php getText "Mission" | head -20
echo "----"
docker exec swccg_wiki php maintenance/run.php getText "Rulebooks" | head -25
echo "---- files ----"
docker exec swccg_wiki bash -c "find /var/www/html/images -name 'AR-version-2-0-final.pdf' -o -name 'AR20-cover.png' -o -name 'AR20-force-circulation.png' 2>/dev/null | head -20"
echo "AR20 apply done"