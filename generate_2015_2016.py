#!/usr/bin/env python3
"""2015–2016 tournament hubs from PC wrap lists + dest slang → printed titles."""
from __future__ import annotations

import html as htmlmod
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_html_missing as hm  # noqa: E402
from generate_2019_2021 import (  # noqa: E402
    TOKEN,
    is_bio,
    is_junk_player,
    refs,
    tidy_player_page,
    wiki_fname,
)
from generate_2026_remaining import upsert_stub  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
WRAP = ROOT / "encyclopedia" / "pc-2015-2016"
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
EC = PAGES / "European_Championships.wiki"
TSV = ROOT / "y2015-2016-titles.tsv"

CANON = dict(TOKEN)
CANON.update(
    {
        "Emil Wallen": "Emil Wallin",
        "Johnny Chu": "Jonny Chu",
        "Casper Jørgenson": "Casper Jørgensen",
        "Casper Jorgenson": "Casper Jørgensen",
        "Casper Jorgensen": "Casper Jørgensen",
        "Quirin Furgut": "Quirin Fürgut",
        "Quirin Fuergut": "Quirin Fürgut",
        "Cedrik Vanderhagen": "Cedrik Vanderhaegen",
        "Jonas Hagen": "Jonas Hagen Nørregaard",
        "Jonas Norregaard": "Jonas Hagen Nørregaard",
        "Jonas Nørregaard": "Jonas Hagen Nørregaard",
        "John Morley": "John Moorley",
        "Jan Bereuda": "Jan Berueda",
        "Jason Reindeau": "Jason Riendeau",
        "Kyle Kreuger": "Kyle Krueger",
        "Steve Cellucci": "Stephen Cellucci",
        "Brian Mischke": "Bryan Mischke",
        "Mike D’amboise": "Mike d'Amboise",
        "Mike D'amboise": "Mike d'Amboise",
        "Trevor Partidge": "Trevor Partridge",
        "Trevor Patridge": "Trevor Partridge",
        "Matthew Carulli": "Matt Carulli",
        "Pat Johnson": "Patrick Johnson",
        "György (Bill)": "György Póra",
        "Gyorgy (Bill)": "György Póra",
        "Pete the Welsh": "Peter Rowlands",
        "Jimmy Falleans": "Jimmy Faelens",
        "Noah Falleans": "Noah Faelens",
        "Julian-Adres Smolarek": "Julian Smolarek",
        "Julian-Andrés Smolarek": "Julian Smolarek",
        "Julien Schmolarik": "Julian Smolarek",
        "Jonas Jukubowski": "Jonas Jakubowski",
        "David Luhaær": "David Luhaær",
        "Zeimowit Skwara": "Ziemowit Skwara",
        "Stephen Skilton": "Steve Skilton",
        "Steve Skilton": "Steve Skilton",
        "Michael Richards": "Mike Richards",
        "Michael Turner": "Mike Turner",
        "Joseph Phillips": "Joe Phillips",
        "Joseph Graham": "Joseph Graham",
        "Sandwhirl": "Sandwhirl",
        "Alex T.": "Alex T.",
        "Kent L.": "Kent Larsen",
        "Piotr Dash_R": "Piotr Dash_R",
        "Clint Menzel": "Clint Menzel",
        "Adam Kwart": "Adam Kwart",
        "Pete Srodoski": "Pete Srodoski",
        "Caleb Foth": "Caleb Foth",
        "Frank Lam": "Frank Lam",
        "Brandon Bunn": "Brandon Bunn",
        "Vince Hutchins": "Vince Hutchins",
        "Joel Pittman": "Joel Pittman",
        "Ross Littauer": "Ross Littauer",
        "Cyrus Morosoff": "Cyrus Morosoff",
        "Travis Egan": "Travis Egan",
        "Mike French": "Mike French",
        "Colin Wellborn": "Colin Wellborn",
        "Greyson Thompson": "Greyson Thompson",
        "Kyle Szklenski": "Kyle Szklenski",
        "Ryan Obman": "Ryan Obman",
        "Vinny Rossi": "Vinny Rossi",
        "Jon McFarland": "Jon McFarland",
        "Michael Tomashewski": "Michael Tomashewski",
        "Nick Amato": "Nick Amato",
        "John Michael Earwood": "John Michael Earwood",
        "Mike Gemme": "Mike Gemme",
        "Matt Schmaltz": "Matt Schmaltz",
        "Mark Sebring": "Mark Sebring",
        "Seth Acree": "Seth Acree",
        "James Barnes": "James Barnes",
        "Jonathan Bauer": "Jonathan Bauer",
        "William Ament": "William Ament",
        "Ethan Phou": "Ethan Phou",
        "Fernando Souza": "Fernando Souza",
        "Stephen Fulner": "Stephen Fulner",
        "Benedict Donnay": "Benedict Donnay",
        "Andrew Sauvageau": "Andrew Sauvageau",
        "Andrew Kline": "Andrew Kline",
        "Charlie Herren": "Charlie Herren",
        "Jeff Visseaux": "Jeff Visseaux",
        "Gerald Sieber": "Gerald Sieber",
        "Jerome Nitschke": "Jerome Nitschke",
        "Tobias Bukkehave": "Tobias Bukkehave",
        "Rasmus Juul": "Rasmus Juul",
        "Darren Malins": "Darren Malins",
        "Jon Holtet": "Jon Benkert Holtet",
        "Jon Benkert Holtet": "Jon Benkert Holtet",
        "Mike Rosenberger": "Mike Rosenberger",
        "Christopher Claßen": "Christopher Claßen",
        "Christopher Claẞen": "Christopher Claßen",
        "Stefan Boersma": "Stefan Boersma",
        "Martin Sommer": "Martin Sommer",
        "Massimiliano Colussi": "Massimiliano Colussi",
        "Pete Rowlins": "Peter Rowlands",
        "Ulli Reuter": "Ulli Reuter",
        "Ralf Wachowiak": "Ralf Wachowiak",
        "Oliver Wielicki": "Oliver Wielicki",
        "Tilmann Petersen": "Tilmann Petersen",
        "Nelson Cazon": "Nelson Cazon",
        "Julian Konrad": "Julian Konrad",
        "Jonas Jacobsen": "Jonas Jacobsen",
        "Jordi Paul": "Jordi Paul",
        "Bertrand Momal": "Bertrand Momal",
        "Amar Banger": "Amar Banger",
        "Alexander Sheynis": "Alexander Sheynis",
        "Gibson Yim": "Gibson Yim",
        "Brandon Baity": "Brandon Baity",
        "Matt Thornton": "Matt Thornton",
        "Matt Wadden": "Matt Wadden",
        "Jeff Scales": "Jeffrey Scales",
        "Jeffrey Scales": "Jeffrey Scales",
        "Pat Johnson": "Patrick Johnson",
        "Joe Giannetti": "Joe Giannetti",
        "Joe Gianetti": "Joe Giannetti",
        "Westergaard": "Jan Westergard",
        "Jan Westergaard": "Jan Westergard",
        "Aesen": "Phil Aasen",
        "Bolletino": "Andrew Bollentino",
        "Andrew Bolletino": "Andrew Bollentino",
        "Gianetti": "Joe Giannetti",
        "Terwilleger": "Brian Terwilliger",
        "d'Ambroise": "Mike d'Amboise",
        "d’Ambroise": "Mike d'Amboise",
        "Mike d'Ambroise": "Mike d'Amboise",
        "Mike D'Ambroise": "Mike d'Amboise",
        "Patrick M": "Patrick Johnson",
        "Patrick M Johnson": "Patrick Johnson",
        "Johnson, Patrick M": "Patrick Johnson",
        "tWelsh Pete": "Peter Rowlands",
        "tWelsh, Pete": "Peter Rowlands",
        "Rowlands, tWelsh, Pete": "Peter Rowlands",
        "Pete Rowlands": "Peter Rowlands",
        "Pete the Welsh": "Peter Rowlands",
        "Yaeger Steve": "Steve Yaeger",
        "Steve Yaeger": "Steve Yaeger",
        "Lush Matt": "Matt Lush",
        "Kyle Kreuger": "Kyle Krueger",
        "Walf Wachowiak": "Ralf Wachowiak",
        "Wachowiak, Walf": "Ralf Wachowiak",
        "Christopher Claben": "Christopher Claßen",
        "Claben, Christopher": "Christopher Claßen",
        "Moritz Krage": "Moritz Karge",
        "Krage, Moritz": "Moritz Karge",
        "Steve Skilton": "Stephen Skilton",
        "Skilton, Steve": "Stephen Skilton",
        "Faellens, Jimmy": "Jimmy Faelens",
        "Jimmy Faellens": "Jimmy Faelens",
        "Den Boef, Martin": "Martin den Boef",
        "Martin Den Boef": "Martin den Boef",
        "de Vries, Floris": "Floris de Vries",
        "Floris de Vries": "Floris de Vries",
        "Dufreney, Franck": "Franck Dufreney",
        "Franck Dufreney": "Franck Dufreney",
        "Johnny Chu": "Jonny Chu",
        "Chu, Johnny": "Jonny Chu",
        "Brian Mischke": "Bryan Mischke",
        "Mischke, Brian": "Bryan Mischke",
        "Nabroo CRv": "Nabroo CRv",
        "Zeimowit Skwara": "Ziemowit Skwara",
        "Skwara, Zeimowit": "Ziemowit Skwara",
        "Jonas Hagen": "Jonas Hagen Nørregaard",
        "Norregaard, Jonas Hagen": "Jonas Hagen Nørregaard",
        "Jonas Hagen Norregaard": "Jonas Hagen Nørregaard",
        "Julian-Andres Smolarek": "Julian Smolarek",
        "Smolarek, Julian-Andres": "Julian Smolarek",
        "Smolarek, Julian-Andrés": "Julian Smolarek",
        "Vanderhagen, Cedrik": "Cedrik Vanderhaegen",
        "Cedrik Vanderhagen": "Cedrik Vanderhaegen",
        "John Morley": "John Moorley",
        "Moorley, John": "John Moorley",
        "Morley, John": "John Moorley",
        "Stephen Cellucci": "Stephen Cellucci",
        "Steve Cellucci": "Stephen Cellucci",
        "Cellucci, Steve": "Stephen Cellucci",
        "Charlie Arlandson": "Charlie Arlandson",
        "Arlandson, Charlie": "Charlie Arlandson",
        "Andrew Bollentino": "Andrew Bollentino",
        "Bollentino, Andrew": "Andrew Bollentino",
        "Joe Giannetti": "Joe Giannetti",
        "Giannetti, Joe": "Joe Giannetti",
        "Phil Aasen": "Phil Aasen",
        "Aasen, Phil": "Phil Aasen",
        "Mark Walseth": "Mark Walseth",
        "Walseth, Mark": "Mark Walseth",
        "Matt Harrison-Trainor": "Matthew Harrison-Trainor",
        "Harrison-Trainor, Matt": "Matthew Harrison-Trainor",
        "Matthew Harrison-Trainor": "Matthew Harrison-Trainor",
        "Kevin Shannon": "Kevin Shannon",
        "Shannon, Kevin": "Kevin Shannon",
        "Chris Terwilliger": "Chris Terwilliger",
        "Terwilliger, Chris": "Chris Terwilliger",
        "Brian Terwilliger": "Brian Terwilliger",
        "Terwilliger, Brian": "Brian Terwilliger",
        "Cole Lepine": "Cole Lepine",
        "Lepine, Cole": "Cole Lepine",
        "Steve Brentson": "Steve Brentson",
        "Clayton Atkin": "Clayton Atkin",
        "Mike Pistone": "Mike Pistone",
        "Keith Brown": "Keith Brown",
        "Paul Bansal": "Paul Bansal",
        "Tony Garcia": "Tony Garcia",
        "Dan Tartaglione": "Dan Tartaglione",
        "Barry Alperstein": "Barry Alperstein",
        "Joe Gagliardi": "Joe Gagliardi",
        "Matt Spear": "Matt Spear",
        "Frank Walsh": "Frank Walsh",
        "Jeffrey Johns": "Jeffrey Johns",
        "Arvind Bhaskar": "Arvind Bhaskar",
        "Tom Schwarz": "Tom Schwarz",
        "Gabe Taylor": "Gabe Taylor",
        "Drew Powers": "Drew Powers",
        "Sean Miller": "Sean Miller",
        "Mitch Nieland": "Mitch Nieland",
        "Stephen Kim": "Stephen Kim",
        "Aaron Kingery": "Aaron Kingery",
        "Jake Nelson": "Jake Nelson",
        "Bill Kafer": "Bill Kafer",
        "Jarad Konsker": "Jarad Konsker",
        "Wojtek Wisniewski": "Wojtek Wisniewski",
        "Wisniewski, Wojtek": "Wojtek Wisniewski",
        "Marc Nickels": "Marc Nickels",
        "Nickels, Marc": "Marc Nickels",
        "Lukasz Saczek": "Lukasz Saczek",
        "Saczek, Lukasz": "Lukasz Saczek",
        "Robert Smolarek": "Robert Smolarek",
        "Smolarek, Robert": "Robert Smolarek",
        "Nico Oster": "Nico Oster",
        "Oster, Nico": "Nico Oster",
        "Tamas Papp": "Tamas Papp",
        "Papp, Tamas": "Tamas Papp",
        "Jesper Gravesen": "Jesper Gravesen",
        "Gravesen, Jesper": "Jesper Gravesen",
        "Piotr Ptak": "Piotr Ptak",
        "Ptak, Piotr": "Piotr Ptak",
        "Eric Spijksma": "Eric Spijksma",
        "Spijksma, Eric": "Eric Spijksma",
        "Tony DaCosta": "Tony DaCosta",
        "DaCosta, Tony": "Tony DaCosta",
        "Gosse Zeilstra": "Gosse Zeilstra",
        "Zeilstra, Gosse": "Gosse Zeilstra",
        "Jordi Brainschat": "Jordi Brainschat",
        "Brainschat, Jordi": "Jordi Brainschat",
        "Kent Larsen": "Kent Larsen",
        "Larsen, Kent": "Kent Larsen",
        "Ryan Freeman": "Ryan Freeman",
        "Freeman, Ryan": "Ryan Freeman",
        "Kristian Lund": "Kristian Lund",
        "Lund, Kristian": "Kristian Lund",
        "Sam Olson": "Sam Olson",
        "Olson, Sam": "Sam Olson",
        "Steve Yaeger": "Steve Yaeger",
        "Yaeger, Steve": "Steve Yaeger",
        "Matt Lush": "Matt Lush",
        "Lush, Matt": "Matt Lush",
        "Jim Li": "Jim Li",
        "Li, Jim": "Jim Li",
        "Nick Reisch": "Nick Reisch",
        "Reisch, Nick": "Nick Reisch",
        "Jacy Smith": "Jacy Smith",
        "Smith, Jacy": "Jacy Smith",
        "Dennis Reinhardt": "Dennis Reinhardt",
        "Reinhardt, Dennis": "Dennis Reinhardt",
        "Tim Culver": "Tim Culver",
        "Culver, Tim": "Tim Culver",
        "Marvin Tegeler": "Marvin Tegeler",
        "Tegeler, Marvin": "Marvin Tegeler",
        "Kevin Jaap": "Kevin Jaap",
        "Jaap, Kevin": "Kevin Jaap",
        "Paul McPherson": "Paul McPherson",
        "McPherson, Paul": "Paul McPherson",
        "Patrik Csapi": "Patrik Csapi",
        "Csapi, Patrik": "Patrik Csapi",
        "Piotr Jarnot": "Piotr Jarnot",
        "Jarnot, Piotr": "Piotr Jarnot",
        "James Barnes": "James Barnes",
        "Barnes, James": "James Barnes",
        "Scott Lingrell": "Scott Lingrell",
        "Lingrell, Scott": "Scott Lingrell",
        "Wayne Cullen": "Wayne Cullen",
        "Cullen, Wayne": "Wayne Cullen",
        "Chris Westergard": "Chris Westergard",
        "Westergard, Chris": "Chris Westergard",
        "Jan Westergard": "Jan Westergard",
        "Westergard, Jan": "Jan Westergard",
        "Angelo Consoli": "Angelo Consoli",
        "Consoli, Angelo": "Angelo Consoli",
        "David Destefanis": "David Destefanis",
        "Destefanis, David": "David Destefanis",
        "Casper Jorgensen": "Casper Jørgensen",
        "Jorgensen, Casper": "Casper Jørgensen",
        "Jørgensen, Casper": "Casper Jørgensen",
        "Jonas Jakubowski": "Jonas Jakubowski",
        "Jakubowski, Jonas": "Jonas Jakubowski",
        "Koen Meijssen": "Koen Meijssen",
        "Meijssen, Koen": "Koen Meijssen",
        "Jon Holtet": "Jon Benkert Holtet",
        "Holtet, Jon": "Jon Benkert Holtet",
        "Chris Menzel": "Chris Menzel",
        "Menzel, Chris": "Chris Menzel",
        "Tobias Bukkehave": "Tobias Bukkehave",
        "Bukkehave, Tobias": "Tobias Bukkehave",
        "Rasmus Juul": "Rasmus Juul",
        "Juul, Rasmus": "Rasmus Juul",
        "Massimiliano Colussi": "Massimiliano Colussi",
        "Colussi, Massimiliano": "Massimiliano Colussi",
        "Jordi Paul": "Jordi Paul",
        "Paul, Jordi": "Jordi Paul",
        "Jerome Nitschke": "Jerome Nitschke",
        "Nitschke, Jerome": "Jerome Nitschke",
        "Franck Dufreney": "Franck Dufreney",
        "Martin den Boef": "Martin den Boef",
        "Ralf Wachowiak": "Ralf Wachowiak",
        "Floris de Vries": "Floris de Vries",
        "Christopher Claßen": "Christopher Claßen",
        "Claßen, Christopher": "Christopher Claßen",
        "Moritz Karge": "Moritz Karge",
        "Karge, Moritz": "Moritz Karge",
        "Ziemowit Skwara": "Ziemowit Skwara",
        "Skwara, Ziemowit": "Ziemowit Skwara",
        "Jimmy Faelens": "Jimmy Faelens",
        "Faelens, Jimmy": "Jimmy Faelens",
        "Stephen Skilton": "Stephen Skilton",
        "Skilton, Stephen": "Stephen Skilton",
        "Tom Haid": "Tom Haid",
        "Haid, Tom": "Tom Haid",
        "Reid Smith": "Reid Smith",
        "Smith, Reid": "Reid Smith",
        "Emil Wallin": "Emil Wallin",
        "Wallin, Emil": "Emil Wallin",
        "Justin Desai": "Justin Desai",
        "Desai, Justin": "Justin Desai",
        "Jonny Chu": "Jonny Chu",
        "Chu, Jonny": "Jonny Chu",
        "Tom Kelly": "Tom Kelly",
        "Kelly, Tom": "Tom Kelly",
        "Casey Anis": "Casey Anis",
        "Anis, Casey": "Casey Anis",
        "Joe Olson": "Joe Olson",
        "Olson, Joe": "Joe Olson",
        "Brian Fred": "Brian Fred",
        "Fred, Brian": "Brian Fred",
        "Matt Sokol": "Matt Sokol",
        "Sokol, Matt": "Matt Sokol",
        "Greg Shaw": "Greg Shaw",
        "Shaw, Greg": "Greg Shaw",
        "Steve Baroni": "Steve Baroni",
        "Baroni, Steve": "Steve Baroni",
        "Andy Wexsetten": "Andy Wexstten",
        "Wexsetten, Andy": "Andy Wexstten",
        "Andy Wexstten": "Andy Wexstten",
        "Thomas Whaley": "Thomas Whaley",
        "Whaley, Thomas": "Thomas Whaley",
        "Chad Mears": "Chad Mears",
        "Mears, Chad": "Chad Mears",
        "Matt Wadden": "Matt Wadden",
        "Wadden, Matt": "Matt Wadden",
        "Jonathan Bauer": "Jonathan Bauer",
        "Bauer, Jonathan": "Jonathan Bauer",
        "Brian Speight": "Brian Speight",
        "Speight, Brian": "Brian Speight",
        "Robbie Hendon": "Robbie Hendon",
        "Hendon, Robbie": "Robbie Hendon",
        "Mike French": "Mike French",
        "French, Mike": "Mike French",
        "Evan Kirkpatrick": "Evan Kirkpatrick",
        "Kirkpatrick, Evan": "Evan Kirkpatrick",
        "Nathan Trothing": "Nathan Trothing",
        "Trothing, Nathan": "Nathan Trothing",
        "Steve Miller": "Steve Miller",
        "Miller, Steve": "Steve Miller",
        "Geoff Dearing": "Geoff Dearing",
        "Dearing, Geoff": "Geoff Dearing",
        "Derek Chng": "Derek Chng",
        "Chng, Derek": "Derek Chng",
        "Todd Johnson": "Todd Johnson",
        "Johnson, Todd": "Todd Johnson",
        "Jerry Heine": "Jerry Heine",
        "Heine, Jerry": "Jerry Heine",
        "Brian Herold": "Brian Herold",
        "Herold, Brian": "Brian Herold",
        "Anthony Howard": "Anthony Howard",
        "Howard, Anthony": "Anthony Howard",
        "Jeb Benthin": "Jeb Benthin",
        "Benthin, Jeb": "Jeb Benthin",
        "Jeremy Gardner": "Jeremy Gardner",
        "Gardner, Jeremy": "Jeremy Gardner",
        "Jonathan Murray": "Jonathan Murray",
        "Murray, Jonathan": "Jonathan Murray",
        "Brandon Romano": "Brandon Romano",
        "Romano, Brandon": "Brandon Romano",
        "Camden Yanaga": "Camden Yanaga",
        "Yanaga, Camden": "Camden Yanaga",
        "Scott Diehl": "Scott Diehl",
        "Diehl, Scott": "Scott Diehl",
        "Matt Thornton": "Matt Thornton",
        "Thornton, Matt": "Matt Thornton",
        "Joe Phillips": "Joe Phillips",
        "Phillips, Joe": "Joe Phillips",
        "Michael Erisman": "Michael Erisman",
        "Erisman, Michael": "Michael Erisman",
        "David Beaubier": "David Beaubier",
        "Beaubier, David": "David Beaubier",
        "Matt Paragano": "Matt Paragano",
        "Paragano, Matt": "Matt Paragano",
        "Russell Chou": "Russell Chou",
        "Chou, Russell": "Russell Chou",
        "Bryan Gravener": "Bryan Gravener",
        "Gravener, Bryan": "Bryan Gravener",
        "John Veasey": "John Veasey",
        "Veasey, John": "John Veasey",
        "Arvind Bhaskar": "Arvind Bhaskar",
        "Bhaskar, Arvind": "Arvind Bhaskar",
        "Martin den Boef": "Martin den Boef",
        "Martin Boef": "Martin den Boef",
        "Boef, Martin": "Martin den Boef",
        "Floris Vries": "Floris de Vries",
        "Vries, Floris": "Floris de Vries",
        "Travis Egan": "Travis Egan",
        "Egan, Travis": "Travis Egan",
    }
)

