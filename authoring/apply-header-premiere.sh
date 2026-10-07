#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d

edit() {
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="header/premiere thumbs" "$1" < "$2"
}

edit "MediaWiki:Common.css" "$PAGES/MediaWiki_Common.css.wiki"
edit "MediaWiki:Common.js" "$PAGES/MediaWiki_Common.js.wiki"
edit "Main Page" "$PAGES/Main_Page.wiki"

bash "$ROOT/fetch-wookiee-sets.sh"

python3 "$ROOT/build_premiere_thumbs.py"
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
print("premiere page chars", len(article))
PY

PREF=/opt/swccg-wiki/premiere-card-art/prefixed
if [ -d "$PREF" ]; then
  docker cp "$PREF" swccg_wiki:/tmp/premiere-gifs
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="Premiere card images from PC cardlists" --overwrite /tmp/premiere-gifs \
    || docker exec swccg_wiki php maintenance/importImages.php --user=Admin --overwrite /tmp/premiere-gifs || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images
fi

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="Premiere thumbs" "Premiere Limited" < /tmp/premiere-limited.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf 'Main Page\nPremiere Limited\n' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo "header+premiere done"
