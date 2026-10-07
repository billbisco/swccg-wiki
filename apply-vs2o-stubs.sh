#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs2-original
STUBS=$ROOT/pages/vs2-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs2o-stubs-import

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

echo "== importImages VS2O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS2O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs2o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs2o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 2 (Original) Remaster slip faces from VirtualCards2.pdf" \
  --overwrite \
  /tmp/vs2o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 2 (Original)" "$HUBS/Virtual_Set_2_(Original).wiki" "VS2 Original: link all 50 Remaster slip stubs"

edit 'Affect Mind (V) (Virtual Set 2)' "$STUBS/Affect_Mind_(V)_(Virtual_Set_2).wiki" "VS2O stub 01"
edit 'Biggs Darklighter (V) (Virtual Set 2)' "$STUBS/Biggs_Darklighter_(V)_(Virtual_Set_2).wiki" "VS2O stub 02"
edit 'C-3PO (See-Threepio) (V) (Virtual Set 2)' "$STUBS/C3PO_(SeeThreepio)_(V)_(Virtual_Set_2).wiki" "VS2O stub 03"
edit 'Cantina Brawl (V) (Virtual Set 2)' "$STUBS/Cantina_Brawl_(V)_(Virtual_Set_2).wiki" "VS2O stub 04"
edit 'Demotion (V) (Virtual Set 2)' "$STUBS/Demotion_(V)_(Virtual_Set_2).wiki" "VS2O stub 05"
edit 'Escape Pod (V) (Virtual Set 2)' "$STUBS/Escape_Pod_(V)_(Virtual_Set_2).wiki" "VS2O stub 06"
edit 'General Dodonna (V) (Virtual Set 2)' "$STUBS/General_Dodonna_(V)_(Virtual_Set_2).wiki" "VS2O stub 07"
edit 'Han'\''s Back (V) (Virtual Set 2)' "$STUBS/Hans_Back_(V)_(Virtual_Set_2).wiki" "VS2O stub 08"
edit 'Han'\''s Dice (V) (Virtual Set 2)' "$STUBS/Hans_Dice_(V)_(Virtual_Set_2).wiki" "VS2O stub 09"
edit 'Into The Garbage Chute, Flyboy (V) (Virtual Set 2)' "$STUBS/Into_The_Garbage_Chute_Flyboy_(V)_(Virtual_Set_2).wiki" "VS2O stub 10"
edit 'Jawa Siesta (V) (Virtual Set 2)' "$STUBS/Jawa_Siesta_(V)_(Virtual_Set_2).wiki" "VS2O stub 11"
edit 'K'\''lor'\''slug (V) (Virtual Set 2)' "$STUBS/Klorslug_(V)_(Virtual_Set_2).wiki" "VS2O stub 12"
edit 'Leia'\''s Back (V) (Virtual Set 2)' "$STUBS/Leias_Back_(V)_(Virtual_Set_2).wiki" "VS2O stub 13"
edit 'Luke'\''s Back (V) (Virtual Set 2)' "$STUBS/Lukes_Back_(V)_(Virtual_Set_2).wiki" "VS2O stub 14"
edit 'Nightfall (V) (Virtual Set 2)' "$STUBS/Nightfall_(V)_(Virtual_Set_2).wiki" "VS2O stub 15"
edit 'Obi-Wan'\''s Cape (V) (Virtual Set 2)' "$STUBS/ObiWans_Cape_(V)_(Virtual_Set_2).wiki" "VS2O stub 16"
edit 'Panic (V) (Virtual Set 2)' "$STUBS/Panic_(V)_(Virtual_Set_2).wiki" "VS2O stub 17"
edit 'Rebel Reinforcements (V) (Virtual Set 2)' "$STUBS/Rebel_Reinforcements_(V)_(Virtual_Set_2).wiki" "VS2O stub 18"
edit 'Rebel Trooper (V) (Virtual Set 2)' "$STUBS/Rebel_Trooper_(V)_(Virtual_Set_2).wiki" "VS2O stub 19"
edit 'Return Of A Jedi (V) (Virtual Set 2)' "$STUBS/Return_Of_A_Jedi_(V)_(Virtual_Set_2).wiki" "VS2O stub 20"
edit 'Rycar Ryjerd (V) (Virtual Set 2)' "$STUBS/Rycar_Ryjerd_(V)_(Virtual_Set_2).wiki" "VS2O stub 21"
edit 'Sandcrawler (V) (Light) (Virtual Set 2)' "$STUBS/Sandcrawler_(V)_(Light)_(Virtual_Set_2).wiki" "VS2O stub 22"
edit 'Special Modifications (V) (Virtual Set 2)' "$STUBS/Special_Modifications_(V)_(Virtual_Set_2).wiki" "VS2O stub 23"
edit 'Utinni! (V) (Light) (Virtual Set 2)' "$STUBS/Utinni_(V)_(Light)_(Virtual_Set_2).wiki" "VS2O stub 24"
edit 'Yavin Sentry (V) (Virtual Set 2)' "$STUBS/Yavin_Sentry_(V)_(Virtual_Set_2).wiki" "VS2O stub 25"
edit 'Admiral Motti (V) (Virtual Set 2)' "$STUBS/Admiral_Motti_(V)_(Virtual_Set_2).wiki" "VS2O stub 26"
edit 'Bantha (V) (Virtual Set 2)' "$STUBS/Bantha_(V)_(Virtual_Set_2).wiki" "VS2O stub 27"
edit 'Commander Praji (V) (Virtual Set 2)' "$STUBS/Commander_Praji_(V)_(Virtual_Set_2).wiki" "VS2O stub 28"
edit 'Death Star Sentry (V) (Virtual Set 2)' "$STUBS/Death_Star_Sentry_(V)_(Virtual_Set_2).wiki" "VS2O stub 29"
edit 'Djas Puhr (V) (Virtual Set 2)' "$STUBS/Djas_Puhr_(V)_(Virtual_Set_2).wiki" "VS2O stub 30"
edit 'Emergency Deployment (V) (Virtual Set 2)' "$STUBS/Emergency_Deployment_(V)_(Virtual_Set_2).wiki" "VS2O stub 31"
edit 'Fear Will Keep Them In Line (V) (Virtual Set 2)' "$STUBS/Fear_Will_Keep_Them_In_Line_(V)_(Virtual_Set_2).wiki" "VS2O stub 32"
edit 'General Tagge (V) (Virtual Set 2)' "$STUBS/General_Tagge_(V)_(Virtual_Set_2).wiki" "VS2O stub 33"
edit 'Han Seeker (V) (Virtual Set 2)' "$STUBS/Han_Seeker_(V)_(Virtual_Set_2).wiki" "VS2O stub 34"
edit 'I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)' "$STUBS/I_Find_Your_Lack_Of_Faith_Disturbing_(V)_(Virtual_Set_2).wiki" "VS2O stub 35"
edit 'Imperial-Class Star Destroyer (V) (Virtual Set 2)' "$STUBS/ImperialClass_Star_Destroyer_(V)_(Virtual_Set_2).wiki" "VS2O stub 36"
edit 'Imperial Reinforcements (V) (Virtual Set 2)' "$STUBS/Imperial_Reinforcements_(V)_(Virtual_Set_2).wiki" "VS2O stub 37"
edit 'Jawa Pack (V) (Virtual Set 2)' "$STUBS/Jawa_Pack_(V)_(Virtual_Set_2).wiki" "VS2O stub 38"
edit 'Kitik Keed'\''kak (V) (Virtual Set 2)' "$STUBS/Kitik_Keedkak_(V)_(Virtual_Set_2).wiki" "VS2O stub 39"
edit 'Labria (V) (Virtual Set 2)' "$STUBS/Labria_(V)_(Virtual_Set_2).wiki" "VS2O stub 40"
edit 'Local Trouble (V) (Virtual Set 2)' "$STUBS/Local_Trouble_(V)_(Virtual_Set_2).wiki" "VS2O stub 41"
edit 'Molator (V) (Virtual Set 2)' "$STUBS/Molator_(V)_(Virtual_Set_2).wiki" "VS2O stub 42"
edit 'Sandcrawler (V) (Dark) (Virtual Set 2)' "$STUBS/Sandcrawler_(V)_(Dark)_(Virtual_Set_2).wiki" "VS2O stub 43"
edit 'Send A Detachment Down (V) (Virtual Set 2)' "$STUBS/Send_A_Detachment_Down_(V)_(Virtual_Set_2).wiki" "VS2O stub 44"
edit 'Stormtrooper (V) (Virtual Set 2)' "$STUBS/Stormtrooper_(V)_(Virtual_Set_2).wiki" "VS2O stub 45"
edit 'Sunsdown (V) (Virtual Set 2)' "$STUBS/Sunsdown_(V)_(Virtual_Set_2).wiki" "VS2O stub 46"
edit 'Tactical Re-Call (V) (Virtual Set 2)' "$STUBS/Tactical_ReCall_(V)_(Virtual_Set_2).wiki" "VS2O stub 47"
edit 'The Empire'\''s Back (V) (Virtual Set 2)' "$STUBS/The_Empires_Back_(V)_(Virtual_Set_2).wiki" "VS2O stub 48"
edit 'Utinni! (V) (Dark) (Virtual Set 2)' "$STUBS/Utinni_(V)_(Dark)_(Virtual_Set_2).wiki" "VS2O stub 49"
edit 'We'\''re All Gonna Be A Lot Thinner! (V) (Virtual Set 2)' "$STUBS/Were_All_Gonna_Be_A_Lot_Thinner_(V)_(Virtual_Set_2).wiki" "VS2O stub 50"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 2 (Original)
Affect Mind (V) (Virtual Set 2)
Biggs Darklighter (V) (Virtual Set 2)
C-3PO (See-Threepio) (V) (Virtual Set 2)
Cantina Brawl (V) (Virtual Set 2)
Demotion (V) (Virtual Set 2)
Escape Pod (V) (Virtual Set 2)
General Dodonna (V) (Virtual Set 2)
Han's Back (V) (Virtual Set 2)
Han's Dice (V) (Virtual Set 2)
Into The Garbage Chute, Flyboy (V) (Virtual Set 2)
Jawa Siesta (V) (Virtual Set 2)
K'lor'slug (V) (Virtual Set 2)
Leia's Back (V) (Virtual Set 2)
Luke's Back (V) (Virtual Set 2)
Nightfall (V) (Virtual Set 2)
Obi-Wan's Cape (V) (Virtual Set 2)
Panic (V) (Virtual Set 2)
Rebel Reinforcements (V) (Virtual Set 2)
Rebel Trooper (V) (Virtual Set 2)
Return Of A Jedi (V) (Virtual Set 2)
Rycar Ryjerd (V) (Virtual Set 2)
Sandcrawler (V) (Light) (Virtual Set 2)
Special Modifications (V) (Virtual Set 2)
Utinni! (V) (Light) (Virtual Set 2)
Yavin Sentry (V) (Virtual Set 2)
Admiral Motti (V) (Virtual Set 2)
Bantha (V) (Virtual Set 2)
Commander Praji (V) (Virtual Set 2)
Death Star Sentry (V) (Virtual Set 2)
Djas Puhr (V) (Virtual Set 2)
Emergency Deployment (V) (Virtual Set 2)
Fear Will Keep Them In Line (V) (Virtual Set 2)
General Tagge (V) (Virtual Set 2)
Han Seeker (V) (Virtual Set 2)
I Find Your Lack Of Faith Disturbing (V) (Virtual Set 2)
Imperial-Class Star Destroyer (V) (Virtual Set 2)
Imperial Reinforcements (V) (Virtual Set 2)
Jawa Pack (V) (Virtual Set 2)
Kitik Keed'kak (V) (Virtual Set 2)
Labria (V) (Virtual Set 2)
Local Trouble (V) (Virtual Set 2)
Molator (V) (Virtual Set 2)
Sandcrawler (V) (Dark) (Virtual Set 2)
Send A Detachment Down (V) (Virtual Set 2)
Stormtrooper (V) (Virtual Set 2)
Sunsdown (V) (Virtual Set 2)
Tactical Re-Call (V) (Virtual Set 2)
The Empire's Back (V) (Virtual Set 2)
Utinni! (V) (Dark) (Virtual Set 2)
We're All Gonna Be A Lot Thinner! (V) (Virtual Set 2)
Main Page
Category:Virtual Original sets
PURGE

