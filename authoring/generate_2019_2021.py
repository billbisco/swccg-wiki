#!/usr/bin/env python3
"""2019–2021 tournament hubs + GEMP/plaintext/HTML decks + player stubs + List rows."""
from __future__ import annotations

import html as htmlmod
import re
import shutil
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT))
import generate_2026_euro as ge  # noqa: E402
import generate_2026_remaining as g26  # noqa: E402
import generate_html_missing as hm  # noqa: E402
import update_gempc_start_fields as ug  # noqa: E402
from file_player import FILE_PLAYER  # noqa: E402
from generate_2026_remaining import upsert_stub  # noqa: E402
from generate_2026_sdso import load_bp_simple, parse_gemp_counts
from generate_2026_sdso import wiki_fname as _wiki_fname


def wiki_fname(title: str) -> str:
    return _wiki_fname(re.sub(r'[?*"]', "", title))  # noqa: E402

PAGES = ROOT / "pages"
STUBS = PAGES / "player-stubs"
MEDIA = ROOT / "y2019-2021-media"
TD = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\td-2021-2026")
DECKS = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2019-2021-decks")
WRAP = Path(r"C:\Users\gythe\.grok\tmp-swccg-gemp\pc-2019-2021")
LIST = PAGES / "List_of_SWCCG_tournaments.wiki"
EC = PAGES / "European_Championships.wiki"

TOKEN = dict(FILE_PLAYER)
TOKEN.update(
    {
        "CKelly": "Chris Kelly",
        "TKelly": "Tom Kelly",
        "CJohnson": "Casey Johnson",
        "JCarulli": "Justin Carulli",
        "MCarulli": "Matt Carulli",
        "Carulli": "Matt Carulli",
        "Castanon": "Fernando Castañón",
        "Castañón": "Fernando Castañón",
        "d'Amboise": "Mike d'Amboise",
        "Palmqvist": "Björn Palmqvist",
        "BTerwilliger": "Brian Terwilliger",
        "CTerwilliger": "Chris Terwilliger",
        "Terwiliger": "Chris Terwilliger",
        "Skilton": "Stephen Skilton",
        "Elia": "Kevin Elia",
        "Sanders": "Steve Sanders",
        "Hummel": "Geoff Hummel",
        "Manning": "Matt Manning",
        "MLewis": "Morgan Lewis",
        "Lavinge": "Jeff Lavigne",
        "Myers": "Paul Myers",
        "Hull": "Chris Hull",
        "Lichtenstein": "Drew Lichtenstein",
        "Malins": "Darren Malins",
        "Martin": "James Martin",
        "McLean": "Kyle McLean",
        "Ortlund": "Gavin Ortlund",
        "Peterson": "Chris Peterson",
        "Pipitone": "Phil Pipitone",
        "Sarachan": "Tom Sarachan",
        "Stearns": "Samuel Stearns",
        "Stenerson": "Zach Stenerson",
        "Tarin": "Miguel Tarin",
        "Trunzo": "Adam Trunzo",
        "Winkelhaus": "Bastian Winkelhaus",
        "Winklehaus": "Bastian Winkelhaus",
        "Culpepper": "Nick Culpepper",
        "Destefanis": "David Destefanis",
        "Engelking": "Rhett Engelking",
        "Eriksen": "Rikard Eriksen",
        "Erisman": "Michael Erisman",
        "Gianetti": "Joe Gianetti",
        "Gilligan": "Mason Gilligan",
        "Hutchins": "Grady Hutchins",
        "Kopsen": "Hugh Kopsen",
        "Main": "Alex Main",
        "Cassidy": "Jonathan Cassidy",
        "Birrer": "Bobby Birrer",
        "Carlson": "Brett Carlson",
        "Chong": "Brandon Chong",
        "Haid": "Tom Haid",
        "Johns": "Jeffrey Johns",
        "JJohns": "Jeffrey Johns",
        "Mack": "Josh Mack",
        "Pittman": "Bill Pittman",
        "Rubin": "Lenny Rubin",
        "Schellberg": "Adam Schellberg",
        "Sobieszczyk": "Forrest Sobieszczyk",
        "Sobieszcyk": "Forrest Sobieszczyk",
        "Shannon": "Kevin Shannon",
        "Jensen": "Jeramie Jensen",
        "Babb": "Kevin Babb",
        "Craft": "Rich Craft",
        "Dredge": "David Dredge",
        "Dubreuil": "Pierre Dubreuil",
        "Jackson": "Derek Jackson",
        "McPherson": "Paul McPherson",
        "Miguel Tarin Vegas": "Miguel Tarin",
        "Miguel Tarin": "Miguel Tarin",
        "Tarin": "Miguel Tarin",
        "Kenneth Brennen": "Kenneth Brennen",
        "Brennen": "Kenneth Brennen",
        "Paul Mcpherson": "Paul McPherson",
        "Mcpherson": "Paul McPherson",
        "Stephan De Vos": "Stephan de Vos",
        "De Vos": "Stephan de Vos",
        "Martin Den Boef": "Martin den Boef",
        "Den Boef": "Martin den Boef",
        "Bastian Winklehaus": "Bastian Winkelhaus",
        "Winklehaus": "Bastian Winkelhaus",
        "Quirin Furgut": "Quirin Fürgut",
        "Matthew Carulli": "Matt Carulli",
        "Alex Hatoum": "AJ Hatoum",
        "John McFarland": "Jon McFarland",
        "Steve Yaeger": "Steven Yaeger",
        "Stephen Baroni": "Steve Baroni",
        "Reisch": "Nick Reisch",
        "jnapolitano": "Jared Napolitano",
        "gogolen": "Chris Gogolen",
        "carulli": "Matt Carulli",
        "HHunter": "Hayes Hunter",
        "EHunter": "Eric Hunter",
        "Hayes": "Hayes Hunter",
        "Fletcher": "Adam Fletcher",
        "FletcherA": "Adam Fletcher",
        "Garchow": "Eric Garchow",
        "Heine": "Jerry Heine",
        "Lamar": "Danny Lamar",
        "Moss": "Andrew Moss",
        "Murray": "Jonathon Murray",
        "DiPaolo": "Jeremy DiPaolo",
        "Dipaolo": "Jeremy DiPaolo",
        "Gladney": "Phillip Gladney",
        "Yim": "Gibson Yim",
        "Bailey": "Brett Bailey",
        "Gorski": "Nick Gorski",
        "Butterworth": "Ben Butterworth",
        "West": "Brian West",
        "Eier": "Brad Eier",
        "Luhks": "Sean Luhks",
        "Billings": "Mark Billings",
        "Coggins": "Paul Coggins",
        "Sperling": "Matt Sperling",
        "Field": "Michael Field",
        "Heilman": "Keegan Heilman",
        "Louderback": "Nate Louderback",
        "Romano": "Brandon Romano",
        "Riendeau": "Jason Riendeau",
        "Huo": "Ming Huo",
        "PJohnson": "Patrick Johnson",
        "Reid Smith": "Reid Smith",
        "SmithR": "Reid Smith",
        "de Vos": "Stephan de Vos",
        "DeVos": "Stephan de Vos",
        "Furgut": "Quirin Fürgut",
        "Fürgut": "Quirin Fürgut",
        "Fürgut": "Quirin Fürgut",
        "Meijssen": "Koen Meijssen",
        "SYFCA": "SYCFA",
        "matt-luts": "Matt Lutz",
        "Matt Luts": "Matt Lutz",
        "matt-mannning": "Matt Manning",
        "Matt Mannning": "Matt Manning",
        "stephen-sanders": "Steve Sanders",
        "Stephen Sanders": "Steve Sanders",
        "stephan-devos": "Stephan de Vos",
        "Stephan Devos": "Stephan de Vos",
        "StephanDeVos": "Stephan de Vos",
        "pat-johnson": "Patrick Johnson",
        "Pat Johnson": "Patrick Johnson",
        "jeffrey-lavigne": "Jeff Lavigne",
        "Jeffrey Lavigne": "Jeff Lavigne",
        "clay-atkin": "Clayton Atkin",
        "Clay Atkin": "Clayton Atkin",
        "charlie-anderson": "Charlie Arlandson",
        "Charlie Anderson": "Charlie Arlandson",
        "bob-birrer": "Bobby Birrer",
        "Bob Birrer": "Bobby Birrer",
        "quirin-fürgut": "Quirin Fürgut",
        "Noah Faelens": "Noah Faelens",
        "Bertrand Momal": "Bertrand Momal",
        "Vjeko Keskic": "Vjeko Keskic",
        "Jan Berueda": "Jan Berueda",
        "Camden Yanaga": "Camden Yanaga",
        "Mitch Nieland": "Mitch Nieland",
        "Stephen Morgan": "Stephen Morgan",
        "Joe Phillips": "Joe Phillips",
        "Jacy Smith": "Jacy Smith",
        "Cal Aldred": "Cal Aldred",
        "Michael Erisman": "Michael Erisman",
        "Brandon Baity": "Brandon Baity",
        "Vikram Bali": "Vikram Bali",
        "Kyle Kallin": "Kyle Kallin",
        "Thang Le": "Thang Le",
        "Chris Angulo": "Chris Angulo",
        "Gabriel Angulo": "Gabriel Angulo",
        "Nathan Angulo": "Nathan Angulo",
        "Andrew Bollentino": "Andrew Bollentino",
        "Stephen Cellucci": "Stephen Cellucci",
        "Ming Huo": "Ming Huo",
        "Adam Schellberg": "Adam Schellberg",
        "Logan Pietig": "Logan Pietig",
        "Sam Tashima": "Sam Tashima",
        "AJ Hatoum": "AJ Hatoum",
        "Lee Edwards": "Lee Edwards",
        "Vinny Rossi": "Vinny Rossi",
        "Jon McFarland": "Jon McFarland",
        "Amar Banger": "Amar Banger",
        "Jeremy DiPaolo": "Jeremy DiPaolo",
        "Brad Eier": "Brad Eier",
        "Gibson Yim": "Gibson Yim",
        "Brett Bailey": "Brett Bailey",
        "Nick Gorski": "Nick Gorski",
        "Ben Butterworth": "Ben Butterworth",
        "Stephen Squirlock": "Stephen Squirlock",
        "Brian West": "Brian West",
        "Winston Plunkett": "Winston Plunkett",
        "Erich Hawbaker": "Erich Hawbaker",
        "Andrew Bethell": "Andrew Bethell",
        "Chris Hull": "Chris Hull",
        "Dan Tartaglione": "Dan Tartaglione",
        "Steve Harpster": "Steve Harpster",
        "Dennis Reinhardt": "Dennis Reinhardt",
        "Bryan Mischke": "Bryan Mischke",
        "Phil Aasen": "Phil Aasen",
        "Ryan Jellison": "Ryan Jellison",
        "Lenny Rubin": "Lenny Rubin",
        "Kyle Krueger": "Kyle Krueger",
        "Matt Lutz": "Matt Lutz",
        "Reid Smith": "Reid Smith",
        "Tom Haid": "Tom Haid",
        "Tom Damen": "Tom Damen",
        "Alex Klimo": "Alex Klimo",
        "Angelo Consoli": "Angelo Consoli",
        "Horst Draudt": "Horst Draudt",
        "Jimmy Faelens": "Jimmy Faelens",
        "Jonas Jakubowski": "Jonas Jakubowski",
        "Mike Klarenbeek": "Mike Klarenbeek",
        "Moritz Karge": "Moritz Karge",
        "Nelson Cazon": "Nelson Cazon",
        "John Moorley": "John Moorley",
        "Kevin Jaap": "Kevin Jaap",
        "Chris Menzel": "Chris Menzel",
        "Marvin Tegeler": "Marvin Tegeler",
        "Gunnar Branden": "Gunnar Branden",
        "Floris de Vries": "Floris de Vries",
        "Cedrik Vanderhaegen": "Cedrik Vanderhaegen",
        "Marc Nickels": "Marc Nickels",
        "Julian-Andrés Smolarek": "Julian Smolarek",
        "Julian Andres Smolarek": "Julian Smolarek",
        "Julian Andrés Smolarek": "Julian Smolarek",
        "Julian Smolarek": "Julian Smolarek",
        "Michael Richards": "Mike Richards",
        "Mike Richards": "Mike Richards",
        "Richards": "Mike Richards",
        "David Destefanis": "David Destefanis",
        "Chris Westergard": "Chris Westergard",
        "Jan Westergard": "Jan Westergard",
        "Greg Nirshberg": "Greg Nirshberg",
        "Jerry Hsiao": "Jerry Hsiao",
        "Jerry Hsaio": "Jerry Hsiao",
        "Jim Li": "Jim Li",
        "Jason Riendeau": "Jason Riendeau",
        "Mike Kessling": "Mike Kessling",
        "Kevin Shannon": "Kevin Shannon",
        "Matt Sperling": "Matt Sperling",
        "Cory Lauer": "Cory Lauer",
        "David Woods": "David Woods",
        "Mark Walseth": "Mark Walseth",
        "Brandon Chong": "Brandon Chong",
        "Daniel Amor": "Daniel Amor",
        "Nate Louderback": "Nate Louderback",
        "Mike Turner": "Mike Turner",
        "Paul Coggins": "Paul Coggins",
        "Brandon Romano": "Brandon Romano",
        "Danny Lamar": "Danny Lamar",
        "Adam Bott": "Adam Bott",
        "John Veasey": "John Veasey",
        "Keegan Heilman": "Keegan Heilman",
        "Casey Johnson": "Casey Johnson",
        "Anthony Howard": "Anthony Howard",
        "Bobby Birrer": "Bobby Birrer",
        "Justin Branch": "Justin Branch",
        "Matthew Harrison-Trainor": "Matthew Harrison-Trainor",
        "Jared Napolitano": "Jared Napolitano",
        "Chris Gogolen": "Chris Gogolen",
        "Chris Wirfs": "Chris Wirfs",
        "Matt Carulli": "Matt Carulli",
        "Justin Carulli": "Justin Carulli",
        "Keith Brown": "Keith Brown",
        "Scott Lingrell": "Scott Lingrell",
        "Paul Myers": "Paul Myers",
        "Steve Baroni": "Steve Baroni",
        "Jarad Konsker": "Jarad Konsker",
        "Conor Britain": "Conor Britain",
        "Gavin Ortlund": "Gavin Ortlund",
        "Brad Kippel": "Brad Kippel",
        "Rikard Eriksen": "Rikard Eriksen",
        "Adam Trunzo": "Adam Trunzo",
        "Ziemowit Skwara": "Ziemowit Skwara",
        "Timo Dusel": "Timo Dusel",
        "Brett Carlson": "Brett Carlson",
        "Justin Miyashiro": "Justin Miyashiro",
        "Matt Sokol": "Matt Sokol",
        "Bill Kafer": "Bill Kafer",
        "Aaron Kingery": "Aaron Kingery",
        "James Martin": "James Martin",
        "Drew Lichtenstein": "Drew Lichtenstein",
        "Ryan Sersen": "Ryan Sersen",
        "Patrick Johnson": "Patrick Johnson",
        "Barry Alperstein": "Barry Alperstein",
        "Casey Anis": "Casey Anis",
        "Robbie Hendon": "Robbie Hendon",
        "Tom Kelly": "Tom Kelly",
        "Chris Kelly": "Chris Kelly",
        "Joe Olson": "Joe Olson",
        "Matt Scott": "Matt Scott",
        "Greg Shaw": "Greg Shaw",
        "Hayes Hunter": "Hayes Hunter",
        "Eric Hunter": "Eric Hunter",
        "Jonny Chu": "Jonny Chu",
        "Emil Wallin": "Emil Wallin",
        "Bastian Winkelhaus": "Bastian Winkelhaus",
        "Quirin Fürgut": "Quirin Fürgut",
        "Fernando Castañón": "Fernando Castañón",
        "Stephen Skilton": "Stephen Skilton",
        "Kevin Elia": "Kevin Elia",
        "Jeffrey Johns": "Jeffrey Johns",
        "Geoff Hummel": "Geoff Hummel",
        "Matt Manning": "Matt Manning",
        "Morgan Lewis": "Morgan Lewis",
        "Garrett Larson": "Garrett Larson",
        "Brad Reinhold": "Brad Reinhold",
        "Kendall Halman": "Kendall Halman",
        "Phillip Gladney": "Phillip Gladney",
        "Jonathon Murray": "Jonathon Murray",
        "Jerry Heine": "Jerry Heine",
        "Paul Coggins": "Paul Coggins",
        "Mark Billings": "Mark Billings",
        "Miguel Tarin Vegas": "Miguel Tarin",
        "Miguel Tarin": "Miguel Tarin",
        "Kenneth Brennen": "Kenneth Brennen",
        "Andrew Bethell": "Andrew Bethell",
        "Justin Branch": "Justin Branch",
        "Ziemowit Skwara": "Ziemowit Skwara",
        "Timo Dusel": "Timo Dusel",
        "Andrew Moss": "Andrew Moss",
        "Elspeth Jellison": "Elspeth Jellison",
        "Nate Davis": "Nate Davis",
        "Gosse Zeilstra": "Gosse Zeilstra",
        "David Beaubier": "David Beaubier",
        "Matt Smith": "Matt Smith",
        "Seth Acree": "Seth Acree",
        "Steve Brentson": "Steve Brentson",
        "Brentson": "Steve Brentson",
        "Shawn Dickson": "Shawn Dickson",
        "Dickson": "Shawn Dickson",
        "Bryan Gravener": "Bryan Gravener",
        "Gravener": "Bryan Gravener",
        "Mike Pistone": "Mike Pistone",
        "Michael Pistone": "Mike Pistone",
        "Pistone": "Mike Pistone",
        "Tim Simon": "Tim Simon",
        "Isaac Story": "Isaac Story",
        "Issac Story": "Isaac Story",
        "Story": "Isaac Story",
        "Nathan Trothing": "Nathan Trothing",
        "Trothing": "Nathan Trothing",
        "Andy Wexstten": "Andy Wexstten",
        "Wexstten": "Andy Wexstten",
        "Edward Chien": "Edward Chien",
        "Chien": "Edward Chien",
        "Trevor Partridge": "Trevor Partridge",
        "Partridge": "Trevor Partridge",
        "Joe Pinto": "Joe Pinto",
        "Pinto": "Joe Pinto",
        "Jeffrey Scales": "Jeffrey Scales",
        "Scales": "Jeffrey Scales",
        "Travis Thompson": "Travis Thompson",
        "Sam Olson": "Sam Olson",
        "Brian Herold": "Brian Herold",
        "Herold": "Brian Herold",
        "Tom Marlin": "Tom Marlin",
        "Marlin": "Tom Marlin",
        "Sean Miller": "Sean Miller",
        "Mike Richards": "Mike Richards",
        "Richards": "Mike Richards",
        "Matt Thornton": "Matt Thornton",
        "Thornton": "Matt Thornton",
        "Max DeWitt": "Max DeWitt",
        "DeWitt": "Max DeWitt",
        "Austin Jacobus": "Austin Jacobus",
        "Jacobus": "Austin Jacobus",
        "Piotr Ptak": "Piotr Ptak",
        "Ptak": "Piotr Ptak",
        "Nico Johannes Kreidl": "Nico Johannes Kreidl",
        "Nico Kreidl": "Nico Johannes Kreidl",
        "Kreidl": "Nico Johannes Kreidl",
        "Lukasz Saczek": "Lukasz Saczek",
        "Łukasz Saczek": "Lukasz Saczek",
        "Saczek": "Lukasz Saczek",
        "Kristian Lund": "Kristian Lund",
        "Lund": "Kristian Lund",
        "Dennis Schwarz": "Dennis Schwarz",
        "Schwarz": "Dennis Schwarz",
        "Rasmus Juul": "Rasmus Juul",
        "Juul": "Rasmus Juul",
        "Kristoffer Basse Hedlund": "Kristoffer Basse Hedlund",
        "Hedlund": "Kristoffer Basse Hedlund",
        "György Póra": "György Póra",
        "Gyorgy Pora": "György Póra",
        "Póra": "György Póra",
        "Ulli Reuter": "Ulli Reuter",
        "Reuter": "Ulli Reuter",
        "Piotr Jarnot": "Piotr Jarnot",
        "Jarnot": "Piotr Jarnot",
        "Julian Cochard": "Julian Cochard",
        "Cochard": "Julian Cochard",
        "Ralf W.": "Ralf W.",
        "Ralf W": "Ralf W.",
        "Kent Larsen": "Kent Larsen",
        "Peter Rowlands": "Peter Rowlands",
        "Rowlands": "Peter Rowlands",
        "Stefan Boersma": "Stefan Boersma",
        "Boersma": "Stefan Boersma",
        "Robert Smolarek": "Robert Smolarek",
        "Smolarek": "Robert Smolarek",
        "Gunnar Brandén": "Gunnar Brandén",
        "Gunnar Branden": "Gunnar Brandén",
        "Brandén": "Gunnar Brandén",
        "Branden": "Gunnar Brandén",
        "Jay Chutino": "Jay Chutino",
        "Chutino": "Jay Chutino",
        "Nathan Angulo": "Nathan Angulo",
        "Aaron Bott": "Aaron Bott",
        "Steven Lamar": "Danny Lamar",
        "Erich Hawbaker": "Erich Hawbaker",
        "Eric Hawbaker": "Erich Hawbaker",
        "Hawbaker": "Erich Hawbaker",
        "Jon Holtet": "Jon Benkert Holtet",
        "Jon Benkert Holtet": "Jon Benkert Holtet",
        "Holtet": "Jon Benkert Holtet",
        "Casper Jørgensen": "Casper Jørgensen",
        "Casper Jorgensen": "Casper Jørgensen",
        "Jørgensen": "Casper Jørgensen",
        "Jonas Hagen Nørregaard": "Jonas Hagen Nørregaard",
        "Jonas Hagen Norregaard": "Jonas Hagen Nørregaard",
        "Nørregaard": "Jonas Hagen Nørregaard",
        "Erik Spijksma": "Erik Spijksma",
        "Eric Spijksma": "Erik Spijksma",
        "Spijksma": "Erik Spijksma",
        "Darren Malins": "Darren Malins",
        "Peter Jacobson": "Peter Jacobson",
        "Jacobson": "Peter Jacobson",
        "Marc Nickels": "Marc Nickels",
        "Nickels": "Marc Nickels",
        "Joe Gianetti": "Joe Gianetti",
        "Joe Giannetti": "Joe Giannetti",
        "Giannetti": "Joe Giannetti",
        "Adam Fletcher": "Adam Fletcher",
        "Grady Hutchins": "Grady Hutchins",
        "Hutchins": "Grady Hutchins",
        "Tom Sarachan": "Tom Sarachan",
        "Sarachan": "Tom Sarachan",
        "Kyle McLean": "Kyle McLean",
        "McLean": "Kyle McLean",
        "Nick Reisch": "Nick Reisch",
        "Reisch": "Nick Reisch",
        "Sean Mackin": "Sean Mackin",
        "Mackin": "Sean Mackin",
        "Chad Lawrence": "Chad Lawrence",
        "Lawrence": "Chad Lawrence",
        "Dan Tartaglione": "Dan Tartaglione",
        "Tartaglione": "Dan Tartaglione",
        "Wayne Cullen": "Wayne Cullen",
        "Cullen": "Wayne Cullen",
        "Stephen Cellucci": "Stephen Cellucci",
        "Cellucci": "Stephen Cellucci",
        "Stephen Morgan": "Stephen Morgan",
        "Jeff Lavigne": "Jeff Lavigne",
        "Jeffrey Lavigne": "Jeff Lavigne",
        "Lavigne": "Jeff Lavigne",
        "Fernando Castañón": "Fernando Castañón",
        "Fernando Castanon": "Fernando Castañón",
        "Ziemowit Skwara": "Ziemowit Skwara",
        "Skwara": "Ziemowit Skwara",
        "Patrik Csapi": "Patrik Csapi",
        "Csapi": "Patrik Csapi",
        "Vjeko Keskic": "Vjeko Keskic",
        "Keskic": "Vjeko Keskic",
        "Noah Faelens": "Noah Faelens",
        "Jimmy Faelens": "Jimmy Faelens",
        "Faelens": "Jimmy Faelens",
        "Bertrand Momal": "Bertrand Momal",
        "Momal": "Bertrand Momal",
        "Jonas Jakubowski": "Jonas Jakubowski",
        "Jakubowski": "Jonas Jakubowski",
        "Alex Klimo": "Alex Klimo",
        "Klimo": "Alex Klimo",
        "Angelo Consoli": "Angelo Consoli",
        "Consoli": "Angelo Consoli",
        "Horst Draudt": "Horst Draudt",
        "Draudt": "Horst Draudt",
        "Mike Klarenbeek": "Mike Klarenbeek",
        "Klarenbeek": "Mike Klarenbeek",
        "Moritz Karge": "Moritz Karge",
        "Karge": "Moritz Karge",
        "Nelson Cazon": "Nelson Cazon",
        "Cazon": "Nelson Cazon",
        "John Moorley": "John Moorley",
        "Moorley": "John Moorley",
        "Marvin Tegeler": "Marvin Tegeler",
        "Tegeler": "Marvin Tegeler",
        "Floris de Vries": "Floris de Vries",
        "Cedrik Vanderhaegen": "Cedrik Vanderhaegen",
        "Vanderhaegen": "Cedrik Vanderhaegen",
        "Julian Smolarek": "Julian Smolarek",
        "Julian-Andrés Smolarek": "Julian Smolarek",
        "Smolarek": "Julian Smolarek",
        "David Destefanis": "David Destefanis",
        "Destefanis": "David Destefanis",
        "Greg Nirshberg": "Greg Nirshberg",
        "Nirshberg": "Greg Nirshberg",
        "Jerry Hsiao": "Jerry Hsiao",
        "Hsiao": "Jerry Hsiao",
        "Jim Li": "Jim Li",
        "Thang Le": "Thang Le",
        "Andrew Bollentino": "Andrew Bollentino",
        "Bollentino": "Andrew Bollentino",
        "Camden Yanaga": "Camden Yanaga",
        "Yanaga": "Camden Yanaga",
        "Mitch Nieland": "Mitch Nieland",
        "Nieland": "Mitch Nieland",
        "Joe Phillips": "Joe Phillips",
        "Winston Plunkett": "Winston Plunkett",
        "Plunkett": "Winston Plunkett",
        "Ralf W.": "Ralf W.",
        "Adam Radic": "Adam Radic",
        "Radic": "Adam Radic",
        "John Werner": "John Werner",
        "Werner": "John Werner",
        "Zach Stenerson": "Zach Stenerson",
        "Zack Stenerson": "Zach Stenerson",
        "Stenerson": "Zach Stenerson",
        "Jeremie Jensen": "Jeramie Jensen",
        "Jeramie Jensen": "Jeramie Jensen",
        "Kevin Babb": "Kevin Babb",
        "Babb": "Kevin Babb",
        "Rich Craft": "Rich Craft",
        "Craft": "Rich Craft",
        "Pierre Dubreuil": "Pierre Dubreuil",
        "Dubreuil": "Pierre Dubreuil",
        "Derek Jackson": "Derek Jackson",
        "Steven Yaeger": "Steven Yaeger",
        "Yaeger": "Steven Yaeger",
        "Brandon Nguyen": "Brandon Nguyen",
        "Nguyen": "Brandon Nguyen",
        "Jeff Johns": "Jeffrey Johns",
        "Michael Pistone": "Mike Pistone",
        "Zachary Stenerson": "Zach Stenerson",
    }
)

