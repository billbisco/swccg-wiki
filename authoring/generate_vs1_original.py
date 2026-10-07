# -*- coding: utf-8 -*-
from pathlib import Path

wiki = Path(r"C:\Users\gythe\.grok\worktrees\gythe-gemp-swccg-dev\code-swccg1\wiki")
out_cards = wiki / "pages" / "original-vs1"
out_hubs = wiki / "pages" / "set-hubs"
out_cards.mkdir(parents=True, exist_ok=True)

SRC_PDF = "https://res.starwarsccg.org/legacyblocks/VirtualCards1Premium.pdf"
SRC_SLIPS = "https://www.starwarsccg.org/resources/virtual-slips/"
SET = "Virtual Set 1 (Original)"
SET_BAND = "Virtual"

# Icon expansions for readable ASCII game text (from Premium PDF ICON KEY)
# ▲ = Take into hand from Reserve Deck; reshuffle.
# ▼ = Deploy on table from Reserve Deck; reshuffle.
# P X = Adds X to power of anything he/she pilots + Pilot icon (unless otherwise specified)
# A = Immune to Alter.

def esc(s: str) -> str:
    return (s.replace("&", "&amp;")
             .replace("<", "&lt;")
             .replace(">", "&gt;"))

# Cards: page_title, display_title, image, side, type, subtype, subtype_link, model,
# rarity from Decipher, uniqueness, destiny/power/ability/deploy/forfeit/maneuver/hyperspeed/icons from Decipher,
# lore from Decipher, game_text from slip (readable), decipher_link, hatnote extras, card_uid
CARDS = []

def add(**kw):
    CARDS.append(kw)

add(
    sort="01", num="0•1", file="VS1P-01-Bo-Shek.png",
    page="Bo Shek (V) (Virtual Set 1 Original)", title="Bo Shek (V)",
    side="Light", type_="Character", subtype="Alien", subtype_link="Alien",
    rarity="U1", rarity_link="Rarity#Uncommon", uniqueness="Unique",
    destiny="1", power="2", ability="4", deploy="4", forfeit="3", landspeed="1",
    icons="[[Alien]] [[Pilot]]",
    lore="Rogue pilot. Outlaw starship tech. Has secret lab in Mos Eisley. He bragged about beating Han Solo's Kessel Run record. Left fringe life behind after meeting Obi-Wan Kenobi.",
    game_text="[P] 3. Deploys -2 to any docking bay, starship or Cantina. Considered \"matching pilot\" for any starship. Twice per game, may take a device into hand from Reserve Deck; reshuffle. Immune to attrition &lt; 3.",
    game_text_note="Slip icons expanded: [P] = Adds X to power of anything he/she pilots (and counts as Pilot). Triangle search = take into hand from Reserve Deck; reshuffle. Source slip: VirtualCards1Premium.pdf.",
    decipher="[[BoShek]]",
    hatnote="Decipher printing: [[BoShek]]. Other Virtual versions may exist under different set hubs.",
)

add(
    sort="02", num="0•2", file="VS1P-02-Fusion-Generator-Supply-Tanks.png",
    page="Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)", title="Fusion Generator Supply Tanks (V)",
    side="Light", type_="Device", subtype="", subtype_link="",
    rarity="C2", rarity_link="Rarity#Common", uniqueness="Unrestricted",
    destiny="4", icons="[[Device]]",
    lore="Uses standard fusion technology. Provides starships with energy for hyperspace travel. Installed at docking bays and throughout the Outer Rim Territories.",
    game_text="Deploy on a docking bay or your capital starship. Your unique (*) starships are power, maneuver, and hyperspeed +1. May place this card in Lost Pile to cancel Lateral Damage. Place in Used Pile if opponent controls this location.",
    game_text_note="(*) = unique bullet on slip. Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Fusion Generator Supply Tanks]]",
    hatnote="Decipher printing: [[Fusion Generator Supply Tanks]]. For the Dark Side Virtual Original slip see [[Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)]].",
)

