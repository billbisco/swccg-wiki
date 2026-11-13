import json,re,sys
from pathlib import Path
sys.path.insert(0,'../luke-family-pilot')
sys.path.insert(0,'../work-board-authors/evidence/367')
import style_lint
ROOT=Path(__file__).resolve().parent
p=json.loads((ROOT/'live-before.json').read_text(encoding='utf8'))
def src(t):return p[t].get('revisions',[{}])[0].get('slots',{}).get('main',{}).get('content','')
encyc='[https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf SWCCG Collecting Encyclopedia 3.2], pp. 5, 20–22, 34–35, 39–41, 48. Preserved copy: [https://web.archive.org/web/20261008192828/https://res.starwarsccg.org/Resources/Star_Wars_CCG_Collecting_Encyclopedia_3.2.pdf Internet Archive].'
check='[https://res.starwarsccg.org/Resources/swccgcardlist4.0.pdf Complete Card List v4.0], pp. 29–32. Preserved copy: [https://web.archive.org/web/20261009184033/https://res.starwarsccg.org/Resources/swccgcardlist4.0.pdf Internet Archive].'
collection='[http://www.decipher.com/starwars/productlibrary/thecollection/index.html Star Wars CCG: The Expansions], Decipher. Preserved copy: [https://web.archive.org/web/19990504174938/http://www.decipher.com/starwars/productlibrary/thecollection/index.html Internet Archive] (4 May 1999).'
japan='[http://www.decipher.com/newsandhighlights/japancoolstory.html Star Wars CCG in Japan], Rich Loftus, Decipher (1 April 1997). Preserved copy: [https://web.archive.org/web/19970607092233/http://www.decipher.com/newsandhighlights/japancoolstory.html Internet Archive].'
overview="""{{Set infobox
|name=Premiere
|image=Premiere-Limited-box-encyc.png
|publisher=[[Decipher]]; Japanese edition with [[Takara]]
|era=[[Decipher era|Decipher Era]]
|released=December 1995 (Limited)
|cards=324 original cards (162 Light, 162 Dark)
|language=English; Japanese
|related=[[Premiere Limited]] · [[Premiere Unlimited]] · [[Premiere (Japanese)|Premiere Japanese]]
}}

For the constructed format, see [[Premiere (format)]].

'''Premiere''' is the first expansion of Star Wars Customizable Card Game, published by [[Decipher]] in December 1995. Its 324-card pool appeared in English [[Premiere Limited|Limited]] and [[Premiere Unlimited|Unlimited]] editions and in [[Premiere (Japanese)|Japanese]].<ref name="collection">COLLECTION</ref><ref name="japan">JAPAN</ref> The '''Premiere expansion family''' connects those editions with later reprints, promotional printings and [[Errata|errata]] of its cards.

== Editions ==
{| class="wikitable"
! Edition !! Release !! Language and border !! Cards and card list
|-
| [[Premiere Limited]] || December 1995 || English; black border || [[Premiere Limited#Card list|324 cards]]
|-
| [[Premiere Unlimited]] || February 1996 || English; white border || [[Premiere Unlimited#Card list|324 cards]]
|-
| [[Premiere (Japanese)|Premiere Japanese]] || April 1997 || Japanese; black border || [[Premiere (Japanese)#Card list|324 cards]]
|}
Limited and Unlimited were sold in boosters and starter decks. [[Takara]] published the Japanese edition in Japan.<ref name="collection" /><ref name="japan" /><ref name="encyc">ENCYC</ref>

<gallery widths="180" heights="180">
Premiere-Limited-box-encyc.png|[[Premiere Limited|Limited]]
Premiere-Unlimited-display-transparent.png|[[Premiere Unlimited|Unlimited]]
Premiere-Japanese-box.png|[[Premiere (Japanese)|Japanese]]
</gallery>

== Reprints and related products ==
Premiere cards also appeared in introductory games, anthology products and foil releases. A card's original expansion and the product containing a later printing can therefore differ.

{| class="wikitable"
! Product or program !! Relationship to Premiere !! Examples or further details
|-
| [[Premiere Two-Player Introductory Game]] || White-border Premiere reprints alongside six exclusive cards || [[Premiere Two-Player Introductory Game#Card list|Product card list]]
|-
| [[First Anthology]] || Includes Premiere Unlimited starter decks || Its preview cards are separate from the Premiere pool.
|-
| [[Official Tournament Sealed Deck]] || Includes Premiere Unlimited booster packs || Its fixed premium cards are separate from the Premiere pool.
|-
| [[Second Anthology]] || Includes Premiere Unlimited booster packs || Its preview cards are separate from the Premiere pool.
|-
| [[Enhanced Premiere]] || Includes Premiere Unlimited boosters with new premium characters || [[Luke With Lightsaber]] is a different card from [[Luke Skywalker]].
|-
| [[Reflections]] || Foil reprints of selected earlier cards, including Premiere cards || [[Luke Skywalker (Reflections Foil)|Luke Skywalker foil]]
|-
| [[Reflections II: Expanding the Galaxy|Reflections II]] || Selected foil reprints || Its [[Luke Skywalker, Jedi Knight]] foil reprints the [[Death Star II]] card, not Premiere Luke.
|-
| [[Reflections III]] || Selected foil reprints, including Japanese Premiere cards || [[Luke Skywalker (Japanese Reflections III Foil)|Japanese Luke Skywalker foil]]
|-
| [[Promotional Foils]] || Selected reprints distributed through tournaments and other promotions || [[A Few Maneuvers (Promotional Foil)|A Few Maneuvers]], [[Corellian Corvette (Promotional Foil)|Corellian Corvette]] and [[Rebel Barrier (Promotional Foil)|Rebel Barrier]]
|}
The boxed-product contents are described in Decipher's product library.<ref name="collection" /> The foil checklists distinguish the Reflections printings.<ref name="checklist">CHECK</ref> Promotional distributions included tournament prizes, convention promotions and wrapper redemptions.<ref name="encyc" />

=== Tournament and promotional printings ===
[[Promotional Foils]] includes Premiere reprints such as [[Alter (Light) (Promotional Foil)|Alter]], [[Sense (Light) (Promotional Foil)|Sense]] and [[It Could Be Worse (Promotional Foil)|It Could Be Worse]]. [[Corellian Corvette (Promotional Foil)|Corellian Corvette]] was distributed through more than one promotion. Its different distribution occasions do not make it a different printed card.<ref name="encyc" />

<gallery widths="140" heights="200">
Promo-Foil-L-afewmaneuvers.jpg|[[A Few Maneuvers (Promotional Foil)|A Few Maneuvers]]
Promo-Foil-L-corelliancorvette.jpg|[[Corellian Corvette (Promotional Foil)|Corellian Corvette]]
Promo-Foil-L-rebelbarrier.jpg|[[Rebel Barrier (Promotional Foil)|Rebel Barrier]]
</gallery>

== Errata and later printings ==
Some Premiere cards received [[Errata|Decipher errata]] or later [[Errata|Players Committee errata]]. A later printed card can incorporate revised wording: the [[Luke Skywalker (Reflections Foil)|Reflections Luke foil]] uses “not at a Tatooine site” where the [[Luke Skywalker|original Limited card]] says “present at any non-Tatooine location”.<ref name="luke-faces">Printed faces: [[:File:Premiere-L-lukeskywalker-decipher-archive.gif|Premiere Limited Luke Skywalker]] and [[:File:Luke-Skywalker-Reflections-Foil-PSA.jpg|Reflections Luke Skywalker foil]].</ref>

Each card's Versions navigator connects its printings and errata. A foil's finish and its printed wording are separate features: [[Luke Skywalker (Reflections Foil)|the English Reflections foil]] and [[Luke Skywalker (Japanese Reflections III Foil)|the Japanese Reflections III foil]] have separate publication articles and release contexts.

== Later Virtual adaptations ==
Premiere cards also became underlying cards for [[Virtual Original]], [[Virtual Legacy]] and [[Virtual Modern]] designs. For example, the Premiere [[Luke Skywalker]] family links to [[Luke Skywalker (V) (Virtual Set 1)|Original Virtual Set 1 Luke]], [[Luke Skywalker (V) (Virtual Block 1)|Virtual Block 1 Luke]] and [[Luke Skywalker (V)|Virtual Set 0 Luke]]. These are Virtual publications in their own eras and sets.

== See also ==
* [[Sets]]
* [[Decipher era|Decipher Era]]
* [[Translations of SWCCG]]
* [[Card versions]]

== References ==
<references />

[[Category:Decipher sets]]
""".replace('COLLECTION',collection).replace('JAPAN',japan).replace('ENCYC',encyc).replace('CHECK',check)
# Naming of concept links is checked against live targets before publication.
foil="""{{Card
|title=Luke Skywalker
|publication_id=decipher-reflections-luke-skywalker-foil-en
|image=Luke-Skywalker-Reflections-Foil-PSA.jpg
|image_note=Reflections foil, photographed in a grading holder.
|side=Light
|type=Character
|subtype=Rebel
|subtype_link=Rebel
|set=Reflections
|set_icon=None ([[Premiere|Premiere]])
|publisher=[[Decipher]]
|era=[[Decipher era|Decipher Era]]
|rarity=UR
|rarity_link=Rarity
|uniqueness=Unique
|destiny=1
|power=3
|ability=4
|deploy=3
|forfeit=7
|landspeed=1
|icons=[[Rebel]] [[Pilot]] [[Warrior]]
|extra_info=<tr><th>Finish</th><td>Foil</td></tr><tr><th>Original expansion</th><td>[[Premiere]]</td></tr><tr><th>Publication ID</th><td><code>decipher-reflections-luke-skywalker-foil-en</code></td></tr>
|version_label=Reflections foil
|set_band=Decipher
|navigation=[[Reflections]] · [[Premiere]]
|versions={{Card versions/Luke Skywalker (Premiere)}}
|lead='''Luke Skywalker''' is a [[Light]] [[Character]] — [[Rebel]] released as an ultra-rare foil in [[Reflections]] in January 2000. It is a foil printing of the [[Premiere]] card.<ref name="checklist">CHECK</ref><ref name="encyc">ENCYC</ref>
|lore=Son of Anakin Skywalker. Student of Obi-Wan Kenobi. Honed piloting skills while bullseyeing womp rats in Beggar's Canyon aboard T-16 skyhopper.
|game_text=You may activate 1 extra Force each turn if Luke is not at a Tatooine site. Adds 3 to power of anything he pilots. When piloting Red 5, also adds 2 to maneuver. Immune to attrition &lt; 3.
|errata_history=The foil uses the revised activation condition “not at a Tatooine site”, instead of “present at any non-Tatooine location” on [[Luke Skywalker|Premiere Limited Luke Skywalker]]. It also says “anything he pilots” and “When piloting Red 5” in place of the original “any starship he pilots” and “On Red 5”. The original printing and [[Luke Skywalker (Errata)|Decipher errata]] remain separate articles.<ref name="faces">Printed faces: [[:File:Luke-Skywalker-Reflections-Foil-PSA.jpg|Reflections foil]] and [[:File:Premiere-L-lukeskywalker-decipher-archive.gif|Premiere Limited]].</ref>
|personas=* [[Luke Skywalker (persona)|Luke]]
|characteristics=* Force-Sensitive
* Skywalker
|notes=The Reflections checklist lists this foil as R72 at rarity UR. R72 is a collecting-checklist reference.<ref name="checklist" />
|sources=* Original printed foil face: [[:File:Luke-Skywalker-Reflections-Foil-PSA.jpg|Luke Skywalker, Reflections foil]], PSA certificate 68373908, collector Adam182R.
|has_refs=1
}}
""".replace('CHECK',check).replace('ENCYC',encyc)
nav=src('Template:Card versions/Luke Skywalker (Premiere)')
nav=nav.replace('[[Premiere Limited|Premiere]]','[[Premiere]]',1)
needle='{{Card version link|page=Luke Skywalker (Japanese Reflections III Foil)'
i=nav.index(needle)
nav=nav[:i]+'{{Card version link|page=Luke Skywalker (Reflections Foil)|label=Reflections foil|current={{{current|{{FULLPAGENAME}}}}}}} · <!--\n-->'+nav[i:]
nav=nav.replace('The first live pilot','The live pilot')
guide=src('SWCCG Wiki:Style guide')
addition="""
=== Expansion families and reprint publications (Bill, 13 November 2026) ===
An '''expansion family''' overview uses the expansion's ordinary title, such as [[Premiere]], and links its named editions, later reprints and errata. Preserve separate edition articles such as [[Premiere Limited]], [[Premiere Unlimited]] and [[Premiere (Japanese)]]. Later-product foils retain their actual release product; they are not extra entries in the original expansion's checklist. Underlying cards connect to Virtual successors across eras through their family navigator.

Include a verified tournament or promotional reprint in its originating card family while recording the actual promotional program, publisher and era. Identical copies distributed on several occasions share one publication article with multiple distribution records. Distinguishable official printings retain separate publication identities. Verify the actual face: language, border, finish, copyright and printed text. A generic GEMP foil effect does not establish a historical printing, and a new publication does not automatically need a new gameplay ID.

For migrated families, edit the shared family template once and include it in each member article. Era and set headings are bold, underlined article links. Individual publication labels remain concise; the current article is bold black. Keep an obvious Edit versions link and editing help. Adding a publication requires its article and shared entry in the same batch, followed by checks of every member's membership and current selection.
"""
assert '=== Expansion families and reprint publications' not in guide
guide=guide.replace('== Foreign-language card articles',addition+'\n== Foreign-language card articles',1)
drafts={'Premiere':overview,'Luke Skywalker (Reflections Foil)':foil,'Template:Card versions/Luke Skywalker (Premiere)':nav,'SWCCG Wiki:Style guide':guide}
drafts['File:Luke-Skywalker-Reflections-Foil-PSA.jpg']='''== Summary ==
Original physical [[Luke Skywalker (Reflections Foil)|Luke Skywalker Reflections foil]], photographed in a PSA grading holder, certificate 68373908. [[Decipher]], 2000. The photograph preserves the printed card, including its foil finish and revised wording.

== Source ==
[https://caimages.collectors.com/psaimages/106470/68373908/img20230825_12320377_original.jpg Original photograph], PSA Set Registry / Collectors. Preserved copy: [https://web.archive.org/web/20261113233117/https://caimages.collectors.com/psaimages/106470/68373908/img20230825_12320377_original.jpg Internet Archive].

Card artwork and text copyright Lucasfilm and Decipher; reproduced for identification and historical documentation.
'''
drafts['Talk:Premiere']=src('Talk:Premiere')+'''\n== Expansion-family overview, 13 November 2026 ==
Bill approved the Premiere overview, the term expansion family, inclusion of verified tournament/promotional reprints with their actual program/publisher/era, and the Premiere-plus-Luke first delivery. Edition articles and original set checklists remain separate. Distinguishable physical printings have publication identities; identical copies distributed on several occasions have distribution records. The Luke shared navigator now includes the verified Reflections foil.

=== Unresolved source conflicts ===
Premiere Unlimited: Decipher's product-library collection page dates the edition February 1996; Collecting Encyclopedia 3.2 dates it April 1996 (p. 35 and release list). The overview provisionally follows the primary Decipher date. Existing edition articles disagree on this point and need a separately sourced reconciliation.<ref>COLLECTION</ref><ref>ENCYC</ref>

The Star Wars Collectors Archive's Reflections Luke record has inconsistent year metadata: the 2013 capture says 1995 and the current record says 1999. Neither establishes the Reflections release date. The overview and foil article follow the Reflections product date in the collecting references, January 2000, consistent with the photographed PSA label. The collector archive's photograph could not be downloaded; a separate PSA photograph of the actual foil was obtained and archived instead.<ref>[https://web.archive.org/web/20130622021057/http://theswca.com/index.php?action=disp_item&item_id=45021 Reflections I foil Luke Skywalker], Star Wars Collectors Archive (capture 22 June 2013).</ref><ref>ENCYC</ref>

=== Follow-up ===
This delivery inventories the product/program categories and completes the existing Luke pilot's verified English Reflections foil entry. It does not certify every possible unlocated manufacturing variation or every later PC promotional print. Further Premiere families should be processed in source-verified batches. No tournament-foil Premiere Luke is asserted. ~~~~

== References ==
<references />
'''.replace('COLLECTION',collection).replace('ENCYC',encyc)
drafts['Talk:Luke Skywalker (Reflections Foil)']='''== Reflections foil source audit, 13 November 2026 ==
The actual photographed foil (PSA certificate 68373908) was read independently: unique; destiny 1; power 3; ability 4; deploy 3; forfeit 7; Pilot and Warrior; no expansion symbol; revised game text beginning “You may activate 1 extra Force each turn if Luke is not at a Tatooine site.” Lore matches the photographed card. Landspeed 1 is the character rule default, not a printed number.

The article has a stable publication ID and uses the shared Premiere Luke family navigator. No new numeric GEMP family was allocated and no foil-modifier mapping is advertised. The source scan is retained complete in its grading holder; a cleaner card-only scan can replace its display later without changing this publication identity. The ordinary Japanese and Japanese Reflections III foil remain separate publications. ~~~~
'''
(ROOT/'drafts.json').write_text(json.dumps(drafts,ensure_ascii=False,indent=2),encoding='utf8')
for title,s in drafts.items():
    flags=style_lint.lint(s,title)[0];print(title,len(flags),str(flags)[:1000])