LS_OBJ = re.compile(
    r"(?i)^(WYS|HITCO|OA|Legend|Profit|TRM|EBO|Diplo|QMC|NoIdea|No Idea|"
    r"QuiCommuning|YodaCommuning|WHAP|HB|Hidden Base|TIGIH|RST|MWYHL|"
    r"AiTC|AITC|Harvest|ObiHut|ChiefChirpasHut|CheifChirpasHut|"
    r"MainPowerGenerators|RendezvousPoint|Hyperdrive|Y4O|Y4Ops|LTWW|"
    r"Agents in the Court|Old Allies|Watch Your Step|They Have No Idea|"
    r"Echo Base|Quiet Mining|We Have A Plan|We Had A|Rescue The Princess|"
    r"Communing|Yavin 4|Combat Preparedness|Careful Planning|"
    r"Let The Wookiee|He Is The Chosen|Diplomatic Mission|"
    r"The Galaxy May Need|There Is Good|This Is Getting Out|"
    r"Mind What You|The Hyperdrive|You Can Either Profit|"
    r"Plead My Case|The Hidden Path|On The Verge|The Force Is Strong|"
    r"Rebel Strike|Massassi|Don't Underestimate|I Don't Like You|"
    r"Local Uprising|Senate Gungans|Jcc Mains|HITCO)",
)
DS_OBJ = re.compile(
    r"(?i)^(HD|HDv|Hunt Down|ISB|AOBS|BHBM|CCT|Map|SC|SYCFA|SYFCA|"
    r"TDIGWATT|TTO|IE|Invasion|Court|Watto|Combat Readiness|MKOS|ASM|"
    r"Maul|EOps|Eops|ROps|ROPS|Senate Occupied|Mustafar|HothCR|Hoth CR|"
    r"COVG|SSA|Shadow Collective|This Deal|Carbon Chamber|Bring Him|"
    r"A Stunning|Imperial Entanglements|Endor Ops|Endor Operations|"
    r"Ralltiir|I Want That Map|Agents Of Black Sun|No Money|"
    r"My Kind Of Scum|Set Your Course|There Is No Try|"
    r"A Great Tactician|The First Order Reigns|The Shield Will Be Down|"
    r"Hunt For The Droid|Emperor's Orders|Watto's Box|"
    r"Court Of The Vile|5th Marker)",
)


def canon(token: str) -> str:
    token = re.sub(r"\s+", " ", token).strip(" -_")
    token = token.replace("Winklehaus", "Winkelhaus").replace("Pat Johnson", "Patrick Johnson")
    token = token.replace("Furgut", "Fürgut").replace("Castanon", "Castañón")
    token = token.replace("Eric Spijksma", "Erik Spijksma")
    if token in TOKEN:
        return TOKEN[token]
    last = token.split()[-1] if token else token
    if last in TOKEN and " " not in token:
        return TOKEN[last]
    return TOKEN.get(token, token)


def stem(name: str) -> str:
    for ext in (".txt", ".html", ".xml", ".TXT"):
        if name.endswith(ext):
            name = name[: -len(ext)]
    return name.strip()


def side_from_obj(obj: str) -> str | None:
    o = obj.strip()
    if LS_OBJ.match(o) and not DS_OBJ.match(o):
        return "LS"
    if DS_OBJ.match(o) and not LS_OBJ.match(o):
        return "DS"
    return None


