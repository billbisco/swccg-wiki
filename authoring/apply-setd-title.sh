#!/bin/bash
# Apply Virtual Set D official cardlist title GIF (hub wikitext jpg->gif).
# Does NOT touch Legacy Block Set-VB*/Set-VSh. Does NOT invent art.
set -euo pipefail
ROOT=/opt/swccg-wiki
HUB="$ROOT/pages/set-hubs/Virtual_Set_D.wiki"
STAGE=/tmp/set-vd-title-gif

mkdir -p "$STAGE"
if [ -f "$ROOT/images/set-titles/Set-VD-title.gif" ]; then
  cp -f "$ROOT/images/set-titles/Set-VD-title.gif" "$STAGE/Set-VD-title.gif"
elif [ -f "$ROOT/set-art-virtual/Set-VD-title.gif" ]; then
  cp -f "$ROOT/set-art-virtual/Set-VD-title.gif" "$STAGE/Set-VD-title.gif"
else
  echo "ERROR: missing Set-VD-title.gif master" >&2
  exit 1
fi
ls -la "$STAGE"

docker exec swccg_wiki mkdir -p /tmp/set-vd-title-gif
docker cp "$STAGE/." swccg_wiki:/tmp/set-vd-title-gif/
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set D title: official PC cardlist SETD_title.gif (match V1/V2)" \
  --overwrite \
  /tmp/set-vd-title-gif

docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true
docker exec swccg_wiki php maintenance/run.php refreshImageMetadata --force || true

if [ ! -s "$HUB" ]; then
  echo "ERROR: missing $HUB" >&2
  exit 1
fi
docker exec -i swccg_wiki php maintenance/run.php edit \
  --user=Admin \
  --summary="Virtual Set D infobox: Set-VD-title.gif (official cardlist banner, match V1/V2)" \
  "Virtual Set D" < "$HUB"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin || true

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOF' || true
Virtual Set D
Main Page
File:Set-VD-title.gif
File:Set-VD-title.jpg
EOF

echo "==== verify hub raw ===="
docker exec swccg_wiki php maintenance/run.php getText "Virtual Set D" | head -10
echo "==== verify file on disk ===="
docker exec swccg_wiki bash -c "find /var/www/html/images -name 'Set-VD-title.gif' -printf '%p %s\n' 2>/dev/null | head -5"
echo "Set D title GIF apply done"