SLANG = {
    "tto": "Endor Operations",
    "eops": "Endor Operations",
    "eop": "Endor Operations",
    "endor ops": "Endor Operations",
    "endor operations": "Endor Operations",
    "that thing's operational": "Endor Operations",
    "ie": "Imperial Entanglements",
    "ie mains": "Imperial Entanglements",
    "imperial entanglements": "Imperial Entanglements",
    "map": "I Want That Map",
    "aobs": "Agents Of Black Sun",
    "black sun": "Agents Of Black Sun",
    "court": "Court Of The Vile Gangster",
    "court mains": "Court Of The Vile Gangster",
    "court scum": "Court Of The Vile Gangster",
    "cotvg": "Court Of The Vile Gangster",
    "cotvg mains": "Court Of The Vile Gangster",
    "first order court": "Court Of The Vile Gangster",
    "hd": "Hunt Down And Destroy The Jedi",
    "hdadtj": "Hunt Down And Destroy The Jedi",
    "hunt down": "Hunt Down And Destroy The Jedi",
    "fo hd": "Hunt Down And Destroy The Jedi",
    "hd tanks": "Hunt Down And Destroy The Jedi",
    "isb": "ISB Operations",
    "bhbm": "Bring Him Before Me",
    "cct": "Carbon Chamber Testing",
    "cct scum": "Carbon Chamber Testing",
    "cct ig": "Carbon Chamber Testing",
    "cct ig-88": "Carbon Chamber Testing",
    "invasion": "Invasion",
    "mkos": "My Kind Of Scum",
    "tdigwatt": "This Deal Is Getting Worse All The Time",
    "fo deal": "This Deal Is Getting Worse All The Time",
    "sycfa": "Set Your Course For Alderaan",
    "senate": "Plead My Case To The Senate",
    "fo senate": "Senate Occupied",
    "ds senate": "Senate Occupied",
    "ls senate": "Plead My Case To The Senate",
    "watto": "No Money, No Parts, No Deal!",
    "combat": "Combat Readiness",
    "ds combat": "Combat Readiness",
    "ls combat": "Combat Preparedness",
    "dark combat": "Combat Readiness",
    "coruscant crv": "Combat Readiness (V)",
    "corsucant crv": "Combat Readiness (V)",
    "hoth crv": "Combat Readiness (V)",
    "tatooine crv": "Combat Readiness (V)",
    "bespin crv": "Combat Readiness (V)",
    "jakku cpv": "Combat Preparedness (V)",
    "tatooine cpv": "Combat Preparedness (V)",
    "hoth cpv": "Combat Preparedness (V)",
    "hoth cpv mains": "Combat Preparedness (V)",
    "yavin 4 cpv": "Combat Preparedness (V)",
    "wys": "Watch Your Step",
    "oa": "Old Allies",
    "old allies": "Old Allies",
    "diplo": "Diplomatic Mission To Alderaan",
    "dmta": "Diplomatic Mission To Alderaan",
    "trm": "Yavin 4: Massassi Throne Room",
    "qmc": "Quiet Mining Colony",
    "hb": "Hidden Base",
    "hidden base": "Hidden Base",
    "hb sandwhirl": "Hidden Base",
    "hb quads": "Hidden Base",
    "hb mains": "Hidden Base",
    "hb b-wings": "Hidden Base",
    "hb b-wings": "Hidden Base",
    "hb acclamators": "Hidden Base",
    "profit": "You Can Either Profit By This",
    "hitco": "He Is The Chosen One",
    "tigih": "This Is Getting Out Of Hand",
    "whap": "We Have A Plan",
    "rst": "Rebel Strike Team",
    "ebo": "Echo Base Operations",
    "y4ops": "Yavin 4 Operations",
    "mwyhl": "Mind What You Have Learned",
    "no idea": "They Have No Idea We're Coming",
    "rtp": "Rescue The Princess",
    "thgg": "The Hyperdrive Generator's Gone (V)",
    "hyperdrive": "The Hyperdrive Generator's Gone (V)",
    "mbo": "Massassi Base Operations",
    "gungans": "Watch Your Step",
    "twin suns": "Twin Suns Of Tatooine",
    "tsot": "Twin Suns Of Tatooine",
    "jcc mains": "Coruscant: Jedi Council Chamber",
    "naboo gungans": "Watch Your Step",
    "rops": "Ralltiir Operations",
    "ropsv": "Ralltiir Operations (V)",
    "rops(v)": "Ralltiir Operations (V)",
    "diplomatic mission": "Diplomatic Mission To Alderaan",
    "there is good in him": "There Is Good In Him",
    "combat readiness v": "Combat Readiness (V)",
    "combat preparedness v": "Combat Preparedness (V)",
    "hb corvette quads": "Hidden Base",
    "hb corvette": "Hidden Base",
    "crv endor first order": "Combat Readiness (V)",
    "endor first order": "Combat Readiness (V)",
    "cpv jakku mains": "Combat Preparedness (V)",
    "hidden base mains": "Hidden Base",
    "naboo mains": "Watch Your Step",
    "hdadtj": "Hunt Down And Destroy The Jedi",
    "naboo crv": "Combat Readiness (V)",
    "nabroo crv": "Combat Readiness (V)",
    "tat crv": "Combat Readiness (V)",
    "tatooine crv": "Combat Readiness (V)",
    "tatooine crv spies": "Combat Readiness (V)",
    "hoth crv": "Combat Readiness (V)",
    "hoth cr(v)": "Combat Readiness (V)",
    "hoth cr (v)": "Combat Readiness (V)",
    "bespin crv": "Combat Readiness (V)",
    "coruscant crv": "Combat Readiness (V)",
    "coruscant cr(v)": "Combat Readiness (V)",
    "naboo cpv": "Combat Preparedness (V)",
    "naboo cp(v)": "Combat Preparedness (V)",
    "yavin cpv": "Combat Preparedness (V)",
    "jakku cp(v)": "Combat Preparedness (V)",
    "jakku cpv": "Combat Preparedness (V)",
    "tatooine cp(v)": "Combat Preparedness (V)",
    "tatooine cpv": "Combat Preparedness (V)",
    "lsc": "Combat Preparedness",
    "ls combat": "Combat Preparedness",
    "lightsaber combat": "Combat Preparedness",
    "combat racing": "Combat Preparedness",
    "combat space": "Combat Preparedness",
    "dark combat": "Combat Readiness",
    "ds2 throne room atmd": "Set Your Course For Alderaan",
    "ds2 throne room": "Set Your Course For Alderaan",
    "dsii trm": "Set Your Course For Alderaan",
    "h1wr gungans": "Watch Your Step",
    "h1wr": "Watch Your Step",
    "bnc gungans": "Watch Your Step",
    "jcc mains": "Coruscant: Jedi Council Chamber",
    "wys lsjk": "Watch Your Step",
    "wys raiders": "Watch Your Step",
    "wys spies": "Watch Your Step",
    "wys quads": "Watch Your Step",
    "wys freighters": "Watch Your Step",
    "hb acclamators": "Hidden Base",
    "hb quads": "Hidden Base",
    "hb mains": "Hidden Base",
    "hb b-wings": "Hidden Base",
    "hb corvettes": "Hidden Base",
    "hb freighters": "Hidden Base",
    "hb x-wings": "Hidden Base",
    "hb snubs": "Hidden Base",
    "hidden base snubs": "Hidden Base",
    "hidden base x-wings": "Hidden Base",
    "hidden base corvettes": "Hidden Base",
    "hidden base freighters": "Hidden Base",
    "hidden base b-wings": "Hidden Base",
    "tdigw": "This Deal Is Getting Worse All The Time",
    "tdigwatt tanks": "This Deal Is Getting Worse All The Time",
    "tdigwatt tanks": "This Deal Is Getting Worse All The Time",
    "ls senate": "Plead My Case To The Senate",
    "ds senate": "Senate Occupied",
    "cpi": "Set Your Course For Alderaan",
    "death star": "Set Your Course For Alderaan",
    "combat atmd": "Combat Readiness",
    "whap space": "We Have A Plan",
    "trm gungan podracing": "Yavin 4: Massassi Throne Room",
    "trm gungans": "Yavin 4: Massassi Throne Room",
    "naboo crv bombers": "Combat Readiness (V)",
    "sycfa ties": "Set Your Course For Alderaan",
    "sycfa brangus": "Set Your Course For Alderaan",
    "cct ig-88": "Carbon Chamber Testing",
    "cct ig 88": "Carbon Chamber Testing",
    "hoth tractor beams": "Combat Readiness",
    "tatooine tractor beams": "Combat Readiness (V)",
    "endor first order": "Combat Readiness (V)",
    "lightsaber combat podracing": "Combat Preparedness",
    "space weapons lock": "Endor Operations",
    "ebo ketwol": "Echo Base Operations",
    "trm speeders": "Yavin 4: Massassi Throne Room",
    "hoth cpv": "Combat Preparedness (V)",
    "hoth cpv mains": "Combat Preparedness (V)",
    "yavin 4 cpv": "Combat Preparedness (V)",
    "yavin cpv": "Combat Preparedness (V)",
    "rst mains": "Rebel Strike Team",
    "ds2 throne room mains": "Set Your Course For Alderaan",
    "tto ties": "Endor Operations",
    "endor ops": "Endor Operations",
    "trv": "Set Your Course For Alderaan",
    "ds sycfa": "Set Your Course For Alderaan",
    "ds sycfa ties": "Set Your Course For Alderaan",
    "wht space": "Combat Preparedness",
    "combat amn": "Combat Readiness",
    "naboo cpv gungans": "Combat Preparedness (V)",
}