GH_HEAD = {
    "STARTING": None,
    "CHARACTER": "CHARACTER",
    "CHARACTERS": "CHARACTER",
    "DEVICE": "DEVICE",
    "DEVICES": "DEVICE",
    "EFFECT": "EFFECT",
    "EFFECTS": "EFFECT",
    "INTERRUPT": "INTERRUPT",
    "INTERRUPTS": "INTERRUPT",
    "LOCATION": "LOCATION",
    "LOCATIONS": "LOCATION",
    "STARSHIP": "STARSHIP",
    "STARSHIPS": "STARSHIP",
    "VEHICLE": "VEHICLE",
    "VEHICLES": "VEHICLE",
    "WEAPON": "WEAPON",
    "WEAPONS": "WEAPON",
    "OBJECTIVE": "OBJECTIVE",
    "OBJECTIVES": "OBJECTIVE",
    "ADMIRAL'S ORDER": "ADMIRAL'S_ORDER",
    "ADMIRAL'S ORDERS": "ADMIRAL'S_ORDER",
    "ADMIRALS ORDER": "ADMIRAL'S_ORDER",
    "EPIC EVENT": "EPIC_EVENT",
    "EPIC EVENTS": "EPIC_EVENT",
    "JEDI TEST": "JEDI_TEST",
    "JEDI TESTS": "JEDI_TEST",
    "PODRACER": "PODRACER",
    "PODRACERS": "PODRACER",
    "DEFENSIVE SHIELD": "DEFENSIVE_SHIELD",
    "DEFENSIVE SHIELDS": "DEFENSIVE_SHIELD",
}


def parse_github_txt(path: Path, by_id, by_title):
    text = path.read_text(encoding="utf-8", errors="replace")
    cat = None
    counts = Counter()
    cards = []
    for line in text.splitlines():
        line = line.strip()
        if not line:
            continue
        key = line.upper().replace("’", "'")
        if key in GH_HEAD:
            cat = GH_HEAD[key]
            continue
        if cat is None and key in ("STARTING",):
            cat = None
            continue
        mm = re.match(r"(\d+)\s*x\s+(.+)$", line, re.I)
        if mm:
            n = int(mm.group(1))
            title = mm.group(2).strip()
        else:
            if cat is None and not line[0].isalpha():
                continue
            if cat is None and len(line) > 60:
                continue
            n = 1
            title = line
        title = title.replace("’", "'")
        rec = by_title.get(title.lower())
        use_cat = cat
        if use_cat is None:
            use_cat = rec["cat"] if rec else "UNKNOWN"
        counts[(use_cat, title)] += n
        for _ in range(n):
            cards.append(("", title, "card"))
    return counts, cards


def attach_ids(cards, bp):
    title_to_id = {}
    for cid, row in bp.items():
        title = (row.get("title") or "").strip()
        if not title:
            continue
        title_to_id.setdefault(title.lower(), cid)
        if bool(row.get("hasVirtualSuffix")):
            title_to_id.setdefault(title.lower() + " (v)", cid)
            if not title.endswith("(V)"):
                title_to_id.setdefault((title + " (V)").lower(), cid)
    out = []
    for cid, title, tag in cards:
        if not cid:
            cid = (
                title_to_id.get(title.lower())
                or title_to_id.get(title.replace(" (V)", "").lower())
                or ""
            )
            if not cid and "/" in title:
                left = title.split("/")[0].strip()
                cid = (
                    title_to_id.get(left.lower())
                    or title_to_id.get(left.replace(" (V)", "").lower())
                    or ""
                )
        out.append((cid, title, tag))
    return out


def enrich(cards, bp, by_title):
    cards = attach_ids(cards, bp)
    counts = Counter()
    for cid, title, tag in cards:
        if tag != "card":
            continue
        rec = bp.get(cid) or {}
        cat = (rec.get("cardCategory") or "").upper()
        if not cat:
            rec2 = by_title.get(title.lower()) or by_title.get(title.replace(" (V)", "").lower()) or {}
            cat = (rec2.get("cat") or "UNKNOWN").upper()
        counts[(cat, title)] += 1
    return counts, cards


LEGACY_HEAD = {
    "STARTING": None,
    "STARTING:": None,
    "CHARACTER": "CHARACTER",
    "CHARACTERS": "CHARACTER",
    "CHARACTERS:": "CHARACTER",
    "EFFECT": "EFFECT",
    "EFFECTS": "EFFECT",
    "EFFECTS:": "EFFECT",
    "INTERRUPT": "INTERRUPT",
    "INTERRUPTS": "INTERRUPT",
    "INTERRUPTS:": "INTERRUPT",
    "LOCATION": "LOCATION",
    "LOCATIONS": "LOCATION",
    "LOCATIONS:": "LOCATION",
    "STARSHIP": "STARSHIP",
    "STARSHIPS": "STARSHIP",
    "STARSHIPS:": "STARSHIP",
    "STARSHPIS": "STARSHIP",
    "STARSHPIS:": "STARSHIP",
    "VEHICLE": "VEHICLE",
    "VEHICLES": "VEHICLE",
    "VEHICLES:": "VEHICLE",
    "WEAPON": "WEAPON",
    "WEAPONS": "WEAPON",
    "WEAPONS:": "WEAPON",
    "DEVICE": "DEVICE",
    "DEVICES": "DEVICE",
    "DEVICES:": "DEVICE",
    "OBJECTIVE": "OBJECTIVE",
    "OBJECTIVES": "OBJECTIVE",
    "OBJECTIVES:": "OBJECTIVE",
    "EPIC EVENT": "EPIC_EVENT",
    "EPIC EVENTS": "EPIC_EVENT",
    "EPIC EVENTS:": "EPIC_EVENT",
    "DEFENSIVE SHIELD": "DEFENSIVE_SHIELD",
    "DEFENSIVE SHIELDS": "DEFENSIVE_SHIELD",
    "DEFENSIVE SHIELDS:": "DEFENSIVE_SHIELD",
    "ADMIRAL'S ORDER": "ADMIRAL'S_ORDER",
    "ADMIRAL'S ORDERS": "ADMIRAL'S_ORDER",
    "ADMIRAL'S ORDERS:": "ADMIRAL'S_ORDER",
    "JEDI TEST": "JEDI_TEST",
    "JEDI TESTS": "JEDI_TEST",
    "PODRACER": "PODRACER",
    "PODRACERS": "PODRACER",
}


