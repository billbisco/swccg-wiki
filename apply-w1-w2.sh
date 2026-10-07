#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"
PAGES="$ROOT/pages"

python3 - <<'PY'
from pathlib import Path
p = Path("/etc/nginx/sites-enabled/wiki.swccg.com")
text = p.read_text()
block = """
    location = /wiki {
        return 301 /wiki/Main_Page;
    }
    location /wiki/ {
        rewrite ^/wiki/(.*)$ /index.php?title=$1 break;
        proxy_pass http://127.0.0.1:17003;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
"""
if "location /wiki/" not in text:
    needle = "    location / {"
    if needle not in text:
        raise SystemExit("no location / in wiki vhost")
    text = text.replace(needle, block + "\n" + needle, 1)
    p.write_text(text)
    print("added /wiki/ rewrite")
else:
    print("/wiki/ already present")
PY

if ! grep -q "extra-settings.php" "$ROOT/LocalSettings.php"; then
  echo 'require_once "$IP/extra-settings.php";' >> "$ROOT/LocalSettings.php"
fi

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d
nginx -t
systemctl reload nginx
docker exec swccg_wiki php maintenance/run.php update --quick

import_page() {
  local title="$1"
  local file="$2"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="WP-W1/W2 stub" "$title" < "$file"
}

import_page "Template:Card" "$PAGES/Template_Card.wiki"
import_page "Main Page" "$PAGES/Main_Page.wiki"
import_page "Sets" "$PAGES/Sets.wiki"
import_page "Rules" "$PAGES/Rules.wiki"
import_page "Players Committee" "$PAGES/Players_Committee.wiki"
import_page "GEMP" "$PAGES/GEMP.wiki"
import_page "Contribute" "$PAGES/Contribute.wiki"
import_page "Championships" "$PAGES/Championships.wiki"
import_page "How to play" "$PAGES/How_to_play.wiki"
import_page "Premiere" "$PAGES/Premiere.wiki"
import_page "Decipher vs Players Committee vs this site" "$PAGES/Decipher_vs_PC.wiki"
import_page "Card:1_109" "$PAGES/Card_1_109.wiki"
import_page "Sense (Premiere)" "$PAGES/Sense_Premiere_redirect.wiki"

# Hub stubs for nav
for t in Cards Formats Decks People History Designers "World Championship 1996"; do
  echo "Stub. Construction. See [[Main Page]]." | docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="nav stub" "$t"
done

echo "WP-W1/W2 pages imported."
curl -sI -m 10 "https://wiki.swccg.com/wiki/Main_Page" | head -12
curl -sI -m 10 "https://wiki.swccg.com/wiki/Card:1_109" | head -12