DS_FORCE = {
    "Senate Occupied",
    "No Money, No Parts, No Deal!",
    "Combat Readiness",
    "Combat Readiness (V)",
    "Endor Operations",
    "Imperial Entanglements",
    "I Want That Map",
    "Agents Of Black Sun",
    "Court Of The Vile Gangster",
    "Hunt Down And Destroy The Jedi",
    "ISB Operations",
    "Bring Him Before Me",
    "Carbon Chamber Testing",
    "Invasion",
    "My Kind Of Scum",
    "This Deal Is Getting Worse All The Time",
    "Set Your Course For Alderaan",
    "Ralltiir Operations",
    "Ralltiir Operations (V)",
}
LS_FORCE = {
    "Plead My Case To The Senate",
    "Watch Your Step",
    "Old Allies",
    "Diplomatic Mission To Alderaan",
    "Yavin 4: Massassi Throne Room",
    "Quiet Mining Colony",
    "Hidden Base",
    "You Can Either Profit By This",
    "He Is The Chosen One",
    "This Is Getting Out Of Hand",
    "We Have A Plan",
    "Rebel Strike Team",
    "Echo Base Operations",
    "Yavin 4 Operations",
    "Mind What You Have Learned",
    "They Have No Idea We're Coming",
    "Rescue The Princess",
    "The Hyperdrive Generator's Gone (V)",
    "Massassi Base Operations",
    "Combat Preparedness",
    "Combat Preparedness (V)",
    "There Is Good In Him",
    "Coruscant: Jedi Council Chamber",
    "Twin Suns Of Tatooine",
}

