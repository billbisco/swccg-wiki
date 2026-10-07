#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="chrome zoom popup" "MediaWiki:Common.css" < "$ROOT/pages/MediaWiki_Common.css.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="chrome zoom popup" "MediaWiki:Common.js" < "$ROOT/pages/MediaWiki_Common.js.wiki"
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
print("chars", len(article), "200px", article.count("|200px|"))
PY
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="200px thumbs" "Premiere Limited" < /tmp/premiere-limited.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf 'Main Page\nPremiere Limited\nMediaWiki:Common.js\nMediaWiki:Common.css\n' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo zoom-fix done
