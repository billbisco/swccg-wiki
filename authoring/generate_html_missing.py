#!/usr/bin/env python3
"""Two-column deck pages from PC HTML for OCS, Euro 2025, Jawa, Retro US Nats, regionals."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2026_euro as ge  # noqa: E402
import update_gempc_start_fields as ug  # noqa: E402

PAGES = ROOT / "pages"
DECKS = ROOT / "encyclopedia" / "needed-decks"
URL_FILES = [
    ROOT / "encyclopedia" / "priority-deck-urls.txt",
    ROOT / "encyclopedia" / "regional-deck-urls.txt",
    ROOT / "encyclopedia" / "vegas-gap-urls.txt",
]

PREFIXES = [
    ("2025-las-vegas-grand-prix-day-2-", "2025 Las Vegas Grand Prix", "Top 8", True, "2025"),
    ("2025-las-vegas-grand-prix-", "2025 Las Vegas Grand Prix", "Day 1", False, "2025"),
    ("2025-ocs-playoff-finals-", "2025 Online Championship Series Playoffs", "Finals", True, "2025"),
    ("2025-ocs-playoff-semi-finals-", "2025 Online Championship Series Playoffs", "Semifinals", True, "2025"),
    ("2025-ocs-playoff-quarterfinals-", "2025 Online Championship Series Playoffs", "Quarterfinals", True, "2025"),
    ("2025-ocs-playoff-top-16-", "2025 Online Championship Series Playoffs", "Top 16", True, "2025"),
    ("2025-european-championship-top-4-", "2025 European Championship", "Top 4", True, "2025"),
    ("2025-european-championship-", "2025 European Championship", "Day 1", False, "2025"),
    ("2026-jawa-cup-finals-", "2026 Jawa Cup", "Finals", True, "2026"),
    ("2026-jawa-cup-top-4-", "2026 Jawa Cup", "Top 4", True, "2026"),
    ("2026-jawa-cup-top-8-", "2026 Jawa Cup", "Top 8", True, "2026"),
    ("2026-jawa-cup-", "2026 Jawa Cup", "Swiss", False, "2026"),
    ("2026-retro-us-nationals-", "2026 Retro U.S. Nationals", "constructed", False, "2026"),
    ("2026-us-retro-nationals-", "2026 Retro U.S. Nationals", "constructed", False, "2026"),
]

PLANET_NAME = {
    "nal-hutta": "Nal Hutta",
    "yavin-4": "Yavin 4",
    "corellia": "Corellia",
    "coruscant": "Coruscant",
    "endor": "Endor",
    "bespin": "Bespin",
    "naboo": "Naboo",
    "tatooine": "Tatooine",
    "ryloth": "Ryloth",
    "alderaan": "Alderaan",
    "dagobah": "Dagobah",
    "ithor": "Ithor",
    "ralltiir": "Ralltiir",
    "scarif": "Scarif",
    "toola": "Toola",
    "bothawui": "Bothawui",
    "kashyyyk": "Kashyyyk",
}

NAME = {
    "pat-johnson": "Patrick Johnson",
    "matthew-harrison-trainor": "Matthew Harrison-Trainor",
    "jon-benkert-holtet": "Jon Benkert Holtet",
    "jonas-hagen-norregaard": "Jonas Hagen Nørregaard",
    "jonas-hagen": "Jonas Hagen Nørregaard",
    "cedrik-vanderhawgen": "Cedrik Vanderhaegen",
    "l-pater": "L. Pater",
    "randall-scott": "Randy Scott",
    "jon-holtet": "Jon Benkert Holtet",
    "casper-jorgensen": "Casper Jørgensen",
    "quirin-furgut": "Quirin Fürgut",
    "floris-de-vries": "Floris de Vries",
    "martin-den-boef": "Martin den Boef",
    "eric-spijksma": "Erik Spijksma",
    "cedrik-vanderhaegen": "Cedrik Vanderhaegen",
    "justin-branch": "Justin Branch",
    "justin-miyashiro": "Justin Miyashiro",
    "jason-riendeau": "Jason Riendeau",
    "sean-luhks": "Sean Luhks",
    "bill-bacheler": "Bill Bacheler",
    "william-bacheler": "Bill Bacheler",
    "matt-sokol": "Matt Sokol",
    "matt-ford": "Matthew Ford",
    "andy-talaga": "Andy Talaga",
    "joe-giannetti": "Joe Giannetti",
    "apollo-chu": "Apollo Chu",
    "matt-manning": "Matt Manning",
    "steve-sanders": "Steve Sanders",
    "jonny-chu": "Jonny Chu",
    "chris-kelly": "Chris Kelly",
    "andrew-moss": "Andrew Moss",
    "conor-britain": "Conor Britain",
    "casey-anis": "Casey Anis",
    "justin-desai": "Justin Desai",
    "patrik-csapi": "Patrik Csapi",
    "ryan-jellison": "Ryan Jellison",
    "jarad-konsker": "Jarad Konsker",
    "jeff-lavigne": "Jeff Lavigne",
    "anthony-howard": "Anthony Howard",
    "kyle-krueger": "Kyle Krueger",
    "brad-kippel": "Brad Kippel",
    "joe-olson": "Joe Olson",
    "greg-shaw": "Greg Shaw",
    "sam-tashima": "Sam Tashima",
    "timo-dusel": "Timo Dusel",
    "emil-wallin": "Emil Wallin",
    "koen-meijssen": "Koen Meijssen",
    "marvin-tegeler": "Marvin Tegeler",
    "chris-menzel": "Chris Menzel",
    "john-moorley": "John Moorley",
    "kevin-jaap": "Kevin Jaap",
    "julian-smolarek": "Julian Smolarek",
    "julian-andres-smolarek": "Julian Smolarek",
    "michael-richards": "Mike Richards",
    "mike-richards": "Mike Richards",
    "mike-pistone": "Mike Pistone",
    "michael-pistone": "Mike Pistone",
    "aj-hatoum": "AJ Hatoum",
    "abe-christensen": "Abe Christensen",
    "brandon-nguyen": "Brandon Nguyen",
    "carson-stockman": "Carson Stockman",
    "charlie-arlandson": "Charlie Arlandson",
    "cory-lauer": "Cory Lauer",
    "ellie-hoyt": "Ellie Hoyt",
    "garrett-larson": "Garrett Larson",
    "jacoby-kramer": "Jacoby Kramer",
    "logan-pietig": "Logan Pietig",
    "mark-walseth": "Mark Walseth",
    "nick-swedal": "Nick Swedal",
    "scott-morgan": "Scott Morgan",
    "sean-miller": "Sean Miller",
    "will-tarbox": "Will Tarbox",
    "hayes-hunter": "Hayes Hunter",
    "hayes-hunter-vegas": "Hayes Hunter",
    "brad-eier": "Brad Eier",
    "ryan-sersen": "Ryan Sersen",
    "karl-koenig": "Karl Koenig",
    "kendall-halman": "Kendall Halman",
    "brian-fred": "Brian Fred",
    "chad-lawrence": "Chad Lawrence",
    "travis-morris": "Travis Morris",
    "wayne-cullen": "Wayne Cullen",
    "scott-lingrell": "Scott Lingrell",
    "greg-zinn": "Greg Zinn",
    "stephen-squirlock": "Stephen Squirlock",
    "mark-billings": "Mark Billings",
    "paul-coggins": "Paul Coggins",
    "randy-scott": "Randy Scott",
    "adam-bott": "Adam Bott",
    "ken-cross": "Ken Cross",
    "jacy-smith": "Jacy Smith",
    "kyle-kallin": "Kyle Kallin",
    "chris-wirfs": "Chris Wirfs",
    "matt-scott": "Matt Scott",
    "matt-wadden": "Matt Wadden",
    "matthijs-van-leeuwen": "Matthijs van Leeuwen",
    "bill-kafer": "Bill Kafer",
    "chris-westergard": "Chris Westergard",
    "jacob-vawter": "Jacob Vawter",
    "l-pater": "L. Pater",
    "marc-nickels": "Marc Nickels",
    "peter-jacobson": "Peter Jacobson",
    "tamas-papp": "Tamás Papp",
    "wayne-poppleton": "Wayne Poppleton",
    "andrew-davies": "Andrew Davies",
    "conrad-simmering": "Conrad Simmering",
    "enno-haede": "Enno Haede",
    "sean-mackin": "Sean Mackin",
    "mike-turner": "Mike Turner",
    "scott-morgan": "Scott Morgan",
    "sean-miller": "Sean Miller",
    "matt-luts": "Matt Lutz",
    "matt-mannning": "Matt Manning",
    "stephen-sanders": "Steve Sanders",
    "stephan-devos": "Stephan de Vos",
    "jerry-hsaio": "Jerry Hsiao",
    "jerry-hsiao": "Jerry Hsiao",
    "charlie-anderson": "Charlie Arlandson",
    "bob-birrer": "Bobby Birrer",
    "clay-atkin": "Clayton Atkin",
    "jeffrey-lavigne": "Jeff Lavigne",
    "quirin-furgut": "Quirin Fürgut",
    "matthew-carulli": "Matt Carulli",
    "jon-mcfarland": "Jon McFarland",
    "john-mcfarland": "Jon McFarland",
    "pat-johnson": "Patrick Johnson",
    "paul-mcpherson": "Paul McPherson",
    "stephan-de-vos": "Stephan de Vos",
    "martin-den-boef": "Martin den Boef",
    "miguel-tarin-vegas": "Miguel Tarin",
    "miguel-tarin": "Miguel Tarin",
    "kenneth-brennen": "Kenneth Brennen",
    "andrew-bethell": "Andrew Bethell",
    "bastian-winklehaus": "Bastian Winkelhaus",
    "quirin-furgut": "Quirin Fürgut",
    "elspeth-jellison": "Elspeth Jellison",
    "nate-davis": "Nate Davis",
    "gosse-zeilstra": "Gosse Zeilstra",
    "david-beaubier": "David Beaubier",
    "matt-smith": "Matt Smith",
    "seth-acree": "Seth Acree",
    "steve-brentson": "Steve Brentson",
    "shawn-dickson": "Shawn Dickson",
    "bryan-gravener": "Bryan Gravener",
    "mike-pistone": "Mike Pistone",
    "michael-pistone": "Mike Pistone",
    "tim-simon": "Tim Simon",
    "isaac-story": "Isaac Story",
    "issac-story": "Isaac Story",
    "nathan-trothing": "Nathan Trothing",
    "andy-wexstten": "Andy Wexstten",
    "edward-chien": "Edward Chien",
    "trevor-partridge": "Trevor Partridge",
    "joe-pinto": "Joe Pinto",
    "jeffrey-scales": "Jeffrey Scales",
    "travis-thompson": "Travis Thompson",
    "sam-olson": "Sam Olson",
    "brian-herold": "Brian Herold",
    "tom-marlin": "Tom Marlin",
    "mike-richards": "Mike Richards",
    "matt-thornton": "Matt Thornton",
    "max-dewitt": "Max DeWitt",
    "austin-jacobus": "Austin Jacobus",
    "piotr-ptak": "Piotr Ptak",
    "nico-johannes-kreidl": "Nico Johannes Kreidl",
    "nico-kreidl": "Nico Johannes Kreidl",
    "lukasz-saczek": "Lukasz Saczek",
    "kristian-lund": "Kristian Lund",
    "dennis-schwarz": "Dennis Schwarz",
    "rasmus-juul": "Rasmus Juul",
    "kristoffer-basse-hedlund": "Kristoffer Basse Hedlund",
    "gyorgy-pora": "György Póra",
    "ulli-reuter": "Ulli Reuter",
    "piotr-jarnot": "Piotr Jarnot",
    "julian-cochard": "Julian Cochard",
    "ralf-w": "Ralf W.",
    "kent-larsen": "Kent Larsen",
    "peter-rowlands": "Peter Rowlands",
    "stefan-boersma": "Stefan Boersma",
    "robert-smolarek": "Robert Smolarek",
    "gunnar-branden": "Gunnar Brandén",
    "jay-chutino": "Jay Chutino",
    "nathan-angulo": "Nathan Angulo",
    "aaron-bott": "Aaron Bott",
    "steven-lamar": "Danny Lamar",
    "danny-lamar": "Danny Lamar",
    "eric-hawbaker": "Erich Hawbaker",
    "erich-hawbaker": "Erich Hawbaker",
    "jon-holtet": "Jon Benkert Holtet",
    "casper-jorgensen": "Casper Jørgensen",
    "jonas-hagen-norregaard": "Jonas Hagen Nørregaard",
    "eric-spijksma": "Erik Spijksma",
    "erik-spijksma": "Erik Spijksma",
    "stephen-baroni": "Steve Baroni",
    "jeffrey-johns": "Jeffrey Johns",
    "joe-gianetti": "Joe Gianetti",
    "joe-giannetti": "Joe Giannetti",
    "matt-lutz": "Matt Lutz",
    "drew-lichtenstein": "Drew Lichtenstein",
    "ziemowit-skwara": "Ziemowit Skwara",
    "fernando-castanon": "Fernando Castañón",
    "paul-myers": "Paul Myers",
    "chris-hull": "Chris Hull",
    "mike-kessling": "Mike Kessling",
    "kevin-shannon": "Kevin Shannon",
    "matt-sperling": "Matt Sperling",
    "nate-louderback": "Nate Louderback",
    "brandon-romano": "Brandon Romano",
    "adam-fletcher": "Adam Fletcher",
    "grady-hutchins": "Grady Hutchins",
    "tom-sarachan": "Tom Sarachan",
    "kyle-mclean": "Kyle McLean",
    "nick-reisch": "Nick Reisch",
    "sean-mackin": "Sean Mackin",
    "chad-lawrence": "Chad Lawrence",
    "dan-tartaglione": "Dan Tartaglione",
    "stephen-cellucci": "Stephen Cellucci",
    "stephen-morgan": "Stephen Morgan",
    "jeffrey-lavigne": "Jeff Lavigne",
    "darren-malins": "Darren Malins",
    "marc-nickels": "Marc Nickels",
    "peter-jacobson": "Peter Jacobson",
    "horst-draudt": "Horst Draudt",
    "mike-klarenbeek": "Mike Klarenbeek",
    "nelson-cazon": "Nelson Cazon",
    "moritz-karge": "Moritz Karge",
    "jimmy-faelens": "Jimmy Faelens",
    "jonas-jakubowski": "Jonas Jakubowski",
    "alex-klimo": "Alex Klimo",
    "angelo-consoli": "Angelo Consoli",
    "vjeko-keskic": "Vjeko Keskic",
    "noah-faelens": "Noah Faelens",
    "bertrand-momal": "Bertrand Momal",
    "camden-yanaga": "Camden Yanaga",
    "mitch-nieland": "Mitch Nieland",
    "joe-phillips": "Joe Phillips",
    "thang-le": "Thang Le",
    "andrew-bollentino": "Andrew Bollentino",
    "ming-huo": "Ming Huo",
    "adam-schellberg": "Adam Schellberg",
    "sam-tashima": "Sam Tashima",
    "winston-plunkett": "Winston Plunkett",
    "phil-aasen": "Phil Aasen",
    "bryan-mischke": "Bryan Mischke",
    "lenny-rubin": "Lenny Rubin",
    "reid-smith": "Reid Smith",
    "tom-haid": "Tom Haid",
    "tom-damen": "Tom Damen",
    "tom-kelly": "Tom Kelly",
    "matt-carulli": "Matt Carulli",
    "justin-carulli": "Justin Carulli",
    "keith-brown": "Keith Brown",
    "jared-napolitano": "Jared Napolitano",
    "chris-gogolen": "Chris Gogolen",
    "geoff-hummel": "Geoff Hummel",
    "morgan-lewis": "Morgan Lewis",
    "stephen-skilton": "Stephen Skilton",
    "kevin-elia": "Kevin Elia",
    "steve-sanders": "Steve Sanders",
    "brad-reinhold": "Brad Reinhold",
    "phillip-gladney": "Phillip Gladney",
    "jonathon-murray": "Jonathon Murray",
    "jerry-heine": "Jerry Heine",
    "vinny-rossi": "Vinny Rossi",
    "lee-edwards": "Lee Edwards",
    "amar-banger": "Amar Banger",
    "jeremy-dipaolo": "Jeremy DiPaolo",
    "gibson-yim": "Gibson Yim",
    "brett-bailey": "Brett Bailey",
    "nick-gorski": "Nick Gorski",
    "ben-butterworth": "Ben Butterworth",
    "stephen-squirlock": "Stephen Squirlock",
    "brian-west": "Brian West",
    "eric-garchow": "Eric Garchow",
    "brandon-baity": "Brandon Baity",
    "vikram-bali": "Vikram Bali",
    "cal-aldred": "Cal Aldred",
    "michael-erisman": "Michael Erisman",
    "chris-angulo": "Chris Angulo",
    "gabriel-angulo": "Gabriel Angulo",
    "jan-berueda": "Jan Berueda",
    "jan-westergard": "Jan Westergard",
    "chris-westergard": "Chris Westergard",
    "greg-nirshberg": "Greg Nirshberg",
    "jim-li": "Jim Li",
    "daniel-amor": "Daniel Amor",
    "brandon-chong": "Brandon Chong",
    "bobby-birrer": "Bobby Birrer",
    "anthony-howard": "Anthony Howard",
    "john-veasey": "John Veasey",
    "keegan-heilman": "Keegan Heilman",
    "casey-johnson": "Casey Johnson",
    "bill-pittman": "Bill Pittman",
    "josh-mack": "Josh Mack",
    "forrest-sobieszczyk": "Forrest Sobieszczyk",
    "adam-trunzo": "Adam Trunzo",
    "conor-britain": "Conor Britain",
    "gavin-ortlund": "Gavin Ortlund",
    "rikard-eriksen": "Rikard Eriksen",
    "brett-carlson": "Brett Carlson",
    "aaron-kingery": "Aaron Kingery",
    "james-martin": "James Martin",
    "patrick-johnson": "Patrick Johnson",
    "barry-alperstein": "Barry Alperstein",
    "casey-anis": "Casey Anis",
    "robbie-hendon": "Robbie Hendon",
    "matt-scott": "Matt Scott",
    "hayes-hunter": "Hayes Hunter",
    "eric-hunter": "Eric Hunter",
    "jonny-chu": "Jonny Chu",
    "emil-wallin": "Emil Wallin",
    "bastian-winkelhaus": "Bastian Winkelhaus",
    "steve-harpster": "Steve Harpster",
    "dennis-reinhardt": "Dennis Reinhardt",
    "matt-wadden": "Matt Wadden",
    "clayton-atkin": "Clayton Atkin",
    "wayne-cullen": "Wayne Cullen",
    "scott-lingrell": "Scott Lingrell",
    "adam-radic": "Adam Radic",
    "john-werner": "John Werner",
    "zack-stenerson": "Zach Stenerson",
    "zach-stenerson": "Zach Stenerson",
    "jeremie-jensen": "Jeramie Jensen",
    "jeramie-jensen": "Jeramie Jensen",
    "kevin-babb": "Kevin Babb",
    "rich-craft": "Rich Craft",
    "pierre-dubreuil": "Pierre Dubreuil",
    "derek-jackson": "Derek Jackson",
    "steven-yaeger": "Steven Yaeger",
    "brandon-nguyen": "Brandon Nguyen",
    "jeff-johns": "Jeffrey Johns",
    "gosse-zeilstra": "Gosse Zeilstra",
    "elspeth-jellison": "Elspeth Jellison",
    "nate-davis": "Nate Davis",
    "david-beaubier": "David Beaubier",
    "matt-smith": "Matt Smith",
}

SLANG_HUB = {
    "skywalker saga luke": "The Force Is Strong In My Family",
    "skywalker saga anakin": "The Force Is Strong In My Family",
    "skywalker saga rey": "The Force Is Strong In My Family",
    "luke saga": "The Force Is Strong In My Family",
    "anakin saga": "The Force Is Strong In My Family",
    "rey saga": "The Force Is Strong In My Family",
    "saga luke": "The Force Is Strong In My Family",
    "shadow collective": "Shadow Collective",
    "wys": "Watch Your Step",
    "watch your step": "Watch Your Step",
    "hunt down": "Hunt Down And Destroy The Jedi",
    "hunt down (V)": "Hunt Down And Destroy The Jedi (V)",
    "first order reigns": "The First Order Reigns",
    "endor operations": "Endor Operations",
    "eops": "Endor Operations",
    "old allies": "Old Allies",
    "oa": "Old Allies",
    "diplo": "Diplomatic Mission To Alderaan",
    "whap": "We Have A Plan",
    "hitco": "He Is The Chosen One",
    "mwyhlv": "Mind What You Have Learned (V)",
    "rst": "Rebel Strike Team",
    "rebel strike team": "Rebel Strike Team",
    "no idea": "They Have No Idea We're Coming",
    "senate": "Plead My Case To The Senate",
    "map": "I Want That Map",
    "i want that map": "I Want That Map",
    "walkers": "The Shield Will Be Down in Moments",
    "thrawn": "A Great Tactician Creates Plans",
    "court": "Court Of The Vile Gangster",
    "clones": "Hunt For The Droid General",
    "coruscant crv": "Combat Readiness (V)",
    "trm": "Yavin 4: Massassi Throne Room",
    "rots dooku": "Revenge Of The Sith",
    "rots vader": "Revenge Of The Sith",
    "isb operations": "ISB Operations",
    "isb": "ISB Operations",
    "imperial entanglements": "Imperial Entanglements",
    "legend": "The Galaxy May Need A Legend",
    "rescue the princess v": "Rescue The Princess (V)",
    "rtpv": "Rescue The Princess (V)",
    "a stunning move": "A Stunning Move",
    "vaders castle ssav": "Set Your Course For Alderaan",
    "aitc": "All I Need Is Your Scum",
    "tto": "There Is No Try",
    "ebo": "Echo Base Operations",
    "tdigwattv": "This Deal Is Getting Worse All The Time (V)",
    "tdigwatt": "This Deal Is Getting Worse All The Time",
    "hyperdrive v": "Hyperdrive (V)",
    "agents of black sun": "Agents Of Black Sun",
    "there is good in him": "There Is Good In Him",
    "skywalker hut": "Let The Wookiee Win (V)",
    "bhbm": "Bring Him Before Me",
    "sycfa": "Set Your Course For Alderaan",
    "profit": "You Can Either Profit By This",
    "hidden base": "Hidden Base",
    "tigih": "This Is Getting Out Of Hand",
    "zero hour": "Zero Hour",
    "mkos": "My Kind Of Scum",
    "my kind of scum": "My Kind Of Scum",
    "hidden path": "The Hidden Path",
    "watto": "Watto's Box",
    "lwww v": "Let The Wookiee Win (V)",
    "communing obi wan": "Communing",
    "communing qui gon": "Communing",
    "wookiees": "Let The Wookiee Win (V)",
    "chewies hut ltwwv": "Let The Wookiee Win (V)",
    "chief chirpas hut ltwwv": "Let The Wookiee Win (V)",
    "chief chirpas hut mains": "Let The Wookiee Win (V)",
    "chief chirpas hut": "Let The Wookiee Win (V)",
    "verge": "On The Verge Of Greatness",
    "verge of greatness": "On The Verge Of Greatness",
    "hoth clones": "Hunt For The Droid General",
    "yavin 4 base ops": "Yavin 4 Base Operations",
    "cct ig": "Carbon Chamber Testing",
    "cct mains": "Carbon Chamber Testing",
    "cct musicians": "Carbon Chamber Testing",
    "ropsv mains": "Ralltiir Operations (V)",
    "chief chirpa mains": "Let The Wookiee Win (V)",
    "hyper profit": "You Can Either Profit By This",
    "desert landing site ssav": "Set Your Course For Alderaan",
    "dagobah cave ssav": "Set Your Course For Alderaan",
    "ds senate": "Senate Occupied",
    "12 card death star": "Set Your Course For Alderaan",
    "mauls chambers ssa": "Set Your Course For Alderaan",
    "dathomir mauls chambers ssav": "Set Your Course For Alderaan",
    "bespin crv": "Combat Readiness (V)",
    "hoth cr v": "Combat Readiness (V)",
    "qui communing": "Communing",
    "rescue the princess v": "Rescue The Princess (V)",
    "hidden base mains": "Hidden Base",
    "endor cp v": "Combat Preparedness (V)",
    "ls combat": "Combat Preparedness",
    "dark combat": "Combat Readiness",
    "coruscant cr v": "Combat Readiness (V)",
    "coruscant crv": "Combat Readiness (V)",
    "5th marker v ssav": "Set Your Course For Alderaan",
    "ih bridge ssav": "Set Your Course For Alderaan",
    "cave ssav": "Set Your Course For Alderaan",
    "hidden base quads": "Hidden Base",
    "ds2 throne room atmd": "Set Your Course For Alderaan",
    "first order ropsv": "Ralltiir Operations (V)",
    "first order rops (V)": "Ralltiir Operations (V)",
    "first order rops v": "Ralltiir Operations (V)",
    "first order rops": "Ralltiir Operations (V)",
    "cotvg": "Court Of The Vile Gangster",
    "coruscant crv tanks": "Combat Readiness (V)",
    "combat 7s": "Combat Preparedness",
    "naboo gungans": "Watch Your Step",
    "trm hdwgitm": "Yavin 4: Massassi Throne Room",
    "invisible hand ssa (V)": "Set Your Course For Alderaan",
    "invisible hand ssa v": "Set Your Course For Alderaan",
    "invisible hand ssa": "Set Your Course For Alderaan",
    "dagobah cave ssa (V)": "Set Your Course For Alderaan",
    "endor chief chirpas hut ltww": "Let The Wookiee Win (V)",
    "syfca": "Set Your Course For Alderaan",
    "ds2 throne room ssa": "Set Your Course For Alderaan",
    "dsiithrone room ssav": "Set Your Course For Alderaan",
    "hoth mains": "Echo Base Operations",
    "hoth cpv": "Combat Preparedness (V)",
    "ls senate": "Senate Occupied",
    "tigih speeders": "This Is Getting Out Of Hand",
    "sycfa brangus": "Set Your Course For Alderaan",
    "ltwwv mains": "Let The Wookiee Win (V)",
    "ltwwv dwell": "Let The Wookiee Win (V)",
    "mwyhl": "Mind What You Have Learned",

    "speeders": "The Empire Knows We're Here",
    "hoth crv": "Combat Readiness (V)",
    "yavin 4 base operations": "Yavin 4 Base Operations",
    "hyperdrive": "The Hyperdrive Generator's Gone (V)",
    "old allies": "Old Allies",
    "aobs": "Agents Of Black Sun",
    "watto": "No Money, No Parts, No Deal!",
    "quiet mining colony": "Quiet Mining Colony",
    "luke saga": "The Force Is Strong In My Family",

    "qmc": "Quiet Mining Colony",
    "yavin 4 operations": "Yavin 4 Operations",
    "throne room": "Yavin 4: Massassi Throne Room",
    "tatooine cpv": "Combat Preparedness (V)",
    "cct": "Carbon Chamber Testing",
    "invasion": "Invasion",
    "rops": "Ralltiir Operations",
    "ropsv": "Ralltiir Operations (V)",
    "rops v": "Ralltiir Operations (V)",
    "ralltiir operations v": "Ralltiir Operations (V)",
    "sc": "Shadow Collective",
    "hd": "Hunt Down And Destroy The Jedi",
    "hdv": "Hunt Down And Destroy The Jedi (V)",
    "hunt down v": "Hunt Down And Destroy The Jedi (V)",
    "ie": "Imperial Entanglements",
    "asm": "A Stunning Move",
    "aobs racing": "Agents Of Black Sun",
    "ltww": "Let The Wookiee Win (V)",
    "ltww mains": "Let The Wookiee Win (V)",
    "ltww space": "Let The Wookiee Win (V)",
    "ltww cch": "Let The Wookiee Win (V)",
    "chief chirpas hut ltww": "Let The Wookiee Win (V)",
    "rendezvous point ltww": "Let The Wookiee Win (V)",
    "qui communing": "Communing",
    "yoda communing": "Communing",
    "communing yoda": "Communing",
    "communing qui gon": "Communing",
    "y4o": "Yavin 4 Operations",
    "y4ops": "Yavin 4 Operations",
    "yavin 4 ops": "Yavin 4 Operations",
    "combat": "Combat Readiness",
    "mbo": "Massassi Base Operations",
    "noidea": "They Have No Idea We're Coming",
    "dark senate": "Senate Occupied",
    "ls senate": "Senate Occupied",
    "ds senate": "Senate Occupied",
    "senate": "Plead My Case To The Senate",
    "mauls chambers ssav": "Set Your Course For Alderaan",
    "mustafar crv": "Combat Readiness (V)",
    "hoth crv": "Combat Readiness (V)",
    "hoth cr": "Combat Readiness",
    "dsii throne room ssav": "Set Your Course For Alderaan",
    "ds2 throne room ssav": "Set Your Course For Alderaan",
    "emperors orders exe ctrl station v ssa": "Emperor's Orders",
    "first order ropsv": "Ralltiir Operations (V)",
    "cct flip": "Carbon Chamber Testing",
    "cct musicians": "Carbon Chamber Testing",
    "cct ig": "Carbon Chamber Testing",
    "verge of greatness": "On The Verge Of Greatness",
    "harvest sense alter control": "Harvest",
    "whap": "We Have A Plan",
    "hb": "Hidden Base",
    "hb mon cals": "Hidden Base",
    "tto": "There Is No Try",
    "map": "I Want That Map",
    "court fo": "Court Of The Vile Gangster",
    "sycfa tractor beams": "Set Your Course For Alderaan",
    "sycfa brangus": "Set Your Course For Alderaan",
    "hyperdrive v": "The Hyperdrive Generator's Gone (V)",
    "jakku cpv": "Combat Preparedness (V)",
    "tatooine cr v": "Combat Readiness (V)",
    "tatooine cp v": "Combat Preparedness (V)",
    "endor cp v": "Combat Preparedness (V)",
    "bespin crv": "Combat Readiness (V)",
    "5th marker v ssa": "Set Your Course For Alderaan",
    "cave ssa": "Set Your Course For Alderaan",
    "ih bridge ssa": "Set Your Course For Alderaan",
    "desert landing site ssa": "Set Your Course For Alderaan",
    "hunt down dueling": "Hunt Down And Destroy The Jedi",
    "hunt down racing": "Hunt Down And Destroy The Jedi",
    "endor ops": "Endor Operations",
    "endor cpv": "Combat Preparedness (V)",
    "senate gungans": "Plead My Case To The Senate",
    "jcc mains": "Watch Your Step",
    "5th marker v ssa v": "Set Your Course For Alderaan",
    "5th marker v ssa": "Set Your Course For Alderaan",
}

OCS_ORDER = {
    "Finals": ["Patrick Johnson", "Greg Shaw"],
    "Semifinals": ["Patrick Johnson", "Matthew Harrison-Trainor", "Greg Shaw", "Joe Olson"],
    "Quarterfinals": [
        "Matthew Harrison-Trainor",
        "Brad Kippel",
        "Patrick Johnson",
        "Kyle Krueger",
        "Joe Olson",
        "Anthony Howard",
        "Greg Shaw",
        "Jarad Konsker",
    ],
    "Top 16": [
        "Matthew Harrison-Trainor",
        "Conor Britain",
        "Brad Kippel",
        "Patrik Csapi",
        "Patrick Johnson",
        "Jeff Lavigne",
        "Kyle Krueger",
        "Timo Dusel",
        "Joe Olson",
        "Justin Desai",
        "Anthony Howard",
        "Casey Anis",
        "Jarad Konsker",
        "Sam Tashima",
        "Greg Shaw",
        "Ryan Jellison",
    ],
}
EURO_T4 = ["Emil Wallin", "Justin Branch", "Patrik Csapi", "Cedrik Vanderhaegen"]
EURO_D1 = [
    "Emil Wallin",
    "Patrik Csapi",
    "Cedrik Vanderhaegen",
    "Justin Branch",
    "Jonas Hagen Nørregaard",
    "Casper Jørgensen",
    "Floris de Vries",
    "Koen Meijssen",
    "Timo Dusel",
    "Jon Benkert Holtet",
    "Erik Spijksma",
    "Marvin Tegeler",
    "Chris Menzel",
    "Martin den Boef",
    "John Moorley",
    "Kevin Jaap",
    "Julian Smolarek",
]
JAWA_ORDER = {
    "Finals": ["Justin Miyashiro", "Andrew Moss"],
    "Top 4": ["Justin Miyashiro", "Andrew Moss", "Justin Branch", "Jason Riendeau"],
    "Top 8": [
        "Justin Miyashiro",
        "Andrew Moss",
        "Justin Branch",
        "Jason Riendeau",
        "Chris Kelly",
        "Matt Sokol",
        "Sean Luhks",
        "Bill Bacheler",
    ],
}


def pretty_name(slug: str) -> str:
    if slug in NAME:
        return NAME[slug]
    return " ".join(w.capitalize() for w in slug.split("-"))


def pretty_obj(slug: str) -> str:
    s = slug.replace("-", " ")
    s = re.sub(r"\((v)\)", "(V)", s, flags=re.I)
    s = re.sub(r"(?<!\()\bv\b(?!\))", "(V)", s, flags=re.I)
    return s


def parse_url(url: str):
    slug = url.rstrip("/").split("/")[-1].lower()
    m = re.search(r"-(ds|ls)-(.+)$", slug)
    if not m:
        return None
    side = m.group(1).upper()
    obj = pretty_obj(m.group(2))
    left = slug[: m.start()]
    rm = re.match(r"(\d{4})-([a-z0-9-]+)-regionals-(.+)$", left)
    if rm:
        year, planet, player_slug = rm.groups()
        planet_title = PLANET_NAME.get(planet, pretty_name(planet))
        event = f"{year} Regional Championships"
        return event, planet_title, False, year, pretty_name(player_slug), side, obj, url
    for pref, event, stage, t8, year in PREFIXES:
        if left.startswith(pref):
            rest = left[len(pref) :]
            player = pretty_name(rest.strip("-"))
            return event, stage, t8, year, player, side, obj, url
    return None


def deck_title(event, stage, player, side, obj):
    if event.endswith("Regional Championships"):
        year = event.split()[0]
        return f"{year} {stage} Regionals {player} {side} {obj}"
    short = {
        "2025 Online Championship Series Playoffs": "2025 OCS",
        "2025 European Championship": "2025 European Championship",
        "2025 Las Vegas Grand Prix": "2025 LVGP",
        "2026 Jawa Cup": "2026 Jawa Cup",
        "2026 Retro U.S. Nationals": "2026 Retro U.S. Nationals",
    }[event]
    st = "" if stage in ("Day 1", "Swiss", "constructed") else stage + " "
    return f"{short} {st}{player} {side} {obj}"


def wiki_fname(title: str) -> str:
    return title.replace(" ", "_").replace("/", "_") + ".wiki"


def format_for(event: str) -> str:
    if event == "2026 Jawa Cup":
        return "[[Jawa]]"
    if event == "2026 Retro U.S. Nationals":
        return "[[Premiere - Death Star II]]"
    return "[[Open]]"


def polish_hub(hub: str | None, obj: str) -> str:
    if not hub:
        hub = obj
    key = obj.strip().lower()
    if hub.lower() == key or hub[:1].islower() or hub == obj:
        return SLANG_HUB.get(key, hub)
    return hub


def replace_section(text: str, headings: tuple[str, ...], new_heading: str, body: str) -> str:
    alt = "|".join(re.escape(h) for h in headings)
    pat = rf"== (?:{alt}) ==\n.*?(?=\n== )"
    repl = f"== {new_heading} ==\n\n{body}\n\n"
    new, n = re.subn(pat, repl, text, count=1, flags=re.S)
    if n:
        return new
    if "== See also ==" in text:
        return text.replace("== See also ==", f"== {new_heading} ==\n\n{body}\n\n== See also ==", 1)
    return text + f"\n== {new_heading} ==\n\n{body}\n"


def ordered_players(stage_map: dict, preferred: list[str]) -> list[str]:
    seen = []
    for p in preferred:
        if p in stage_map and p not in seen:
            seen.append(p)
    for p in stage_map:
        if p not in seen:
            seen.append(p)
    return seen


def wikitable(headers: list[str], rows: list[list[str]], sortable: bool = False) -> str:
    cls = 'class="wikitable sortable"' if sortable else 'class="wikitable"'
    bits = ["{|" + f" {cls}", "! " + " !! ".join(headers)]
    for row in rows:
        bits += ["|-", "| " + " || ".join(row)]
    bits.append("|}")
    return "\n".join(bits)


def main():
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    urls = []
    for path in URL_FILES:
        if path.exists():
            urls.extend(ln.strip() for ln in path.read_text(encoding="utf-8").splitlines() if ln.strip())
    parsed = []
    for url in urls:
        info = parse_url(url)
        if not info:
            print("SKIPURL", url)
            continue
        event, stage, t8, year, player, side, obj, url = info
        html = DECKS / (url.rstrip("/").split("/")[-1] + ".html")
        if not html.exists():
            print("NOFILE", html.name)
            continue
        counts, cards = ge.parse_pc_html(html)
        if sum(counts.values()) < 10:
            print("THIN", html.name, sum(counts.values()))
            continue
        parsed.append((event, stage, t8, year, player, side, obj, url, counts, cards))

    deck_pages = {}
    hub_labels = {}
    pages_for = defaultdict(list)
    for event, stage, t8, year, player, side, obj, url, counts, cards in parsed:
        title = deck_title(event, stage, player, side, obj)
        deck_pages[(event, stage, player, side, obj)] = title
        pages_for[(event, stage, player, side)].append(title)

    for event, stage, t8, year, player, side, obj, url, counts, cards in parsed:
        other = "LS" if side == "DS" else "DS"
        companion = None
        others = pages_for.get((event, stage, player, other)) or []
        if others:
            companion = others[0]
        ge.EVENT_TITLE = event
        ge.deck_page_title = lambda p, t, s, o, event=event, stage=stage: deck_title(
            event, stage, p, s, o
        )
        title, body, hub = ge.render_deck(
            player, t8, side, obj, counts, cards, url, companion, dests, title_map, bp
        )
        hub = polish_hub(hub, obj)
        body = body.replace("[[Category:2026]]", f"[[Category:{year}]]")
        body = body.replace("* [[European Championships]]", "* [[List of SWCCG tournaments]]")
        body = body.replace(f"* '''Stage:''' {'Top 8' if t8 else 'Day 1'}", f"* '''Stage:''' {stage}")
        body = body.replace("* '''Format:''' [[Open]]", f"* '''Format:''' {format_for(event)}")
        (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
        hub_labels[title] = hub
        print("deck", title, "->", hub, "n", sum(counts.values()))

    def cell(event, stage, player, side):
        titles = pages_for.get((event, stage, player, side)) or []
        if not titles:
            return "—"
        bits = []
        for page in titles:
            bits.append(f"[[{page}|{hub_labels.get(page, page)}]]")
        return " · ".join(bits)

    def players_in(event, stage):
        out = []
        for e, st, t8, year, player, side, obj, url, counts, cards in parsed:
            if e == event and st == stage and player not in out:
                out.append(player)
        return out

    ocs = PAGES / "2025_Online_Championship_Series_Playoffs.wiki"
    if ocs.exists():
        ev = "2025 Online Championship Series Playoffs"
        rows = []
        for st in ("Finals", "Semifinals", "Quarterfinals", "Top 16"):
            for p in ordered_players({x: 1 for x in players_in(ev, st)}, OCS_ORDER.get(st, [])):
                rows.append([st, f"[[{p}]]", cell(ev, st, p, "DS"), cell(ev, st, p, "LS")])
        table = wikitable(["Round", "Player", "Dark", "Light"], rows)
        text = replace_section(ocs.read_text(encoding="utf-8"), ("Bracket", "Decklists"), "Decklists", table)
        ocs.write_text(text, encoding="utf-8", newline="\n")

    euro = PAGES / "2025_European_Championship.wiki"
    if euro.exists():
        ev = "2025 European Championship"

        def ptab(heading, preferred, stage, sortable=True):
            rows = []
            for i, p in enumerate(ordered_players({x: 1 for x in players_in(ev, stage)}, preferred), 1):
                rows.append([str(i), f"[[{p}]]", cell(ev, stage, p, "DS"), cell(ev, stage, p, "LS")])
            return wikitable([heading, "Player", "Dark", "Light"], rows, sortable=sortable)

        text = euro.read_text(encoding="utf-8")
        text = replace_section(text, ("Top 4",), "Top 4", ptab("Finish", EURO_T4, "Top 4"))
        text = replace_section(text, ("Day 1",), "Day 1", ptab("Day 1", EURO_D1, "Day 1"))
        euro.write_text(text, encoding="utf-8", newline="\n")

    jawa = PAGES / "2026_Jawa_Cup.wiki"
    if jawa.exists():
        ev = "2026 Jawa Cup"
        rows = []
        for st in ("Finals", "Top 4", "Top 8", "Swiss"):
            for p in ordered_players({x: 1 for x in players_in(ev, st)}, JAWA_ORDER.get(st, [])):
                rows.append([st, f"[[{p}]]", cell(ev, st, p, "DS"), cell(ev, st, p, "LS")])
        table = wikitable(["Stage", "Player", "Dark", "Light"], rows)
        text = replace_section(jawa.read_text(encoding="utf-8"), ("Bracket", "Decklists"), "Decklists", table)
        jawa.write_text(text, encoding="utf-8", newline="\n")

    retro = PAGES / "2026_Retro_U.S._Nationals.wiki"
    if retro.exists():
        ev = "2026 Retro U.S. Nationals"
        preferred = ["Jonny Chu"]
        rows = []
        for i, p in enumerate(ordered_players({x: 1 for x in players_in(ev, "constructed")}, preferred), 1):
            rows.append([str(i), f"[[{p}]]", cell(ev, "constructed", p, "DS"), cell(ev, "constructed", p, "LS")])
        table = "Finish as published.\n\n" + wikitable(
            ["Finish", "Player", "Dark", "Light"], rows, sortable=True
        )
        text = replace_section(
            retro.read_text(encoding="utf-8"), ("Results",), "Results", table
        )
        retro.write_text(text, encoding="utf-8", newline="\n")

    for year in ("2025", "2026"):
        hubp = PAGES / f"{year}_Regional_Championships.wiki"
        if not hubp.exists():
            continue
        ev = f"{year} Regional Championships"
        found = []
        for e, st, t8, y, player, side, obj, url, counts, cards in parsed:
            if e == ev and st not in found:
                found.append(st)
        preferred = {
            "2025": ["Coruscant", "Corellia", "Nal Hutta", "Tatooine", "Endor", "Bespin", "Naboo"],
            "2026": ["Nal Hutta", "Endor", "Yavin 4", "Bespin", "Naboo", "Ryloth"],
        }[year]
        planets = ordered_players({p: 1 for p in found}, preferred)
        if not planets:
            continue
        chunks = ["Published constructed lists as posted on the PC results page."]
        for planet in planets:
            rows = []
            for p in players_in(ev, planet):
                rows.append([f"[[{p}]]", cell(ev, planet, p, "DS"), cell(ev, planet, p, "LS")])
            chunks.append(
                f"=== {planet} Regionals ===\n\n"
                + wikitable(["Player", "Dark", "Light"], rows, sortable=True)
            )
        body = "\n\n".join(chunks)
        text = hubp.read_text(encoding="utf-8")
        text = replace_section(text, ("Decklists",), "Decklists", body)
        hubp.write_text(text, encoding="utf-8", newline="\n")

    print("html decks", len(parsed))


if __name__ == "__main__":
    main()
