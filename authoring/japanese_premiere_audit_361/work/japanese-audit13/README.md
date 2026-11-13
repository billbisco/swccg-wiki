# Japanese Premiere audit and verified repairs — Story #361

Completed a coverage audit of all 324 regular Japanese Premiere printings. Published repairs on **164 card articles, the set checklist, and two File descriptions** (167 pages). All changed public reviewed pages match their guarded final text, have zero lint/Cite errors, and retain functioning images.

## Results

- Completed sixteen Japanese game-text/lore entries and their English translations; added missing game/lore translations on Ponda Baba, Overload, Physical Choke and Precise Attack, and title-translation labels on LIN-V8K/Pops.
- Completed Ellorrs Madak's truncated Japanese text and three opposite-side location blocks.
- Corrected four Effect classifications, printed character/ship/vehicle/location symbols, Jawa's variable deploy, Talz's three asterisks and applicable stats. All 37 locations have numeric Force-icon counts; ten systems have verified parsec values. Removed unprinted destiny/deploy defaults from locations.
- Added complete original R4-E1/Tanbris photos without overwriting old frames; verified a source snapshot and both uploaded JPEG Wayback captures byte for byte.
- Fixed 34 bare set-video citations using an opened archived **watch page** and separate preserved card-frame links. This does not claim the archived watch page preserves playable video.
- Reconciled the checklist and retained 323 existing Versions rows verbatim and repaired Reactor Terminal’s malformed row without losing any printing link. No card article was deleted, renamed, merged or newly minted.

## Limits and integration work

[Remaining evidence](remaining-evidence.md) distinguishes coverage from proofreading. Existing fields are present, but this is not a fresh word-for-word certification of every older transcription or a comprehensive subtype rereading. The 135 video-derived filenames form a candidate list for edge inspection/replacement, not 135 proven incomplete scans. Chief Bast's lower-edge uncertainty is stated on the article. Source-verified visible icons are retained without inventing absent symbols or numeric zeros.

All 324 pages still use manual infoboxes. [Recommendations](recommendations.md) are supplied to existing story #287, owned by Alpha1/DatacardGrok; that template migration is not completed by this story. It must rebase its content/category baselines on these revisions.

## Evidence and reproduction

- [324-card manifest](final-manifest.json), [coverage CSV](coverage.csv), [remaining field gaps](remaining-field-gaps.json), [public verification](verification.json), and `navigation-check.json`.
- `changes.diff`, `phase2.diff`, `phase3.diff`, source readings, archive replay hashes, upload/edit receipts, and before/after/diff/desktop/mobile screenshots.
- Reproducible scripts and captured inputs are backed up under `billbisco/swccg-wiki/authoring/japanese_premiere_audit_361/`. From that bundle's root, read-only verification is `python work/japanese-audit13/verify.py` then `python work/japanese-audit13/final-audit.py`. Scripts require Python, requests, BeautifulSoup and Pillow; local screenshots additionally use Playwright and Chrome. Source acquisition uses the documented VPS FlareSolverr endpoint and closes only its own sessions.
- Historical build/publish packets are evidence, **not an instruction to replay stale revisions**. Rebase from live heads before any future write. Publication uses Memory Core ChatGPT's own VPS credential in memory, `bot=1`, revision/hash checks and both edit timestamps. No secrets are committed.

## Editing-method deviation

The legacy card sources use raw HTML headings with no editable section indices; an API rvsection=0 read returns the entire card (section-boundaries.json). The publisher used scoped whole-page writes for changes spanning these infoboxes/body blocks, and an explicit section=0 write for Reactor Terminal. It guarded every write with the exact prior revision and full-text SHA-256 as well as basetimestamp/starttimestamp, stopped on any mismatch, and verified exact final content and preserved family rows afterward. No other editor's concurrent revision was overwritten. This is recorded explicitly rather than claiming the section-edit procedure was used.

## All changed live pages

