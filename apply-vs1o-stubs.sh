#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs1-original-stubs
STUBS=$ROOT/pages/vs1-original-stubs
REDIRS=$ROOT/pages/vs1-original-redirects
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs1o-stubs-import

strip() {
  python3 - <<PY
from pathlib import Path
p=Path("$1")
b=p.read_bytes()
if b.startswith(b"\xef\xbb\xbf"): b=b[3:]
p.write_bytes(b)
n=sum(1 for c in b.decode("utf-8") if ord(c)>127)
print(f"  {p.name} nonascii={n}")
assert n==0, p
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  strip "$file"
  echo "edit: $title"
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

echo "== importImages VS1O slip crops (NOT composites) =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS1O-*.png "$STAGE/"
# Safety: never stage composite filenames
rm -f "$STAGE"/*composite*
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs1o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs1o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 1 (Original) Legacy slip faces from VirtualCards1.pdf" \
  --overwrite \
  /tmp/vs1o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 1 (Original)" "$HUBS/Virtual_Set_1_(Original).wiki" "VS1 Original: locked stub names + Legacy slip-crop thumbs"

edit "Bo Shek (V) (Virtual Set 1)" "$STUBS/Bo_Shek_(V)_(Virtual_Set_1).wiki" "VS1O stub 01 locked name Legacy slip"
edit "Fusion Generator Supply Tanks (V) (Light) (Virtual Set 1)" "$STUBS/Fusion_Generator_Supply_Tanks_(V)_(Light)_(Virtual_Set_1).wiki" "VS1O stub 02 locked name Legacy slip"
edit "Gold 1 (V) (Virtual Set 1)" "$STUBS/Gold_1_(V)_(Virtual_Set_1).wiki" "VS1O stub 03 locked name Legacy slip"
edit "Han's Heavy Blaster Pistol (V) (Virtual Set 1)" "$STUBS/Hans_Heavy_Blaster_Pistol_(V)_(Virtual_Set_1).wiki" "VS1O stub 04 locked name Legacy slip"
edit "Luke Skywalker (V) (Virtual Set 1)" "$STUBS/Luke_Skywalker_(V)_(Virtual_Set_1).wiki" "VS1O stub 05 locked name Legacy slip"
edit "Sai'torr Kal Fas (V) (Virtual Set 1)" "$STUBS/Saitorr_Kal_Fas_(V)_(Virtual_Set_1).wiki" "VS1O stub 06 locked name Legacy slip"
edit "Assault Rifle (V) (Virtual Set 1)" "$STUBS/Assault_Rifle_(V)_(Virtual_Set_1).wiki" "VS1O stub 07 locked name Legacy slip"
edit "Black 2 (V) (Virtual Set 1)" "$STUBS/Black_2_(V)_(Virtual_Set_1).wiki" "VS1O stub 08 locked name Legacy slip"
edit "Blaster Rack (V) (Virtual Set 1)" "$STUBS/Blaster_Rack_(V)_(Virtual_Set_1).wiki" "VS1O stub 09 locked name Legacy slip"
edit "Darth Vader (V) (Virtual Set 1)" "$STUBS/Darth_Vader_(V)_(Virtual_Set_1).wiki" "VS1O stub 10 locked name Legacy slip"
edit "Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1)" "$STUBS/Fusion_Generator_Supply_Tanks_(V)_(Dark)_(Virtual_Set_1).wiki" "VS1O stub 11 locked name Legacy slip"
edit "Prophetess (V) (Virtual Set 1)" "$STUBS/Prophetess_(V)_(Virtual_Set_1).wiki" "VS1O stub 12 locked name Legacy slip"

echo "== redirects from old VS1 Original titles =="
edit "Bo Shek VS1 Original" "$REDIRS/redir-00-Bo_Shek_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Fusion Generator Supply Tanks VS1 Original" "$REDIRS/redir-01-Fusion_Generator_Supply_Tanks_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Gold 1 VS1 Original" "$REDIRS/redir-02-Gold_1_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Han's Heavy Blaster Pistol VS1 Original" "$REDIRS/redir-03-Han_s_Heavy_Blaster_Pistol_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Luke Skywalker VS1 Original" "$REDIRS/redir-04-Luke_Skywalker_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Sai'torr Kal Fas VS1 Original" "$REDIRS/redir-05-Sai_torr_Kal_Fas_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Assault Rifle VS1 Original" "$REDIRS/redir-06-Assault_Rifle_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Black 2 VS1 Original" "$REDIRS/redir-07-Black_2_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Blaster Rack VS1 Original" "$REDIRS/redir-08-Blaster_Rack_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Darth Vader VS1 Original" "$REDIRS/redir-09-Darth_Vader_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Fusion Generator Supply Tanks Dark VS1 Original" "$REDIRS/redir-10-Fusion_Generator_Supply_Tanks_Dark_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Prophetess VS1 Original" "$REDIRS/redir-11-Prophetess_VS1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Bo Shek (V) (Virtual Set 1 Original)" "$REDIRS/redir-12-Bo_Shek__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)" "$REDIRS/redir-13-Fusion_Generator_Supply_Tanks__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)" "$REDIRS/redir-14-Fusion_Generator_Supply_Tanks__V___Dark___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Gold 1 (V) (Virtual Set 1 Original)" "$REDIRS/redir-15-Gold_1__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Gold 1 (V) (Virtual Set 1 Original" "$REDIRS/redir-16-Gold_1__V___Virtual_Set_1_Original.wiki" "VS1O redirect to locked Original stub name"
edit "Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)" "$REDIRS/redir-17-Han_s_Heavy_Blaster_Pistol__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Luke Skywalker (V) (Virtual Set 1 Original)" "$REDIRS/redir-18-Luke_Skywalker__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Sai'torr Kal Fas (V) (Virtual Set 1 Original)" "$REDIRS/redir-19-Sai_torr_Kal_Fas__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Assault Rifle (V) (Virtual Set 1 Original)" "$REDIRS/redir-20-Assault_Rifle__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Black 2 (V) (Virtual Set 1 Original)" "$REDIRS/redir-21-Black_2__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Blaster Rack (V) (Virtual Set 1 Original)" "$REDIRS/redir-22-Blaster_Rack__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Darth Vader (V) (Virtual Set 1 Original)" "$REDIRS/redir-23-Darth_Vader__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"
edit "Prophetess (V) (Virtual Set 1 Original)" "$REDIRS/redir-24-Prophetess__V___Virtual_Set_1_Original_.wiki" "VS1O redirect to locked Original stub name"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -12

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 1 (Original)
Bo Shek (V) (Virtual Set 1)
Fusion Generator Supply Tanks (V) (Light) (Virtual Set 1)
Gold 1 (V) (Virtual Set 1)
Han's Heavy Blaster Pistol (V) (Virtual Set 1)
Luke Skywalker (V) (Virtual Set 1)
Sai'torr Kal Fas (V) (Virtual Set 1)
Assault Rifle (V) (Virtual Set 1)
Black 2 (V) (Virtual Set 1)
Blaster Rack (V) (Virtual Set 1)
Darth Vader (V) (Virtual Set 1)
Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1)
Prophetess (V) (Virtual Set 1)
Bo Shek VS1 Original
Fusion Generator Supply Tanks VS1 Original
Gold 1 VS1 Original
Han's Heavy Blaster Pistol VS1 Original
Luke Skywalker VS1 Original
Sai'torr Kal Fas VS1 Original
Assault Rifle VS1 Original
Black 2 VS1 Original
Blaster Rack VS1 Original
Darth Vader VS1 Original
Fusion Generator Supply Tanks Dark VS1 Original
Prophetess VS1 Original
Bo Shek (V) (Virtual Set 1 Original)
Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)
Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)
Gold 1 (V) (Virtual Set 1 Original)
Gold 1 (V) (Virtual Set 1 Original
Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)
Luke Skywalker (V) (Virtual Set 1 Original)
Sai'torr Kal Fas (V) (Virtual Set 1 Original)
Assault Rifle (V) (Virtual Set 1 Original)
Black 2 (V) (Virtual Set 1 Original)
Blaster Rack (V) (Virtual Set 1 Original)
Darth Vader (V) (Virtual Set 1 Original)
Prophetess (V) (Virtual Set 1 Original)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
slugs=['Bo_Shek_(V)_(Virtual_Set_1)', 'Fusion_Generator_Supply_Tanks_(V)_(Light)_(Virtual_Set_1)', 'Gold_1_(V)_(Virtual_Set_1)', "Han's_Heavy_Blaster_Pistol_(V)_(Virtual_Set_1)", 'Luke_Skywalker_(V)_(Virtual_Set_1)', "Sai'torr_Kal_Fas_(V)_(Virtual_Set_1)", 'Assault_Rifle_(V)_(Virtual_Set_1)', 'Black_2_(V)_(Virtual_Set_1)', 'Blaster_Rack_(V)_(Virtual_Set_1)', 'Darth_Vader_(V)_(Virtual_Set_1)', 'Fusion_Generator_Supply_Tanks_(V)_(Dark)_(Virtual_Set_1)', 'Prophetess_(V)_(Virtual_Set_1)']
pass_n=0; fail=[]
for slug in slugs:
  u="https://wiki.swccg.com/wiki/"+urllib.parse.quote(slug, safe="()_,!'?")
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    ok=(r.status==200)
  except Exception:
    ok=False
  print(("PASS" if ok else "FAIL"), u)
  if ok: pass_n+=1
  else: fail.append(u)
print("STUBS %d/12 PASS fail=%s" % (pass_n, fail))
u="https://wiki.swccg.com/wiki/Virtual_Set_1_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
for old in ["Bo_Shek_VS1_Original", "Bo_Shek_(V)_(Virtual_Set_1_Original)", "Fusion_Generator_Supply_Tanks_Dark_VS1_Original"]:
  u="https://wiki.swccg.com/wiki/"+old
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    print("REDIR", old, r.status, r.geturl())
  except Exception as e:
    print("REDIR FAIL", old, e)
print("VS1O STUBS APPLY OK")
PY

