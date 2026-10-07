#!/bin/bash
# Roll dual-face Objective layout (image2 + image2_layout=responsive) to all remaining Objectives.
# Do NOT touch Template:Card / Common.css / Common.js / CacheEpoch.
set -euo pipefail
ROOT=/opt/swccg-wiki
PAGES="$ROOT/pages"
cd "$ROOT"

strip_bom() {
  python3 - "$1" <<'PY'
from pathlib import Path
import sys
p = Path(sys.argv[1])
raw = p.read_bytes()
if raw.startswith(b"\xef\xbb\xbf"):
    raw = raw[3:]
text = raw.decode("utf-8").replace("\r\n", "\n").replace("\r", "\n")
p.write_text(text, encoding="utf-8", newline="\n")
print(p.name, "ok", len(text))
PY
}

edit() {
  local title="$1" file="$2" summary="$3"
  if [ ! -s "$file" ]; then echo "ERROR: missing $file" >&2; exit 1; fi
  strip_bom "$file"
  echo "== edit $title =="
  docker exec -i swccg_wiki php maintenance/run.php edit --user=Admin --summary="$summary" "$title" < "$file"
}

SUMMARY="Objective dual-face: |image2= 7-side GIF + |image2_layout=responsive (match SYCFA gold)"
echo "== Rolling image2 to 81 Objective pages =="