add(
    sort="03", num="0•3", file="VS1P-03-Gold-1.png",
    page="Gold 1 (V) (Virtual Set 1 Original)", title="Gold 1 (V)",
    side="Light", type_="Starship", subtype="Starfighter", subtype_link="Starfighter", model="Y Wing",
    rarity="R2", rarity_link="Rarity#Rare", uniqueness="Unique",
    destiny="3", power="2", deploy="1", forfeit="3", maneuver="3", hyperspeed="4",
    icons="[[Starship]] [[Nav Computer]] [[Scomp Link]]",
    lore="Lead fighter of Gold Squadron at Battle of Yavin. Flown by Jon 'Dutch' Vander. Designated Specter 1 at Renforra Base.",
    game_text="May add 2 pilots or passengers. Once per control phase, may use 1 Force (free if Dutch aboard) to take the top or bottom card of your Force Pile into hand. Power +2 and immune to attrition &lt; 4 while Dutch piloting.",
    game_text_note="Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Gold 1]]",
    hatnote="Decipher printing: [[Gold 1]].",
)

add(
    sort="04", num="0•4", file="VS1P-04-Hans-Heavy-Blaster-Pistol.png",
    page="Han's Heavy Blaster Pistol (V) (Virtual Set 1 Original)", title="Han's Heavy Blaster Pistol (V)",
    side="Light", type_="Weapon", subtype="Character", subtype_link="Character Weapon",
    rarity="R2", rarity_link="Rarity#Rare", uniqueness="Unique",
    destiny="2", icons="[[Weapon]]",
    lore="BlasTech DL-44 heavy pistol. Short range, but relatively powerful. Carries energy for 25 shots. Illegal or restricted on most systems.",
    game_text="Deploy on Han (except TK-422), even as a 'react'. May target a character for free. Draw destiny. Target hit (opponent loses 1 Force) and its forfeit = 0, if destiny +1 &gt; defense value. May fire once during your control phase for 1 Force.",
    game_text_note="Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Han's Heavy Blaster Pistol]]",
    hatnote="Decipher printing: [[Han's Heavy Blaster Pistol]].",
)

add(
    sort="05", num="0•5", file="VS1P-05-Luke-Skywalker.png",
    page="Luke Skywalker (V) (Virtual Set 1 Original)", title="Luke Skywalker (V)",
    side="Light", type_="Character", subtype="Rebel", subtype_link="Rebel",
    rarity="R1", rarity_link="Rarity#Rare", uniqueness="Unique",
    destiny="1", power="3", ability="4", deploy="3", forfeit="7", landspeed="1",
    icons="[[Rebel]] [[Pilot]] [[Warrior]]",
    lore="Son of Anakin Skywalker. Student of Obi-Wan Kenobi. Honed piloting skills while bullseyeing womp rats in Beggar's Canyon aboard T-16 skyhopper.",
    game_text="[P] 3. Adds 3 to Attack Run total if piloting lead starfighter. If piloting at a battleground during your control phase, you may retrieve 1 Force or take Darklighter Spin into hand from Reserve Deck; reshuffle.",
    game_text_note="Slip icons expanded: [P] = Adds X to power of anything he/she pilots (and counts as Pilot). Triangle search expanded in text. Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Luke Skywalker]]",
    hatnote="Decipher printing: [[Luke Skywalker]]. Do not confuse with later Virtual Block / Modern [[Luke Skywalker (V)]] printings.",
)

add(
    sort="06", num="0•6", file="VS1P-06-Saitorr-Kal-Fas.png",
    page="Sai'torr Kal Fas (V) (Virtual Set 1 Original)", title="Sai'torr Kal Fas (V)",
    side="Light", type_="Effect", subtype="", subtype_link="",
    rarity="C2", rarity_link="Rarity#Common", uniqueness="Unrestricted",
    destiny="4", icons="[[Effect]]",
    lore="Saurin female from planet Durkteel. Bodyguard of Hrchek, a Saurin droid trader. Sai'torr will teach battle skills to those who prove themselves worthy.",
    game_text="Deploy on table. Once per deploy phase, if you just deployed a unique (*) character, you may deploy a \"matching weapon\" on that character from Reserve Deck; reshuffle. (Immune to Alter.)",
    game_text_note="Slip shows Immune-to-Alter mark (A). Triangle-down expanded as deploy from Reserve Deck; reshuffle (Premium ICON KEY). Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Sai'torr Kal Fas]]",
    hatnote="Decipher printing: [[Sai'torr Kal Fas]] (Light Effect).",
)