def parse_pc_legacy(path: Path):
    """2019–2021 PC HTML: 'Characters:' headings, bare titles, and 'Title x2'."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(
        r"(?is)fl-module-fl-post-content[\s\S]*?fl-module-content fl-node-content\">([\s\S]+?)Posted in",
        raw,
    )
    chunk = m.group(1) if m else raw
    chunk = re.sub(r"<br\s*/?>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"</p>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<p[^>]*>", "\n", chunk, flags=re.I)
    chunk = re.sub(r"<[^>]+>", "\n", chunk)
    chunk = htmlmod.unescape(chunk)
    chunk = re.sub(r"[ \t]+", " ", chunk)
    cat = None
    in_list = False
    counts = Counter()
    cards = []
    for line in chunk.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("Posted"):
            break
        key = line.upper().replace("’", "'").replace("‘", "'")
        if key in LEGACY_HEAD:
            cat = LEGACY_HEAD[key]
            in_list = True
            continue
        if key.rstrip(":") in LEGACY_HEAD:
            cat = LEGACY_HEAD[key.rstrip(":")]
            in_list = True
            continue
        if not in_list:
            if (
                re.search(r"\(V\)", line)
                or re.match(r"\d+\s*x\s+", line, re.I)
                or re.match(r".+\s+x\s*\d+$", line, re.I)
                or (
                    line[0].isupper()
                    and len(line.split()) >= 2
                    and not line.lower().startswith(("home ", "posted", "skip to", "volunteer"))
                )
            ):
                in_list = True
            else:
                continue
        n = 1
        title = line
        mm = re.match(r"(\d+)\s*x\s+(.+)$", line, re.I)
        if mm:
            n = int(mm.group(1))
            title = mm.group(2).strip()
        else:
            mm = re.match(r"(.+?)\s+x\s*(\d+)$", line, re.I)
            if mm:
                title = mm.group(1).strip()
                n = int(mm.group(2))
        title = title.replace("’", "'").rstrip("*")
        title = re.sub(r"\s+v$", " (V)", title, flags=re.I)
        use_cat = cat or "UNKNOWN"
        counts[(use_cat, title)] += n
        for _ in range(n):
            cards.append(("", title, "card"))
    return counts, cards


def parse_html_deck(path: Path, bp, by_title):
    counts, cards = ge.parse_pc_html(path)
    if sum(counts.values()) < 20:
        legacy, lcards = parse_pc_legacy(path)
        if sum(legacy.values()) > sum(counts.values()):
            counts, cards = legacy, lcards
    return enrich(cards, bp, by_title)


def parse_any(path: Path, by_id, by_title, bp):
    try:
        counts, cards = parse_gemp_counts(path, by_id, by_title)
    except Exception:
        counts, cards = Counter(), []
    if sum(counts.values()) < 8:
        gh_counts, gh_cards = parse_github_txt(path, by_id, by_title)
        if sum(gh_counts.values()) > sum(counts.values()):
            counts, cards = gh_counts, gh_cards
    return enrich(cards, bp, by_title)


def split_glued(rest: str):
    rest = rest.replace("_", " ").strip()
    m = re.match(r"(.+?)(DS|LS|Ds|Ls|ds|ls)[-_ ]+(.+)$", rest)
    if m:
        token, side, obj = m.groups()
        if side == "DS" and re.match(
            r"(?i)^(OA|HITCO|Profit|Legend|Diplo|QMC|EBO|WHAP)$", obj.strip()
        ):
            side = "LS"
        return canon(token.strip()), side.upper(), obj.strip()
    m = re.match(r"(.+?)(DS|LS|Ds|Ls|ds|ls)(.+)$", rest)
    if m:
        return canon(m.group(1).strip()), m.group(2).upper(), m.group(3).strip(" -_")
    return None


def parse_gemp_file(folder: str, name: str):
    if name in NATS_FILES:
        return NATS_FILES[name]
    raw = stem(name)
    raw = raw.replace("  ", " ").strip()
    m = re.match(r"Day ([123]) (.+)$", raw)
    if m:
        day, rest = m.groups()
        got = split_glued(rest)
        if not got:
            return None
        player, side, obj = got
        t8 = day != "1"
        stage = {"1": "d1", "2": "d2", "3": "d3"}[day]
        return player, t8, side, obj, stage
    m = re.match(r"2021 MPC (Day 1|Top 4) (.+)$", raw)
    if m:
        st, rest = m.groups()
        rest = rest.replace("-Top4-", "-").replace("Top4-", "")
        got = split_glued(rest)
        if not got:
            return None
        player, side, obj = got
        t8 = st == "Top 4"
        return player, t8, side, obj, ("t4" if t8 else "d1")
    m = re.match(r"(.+?)Day([123])(DS|LS)[-_ ](.+)$", raw)
    if m:
        token, day, side, obj = m.groups()
        if side == "DS" and re.match(
            r"(?i)^(OA|HITCO|Profit|Legend|Diplo|QMC|EBO|WHAP)$", obj.strip()
        ):
            side = "LS"
        t8 = day != "1"
        stage = {"1": "d1", "2": "d2", "3": "d3"}[day]
        return canon(token), t8, side, obj, stage
    if folder.startswith("2020-worlds") or folder.startswith("2021-"):
        got = split_glued(raw)
        if got:
            player, side, obj = got
            if "d3" in folder:
                return player, True, side, obj, "d3"
            if "d2" in folder or folder.endswith("-t4"):
                return player, True, side, obj, "d2" if "d2" in folder else "t4"
            if "throwback" in folder:
                return None
            return player, False, side, obj, "d1"
    m = re.match(r"PREF2 2021 Event Decklists (\d+) PREF2 (.+?) 2021\s*$", raw)
    if m:
        place = int(m.group(1))
        blob = m.group(2).strip()
        player = THROWBACK[place - 1] if 1 <= place <= len(THROWBACK) else None
        if not player:
            return None
        side = "LS" if LS_OBJ.search(blob) and not DS_OBJ.search(blob) else "DS"
        if DS_OBJ.search(blob) and not LS_OBJ.search(blob):
            side = "DS"
        if re.search(r"(?i)\b(WYS|EBO|RST|MWYHL|HITCO|Profit|Harvest)\b", blob):
            side = "LS"
        if re.search(r"(?i)\b(ISB|MKOS|SYCFA|HD|BHBM|CCT|AOBS|Eops|EOps)\b", blob):
            side = "DS"
        obj = blob
        return player, True, side, obj, "t8"
    return None


THROWBACK = [
    "Stephen Skilton",
    "Jared Napolitano",
    "Matt Carulli",
    "Kevin Elia",
    "Steve Sanders",
    "Jeffrey Johns",
    "Winston Plunkett",
    "Chris Gogolen",
    "Garrett Larson",
    "Erich Hawbaker",
    "Morgan Lewis",
    "Ryan Sersen",
    "Brad Reinhold",
    "Geoff Hummel",
    "Matt Manning",
    "Kendall Halman",
]

EVENTS = [
    {
        "key": "21worlds",
        "folders": ["2021-worlds"],
        "title": "2021 World Championship",
        "year": "2021",
        "tag": "2021-10",
        "dates": "7–10 October 2021",
        "site": "Arlington, Virginia (Washington, D.C.)",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2021 World Championship''' was the Players Committee World Championship in Arlington, Virginia (Washington, D.C.), 7–10 October 2021. [[Joe Olson]] defeated [[Matt Scott]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2021-world-championships/",
        "forum": "https://forum.starwarsccg.org/viewforum.php?f=1240",
        "deck_prefix": "2021 Worlds",
        "list_label": "World Championship",
        "stages": [("d2", "Top 8", True), ("d1", "Day 1", False)],
        "order": {
            "d2": [
                "Joe Olson",
                "Matt Scott",
                "Jared Napolitano",
                "Barry Alperstein",
                "Tom Haid",
                "Greg Shaw",
                "Robbie Hendon",
                "Casey Anis",
            ]
        },
    },
    {
        "key": "21throwback",
        "folders": ["2021-throwback"],
        "title": "2021 Worlds Throwback Event",
        "year": "2021",
        "tag": "2021-10",
        "dates": "8 October 2021",
        "site": "Arlington, Virginia (Washington, D.C.)",
        "format": "[[Premiere - Reflections II]]",
        "winner": "Stephen Skilton",
        "lead": "'''2021 Worlds Throwback Event''' (Prem-RefII) was the Players Committee Premiere–Reflections II constructed event at the 2021 World Championship weekend in Arlington, Virginia, 8 October 2021. [[Stephen Skilton]] finished 1st in the published field of 16.",
        "pc": "https://www.starwarsccg.org/2021-worlds-retro-prem-ref-ii-event/",
        "forum": "https://www.starwarsccg.org/2021-10-worlds-throwback-prem-refii-event/",
        "deck_prefix": "2021 Worlds Throwback",
        "list_label": "Worlds Throwback Event (Prem-RefII)",
        "stages": [("t8", "Finish", True)],
        "order": {"t8": THROWBACK},
    },
    {
        "key": "21ocs",
        "folders": [],
        "title": "2021 Online Championship Series Playoffs",
        "year": "2021",
        "tag": "2021-11",
        "dates": "October–November 2021",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Matthew Harrison-Trainor",
        "lead": "'''2021 Online Championship Series Playoffs''' was the Players Committee OCS playoff on GEMP, October–November 2021. [[Matthew Harrison-Trainor]] defeated [[Justin Branch]] in the Finals. Harrison-Trainor defeated [[Brad Kippel]] in the Round of 16 (Carbon Chamber Testing / Quiet Mining Colony), [[Drew Lichtenstein]] in the Quarterfinals (Hunt Down / Qui-Gon Communing), and [[Charlie Arlandson]] in the Semifinals (ISB Operations / They Have No Idea We're Coming). Branch defeated [[Brian Fred]] in the Round of 16, [[Paul Myers]] in the Quarterfinals (Hunt Down (V) / Echo Base Operations), and [[Chris Hull]] in the Final Four (ISB Operations / Yoda Communing).",
        "pc": "https://www.starwarsccg.org/2021-online-championship-series-wrap-mht-victorious/",
        "forum": "https://forum.starwarsccg.org/viewforum.php?f=1240",
        "deck_prefix": "2021 OCS",
        "list_label": "Online Championship Series Playoffs",
        "stages": [],
        "order": {},
        "stub_only": True,
    },
    {
        "key": "21outrider",
        "folders": [],
        "title": "2021 Outrider Cup",
        "year": "2021",
        "tag": "2021-12",
        "dates": "November 2021 – 26 January 2022",
        "site": "GEMP (teams)",
        "format": "[[Open]]",
        "winner": "[[Team Europe]]",
        "lead": "'''2021 Outrider Cup''' (Outrider Cup II) was the Players Committee biennial Europe versus United States team event on GEMP, November 2021 – 26 January 2022. Team Europe defeated Team USA in a captains' tiebreaker after the 12 regulation games finished 6–6.",
        "pc": "https://www.starwarsccg.org/outrider-cup-ii/",
        "forum": "",
        "deck_prefix": "2021 Outrider Cup",
        "list_label": "Outrider Cup",
        "stages": [("usa", "Team USA", True), ("eur", "Team Europe", True), ("tb", "Tiebreaker", True)],
        "order": {
            "usa": [
                "Joe Olson",
                "Matthew Harrison-Trainor",
                "Hayes Hunter",
                "Paul Myers",
                "Justin Desai",
                "Jared Napolitano",
            ],
            "eur": [
                "Bastian Winkelhaus",
                "Justin Branch",
                "Quirin Fürgut",
                "Timo Dusel",
                "Ziemowit Skwara",
                "Miguel Tarin",
            ],
        },
        "html_only": True,
    },
    {
        "key": "21regionals",
        "folders": [],
        "title": "2021 Regional Championships",
        "year": "2021",
        "tag": "2021-08",
        "dates": "21 August – 4 December 2021",
        "site": "various",
        "format": "[[Open]]",
        "winner": "—",
        "lead": "'''2021 Regional Championships''' were the Players Committee regional constructed events from 21 August to 4 December 2021.",
        "pc": "https://www.starwarsccg.org/2021-regional-championships/",
        "forum": "",
        "deck_prefix": "2021 Regionals",
        "list_label": "Regional Championships",
        "stages": [],
        "order": {},
        "html_only": True,
        "regional": True,
    },
    {
        "key": "21nats",
        "folders": ["2021-nats"],
        "title": "2021 U.S. National Championship",
        "year": "2021",
        "tag": "2021-07",
        "dates": "17–18 July 2021",
        "site": "Denver, Colorado",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2021 U.S. National Championship''' was the Players Committee U.S. National Championship in Colorado, 17–18 July 2021. [[Joe Olson]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2021-us-nationals/",
        "forum": "",
        "deck_prefix": "2021 US Nationals",
        "list_label": "U.S. National Championship",
        "stages": [("d2", "Day 2", True), ("d1", "Day 1", False)],
        "order": {
            "d2": [
                "Joe Olson",
                "Hayes Hunter",
                "Dennis Reinhardt",
                "Mike Kessling",
                "Charlie Arlandson",
                "Kevin Shannon",
                "Matt Lutz",
                "Kyle Krueger",
            ],
            "d1": [
                "Charlie Arlandson",
                "Dennis Reinhardt",
                "Kevin Shannon",
                "Joe Olson",
                "Mike Kessling",
                "Hayes Hunter",
                "Matt Lutz",
                "Kyle Krueger",
                "Justin Desai",
                "Matt Sperling",
                "Cal Aldred",
                "Cory Lauer",
                "David Woods",
                "Vikram Bali",
                "Brian Fred",
                "Chris Wirfs",
                "Jeff Lavigne",
                "Mark Walseth",
                "Justin Miyashiro",
                "Brandon Chong",
                "Daniel Amor",
                "Jan Westergard",
                "Anthony Howard",
                "Bobby Birrer",
                "Matt Wadden",
                "Clayton Atkin",
                "Lenny Rubin",
                "Nate Louderback",
                "Mike Turner",
                "Drew Lichtenstein",
                "Steve Harpster",
                "Bill Kafer",
                "Paul Coggins",
                "Lee Edwards",
                "Ryan Sersen",
                "Brandon Romano",
                "Danny Lamar",
                "Adam Bott",
                "Jason Riendeau",
                "John Veasey",
                "Keegan Heilman",
                "Casey Johnson",
                "Jon McFarland",
                "Vinny Rossi",
                "Aaron Bott",
                "Michael Field",
                "Brad Reinhold",
            ],
        },
        "html_only": True,
    },
    {
        "key": "21retro",
        "folders": [],
        "title": "2021 Retro Event (Premiere to Death Star II)",
        "year": "2021",
        "tag": "2021-05",
        "dates": "May 2021",
        "site": "GEMP",
        "format": "[[Premiere - Death Star II]]",
        "winner": "Bastian Winkelhaus",
        "lead": "'''2021 Retro Event''' (PDS2) was the Players Committee Premiere–Death Star II constructed event on GEMP, May 2021. [[Bastian Winkelhaus]] finished 1st in the published Top 8.",
        "pc": "https://www.starwarsccg.org/2021-retro-event-top-8-pds2/",
        "forum": "",
        "deck_prefix": "2021 Retro PDS2",
        "list_label": "Retro Event (Premiere to DSII)",
        "stages": [("t8", "Top 8", True)],
        "order": {
            "t8": [
                "Bastian Winkelhaus",
                "Hayes Hunter",
                "Justin Desai",
                "Joe Olson",
                "Andrew Bethell",
                "Miguel Tarin",
                "Koen Meijssen",
                "Kenneth Brennen",
            ]
        },
        "html_only": True,
    },
    {
        "key": "21mpc",
        "folders": ["2021-mpc", "2021-mpc-t4"],
        "title": "2021 Match Play Championship",
        "year": "2021",
        "tag": "2021-04",
        "dates": "23–25 April 2021",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2021 Match Play Championship''' was the Players Committee match-play championship on GEMP, 23–25 April 2021. [[Joe Olson]] finished 1st in the Final Four.",
        "pc": "https://www.starwarsccg.org/2021-match-play-championship/",
        "forum": "",
        "deck_prefix": "2021 MPC",
        "list_label": "Match Play Championship",
        "stages": [("t4", "Final Four", True), ("d1", "Day 1", False)],
        "order": {
            "t4": ["Joe Olson", "Jared Napolitano", "Chris Gogolen", "Chris Wirfs"],
        },
    },
    {
        "key": "20worlds",
        "folders": ["2020-worlds-d3", "2020-worlds-d2", "2020-worlds-d1"],
        "title": "2020 World Championship",
        "year": "2020",
        "tag": "2020-12",
        "dates": "5–6 and 12–13 December 2020",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Joe Olson",
        "lead": "'''2020 World Championship''' was the Players Committee World Championship on GEMP (Day 1 5–6 December, Day 2 12 December, Day 3 13 December 2020). [[Joe Olson]] defeated [[Quirin Fürgut]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2020-world-championships/",
        "forum": "https://www.starwarsccg.org/joe-olson-wins-the-25th-star-wars-ccg-world-championship/",
        "deck_prefix": "2020 Worlds",
        "list_label": "World Championship",
        "stages": [("d3", "Day 3", True), ("d2", "Day 2", True), ("d1", "Day 1", False)],
        "order": {
            "d3": [
                "Joe Olson",
                "Quirin Fürgut",
                "Paul Myers",
                "Chris Kelly",
                "Bastian Winkelhaus",
                "Jared Napolitano",
                "Justin Desai",
                "Fernando Castañón",
            ],
            "d2": [
                "Bastian Winkelhaus",
                "Joe Olson",
                "Jared Napolitano",
                "Justin Desai",
                "Quirin Fürgut",
                "Paul Myers",
                "Fernando Castañón",
                "Chris Kelly",
                "Steve Baroni",
                "Matthew Harrison-Trainor",
                "Greg Shaw",
                "Drew Lichtenstein",
                "Matt Lutz",
                "Charlie Arlandson",
                "Jarad Konsker",
                "James Martin",
                "Ryan Jellison",
                "Conor Britain",
                "Kyle Krueger",
                "Gavin Ortlund",
                "Brad Kippel",
                "Rikard Eriksen",
                "Adam Trunzo",
                "Ziemowit Skwara",
                "Tom Kelly",
                "Timo Dusel",
                "Brett Carlson",
                "Chris Wirfs",
                "Justin Miyashiro",
                "Matt Sokol",
                "Bill Kafer",
                "Aaron Kingery",
            ],
        },
    },
    {
        "key": "20ocs",
        "folders": [],
        "title": "2020 Online Championship Series Playoffs",
        "year": "2020",
        "tag": "2020-11",
        "dates": "October–November 2020",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Justin Desai",
        "lead": "'''2020 Online Championship Series Playoffs''' was the Players Committee OCS playoff on GEMP. [[Justin Desai]] defeated [[Paul Myers]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2022-online-championship-series-registration-opens/",
        "forum": "https://www.starwarsccg.org/major-event-winners/",
        "deck_prefix": "2020 OCS",
        "list_label": "Online Championship Series Playoffs",
        "stages": [("final", "Finals", True)],
        "order": {"final": ["Justin Desai", "Paul Myers"]},
        "stub_only": True,
    },
    {
        "key": "20tmw",
        "folders": [],
        "title": "2020 Texas Mini Worlds",
        "year": "2020",
        "tag": "2020-08",
        "dates": "August 2020",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Matthew Harrison-Trainor",
        "lead": "'''2020 Texas Mini Worlds''' was a Players Committee match-play major on GEMP. [[Matthew Harrison-Trainor]] defeated [[Greg Shaw]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2020-texas-mini-worlds/",
        "forum": "",
        "deck_prefix": "2020 TMW",
        "list_label": "Texas Mini Worlds",
        "stages": [("final", "Final Confrontation", True), ("t4", "Final 4", True), ("t8", "Round of 8", True), ("t16", "Round of 16", True), ("pod", "Pods", False)],
        "order": {
            "final": ["Matthew Harrison-Trainor", "Greg Shaw"],
            "t4": ["Greg Shaw", "Joe Olson", "Matthew Harrison-Trainor", "Mike Kessling"],
            "t8": [
                "Matt Lutz",
                "Greg Shaw",
                "Joe Olson",
                "Bill Kafer",
                "Justin Desai",
                "Matthew Harrison-Trainor",
                "Brad Kippel",
                "Mike Kessling",
            ],
            "t16": [
                "Matt Lutz",
                "David Woods",
                "Greg Shaw",
                "Jacy Smith",
                "Steve Baroni",
                "Joe Olson",
                "Bill Kafer",
                "Dan Tartaglione",
                "Justin Desai",
                "Jarad Konsker",
                "Matthew Harrison-Trainor",
                "Bastian Winkelhaus",
                "Edward Chien",
                "Brad Kippel",
                "Mike Kessling",
                "Erik Spijksma",
            ],
        },
        "html_only": True,
    },
    {
        "key": "20mpc",
        "folders": [],
        "title": "2020 Match Play Championship",
        "year": "2020",
        "tag": "2020-04",
        "dates": "April 2020",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Hayes Hunter",
        "lead": "'''2020 Match Play Championship''' was the Players Committee match-play championship on GEMP. [[Hayes Hunter]] finished 1st in the Final Four.",
        "pc": "https://www.starwarsccg.org/2020-match-play-championships/",
        "forum": "",
        "deck_prefix": "2020 MPC",
        "list_label": "Match Play Championship",
        "stages": [("t4", "Final Four", True), ("d1", "Day 1", False)],
        "order": {
            "t4": ["Hayes Hunter", "Jarad Konsker", "Kyle Krueger", "Matt Wadden"],
        },
        "html_only": True,
    },
    {
        "key": "20egp",
        "folders": [],
        "title": "2020 Endor Grand Prix",
        "year": "2020",
        "tag": "2020-01",
        "dates": "January 2020",
        "site": "Seattle, Washington",
        "format": "[[Open]]",
        "winner": "Hayes Hunter",
        "lead": "'''2020 Endor Grand Prix''' was a Players Committee major event in Seattle, Washington, January 2020 (the only in-person major of that year). [[Hayes Hunter]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2020-endor-grand-prix/",
        "forum": "",
        "deck_prefix": "2020 EGP",
        "list_label": "Endor Grand Prix",
        "stages": [("d2", "Day 2", True), ("d1", "Day 1", False)],
        "order": {
            "d2": [
                "Hayes Hunter",
                "Brian Fred",
                "Eric Hunter",
                "Conor Britain",
                "Bryan Mischke",
                "Bill Kafer",
                "Steve Harpster",
                "Dennis Reinhardt",
            ],
            "d1": [
                "Eric Hunter",
                "Conor Britain",
                "Hayes Hunter",
                "Brian Fred",
                "Bryan Mischke",
                "Bill Kafer",
                "Steve Harpster",
                "Dennis Reinhardt",
                "Joe Olson",
                "Scott Lingrell",
                "Phil Aasen",
                "Charlie Arlandson",
                "Kyle Krueger",
                "Chris Wirfs",
                "Justin Miyashiro",
                "Vikram Bali",
                "Matt Wadden",
                "Gosse Zeilstra",
                "Casey Anis",
                "Ryan Jellison",
                "Cal Aldred",
                "Elspeth Jellison",
                "Ryan Sersen",
                "Barry Alperstein",
                "Chris Westergard",
                "Lenny Rubin",
                "Jeremy DiPaolo",
                "Nate Davis",
                "Mike Kessling",
                "Paul Coggins",
                "Michael Erisman",
                "Brandon Baity",
                "Dan Tartaglione",
                "Brandon Romano",
                "Jacy Smith",
                "Edward Chien",
                "Joe Phillips",
                "Mike Turner",
                "Kyle Kallin",
                "David Beaubier",
                "Matt Smith",
            ],
        },
        "html_only": True,
    },
    {
        "key": "19outrider",
        "folders": [],
        "title": "2019 Outrider Cup",
        "year": "2019",
        "tag": "2019-12",
        "dates": "3 December 2019 – 20 January 2020",
        "site": "GEMP (teams)",
        "format": "[[Open]]",
        "winner": "[[Team USA]]",
        "lead": "'''2019 Outrider Cup''' was the inaugural Players Committee biennial Europe versus United States team event on GEMP, 3 December 2019 – 20 January 2020. Team USA defeated Team Europe 7–4.",
        "pc": "https://www.starwarsccg.org/2019-outrider-cup/",
        "forum": "",
        "deck_prefix": "2019 Outrider Cup",
        "list_label": "Outrider Cup",
        "stages": [("r1", "Round 1", True), ("r2", "Round 2", True)],
        "order": {
            "r1": [
                "Justin Branch",
                "Tom Damen",
                "Stephan de Vos",
                "Quirin Fürgut",
                "Emil Wallin",
                "Bastian Winkelhaus",
                "Justin Desai",
                "Chris Kelly",
                "Bryan Mischke",
                "Joe Olson",
                "Greg Shaw",
                "Chris Wirfs",
            ],
            "r2": [
                "Justin Branch",
                "Tom Damen",
                "Stephan de Vos",
                "Quirin Fürgut",
                "Emil Wallin",
                "Bastian Winkelhaus",
                "Justin Desai",
                "Chris Kelly",
                "Bryan Mischke",
                "Joe Olson",
                "Greg Shaw",
                "Chris Wirfs",
            ],
        },
        "html_only": True,
    },
    {
        "key": "19ocs",
        "folders": [],
        "title": "2019 Online Championship Series Playoffs",
        "year": "2019",
        "tag": "2019-11",
        "dates": "October–December 2019",
        "site": "GEMP",
        "format": "[[Open]]",
        "winner": "Bastian Winkelhaus",
        "lead": "'''2019 Online Championship Series Playoffs''' was the Players Committee OCS playoff on GEMP. [[Bastian Winkelhaus]] defeated [[Justin Branch]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2022-online-championship-series-registration-opens/",
        "forum": "https://www.starwarsccg.org/major-event-winners/",
        "deck_prefix": "2019 OCS",
        "list_label": "Online Championship Series Playoffs",
        "stages": [("final", "Finals", True)],
        "order": {"final": ["Bastian Winkelhaus", "Justin Branch"]},
        "stub_only": True,
    },
    {
        "key": "19worlds",
        "folders": [],
        "title": "2019 World Championship",
        "year": "2019",
        "tag": "2019-09",
        "dates": "20–22 September 2019",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Bastian Winkelhaus",
        "lead": "'''2019 World Championship''' was the Players Committee World Championship in Bochum, Germany, 20–22 September 2019. [[Bastian Winkelhaus]] defeated [[Bryan Mischke]] in the Final Confrontation.",
        "pc": "https://www.starwarsccg.org/2019-worlds/",
        "forum": "",
        "deck_prefix": "2019 Worlds",
        "list_label": "World Championship",
        "stages": [("d3", "Day 3", True), ("d2", "Day 2", True)],
        "order": {
            "d3": [
                "Bastian Winkelhaus",
                "Bryan Mischke",
                "Emil Wallin",
                "Joe Olson",
                "Justin Desai",
                "Hayes Hunter",
                "Steve Baroni",
                "Stephan de Vos",
            ],
            "d2": [
                "Bastian Winkelhaus",
                "Justin Desai",
                "Hayes Hunter",
                "Bryan Mischke",
                "Steve Baroni",
                "Stephan de Vos",
                "Joe Olson",
                "Emil Wallin",
                "Matt Carulli",
                "Quirin Fürgut",
                "Greg Shaw",
                "Tom Kelly",
                "Angelo Consoli",
                "Chris Gogolen",
                "Tom Haid",
                "Casey Anis",
                "Mike Kessling",
                "Charlie Arlandson",
                "Marc Nickels",
                "Koen Meijssen",
                "Dennis Reinhardt",
                "Justin Carulli",
                "Brian Fred",
                "David Destefanis",
                "Justin Branch",
                "Paul McPherson",
                "Cedrik Vanderhaegen",
                "Floris de Vries",
                "Chris Westergard",
                "Marvin Tegeler",
                "Gunnar Brandén",
                "Rikard Eriksen",
                "Piotr Ptak",
                "Kyle Krueger",
                "Erik Spijksma",
                "Nico Johannes Kreidl",
                "Jonas Hagen Nørregaard",
                "Lukasz Saczek",
                "Kristian Lund",
                "Darren Malins",
                "Patrik Csapi",
                "Jacy Smith",
                "Dennis Schwarz",
                "Tom Damen",
                "Moritz Karge",
                "John Moorley",
                "Robert Smolarek",
                "Casper Jørgensen",
                "Rasmus Juul",
                "Kristoffer Basse Hedlund",
                "Kevin Jaap",
                "John Veasey",
                "Jon Benkert Holtet",
                "György Póra",
                "Jan Berueda",
                "Ulli Reuter",
                "Peter Jacobson",
                "Martin den Boef",
                "Piotr Jarnot",
                "Jan Westergard",
                "Julian Smolarek",
                "Nelson Cazon",
                "Julian Cochard",
                "Ralf W.",
                "Kent Larsen",
                "Peter Rowlands",
                "Horst Draudt",
                "Mike Klarenbeek",
                "Stefan Boersma",
            ],
        },
        "html_only": True,
    },
    {
        "key": "19nac",
        "folders": [],
        "title": "2019 North American Continental Championship",
        "year": "2019",
        "tag": "2019-08",
        "dates": "August 2019",
        "site": "United States",
        "format": "[[Open]]",
        "winner": "Greg Shaw",
        "lead": "'''2019 North American Continental Championship''' (John Anderson Memorial) was the Players Committee North American Continental Championship, August 2019. [[Greg Shaw]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2019-north-american-continentals/",
        "forum": "",
        "deck_prefix": "2019 NAC",
        "list_label": "North American Continental Championship",
        "stages": [("d2", "Day 2", True), ("d1", "Day 1", False)],
        "order": {
            "d2": [
                "Greg Shaw",
                "Joe Olson",
                "Chris Wirfs",
                "Bryan Mischke",
                "Tom Haid",
                "Reid Smith",
                "Adam Trunzo",
                "Matt Scott",
            ],
            "d1": [
                "Joe Olson",
                "Tom Haid",
                "Chris Wirfs",
                "Bryan Mischke",
                "Reid Smith",
                "Greg Shaw",
                "Adam Trunzo",
                "Matt Scott",
                "Charlie Arlandson",
                "Phil Aasen",
                "Zach Stenerson",
                "Chris Gogolen",
                "Andrew Moss",
                "Chris Kelly",
                "Ryan Jellison",
                "Brian Fred",
                "Ming Huo",
                "Bill Kafer",
                "Dennis Reinhardt",
                "Justin Carulli",
                "Sam Olson",
                "Vikram Bali",
                "Brandon Baity",
                "Sam Tashima",
                "Mitch Nieland",
                "Mike Pistone",
                "Barry Alperstein",
                "Mark Walseth",
                "Cal Aldred",
                "Brian Herold",
                "Ryan Sersen",
                "Kendall Halman",
                "Lenny Rubin",
                "Tom Marlin",
                "Sean Miller",
                "Mike Turner",
                "Justin Miyashiro",
                "Adam Schellberg",
                "Jason Riendeau",
                "Mike Richards",
                "Greg Nirshberg",
                "Matt Wadden",
                "Jan Westergard",
                "AJ Hatoum",
                "Chris Angulo",
                "Jan Berueda",
                "Nate Louderback",
                "Matt Thornton",
                "Patrick Johnson",
                "Max DeWitt",
                "Logan Pietig",
                "Danny Lamar",
                "Thang Le",
                "Brandon Nguyen",
                "Jim Li",
                "John Veasey",
                "Mike Kessling",
                "Gabriel Angulo",
                "Kyle Kallin",
                "Jerry Hsiao",
                "Austin Jacobus",
            ],
        },
        "html_only": True,
    },
    {
        "key": "19euro",
        "folders": [],
        "title": "2019 European Championship",
        "year": "2019",
        "tag": "2019-07",
        "dates": "12–14 July 2019",
        "site": "Bochum, Germany",
        "format": "[[Open]]",
        "winner": "Bastian Winkelhaus",
        "lead": "'''2019 European Championship''' was the Players Committee European Championship at Zu Den Vier Winden in Bochum, Germany, 12–14 July 2019. [[Bastian Winkelhaus]] defeated [[Emil Wallin]] in Day 3.",
        "pc": "https://www.starwarsccg.org/2019-european-championships/",
        "forum": "https://www.starwarsccg.org/resources/tournament-decklists/",
        "deck_prefix": "2019 European Championship",
        "list_label": "European Championship",
        "stages": [("d3", "Day 3", True), ("d2", "Day 2", True)],
        "order": {
            "d3": [
                "Bastian Winkelhaus",
                "Emil Wallin",
                "Koen Meijssen",
                "Tom Damen",
                "Chris Menzel",
                "Quirin Fürgut",
                "Paul McPherson",
                "Kevin Jaap",
            ]
        },
        "html_only": True,
        "ls_first": True,
    },
    {
        "key": "19mpc",
        "folders": [],
        "title": "2019 Match Play Championship",
        "year": "2019",
        "tag": "2019-04",
        "dates": "April 2019",
        "site": "United States",
        "format": "[[Open]]",
        "winner": "Chris Kelly",
        "lead": "'''2019 Match Play Championship''' was the Players Committee match-play championship, April 2019. [[Chris Kelly]] finished 1st in the Final Four.",
        "pc": "https://www.starwarsccg.org/2019-match-play-championships/",
        "forum": "",
        "deck_prefix": "2019 MPC",
        "list_label": "Match Play Championship",
        "stages": [("t4", "Final Four", True), ("d1", "Day 1", False)],
        "order": {
            "t4": ["Chris Kelly", "Tom Kelly", "Brian Fred", "Chris Gogolen"],
        },
        "html_only": True,
    },
    {
        "key": "19egp",
        "folders": [],
        "title": "2019 Endor Grand Prix",
        "year": "2019",
        "tag": "2019-01",
        "dates": "January 2019",
        "site": "United States",
        "format": "[[Open]]",
        "winner": "Jonny Chu",
        "lead": "'''2019 Endor Grand Prix''' was a Players Committee major event, January 2019. [[Jonny Chu]] finished 1st in Day 2.",
        "pc": "https://www.starwarsccg.org/2019-endor-grand-prix/",
        "forum": "",
        "deck_prefix": "2019 EGP",
        "list_label": "Endor Grand Prix",
        "stages": [("d2", "Day 2", True), ("d1", "Day 1", False)],
        "order": {
            "d2": [
                "Jonny Chu",
                "Steve Harpster",
                "Matt Wadden",
                "Brian Fred",
                "Matt Sokol",
                "Joe Olson",
                "Ryan Sersen",
                "Phil Aasen",
            ],
            "d1": [
                "Matt Sokol",
                "Joe Olson",
                "Matt Wadden",
                "Steve Harpster",
                "Jonny Chu",
                "Ryan Sersen",
                "Brian Fred",
                "Phil Aasen",
                "Bryan Mischke",
                "Ryan Jellison",
                "Lenny Rubin",
                "Kyle Krueger",
                "Dennis Reinhardt",
                "Jacy Smith",
                "Charlie Arlandson",
                "Clayton Atkin",
                "Joe Phillips",
                "Chris Wirfs",
                "Barry Alperstein",
                "Stephen Morgan",
                "Mitch Nieland",
                "Camden Yanaga",
                "Jan Berueda",
                "Brandon Baity",
                "Vikram Bali",
                "Kyle Kallin",
                "Cal Aldred",
                "Michael Erisman",
            ],
        },
        "html_only": True,
    },
]

BY_KEY = {e["key"]: e for e in EVENTS}

REGIONS_2021 = [
    ("Bespin", "21 August 2021", "Charlie Arlandson"),
    ("Endor", "4 September 2021", "Joe Olson"),
    ("Yavin 4", "4 September 2021", "Patrick Johnson"),
    ("Tatooine", "11 September 2021", "Justin Miyashiro"),
    ("Coruscant", "19 September 2021", "Matt Wadden"),
    ("Dagobah", "25 September 2021", "Brad Reinhold"),
    ("Corellia", "25 September 2021", "Matt Carulli"),
    ("Alderaan", "4 December 2021", "Anthony Howard"),
    ("Nal Hutta", "4 December 2021", "Kendall Halman"),
]

STAGE_LABEL = {
    "final": "Finals",
    "t4": "Final Four",
    "qf": "Quarterfinals",
    "sf": "Semifinals",
    "t16": "Round of 16",
    "t8": "Top 8",
    "d3": "Day 3",
    "d2": "Day 2",
    "d1": "Day 1",
    "r1": "Round 1",
    "r2": "Round 2",
    "pod": "Pods",
    "eur": "Team Europe",
    "usa": "Team USA",
    "tb": "Tiebreaker",
}

HTML_PREFIXES = [
    ("2021-worlds-day-2-top-8-", "21worlds", "d2"),
    ("2021-worlds-day-2-", "21worlds", "d2"),
    ("2021-worlds-retro-prem-ref-ii-", "21throwback", "t8"),
    ("2021-worlds-throwback-", "21throwback", "t8"),
    ("2021-worlds-", "21worlds", "d1"),
    ("2021-outrider-cup-tiebreaker-", "21outrider", "tb"),
    ("2021-outrider-cup-eur-", "21outrider", "eur"),
    ("2021-outrider-cup-usa-", "21outrider", "usa"),
    ("2021-outrider-cup-", "21outrider", "t8"),
    ("2021-match-play-championship-day-1-top-4-", "21mpc", "t4"),
    ("2021-match-play-championship-top-4-", "21mpc", "t4"),
    ("2021-match-play-championship-final-four-", "21mpc", "t4"),
    ("2021-match-play-championship-day-1-", "21mpc", "d1"),
    ("2021-mpc-day-1-", "21mpc", "d1"),
    ("2021-us-nationals-day-2-", "21nats", "d2"),
    ("2021-us-nationals-", "21nats", "d1"),
    ("2021-07-us-nationals-", "21nats", "d1"),
    ("2021-retro-event-pds2-", "21retro", "t8"),
    ("2021-retro-event-", "21retro", "t8"),
    ("2021-05-retro-event-", "21retro", "t8"),
    ("2021-jawa-cup-finals-", "21jawa", "final"),
    ("2021-jawa-cup-final-confrontation-", "21jawa", "final"),
    ("2021-jawa-cup-semifinals-", "21jawa", "sf"),
    ("2021-jawa-cup-quarterfinals-", "21jawa", "qf"),
    ("2021-jawa-cup-top-8-", "21jawa", "qf"),
    ("2021-jawa-cup-", "21jawa", "qf"),
    ("2020-worlds-day-3-", "20worlds", "d3"),
    ("2020-worlds-day-2-", "20worlds", "d2"),
    ("2020-worlds-day-1-", "20worlds", "d1"),
    ("2020-texas-mini-worlds-", "20tmw", "pod"),
    ("2020-tmw-sweet-16-", "20tmw", "t16"),
    ("2020-tmw-round-of-16-", "20tmw", "t16"),
    ("2020-tmw-round-of-8-", "20tmw", "t8"),
    ("2020-tmw-elite-8-", "20tmw", "t8"),
    ("2020-tmw-matthew-harrison-trainor-final-confrontation-", "20tmw", "final"),
    ("2020-tmw-greg-shaw-final-confrontation-", "20tmw", "final"),
    ("2020-tmw-matthew-harrison-trainor-final-four-", "20tmw", "t4"),
    ("2020-tmw-mike-kessling-final-four-", "20tmw", "t4"),
    ("2020-tmw-greg-shaw-final-four-", "20tmw", "t4"),
    ("2020-tmw-joe-olson-final-four-", "20tmw", "t4"),
    ("2020-tmw-final-4-", "20tmw", "t4"),
    ("2020-tmw-final-confrontation-", "20tmw", "final"),
    ("2020-tmw-", "20tmw", "pod"),
    ("2020-mpc-top-4-", "20mpc", "t4"),
    ("2020-mpc-day-1-", "20mpc", "d1"),
    ("2020-match-play-championships-top-4-", "20mpc", "t4"),
    ("2020-match-play-championships-", "20mpc", "d1"),
    ("2020-egp-day-2-", "20egp", "d2"),
    ("2020-egp-day-1-", "20egp", "d1"),
    ("2020-egp-", "20egp", "d1"),
    ("2020-day-1-", "20mpc", "d1"),
    ("2020-endor-grand-prix-day-2-", "20egp", "d2"),
    ("2020-endor-grand-prix-day-1-", "20egp", "d1"),
    ("2019-worlds-", "19worlds", "d2"),
    ("2019-nac-", "19nac", "d1"),
    ("2019-north-american-continentals-", "19nac", "d1"),
    ("2019-outrider-cup-round-2-", "19outrider", "r2"),
    ("2019-outrider-cup-round-1-", "19outrider", "r1"),
    ("2019-outrider-cup-", "19outrider", "r1"),
    ("2019-worlds-day-3-", "19worlds", "d3"),
    ("2019-worlds-day-2-", "19worlds", "d2"),
    ("2019-north-american-continentals-day-2-", "19nac", "d2"),
    ("2019-north-american-continentals-day-1-", "19nac", "d1"),
    ("2019-nac-day-2-", "19nac", "d2"),
    ("2019-nac-day-1-", "19nac", "d1"),
    ("2019-ec-day-3-", "19euro", "d3"),
    ("2019-ec-day-2-", "19euro", "d2"),
    ("2019-european-championships-day-3-", "19euro", "d3"),
    ("2019-european-championships-day-2-", "19euro", "d2"),
    ("2019-ec-", "19euro", "d2"),
    ("2019-mpc-day-2-", "19mpc", "t4"),
    ("2019-mpc-day-1-", "19mpc", "d1"),
    ("2019-match-play-championships-", "19mpc", "d1"),
    ("2019-endor-grand-prix-day-2-", "19egp", "d2"),
    ("2019-endor-grand-prix-day-1-", "19egp", "d1"),
]
HTML_PREFIXES.sort(key=lambda x: len(x[0]), reverse=True)

OBJ_SLUGS = sorted(
    {
        re.sub(r"[^a-z0-9]+", "-", k.lower()).strip("-")
        for k in list(hm.SLANG_HUB.keys())
        + [
            "hunt-down",
            "hunt-down-v",
            "hunt-down-dueling",
            "hunt-down-racing",
            "hidden-base",
            "hitco",
            "ie",
            "oa",
            "invasion",
            "map",
            "trm",
            "combat",
            "dark-combat",
            "wys",
            "bhbm",
            "y4ops",
            "y4o",
            "yavin-4-ops",
            "yavin-4-base-ops",
            "tdigwatt",
            "ebo",
            "isb",
            "endor-ops",
            "eops",
            "hoth-cpv",
            "hoth-crv",
            "hoth-clones",
            "profit",
            "diplo",
            "rops",
            "rops-v",
            "ropsv",
            "ropsv-mains",
            "sycfa",
            "syfca",
            "aobs",
            "aobs-racing",
            "watto",
            "tigih",
            "court",
            "qmc",
            "tatooine-cr-v",
            "tatooine-cp-v",
            "tatooine-cpv",
            "tatooine-crv",
            "hyperdrive",
            "hyperdrive-v",
            "old-allies",
            "tto",
            "rst",
            "cct",
            "cct-flip",
            "cct-ig",
            "first-order-ropsv",
            "hb-mon-cals",
            "no-idea",
            "legend",
            "whap",
            "shadow-collective",
            "ltww-mains",
            "ls-senate",
            "ds-senate",
            "senate",
            "sc",
            "hd",
            "asm",
            "mkos",
            "mwyhl",
            "harvest-sense-alter-control",
            "communing-yoda",
            "communing-obi-wan",
            "communing-qui-gon",
            "rtpv",
            "jakku-cpv",
            "mustafar-crv",
            "a-stunning-move",
            "ralltiir-operations-v",
            "mauls-chambers-ssav",
            "emperors-orders-exe-ctrl-station-v-ssa",
            "dsii-throne-room-ssav",
            "sycfa-tractor-beams",
            "sycfa-brangus",
            "dathomir-mauls-chambers-ssav",
            "bespin-crv",
            "qui-communing",
            "rescue-the-princess-v",
            "ltww-space",
            "cct-musicians",
            "verge-of-greatness",
            "hoth-clones",
            "yavin-4-base-ops",
            "cct-ig",
            "cct-mains",
            "ropsv-mains",
            "chief-chirpa-mains",
            "chief-chirpas-hut-mains",
            "chief-chirpas-hut",
            "hyper-profit",
            "desert-landing-site-ssav",
            "dagobah-cave-ssav",
            "ds-senate",
            "12-card-death-star",
            "mauls-chambers-ssa",
            "ltww-cch",
            "hoth-cr-v",
            "naboo-gungans",
            "first-order-rops-v",
            "first-order-rops",
            "cotvg",
            "coruscant-crv-tanks",
            "combat-7s",
            "trm-hdwgitm",
            "invisible-hand-ssa-v",
            "invisible-hand-ssa",
            "dagobah-cave-ssa-v",
            "dsii-throne-room-ssav",
            "dsiithrone-room-ssav",
            "ds2-throne-room-ssa",
            "hidden-base-mains",
            "endor-cp-v",
            "ls-combat",
            "dark-combat",
            "coruscant-cr-v",
            "coruscant-crv",
            "5th-marker-v-ssav",
            "5th-marker-v-ssa-v",
            "5th-marker-v-ssa",
            "senate-gungans",
            "jcc-mains",
            "endor-cpv",
            "endor-ops",
            "ih-bridge-ssav",
            "cave-ssav",
            "hidden-base-quads",
            "ds2-throne-room-atmd",
            "first-order-ropsv",
            "hoth-mains",
            "hoth-cpv",
            "ls-senate",
            "tigih-speeders",
            "sycfa-brangus",
            "ltwwv-mains",
            "ltwwv-dwell",
            "mwyhl",
            "trm",
        ]
    },
    key=len,
    reverse=True,
)

NATS_FILES = {
    "7-21 open No Idea day 1 Joe.txt": ("Joe Olson", False, "LS", "No Idea", "d1"),
    "7-21 open Old Allies Kessling day1.txt": ("Mike Kessling", False, "LS", "Old Allies", "d1"),
    "7-23 Map open Charlie day 1.txt": ("Charlie Arlandson", False, "DS", "Map", "d1"),
    "7-24 Joe Day 1 BHBM.txt": ("Joe Olson", False, "DS", "BHBM", "d1"),
    "7_23 Open DEAL Joe day 2.txt": ("Joe Olson", True, "DS", "TDIGWATT", "d2"),
}

WRAP_FILE = {
    "19egp": "19egp.html",
    "19mpc": "19mpc.html",
    "19euro": "19euro.html",
    "19nac": "19nac.html",
    "19worlds": "19worlds.html",
    "19outrider": "19outrider.html",
    "20egp": "20egp.html",
    "20mpc": "20mpc.html",
    "20tmw": "20texas.html",
    "20worlds": "20worlds.html",
    "21mpc": "21mpc.html",
    "21nats": "21nats.html",
    "21regionals": "21regionals.html",
    "21throwback": "21throwback.html",
    "21worlds": "21worlds.html",
    "21jawa": "2021-jawa-cup-top-8.html",
    "21outrider": "outrider-cup-ii.html",
    "21retro": "2021-retro-event-top-8-pds2.html",
    "21ocs": "21ocs.html",
}

HEAD_STAGE = [
    (re.compile(r"(?i)^day\s*2\s*final four"), "t4"),
    (re.compile(r"(?i)^final confrontation"), "final"),
    (re.compile(r"(?i)^semifinals?"), "sf"),
    (re.compile(r"(?i)^quarterfinals?"), "qf"),
    (re.compile(r"(?i)^final four|^final 4"), "t4"),
    (re.compile(r"(?i)^round of 16"), "t16"),
    (re.compile(r"(?i)^round of 8"), "t8"),
    (re.compile(r"(?i)^round 1"), "r1"),
    (re.compile(r"(?i)^round 2"), "r2"),
    (re.compile(r"(?i)^day\s*3|^day 3"), "d3"),
    (re.compile(r"(?i)^day\s*2|^day 2"), "d2"),
    (re.compile(r"(?i)^day\s*1|^day 1|^heat\s*[1-4]"), "d1"),
    (re.compile(r"(?i)^pod\s*[a-h]|^pods?$|^pod results|^matchplay"), "pod"),
    (re.compile(r"(?i)^team europe"), "eur"),
    (re.compile(r"(?i)^team usa"), "usa"),
    (re.compile(r"(?i)^tiebreaker"), "tb"),
    (re.compile(r"(?i)^bespin\b"), "Bespin"),
    (re.compile(r"(?i)^endor\b"), "Endor"),
    (re.compile(r"(?i)^yavin\s*4\b"), "Yavin 4"),
    (re.compile(r"(?i)^tatooine\b"), "Tatooine"),
    (re.compile(r"(?i)^coruscant\b"), "Coruscant"),
    (re.compile(r"(?i)^dagobah\b"), "Dagobah"),
    (re.compile(r"(?i)^corellia\b"), "Corellia"),
    (re.compile(r"(?i)^alderaan\b"), "Alderaan"),
    (re.compile(r"(?i)^nal hutta\b"), "Nal Hutta"),
]


def refs():
    return """{{#if:1|<nowiki />
<h2>References</h2>
<references />}}"""


def safe_title(s: str) -> str:
    return re.sub(r'[#<>\[\]\|\{\}?*"]', "", s).replace("  ", " ").strip()


def deck_title(meta, player, side, obj, stage):
    pfx = meta["deck_prefix"]
    lab = STAGE_LABEL.get(stage, "")
    if lab in ("Day 1", "constructed", ""):
        st = ""
    else:
        st = lab + " "
    obj = re.sub(r"[#<>\[\]\|\{\}]", "", obj or "")
    return safe_title(f"{pfx} {st}{player} {side} {obj}")


def ordered(found, preferred):
    """Preferred first even when wrap/HTML missed a name, then extras."""
    seen = []
    for p in preferred or []:
        if p not in seen:
            seen.append(p)
    for p in found:
        if p not in seen:
            seen.append(p)
    return seen


def cell(dt, hl, player, stage, side):
    page = dt.get((player, stage, side))
    if not page:
        page = dt.get((player, "t8" if stage in ("d2", "d3", "t4", "final") else stage, side))
    if not page:
        return "—"
    return f"[[{page}|{hl.get(page, page)}]]"


def people_table(heading, players, dt, hl, stage, order_list=None):
    bits = ['{| class="wikitable sortable"', f"! {heading} !! Player !! Dark !! Light"]
    for i, p in enumerate(players, 1):
        if order_list and p in order_list:
            fin = str(order_list.index(p) + 1)
        elif order_list:
            fin = "—"
        else:
            fin = "—"
        bits += [
            "|-",
            f"| {fin} || [[{p}]] || {cell(dt, hl, p, stage, 'DS')} || {cell(dt, hl, p, stage, 'LS')}",
        ]
    bits.append("|}")
    return "\n".join(bits)


def is_bio(text: str) -> bool:
    if "== Interviews ==" in text or "fan encyclopedia" in text.lower():
        return True
    if "Documented PC roles" in text:
        return True
    return "[[Category:People]]" in text and len(text) > 2500


def write_hub(meta, dt, hl, by_stage, order=None):
    secs = []
    order = order or {}
    for stage, heading, _t8 in meta.get("stages") or []:
        players = by_stage.get(stage) or []
        if not players:
            continue
        tbl = people_table(heading, players, dt, hl, stage, order.get(stage))
        note = ""
        if heading == "Day 1":
            note = "Published constructed lists (every published pair, not Top 8 only).\n\n"
        secs.append(f"== {heading} ==\n\n{note}{tbl}\n")
    if meta.get("regional"):
        bits = ["== Sites ==\n"]
        bits.append('{| class="wikitable sortable"')
        bits.append("! Planet !! Date !! Winner")
        for planet, dt_s, winner in REGIONS_2021:
            bits += ["|-", f"| {planet} || {dt_s} || [[{winner}]]"]
        bits.append("|}\n")
        secs.append("\n".join(bits))
        # per-planet tables filled from dt keys that use planet as stage
        for planet, dt_s, winner in REGIONS_2021:
            players = by_stage.get(planet) or []
            if not players:
                continue
            tbl = people_table("Finish", players, dt, hl, planet, order.get(planet))
            secs.append(f"== {planet} ==\n\n{dt_s}. Winner: [[{winner}]].\n\n{tbl}\n")
    body_sec = "\n".join(secs)
    if not body_sec:
        body_sec = "== Results ==\n\nStandings as published on the PC results page.\n"
    fmt_env = meta["format"]
    forum_line = f"* '''GEMP importable decks:''' [{meta['forum']} forum]\n" if meta.get("forum") else ""
    body = f"""{meta["lead"]}<ref name="pc">{meta["pc"]}</ref>