EVENTS = [
    {
        "key": "16tmw",
        "wrap": "16tmw.html",
        "title": "2016 Texas Mini Worlds",
        "year": "2016",
        "tag": "2016-10-28",
        "dates": "28–30 October 2016",
        "site": "Houston, Texas",
        "format": "[[Open]]",
        "winner": "Steve Baroni",
        "lead": "'''2016 Texas Mini Worlds''' was a Players Committee match-play major in Houston, Texas, 28–30 October 2016. [[Steve Baroni]] is the published winner.",
        "pc": "https://www.starwarsccg.org/2016-texas-mini-worlds/",
        "deck_prefix": "2016 Texas Mini Worlds",
        "list_label": "Texas Mini Worlds",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "16euro",
        "wrap": "16euro.html",
        "title": "2016 European Championship",
        "year": "2016",
        "tag": "2016-09-23",
        "dates": "23–25 September 2016",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Emil Wallin",
        "lead": "'''2016 European Championship''' was the Players Committee European Championship at Zu Den Vier Winden in Bochum, Germany, 23–25 September 2016. [[Emil Wallin]] finished 1st in Day 3. Wrap labels Day 3 as Day 2 and Day 2 as Day 1; individual list titles use Day 3 for the Top 8.",
        "pc": "https://www.starwarsccg.org/2016-european-championships/",
        "deck_prefix": "2016 European Championship",
        "list_label": "European Championship",
        "stages": [("d3", "Day 3"), ("d2", "Day 2")],
        "wrap_remap": {"d2": "d3", "d1": "d2"},
    },
    {
        "key": "16worlds",
        "wrap": "16worlds.html",
        "title": "2016 World Championship",
        "year": "2016",
        "tag": "2016-08-11",
        "dates": "11–15 August 2016",
        "site": "Princeton, New Jersey",
        "format": "[[Open]]",
        "winner": "Tom Haid",
        "lead": "'''2016 World Championship''' was the Players Committee World Championship in Princeton, New Jersey, 11–15 August 2016. [[Tom Haid]] finished 1st in Day 3. Wrap labels Day 3 as Day 2 and Day 2 as Day 1; individual list titles use Day 3 for the Top 8.",
        "pc": "https://www.starwarsccg.org/2016-world-championships/",
        "deck_prefix": "2016 Worlds",
        "list_label": "World Championship",
        "stages": [("d3", "Day 3"), ("d2", "Day 2")],
        "wrap_remap": {"d2": "d3", "d1": "d2"},
    },
    {
        "key": "16egp",
        "wrap": "16egp.html",
        "title": "2016 Endor Grand Prix",
        "year": "2016",
        "tag": "2016-05-20",
        "dates": "20–22 May 2016",
        "site": "Seattle, Washington",
        "format": "[[Open]]",
        "winner": "Brian Fred",
        "lead": "'''2016 Endor Grand Prix''' was a Players Committee major event in Seattle, Washington, 20–22 May 2016. [[Brian Fred]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2016-endor-grand-prix/",
        "deck_prefix": "2016 EGP",
        "list_label": "Endor Grand Prix",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "16mpc",
        "wrap": "16mpc.html",
        "title": "2016 Match Play Championship",
        "year": "2016",
        "tag": "2016-01-08",
        "dates": "8–10 January 2016",
        "site": "United States",
        "format": "[[Open]]",
        "winner": "Tom Kelly",
        "lead": "'''2016 Match Play Championship''' was the Players Committee match-play championship, 8–10 January 2016. [[Tom Kelly]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2016-match-play-championship/",
        "deck_prefix": "2016 MPC",
        "list_label": "Match Play Championship",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "15tmw",
        "wrap": "15tmw.html",
        "title": "2015 Texas Mini Worlds",
        "year": "2015",
        "tag": "2015-10-23",
        "dates": "23–25 October 2015",
        "site": "Texas",
        "format": "[[Open]]",
        "winner": "Brian Fred",
        "lead": "'''2015 Texas Mini Worlds''' was a Players Committee match-play major, 23–25 October 2015. [[Brian Fred]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2015-texas-mini-worlds/",
        "deck_prefix": "2015 Texas Mini Worlds",
        "list_label": "Texas Mini Worlds",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "15euro",
        "wrap": "15euro.html",
        "title": "2015 European Championship",
        "year": "2015",
        "tag": "2015-10-16",
        "dates": "16–18 October 2015",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Ziemowit Skwara",
        "lead": "'''2015 European Championship''' was the Players Committee European Championship at Zu Den Vier Winden in Bochum, Germany, 16–18 October 2015. [[Ziemowit Skwara]] finished 1st in Day 3. Wrap labels Day 3 as Day 2 and Day 2 as Day 1; stages follow the tournament-decklists accordion.",
        "pc": "https://www.starwarsccg.org/2015-european-championships/",
        "deck_prefix": "2015 European Championship",
        "list_label": "European Championship",
        "stages": [("d3", "Day 3"), ("d2", "Day 2")],
        "wrap_remap": {"d2": "d3", "d1": "d2"},
    },
    {
        "key": "15worlds",
        "wrap": "15worlds.html",
        "title": "2015 World Championship",
        "year": "2015",
        "tag": "2015-08-06",
        "dates": "6–9 August 2015",
        "site": "Philadelphia, Pennsylvania",
        "format": "[[Open]]",
        "winner": "Justin Desai",
        "lead": "'''2015 World Championship''' was the Players Committee World Championship in Philadelphia, Pennsylvania, 6–9 August 2015. [[Justin Desai]] finished 1st in Day 3. Wrap labels Day 3 as Day 2 and Day 2 as Day 1; stages follow the tournament-decklists accordion.",
        "pc": "https://www.starwarsccg.org/2015-world-championships/",
        "deck_prefix": "2015 Worlds",
        "list_label": "World Championship",
        "stages": [("d3", "Day 3"), ("d2", "Day 2")],
        "wrap_remap": {"d2": "d3", "d1": "d2"},
    },
    {
        "key": "15mpc",
        "wrap": "15mpc.html",
        "title": "2015 Match Play Championship",
        "year": "2015",
        "tag": "2015-05-01",
        "dates": "1–3 May 2015",
        "site": "United States",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2015 Match Play Championship''' was the Players Committee match-play championship, 1–3 May 2015. [[Joe Olson]] finished 1st. Day 2 is the published Final Four (names only); Day 1 is the constructed field.",
        "pc": "https://www.starwarsccg.org/2015-match-play-championship/",
        "deck_prefix": "2015 MPC",
        "list_label": "Match Play Championship",
        "stages": [("d2", "Day 2"), ("d1", "Day 1")],
    },
    {
        "key": "15sdgp",
        "wrap": "15sdgp.html",
        "title": "2015 San Diego Grand Prix",
        "year": "2015",
        "tag": "2015-01-09",
        "dates": "9–11 January 2015",
        "site": "San Diego, California",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2015 San Diego Grand Prix''' was a Players Committee major event in San Diego, California, 9–11 January 2015. [[Joe Olson]] finished 1st. The numbered tournament-decklists accordion is placement order ([[Kevin Shannon]] 2nd, [[Brian Fred]] 3rd); the wrap numbered Fred 2nd.",
        "pc": "https://www.starwarsccg.org/2015-san-diego-grand-prix/",
        "deck_prefix": "2015 San Diego Grand Prix",
        "list_label": "San Diego Grand Prix",
        "stages": [("t4", "Top 4"), ("list", "Results")],
    },
]