add(
    sort="07", num="0•7", file="VS1P-07-Assault-Rifle.png",
    page="Assault Rifle (V) (Virtual Set 1 Original)", title="Assault Rifle (V)",
    side="Dark", type_="Weapon", subtype="Character", subtype_link="Character Weapon",
    rarity="R2", rarity_link="Rarity#Rare", uniqueness="Unrestricted",
    destiny="2", icons="[[Weapon]]",
    lore="BlasTech model DLT-19 'heavy blaster rifle.' Enhanced with extra power packagedProduct and greater range.",
    game_text="Deploy on any Imperial warrior or Chief Bast. May fire during a battle or attack at same or adjacent site. May target a character, creature or vehicle for 1 Force. Draw destiny. Target immediately lost if destiny +1 &gt; defense value.",
    game_text_note="Source slip: VirtualCards1Premium.pdf. Decipher lore kept as printed on wiki base page (including 'packagedProduct' OCR quirk on base page).",
    decipher="[[Assault Rifle]]",
    hatnote="Decipher printing: [[Assault Rifle]].",
)

add(
    sort="08", num="0•8", file="VS1P-08-Black-2.png",
    page="Black 2 (V) (Virtual Set 1 Original)", title="Black 2 (V)",
    side="Dark", type_="Starship", subtype="Starfighter", subtype_link="Starfighter", model="Tie Ln",
    rarity="R1", rarity_link="Rarity#Rare", uniqueness="Unique",
    destiny="2", power="1", deploy="1", forfeit="3", maneuver="4",
    icons="[[Starship]]",
    lore="TIE/ln assigned to pilot DS-61-2. Has 27 'flames' on cockpit, one for each Rebel kill. Control yoke has a holo of Mithels' young son, Rejili.",
    game_text="May add 1 pilot. During your deploy phase, may take one Pride Of The Empire into hand from Reserve Deck; reshuffle. Organized Attack and All Wings Report In may not be played. Immune to attrition &lt; 5 while DS-61-2 piloting.",
    game_text_note="Slip prints NO HYPERSPEED. Triangle search expanded. Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Black 2]]",
    hatnote="Decipher printing: [[Black 2]].",
)

add(
    sort="09", num="0•9", file="VS1P-09-Blaster-Rack.png",
    page="Blaster Rack (V) (Virtual Set 1 Original)", title="Blaster Rack (V)",
    side="Light", type_="Effect", subtype="", subtype_link="",
    rarity="U1", rarity_link="Rarity#Uncommon", uniqueness="Unrestricted",
    destiny="3", icons="[[Effect]]",
    lore="Imperial facilities like the Death Star and garrison bases have blaster racks at key locations to equip soldiers with weapons like blaster rifles and thermal detonators.",
    game_text="Deploy on table. Once per deploy phase, if you just deployed a unique (*) character, you may deploy a \"matching weapon\" on that character from Reserve Deck; reshuffle. (Immune to Alter.)",
    game_text_note="Alpha1 inventory marks this slip Light Side. Decipher [[Blaster Rack]] is Dark Side Effect; lore/destiny taken from that Decipher page. Slip Immune-to-Alter mark expanded. Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Blaster Rack]]",
    hatnote="Decipher printing: [[Blaster Rack]] (Dark Effect). Virtual Original inventory side: Light (Alpha1).",
)

add(
    sort="10", num="0•10", file="VS1P-10-Darth-Vader.png",
    page="Darth Vader (V) (Virtual Set 1 Original)", title="Darth Vader (V)",
    side="Dark", type_="Character", subtype="Imperial", subtype_link="Imperial",
    rarity="R1", rarity_link="Rarity#Rare", uniqueness="Unique",
    destiny="1", power="6", ability="6", deploy="6", forfeit="8", landspeed="1",
    icons="[[Imperial]] [[Pilot]] [[Warrior]]",
    lore="Dark Lord of the Sith. Servant of Emperor's. Encased in armor with cybernetic life support. Student of Obi-Wan Kenobi. Was the best starpilot in the galaxy. Cunning warrior.",
    game_text="[P] 4. While aboard a starship, it is immune to attrition &lt; 5. Once per battle at same system (twice if with a Black Squadron pilot), may subtract 3 from a just drawn destiny. Immune to attrition &lt; 5.",
    game_text_note="Slip also labels DARK JEDI. [P] expanded per Premium ICON KEY. Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Darth Vader]]",
    hatnote="Decipher printing: [[Darth Vader]].",
)

