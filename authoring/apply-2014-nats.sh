#!/bin/bash
# Apply 2014 US Nationals hub and Day 2 typed lists.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2014-nats.tgz" ]; then
  tar xzf "$ROOT/y2014-nats.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2014-nats-titles.tsv}"
SUMMARY="${2:-2014 US Nationals Day 2 typed lists}"

echo "== importImages =="
if [ -d "$ROOT/y2014-nats-media" ]; then
  docker exec swccg_wiki mkdir -p /tmp/y2014-nats-media
  docker cp "$ROOT/y2014-nats-media/." swccg_wiki:/tmp/y2014-nats-media/
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2014 US Nationals decklist scans" \
    --extensions=pdf \
    /tmp/y2014-nats-media || true
  docker exec swccg_wiki php maintenance/run.php importImages \
    --user=Admin \
    --comment="2014 US Nationals decklist page scans" \
    --extensions=png \
    /tmp/y2014-nats-media || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
fi

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== ReviewTitles force stable =="
cut -f1 "$TSV" | docker exec -i swccg_wiki php /var/www/html/maintenance/ReviewTitles.php || true
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2014 US Nationals
Category:2014
Matthew Harrison-Trainor
Matt Sokol
Matt Carulli
Chris Terwilliger
Mike Tomashewski
Brad Eier
Bill Kafer
Legacy Open
EOF
echo APPLY-2014-NATS-DONE
