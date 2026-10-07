#!/bin/bash
set -u
cd /opt/swccg-wiki
bash /opt/swccg-wiki/fetch-ds2-starters.sh
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="stats one per row" "Template:Card" < /opt/swccg-wiki/pages/Template_Card.wiki
python3 - <<'PY'
import importlib.util
spec = importlib.util.spec_from_file_location("isp", "/opt/swccg-wiki/import_set_pages.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.import_page("Death Star II Starter Decks", mod.PAGES["Death Star II Starter Decks"])
PY
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf 'Template:Card\n2X-3KPR (Tooex)\nDeath Star II Starter Decks\nMain Page\nFile:Set-ds2-starter-ls.jpg\nFile:Set-ds2-starter-ds.jpg\n' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo stats-ds2 done
