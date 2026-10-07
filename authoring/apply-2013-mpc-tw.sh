#!/bin/bash
# Apply 2013 MPC Day 1 Mike Tomashewski + Chris Westergard Xerox leftover.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-mpc-tw.tgz" ]; then
  tar xzf "$ROOT/y2013-mpc-tw.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-mpc-tw-titles.tsv}"
SUMMARY="${2:-2013 MPC Day 1 Tomashewski Westergard Xerox}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
if [ -d "$ROOT/y2013-mpc-tw-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-mpc-tw-media
  docker cp "$ROOT/y2013-mpc-tw-media/." swccg_wiki:/tmp/y2013-mpc-tw-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Match Play Championship Tomashewski Westergard scans" \
    --extensions=png \
    /tmp/y2013-mpc-tw-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
2013 Match Play Championship
2013 Match Play Championship Day 1 Mike Tomashewski LS Yavin 4: Massassi Throne Room
2013 Match Play Championship Day 1 Mike Tomashewski DS Invasion
2013 Match Play Championship Day 1 Chris Westergard LS Watch Your Step
2013 Match Play Championship Day 1 Chris Westergard DS Wookiee Slaving Operation
Mike Tomashewski
Chris Westergard
EOF
echo APPLY-2013-MPC-TW-DONE
