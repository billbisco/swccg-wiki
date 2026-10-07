#!/bin/bash
# Rename leftover Objective / Starting Location (and any remaining
# Starting Location / Objective) to Starting Card on Category:Decklists.
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

docker cp "$ROOT/rename_start_card.php" swccg_wiki:/tmp/rename_start_card.php
docker exec swccg_wiki php /tmp/rename_start_card.php

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF'
2025 OCS Finals Patrick Johnson LS watch your step
2026 European Championship Top 8 Timo Dusel DS Thrawn
2025 Worlds Top 8 Greg Shaw DS SC
2025 Bespin Regionals Sean Miller DS walkers
2026 Retro GEMPC Kevin Bing LS Profit
2026 Retro GEMPC Patrick Johnson LS Hidden Base
2026 GEMPC Top 8 Pat Johnson DS TDIGWATT(V)
EOF

echo DONE rename-start-card
