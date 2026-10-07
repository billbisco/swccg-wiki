#!/bin/bash
# Apply 2013 Match Play Championship hub and Day 1 typed Banger/Brown lists.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2013-mpc.tgz" ]; then
  tar xzf "$ROOT/y2013-mpc.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2013-mpc-titles.tsv}"
SUMMARY="${2:-2013 Match Play Championship Day 1 Xerox Lepine Marlow}"

echo "== importImages =="
if [ -d "$ROOT/y2013-mpc-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2013-mpc-media
  docker cp "$ROOT/y2013-mpc-media/." swccg_wiki:/tmp/y2013-mpc-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Match Play Championship decklist scans" \
    --extensions=pdf \
    /tmp/y2013-mpc-media || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2013 Match Play Championship decklist page scans" \
    --extensions=png \
    /tmp/y2013-mpc-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2013 Match Play Championship
Category:2013
Amar Banger
Keith Brown
Barry Alperstein
Nicholas Amato
John Anderson
Steve Baroni
Casey Anis
Andrew Bollentino
Brian Brodsky
Carl Buck
Matt Carulli
Justin Carulli
Wayne Cullen
Jerry Heine
Brian Herold
Brian Hunter
Cole Lepine
Sam Marlow
Matthew Harrison-Trainor
Joe Pinto
Mike Tomashewski
Chris Westergard
Legacy Open
EOF
echo APPLY-2013-MPC-DONE