def flip_last_first(name: str) -> str:
    """Haid, Tom → Tom Haid. Keep already-flipped First Last."""
    if "," not in name:
        return name
    if name in CANON:
        return CANON[name]
    last, first = name.split(",", 1)
    last, first = last.strip(), first.strip()
    if not last or not first:
        return name
    # "Rowlands, tWelsh, Pete"
    if "," in first:
        bits = [p.strip() for p in first.split(",")]
        first = bits[-1]
    return f"{first} {last}".strip()


def canon(name: str) -> str:
    name = re.sub(r"\s+", " ", name or "").strip().strip(",")
    name = name.replace("’", "'").replace("\u2019", "'").replace("\u2018", "'")
    if name.isupper() and " " in name:
        name = name.title()
    if name in CANON:
        return CANON[name]
    flipped = flip_last_first(name)
    if flipped in CANON:
        return CANON[flipped]
    if name in TOKEN:
        return TOKEN[name]
    if flipped in TOKEN:
        return TOKEN[flipped]
    return flipped


def map_slang(raw: str, side: str | None = None) -> str | None:
    if not raw:
        return None
    s = htmlmod.unescape(raw)
    s = re.sub(r"<[^>]+>", " ", s)
    s = re.sub(r"\s+", " ", s).strip(" .")
    s = s.replace("’", "'").replace("\u2019", "'")
    k0 = s.lower().strip()
    if k0 in ("day 1", "day 2", "day 3", "drops", "results"):
        return None
    k1 = re.sub(r"\s+", " ", k0.replace("(", "").replace(")", "")).strip()
    k2 = re.sub(
        r"\s+(mains|quads|sandwhirl|b-wings|bwings|tanks|racing|ig-88|ig 88|ansb|lsjk|corvette|spies|space|snubs|freighters|acclamators|x-wings|bombers|ketwol|speeders|podracing|gungan podracing|gungans)$",
        "",
        k1,
    ).strip()
    dest = None
    for key in (k0, k1, k2):
        if key in SLANG:
            dest = SLANG[key]
            break
        if key in hm.SLANG_HUB:
            dest = hm.SLANG_HUB[key]
            if dest == "There Is No Try":
                dest = "Endor Operations"
            if dest == "Watto's Box":
                dest = "No Money, No Parts, No Deal!"
            break
    if not dest:
        return None
    if side == "DS" and dest == "Plead My Case To The Senate":
        dest = "Senate Occupied"
    if side == "LS" and dest == "Senate Occupied":
        dest = "Plead My Case To The Senate"
    if side == "DS" and dest == "Combat Preparedness":
        dest = "Combat Readiness"
    if side == "LS" and dest == "Combat Readiness":
        dest = "Combat Preparedness"
    return dest