edit "A Great Tactician Creates Plans / The Result Is Often Resentment" "$PAGES/A_Great_Tactician_Creates_Plans___The_Result_Is_Often_Resentment.wiki" "$SUMMARY"
edit "A Great Tactician Creates Plans / The Result Is Often Resentment (Dark)" "$PAGES/A_Great_Tactician_Creates_Plans___The_Result_Is_Often_Resentment_(Dark).wiki" "$SUMMARY"
edit "A Stunning Move / A Valuable Hostage" "$PAGES/A_Stunning_Move___A_Valuable_Hostage.wiki" "$SUMMARY"
edit "A Stunning Move / A Valuable Hostage (Dark)" "$PAGES/A_Stunning_Move___A_Valuable_Hostage_(Dark).wiki" "$SUMMARY"
edit "Agents In The Court / No Love For The Empire" "$PAGES/Agents_In_The_Court___No_Love_For_The_Empire.wiki" "$SUMMARY"
edit "Agents Of Black Sun / Vengeance Of The Dark Prince" "$PAGES/Agents_Of_Black_Sun___Vengeance_Of_The_Dark_Prince.wiki" "$SUMMARY"
edit "Bring Him Before Me / Take Your Father's Place" "$PAGES/Bring_Him_Before_Me___Take_Your_Father's_Place.wiki" "$SUMMARY"
edit "Carbon Chamber Testing / My Favorite Decoration" "$PAGES/Carbon_Chamber_Testing___My_Favorite_Decoration.wiki" "$SUMMARY"
edit "City In The Clouds / You Truly Belong Here With Us" "$PAGES/City_In_The_Clouds___You_Truly_Belong_Here_With_Us.wiki" "$SUMMARY"
edit "Court Of The Vile Gangster / I Shall Enjoy Watching You Die" "$PAGES/Court_Of_The_Vile_Gangster___I_Shall_Enjoy_Watching_You_Die.wiki" "$SUMMARY"
edit "Dantooine Base Operations / More Dangerous Than You Realize" "$PAGES/Dantooine_Base_Operations___More_Dangerous_Than_You_Realize.wiki" "$SUMMARY"
edit "Diplomatic Mission To Alderaan / A Weakness Can Be Found" "$PAGES/Diplomatic_Mission_To_Alderaan___A_Weakness_Can_Be_Found.wiki" "$SUMMARY"
edit "Diplomatic Mission To Alderaan / A Weakness Can Be Found (Virtual Set 3)" "$PAGES/Diplomatic_Mission_To_Alderaan___A_Weakness_Can_Be_Found_(Virtual_Set_3).wiki" "$SUMMARY"
edit "Endor Operations / Imperial Outpost" "$PAGES/Endor_Operations___Imperial_Outpost.wiki" "$SUMMARY"
edit "He Is The Chosen One / He Will Bring Balance" "$PAGES/He_Is_The_Chosen_One___He_Will_Bring_Balance.wiki" "$SUMMARY"
edit "He Is The Chosen One / He Will Bring Balance (Virtual Set 8)" "$PAGES/He_Is_The_Chosen_One___He_Will_Bring_Balance_(Virtual_Set_8).wiki" "$SUMMARY"
edit "Hidden Base / Systems Will Slip Through Your Fingers" "$PAGES/Hidden_Base___Systems_Will_Slip_Through_Your_Fingers.wiki" "$SUMMARY"
edit "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe" "$PAGES/Hunt_Down_And_Destroy_The_Jedi___Their_Fire_Has_Gone_Out_Of_The_Universe.wiki" "$SUMMARY"
edit "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe (V)" "$PAGES/Hunt_Down_And_Destroy_The_Jedi___Their_Fire_Has_Gone_Out_Of_The_Universe_(V).wiki" "$SUMMARY"
edit "Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe (V) (Dark)" "$PAGES/Hunt_Down_And_Destroy_The_Jedi___Their_Fire_Has_Gone_Out_Of_The_Universe_(V)_(Dark).wiki" "$SUMMARY"
edit "Hunt For The Droid General / He's A Coward" "$PAGES/Hunt_For_The_Droid_General___He's_A_Coward.wiki" "$SUMMARY"
edit "Hunt For The Droid General / He's A Coward (Virtual Set 21)" "$PAGES/Hunt_For_The_Droid_General___He's_A_Coward_(Virtual_Set_21).wiki" "$SUMMARY"
edit "I Want That Map / And Now You'll Give It To Me" "$PAGES/I_Want_That_Map___And_Now_You'll_Give_It_To_Me.wiki" "$SUMMARY"
edit "I Want That Map / And Now You'll Give It To Me (Dark)" "$PAGES/I_Want_That_Map___And_Now_You'll_Give_It_To_Me_(Dark).wiki" "$SUMMARY"
edit "ISB Operations / Empire's Sinister Agents" "$PAGES/ISB_Operations___Empire's_Sinister_Agents.wiki" "$SUMMARY"
edit "Imperial Entanglements / No One To Stop Us This Time" "$PAGES/Imperial_Entanglements___No_One_To_Stop_Us_This_Time.wiki" "$SUMMARY"
edit "Imperial Entanglements / No One To Stop Us This Time (Dark)" "$PAGES/Imperial_Entanglements___No_One_To_Stop_Us_This_Time_(Dark).wiki" "$SUMMARY"
edit "Imperial Occupation / Imperial Control" "$PAGES/Imperial_Occupation___Imperial_Control.wiki" "$SUMMARY"
edit "Invasion / In Complete Control" "$PAGES/Invasion___In_Complete_Control.wiki" "$SUMMARY"
edit "Let Them Make The First Move / At Last We Will Have Revenge" "$PAGES/Let_Them_Make_The_First_Move___At_Last_We_Will_Have_Revenge.wiki" "$SUMMARY"
edit "Local Uprising / Liberation" "$PAGES/Local_Uprising___Liberation.wiki" "$SUMMARY"
edit "Massassi Base Operations / One In A Million" "$PAGES/Massassi_Base_Operations___One_In_A_Million.wiki" "$SUMMARY"
edit "Mind What You Have Learned / Save You It Can" "$PAGES/Mind_What_You_Have_Learned___Save_You_It_Can.wiki" "$SUMMARY"
edit "Mind What You Have Learned / Save You It Can (V)" "$PAGES/Mind_What_You_Have_Learned___Save_You_It_Can_(V).wiki" "$SUMMARY"
edit "Mind What You Have Learned / Save You It Can (V) (Virtual Set 25)" "$PAGES/Mind_What_You_Have_Learned___Save_You_It_Can_(V)_(Virtual_Set_25).wiki" "$SUMMARY"
edit "My Kind Of Scum / Fearless And Inventive" "$PAGES/My_Kind_Of_Scum___Fearless_And_Inventive.wiki" "$SUMMARY"
edit "My Lord, Is That Legal? / I Will Make It Legal" "$PAGES/My_Lord,_Is_That_Legal___I_Will_Make_It_Legal.wiki" "$SUMMARY"
edit "No Money, No Parts, No Deal! / You're A Slave?" "$PAGES/No_Money,_No_Parts,_No_Deal!___You're_A_Slave.wiki" "$SUMMARY"
edit "Old Allies / We Need Your Help" "$PAGES/Old_Allies___We_Need_Your_Help.wiki" "$SUMMARY"
edit "Old Allies / We Need Your Help (Virtual Set 4)" "$PAGES/Old_Allies___We_Need_Your_Help_(Virtual_Set_4).wiki" "$SUMMARY"
edit "On The Verge Of Greatness / Taking Control Of The Weapon" "$PAGES/On_The_Verge_Of_Greatness___Taking_Control_Of_The_Weapon.wiki" "$SUMMARY"
edit "On The Verge Of Greatness / Taking Control Of The Weapon (Dark)" "$PAGES/On_The_Verge_Of_Greatness___Taking_Control_Of_The_Weapon_(Dark).wiki" "$SUMMARY"
edit "Plead My Case To The Senate / Sanity And Compassion" "$PAGES/Plead_My_Case_To_The_Senate___Sanity_And_Compassion.wiki" "$SUMMARY"
edit "Quiet Mining Colony / Independent Operation" "$PAGES/Quiet_Mining_Colony___Independent_Operation.wiki" "$SUMMARY"
edit "Ralltiir Operations / In The Hands Of The Empire" "$PAGES/Ralltiir_Operations___In_The_Hands_Of_The_Empire.wiki" "$SUMMARY"
edit "Rebel Strike Team / Garrison Destroyed" "$PAGES/Rebel_Strike_Team___Garrison_Destroyed.wiki" "$SUMMARY"
edit "Rescue The Princess / Sometimes I Amaze Even Myself" "$PAGES/Rescue_The_Princess___Sometimes_I_Amaze_Even_Myself.wiki" "$SUMMARY"
edit "Rescue The Princess / Sometimes I Amaze Even Myself (V)" "$PAGES/Rescue_The_Princess___Sometimes_I_Amaze_Even_Myself_(V).wiki" "$SUMMARY"
edit "Rescue The Princess / Sometimes I Amaze Even Myself (V) (Virtual Set 15)" "$PAGES/Rescue_The_Princess___Sometimes_I_Amaze_Even_Myself_(V)_(Virtual_Set_15).wiki" "$SUMMARY"
edit "Shadow Collective / You Know Who I Answer To" "$PAGES/Shadow_Collective___You_Know_Who_I_Answer_To.wiki" "$SUMMARY"
edit "Shadow Collective / You Know Who I Answer To (Dark)" "$PAGES/Shadow_Collective___You_Know_Who_I_Answer_To_(Dark).wiki" "$SUMMARY"
edit "The Empire Knows We're Here / Prepare For Ground Assault" "$PAGES/The_Empire_Knows_We're_Here___Prepare_For_Ground_Assault.wiki" "$SUMMARY"
edit "The Empire Knows We're Here / Prepare For Ground Assault (Virtual Set 22)" "$PAGES/The_Empire_Knows_We're_Here___Prepare_For_Ground_Assault_(Virtual_Set_22).wiki" "$SUMMARY"
edit "The First Order Reigns / The Resistance Is Doomed" "$PAGES/The_First_Order_Reigns___The_Resistance_Is_Doomed.wiki" "$SUMMARY"
edit "The First Order Reigns / The Resistance Is Doomed (Dark)" "$PAGES/The_First_Order_Reigns___The_Resistance_Is_Doomed_(Dark).wiki" "$SUMMARY"
edit "The Galaxy May Need A Legend / We Need Luke Skywalker" "$PAGES/The_Galaxy_May_Need_A_Legend___We_Need_Luke_Skywalker.wiki" "$SUMMARY"
edit "The Galaxy May Need A Legend / We Need Luke Skywalker (Virtual Set 11)" "$PAGES/The_Galaxy_May_Need_A_Legend___We_Need_Luke_Skywalker_(Virtual_Set_11).wiki" "$SUMMARY"
edit "The Hidden Path / Gather Allies And Train" "$PAGES/The_Hidden_Path___Gather_Allies_And_Train.wiki" "$SUMMARY"
edit "The Hidden Path / Gather Allies And Train (Virtual Set 26)" "$PAGES/The_Hidden_Path___Gather_Allies_And_Train_(Virtual_Set_26).wiki" "$SUMMARY"
edit "The Hyperdrive Generator's Gone / We'll Need A New One" "$PAGES/The_Hyperdrive_Generator's_Gone___We'll_Need_A_New_One.wiki" "$SUMMARY"
edit "The Hyperdrive Generator's Gone / We'll Need A New One (V)" "$PAGES/The_Hyperdrive_Generator's_Gone___We'll_Need_A_New_One_(V).wiki" "$SUMMARY"
edit "The Hyperdrive Generator's Gone / We'll Need A New One (V) (Virtual Set 10)" "$PAGES/The_Hyperdrive_Generator's_Gone___We'll_Need_A_New_One_(V)_(Virtual_Set_10).wiki" "$SUMMARY"
edit "The Shield Will Be Down In Moments / Imperial Troops Have Entered The Base!" "$PAGES/The_Shield_Will_Be_Down_In_Moments___Imperial_Troops_Have_Entered_The_Base!.wiki" "$SUMMARY"
edit "The Shield Will Be Down In Moments / Imperial Troops Have Entered The Base! (AI)" "$PAGES/The_Shield_Will_Be_Down_In_Moments___Imperial_Troops_Have_Entered_The_Base!_(AI).wiki" "$SUMMARY"
edit "The Shield Will Be Down In Moments / Imperial Troops Have Entered The Base! (AI) (Dark)" "$PAGES/The_Shield_Will_Be_Down_In_Moments___Imperial_Troops_Have_Entered_The_Base!_(AI)_(Dark).wiki" "$SUMMARY"
edit "The Shield Will Be Down In Moments / Imperial Troops Have Entered The Base! (Dark)" "$PAGES/The_Shield_Will_Be_Down_In_Moments___Imperial_Troops_Have_Entered_The_Base!_(Dark).wiki" "$SUMMARY"
edit "There Is Good In Him / I Can Save Him" "$PAGES/There_Is_Good_In_Him___I_Can_Save_Him.wiki" "$SUMMARY"
edit "They Have No Idea We're Coming / Until We Win, Or The Chances Are Spent" "$PAGES/They_Have_No_Idea_We're_Coming___Until_We_Win,_Or_The_Chances_Are_Spent.wiki" "$SUMMARY"
edit "They Have No Idea We're Coming / Until We Win, Or The Chances Are Spent (Virtual Set 9)" "$PAGES/They_Have_No_Idea_We're_Coming___Until_We_Win,_Or_The_Chances_Are_Spent_(Virtual_Set_9).wiki" "$SUMMARY"
edit "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further" "$PAGES/This_Deal_Is_Getting_Worse_All_The_Time___Pray_I_Don't_Alter_It_Any_Further.wiki" "$SUMMARY"
edit "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further (V)" "$PAGES/This_Deal_Is_Getting_Worse_All_The_Time___Pray_I_Don't_Alter_It_Any_Further_(V).wiki" "$SUMMARY"
edit "This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further (V) (Dark)" "$PAGES/This_Deal_Is_Getting_Worse_All_The_Time___Pray_I_Don't_Alter_It_Any_Further_(V)_(Dark).wiki" "$SUMMARY"
edit "Twin Suns Of Tatooine / Well Trained In The Jedi Arts" "$PAGES/Twin_Suns_Of_Tatooine___Well_Trained_In_The_Jedi_Arts.wiki" "$SUMMARY"
edit "Watch Your Step / This Place Can Be A Little Rough" "$PAGES/Watch_Your_Step___This_Place_Can_Be_A_Little_Rough.wiki" "$SUMMARY"
edit "We Have A Plan / They Will Be Lost And Confused" "$PAGES/We_Have_A_Plan___They_Will_Be_Lost_And_Confused.wiki" "$SUMMARY"
edit "We'll Handle This / Duel Of The Fates" "$PAGES/We'll_Handle_This___Duel_Of_The_Fates.wiki" "$SUMMARY"
edit "Yavin 4 Base Operations / The Time To Fight Is Now" "$PAGES/Yavin_4_Base_Operations___The_Time_To_Fight_Is_Now.wiki" "$SUMMARY"
edit "Yavin 4 Base Operations / The Time To Fight Is Now (Virtual Set 8)" "$PAGES/Yavin_4_Base_Operations___The_Time_To_Fight_Is_Now_(Virtual_Set_8).wiki" "$SUMMARY"
edit "You Can Either Profit By This... / Or Be Destroyed" "$PAGES/You_Can_Either_Profit_By_This...___Or_Be_Destroyed.wiki" "$SUMMARY"
edit "Zero Hour / Liberation Of Lothal" "$PAGES/Zero_Hour___Liberation_Of_Lothal.wiki" "$SUMMARY"
edit "Zero Hour / Liberation Of Lothal (Virtual Set 19)" "$PAGES/Zero_Hour___Liberation_Of_Lothal_(Virtual_Set_19).wiki" "$SUMMARY"