== Format ==

* '''Environment:''' {fmt_env}
* '''Site:''' {meta["site"]}
* '''Dates:''' {meta["dates"]}
{forum_line}
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
    for year in ("2021", "2020", "2019"):
        rows = year_rows.get(year) or []
        if not rows:
            continue
        section = f"""== {year} ==

{{| class="wikitable sortable"
|-
! Tag !! Event !! Dates !! Site !! Format !! Winner
{chr(10).join(rows)}
|}}

"""
        if f"== {year} ==" in text:
            text = re.sub(
                rf"== {year} ==.*?(?=\n== )",
                section,
                text,
                count=1,
                flags=re.S,
            )
        else:
            text = text.replace(
                "== Decipher World Championships ==",
                section + "== Decipher World Championships ==",
                1,
            )
        if f"[[Category:{year}]]" not in text:
            text = text.replace("[[Category:2022]]", f"[[Category:2022]]\n[[Category:{year}]]")
    LIST.write_text(text, encoding="utf-8", newline="\n")
    if EC.exists():
        et = EC.read_text(encoding="utf-8")
        et = et.replace(
            "| 2019 || 2019 European Championships || Bochum, Germany || — || [[Emil Wallin]]",
            "| 2019 || [[2019 European Championship]] || Bochum, Germany || [[Open]] || [[Bastian Winkelhaus]]",
        )
        et = et.replace(
            "| 2019 || [[2019 European Championship]] || Bochum, Germany || [[Open]] || [[Emil Wallin]]",
            "| 2019 || [[2019 European Championship]] || Bochum, Germany || [[Open]] || [[Bastian Winkelhaus]]",
        )
        EC.write_text(et, encoding="utf-8", newline="\n")