def wrap_visible(raw: str) -> str:
    m = re.search(r"<h1[^>]*>[\s\S]*?</h1>([\s\S]+?)Posted in", raw, re.I)
    if not m:
        m = re.search(r"<h1[^>]*>[\s\S]*?</h1>([\s\S]{0,40000})", raw, re.I)
    s = m.group(1) if m else raw
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</(p|tr|li|h[1-6]|div)>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmlmod.unescape(s)
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = re.sub(r"[ \t]+", " ", s)
    cut = re.search(r"(?i)(?:posted in|posts navigation|scroll to top)", s)
    if cut:
        s = s[: cut.start()]
    return "\n".join(ln.strip() for ln in s.splitlines() if ln.strip())


def heading_stage(line: str) -> str | None:
    tl = line.strip().lower()
    tl = re.sub(r"^results\s+", "", tl).strip(" :-")
    tl = re.sub(r"^\d{4}\s+(worlds|euros?|mpc|egp|tmw|sdgp)\s+", "", tl)
    tl = re.sub(r"^(?:2015|2016)\s+", "", tl)
    if re.search(r"\bday\s*3\b", tl) and not re.search(r"\bday\s*[12]\b", tl):
        return "d3"
    if re.search(r"\bday\s*2\b", tl) and not re.search(r"\bday\s*[13]\b", tl):
        return "d2"
    if re.search(r"\bday\s*1\b", tl) and not re.search(r"\bday\s*[23]\b", tl):
        return "d1"
    if re.match(r"^top\s*4\b", tl):
        return "t4"
    if re.match(r"^drops?$", tl):
        return "drop"
    if re.match(r"^results$", tl):
        return None
    return None


CHROME = {
    "skip to content",
    "volunteer",
    "forum",
    "card search",
    "play",
    "print cards",
    "menu",
    "home",
    "about us",
    "news",
    "store",
    "media",
    "podcasts",
    "videos",
    "tournaments",
    "cube",
    "rules",
    "collecting",
    "donations",
    "posts navigation",
    "scroll to top",
    "the games",
    "the players committee",
    "org chart",
    "player locator",
    "new & returning players",
    "awards and hall of fame",
    "star wars ccg",
    "swccg formats",
    "swccg rules",
    "swccg faq",
    "online play",
    "tournament decklists",
    "tournament resources",
    "tournament software",
    "jawa format",
    "major event winners",
    "cube format",
    "legacy format",
    "limited resources",
    "scavenger format",
    "utinni! format",
    "jedi knights tcg",
    "young jedi ccg",
    "new & returning players",
    "player locator",
    "original (decipher) release sets",
    "virtual (new) release sets",
    "print cards",
    "card search",
    "100 card deck format",
    "skip to content",
    "awards and hall of fame",
    "org chart",
    "the games",
    "the players committee",
}

ROW = re.compile(
    r"^(?:\(?(\d{1,2})(?:st|nd|rd|th)?\)?[.\)\]]?\s*[–—-]?\s*)?([A-Za-z][A-Za-z .,'\-éøæåüßẞÖöÄäÜÉØÆÅ/_().]+?)\s+[–—-]\s+(.+)$"
)
NAME_ONLY_NUM = re.compile(
    r"^(?:\(?(\d{1,2})(?:st|nd|rd|th)?\)?[.\)\]]\s*|\b(?:1st|2nd|3rd|4th|5th|6th|7th|8th)\s+)([A-Za-z][A-Za-z .,'\-éøæåüßẞÖöÄäÜÉØÆÅ/_().]+?)\s*$"
)
NAME_ONLY = re.compile(
    r"^([A-Za-z][A-Za-z'\-éøæåüßẞÖöÄäÜÉØÆÅ]+,\s+[A-Za-z][A-Za-z .'\-éøæåüßẞÖöÄäÜÉØÆÅ]+)$"
)
SKIP_NAMES = {
    "sandwhirl",
    "results",
    "decklist pdfs",
    "day 1",
    "day 2",
    "day 3",
}


def explode_rows(text: str) -> str:
    text = re.sub(r"\s+((?:Day|DAY)\s*[123])\b", r"\n\1", text)
    text = re.sub(r"\s+(Drops?)\b", r"\n\1", text)
    text = re.sub(r"\s+(\(?\d{1,2}\)(?:st|nd|rd|th)?[.\)]\s*)", r"\n\1", text)
    text = re.sub(r"\s+(\d{1,2}\.\s+[A-Za-z])", r"\n\1", text)
    text = re.sub(r"\s+(\d{1,2}(?:st|nd|rd|th)\s+)", r"\n\1", text)
    text = re.sub(
        r"(?<![Dd][Aa][Yy])\s+(\d{1,2}\s+[–—-]\s+[A-Za-z])",
        r"\n\1",
        text,
    )
    text = re.sub(
        r"\s+((?:(?:de|den|van|von)\s+)?(?:d['’])?[A-Za-z][A-Za-z'\-]+,\s+[A-Za-z])",
        r"\n\1",
        text,
        flags=re.I,
    )
    return text


def parse_text(text: str, default_stage: str = "list"):
    text = re.sub(r"\([0-9]+-[0-9]+\)", "", text)
    text = re.sub(r"\s+\d-\d\b", "", text)
    text = explode_rows(text)
    stage = None
    out = defaultdict(list)
    dest = defaultdict(dict)
    place_n = defaultdict(int)

    def keep(p: str) -> bool:
        if not p or " " not in p:
            return False
        if is_junk_player(p) or p.lower() in CHROME or p.lower() in SKIP_NAMES:
            return False
        return True

    def assign(stage_k, p, ds, ls, fin):
        if p not in out[stage_k]:
            out[stage_k].append(p)
        dest[stage_k][p] = (ds, ls, fin)

    for ln in text.splitlines():
        hs = heading_stage(ln)
        if hs:
            stage = hs
            continue
        if not stage:
            if " – " in ln or " — " in ln or " - " in ln:
                stage = default_stage
            else:
                continue
        m = ROW.match(ln)
        if not m:
            m3 = NAME_ONLY_NUM.match(ln)
            if m3:
                p = canon(m3.group(2))
                if keep(p):
                    place_n[stage] += 1
                    fin = int(re.sub(r"\D", "", m3.group(1) or "") or place_n[stage])
                    assign(stage, p, None, None, fin)
                continue
            m4 = NAME_ONLY.match(ln)
            if m4:
                p = canon(m4.group(1))
                if keep(p):
                    place_n[stage] += 1
                    assign(stage, p, None, None, place_n[stage])
                continue
            m2 = re.match(r"^([A-Z][a-z]+(?:\s+[A-Z][a-z'.\-]+)+)$", ln)
            if m2:
                p = canon(m2.group(1))
                if keep(p):
                    place_n[stage] += 1
                    assign(stage, p, None, None, place_n[stage])
            continue
        place, name, rest = m.groups()
        p = canon(name)
        if not keep(p):
            continue
        parts = re.split(r"\s+[–—-]\s+", rest)
        ds_raw = parts[0].strip() if parts else ""
        ls_raw = parts[1].strip() if len(parts) > 1 else ""
        if len(parts) >= 3:
            ls_raw = parts[-1].strip()
        ds = map_slang(ds_raw, "DS")
        ls = map_slang(ls_raw, "LS")
        if ds in LS_FORCE and ds not in DS_FORCE:
            if ls in DS_FORCE and ls not in LS_FORCE:
                ds, ls = ls, ds
            elif not ls:
                ls, ds = ds, None
        if ls in DS_FORCE and ls not in LS_FORCE and not ds:
            ds, ls = ls, None
        if ds and ds in LS_FORCE and ds not in DS_FORCE and ls == ds:
            ds = None
        if ls and ls in DS_FORCE and ls not in LS_FORCE and ds == ls:
            ls = None
        place_n[stage] += 1
        fin = int(place) if place else place_n[stage]
        assign(stage, p, ds, ls, fin)
    return out, dest


