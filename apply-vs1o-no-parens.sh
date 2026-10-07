#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
CONTAINER=swccg_wiki
STAGE=/tmp/vs1o-no-parens
mkdir -p "$STAGE"
rm -f "$STAGE"/*

# Capture the exact requested baseline before changing pages.
echo '== BEFORE =='
curl -sL -o /dev/null -w '%{http_code} %{url_effective}\n' 'https://wiki.swccg.com/wiki/Gold_1_(V)_(Virtual_Set_1_Original'
curl -sL -o /dev/null -w '%{http_code} %{url_effective}\n' 'https://wiki.swccg.com/wiki/Gold_1_(V)_(Virtual_Set_1_Original)'

cat > "$STAGE/moves.txt" <<'EOF'
Bo Shek (V) (Virtual Set 1 Original)|Bo Shek VS1 Original
Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)|Fusion Generator Supply Tanks VS1 Original
Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)|Fusion Generator Supply Tanks Dark VS1 Original
Gold 1 (V) (Virtual Set 1 Original)|Gold 1 VS1 Original
Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)|Han's Heavy Blaster Pistol VS1 Original
Luke Skywalker (V) (Virtual Set 1 Original)|Luke Skywalker VS1 Original
Sai'torr Kal Fas (V) (Virtual Set 1 Original)|Sai'torr Kal Fas VS1 Original
Blaster Rack (V) (Virtual Set 1 Original)|Blaster Rack VS1 Original
Assault Rifle (V) (Virtual Set 1 Original)|Assault Rifle VS1 Original
Black 2 (V) (Virtual Set 1 Original)|Black 2 VS1 Original
Darth Vader (V) (Virtual Set 1 Original)|Darth Vader VS1 Original
Prophetess (V) (Virtual Set 1 Original)|Prophetess VS1 Original
EOF

docker exec "$CONTAINER" mkdir -p "$STAGE"
docker cp "$STAGE/moves.txt" "$CONTAINER:$STAGE/moves.txt"
echo '== MOVE 12 VS1 Original pages =='
docker exec "$CONTAINER" php maintenance/run.php moveBatch --u=Admin --r='VS1 Original card title normalization (no parentheses)' "$STAGE/moves.txt"

# Build source files under the new titles and change card-nav prev/next links.
python3 - <<'PY'
from pathlib import Path
root = Path('/opt/swccg-wiki')
carddir = root / 'pages' / 'original-vs1'
items = [
 ('Bo_Shek_(V)_(Virtual_Set_1_Original).wiki', 'Bo_Shek_VS1_Original.wiki', 'Bo Shek (V) (Virtual Set 1 Original)', 'Bo Shek VS1 Original'),
 ('Fusion_Generator_Supply_Tanks_(V)_(Virtual_Set_1_Original).wiki', 'Fusion_Generator_Supply_Tanks_VS1_Original.wiki', 'Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)', 'Fusion Generator Supply Tanks VS1 Original'),
 ('Fusion_Generator_Supply_Tanks_(V)_(Dark)_(Virtual_Set_1_Original).wiki', 'Fusion_Generator_Supply_Tanks_Dark_VS1_Original.wiki', 'Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)', 'Fusion Generator Supply Tanks Dark VS1 Original'),
 ('Gold_1_(V)_(Virtual_Set_1_Original).wiki', 'Gold_1_VS1_Original.wiki', 'Gold 1 (V) (Virtual Set 1 Original)', 'Gold 1 VS1 Original'),
 ("Hans_Heavy_Blaster_Pistol_(V)_(Virtual_Set_1_Original).wiki", "Hans_Heavy_Blaster_Pistol_VS1_Original.wiki", "Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)", "Han's Heavy Blaster Pistol VS1 Original"),
 ('Luke_Skywalker_(V)_(Virtual_Set_1_Original).wiki', 'Luke_Skywalker_VS1_Original.wiki', 'Luke Skywalker (V) (Virtual Set 1 Original)', 'Luke Skywalker VS1 Original'),
 ('Saitorr_Kal_Fas_(V)_(Virtual_Set_1_Original).wiki', 'Saitorr_Kal_Fas_VS1_Original.wiki', "Sai'torr Kal Fas (V) (Virtual Set 1 Original)", "Sai'torr Kal Fas VS1 Original"),
 ('Blaster_Rack_(V)_(Virtual_Set_1_Original).wiki', 'Blaster_Rack_VS1_Original.wiki', 'Blaster Rack (V) (Virtual Set 1 Original)', 'Blaster Rack VS1 Original'),
 ('Assault_Rifle_(V)_(Virtual_Set_1_Original).wiki', 'Assault_Rifle_VS1_Original.wiki', 'Assault Rifle (V) (Virtual Set 1 Original)', 'Assault Rifle VS1 Original'),
 ('Black_2_(V)_(Virtual_Set_1_Original).wiki', 'Black_2_VS1_Original.wiki', 'Black 2 (V) (Virtual Set 1 Original)', 'Black 2 VS1 Original'),
 ('Darth_Vader_(V)_(Virtual_Set_1_Original).wiki', 'Darth_Vader_VS1_Original.wiki', 'Darth Vader (V) (Virtual Set 1 Original)', 'Darth Vader VS1 Original'),
 ('Prophetess_(V)_(Virtual_Set_1_Original).wiki', 'Prophetess_VS1_Original.wiki', 'Prophetess (V) (Virtual Set 1 Original)', 'Prophetess VS1 Original'),
]
repls = {old: new for _, _, old, new in items}
for oldfile, newfile, _, _ in items:
    oldpath = carddir / oldfile
    text = oldpath.read_text(encoding='utf-8')
    for old, new in repls.items():
        text = text.replace(old, new)
    (carddir / newfile).write_text(text, encoding='utf-8', newline='\n')
    oldpath.write_text(f'#REDIRECT [[{dict((o,n) for _,_,o,n in items)[_]}]]\n', encoding='utf-8', newline='\n') if False else None
# Keep the old source filenames as redirect sources too.
for oldfile, newfile, old, new in items:
    (carddir / oldfile).write_text(f'#REDIRECT [[{new}]]\n', encoding='utf-8', newline='\n')

hub = root / 'pages' / 'set-hubs' / 'Virtual_Set_1_(Original).wiki'
h = hub.read_text(encoding='utf-8')
for old, new in repls.items():
    h = h.replace(old, new)
hub.write_text(h, encoding='utf-8', newline='\n')
PY

edit() {
  local title="$1" file="$2" summary="$3"
  echo "edit: $title"
  docker exec -i "$CONTAINER" php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

# Re-save each moved page so Template:Card card-nav links use the normalized titles.
edit 'Bo Shek VS1 Original' "$ROOT/pages/original-vs1/Bo_Shek_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Fusion Generator Supply Tanks VS1 Original' "$ROOT/pages/original-vs1/Fusion_Generator_Supply_Tanks_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Fusion Generator Supply Tanks Dark VS1 Original' "$ROOT/pages/original-vs1/Fusion_Generator_Supply_Tanks_Dark_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Gold 1 VS1 Original' "$ROOT/pages/original-vs1/Gold_1_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit "Han's Heavy Blaster Pistol VS1 Original" "$ROOT/pages/original-vs1/Hans_Heavy_Blaster_Pistol_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Luke Skywalker VS1 Original' "$ROOT/pages/original-vs1/Luke_Skywalker_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit "Sai'torr Kal Fas VS1 Original" "$ROOT/pages/original-vs1/Saitorr_Kal_Fas_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Blaster Rack VS1 Original' "$ROOT/pages/original-vs1/Blaster_Rack_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Assault Rifle VS1 Original' "$ROOT/pages/original-vs1/Assault_Rifle_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Black 2 VS1 Original' "$ROOT/pages/original-vs1/Black_2_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Darth Vader VS1 Original' "$ROOT/pages/original-vs1/Darth_Vader_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'
edit 'Prophetess VS1 Original' "$ROOT/pages/original-vs1/Prophetess_VS1_Original.wiki" 'VS1 Original title normalization and card-nav links'

# The malformed URL is a separate title and must point to the normalized Gold page.
printf '%s\n' '#REDIRECT [[Gold 1 VS1 Original]]' > "$STAGE/Gold_1_broken.wiki"
edit 'Gold 1 (V) (Virtual Set 1 Original' "$STAGE/Gold_1_broken.wiki" 'Redirect malformed VS1 Original Gold 1 title'

# Update the hub targets while retaining the printed card labels.
edit 'Virtual Set 1 (Original)' "$ROOT/pages/set-hubs/Virtual_Set_1_(Original).wiki" 'VS1 Original hub links to normalized card titles'

# Review all changed pages and purge old/new titles, hub, and Template:Card.
echo '== FLAGGEDREVS =='
docker exec "$CONTAINER" php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1
cat > "$STAGE/purge.txt" <<'EOF'
Virtual Set 1 (Original)
Template:Card
Bo Shek VS1 Original
Fusion Generator Supply Tanks VS1 Original
Fusion Generator Supply Tanks Dark VS1 Original
Gold 1 VS1 Original
Han's Heavy Blaster Pistol VS1 Original
Luke Skywalker VS1 Original
Sai'torr Kal Fas VS1 Original
Blaster Rack VS1 Original
Assault Rifle VS1 Original
Black 2 VS1 Original
Darth Vader VS1 Original
Prophetess VS1 Original
Bo Shek (V) (Virtual Set 1 Original)
Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)
Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)
Gold 1 (V) (Virtual Set 1 Original)
Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)
Luke Skywalker (V) (Virtual Set 1 Original)
Sai'torr Kal Fas (V) (Virtual Set 1 Original)
Blaster Rack (V) (Virtual Set 1 Original)
Assault Rifle (V) (Virtual Set 1 Original)
Black 2 (V) (Virtual Set 1 Original)
Darth Vader (V) (Virtual Set 1 Original)
Prophetess (V) (Virtual Set 1 Original)
Gold 1 (V) (Virtual Set 1 Original
EOF
cat "$STAGE/purge.txt" | docker exec -i "$CONTAINER" php maintenance/run.php purgePage

echo '== AFTER =='
curl -sL -o /dev/null -w '%{http_code} %{url_effective}\n' 'https://wiki.swccg.com/wiki/Gold_1_(V)_(Virtual_Set_1_Original'
curl -sL -o /dev/null -w '%{http_code} %{url_effective}\n' 'https://wiki.swccg.com/wiki/Gold_1_(V)_(Virtual_Set_1_Original)'
curl -sL -o /dev/null -w '%{http_code} %{url_effective}\n' 'https://wiki.swccg.com/wiki/Gold_1_VS1_Original'
html=$(curl -sL 'https://wiki.swccg.com/wiki/Gold_1_VS1_Original')
if printf '%s' "$html" | grep -q 'card-portrait'; then echo 'Gold 1 VS1 Original: card-portrait=present'; else echo 'Gold 1 VS1 Original: card-portrait=MISSING'; exit 1; fi
printf '%s\n' 'VS1 NO-PAREN TITLES COMPLETE'

