#!/bin/bash
# Apply Team USA/Europe pages, 2023 retro Timo winner, and 2017–2018 tournament hubs.
set -euo pipefail
export LANG=C.UTF-8
ROOT=/opt/swccg-wiki
cd "$ROOT"
if [ -f "$ROOT/team-1718.tgz" ]; then
  tar xzf "$ROOT/team-1718.tgz" -C "$ROOT"
fi
bash "$ROOT/apply-tsv.sh" "$ROOT/team-1718-titles.tsv" "Team USA/Europe, 2023 retro Timo winner, 2017-2018 tournament hubs"
echo "== extra hub purge =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Team USA
Team Europe
Team North America
Category:Teams
Category:2017
Category:2018
2019 Outrider Cup
2021 Outrider Cup
2023 Outrider Cup III
2026 Outrider Cup IV
2023 Online Retro Event
2018 World Championship
2018 European Championship
2018 U.S. National Championship
2018 Endor Grand Prix
2018 European Match Play Championship
2018 Match Play Championship
2018 Online Championship Series
2017 Texas Mini Worlds
2017 European Championship
2017 World Championship
2017 U.S. National Championship
2017 Endor Grand Prix
2017 Match Play Championship
List of SWCCG tournaments
European Championships
Timo Dusel
Joe Olson
Bastian Winkelhaus
Justin Desai
Emil Wallin
Jonny Chu
Phil Aasen
Chris Kelly
Tom Haid
Lenny Rubin
Kevin Jaap
Reid Smith
Steve Baroni
Tom Kelly
EOF
echo APPLY-TEAM-1718-DONE
