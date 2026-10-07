#!/bin/bash
# Apply 2013 Alderaan Regionals hub and leftover typed lists.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-alderaan.tgz" ]; then
  tar xzf "$ROOT/y2013-alderaan.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-alderaan-titles.tsv}"
SUMMARY="${2:-2013 Alderaan Regionals hub and leftover typed dest}"

echo "== importImages =="
if [ -d "$ROOT/y2013-alderaan-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-alderaan-media
  docker cp "$ROOT/y2013-alderaan-media/." swccg_wiki:/tmp/y2013-alderaan-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Alderaan Regionals decklist scans" \
    --extensions=pdf \
    /tmp/y2013-alderaan-media || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Alderaan Regionals decklist page scans" \
    --extensions=png \
    /tmp/y2013-alderaan-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 Alderaan Regionals
Category:2013
Ryan Jellison
Clayton Atkin
Bren Derlin
Anthony Massung
Roy McCarthy
Chris Menzel
Matthew Harrison-Trainor
Ganden Yanaga
Legacy Open
EOF
echo APPLY-2013-ALDERAAN-DONE