add(
    sort="11", num="0•11", file="VS1P-11-Fusion-Generator-Supply-Tanks.png",
    page="Fusion Generator Supply Tanks (V) (Dark) (Virtual Set 1 Original)", title="Fusion Generator Supply Tanks (V)",
    side="Dark", type_="Device", subtype="", subtype_link="",
    rarity="C2", rarity_link="Rarity#Common", uniqueness="Unrestricted",
    destiny="4", icons="[[Device]]",
    lore="Installed at many facilities throughout the Empire to provide power to the Imperial spacefleet. Supplies starships with energy necessary for sublight and hyperspace travel.",
    game_text="Deploy on a docking bay or your capital starship. Star Destroyers and unique (*) TIEs are immune to attrition &lt; 3. May place this card in Lost Pile to cancel Power Pivot or Hyper Escape. Place in Used Pile if opponent controls this location.",
    game_text_note="(*) = unique bullet on slip. Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Fusion Generator Supply Tanks (Dark)]]",
    hatnote="Decipher printing: [[Fusion Generator Supply Tanks (Dark)]]. For the Light Side Virtual Original slip see [[Fusion Generator Supply Tanks (V) (Virtual Set 1 Original)]].",
)

add(
    sort="12", num="0•12", file="VS1P-12-Prophetess.png",
    page="Prophetess (V) (Virtual Set 1 Original)", title="Prophetess (V)",
    side="Dark", type_="Character", subtype="Alien", subtype_link="Alien",
    rarity="U1", rarity_link="Rarity#Uncommon", uniqueness="Unique",
    destiny="2", power="1", ability="4", deploy="3", forfeit="2", landspeed="1",
    icons="[[Alien]]",
    lore="Renowned female psychic. Predictor of doom. Agent for Governor Aryon of Tatooine. Tailed Jabba and his thugs to Docking Bay 94 when they confronted Han Solo.",
    game_text="Deploy -1 and forfeit +3 at a site. Once per turn, you may peek at the top card of opponent's Used Pile or Reserve Deck; you may then reshuffle. Immune to attrition &lt; 3.",
    game_text_note="Source slip: VirtualCards1Premium.pdf.",
    decipher="[[Prophetess]]",
    hatnote="Decipher printing: [[Prophetess]].",
)

# Fix assault rifle lore - remove packagedProduct quirk, use cleaned lore from Decipher intent
for c in CARDS:
    if c["sort"] == "07":
        c["lore"] = "BlasTech model DLT-19 heavy blaster rifle. Enhanced with extra power and greater range."
        c["game_text_note"] = "Source slip: VirtualCards1Premium.pdf."

# nav links
for i, c in enumerate(CARDS):
    c["prev"] = CARDS[i-1]["page"] if i else ""
    c["next"] = CARDS[i+1]["page"] if i+1 < len(CARDS) else ""

def card_wikitext(c):
    uid = f"vs1o|{c['sort']}|{c['file']}"
    lines = [
        "{{Card",
        f"|title={c['title']}",
        f"|card_uid={uid}",
        f"|image={c['file']}",
        f"|side={c['side']}",
        f"|type={c['type_']}",
    ]
    if c.get("subtype"):
        lines.append(f"|subtype={c['subtype']}")
        lines.append(f"|subtype_link={c['subtype_link']}")
    if c.get("model"):
        lines.append(f"|model={c['model']}")
    lines += [
        f"|set={SET}",
        f"|rarity={c['rarity']}",
        f"|rarity_link={c['rarity_link']}",
        f"|uniqueness={c['uniqueness']}",
        f"|destiny={c['destiny']}",
    ]
    for k in ("power", "ability", "deploy", "forfeit", "armor", "maneuver", "hyperspeed", "landspeed", "icons"):
        if c.get(k):
            lines.append(f"|{k}={c[k]}")
    lines += [
        "|version_label=virtual",
        f"|set_band={SET_BAND}",
    ]
    if c.get("prev"):
        lines.append(f"|prev={c['prev']}")
    if c.get("next"):
        lines.append(f"|next={c['next']}")
    lines += [
        f"|lore={c['lore']}",
        f"|game_text={c['game_text']}",
        f"|game_text_note={c['game_text_note']}",
        f"|printings='''{SET}''' (Virtual Set #1 Premium Edition slip {c['num']}) &mdash; this page",
        f"|sources=* [{SRC_PDF} VirtualCards1Premium.pdf] at res.starwarsccg.org/legacyblocks &mdash; Virtual Set #1 Premium Edition slip {c['num']}",
        f"* [{SRC_SLIPS} Virtual slips] at starwarsccg.org &mdash; Legacy Blocks inventory (naming)",
        f"* Decipher base: {c['decipher']}",
        f"|hatnote={c['hatnote']}",
        "|notes=Virtual Original-era printable slip (2002 Premium Edition). Overlay for the cited Decipher card. Not valid for current Standard / Modern Virtual play.",
        "}}",
        "",
        "[[Category:Virtual Original sets]]",
        "",
    ]
    return "\n".join(lines)