| Page | Final reviewed revision |
|---|---:|
| [2X-3KPR (Tooex) (Japanese)](https://wiki.swccg.com/wiki/2X-3KPR_(Tooex)_(Japanese)) | 299853 |
| [Beru Lars (Japanese)](https://wiki.swccg.com/wiki/Beru_Lars_(Japanese)) | 299854 |
| [Biggs Darklighter (Japanese)](https://wiki.swccg.com/wiki/Biggs_Darklighter_(Japanese)) | 299855 |
| [BoShek (Japanese)](https://wiki.swccg.com/wiki/BoShek_(Japanese)) | 299856 |
| [C-3PO (See-Threepio) (Japanese)](https://wiki.swccg.com/wiki/C-3PO_(See-Threepio)_(Japanese)) | 299857 |
| [CZ-3 (Seezee-Three) (Japanese)](https://wiki.swccg.com/wiki/CZ-3_(Seezee-Three)_(Japanese)) | 299858 |
| [Dice Ibegon (Japanese)](https://wiki.swccg.com/wiki/Dice_Ibegon_(Japanese)) | 299859 |
| [Dutch (Japanese)](https://wiki.swccg.com/wiki/Dutch_(Japanese)) | 299860 |
| [Figrin D'an (Japanese)](https://wiki.swccg.com/wiki/Figrin_D'an_(Japanese)) | 299861 |
| [General Dodonna (Japanese)](https://wiki.swccg.com/wiki/General_Dodonna_(Japanese)) | 299862 |
| [Han Solo (Japanese)](https://wiki.swccg.com/wiki/Han_Solo_(Japanese)) | 299863 |
| [Jawa (Light) (Premiere) (Japanese)](https://wiki.swccg.com/wiki/Jawa_(Light)_(Premiere)_(Japanese)) | 299864 |
| [Jek Porkins (Japanese)](https://wiki.swccg.com/wiki/Jek_Porkins_(Japanese)) | 299865 |
| [Kabe (Japanese)](https://wiki.swccg.com/wiki/Kabe_(Japanese)) | 299866 |
| [Kal'Falnl C'ndros (Japanese)](https://wiki.swccg.com/wiki/Kal'Falnl_C'ndros_(Japanese)) | 299867 |
| [Leesub Sirln (Japanese)](https://wiki.swccg.com/wiki/Leesub_Sirln_(Japanese)) | 299868 |
| [Leia Organa (Japanese)](https://wiki.swccg.com/wiki/Leia_Organa_(Japanese)) | 299869 |
| [LIN-V8K (Elleyein-Veeatekay) (Japanese)](https://wiki.swccg.com/wiki/LIN-V8K_(Elleyein-Veeatekay)_(Japanese)) | 300033 |
| [Luke Skywalker (Japanese)](https://wiki.swccg.com/wiki/Luke_Skywalker_(Japanese)) | 299871 |
| [Momaw Nadon (Japanese)](https://wiki.swccg.com/wiki/Momaw_Nadon_(Japanese)) | 299872 |
| [Obi-Wan Kenobi (Japanese)](https://wiki.swccg.com/wiki/Obi-Wan_Kenobi_(Japanese)) | 299873 |
| [Owen Lars (Japanese)](https://wiki.swccg.com/wiki/Owen_Lars_(Japanese)) | 299874 |
| [Pops (Japanese)](https://wiki.swccg.com/wiki/Pops_(Japanese)) | 300034 |
| [R2-X2 (Artoo-Extoo) (Japanese)](https://wiki.swccg.com/wiki/R2-X2_(Artoo-Extoo)_(Japanese)) | 299876 |
| [R4-E1 (Arfour-Eeone) (Japanese)](https://wiki.swccg.com/wiki/R4-E1_(Arfour-Eeone)_(Japanese)) | 299980 |
| [Rebel Guard (Japanese)](https://wiki.swccg.com/wiki/Rebel_Guard_(Japanese)) | 299878 |
| [Rebel Pilot (Japanese)](https://wiki.swccg.com/wiki/Rebel_Pilot_(Japanese)) | 299879 |
| [Rebel Trooper (Japanese)](https://wiki.swccg.com/wiki/Rebel_Trooper_(Japanese)) | 299880 |
| [Red Leader (Japanese)](https://wiki.swccg.com/wiki/Red_Leader_(Japanese)) | 299881 |
| [Shistavanen Wolfman (Japanese)](https://wiki.swccg.com/wiki/Shistavanen_Wolfman_(Japanese)) | 299882 |
| [Talz (Japanese)](https://wiki.swccg.com/wiki/Talz_(Japanese)) | 299981 |
| [WED-9-M1 'Bantha' Droid (Japanese)](https://wiki.swccg.com/wiki/WED-9-M1_'Bantha'_Droid_(Japanese)) | 299884 |
| [Wioslea (Japanese)](https://wiki.swccg.com/wiki/Wioslea_(Japanese)) | 299885 |
| [Ellorrs Madak (Japanese)](https://wiki.swccg.com/wiki/Ellorrs_Madak_(Japanese)) | 299886 |
| [K'lor'slug (Japanese)](https://wiki.swccg.com/wiki/K'lor'slug_(Japanese)) | 299887 |
| [Mantellian Savrip (Japanese)](https://wiki.swccg.com/wiki/Mantellian_Savrip_(Japanese)) | 299888 |
| [Rycar Ryjerd (Japanese)](https://wiki.swccg.com/wiki/Rycar_Ryjerd_(Japanese)) | 299889 |
| [Yerka Mig (Japanese)](https://wiki.swccg.com/wiki/Yerka_Mig_(Japanese)) | 299890 |
| [Help Me Obi-Wan Kenobi (Japanese)](https://wiki.swccg.com/wiki/Help_Me_Obi-Wan_Kenobi_(Japanese)) | 300035 |
| [Alderaan (Japanese)](https://wiki.swccg.com/wiki/Alderaan_(Japanese)) | 299892 |
| [Dantooine (Japanese)](https://wiki.swccg.com/wiki/Dantooine_(Japanese)) | 299893 |
| [Death Star: Detention Block Control Room (Japanese)](https://wiki.swccg.com/wiki/Death_Star:_Detention_Block_Control_Room_(Japanese)) | 299894 |
| [Death Star: Docking Bay 327 (Japanese)](https://wiki.swccg.com/wiki/Death_Star:_Docking_Bay_327_(Japanese)) | 299895 |
| [Death Star: Trash Compactor (Japanese)](https://wiki.swccg.com/wiki/Death_Star:_Trash_Compactor_(Japanese)) | 299896 |
| [Kessel (Japanese)](https://wiki.swccg.com/wiki/Kessel_(Japanese)) | 299897 |
| [Tatooine (Light) (Premiere) (Japanese)](https://wiki.swccg.com/wiki/Tatooine_(Light)_(Premiere)_(Japanese)) | 299898 |
| [Tatooine: Cantina (Light) (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Cantina_(Light)_(Japanese)) | 299899 |
| [Tatooine: Docking Bay 94 (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Docking_Bay_94_(Japanese)) | 299900 |
| [Tatooine: Dune Sea (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Dune_Sea_(Japanese)) | 299901 |
| [Tatooine: Jawa Camp (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Jawa_Camp_(Japanese)) | 299902 |
| [Tatooine: Lars' Moisture Farm (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Lars'_Moisture_Farm_(Japanese)) | 299903 |
| [Tatooine: Mos Eisley (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Mos_Eisley_(Japanese)) | 299904 |
| [Tatooine: Obi-Wan's Hut (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Obi-Wan's_Hut_(Japanese)) | 299905 |
| [Yavin 4 (Japanese)](https://wiki.swccg.com/wiki/Yavin_4_(Japanese)) | 299906 |
| [Yavin 4: Docking Bay (Japanese)](https://wiki.swccg.com/wiki/Yavin_4:_Docking_Bay_(Japanese)) | 299907 |
| [Yavin 4: Jungle (Japanese)](https://wiki.swccg.com/wiki/Yavin_4:_Jungle_(Japanese)) | 299908 |
| [Yavin 4: Massassi Throne Room (Japanese)](https://wiki.swccg.com/wiki/Yavin_4:_Massassi_Throne_Room_(Japanese)) | 299909 |
| [Yavin 4: Massassi War Room (Japanese)](https://wiki.swccg.com/wiki/Yavin_4:_Massassi_War_Room_(Japanese)) | 299910 |
| [Corellian Corvette (Japanese)](https://wiki.swccg.com/wiki/Corellian_Corvette_(Japanese)) | 299911 |
| [Gold 1 (Japanese)](https://wiki.swccg.com/wiki/Gold_1_(Japanese)) | 299912 |
| [Gold 5 (Japanese)](https://wiki.swccg.com/wiki/Gold_5_(Japanese)) | 299913 |
| [Millennium Falcon (Japanese)](https://wiki.swccg.com/wiki/Millennium_Falcon_(Japanese)) | 299914 |
| [Red 1 (Japanese)](https://wiki.swccg.com/wiki/Red_1_(Japanese)) | 299915 |
| [Red 3 (Japanese)](https://wiki.swccg.com/wiki/Red_3_(Japanese)) | 299916 |
| [X-wing (Japanese)](https://wiki.swccg.com/wiki/X-wing_(Japanese)) | 299917 |
| [Y-wing (Japanese)](https://wiki.swccg.com/wiki/Y-wing_(Japanese)) | 299918 |
| [Lift Tube (Japanese)](https://wiki.swccg.com/wiki/Lift_Tube_(Japanese)) | 299919 |
| [Luke's X-34 Landspeeder (Japanese)](https://wiki.swccg.com/wiki/Luke's_X-34_Landspeeder_(Japanese)) | 299920 |
| [Sandcrawler (Japanese)](https://wiki.swccg.com/wiki/Sandcrawler_(Japanese)) | 299921 |
| [SoroSuub V-35 Landspeeder (Japanese)](https://wiki.swccg.com/wiki/SoroSuub_V-35_Landspeeder_(Japanese)) | 299922 |
| [5D6-RA-7 (Fivedesix) (Japanese)](https://wiki.swccg.com/wiki/5D6-RA-7_(Fivedesix)_(Japanese)) | 299923 |
| [Admiral Motti (Japanese)](https://wiki.swccg.com/wiki/Admiral_Motti_(Japanese)) | 299924 |
| [Darth Vader (Japanese)](https://wiki.swccg.com/wiki/Darth_Vader_(Japanese)) | 299925 |
| [Djas Puhr (Japanese)](https://wiki.swccg.com/wiki/Djas_Puhr_(Japanese)) | 299926 |
| [Dr. Evazan (Japanese)](https://wiki.swccg.com/wiki/Dr._Evazan_(Japanese)) | 299927 |
| [EG-6 (Eegee-Six) (Japanese)](https://wiki.swccg.com/wiki/EG-6_(Eegee-Six)_(Japanese)) | 299928 |
| [Garindan (Japanese)](https://wiki.swccg.com/wiki/Garindan_(Japanese)) | 299929 |
| [General Tagge (Japanese)](https://wiki.swccg.com/wiki/General_Tagge_(Japanese)) | 299930 |
| [Grand Moff Tarkin (Japanese)](https://wiki.swccg.com/wiki/Grand_Moff_Tarkin_(Japanese)) | 299931 |
| [Imperial Pilot (Japanese)](https://wiki.swccg.com/wiki/Imperial_Pilot_(Japanese)) | 299932 |
| [Imperial Trooper Guard (Japanese)](https://wiki.swccg.com/wiki/Imperial_Trooper_Guard_(Japanese)) | 299933 |
| [Jawa (Dark) (Premiere) (Japanese)](https://wiki.swccg.com/wiki/Jawa_(Dark)_(Premiere)_(Japanese)) | 299934 |
| [Kitik Keed'kak (Japanese)](https://wiki.swccg.com/wiki/Kitik_Keed'kak_(Japanese)) | 299935 |
| [Labria (Japanese)](https://wiki.swccg.com/wiki/Labria_(Japanese)) | 299936 |
| [LIN-V8M (Elleyein-Veeateemm) (Japanese)](https://wiki.swccg.com/wiki/LIN-V8M_(Elleyein-Veeateemm)_(Japanese)) | 299937 |
| [MSE-6 'Mouse' Droid (Japanese)](https://wiki.swccg.com/wiki/MSE-6_'Mouse'_Droid_(Japanese)) | 299938 |
| [Myo (Japanese)](https://wiki.swccg.com/wiki/Myo_(Japanese)) | 299939 |
| [Ponda Baba (Japanese)](https://wiki.swccg.com/wiki/Ponda_Baba_(Japanese)) | 300036 |
| [Prophetess (Japanese)](https://wiki.swccg.com/wiki/Prophetess_(Japanese)) | 299941 |
| [R1-G4 (Arone-Geefour) (Japanese)](https://wiki.swccg.com/wiki/R1-G4_(Arone-Geefour)_(Japanese)) | 299942 |
| [R4-M9 (Arfour-Emmnine) (Japanese)](https://wiki.swccg.com/wiki/R4-M9_(Arfour-Emmnine)_(Japanese)) | 299943 |
| [Stormtrooper (Japanese)](https://wiki.swccg.com/wiki/Stormtrooper_(Japanese)) | 299944 |
| [Tonnika Sisters (Japanese)](https://wiki.swccg.com/wiki/Tonnika_Sisters_(Japanese)) | 299945 |
| [Tusken Raider (Japanese)](https://wiki.swccg.com/wiki/Tusken_Raider_(Japanese)) | 299946 |
| [WED15-I662 'Treadwell' Droid (Japanese)](https://wiki.swccg.com/wiki/WED15-I662_'Treadwell'_Droid_(Japanese)) | 299947 |
| [Wuher (Japanese)](https://wiki.swccg.com/wiki/Wuher_(Japanese)) | 299948 |
| [Alderaan (Dark) (Japanese)](https://wiki.swccg.com/wiki/Alderaan_(Dark)_(Japanese)) | 299949 |
| [Dantooine (Dark) (Japanese)](https://wiki.swccg.com/wiki/Dantooine_(Dark)_(Japanese)) | 299950 |
| [Death Star: Central Core (Japanese)](https://wiki.swccg.com/wiki/Death_Star:_Central_Core_(Japanese)) | 299951 |
| [Death Star: Detention Block Corridor (Japanese)](https://wiki.swccg.com/wiki/Death_Star:_Detention_Block_Corridor_(Japanese)) | 299952 |
| [Death Star: Docking Bay 327 (Dark) (Japanese)](https://wiki.swccg.com/wiki/Death_Star:_Docking_Bay_327_(Dark)_(Japanese)) | 299953 |
| [Death Star: Level 4 Military Corridor (Japanese)](https://wiki.swccg.com/wiki/Death_Star:_Level_4_Military_Corridor_(Japanese)) | 299954 |
| [Death Star: War Room (Japanese)](https://wiki.swccg.com/wiki/Death_Star:_War_Room_(Japanese)) | 299955 |
| [Kessel (Dark) (Japanese)](https://wiki.swccg.com/wiki/Kessel_(Dark)_(Japanese)) | 299956 |
| [Tatooine (Dark) (Premiere) (Japanese)](https://wiki.swccg.com/wiki/Tatooine_(Dark)_(Premiere)_(Japanese)) | 299957 |
| [Tatooine: Cantina (Dark) (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Cantina_(Dark)_(Japanese)) | 299958 |
| [Tatooine: Docking Bay 94 (Dark) (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Docking_Bay_94_(Dark)_(Japanese)) | 299959 |
| [Tatooine: Jawa Camp (Dark) (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Jawa_Camp_(Dark)_(Japanese)) | 299960 |
| [Tatooine: Jundland Wastes (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Jundland_Wastes_(Japanese)) | 299961 |
| [Tatooine: Lars' Moisture Farm (Dark) (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Lars'_Moisture_Farm_(Dark)_(Japanese)) | 299962 |
| [Tatooine: Mos Eisley (Dark) (Japanese)](https://wiki.swccg.com/wiki/Tatooine:_Mos_Eisley_(Dark)_(Japanese)) | 299963 |
| [Yavin 4 (Dark) (Japanese)](https://wiki.swccg.com/wiki/Yavin_4_(Dark)_(Japanese)) | 299964 |
| [Yavin 4: Docking Bay (Dark) (Japanese)](https://wiki.swccg.com/wiki/Yavin_4:_Docking_Bay_(Dark)_(Japanese)) | 299965 |
| [Yavin 4: Jungle (Dark) (Japanese)](https://wiki.swccg.com/wiki/Yavin_4:_Jungle_(Dark)_(Japanese)) | 299966 |
| [Black 3 (Japanese)](https://wiki.swccg.com/wiki/Black_3_(Japanese)) | 300015 |
| [Devastator (Japanese)](https://wiki.swccg.com/wiki/Devastator_(Japanese)) | 299968 |
| [Imperial-Class Star Destroyer (Japanese)](https://wiki.swccg.com/wiki/Imperial-Class_Star_Destroyer_(Japanese)) | 299969 |
| [TIE Advanced x1 (Japanese)](https://wiki.swccg.com/wiki/TIE_Advanced_x1_(Japanese)) | 299970 |
| [TIE Fighter (Japanese)](https://wiki.swccg.com/wiki/TIE_Fighter_(Japanese)) | 299971 |
| [TIE Scout (Japanese)](https://wiki.swccg.com/wiki/TIE_Scout_(Japanese)) | 299972 |
| [Vader's Custom TIE (Japanese)](https://wiki.swccg.com/wiki/Vader's_Custom_TIE_(Japanese)) | 299973 |
| [Bantha (Japanese)](https://wiki.swccg.com/wiki/Bantha_(Japanese)) | 299974 |
| [Sandcrawler (Dark) (Japanese)](https://wiki.swccg.com/wiki/Sandcrawler_(Dark)_(Japanese)) | 299975 |
| [Ubrikkian 9000 Z001 (Japanese)](https://wiki.swccg.com/wiki/Ubrikkian_9000_Z001_(Japanese)) | 299976 |
| [Premiere (Japanese)](https://wiki.swccg.com/wiki/Premiere_(Japanese)) | 300021 |
| [Chief Bast (Japanese)](https://wiki.swccg.com/wiki/Chief_Bast_(Japanese)) | 299982 |
| [Colonel Wullf Yularen (Japanese)](https://wiki.swccg.com/wiki/Colonel_Wullf_Yularen_(Japanese)) | 299983 |
| [Commander Praji (Japanese)](https://wiki.swccg.com/wiki/Commander_Praji_(Japanese)) | 299984 |
| [Dathcha (Japanese)](https://wiki.swccg.com/wiki/Dathcha_(Japanese)) | 299985 |
| [Death Star Trooper (Japanese)](https://wiki.swccg.com/wiki/Death_Star_Trooper_(Japanese)) | 299986 |
| [DS-61-2 (Japanese)](https://wiki.swccg.com/wiki/DS-61-2_(Japanese)) | 299987 |
| [DS-61-3 (Japanese)](https://wiki.swccg.com/wiki/DS-61-3_(Japanese)) | 299988 |
| [Feltipern Trevagg (Japanese)](https://wiki.swccg.com/wiki/Feltipern_Trevagg_(Japanese)) | 299989 |
| [Lieutenant Tanbris (Japanese)](https://wiki.swccg.com/wiki/Lieutenant_Tanbris_(Japanese)) | 299990 |
| [M'iiyoom Onith (Japanese)](https://wiki.swccg.com/wiki/M'iiyoom_Onith_(Japanese)) | 299991 |
| [Caller (Dark) (Japanese)](https://wiki.swccg.com/wiki/Caller_(Dark)_(Japanese)) | 299992 |
| [Restraining Bolt (Dark) (Japanese)](https://wiki.swccg.com/wiki/Restraining_Bolt_(Dark)_(Japanese)) | 299993 |
| [Blast Door Controls (Japanese)](https://wiki.swccg.com/wiki/Blast_Door_Controls_(Japanese)) | 299994 |
| [Blaster Rack (Japanese)](https://wiki.swccg.com/wiki/Blaster_Rack_(Japanese)) | 299995 |
| [Fear Will Keep Them In Line (Japanese)](https://wiki.swccg.com/wiki/Fear_Will_Keep_Them_In_Line_(Japanese)) | 299996 |
| [Jawa Pack (Japanese)](https://wiki.swccg.com/wiki/Jawa_Pack_(Japanese)) | 299997 |
| [Juri Juice (Japanese)](https://wiki.swccg.com/wiki/Juri_Juice_(Japanese)) | 299998 |
| [Luke? Luuuuke! (Japanese)](https://wiki.swccg.com/wiki/Luke%3F_Luuuuke%21_(Japanese)) | 299999 |
| [Boring Conversation Anyway (Japanese)](https://wiki.swccg.com/wiki/Boring_Conversation_Anyway_(Japanese)) | 300000 |
| [Collateral Damage (Japanese)](https://wiki.swccg.com/wiki/Collateral_Damage_(Japanese)) | 300001 |
| [Dark Jedi Presence (Japanese)](https://wiki.swccg.com/wiki/Dark_Jedi_Presence_(Japanese)) | 300002 |
| [Dead Jawa (Japanese)](https://wiki.swccg.com/wiki/Dead_Jawa_(Japanese)) | 300003 |
| [Elis Helrot (Japanese)](https://wiki.swccg.com/wiki/Elis_Helrot_(Japanese)) | 300004 |
| [Evacuate? (Japanese)](https://wiki.swccg.com/wiki/Evacuate%3F_(Japanese)) | 300005 |
| [Gravel Storm (Japanese)](https://wiki.swccg.com/wiki/Gravel_Storm_(Japanese)) | 300006 |
| [Imperial Barrier (Japanese)](https://wiki.swccg.com/wiki/Imperial_Barrier_(Japanese)) | 300007 |
| [Imperial Code Cylinder (Japanese)](https://wiki.swccg.com/wiki/Imperial_Code_Cylinder_(Japanese)) | 300008 |
| [Imperial Reinforcements (Japanese)](https://wiki.swccg.com/wiki/Imperial_Reinforcements_(Japanese)) | 300009 |
| [It's Worse (Japanese)](https://wiki.swccg.com/wiki/It's_Worse_(Japanese)) | 300010 |
| [I've Got A Problem Here (Japanese)](https://wiki.swccg.com/wiki/I've_Got_A_Problem_Here_(Japanese)) | 300011 |
| [Lone Warrior (Japanese)](https://wiki.swccg.com/wiki/Lone_Warrior_(Japanese)) | 300012 |
| [Look Sir, Droids (Japanese)](https://wiki.swccg.com/wiki/Look_Sir,_Droids_(Japanese)) | 300013 |
| [Black 2 (Japanese)](https://wiki.swccg.com/wiki/Black_2_(Japanese)) | 300014 |
| [Lift Tube (Dark) (Japanese)](https://wiki.swccg.com/wiki/Lift_Tube_(Dark)_(Japanese)) | 300016 |
| [Dark Jedi Lightsaber (Japanese)](https://wiki.swccg.com/wiki/Dark_Jedi_Lightsaber_(Japanese)) | 300017 |
| [Han Seeker (Japanese)](https://wiki.swccg.com/wiki/Han_Seeker_(Japanese)) | 300018 |
| [File:Japanese-Premiere-1301-185o-SWCA.jpg](https://wiki.swccg.com/wiki/File:Japanese-Premiere-1301-185o-SWCA.jpg) | 300019 |
| [File:Japanese-Premiere-1301-25o-SWCA.jpg](https://wiki.swccg.com/wiki/File:Japanese-Premiere-1301-25o-SWCA.jpg) | 300020 |
| [Overload (Japanese)](https://wiki.swccg.com/wiki/Overload_(Japanese)) | 300037 |
| [Physical Choke (Japanese)](https://wiki.swccg.com/wiki/Physical_Choke_(Japanese)) | 300038 |
| [Precise Attack (Japanese)](https://wiki.swccg.com/wiki/Precise_Attack_(Japanese)) | 300039 |
| [Reactor Terminal (Japanese)](https://wiki.swccg.com/wiki/Reactor_Terminal_(Japanese)) | 300040 |