def normalize_sdgp(text: str) -> str:
    """Accordion lists Light then Dark with match records; emit DS – LS placement lines."""
    lines = ["Results"]
    t4 = []
    rec = re.compile(
        r"^(\d+)\s*[-–—]\s*(.+?)\s*[-–—]\s*(.+?)\s+(\d-\d)\s*[-–—]?\s*(.+?)\s+(\d-\d)\s*(.*)$"
    )
    for raw in text.splitlines():
        ln = re.sub(r"\s+", " ", raw).strip()
        m = rec.match(ln)
        if not m:
            continue
        n, name, ls, _r1, ds, _r2, rest = m.groups()
        name = name.strip()
        ls = ls.strip(" .")
        ds = ds.strip(" .")
        lines.append(f"{n}. {name} – {ds} – {ls}")
        tm = re.search(r"Top 4:\s*(.+?)\s*[-–—]\s*(.+?)\)", rest)
        if tm:
            t4.append(f"1. {name} – {tm.group(2).strip()} – {tm.group(1).strip()}")
    if t4:
        lines.append("Top 4")
        lines.extend(t4)
    return "\n".join(lines)


def accordion_inline():
    """Prefer the 2015 tournament-decklists accordion over wrap order when they disagree."""
    out = {}
    src = WRAP / "resources-td.html"
    if not src.exists():
        return out
    raw = src.read_text(encoding="utf-8", errors="replace")
    m = re.search(r'\[wc_toggle title="2015"\]([\s\S]*?)\[/wc_toggle\]', raw)
    if not m:
        return out
    body = m.group(1)
    mapping = {
        "15euro": "European Championships",
        "15worlds": "World Championship",
        "15sdgp": "SoCal Grand Prix",
    }
    for key, title in mapping.items():
        sm = re.search(
            rf'\[wc_accordion_section title="{re.escape(title)}"\]([\s\S]*?)\[/wc_accordion_section\]',
            body,
        )
        if not sm:
            continue
        text = wrap_visible("<h1>x</h1>" + sm.group(1) + "Posted in")
        text = text.replace(" - ", " – ")
        if key == "15sdgp":
            text = normalize_sdgp(text)
        out[key] = text
        (WRAP / f"accordion-{key}.txt").write_text(text, encoding="utf-8", newline="\n")
    return out


def emit_deck_page(title: str, player: str, side: str, obj: str, stage_lab: str, meta: dict):
    env = meta["format"]
    src = meta["pc"]
    side_word = "Dark" if side == "DS" else "Light"
    obj_link = f"[[{obj}]]" if obj else "—"
    body = f"""'''{title}''' was the {side_word} Side constructed list played by [[{player}]] at [[{meta['title']}]] ({stage_lab}).

== Deck info ==

* '''Starting Card:''' {obj_link}
* '''Format:''' {env}
* '''Stage:''' {stage_lab}
* '''Source:''' [{src} PC list]

== See also ==

* [[{meta['title']}]]
* [[{player}]]
* [[List of SWCCG tournaments]]

== Sources ==

* [{src} {meta['title']}], starwarsccg.org

{refs()}

[[Category:Decklists]]
[[Category:{meta['year']}]]
"""
    (PAGES / wiki_fname(title)).write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def people_table(heading, players, dt, hl, stage, dest_fin):
    bits = ['{| class="wikitable sortable"', f"! {heading} !! Player !! Dark !! Light"]
    for p in players:
        rec = dest_fin.get(p) or (None, None, None)
        if len(rec) < 3:
            rec = (
                rec[0] if rec else None,
                rec[1] if rec and len(rec) > 1 else None,
                None,
            )
        fin = rec[2]
        fin_s = str(fin) if fin else "—"
        ds_page = dt.get((p, stage, "DS"))
        ls_page = dt.get((p, stage, "LS"))
        ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
        ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
        bits += ["|-", f"| {fin_s} || [[{p}]] || {ds} || {ls}"]
    bits.append("|}")
    return "\n".join(bits)


def write_hub(meta, by_stage, dest, dt, hl):
    secs = []
    for stage, heading in meta.get("stages") or []:
        players = by_stage.get(stage) or []
        if not players:
            continue
        note = ""
        if heading == "Day 1":
            note = "Published constructed lists (every published pair, not Top 8 only).\n\n"
        elif heading == "Results":
            note = "Numbered tournament-decklists accordion (placement order).\n\n"
        elif heading == "Top 4":
            note = "Only [[Brian Fred]]'s Top 4 pair is published, distinct from his 3rd-place lists.\n\n"
        tbl = people_table(heading, players, dt, hl, stage, dest.get(stage) or {})
        secs.append(f"== {heading} ==\n\n{note}{tbl}\n")
    body_sec = "\n".join(secs)
    if not body_sec:
        body_sec = ""
    body = f"""{meta["lead"]}<ref name="pc">{meta["pc"]}</ref>

== Format ==

* '''Environment:''' {meta["format"]}
* '''Site:''' {meta["site"]}
* '''Dates:''' {meta["dates"]}
* '''Winner:''' [[{meta["winner"]}]]

{body_sec}
== See also ==

* [[List of SWCCG tournaments]]
* [[Tournaments]] · [[Championships]] · [[Formats]]
* [{meta["pc"]} PC results]

== Sources ==

* [{meta["pc"]} {meta["title"]}], starwarsccg.org

{refs()}

[[Category:Tournaments]]
[[Category:Championships]]
[[Category:{meta["year"]}]]
"""
    (PAGES / wiki_fname(meta["title"])).write_text(body.replace("\r\n", "\n"), encoding="utf-8", newline="\n")


def patch_list(year_rows):
    text = LIST.read_text(encoding="utf-8")
    text = re.sub(r"\n== 2016 ==.*?(?=\n== )", "\n", text, count=1, flags=re.S)
    text = re.sub(r"\n== 2015 ==.*?(?=\n== )", "\n", text, count=1, flags=re.S)
    blocks = []
    for year in ("2016", "2015"):
        rows = year_rows.get(year) or []
        if not rows:
            continue
        blocks.append(
            f"""== {year} ==

{{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
{chr(10).join(rows)}
|}}

"""
        )
        if f"[[Category:{year}]]" not in text:
            text = text.replace("[[Category:2017]]", f"[[Category:2017]]\n[[Category:{year}]]")
    text = text.replace(
        "== Decipher World Championships ==",
        "".join(blocks) + "== Decipher World Championships ==",
        1,
    )
    LIST.write_text(text, encoding="utf-8", newline="\n")
    if EC.exists():
        et = EC.read_text(encoding="utf-8")
        et = et.replace(
            "| 2016 || 2016 European Championship || — || — || [[Emil Wallin]]",
            "| 2016 || [[2016 European Championship]] || Bochum, Germany || [[Open]] || [[Emil Wallin]]",
        )
        et = et.replace(
            "| 2015 || 2015 European Championship || — || — || —",
            "| 2015 || [[2015 European Championship]] || Bochum, Germany || [[Open]] || [[Ziemowit Skwara]]",
        )
        if "2015-european-championships" not in et:
            et = et.replace(
                "* [https://www.starwarsccg.org/2016-european-championships/ 2016 European Championships]",
                "* [https://www.starwarsccg.org/2016-european-championships/ 2016 European Championships]\n* [https://www.starwarsccg.org/2015-european-championships/ 2015 European Championships]",
            )
        EC.write_text(et, encoding="utf-8", newline="\n")