python3 - <<'PY'
import urllib.request, urllib.parse
pass_n=0
fail=[]
slugs=['Affect_Mind_(V)_(Virtual_Set_2)', 'Biggs_Darklighter_(V)_(Virtual_Set_2)', 'C-3PO_(See-Threepio)_(V)_(Virtual_Set_2)', 'Cantina_Brawl_(V)_(Virtual_Set_2)', 'Demotion_(V)_(Virtual_Set_2)', 'Escape_Pod_(V)_(Virtual_Set_2)', 'General_Dodonna_(V)_(Virtual_Set_2)', "Han's_Back_(V)_(Virtual_Set_2)", "Han's_Dice_(V)_(Virtual_Set_2)", 'Into_The_Garbage_Chute,_Flyboy_(V)_(Virtual_Set_2)', 'Jawa_Siesta_(V)_(Virtual_Set_2)', "K'lor'slug_(V)_(Virtual_Set_2)", "Leia's_Back_(V)_(Virtual_Set_2)", "Luke's_Back_(V)_(Virtual_Set_2)", 'Nightfall_(V)_(Virtual_Set_2)', "Obi-Wan's_Cape_(V)_(Virtual_Set_2)", 'Panic_(V)_(Virtual_Set_2)', 'Rebel_Reinforcements_(V)_(Virtual_Set_2)', 'Rebel_Trooper_(V)_(Virtual_Set_2)', 'Return_Of_A_Jedi_(V)_(Virtual_Set_2)', 'Rycar_Ryjerd_(V)_(Virtual_Set_2)', 'Sandcrawler_(V)_(Light)_(Virtual_Set_2)', 'Special_Modifications_(V)_(Virtual_Set_2)', 'Utinni!_(V)_(Light)_(Virtual_Set_2)', 'Yavin_Sentry_(V)_(Virtual_Set_2)', 'Admiral_Motti_(V)_(Virtual_Set_2)', 'Bantha_(V)_(Virtual_Set_2)', 'Commander_Praji_(V)_(Virtual_Set_2)', 'Death_Star_Sentry_(V)_(Virtual_Set_2)', 'Djas_Puhr_(V)_(Virtual_Set_2)', 'Emergency_Deployment_(V)_(Virtual_Set_2)', 'Fear_Will_Keep_Them_In_Line_(V)_(Virtual_Set_2)', 'General_Tagge_(V)_(Virtual_Set_2)', 'Han_Seeker_(V)_(Virtual_Set_2)', 'I_Find_Your_Lack_Of_Faith_Disturbing_(V)_(Virtual_Set_2)', 'Imperial-Class_Star_Destroyer_(V)_(Virtual_Set_2)', 'Imperial_Reinforcements_(V)_(Virtual_Set_2)', 'Jawa_Pack_(V)_(Virtual_Set_2)', "Kitik_Keed'kak_(V)_(Virtual_Set_2)", 'Labria_(V)_(Virtual_Set_2)', 'Local_Trouble_(V)_(Virtual_Set_2)', 'Molator_(V)_(Virtual_Set_2)', 'Sandcrawler_(V)_(Dark)_(Virtual_Set_2)', 'Send_A_Detachment_Down_(V)_(Virtual_Set_2)', 'Stormtrooper_(V)_(Virtual_Set_2)', 'Sunsdown_(V)_(Virtual_Set_2)', 'Tactical_Re-Call_(V)_(Virtual_Set_2)', "The_Empire's_Back_(V)_(Virtual_Set_2)", 'Utinni!_(V)_(Dark)_(Virtual_Set_2)', "We're_All_Gonna_Be_A_Lot_Thinner!_(V)_(Virtual_Set_2)"]
for slug in slugs:
  u="https://wiki.swccg.com/wiki/"+urllib.parse.quote(slug, safe="()_,!")
  try:
    r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
    ok=(r.status==200)
  except Exception as e:
    ok=False
  print(("PASS" if ok else "FAIL"), u)
  if ok: pass_n+=1
  else: fail.append(u)
print("STUBS %d/50 PASS fail=%s" % (pass_n, fail[:10]))
u="https://wiki.swccg.com/wiki/Virtual_Set_2_(Original)"
try:
  r=urllib.request.urlopen(urllib.request.Request(u, method="HEAD"), timeout=30)
  print(("PASS" if r.status==200 else "FAIL"), "HUB", u)
except Exception:
  print("FAIL HUB", u)
print("VS2O STUBS APPLY OK")
PY
