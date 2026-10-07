#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
cd "$ROOT"

# Drop construction banner (idempotent)
python3 - <<'PY'
from pathlib import Path
p = Path("/opt/swccg-wiki/LocalSettings.php")
text = p.read_text()
start = text.find("$wgSiteNotice")
if start != -1:
    end = text.find("';", start)
    if end != -1:
        text = text[:start] + text[end+2:]
        p.write_text(text)
        print("removed wgSiteNotice")
    else:
        print("sitenotice end not found")
else:
    print("no sitenotice")
PY

# Landing: copy GEMP site assets onto swccg.com, then our rewritten index
mkdir -p /var/www/swccg.com
cp -a /var/www/swccggemp/assets /var/www/swccg.com/ 2>/dev/null || true
cp -a /var/www/swccggemp/styles.css /var/www/swccggemp/privacy.html /var/www/swccggemp/terms.html /var/www/swccggemp/robots.txt /var/www/swccg.com/ 2>/dev/null || true
cp "$ROOT/landing/index.html" /var/www/swccg.com/index.html

# play.swccg.com vhost
install -m 644 "$ROOT/nginx/play.swccg.com.conf" /etc/nginx/sites-available/play.swccg.com
ln -sfn /etc/nginx/sites-available/play.swccg.com /etc/nginx/sites-enabled/play.swccg.com

nginx -t
systemctl reload nginx

if [ ! -d /etc/letsencrypt/live/play.swccg.com ]; then
  certbot --nginx -d play.swccg.com --non-interactive --agree-tos --register-unsafely-without-email \
    || certbot --nginx -d play.swccg.com --non-interactive --agree-tos --keep-until-expiring || true
fi

# Redirect old GEMP hostnames (keep their certs for HTTPS 301)
python3 - <<'PY'
from pathlib import Path

def force_https_redirect(path, old_hosts, dest):
    p = Path(path)
    text = p.read_text()
    if f"return 301 https://{dest}" in text and "moved to swccg.com" in text:
        print("already redirected", path)
        return
    ssl_bits = ""
    for line in text.splitlines():
        if "ssl_certificate" in line or "ssl_certificate_key" in line or "options-ssl-nginx" in line or "ssl_dhparam" in line:
            ssl_bits += line + "\n"
    hosts = " ".join(old_hosts)
    conf = f"""# moved to swccg.com
server {{
    listen 80;
    listen [::]:80;
    server_name {hosts};
    return 301 https://{dest}$request_uri;
}}
server {{
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name {hosts};
{ssl_bits}    return 301 https://{dest}$request_uri;
}}
"""
    p.write_text(conf)
    print("rewrote redirect", path)

force_https_redirect("/etc/nginx/sites-enabled/play.swccggemp", ["play.swccggemp.com"], "play.swccg.com")
force_https_redirect("/etc/nginx/sites-enabled/swccggemp", ["swccggemp.com", "www.swccggemp.com"], "swccg.com")
PY

nginx -t
systemctl reload nginx

docker compose -f docker-compose.yml -f docker-compose.localsettings.yml up -d

import_page() {
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="logo/domain/main page" "$1" < "$2"
}
import_page "Main Page" "$ROOT/pages/Main_Page.wiki"
import_page "MediaWiki:Common.css" "$ROOT/pages/MediaWiki_Common.css.wiki"
import_page "MediaWiki:Sidebar" "$ROOT/pages/MediaWiki_Sidebar.wiki"
import_page "GEMP" "$ROOT/pages/GEMP.wiki"
import_page "How to play" "$ROOT/pages/How_to_play.wiki"

echo "https://play.swccg.com/" | docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="play.swccg.com" Play

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

echo "logo/domain applied"
curl -sI -m 10 https://play.swccg.com/ | head -12
curl -sI -m 10 https://swccg.com/ | head -8
curl -sI -m 10 https://wiki.swccg.com/resources/assets/swccg-wiki-logo.png | head -8