def inject_result_rows(text: str, rows: list[str], event_title: str) -> str:
    """Insert Tournament Results rows; create a table when the bio only has bullets."""
    text = re.sub(rf"\|-\s*\n\| [^\n]*\[\[{re.escape(event_title)}\]\][^\n]*\n", "", text)
    text = re.sub(r"== Tournament results ==", "== Tournament Results ==", text, count=1)
    m = re.search(
        r"(== Tournament Results ==\s*\{\| class=\"wikitable\"[\s\S]*?)(\n\|\})",
        text,
    )
    if m:
        return text[: m.start(2)] + "\n" + "\n".join(rows) + text[m.start(2) :]
    table = (
        "\n{| class=\"wikitable\"\n|-\n"
        "! Date !! Event !! Format !! Finish !! Dark !! Light\n"
        + "\n".join(rows)
        + "\n|}\n"
    )
    if "== Tournament Results ==" in text:
        return text.replace("== Tournament Results ==", "== Tournament Results ==" + table, 1)
    if "== See also ==" in text:
        return text.replace(
            "== See also ==",
            "== Tournament Results ==" + table + "\n== See also ==",
            1,
        )
    return text + "\n== Tournament Results ==" + table


def upsert_player(player, rows, meta):
    if is_junk_player(player):
        return None
    dest_stub = STUBS / (player.replace(" ", "_") + ".wiki")
    bio = PAGES / (player.replace(" ", "_") + ".wiki")
    cat = f"[[Category:{meta['year']}]]"
    if bio.exists() and is_bio(bio.read_text(encoding="utf-8", errors="replace")):
        text = inject_result_rows(bio.read_text(encoding="utf-8"), rows, meta["title"])
        if cat not in text:
            text = text.replace("[[Category:Players]]", f"[[Category:Players]]\n{cat}")
        bio.write_text(text, encoding="utf-8", newline="\n")
        tidy_player_page(bio)
        return (player, f"pages/{bio.name}")
    upsert_stub(player, rows, meta["title"], meta["pc"])
    if dest_stub.exists():
        st = dest_stub.read_text(encoding="utf-8")
        if "[[2026 " not in st and "[[Category:2026]]" in st:
            st = st.replace("[[Category:2026]]\n", "").replace("[[Category:2026]]", "")
        if cat not in st:
            st = st.replace("[[Category:Players]]", f"[[Category:Players]]\n{cat}")
        dest_stub.write_text(st, encoding="utf-8", newline="\n")
        tidy_player_page(dest_stub)
        return (player, f"pages/player-stubs/{dest_stub.name}")
    return None


def main():
    STUBS.mkdir(parents=True, exist_ok=True)
    acc = accordion_inline()
    titles = []
    list_rows = defaultdict(list)
    STAGE_LAB = {"d3": "Day 3", "d2": "Day 2", "d1": "Day 1", "list": "Results", "t4": "Top 4", "drop": "Drops"}

    for meta in EVENTS:
        by_stage = defaultdict(list)
        dest = defaultdict(dict)
        if meta.get("stub_only"):
            write_hub(meta, {}, {}, {}, {})
            titles.append((meta["title"], f"pages/{wiki_fname(meta['title'])}"))
            list_rows[meta["year"]].append(
                f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || [[{meta['winner']}]]"
            )
            print("stub", meta["title"])
            continue
        text = ""
        if meta.get("wrap"):
            path = WRAP / meta["wrap"]
            if path.exists():
                text = wrap_visible(path.read_text(encoding="utf-8", errors="replace"))
        if meta["key"] in acc:
            text = acc[meta["key"]]
        default = "list" if meta["key"] in ("15sdgp",) else "d2"
        parsed_stage, parsed_dest = parse_text(text, default)
        remap = meta.get("wrap_remap") or {}
        if remap and meta["key"] not in acc:
            remapped_s, remapped_d = defaultdict(list), defaultdict(dict)
            for st, names in parsed_stage.items():
                st2 = remap.get(st, st)
                remapped_s[st2] = names
                remapped_d[st2] = parsed_dest[st]
            parsed_stage, parsed_dest = remapped_s, remapped_d
        for st, names in parsed_stage.items():
            by_stage[st] = names
            dest[st] = parsed_dest[st]
        dt, hl = {}, {}
        for stage, heading in meta.get("stages") or []:
            for i, p in enumerate(by_stage.get(stage) or [], 1):
                rec = dest.get(stage, {}).get(p)
                if rec and len(rec) == 3:
                    ds, ls, fin = rec
                elif rec and len(rec) == 2:
                    ds, ls = rec
                    fin = i
                    dest[stage][p] = (ds, ls, fin)
                else:
                    ds = ls = None
                    fin = i
                    dest[stage][p] = (None, None, fin)
                lab = STAGE_LAB.get(stage, heading)
                if ds:
                    title = f"{meta['deck_prefix']} {'' if lab == 'Day 1' else lab + ' '}{p} DS {ds}".replace("  ", " ").strip()
                    title = re.sub(r"[#<>\[\]\|\{\}?*\"]", "", title)
                    emit_deck_page(title, p, "DS", ds, lab, meta)
                    dt[(p, stage, "DS")] = title
                    hl[title] = ds
                    titles.append((title, f"pages/{wiki_fname(title)}"))
                if ls:
                    title = f"{meta['deck_prefix']} {'' if lab == 'Day 1' else lab + ' '}{p} LS {ls}".replace("  ", " ").strip()
                    title = re.sub(r"[#<>\[\]\|\{\}?*\"]", "", title)
                    emit_deck_page(title, p, "LS", ls, lab, meta)
                    dt[(p, stage, "LS")] = title
                    hl[title] = ls
                    titles.append((title, f"pages/{wiki_fname(title)}"))
        write_hub(meta, by_stage, dest, dt, hl)
        titles.append((meta["title"], f"pages/{wiki_fname(meta['title'])}"))

        by_p = defaultdict(list)
        for stage, heading in meta.get("stages") or []:
            for p in by_stage.get(stage) or []:
                by_p[p].append(stage)
        rank = {"d3": 0, "t4": 0, "d2": 1, "list": 1, "d1": 2, "drop": 3}
        for p, stages in by_p.items():
            rows = []
            for stage in sorted(set(stages), key=lambda s: rank.get(s, 9)):
                lab = STAGE_LAB.get(stage, stage)
                ev = f"[[{meta['title']}]] ({lab})" if lab not in ("Day 1", "Results") else f"[[{meta['title']}]]"
                rec = dest.get(stage, {}).get(p)
                fin = rec[2] if rec and len(rec) == 3 else "—"
                ds_page = dt.get((p, stage, "DS"))
                ls_page = dt.get((p, stage, "LS"))
                ds = f"[[{ds_page}|{hl[ds_page]}]]" if ds_page else "—"
                ls = f"[[{ls_page}|{hl[ls_page]}]]" if ls_page else "—"
                rows.append(
                    f"|- \n| {meta['dates']} || {ev} || {meta['format']} || {fin} || {ds} || {ls}"
                )
            got = upsert_player(p, rows, meta)
            if got:
                titles.append(got)
        list_rows[meta["year"]].append(
            f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || [[{meta['winner']}]]"
        )
        print(
            "event",
            meta["title"],
            {k: len(v) for k, v in by_stage.items()},
        )

    def tag_key(row: str) -> str:
        m = re.search(r"\| (\d{4}-\d{2}(?:-\d{2})?)", row)
        return m.group(1) if m else ""

    for year in list_rows:
        list_rows[year] = sorted(list_rows[year], key=tag_key, reverse=True)
    patch_list(list_rows)
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    titles.append(("European Championships", "pages/European_Championships.wiki"))
    for year, hubs in (
        (
            "2016",
            [
                "2016 Texas Mini Worlds",
                "2016 European Championship",
                "2016 World Championship",
                "2016 Endor Grand Prix",
                "2016 Match Play Championship",
            ],
        ),
        (
            "2015",
            [
                "2015 Texas Mini Worlds",
                "2015 European Championship",
                "2015 World Championship",
                "2015 Match Play Championship",
                "2015 San Diego Grand Prix",
            ],
        ),
    ):
        catp = PAGES / f"Category_{year}.wiki"
        bullets = "\n".join(f"* [[{h}]]" for h in hubs)
        catp.write_text(
            f"""Pages for {year} events, players, and decklists.

* [[List of SWCCG tournaments]]
{bullets}
* [[European Championships]]

[[Category:Tournaments]]
""",
            encoding="utf-8",
            newline="\n",
        )
        titles.append((f"Category:{year}", f"pages/Category_{year}.wiki"))

    seen = set()
    lines = []
    skip_thin = {"pages/Timo_Dusel.wiki"}
    for title, rel in titles:
        rel = rel.replace("\\", "/")
        if rel in skip_thin:
            continue
        if title in seen:
            continue
        seen.add(title)
        lines.append(f"{title}\t{rel}")
    TSV.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    print("TSV", TSV, "n", len(lines))


if __name__ == "__main__":
    main()