def slug_url(url: str) -> str:
    s = url.rstrip("/").split("/")[-1]
    s = re.sub(r"[^a-zA-Z0-9._-]+", "-", s)
    return s[:180] + ".html"


EXTRA_SLANG = {
    "chief chirpas hut mains": "Let The Wookiee Win (V)",
    "chief chirpas hut": "Let The Wookiee Win (V)",
    "chief chirpa mains": "Let The Wookiee Win (V)",
    "hunt down dueling": "Hunt Down And Destroy The Jedi",
    "hunt down racing": "Hunt Down And Destroy The Jedi",
    "endor ops": "Endor Operations",
    "endor cpv": "Combat Preparedness (V)",
    "endor cp v": "Combat Preparedness (V)",
    "senate gungans": "Plead My Case To The Senate",
    "jcc mains": "Watch Your Step",
    "5th marker v ssa v": "Set Your Course For Alderaan",
    "5th marker v ssa": "Set Your Course For Alderaan",
    "5th marker v ssav": "Set Your Course For Alderaan",
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
    "dagobah cave ssa v": "Set Your Course For Alderaan",
    "endor chief chirpas hut ltww": "Let The Wookiee Win (V)",
    "syfca": "Set Your Course For Alderaan",
    "ds2 throne room ssa": "Set Your Course For Alderaan",
    "dsiithrone room ssav": "Set Your Course For Alderaan",
    "dsii throne room ssav": "Set Your Course For Alderaan",
    "dsii-throne-room-ssav": "Set Your Course For Alderaan",
}

