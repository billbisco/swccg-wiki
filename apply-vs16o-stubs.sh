#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs16-original
STUBS=$ROOT/pages/vs16-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs16o-stubs-import

strip() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p=Path(sys.argv[1])
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

echo "== importImages VS16O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS16O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs16o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs16o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 16 (Original) slip faces from VirtualCards16.pdf" \
  --overwrite \
  /tmp/vs16o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

docker exec -u root swccg_wiki bash -c 'php -r "if(function_exists(\"apcu_clear_cache\")){apcu_clear_cache(); echo \"APCu cleared\n\";} else {echo \"no apcu\n\";}"' || true
docker exec -u root swccg_wiki bash -c 'apachectl graceful 2>/dev/null || apache2ctl graceful 2>/dev/null || true'

edit "Virtual Set 16 (Original)" "$HUBS/Virtual_Set_16_(Original).wiki" "VS16 Original: link all 68 slip stubs"

edit 'Bail Organa (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Bail_Organa_(V)_(Virtual_Set_16).wiki' "VS16O stub 01"
edit 'Senator Jar Jar Binks (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Senator_Jar_Jar_Binks_(V)_(Virtual_Set_16).wiki' "VS16O stub 02"
edit 'Senator Leia Organa (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Senator_Leia_Organa_(V)_(Virtual_Set_16).wiki' "VS16O stub 03"
edit 'Senator Padme Amidala (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Senator_Padme_Amidala_(V)_(Virtual_Set_16).wiki' "VS16O stub 04"
edit 'So This Is How Liberty Dies (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/So_This_Is_How_Liberty_Dies_(V)_(Virtual_Set_16).wiki' "VS16O stub 05"
edit 'Ambush (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Ambush_(V)_(Virtual_Set_16).wiki' "VS16O stub 06"
edit 'Blockade Flagship: Prison (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Blockade_Flagship:_Prison_(V)_(Virtual_Set_16).wiki' "VS16O stub 07"
edit 'Clone Pilot (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Clone_Pilot_(V)_(Virtual_Set_16).wiki' "VS16O stub 08"
edit 'Clone Trooper (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Clone_Trooper_(V)_(Virtual_Set_16).wiki' "VS16O stub 09"
edit 'Supreme Chancellor Palpatine (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Supreme_Chancellor_Palpatine_(V)_(Virtual_Set_16).wiki' "VS16O stub 10"
edit 'We Have A Plan (V) / They Will Be Lost And Confused (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/We_Have_A_Plan_(V)_-_They_Will_Be_Lost_And_Confused_(V)_(Virtual_Set_16).wiki' "VS16O stub 11"
edit 'Bowcaster (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Bowcaster_(V)_(Virtual_Set_16).wiki' "VS16O stub 12"
edit 'Chewbacca Of Kashyyyk (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Chewbacca_Of_Kashyyyk_(V)_(Virtual_Set_16).wiki' "VS16O stub 13"
edit 'Grrrghrrrgh! (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Grrrghrrrgh!_(V)_(Virtual_Set_16).wiki' "VS16O stub 14"
edit 'Kashyyyk (Light) (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Kashyyyk_(Light)_(V)_(Virtual_Set_16).wiki' "VS16O stub 15"
edit 'Kashyyyk: Sacred Forest (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Kashyyyk:_Sacred_Forest_(V)_(Virtual_Set_16).wiki' "VS16O stub 16"
edit 'Kashyyyk: Wookiee Haven (Forest) (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Kashyyyk:_Wookiee_Haven_(Forest)_(V)_(Virtual_Set_16).wiki' "VS16O stub 17"
edit 'Wookiee (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Wookiee_(V)_(Virtual_Set_16).wiki' "VS16O stub 18"
edit 'Wookiee Guide (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Wookiee_Guide_(V)_(Virtual_Set_16).wiki' "VS16O stub 19"
edit 'Wookiee Roar (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Wookiee_Roar_(V)_(Virtual_Set_16).wiki' "VS16O stub 20"
edit 'Yarua (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Yarua_(V)_(Virtual_Set_16).wiki' "VS16O stub 21"
edit 'A Jedi'\''s Patience (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/A_Jedi'\''s_Patience_(V)_(Virtual_Set_16).wiki' "VS16O stub 22"
edit 'Artoo, Brave Little Droid (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Artoo,_Brave_Little_Droid_(V)_(Virtual_Set_16).wiki' "VS16O stub 23"
edit 'Blue Squadron 5 (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Blue_Squadron_5_(V)_(Virtual_Set_16).wiki' "VS16O stub 24"
edit 'BoShek'\''s Modified Light Freighter (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/BoShek'\''s_Modified_Light_Freighter_(V)_(Virtual_Set_16).wiki' "VS16O stub 25"
edit 'Bravo Fighter (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Bravo_Fighter_(V)_(Virtual_Set_16).wiki' "VS16O stub 26"
edit 'Corellia (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Corellia_(V)_(Virtual_Set_16).wiki' "VS16O stub 27"
edit 'Corellian Engineering Corporation (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Corellian_Engineering_Corporation_(V)_(Virtual_Set_16).wiki' "VS16O stub 28"
edit 'Coruscant: Jedi Council Chamber (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Coruscant:_Jedi_Council_Chamber_(V)_(Virtual_Set_16).wiki' "VS16O stub 29"
edit 'Coruscant: Night Club (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Coruscant:_Night_Club_(V)_(Virtual_Set_16).wiki' "VS16O stub 30"
edit 'Don'\''t Tread On Me (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Don'\''t_Tread_On_Me_(V)_(Virtual_Set_16).wiki' "VS16O stub 31"
edit 'Jedi Starfighter (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Jedi_Starfighter_(V)_(Virtual_Set_16).wiki' "VS16O stub 32"
edit 'Jedi Survivor (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Jedi_Survivor_(V)_(Virtual_Set_16).wiki' "VS16O stub 33"
edit 'Lars'\'' Protocol Droid (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Lars'\''_Protocol_Droid_(V)_(Virtual_Set_16).wiki' "VS16O stub 34"
edit 'Plo Koon (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Plo_Koon_(V)_(Virtual_Set_16).wiki' "VS16O stub 35"
edit 'Sergeant Doallyn (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Sergeant_Doallyn_(V)_(Virtual_Set_16).wiki' "VS16O stub 36"
edit 'Simple Tricks And Nonsense (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Simple_Tricks_And_Nonsense_(V)_(Virtual_Set_16).wiki' "VS16O stub 37"
edit 'Ultimatum (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Ultimatum_(V)_(Virtual_Set_16).wiki' "VS16O stub 38"
edit 'Yavin 4: Jedi Academy (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Yavin_4:_Jedi_Academy_(V)_(Virtual_Set_16).wiki' "VS16O stub 39"
edit 'An Enemy Of The Republic (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/An_Enemy_Of_The_Republic_(V)_(Virtual_Set_16).wiki' "VS16O stub 40"
edit 'Coruscant: Chancellor'\''s Office (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Coruscant:_Chancellor'\''s_Office_(V)_(Virtual_Set_16).wiki' "VS16O stub 41"
edit 'Coruscant Guard (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Coruscant_Guard_(V)_(Virtual_Set_16).wiki' "VS16O stub 42"
edit 'Elite Squadron Stormtrooper (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Elite_Squadron_Stormtrooper_(V)_(Virtual_Set_16).wiki' "VS16O stub 43"
edit 'Expand The Empire (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Expand_The_Empire_(V)_(Virtual_Set_16).wiki' "VS16O stub 44"
edit 'Keder The Black (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Keder_The_Black_(V)_(Virtual_Set_16).wiki' "VS16O stub 45"
edit 'Lord Sidious (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Lord_Sidious_(V)_(Virtual_Set_16).wiki' "VS16O stub 46"
edit 'Nute Gunray'\''s Bounty (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Nute_Gunray'\''s_Bounty_(V)_(Virtual_Set_16).wiki' "VS16O stub 47"
edit 'Order 66 (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Order_66_(V)_(Virtual_Set_16).wiki' "VS16O stub 48"
edit 'Strategic Reserves (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Strategic_Reserves_(V)_(Virtual_Set_16).wiki' "VS16O stub 49"
edit 'With Thunderous Applause (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/With_Thunderous_Applause_(V)_(Virtual_Set_16).wiki' "VS16O stub 50"
edit '3B3-10 (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/3B3-10_(V)_(Virtual_Set_16).wiki' "VS16O stub 51"
edit 'Concussion Missiles (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Concussion_Missiles_(V)_(Virtual_Set_16).wiki' "VS16O stub 52"
edit 'Death Star: Conference Room (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Death_Star:_Conference_Room_(V)_(Virtual_Set_16).wiki' "VS16O stub 53"
edit 'Execution Arena (Pit) (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Execution_Arena_(Pit)_(V)_(Virtual_Set_16).wiki' "VS16O stub 54"
edit 'It'\''s Worse (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/It'\''s_Worse_(V)_(Virtual_Set_16).wiki' "VS16O stub 55"
edit 'Katana (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Katana_(V)_(Virtual_Set_16).wiki' "VS16O stub 56"
edit 'Mandalorian Armor (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Mandalorian_Armor_(V)_(Virtual_Set_16).wiki' "VS16O stub 57"
edit 'Myn Kyneugh (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Myn_Kyneugh_(V)_(Virtual_Set_16).wiki' "VS16O stub 58"
edit 'Onyx 2 (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Onyx_2_(V)_(Virtual_Set_16).wiki' "VS16O stub 59"
edit 'Organa'\''s Ceremonial Necklace (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Organa'\''s_Ceremonial_Necklace_(V)_(Virtual_Set_16).wiki' "VS16O stub 60"
edit 'Pride Of The Empire (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Pride_Of_The_Empire_(V)_(Virtual_Set_16).wiki' "VS16O stub 61"
edit 'Release Your Anger (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Release_Your_Anger_(V)_(Virtual_Set_16).wiki' "VS16O stub 62"
edit 'Resistance (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Resistance_(V)_(Virtual_Set_16).wiki' "VS16O stub 63"
edit 'Surface Defense (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Surface_Defense_(V)_(Virtual_Set_16).wiki' "VS16O stub 64"
edit 'Thrawn'\''s Pet (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Thrawn'\''s_Pet_(V)_(Virtual_Set_16).wiki' "VS16O stub 65"
edit 'Vader'\''s Personal Shuttle (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Vader'\''s_Personal_Shuttle_(V)_(Virtual_Set_16).wiki' "VS16O stub 66"
edit 'Watto (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Watto_(V)_(Virtual_Set_16).wiki' "VS16O stub 67"
edit 'Wounded Wookiee (V) (Virtual Set 16)' '/opt/swccg-wiki/pages/vs16-original/Wounded_Wookiee_(V)_(Virtual_Set_16).wiki' "VS16O stub 68"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 16 (Original)
Bail Organa (V) (Virtual Set 16)
Senator Jar Jar Binks (V) (Virtual Set 16)
Senator Leia Organa (V) (Virtual Set 16)
Senator Padme Amidala (V) (Virtual Set 16)
So This Is How Liberty Dies (V) (Virtual Set 16)
Ambush (V) (Virtual Set 16)
Blockade Flagship: Prison (V) (Virtual Set 16)
Clone Pilot (V) (Virtual Set 16)
Clone Trooper (V) (Virtual Set 16)
Supreme Chancellor Palpatine (V) (Virtual Set 16)
We Have A Plan (V) / They Will Be Lost And Confused (V) (Virtual Set 16)
Bowcaster (V) (Virtual Set 16)
Chewbacca Of Kashyyyk (V) (Virtual Set 16)
Grrrghrrrgh! (V) (Virtual Set 16)
Kashyyyk (Light) (V) (Virtual Set 16)
Kashyyyk: Sacred Forest (V) (Virtual Set 16)
Kashyyyk: Wookiee Haven (Forest) (V) (Virtual Set 16)
Wookiee (V) (Virtual Set 16)
Wookiee Guide (V) (Virtual Set 16)
Wookiee Roar (V) (Virtual Set 16)
Yarua (V) (Virtual Set 16)
A Jedi's Patience (V) (Virtual Set 16)
Artoo, Brave Little Droid (V) (Virtual Set 16)
Blue Squadron 5 (V) (Virtual Set 16)
BoShek's Modified Light Freighter (V) (Virtual Set 16)
Bravo Fighter (V) (Virtual Set 16)
Corellia (V) (Virtual Set 16)
Corellian Engineering Corporation (V) (Virtual Set 16)
Coruscant: Jedi Council Chamber (V) (Virtual Set 16)
Coruscant: Night Club (V) (Virtual Set 16)
Don't Tread On Me (V) (Virtual Set 16)
Jedi Starfighter (V) (Virtual Set 16)
Jedi Survivor (V) (Virtual Set 16)
Lars' Protocol Droid (V) (Virtual Set 16)
Plo Koon (V) (Virtual Set 16)
Sergeant Doallyn (V) (Virtual Set 16)
Simple Tricks And Nonsense (V) (Virtual Set 16)
Ultimatum (V) (Virtual Set 16)
Yavin 4: Jedi Academy (V) (Virtual Set 16)
An Enemy Of The Republic (V) (Virtual Set 16)
Coruscant: Chancellor's Office (V) (Virtual Set 16)
Coruscant Guard (V) (Virtual Set 16)
Elite Squadron Stormtrooper (V) (Virtual Set 16)
Expand The Empire (V) (Virtual Set 16)
Keder The Black (V) (Virtual Set 16)
Lord Sidious (V) (Virtual Set 16)
Nute Gunray's Bounty (V) (Virtual Set 16)
Order 66 (V) (Virtual Set 16)
Strategic Reserves (V) (Virtual Set 16)
With Thunderous Applause (V) (Virtual Set 16)
3B3-10 (V) (Virtual Set 16)
Concussion Missiles (V) (Virtual Set 16)
Death Star: Conference Room (V) (Virtual Set 16)
Execution Arena (Pit) (V) (Virtual Set 16)
It's Worse (V) (Virtual Set 16)
Katana (V) (Virtual Set 16)
Mandalorian Armor (V) (Virtual Set 16)
Myn Kyneugh (V) (Virtual Set 16)
Onyx 2 (V) (Virtual Set 16)
Organa's Ceremonial Necklace (V) (Virtual Set 16)
Pride Of The Empire (V) (Virtual Set 16)
Release Your Anger (V) (Virtual Set 16)
Resistance (V) (Virtual Set 16)
Surface Defense (V) (Virtual Set 16)
Thrawn's Pet (V) (Virtual Set 16)
Vader's Personal Shuttle (V) (Virtual Set 16)
Watto (V) (Virtual Set 16)
Wounded Wookiee (V) (Virtual Set 16)
Main Page
Category:Virtual Original sets
PURGE

echo VS16O_APPLY_DONE