echo "== FlaggedRevs reviewAllPages =="
docker exec swccg_wiki php /var/www/html/extensions/FlaggedRevs/maintenance/reviewAllPages.php --username=Admin 2>&1 | tee /tmp/obj-dual-fr.log | tail -30

echo "== purgePage (edited + spot-checks) =="
docker exec -i swccg_wiki php maintenance/run.php purgePage <<'EOFPURGE'
A Great Tactician Creates Plans / The Result Is Often Resentment
A Great Tactician Creates Plans / The Result Is Often Resentment (Dark)
A Stunning Move / A Valuable Hostage
A Stunning Move / A Valuable Hostage (Dark)
Agents In The Court / No Love For The Empire
Agents Of Black Sun / Vengeance Of The Dark Prince
Bring Him Before Me / Take Your Father's Place
Carbon Chamber Testing / My Favorite Decoration
City In The Clouds / You Truly Belong Here With Us
Court Of The Vile Gangster / I Shall Enjoy Watching You Die
Dantooine Base Operations / More Dangerous Than You Realize
Diplomatic Mission To Alderaan / A Weakness Can Be Found
Diplomatic Mission To Alderaan / A Weakness Can Be Found (Virtual Set 3)
Endor Operations / Imperial Outpost
He Is The Chosen One / He Will Bring Balance
He Is The Chosen One / He Will Bring Balance (Virtual Set 8)
Hidden Base / Systems Will Slip Through Your Fingers
Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe
Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe (V)
Hunt Down And Destroy The Jedi / Their Fire Has Gone Out Of The Universe (V) (Dark)
Hunt For The Droid General / He's A Coward
Hunt For The Droid General / He's A Coward (Virtual Set 21)
I Want That Map / And Now You'll Give It To Me
I Want That Map / And Now You'll Give It To Me (Dark)
ISB Operations / Empire's Sinister Agents
Imperial Entanglements / No One To Stop Us This Time
Imperial Entanglements / No One To Stop Us This Time (Dark)
Imperial Occupation / Imperial Control
Invasion / In Complete Control
Let Them Make The First Move / At Last We Will Have Revenge
Local Uprising / Liberation
Massassi Base Operations / One In A Million
Mind What You Have Learned / Save You It Can
Mind What You Have Learned / Save You It Can (V)
Mind What You Have Learned / Save You It Can (V) (Virtual Set 25)
My Kind Of Scum / Fearless And Inventive
My Lord, Is That Legal? / I Will Make It Legal
No Money, No Parts, No Deal! / You're A Slave?
Old Allies / We Need Your Help
Old Allies / We Need Your Help (Virtual Set 4)
On The Verge Of Greatness / Taking Control Of The Weapon
On The Verge Of Greatness / Taking Control Of The Weapon (Dark)
Plead My Case To The Senate / Sanity And Compassion
Quiet Mining Colony / Independent Operation
Ralltiir Operations / In The Hands Of The Empire
Rebel Strike Team / Garrison Destroyed
Rescue The Princess / Sometimes I Amaze Even Myself
Rescue The Princess / Sometimes I Amaze Even Myself (V)
Rescue The Princess / Sometimes I Amaze Even Myself (V) (Virtual Set 15)
Shadow Collective / You Know Who I Answer To
Shadow Collective / You Know Who I Answer To (Dark)
The Empire Knows We're Here / Prepare For Ground Assault
The Empire Knows We're Here / Prepare For Ground Assault (Virtual Set 22)
The First Order Reigns / The Resistance Is Doomed
The First Order Reigns / The Resistance Is Doomed (Dark)
The Galaxy May Need A Legend / We Need Luke Skywalker
The Galaxy May Need A Legend / We Need Luke Skywalker (Virtual Set 11)
The Hidden Path / Gather Allies And Train
The Hidden Path / Gather Allies And Train (Virtual Set 26)
The Hyperdrive Generator's Gone / We'll Need A New One
The Hyperdrive Generator's Gone / We'll Need A New One (V)
The Hyperdrive Generator's Gone / We'll Need A New One (V) (Virtual Set 10)
The Shield Will Be Down In Moments / Imperial Troops Have Entered The Base!
The Shield Will Be Down In Moments / Imperial Troops Have Entered The Base! (AI)
The Shield Will Be Down In Moments / Imperial Troops Have Entered The Base! (AI) (Dark)
The Shield Will Be Down In Moments / Imperial Troops Have Entered The Base! (Dark)
There Is Good In Him / I Can Save Him
They Have No Idea We're Coming / Until We Win, Or The Chances Are Spent
They Have No Idea We're Coming / Until We Win, Or The Chances Are Spent (Virtual Set 9)
This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further
This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further (V)
This Deal Is Getting Worse All The Time / Pray I Don't Alter It Any Further (V) (Dark)
Twin Suns Of Tatooine / Well Trained In The Jedi Arts
Watch Your Step / This Place Can Be A Little Rough
We Have A Plan / They Will Be Lost And Confused
We'll Handle This / Duel Of The Fates
Yavin 4 Base Operations / The Time To Fight Is Now
Yavin 4 Base Operations / The Time To Fight Is Now (Virtual Set 8)
You Can Either Profit By This... / Or Be Destroyed
Zero Hour / Liberation Of Lothal
Zero Hour / Liberation Of Lothal (Virtual Set 19)
Set Your Course For Alderaan / The Ultimate Power In The Universe
HoloNet Transmission
Attack Run
Template:Card
EOFPURGE

echo "== DONE obj-dual-face-rollout (81 pages); CacheEpoch untouched =="
