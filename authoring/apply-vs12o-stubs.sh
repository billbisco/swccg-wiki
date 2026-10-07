#!/bin/bash
set -euo pipefail
ROOT=/opt/swccg-wiki
IMG=$ROOT/images/vs12-original
STUBS=$ROOT/pages/vs12-original
HUBS=$ROOT/pages/set-hubs
STAGE=/tmp/vs12o-stubs-import

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

echo "== importImages VS12O stubs =="
mkdir -p "$STAGE"
rm -f "$STAGE"/*
cp -f "$IMG"/VS12O-*.png "$STAGE/"
ls "$STAGE" | wc -l
docker exec swccg_wiki mkdir -p /tmp/vs12o-stubs-import
docker cp "$STAGE/." swccg_wiki:/tmp/vs12o-stubs-import/
set +e
docker exec swccg_wiki php maintenance/run.php importImages \
  --user=Admin \
  --comment="Virtual Set 12 (Original) Remaster slip faces from VirtualCards12.pdf" \
  --overwrite \
  /tmp/vs12o-stubs-import
rc=$?
set -e
echo "importImages rc=$rc"
docker exec -u root swccg_wiki chown -R www-data:www-data /var/www/html/images || true

edit "Virtual Set 12 (Original)" "$HUBS/Virtual_Set_12_(Original).wiki" "VS12 Original: link all 43 Remaster slip stubs"
edit 'Anakin'"'"'s Lightsaber (V) (Virtual Set 12)' "$STUBS/Anakins_Lightsaber_(V)_(Virtual_Set_12).wiki" "VS12O stub 01"
edit 'At Peace (V) (Virtual Set 12)' "$STUBS/At_Peace_(V)_(Virtual_Set_12).wiki" "VS12O stub 02"
edit 'Changing The Odds (V) (Virtual Set 12)' "$STUBS/Changing_The_Odds_(V)_(Virtual_Set_12).wiki" "VS12O stub 03"
edit 'Chewie, Enraged (V) (Virtual Set 12)' "$STUBS/Chewie,_Enraged_(V)_(Virtual_Set_12).wiki" "VS12O stub 04"
edit 'Commando Training (V) (Virtual Set 12)' "$STUBS/Commando_Training_(V)_(Virtual_Set_12).wiki" "VS12O stub 05"
edit 'Crash Site Memorial (V) (Virtual Set 12)' "$STUBS/Crash_Site_Memorial_(V)_(Virtual_Set_12).wiki" "VS12O stub 06"
edit 'Debnoli (V) (Virtual Set 12)' "$STUBS/Debnoli_(V)_(Virtual_Set_12).wiki" "VS12O stub 07"
edit 'Diversionary Tactics (V) (Virtual Set 12)' "$STUBS/Diversionary_Tactics_(V)_(Virtual_Set_12).wiki" "VS12O stub 08"
edit 'Endor: Ewok Village (V) (Virtual Set 12)' "$STUBS/Endor:_Ewok_Village_(V)_(Virtual_Set_12).wiki" "VS12O stub 09"
edit 'Enhanced Proton Torpedoes (V) (Virtual Set 12)' "$STUBS/Enhanced_Proton_Torpedoes_(V)_(Virtual_Set_12).wiki" "VS12O stub 10"
edit 'Faithful Service (V) (Virtual Set 12)' "$STUBS/Faithful_Service_(V)_(Virtual_Set_12).wiki" "VS12O stub 11"
edit 'I Can'"'"'t Believe He'"'"'s Gone (V) (Virtual Set 12)' "$STUBS/I_Cant_Believe_Hes_Gone_(V)_(Virtual_Set_12).wiki" "VS12O stub 12"
edit 'It Is The Future You See (V) (Virtual Set 12)' "$STUBS/It_Is_The_Future_You_See_(V)_(Virtual_Set_12).wiki" "VS12O stub 13"
edit 'Jeroen Webb (V) (Virtual Set 12)' "$STUBS/Jeroen_Webb_(V)_(Virtual_Set_12).wiki" "VS12O stub 14"
edit 'Ki-Adi-Mundi (V) (Virtual Set 12)' "$STUBS/Ki-Adi-Mundi_(V)_(Virtual_Set_12).wiki" "VS12O stub 15"
edit 'Master Qui-Gon (V) (Virtual Set 12)' "$STUBS/Master_Qui-Gon_(V)_(Virtual_Set_12).wiki" "VS12O stub 16"
edit 'Orrimaarko (V) (Virtual Set 12)' "$STUBS/Orrimaarko_(V)_(Virtual_Set_12).wiki" "VS12O stub 17"
edit 'Precise Hit (V) (Virtual Set 12)' "$STUBS/Precise_Hit_(V)_(Virtual_Set_12).wiki" "VS12O stub 18"
edit 'Rebel Leadership (V) (Virtual Set 12)' "$STUBS/Rebel_Leadership_(V)_(Virtual_Set_12).wiki" "VS12O stub 19"
edit 'Red Squadron 7 (V) (Virtual Set 12)' "$STUBS/Red_Squadron_7_(V)_(Virtual_Set_12).wiki" "VS12O stub 20"
edit 'Yoda, Senior Council Member (V) (Virtual Set 12)' "$STUBS/Yoda,_Senior_Council_Member_(V)_(Virtual_Set_12).wiki" "VS12O stub 21"
edit '3,720 To 1 (V) (Virtual Set 12)' "$STUBS/3,720_To_1_(V)_(Virtual_Set_12).wiki" "VS12O stub 22"
edit 'At Last We Are Getting Results (V) (Virtual Set 12)' "$STUBS/At_Last_We_Are_Getting_Results_(V)_(Virtual_Set_12).wiki" "VS12O stub 23"
edit 'Aurra Sing (V) (Virtual Set 12)' "$STUBS/Aurra_Sing_(V)_(Virtual_Set_12).wiki" "VS12O stub 24"
edit 'Blown Clear (V) (Virtual Set 12)' "$STUBS/Blown_Clear_(V)_(Virtual_Set_12).wiki" "VS12O stub 25"
edit 'Bounty (V) (Virtual Set 12)' "$STUBS/Bounty_(V)_(Virtual_Set_12).wiki" "VS12O stub 26"
edit 'Colonel Wullf Yularen (V) (Virtual Set 12)' "$STUBS/Colonel_Wullf_Yularen_(V)_(Virtual_Set_12).wiki" "VS12O stub 27"
edit 'Coordinated Attack (V) (Virtual Set 12)' "$STUBS/Coordinated_Attack_(V)_(Virtual_Set_12).wiki" "VS12O stub 28"
edit 'Crush The Rebellion (V) (Virtual Set 12)' "$STUBS/Crush_The_Rebellion_(V)_(Virtual_Set_12).wiki" "VS12O stub 29"
edit 'Dark Jedi Lightsaber (V) (Virtual Set 12)' "$STUBS/Dark_Jedi_Lightsaber_(V)_(Virtual_Set_12).wiki" "VS12O stub 30"
edit 'Daultay Dofine (V) (Virtual Set 12)' "$STUBS/Daultay_Dofine_(V)_(Virtual_Set_12).wiki" "VS12O stub 31"
edit 'Forced Servitude (V) (Virtual Set 12)' "$STUBS/Forced_Servitude_(V)_(Virtual_Set_12).wiki" "VS12O stub 32"
edit 'I'"'"'m Sorry (V) (Virtual Set 12)' "$STUBS/Im_Sorry_(V)_(Virtual_Set_12).wiki" "VS12O stub 33"
edit 'Imperial Code Cylinder (V) (Virtual Set 12)' "$STUBS/Imperial_Code_Cylinder_(V)_(Virtual_Set_12).wiki" "VS12O stub 34"
edit 'Janus Greejatus (V) (Virtual Set 12)' "$STUBS/Janus_Greejatus_(V)_(Virtual_Set_12).wiki" "VS12O stub 35"
edit 'Laser Gate (V) (Virtual Set 12)' "$STUBS/Laser_Gate_(V)_(Virtual_Set_12).wiki" "VS12O stub 36"
edit 'Maneuver Check (V) (Virtual Set 12)' "$STUBS/Maneuver_Check_(V)_(Virtual_Set_12).wiki" "VS12O stub 37"
edit 'Mara Jade, The Emperor'"'"'s Hand (V) (Virtual Set 12)' "$STUBS/Mara_Jade,_The_Emperors_Hand_(V)_(Virtual_Set_12).wiki" "VS12O stub 38"
edit 'Obsidian 10 (V) (Virtual Set 12)' "$STUBS/Obsidian_10_(V)_(Virtual_Set_12).wiki" "VS12O stub 39"
edit 'Officer Evax (V) (Virtual Set 12)' "$STUBS/Officer_Evax_(V)_(Virtual_Set_12).wiki" "VS12O stub 40"
edit 'Stinger (V) (Virtual Set 12)' "$STUBS/Stinger_(V)_(Virtual_Set_12).wiki" "VS12O stub 41"
edit 'There Is No Try & Oppressive Enforcement (V) (Virtual Set 12)' "$STUBS/There_Is_No_Try_and_Oppressive_Enforcement_(V)_(Virtual_Set_12).wiki" "VS12O stub 42"
edit 'You Want This, Don'"'"'t You? (V) (Virtual Set 12)' "$STUBS/You_Want_This,_Dont_You?_(V)_(Virtual_Set_12).wiki" "VS12O stub 43"

docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tail -8

docker exec -i swccg_wiki php maintenance/run.php purgePage <<'PURGE'
Virtual Set 12 (Original)
Anakin's Lightsaber (V) (Virtual Set 12)
At Peace (V) (Virtual Set 12)
Changing The Odds (V) (Virtual Set 12)
Chewie, Enraged (V) (Virtual Set 12)
Commando Training (V) (Virtual Set 12)
Crash Site Memorial (V) (Virtual Set 12)
Debnoli (V) (Virtual Set 12)
Diversionary Tactics (V) (Virtual Set 12)
Endor: Ewok Village (V) (Virtual Set 12)
Enhanced Proton Torpedoes (V) (Virtual Set 12)
Faithful Service (V) (Virtual Set 12)
I Can't Believe He's Gone (V) (Virtual Set 12)
It Is The Future You See (V) (Virtual Set 12)
Jeroen Webb (V) (Virtual Set 12)
Ki-Adi-Mundi (V) (Virtual Set 12)
Master Qui-Gon (V) (Virtual Set 12)
Orrimaarko (V) (Virtual Set 12)
Precise Hit (V) (Virtual Set 12)
Rebel Leadership (V) (Virtual Set 12)
Red Squadron 7 (V) (Virtual Set 12)
Yoda, Senior Council Member (V) (Virtual Set 12)
3,720 To 1 (V) (Virtual Set 12)
At Last We Are Getting Results (V) (Virtual Set 12)
Aurra Sing (V) (Virtual Set 12)
Blown Clear (V) (Virtual Set 12)
Bounty (V) (Virtual Set 12)
Colonel Wullf Yularen (V) (Virtual Set 12)
Coordinated Attack (V) (Virtual Set 12)
Crush The Rebellion (V) (Virtual Set 12)
Dark Jedi Lightsaber (V) (Virtual Set 12)
Daultay Dofine (V) (Virtual Set 12)
Forced Servitude (V) (Virtual Set 12)
I'm Sorry (V) (Virtual Set 12)
Imperial Code Cylinder (V) (Virtual Set 12)
Janus Greejatus (V) (Virtual Set 12)
Laser Gate (V) (Virtual Set 12)
Maneuver Check (V) (Virtual Set 12)
Mara Jade, The Emperor's Hand (V) (Virtual Set 12)
Obsidian 10 (V) (Virtual Set 12)
Officer Evax (V) (Virtual Set 12)
Stinger (V) (Virtual Set 12)
There Is No Try & Oppressive Enforcement (V) (Virtual Set 12)
You Want This, Don't You? (V) (Virtual Set 12)
Main Page
Category:Virtual Original sets
PURGE

echo VS12O_APPLY_DONE
