#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

# Owner's Premiere Limited booster box
python3 - <<'PY'
from PIL import Image
from pathlib import Path
src = Path("/opt/swccg-wiki/Premiere-Limited-Booster-Box.png")
dst = Path("/opt/swccg-wiki/set-art-boxes/Set-premiere-limited.jpg")
dst.parent.mkdir(parents=True, exist_ok=True)
if src.exists():
    Image.open(src).convert("RGB").save(dst, "JPEG", quality=90)
    print("converted booster box", dst.stat().st_size)
else:
    print("no owner booster box at", src)
PY

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d
if [ -s "$ROOT/set-art-boxes/Set-premiere-limited.jpg" ]; then
  DST=$(docker exec swccg_wiki find /var/www/html/images -name Set-premiere-limited.jpg | head -1)
  echo "premiere dst $DST"
  if [ -n "$DST" ]; then
    docker cp "$ROOT/set-art-boxes/Set-premiere-limited.jpg" "swccg_wiki:$DST"
    docker exec -u root swccg_wiki chown www-data:www-data "$DST"
    docker exec swccg_wiki bash -c "rm -rf /var/www/html/images/thumb/3/3e/Set-premiere-limited.jpg /var/www/html/images/thumb/*/Set-premiere-limited.jpg" || true
  fi
  docker cp "$ROOT/set-art-boxes/Set-premiere-limited.jpg" swccg_wiki:/tmp/Set-premiere-limited.jpg
  docker exec swccg_wiki mkdir -p /tmp/one-box
  docker exec swccg_wiki cp /tmp/Set-premiere-limited.jpg /tmp/one-box/Set-premiere-limited.jpg
  docker exec swccg_wiki php maintenance/run.php importImages --user=Admin --comment="owner Premiere Limited booster box" --overwrite /tmp/one-box || true
  docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images
fi

docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="logo/search/main h1" "MediaWiki:Common.css" < "$PAGES/MediaWiki_Common.css.wiki"
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="logo stays in sidebar" "MediaWiki:Common.js" < "$PAGES/MediaWiki_Common.js.wiki"

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
docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="mouse droid text" "Premiere Limited" < /tmp/premiere-limited.wiki
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true
printf 'Main Page\nPremiere Limited\n' | docker exec -i swccg_wiki php maintenance/run.php purgePage || true
echo chrome-fix done
