#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki

install -m 644 "$ROOT/nginx/test.swccg.com.conf" /etc/nginx/sites-available/test.swccg.com
ln -sfn /etc/nginx/sites-available/test.swccg.com /etc/nginx/sites-enabled/test.swccg.com
nginx -t
systemctl reload nginx

if [ ! -d /etc/letsencrypt/live/test.swccg.com ]; then
  certbot --nginx -d test.swccg.com --non-interactive --agree-tos --register-unsafely-without-email \
    || certbot --nginx -d test.swccg.com --non-interactive --agree-tos --keep-until-expiring || true
fi

python3 - <<'PY'
from pathlib import Path
p = Path("/etc/nginx/sites-enabled/test.swccggemp")
text = p.read_text()
if "return 301 https://test.swccg.com" in text and "moved to test.swccg.com" in text:
    print("already redirected")
else:
    ssl_bits = ""
    for line in text.splitlines():
        if "ssl_certificate" in line or "ssl_certificate_key" in line or "options-ssl-nginx" in line or "ssl_dhparam" in line:
            ssl_bits += line + "\n"
    p.write_text(f"""# moved to test.swccg.com
server {{
    listen 80;
    listen [::]:80;
    server_name test.swccggemp.com;
    return 301 https://test.swccg.com$request_uri;
}}
server {{
    listen 443 ssl;
    listen [::]:443 ssl;
    server_name test.swccggemp.com;
{ssl_bits}    return 301 https://test.swccg.com$request_uri;
}}
""")
    print("rewrote test.swccggemp redirect")
PY

nginx -t
systemctl reload nginx
echo "test.swccg.com ready"
curl -sI -m 10 https://test.swccg.com/ | head -10
curl -sI -m 10 https://test.swccggemp.com/ | head -8