# Write cards
for c in CARDS:
    safe = c["page"].replace(" ", "_").replace("'", "")
    # keep apostrophe in Sai'torr filename carefully
    fname = c["page"].replace(" ", "_") + ".wiki"
    # MediaWiki titles with apostrophe are fine; file names:
    fname = (
        c["page"]
        .replace(" ", "_")
        .replace("'", "")
        + ".wiki"
    )
    # Actually keep consistent mapping
    mapping = {
        "01": "Bo_Shek_(V)_(Virtual_Set_1_Original).wiki",
        "02": "Fusion_Generator_Supply_Tanks_(V)_(Virtual_Set_1_Original).wiki",
        "03": "Gold_1_(V)_(Virtual_Set_1_Original).wiki",
        "04": "Hans_Heavy_Blaster_Pistol_(V)_(Virtual_Set_1_Original).wiki",
        "05": "Luke_Skywalker_(V)_(Virtual_Set_1_Original).wiki",
        "06": "Saitorr_Kal_Fas_(V)_(Virtual_Set_1_Original).wiki",
        "07": "Assault_Rifle_(V)_(Virtual_Set_1_Original).wiki",
        "08": "Black_2_(V)_(Virtual_Set_1_Original).wiki",
        "09": "Blaster_Rack_(V)_(Virtual_Set_1_Original).wiki",
        "10": "Darth_Vader_(V)_(Virtual_Set_1_Original).wiki",
        "11": "Fusion_Generator_Supply_Tanks_(V)_(Dark)_(Virtual_Set_1_Original).wiki",
        "12": "Prophetess_(V)_(Virtual_Set_1_Original).wiki",
    }
    path = out_cards / mapping[c["sort"]]
    text = card_wikitext(c)
    # ascii check
    assert all(ord(ch) < 128 or ch in "" for ch in text) or True
    non = [ch for ch in text if ord(ch) > 127]
    if non:
        # replace leftover bullets
        for a,b in {"•": "*", "–": "-", "—": " - ", "’": "'", "“": '"', "”": '"'}.items():
            text = text.replace(a,b)
        non = [ch for ch in text if ord(ch) > 127]
    assert not non, non
    path.write_bytes(text.encode("utf-8"))
    print("card", c["sort"], path.name)

# Hub
def thumb_row(c):
    return (
        f"| [[File:{c['file']}|200px|link={c['page']}]] || [[{c['page']}|{c['title']}]] || "
        f"{c['type_']} || {c['num']} || {c['side']} ||"
    )

ls = [c for c in CARDS if c["side"] == "Light"]
ds = [c for c in CARDS if c["side"] == "Dark"]

hub = f"""'''Note:''' '''Virtual Original''' hub for '''Virtual Set #1 Premium Edition''' (2002). These are printable slip modifiers for Decipher cards. '''Not''' the post-2014 [[Virtual Set 1]]. Defensive Shields as a Virtual Set are deferred (not this pilot).

{{| class="wikitable expansion-infobox"
! colspan="2" | Virtual Set 1 (Original)
|-
| colspan="2" style="text-align:center;" | [[File:Set-VS1O-title.png|260px]]
|-
! Game/Set
|| Star Wars CCG
|-
! Expansion
|| Virtual Set #1 Premium Edition
|-
! Publisher
|| Star Wars CCG Players Committee
|-
! Era
|| [[:Category:Virtual Original sets|Virtual Original]] (2002&ndash;2009)
|-
! Date
|| Legal '''9 March 2002''' (community); Premium slip sheet dated PC 2002
|-
! Cards Total
|| 12 slips
|-
! Slip PDF
|| [{SRC_PDF} VirtualCards1Premium.pdf]
|}}

'''Virtual Set 1 (Original)''' is the Players Committee '''Virtual Set #1 Premium Edition''' printable slip sheet. Cutouts overlay Decipher cards. Pack art: '''none''' sourced from the Premium PDF / CDN / virtual-slips (CF-blocked); hub uses a creative placeholder banner (`Set-VS1O-title.png`).

Overview era: [[Virtual Sets (2002-2009)]]. History: [[History of the Players Committee]].

== Card list ==

=== [[Light|Light Side]] ===
{{| class="wikitable card-thumbs"
! Image !! Card !! Type !! # !! Side
|-
"""
for c in ls:
    hub += thumb_row(c) + "\n|-\n"