JUNK_PLAYERS = {
    "top 8",
    "top 4",
    "final four",
    "finals four",
    "four",
    "day 1",
    "day 2",
    "day 3",
    "pods",
    "pod",
    "finish",
    "results",
    "scroll to top",
    "elite 8",
    "sweet 16",
    "round of 8",
    "round of 16",
    "matchplay",
    "n/a",
}


def is_junk_player(name: str) -> bool:
    n = re.sub(r"\s+", " ", name or "").strip().lower()
    if not n or n in JUNK_PLAYERS:
        return True
    if n.startswith(("elite 8 ", "sweet 16 ", "scroll ")):
        return True
    return False


def slang_obj(slug: str) -> str:
    slug = re.sub(r"-\d+$", "", slug or "")
    raw = hm.pretty_obj(slug)
    for key in (
        raw.lower(),
        re.sub(r"\s+", " ", raw.lower().replace("(v)", "(V)")),
        slug.lower().replace("-", " "),
        slug.lower(),
    ):
        if key in EXTRA_SLANG:
            return EXTRA_SLANG[key]
        if key in hm.SLANG_HUB:
            return hm.SLANG_HUB[key]
    return raw


def peel_obj(rest: str):
    rest = rest.strip("-")
    if not rest:
        return "", ""
    for slug in OBJ_SLUGS:
        if rest == slug:
            return "", slug
        if rest.endswith("-" + slug):
            return rest[: -(len(slug) + 1)], slug
    parts = rest.split("-")
    if len(parts) >= 2:
        return "-".join(parts[:-1]), parts[-1]
    return rest, ""


def wrap_visible(path: Path) -> str:
    raw = path.read_text(encoding="utf-8", errors="replace")
    m = re.search(r"<h1[^>]*>.*?</h1>([\s\S]+?)Posted in", raw, re.I)
    if not m:
        m = re.search(r"<h1[^>]*>.*?</h1>([\s\S]{0,25000})", raw, re.I)
    s = m.group(1) if m else raw
    s = re.sub(r"<script[\s\S]*?</script>", " ", s, flags=re.I)
    s = re.sub(r"<style[\s\S]*?</style>", " ", s, flags=re.I)
    s = re.sub(r"<br\s*/?>", "\n", s, flags=re.I)
    s = re.sub(r"</p>", "\n", s, flags=re.I)
    s = re.sub(r"</h[1-6]>", "\n", s, flags=re.I)
    s = re.sub(r"<[^>]+>", " ", s)
    s = htmlmod.unescape(s)
    s = re.sub(r"[ \t]+", " ", s)
    lines = [ln.strip() for ln in s.splitlines() if ln.strip()]
    return "\n".join(ln for ln in lines if not ln.startswith("{") and "function" not in ln[:18])


def heading_stage(line: str) -> str | None:
    t = re.sub(r"[–—:].*$", "", line).strip()
    t = re.sub(r"^\d+\.?\s*", "", t)
    for rx, stage in HEAD_STAGE:
        if rx.match(t):
            return stage
    return None


def split_glued_names(line: str) -> list[str]:
    names = sorted({v for v in TOKEN.values() if " " in v}, key=len, reverse=True)
    pat = "(" + "|".join(re.escape(n) for n in names) + ")"
    bits = re.split(pat, line)
    out = []
    i = 0
    while i < len(bits):
        if bits[i] in TOKEN.values() or bits[i] in names:
            out.append(canon(bits[i]))
        i += 1
    return out


def player_from_line(line: str) -> str | None:
    line = re.sub(r"^\s*(?:\d{1,2}|T-#\d+)[\.\)]?\s+", "", line)
    m = re.match(r"^([A-Za-z][A-Za-z .'\-]+?)\s+[–—-]\s+", line)
    if m:
        p = canon(m.group(1).strip())
        return None if is_junk_player(p) else p
    m = re.match(r"^([A-Z][a-z]+(?:\s+[A-Z][a-z]+)+)\s*$", line)
    if m:
        p = canon(m.group(1))
        return None if is_junk_player(p) else p
    return None


def orders_from_wraps() -> dict:
    found = defaultdict(lambda: defaultdict(list))
    for key, fname in WRAP_FILE.items():
        path = WRAP / fname
        if not path.exists():
            continue
        stage = None
        for ln in wrap_visible(path).splitlines():
            hs = heading_stage(ln)
            if hs:
                stage = hs
                continue
            if not stage:
                continue
            if " – " in ln or " — " in ln or " - " in ln:
                glued = split_glued_names(ln)
                if len(glued) >= 3:
                    for p in glued:
                        if is_junk_player(p):
                            continue
                        if p not in found[key][stage]:
                            found[key][stage].append(p)
                    continue
                p = player_from_line(ln)
                if p and p not in found[key][stage]:
                    found[key][stage].append(p)
            else:
                p = player_from_line(ln)
                if p and p not in found[key][stage]:
                    found[key][stage].append(p)
    return found


def tidy_player_name(name: str) -> str:
    name = re.sub(r"\s+day\s*[123]\s*$", "", name or "", flags=re.I)
    name = re.sub(r"\s+\d+(st|nd|rd|th) marker.*$", "", name, flags=re.I)
    return canon(name.strip())


def polish_side_obj(side: str | None, obj: str | None) -> tuple[str | None, str | None]:
    if not obj:
        return side, obj
    if obj[:1].isupper() and " " in obj:
        mapped = obj
    else:
        mapped = slang_obj(obj) or obj
    ol = mapped.lower()
    if side == "DS" and ("plead my case" in ol or ol in ("senate", "ls senate")):
        mapped = "Senate Occupied"
    elif side == "LS" and ol in ("senate occupied", "ds senate", "senate"):
        mapped = "Plead My Case To The Senate"
    guessed = side_from_obj(mapped) or side_from_obj(obj)
    if side is None:
        side = guessed
    return side, mapped


def hub_obj_from_cards(cards, bp, dests, title_map, by_title, fallback, side):
    """Printed Objective (0-side) for dest titles and hub cells; slang only as fallback."""
    _td, obj, ints, _effs, loc_title, _note, _ltww = ug.analyze(cards, bp, dests, title_map)
    if not obj:
        for cid, title, tag in cards:
            if tag != "card":
                continue
            rec = (bp.get(cid) if cid else None) or {}
            cat = (rec.get("cardCategory") or "").upper()
            if not cat:
                rec2 = by_title.get((title or "").lower()) or {}
                cat = (rec2.get("cat") or "").upper()
            if cat == "OBJECTIVE":
                dest = ug.dest_for_card(title, cid, bp, dests, title_map) if cid else None
                obj = (title, cid, dest)
                break
    if obj:
        dest = obj[2] or ""
        title = obj[0] or ""
        src = dest if dest else title
        label = src.split(" / ")[0].split("/")[0].strip()
        if dest and ug.dest_has_v(dest) and not label.endswith(" (V)"):
            label += " (V)"
        elif not dest:
            label = ug.visible_label(title.split("/")[0].strip(), dest)
        return label
    strat = [t for t, _c, _d in ints if t not in ug.GENERIC_START]
    if strat:
        t = strat[0]
        d = next(d for x, _c, d in ints if x == t)
        return ug.visible_label(t, d)
    if loc_title:
        return loc_title
    for _cid, title, tag in cards:
        if tag == "card" and title == "Yavin 4: Massassi Throne Room":
            return title
    _side, mapped = polish_side_obj(side, fallback)
    mapped = mapped or fallback or ""
    if not mapped or mapped.lower() == "constructed" or mapped[:1].islower():
        mapped = slang_obj(mapped) or mapped
    return mapped


def side_from_cards(cards, by_id, by_title) -> str | None:
    votes = Counter()
    obj_side = None
    for cid, title, tag in cards:
        if tag != "card":
            continue
        rec = (by_id.get(str(cid)) if cid else None) or by_title.get((title or "").lower()) or {}
        cat = (rec.get("cat") or "").upper().replace(" ", "_")
        side = (rec.get("side") or "").upper()
        if cat in ("DEFENSIVE_SHIELD", "DEFENSIVE SHIELD"):
            continue
        if cat == "OBJECTIVE" and side in ("LIGHT", "DARK"):
            obj_side = "LS" if side == "LIGHT" else "DS"
        if side in ("LIGHT", "DARK"):
            votes[side] += 1
    if obj_side:
        return obj_side
    if votes["LIGHT"] > votes["DARK"]:
        return "LS"
    if votes["DARK"] > votes["LIGHT"]:
        return "DS"
    return None


def parse_html_url(url: str):
    slug = unquote(url.rstrip("/").split("/")[-1]).lower()
    slug = slug.replace("fürgut", "furgut").replace("fürgut", "furgut")
    if slug.startswith("019-"):
        slug = "2019-" + slug[4:]
    side = None
    obj = None
    left = slug
    m = re.search(r"-(ds|ls)-(.+)$", slug)
    if m:
        side = m.group(1).upper()
        obj = slang_obj(m.group(2))
        left = slug[: m.start()]
    else:
        m2 = re.search(r"-(ds|ls)$", slug)
        if m2:
            side = m2.group(1).upper()
            left = slug[: m2.start()]
    left = re.sub(r"-day-[123]$", "", left)
    side, obj = polish_side_obj(side, obj)
    rm = re.match(r"(?:2021-)?([a-z0-9-]+)-regionals?-(.+)$", left)
    if rm and rm.group(1) in hm.PLANET_NAME:
        planet, player_slug = rm.groups()
        planet_title = hm.PLANET_NAME[planet]
        player = tidy_player_name(hm.pretty_name(player_slug))
        if side is None:
            rest_player, obj_slug = peel_obj(player_slug)
            if obj_slug:
                obj = slang_obj(obj_slug)
                player = tidy_player_name(hm.pretty_name(rest_player))
                side, obj = polish_side_obj(side, obj)
        if side is None:
            side = side_from_obj(obj or "") or "DS"
        return "21regionals", planet_title, player, side, obj, url
    for pref, key, stage in HTML_PREFIXES:
        pref_n = pref.rstrip("-")
        if left != pref_n and not left.startswith(pref_n + "-"):
            continue
        rest = left[len(pref_n) :].strip("-")
        rest = re.sub(r"-day-[123]$", "", rest)
        if side is None:
            player_slug, obj_slug = peel_obj(rest)
            if not player_slug:
                blob = re.sub(r"^\d{4}-[a-z0-9]+-", "", pref_n)
                blob = re.sub(r"-(final|round|day|tiebreaker|top|elite).*$", "", blob)
                player_slug = blob.strip("-")
            if not player_slug:
                return None
            player = hm.pretty_name(player_slug)
            obj = slang_obj(obj_slug) if obj_slug else rest
            side, obj = polish_side_obj(side, obj)
        else:
            player = hm.pretty_name(rest) if rest else ""
        if not player:
            blob = re.sub(r"^\d{4}-[a-z0-9]+-", "", pref_n)
            blob = re.sub(r"-(final|round|day|tiebreaker|top|elite).*$", "", blob)
            player = hm.pretty_name(blob.strip("-"))
        player = tidy_player_name(player)
        if is_junk_player(player):
            return None
        return key, stage, player, side, obj, url
    return None


def emit_deck(meta, player, t8, side, obj, stage, counts, cards, media, companion, bp, dests, title_map, pc_url=None):
    title = deck_title(meta, player, side, obj, stage)
    g26.deck_title = lambda e, p, t, s, o: title
    g26.event_title = lambda e: meta["title"]
    ev = "Nats"
    title2, body, hub = g26.render_deck(
        ev, player, t8, side, obj, counts, cards, media or "none.txt", companion, bp, dests, title_map
    )
    body = body.replace("[[Category:2026]]", f"[[Category:{meta['year']}]]")
    body = body.replace("* '''Format:''' [[Open]]", f"* '''Format:''' {meta['format']}")
    lab = STAGE_LABEL.get(stage, "Day 1")
    if meta.get("regional") and stage not in STAGE_LABEL:
        lab = stage
    body = re.sub(r"\* '''Stage:''' [^\n]+", f"* '''Stage:''' {lab}", body, count=1)
    if not media:
        if pc_url:
            body = re.sub(
                r"\* '''GEMP Importable deck:'''[^\n]+",
                f"* '''Source:''' [{pc_url} PC list]",
                body,
                count=1,
            )
        else:
            body = re.sub(r"\* '''GEMP Importable deck:'''[^\n]+\n", "", body, count=1)
    (PAGES / wiki_fname(title)).write_text(body, encoding="utf-8", newline="\n")
    return title, hub


def tidy_player_page(path: Path) -> None:
    """Deduplicate See also / Sources / Categories; newest-first Tournament Results."""
    if not path.exists():
        return
    text = path.read_text(encoding="utf-8")
    months = {
        "january": 1, "february": 2, "march": 3, "april": 4, "may": 5, "june": 6,
        "july": 7, "august": 8, "september": 9, "october": 10, "november": 11, "december": 12,
        "jan": 1, "feb": 2, "mar": 3, "apr": 4, "jun": 6, "jul": 7, "aug": 8,
        "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
    }
    stage_rank = {
        "final confrontation": 0, "finals": 0, "championship": 0,
        "day 3": 1, "semifinals": 1, "final four": 1, "final 4": 1, "top 4": 1,
        "quarterfinals": 2, "tiebreaker": 2,
        "top 8": 3, "round of 8": 3, "team usa": 3, "team europe": 3, "round 2": 3,
        "day 2": 4, "round 1": 4,
        "round of 16": 5, "top 16": 5,
        "day 1": 6, "pods": 6,
    }

    def row_key(row: str):
        cells = [c.strip() for c in row.split("||")]
        date = cells[0] if cells else ""
        ev = cells[1] if len(cells) > 1 else ""
        year = 0
        ym = re.search(r"(20\d{2})", date)
        if ym:
            year = int(ym.group(1))
        found_m = [months[m.group(1).lower()] for m in re.finditer(
            r"(January|February|March|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Apr|Jun|Jul|Aug|Sept?|Oct|Nov|Dec)\b",
            date, re.I,
        )]
        month = max(found_m) if found_m else 0
        days = [int(x) for x in re.findall(r"\b(\d{1,2})\b", date) if int(x) <= 31]
        day = max(days) if days else 0
        lab = ""
        lm = re.search(r"\(([^)]+)\)\s*$", ev)
        if lm:
            lab = lm.group(1).strip().lower()
        sr = stage_rank.get(lab, 9)
        return (-year, -month, -day, sr, ev)

    m = re.search(
        r"(== Tournament Results ==\s*\{\| class=\"wikitable\"\s*\|-\s*\n! Date !! Event !! Format !! Finish !! Dark !! Light\n)(.*?)(\n\|\})",
        text,
        re.S,
    )
    if m:
        raw_rows = re.findall(r"\|-\s*\n\| [^\n]+", m.group(2))
        seen = []
        for r in raw_rows:
            r = re.sub(r"^\|-\s*\n", "|- \n", r)
            if r not in seen:
                seen.append(r)
        if raw_rows:
            seen.sort(key=row_key)
            text = text[: m.start()] + m.group(1) + "\n".join(seen) + m.group(3) + text[m.end() :]

    def dedupe_star_block(heading: str, keep_last: tuple[str, ...] = ()) -> None:
        nonlocal text
        mm = re.search(
            "(== " + re.escape(heading) + r" ==\n\n)(.*?)(?=\n== |\n\{\{|\n\[\[Category:)",
            text,
            re.S,
        )
        if not mm:
            return
        lines = [ln for ln in mm.group(2).splitlines() if ln.strip()]
        out = []
        tail = []
        for ln in lines:
            if any(k in ln for k in keep_last):
                if ln not in tail:
                    tail.append(ln)
                continue
            if ln not in out:
                out.append(ln)
        block = "\n".join(out + tail) + "\n"
        text = text[: mm.start()] + mm.group(1) + block + text[mm.end() :]

    dedupe_star_block("See also", ("List of SWCCG tournaments", "Championships"))
    dedupe_star_block("Sources")
    cats = re.findall(r"\[\[Category:[^\]]+\]\]", text)
    if cats:
        uniq = []
        for c in cats:
            if c not in uniq:
                uniq.append(c)
        text = re.sub(r"\n\[\[Category:[^\]]+\]\]", "", text)
        if not text.endswith("\n"):
            text += "\n"
        text += "\n".join(uniq) + "\n"
    path.write_text(text, encoding="utf-8", newline="\n")


