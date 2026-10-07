#!/bin/bash
# Apply 2012 MPC leftover Xerox. ReviewTitles TSV titles only.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/y2012-mpc-xerox.tgz" ]; then
  tar xzf "$ROOT/y2012-mpc-xerox.tgz" -C "$ROOT"
fi
TSV="${1:-$ROOT/y2012-mpc-xerox-titles.tsv}"
SUMMARY="${2:-2012 MPC leftover Xerox}"

sed -i 's/\r$//' apply-tsv.sh "$TSV" || true

echo "== importImages =="
docker exec swccg_wiki bash -c 'rm -rf /tmp/y2012-mpc-xerox; mkdir -p /tmp/y2012-mpc-xerox'
if [ -d "$ROOT/y2012-mpc-media" ]; then
  for f in "$ROOT/y2012-mpc-media"/*; do
    [ -f "$f" ] || continue
    docker cp "$f" "swccg_wiki:/tmp/y2012-mpc-xerox/$(basename "$f")"
  done
fi
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2012 Match Play Championship leftover Xerox PDFs" \
  --extensions=pdf \
  /tmp/y2012-mpc-xerox > /tmp/y2012-mpc-xerox-import.log 2>&1 || true
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="2012 Match Play Championship leftover Xerox page scans" \
  --extensions=png \
  /tmp/y2012-mpc-xerox >> /tmp/y2012-mpc-xerox-import.log 2>&1 || true
grep -E 'Found|Added|Skipped|imported' /tmp/y2012-mpc-xerox-import.log | tail -20 || true
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

bash "$ROOT/apply-tsv.sh" "$TSV" "$SUMMARY"
echo "== extra purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
List of SWCCG tournaments
2012 Match Play Championship
Category:2012
Chris Erwin
Scott Lingrell
Brian Field
Matthew Harrison-Trainor
Kevin Shannon
Matt Sokol
Greg Shaw
Cole Lepine
Jonny Chu
Brad Eier
Aaron Nelson
Steve Baroni
Brian Terwilliger
Caleb Foth
Steve Harpster
Barry Alperstein
John Anderson
Casey Anis
Nicholas Amato
Clayton Atkin
Vikram Bali
Amar Banger
James Booker
Andrew Bollentino
Roy Bordier
Brian Brodsky
Ben Brummett
Carl Buck
Justin Carulli
Wayne Cullen
Dalton
Philippe Dubreuil
Pierre Dubreuil
Chuck Finley
Tony Garcia
Mike Gemme
Chris Gogolen
Matt Gombos
Thomas Graham
Brian Herold
Greg Hodur
Brian Hollingworth
Adam Howland
Hayes Hunter
Steve Skilton
PMT
Wojciech Jankowski
Matt Jourdan
Chris Kelly
Mike Kessling
Aaron Kinsey
Jared
Kyle Krueger
Josh Mack
Sam Marlow
Justin Montgomery
Tim Murray
Chris O'Hare
Joe Pinto
Mike Pistone
Mike Richards
Chris Schoenthal
Reid Smith
Pete Srodoski
Matt Thornton
Marty Terwilliger
Michael Thomas
Chris Terwilliger
John Veasey
Alex W
Chris Westergard
SAN
Chris Wirfs
Patrick Ziagos
light_frank
Legacy Open
EOF
echo APPLY-2012-MPC-XEROX-DONE
