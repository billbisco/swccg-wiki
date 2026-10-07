#!/bin/bash
set -u
cd /opt/swccg-wiki
bash /opt/swccg-wiki/scrape-wookiee-sets.sh
python3 /opt/swccg-wiki/import_set_pages.py
python3 - <<'PY'
from pathlib import Path
import importlib.util
spec = importlib.util.spec_from_file_location("isp", "/opt/swccg-wiki/import_set_pages.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
article = mod.PAGES["Premiere Limited"]
thumbs = Path("/opt/swccg-wiki/premiere-thumbs.wiki").read_text(encoding="utf-8")
if "[[Category:Decipher sets]]" in article:
    article = article.replace("[[Category:Decipher sets]]", thumbs + "\n[[Category:Decipher sets]]\n")
else:
    article += "\n" + thumbs
Path("/tmp/premiere-limited.wiki").write_text(article, encoding="utf-8")
print("premiere chars", len(article))
PY
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="decipher archives + thumbs" "Premiere Limited" < /tmp/premiere-limited.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf 'Main Page\nPremiere Limited\nJedi Pack\n' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo set-sources done