def process():
    EVENTS.sort(key=lambda e: e["tag"], reverse=True)
    title_map = ug.load_json(ug.MAP_PATH)
    obj_inv = ug.load_json(ug.OBJ_INV) if ug.OBJ_INV.exists() else {"members": []}
    dests = ug.dests_index(title_map, obj_inv)
    bp = ug.load_bp()
    by_id, by_title = load_bp_simple()
    MEDIA.mkdir(parents=True, exist_ok=True)
    STUBS.mkdir(parents=True, exist_ok=True)

    list_rows = defaultdict(list)
    titles = []
    total = 0

    # HTML decks keyed by (event_key, stage, player, side)
    html_parsed = []
    if DECKS.exists():
        for path in sorted(DECKS.glob("*.html")):
            try:
                if path.stat().st_size < 4000:
                    continue
                raw = path.read_text(encoding="utf-8", errors="replace")
            except (PermissionError, OSError) as e:
                print("LOCK", path.name, e)
                continue
            if "Page not found" in raw or "doesn't seem to exist" in raw:
                continue
            canon_url = None
            m = re.search(r'rel="canonical" href="([^"]+)"', raw, re.I)
            if m:
                canon_url = m.group(1)
            else:
                m = re.search(r'https://www\.starwarsccg\.org/[a-z0-9-]+/?', raw, re.I)
                canon_url = m.group(0) if m else None
            if not canon_url:
                continue
            info = parse_html_url(canon_url)
            if not info:
                continue
            key, stage, player, side, obj, url = info
            if is_junk_player(player):
                continue
            try:
                counts, cards = parse_html_deck(path, bp, by_title)
            except Exception as e:
                print("BADHTML", path.name, e)
                continue
            if sum(counts.values()) < 10:
                print("THINHTML", path.name, sum(counts.values()))
                continue
            inferred = side_from_cards(cards, by_id, by_title)
            if inferred:
                side = inferred
            elif not side:
                side = side_from_obj(obj or "") or "DS"
            if not obj:
                for _cid, title, tag in cards:
                    if tag != "card":
                        continue
                    rec = by_title.get((title or "").lower()) or {}
                    if (rec.get("cat") or "").upper() == "OBJECTIVE":
                        obj = title.split("/")[0].strip()
                        break
                if not obj:
                    obj = "constructed"
            obj = hub_obj_from_cards(cards, bp, dests, title_map, by_title, obj, side)
            html_parsed.append((key, stage, player, side, obj, counts, cards, url))
        print("html decks", len(html_parsed))

    html_by_ev = defaultdict(list)
    for row in html_parsed:
        html_by_ev[row[0]].append(row)

    wrap_orders = orders_from_wraps()
    for k, stages in wrap_orders.items():
        print("wrap-order", k, {st: len(v) for st, v in stages.items()})

    for meta in EVENTS:
        ev = meta["key"]
        parsed = []  # player, t8, side, obj, media, counts, cards, stage
        for folder in meta.get("folders") or []:
            d = TD / folder
            if not d.exists():
                print("NOFOLDER", d)
                continue
            for path in sorted(d.glob("*")):
                if not path.is_file():
                    continue
                info = parse_gemp_file(folder, path.name)
                if not info:
                    print("SKIP", folder, path.name)
                    continue
                player, t8, side, obj, stage = info
                try:
                    counts, cards = parse_any(path, by_id, by_title, bp)
                except Exception as e:
                    print("BADXML", path.name, e)
                    continue
                if sum(counts.values()) < 8:
                    print("THIN", path.name, sum(counts.values()))
                    continue
                obj = hub_obj_from_cards(cards, bp, dests, title_map, by_title, obj, side)
                media = path.name
                dest_media = MEDIA / media
                if dest_media.exists() and dest_media.resolve() != path.resolve():
                    media = f"{folder}-{path.name}"
                    dest_media = MEDIA / media
                shutil.copy2(path, dest_media)
                parsed.append((player, t8, side, obj, media, counts, cards, stage))

        wrap_st = wrap_orders.get(ev) or {}
        meta_order = dict(meta.get("order") or {})
        for key, stage, player, side, obj, counts, cards, url in html_by_ev.get(ev, []):
            # skip if GEMP already has this player/side/stage
            if any(p == player and s == side and st == stage for p, _t, s, _o, _m, _c, _ca, st in parsed):
                continue
            t8 = stage not in ("d1", "pod")
            parsed.append((player, t8, side, obj, "", counts, cards, stage))
            if stage == "pod":
                for better in ("final", "sf", "t4", "qf", "tb", "t8", "t16"):
                    names = meta_order.get(better) or wrap_st.get(better) or []
                    if player in names and not any(
                        p == player and s == side and st == better for p, _t, s, _o, _m, _c, _ca, st in parsed
                    ):
                        parsed.append((player, True, side, obj, "", counts, cards, better))
                        break

        deck_titles = {}
        hub_labels = {}
        for player, t8, side, obj, media, counts, cards, stage in parsed:
            deck_titles[(player, stage, side)] = deck_title(meta, player, side, obj, stage)

        for player, t8, side, obj, media, counts, cards, stage in parsed:
            other = "LS" if side == "DS" else "DS"
            companion = deck_titles.get((player, stage, other))
            pc_url = meta["pc"]
            title, hub = emit_deck(
                meta, player, t8, side, obj, stage, counts, cards, media, companion, bp, dests, title_map, pc_url
            )
            hub_labels[title] = hub_obj_from_cards(
                cards, bp, dests, title_map, by_title, obj, side
            ) or hub
            titles.append((title, f"pages/{wiki_fname(title)}"))
            total += 1

        dt, hl = {}, {}
        for player, t8, side, obj, media, counts, cards, stage in parsed:
            title = deck_title(meta, player, side, obj, stage)
            dt[(player, stage, side)] = title
            hl[title] = hub_labels.get(title, title)

        by_stage = defaultdict(list)
        for player, t8, side, obj, media, counts, cards, stage in parsed:
            if player not in by_stage[stage]:
                by_stage[stage].append(player)
        order = dict(meta.get("order") or {})
        for st, plist in (wrap_orders.get(ev) or {}).items():
            if len(plist) < 2:
                continue
            if st in order and order[st]:
                order[st] = ordered(plist, order[st])
                continue
            # Day 1 / pod wraps are often alphabetical. 2019 Euro Day 2/3 wrap
            # is Light-then-Dark, not finish order.
            if st in ("d1", "pod", "d2", "d3"):
                continue
            if st[:1].isupper() or st in (
                "final",
                "t4",
                "t8",
                "t16",
                "sf",
                "qf",
                "tb",
                "usa",
                "eur",
                "r1",
                "r2",
            ):
                order[st] = plist
        for stage, players in list(by_stage.items()):
            by_stage[stage] = [p for p in ordered(players, order.get(stage) or []) if not is_junk_player(p)]
        # fill stage lists from wrap/hardcoded order even without decks
        for stage, heading, _t8 in meta.get("stages") or []:
            if stage in order and order[stage]:
                by_stage[stage] = ordered(by_stage.get(stage) or [], order[stage])
                if not by_stage[stage]:
                    by_stage[stage] = list(order[stage])
        if meta.get("regional"):
            for planet, _dt_s, _w in REGIONS_2021:
                if planet in order and order[planet]:
                    by_stage[planet] = ordered(by_stage.get(planet) or [], order[planet])

        if meta["key"] in ("19outrider", "21outrider"):
            # Hubs and player Finish rows are owned by generate_outrider_teams.py
            print("SKIPHUB", meta["title"])
            list_rows[meta["year"]].append(
                f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || {meta['winner']}"
            )
            continue
        write_hub(meta, dt, hl, by_stage, order)
        titles.append((meta["title"], f"pages/{wiki_fname(meta['title'])}"))

        by_p = defaultdict(list)
        for player, t8, side, obj, media, counts, cards, stage in parsed:
            by_p[player].append((t8, stage))
        for player, recs in by_p.items():
            if is_junk_player(player):
                continue
            rows = []
            seen_st = set()
            # later stage first
            rank = {
                "final": 0,
                "sf": 1,
                "t4": 1,
                "qf": 2,
                "tb": 2,
                "t8": 3,
                "d3": 3,
                "r2": 3,
                "usa": 3,
                "eur": 3,
                "d2": 4,
                "r1": 4,
                "t16": 5,
                "d1": 6,
                "pod": 6,
            }
            recs_sorted = sorted(set(recs), key=lambda x: rank.get(x[1], 9))
            for t8, stage in recs_sorted:
                if stage in seen_st:
                    continue
                seen_st.add(stage)
                lab = STAGE_LABEL.get(stage, stage)
                ev_cell = f"[[{meta['title']}]] ({lab})" if lab not in ("Day 1",) else f"[[{meta['title']}]]"
                if meta.get("regional"):
                    ev_cell = f"[[{meta['title']}]] ({stage})"
                    date_cell = next((d for p, d, w in REGIONS_2021 if p == stage), meta["dates"])
                else:
                    date_cell = meta["dates"]
                finish = "—"
                pref = order.get(stage) or []
                if player in pref:
                    finish = str(pref.index(player) + 1)
                rows.append(
                    f"|- \n| {date_cell} || {ev_cell} || {meta['format']} || {finish} || {cell(dt, hl, player, stage, 'DS')} || {cell(dt, hl, player, stage, 'LS')}"
                )
            rows = [r for r in rows if "|| — || —" not in r or "Top 8" in r or "Day 2" in r or "Day 3" in r or "Final" in r]
            if not rows:
                continue
            dest_stub = STUBS / (player.replace(" ", "_") + ".wiki")
            bio = PAGES / (player.replace(" ", "_") + ".wiki")
            if bio.exists() and is_bio(bio.read_text(encoding="utf-8", errors="replace")):
                # merge into bio via a temp copy of upsert on stubs then... write bio
                text = bio.read_text(encoding="utf-8")
                text = re.sub(rf"\|-\s*\n\| [^\n]*\[\[{re.escape(meta['title'])}\]\][^\n]*\n", "", text)
                if "|}" in text and "Tournament Results" in text:
                    text = text.replace("|}\n", "\n".join(rows) + "\n|}\n", 1)
                cat = f"[[Category:{meta['year']}]]"
                if cat not in text:
                    text = text.replace("[[Category:Players]]", f"[[Category:Players]]\n{cat}")
                bio.write_text(text, encoding="utf-8", newline="\n")
                titles.append((player, f"pages/{bio.name}"))
            else:
                upsert_stub(player, rows, meta["title"], meta["pc"])
                if dest_stub.exists():
                    st = dest_stub.read_text(encoding="utf-8")
                    cat = f"[[Category:{meta['year']}]]"
                    if cat not in st:
                        st = st.replace("[[Category:Players]]", f"[[Category:Players]]\n{cat}")
                        st = st.replace("[[Category:2026]]", f"[[Category:{meta['year']}]]")
                        dest_stub.write_text(st, encoding="utf-8", newline="\n")
                    titles.append((player, f"pages/player-stubs/{dest_stub.name}"))

        win = meta["winner"]
        win_cell = f"[[{win}]]" if win not in ("—", "") else "—"
        list_rows[meta["year"]].append(
            f"|- \n| {meta['tag']} || [[{meta['title']}|{meta['list_label']}]] || {meta['dates']} || {meta['site']} || {meta['format']} || {win_cell}"
        )
        print("event", meta["title"], "decks", len(parsed), "stages", {k: len(v) for k, v in by_stage.items()})

    def tag_key(row: str) -> str:
        m = re.search(r"\| (\d{4}-\d{2})", row)
        return m.group(1) if m else ""

    for year in list_rows:
        list_rows[year] = sorted(list_rows[year], key=tag_key, reverse=True)

    patch_list(list_rows)
    titles.append(("List of SWCCG tournaments", "pages/List_of_SWCCG_tournaments.wiki"))
    titles.append(("European Championships", "pages/European_Championships.wiki"))
    titles.append(("Formats", "pages/Formats.wiki"))
    titles.append(("Premiere - Reflections II", "pages/Premiere_-_Reflections_II.wiki"))
    # redirects
    redirs = {
        "2021 World Championships": "2021 World Championship",
        "2020 World Championships": "2020 World Championship",
        "2019 Worlds": "2019 World Championship",
        "2019 European Championships": "2019 European Championship",
        "2019 North American Continentals": "2019 North American Continental Championship",
        "2021 US Nationals": "2021 U.S. National Championship",
        "2021 U.S. Nationals": "2021 U.S. National Championship",
        "2021 Worlds Throwback": "2021 Worlds Throwback Event",
        "2021 Worlds Throwback (Prem-RefII)": "2021 Worlds Throwback Event",
        "2020 Texas Mini-Worlds": "2020 Texas Mini Worlds",
        "2019 Match Play Championships": "2019 Match Play Championship",
        "2020 Match Play Championships": "2020 Match Play Championship",
        "2021 Match Play Championships": "2021 Match Play Championship",
        "2021 Retro Event": "2021 Retro Event (Premiere to Death Star II)",
        "2021 Retro Event (PDS2)": "2021 Retro Event (Premiere to Death Star II)",
        "2019 NAC": "2019 North American Continental Championship",
        "2019 Outrider Cup I": "2019 Outrider Cup",
        "Outrider Cup II": "2021 Outrider Cup",
    }
    for src, dest in redirs.items():
        p = PAGES / wiki_fname(src)
        p.write_text(f"#REDIRECT [[{dest}]]\n", encoding="utf-8", newline="\n")
        titles.append((src, f"pages/{p.name}"))

    seen = {}
    for t, r in titles:
        if t.startswith("Elite 8 ") or is_junk_player(t):
            continue
        seen[t] = r
    for t, r in list(seen.items()):
        p = ROOT / r
        if not p.exists():
            continue
        if r.startswith("pages/player-stubs/") or (
            r.startswith("pages/") and "player-stubs" not in r and is_bio(p.read_text(encoding="utf-8", errors="replace"))
        ):
            tidy_player_page(p)
    tsv = ROOT / "y2019-2021-titles.tsv"
    tsv.write_text("\n".join(f"{t}\t{r}" for t, r in seen.items()) + "\n", encoding="utf-8", newline="\n")
    print("titles", len(seen), "decks", total, "->", tsv)


if __name__ == "__main__":
    process()