if hub.endswith("|-\n"):
    hub = hub[:-3]
hub += "|}\n\n=== [[Dark|Dark Side]] ===\n{| class=\"wikitable card-thumbs\"\n! Image !! Card !! Type !! # !! Side\n|-\n"
for c in ds:
    hub += thumb_row(c) + "\n|-\n"
if hub.endswith("|-\n"):
    hub = hub[:-3]
hub += """|}

== Sources ==
* [""" + SRC_PDF + """ VirtualCards1Premium.pdf] at res.starwarsccg.org/legacyblocks &mdash; Virtual Set #1 Premium Edition (slip images for this hub)
* [""" + SRC_SLIPS + """ Virtual slips] at starwarsccg.org &mdash; Legacy Blocks tab (inventory / naming help; page may be Cloudflare-gated)
* [[Virtual Sets (2002-2009)]] &mdash; pre-reorg overview
* Slip crops: Alpha1 300 DPI extracts <code>VS1P-01</code>&hellip;<code>VS1P-12</code>

== References ==
<references />

[[Category:Virtual Original sets]]
[[Category:Sets]]
"""
# Fix hub table opener - I used {{| which in normal string is {{|
# In the f-string above I used {{| which becomes {|
# But later I appended {| with escaped quotes - good

# Actually first table used {{| in f-string - good
# Second section I started with {| in a regular string concat - the hub string after ls loop uses {| - need to verify

for a,b in {"•": "*", "–": "-", "—": " - ", "…": "...", "’": "'", "“": '"', "”": '"', "\ufeff": ""}.items():
    hub = hub.replace(a,b)
# ensure {| not {{|
hub = hub.replace("{{|", "{|")
(out_hubs / "Virtual_Set_1_(Original).wiki").write_bytes(hub.encode("utf-8"))
print("hub bytes", (out_hubs / "Virtual_Set_1_(Original).wiki").stat().st_size)
print("hub nonascii", sum(1 for c in hub if ord(c)>127))

# Main Page: upgrade VS1 Original tile to use pack art if present as text tile
main = (wiki / "pages" / "Main_Page.wiki").read_text(encoding="utf-8")
old = '<div class="set-tile"><span class="set-name">[[Virtual Set 1 (Original)|VS1 Legacy]]</span><span class="set-meta">9 Mar 2002</span></div>'
# current tile from earlier build
import re
pat = re.compile(r'<div class="set-tile"><span class="set-name">\[\[Virtual Set 1 \(Original\)\|[^\]]+\]\]</span><span class="set-meta">[^<]+</span></div>')
new = '<div class="set-tile">[[File:Set-VS1O-title.png|142px|link=Virtual Set 1 (Original)]]<span class="set-name">[[Virtual Set 1 (Original)|VS1 Premium]]</span><span class="set-meta">9 Mar 2002 &middot; 12</span></div>'
main2, n = pat.subn(new, main, count=1)
if n != 1:
    # try exact from build
    alt = '<div class="set-tile"><span class="set-name">[[Virtual Set 1 (Original)|VS1 Legacy]]</span>'
    if "[[Virtual Set 1 (Original)|VS1 " in main:
        main2 = re.sub(
            r'<div class="set-tile"><span class="set-name">\[\[Virtual Set 1 \(Original\)\|VS1 [^\]]+\]\]</span><span class="set-meta">[^<]*</span></div>',
            new,
            main,
            count=1,
        )
        n = 1 if main2 != main else 0
print("main tile replace", n)
if n == 1:
    (wiki / "pages" / "Main_Page.wiki").write_bytes(main2.encode("utf-8"))

# title map for apply
(wiki / "original-vs1" / "title_map.txt").parent.mkdir(exist_ok=True)
with open(wiki / "original-vs1" / "title_map.txt", "w", encoding="utf-8") as f:
    for c in CARDS:
        f.write(f"{c['sort']}|{c['page']}|{mapping[c['sort']]}|{c['file']}\n")
print("DONE generate", len(CARDS))