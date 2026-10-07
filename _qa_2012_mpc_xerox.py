#!/usr/bin/env python3
"""Live QA for 2012 MPC leftover Xerox dests."""
from __future__ import annotations

import json
import urllib.parse
import urllib.request

API = "https://wiki.swccg.com/api.php"
CHECKS = [
    (
        "2012 Match Play Championship Day 1 Chris Erwin DS A Stunning Move",
        ["A Stunning Move", "Grievous, Hunter Of Jedi", "Battle Droid Squad", "Chris Erwin"],
    ),
    (
        "2012 Match Play Championship Day 1 Chris Erwin LS Yavin 4 (V)",
        ["Yavin 4 (V)", "I'll Take The Leader", "Kier Santage", "Chris Erwin"],
    ),
    (
        "2012 Match Play Championship Day 1 Scott Lingrell DS Agents Of Black Sun",
        ["Agents Of Black Sun", "A Dark Time For The Rebellion", "Scott Lingrell"],
    ),
    (
        "2012 Match Play Championship Day 1 Scott Lingrell LS Kashyyyk (V)",
        ["Kashyyyk (V)", "Let The Wookiee Win", "Grrrghrrrgh!", "Scott Lingrell"],
    ),
    (
        "2012 Match Play Championship",
        [
            "Chris Erwin",
            "Scott Lingrell",
            "Brian Field",
            "Brian Fred",
            "Matthew Harrison-Trainor",
            "Kevin Shannon",
            "Matt Sokol",
            "Greg Shaw",
            "Cole Lepine",
            "Jonny Chu",
            "Brad Eier",
            "Aaron Nelson",
            "Steve Baroni",
            "Brian Terwilliger",
            "Caleb Foth",
            "Steve Harpster",
            "Barry Alperstein",
            "John Anderson",
            "Casey Anis",
            "Nicholas Amato",
            "Clayton Atkin",
            "Vikram Bali",
            "Amar Banger",
            "James Booker",
            "Andrew Bollentino",
            "Roy Bordier",
            "Brian Brodsky",
            "Ben Brummett",
            "Carl Buck",
            "Justin Carulli",
            "Wayne Cullen",
            "Dalton",
            "Philippe Dubreuil",
            "Pierre Dubreuil",
            "Chuck Finley",
            "Tony Garcia",
            "Mike Gemme",
            "Chris Gogolen",
            "Matt Gombos",
            "Thomas Graham",
            "Brian Herold",
            "Greg Hodur",
            "Brian Hollingworth",
            "Adam Howland",
            "Hayes Hunter",
            "Steve Skilton",
            "PMT",
            "Wojciech Jankowski",
            "Matt Jourdan",
            "Chris Kelly",
            "Mike Kessling",
            "Aaron Kinsey",
            "Jared",
            "Kyle Krueger",
            "Josh Mack",
            "Sam Marlow",
            "Justin Montgomery",
            "Tim Murray",
            "Chris O'Hare",
            "Joe Pinto",
            "Mike Pistone",
            "Mike Richards",
            "Chris Schoenthal",
            "Reid Smith",
            "Pete Srodoski",
            "Matt Thornton",
            "Marty Terwilliger",
            "Michael Thomas",
            "Chris Terwilliger",
            "John Veasey",
            "Alex W",
            "Chris Westergard",
            "SAN",
            "Chris Wirfs",
            "Patrick Ziagos",
            "light_frank",
            "Day 2",
            "Yavin 4 (V)",
            "A Stunning Move",
            "Kashyyyk (V)",
            "Legacy Open",
        ],
    ),
    ("Chris Erwin", ["2012 Match Play Championship", "A Stunning Move", "Yavin 4 (V)"]),
    ("Scott Lingrell", ["2012 Match Play Championship", "Agents Of Black Sun", "Kashyyyk (V)"]),
    (
        "2012 Match Play Championship Day 1 Brian Field DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Brian Field"],
    ),
    (
        "2012 Match Play Championship Day 1 Brian Field LS Watch Your Step",
        ["Watch Your Step", "Gold Squadron 1", "Brian Field"],
    ),
    ("Brian Field", ["2012 Match Play Championship", "Hunt Down", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Matthew Harrison-Trainor DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen Marek, Starkiller", "Blay"],
    ),
    (
        "2012 Match Play Championship Day 1 Matthew Harrison-Trainor LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Let The Wookiee Win", "Blay"],
    ),
    (
        "Matthew Harrison-Trainor",
        ["2012 Match Play Championship", "Hunt Down", "Massassi Throne Room"],
    ),
    (
        "2012 Match Play Championship Day 1 Kevin Shannon DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Kevin Shannon"],
    ),
    (
        "2012 Match Play Championship Day 1 Kevin Shannon LS Watch Your Step",
        ["Watch Your Step", "Rycar Ryjerd", "Kevin Shannon"],
    ),
    ("Kevin Shannon", ["2012 Match Play Championship", "Hunt Down", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Matt Sokol DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Matt Sokol"],
    ),
    (
        "2012 Match Play Championship Day 1 Matt Sokol LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Let The Wookiee Win", "Matt Sokol"],
    ),
    ("Matt Sokol", ["2012 Match Play Championship", "Hunt Down", "Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Greg Shaw DS A Stunning Move",
        ["A Stunning Move", "3,720 To 1", "Greg Shaw"],
    ),
    (
        "2012 Match Play Championship Day 1 Greg Shaw LS Communing",
        ["Communing", "Let The Wookiee Win", "Greg Shaw"],
    ),
    ("Greg Shaw", ["2012 Match Play Championship", "A Stunning Move", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Cole Lepine DS Imperial Occupation (V)",
        ["Imperial Occupation", "Juno Eclipse, Black Leader", "clepine"],
    ),
    (
        "2012 Match Play Championship Day 1 Cole Lepine LS Watch Your Step (V)",
        ["Watch Your Step", "Let The Wookiee Win", "clepine"],
    ),
    ("Cole Lepine", ["2012 Match Play Championship", "Imperial Occupation", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Jonny Chu DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Jonny Chu"],
    ),
    (
        "2012 Match Play Championship Day 1 Jonny Chu LS Communing",
        ["Communing", "Let The Wookiee Win", "Jonny Chu"],
    ),
    ("Jonny Chu", ["2012 Match Play Championship", "Hunt Down", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Brad Eier DS Imperial Occupation (V)",
        ["Imperial Occupation", "Juno Eclipse, Black Leader", "Brad Eier"],
    ),
    (
        "2012 Match Play Championship Day 1 Brad Eier LS Communing",
        ["Communing", "Let's Go Left", "Brad Eier"],
    ),
    ("Brad Eier", ["2012 Match Play Championship", "Imperial Occupation", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Aaron Nelson DS Kessel",
        ["Kessel", "We Must Accelerate Our Plans", "Airdog2003", "Aaron Nelson"],
    ),
    (
        "2012 Match Play Championship Day 1 Aaron Nelson LS Watch Your Step",
        ["Watch Your Step", "Let The Wookiee Win", "Airdog2003", "Aaron Nelson"],
    ),
    ("Aaron Nelson", ["2012 Match Play Championship", "Kessel", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Steve Baroni DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Steve Baroni"],
    ),
    (
        "2012 Match Play Championship Day 1 Steve Baroni LS Communing",
        ["Communing", "Let The Wookiee Win", "Steve Baroni"],
    ),
    ("Steve Baroni", ["2012 Match Play Championship", "Hunt Down", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Brian Terwilliger DS Imperial Occupation (V)",
        ["Imperial Occupation", "Knowledge And Defense", "Brian Terwilliger"],
    ),
    (
        "2012 Match Play Championship Day 1 Brian Terwilliger LS Hidden Base",
        ["Hidden Base", "Imperial Atrocity", "Brian Terwilliger"],
    ),
    ("Brian Terwilliger", ["2012 Match Play Championship", "Imperial Occupation", "Hidden Base"]),
    (
        "2012 Match Play Championship Day 1 Caleb Foth DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Knowledge And Defense", "@9N05", "Caleb Foth"],
    ),
    (
        "2012 Match Play Championship Day 1 Caleb Foth LS Communing",
        ["Communing", "Let The Wookiee Win", "@9N05", "Caleb Foth"],
    ),
    ("Caleb Foth", ["2012 Match Play Championship", "Agents Of Black Sun", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Steve Harpster DS Kessel",
        ["Kessel", "We Must Accelerate Our Plans", "Steve Harpster"],
    ),
    (
        "2012 Match Play Championship Day 1 Steve Harpster LS Watch Your Step (V)",
        ["Watch Your Step", "Let The Wookiee Win", "Steve Harpster"],
    ),
    ("Steve Harpster", ["2012 Match Play Championship", "Kessel", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Barry Alperstein DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen Marek, Starkiller", "MrFromMars", "Barry Alperstein"],
    ),
    (
        "2012 Match Play Championship Day 1 Barry Alperstein LS Hidden Base",
        ["Hidden Base", "Imperial Atrocity", "MrFromMars", "Barry Alperstein"],
    ),
    ("Barry Alperstein", ["2012 Match Play Championship", "Hunt Down", "Hidden Base"]),
    (
        "2012 Match Play Championship Day 1 John Anderson DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "John Anderson"],
    ),
    (
        "2012 Match Play Championship Day 1 John Anderson LS Communing",
        ["Communing", "Imperial Atrocity", "John Anderson"],
    ),
    ("John Anderson", ["2012 Match Play Championship", "A Stunning Move", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Casey Anis DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen Marek, Starkiller", "Casey Anis"],
    ),
    (
        "2012 Match Play Championship Day 1 Casey Anis LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Dark Approach", "Jedi Levitation", "Casey Anis"],
    ),
    ("Casey Anis", ["2012 Match Play Championship", "Hunt Down", "Anger, Fear, Aggression"]),
    (
        "2012 Match Play Championship Day 1 Nicholas Amato DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Superlaser", "nicholas.amato", "Nicholas Amato"],
    ),
    (
        "2012 Match Play Championship Day 1 Nicholas Amato LS Rescue The Princess",
        ["Rescue The Princess", "Prisoner 2187", "nicholas.amato", "Nicholas Amato"],
    ),
    ("Nicholas Amato", ["2012 Match Play Championship", "Set Your Course For Alderaan", "Rescue The Princess"]),
    (
        "2012 Match Play Championship Day 1 Clayton Atkin DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Clayton Atkin"],
    ),
    (
        "2012 Match Play Championship Day 1 Clayton Atkin LS Watch Your Step",
        ["Watch Your Step", "BoShek, Brash Smuggler", "Clayton Atkin"],
    ),
    ("Clayton Atkin", ["2012 Match Play Championship", "Hunt Down", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Vikram Bali DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Storm Clouds", "DVD ROTS", "Vikram Bali"],
    ),
    (
        "2012 Match Play Championship Day 1 Vikram Bali LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Podrace Prep", "DVD ROTS", "Vikram Bali"],
    ),
    ("Vikram Bali", ["2012 Match Play Championship", "Hunt Down", "Anger, Fear, Aggression"]),
    (
        "2012 Match Play Championship Day 1 Amar Banger DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Grievous, Hunter Of Jedi", "Amar Banger"],
    ),
    (
        "2012 Match Play Championship Day 1 Amar Banger LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Don't Tread On Me", "Amar Banger"],
    ),
    ("Amar Banger", ["2012 Match Play Championship", "Hunt Down", "Anger, Fear, Aggression"]),
    (
        "2012 Match Play Championship Day 1 James Booker DS A Stunning Move",
        ["A Stunning Move", "Galen Marek, Starkiller", "Darth Maul, Young Apprentice", "James Booker"],
    ),
    (
        "2012 Match Play Championship Day 1 James Booker LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "IL-10", "James Booker"],
    ),
    ("James Booker", ["2012 Match Play Championship", "A Stunning Move", "Anger, Fear, Aggression"]),
    (
        "2012 Match Play Championship Day 1 Andrew Bollentino DS Imperial Occupation (V)",
        ["Imperial Occupation", "ISB Sector Commander", "Lord Bane", "Andrew Bollentino"],
    ),
    (
        "2012 Match Play Championship Day 1 Andrew Bollentino LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Sei Taria", "Andrew Bollentino"],
    ),
    ("Andrew Bollentino", ["2012 Match Play Championship", "Imperial Occupation", "Plead My Case"]),
    (
        "2012 Match Play Championship Day 1 Roy Bordier DS Bring Him Before Me",
        ["Bring Him Before Me", "Kir Kanos With Force Pike", "Spectre", "Roy Bordier"],
    ),
    (
        "2012 Match Play Championship Day 1 Roy Bordier LS You Can Either Profit By This...",
        ["You Can Either Profit By This", "Leia, Rebel Princess", "Roy Bordier"],
    ),
    ("Roy Bordier", ["2012 Match Play Championship", "Bring Him Before Me", "You Can Either Profit By This"]),
    (
        "2012 Match Play Championship Day 1 Brian Brodsky DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Moff Tarkin, Death Star Commandant", "bbrodsky50", "Brian Brodsky"],
    ),
    (
        "2012 Match Play Championship Day 1 Brian Brodsky LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Senator Jar Jar Binks", "Brian Brodsky"],
    ),
    ("Brian Brodsky", ["2012 Match Play Championship", "Set Your Course For Alderaan", "Plead My Case"]),
    (
        "2012 Match Play Championship Day 1 Ben Brummett DS Set Your Course For Alderaan",
        ["Set Your Course For Alderaan", "Grand Admiral Thrawn", "Ben Brummett"],
    ),
    (
        "2012 Match Play Championship Day 1 Ben Brummett LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Impressive, Most Impressive", "Ben Brummett"],
    ),
    ("Ben Brummett", ["2012 Match Play Championship", "Set Your Course For Alderaan", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Carl Buck DS Invasion",
        ["Invasion", "Daultay Dofine", "Carl Buck"],
    ),
    (
        "2012 Match Play Championship Day 1 Carl Buck LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Mandellian Scrubjay", "Carl Buck"],
    ),
    ("Carl Buck", ["2012 Match Play Championship", "Invasion", "Anger, Fear, Aggression"]),
    (
        "2012 Match Play Championship Day 1 Justin Carulli DS A Stunning Move",
        ["A Stunning Move", "Maul Strikes", "Justin Carulli"],
    ),
    (
        "2012 Match Play Championship Day 1 Justin Carulli LS Center Of Tyranny",
        ["Center Of Tyranny", "Bacta Infirmary", "Justin Carulli"],
    ),
    ("Justin Carulli", ["2012 Match Play Championship", "A Stunning Move", "Center Of Tyranny"]),
    (
        "2012 Match Play Championship Day 1 Wayne Cullen DS Combat Readiness (V)",
        ["Combat Readiness", "Tatooine", "Wayne Cullen"],
    ),
    (
        "2012 Match Play Championship Day 1 Wayne Cullen LS Rescue The Princess",
        ["Rescue The Princess", "Desperate Reach", "Wayne Cullen"],
    ),
    ("Wayne Cullen", ["2012 Match Play Championship", "Combat Readiness", "Rescue The Princess"]),
    (
        "2012 Match Play Championship Day 1 Dalton DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Squabbling Delegates", "Dalton"],
    ),
    (
        "2012 Match Play Championship Day 1 Dalton LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Flash Of Insight", "Dalton"],
    ),
    ("Dalton", ["2012 Match Play Championship", "My Lord, Is That Legal?", "Anger, Fear, Aggression"]),
    (
        "2012 Match Play Championship Day 1 Philippe Dubreuil DS Endor Operations",
        ["Endor Operations", "Establish Secret Base", "Philippe Dubreuil"],
    ),
    (
        "2012 Match Play Championship Day 1 Philippe Dubreuil LS Hidden Base (V)",
        ["Hidden Base", "Gold Squadron 1", "Philippe Dubreuil"],
    ),
    ("Philippe Dubreuil", ["2012 Match Play Championship", "Endor Operations", "Hidden Base"]),
    (
        "2012 Match Play Championship Day 1 Pierre Dubreuil DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Pierre Dubreuil"],
    ),
    (
        "2012 Match Play Championship Day 1 Pierre Dubreuil LS Restore Freedom To The Galaxy",
        ["Restore Freedom To The Galaxy", "Massassi Base Sentry", "Pierre Dubreuil"],
    ),
    ("Pierre Dubreuil", ["2012 Match Play Championship", "A Stunning Move", "Restore Freedom To The Galaxy"]),
    (
        "2012 Match Play Championship Day 1 Chuck Finley DS Kessel",
        ["Kessel", "Armored Attack Tank", "Chuck Finley"],
    ),
    (
        "2012 Match Play Championship Day 1 Chuck Finley LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Senator Jar Jar Binks", "Chuck Finley"],
    ),
    ("Chuck Finley", ["2012 Match Play Championship", "Kessel", "Plead My Case To The Senate"]),
    (
        "2012 Match Play Championship Day 1 Tony Garcia DS Invasion",
        ["Invasion", "Destroyer Droid", "Tony Garcia"],
    ),
    (
        "2012 Match Play Championship Day 1 Tony Garcia LS Rescue The Princess",
        ["Rescue The Princess", "Prisoner 2187", "Tony Garcia"],
    ),
    ("Tony Garcia", ["2012 Match Play Championship", "Invasion", "Rescue The Princess"]),
    (
        "2012 Match Play Championship Day 1 Mike Gemme DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Mike Gemme"],
    ),
    (
        "2012 Match Play Championship Day 1 Mike Gemme LS Communing",
        ["Communing", "Chewbacca Of Kashyyyk", "Mike Gemme"],
    ),
    ("Mike Gemme", ["2012 Match Play Championship", "A Stunning Move", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Chris Gogolen DS Endor Operations",
        ["Endor Operations", "Tempest Scout 1", "Chris Gogolen"],
    ),
    (
        "2012 Match Play Championship Day 1 Chris Gogolen LS Anger, Fear, Aggression (V)",
        ["Anger, Fear, Aggression", "Kashyyyk: Wookiee Haven", "Chris Gogolen"],
    ),
    ("Chris Gogolen", ["2012 Match Play Championship", "Endor Operations", "Anger, Fear, Aggression"]),
    (
        "2012 Match Play Championship Day 1 Matt Gombos DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Matt Gombos"],
    ),
    (
        "2012 Match Play Championship Day 1 Matt Gombos LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Master Qui-Gon", "Matt Gombos"],
    ),
    ("Matt Gombos", ["2012 Match Play Championship", "Hunt Down And Destroy The Jedi", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Thomas Graham DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Knowledge And Defense", "Thomas Graham"],
    ),
    (
        "2012 Match Play Championship Day 1 Thomas Graham LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "I'll Take The Odds", "Thomas Graham"],
    ),
    ("Thomas Graham", ["2012 Match Play Championship", "My Lord, Is That Legal?", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Brian Herold DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Gardulla The Hutt", "Brian Herold"],
    ),
    (
        "2012 Match Play Championship Day 1 Brian Herold LS Yavin 4 (V)",
        ["Yavin 4", "Restore Freedom To The Galaxy", "Brian Herold"],
    ),
    ("Brian Herold", ["2012 Match Play Championship", "Agents Of Black Sun", "Yavin 4"]),
    (
        "2012 Match Play Championship Day 1 Greg Hodur DS My Kind Of Scum",
        ["My Kind Of Scum", "Skrilling", "Greg Hodur"],
    ),
    (
        "2012 Match Play Championship Day 1 Greg Hodur LS Center Of Tyranny",
        ["Center Of Tyranny", "Yub Yub, Commander", "Greg Hodur"],
    ),
    ("Greg Hodur", ["2012 Match Play Championship", "My Kind Of Scum", "Center Of Tyranny"]),
    (
        "2012 Match Play Championship Day 1 Brian Hollingworth DS Imperial Occupation (V)",
        ["Imperial Occupation", "Blizzard 2", "Brian Hollingworth"],
    ),
    (
        "2012 Match Play Championship Day 1 Brian Hollingworth LS Watch Your Step (V)",
        ["Watch Your Step", "Yoda, Great Warrior", "Brian Hollingworth"],
    ),
    ("Brian Hollingworth", ["2012 Match Play Championship", "Imperial Occupation", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Adam Howland DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Prince Xizor", "Adam Howland"],
    ),
    (
        "2012 Match Play Championship Day 1 Adam Howland LS Hidden Base",
        ["Hidden Base", "Luke Skywalker, Jedi Knight", "Adam Howland"],
    ),
    ("Adam Howland", ["2012 Match Play Championship", "Agents Of Black Sun", "Hidden Base"]),
    (
        "2012 Match Play Championship Day 1 Hayes Hunter DS Agents Of Black Sun",
        ["Agents Of Black Sun", "We Must Accelerate Our Plans", "Hayes Hunter"],
    ),
    (
        "2012 Match Play Championship Day 1 Hayes Hunter LS Communing",
        ["Communing", "Chewbacca, Protector", "Hayes Hunter"],
    ),
    ("Hayes Hunter", ["2012 Match Play Championship", "Agents Of Black Sun", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Steve Skilton DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Steve Skilton"],
    ),
    (
        "2012 Match Play Championship Day 1 Steve Skilton LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Master Qui-Gon", "Steve Skilton"],
    ),
    ("Steve Skilton", ["2012 Match Play Championship", "Hunt Down And Destroy The Jedi", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 PMT DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "PMT"],
    ),
    (
        "2012 Match Play Championship Day 1 PMT LS Careful Planning",
        ["Careful Planning", "Queen Amidala", "PMT"],
    ),
    ("PMT", ["2012 Match Play Championship", "A Stunning Move", "Careful Planning"]),
    (
        "2012 Match Play Championship Day 1 Wojciech Jankowski DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Imperial Stormtrooper", "Wojciech Jankowski"],
    ),
    (
        "2012 Match Play Championship Day 1 Wojciech Jankowski LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Sandspeeder", "Wojciech Jankowski"],
    ),
    ("Wojciech Jankowski", ["2012 Match Play Championship", "Hunt Down And Destroy The Jedi", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Matt Jourdan DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Matt Jourdan"],
    ),
    (
        "2012 Match Play Championship Day 1 Matt Jourdan LS Yavin 4 (V)",
        ["Yavin 4 (V)", "Padme Naberrie", "Matt Jourdan"],
    ),
    ("Matt Jourdan", ["2012 Match Play Championship", "A Stunning Move", "Yavin 4 (V)"]),
    (
        "2012 Match Play Championship Day 1 Chris Kelly DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Chris Kelly"],
    ),
    (
        "2012 Match Play Championship Day 1 Chris Kelly LS There Is Good In Him",
        ["There Is Good In Him", "Don't Tread On Me", "Chris Kelly"],
    ),
    ("Chris Kelly", ["2012 Match Play Championship", "A Stunning Move", "There Is Good In Him"]),
    (
        "2012 Match Play Championship Day 1 Mike Kessling DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Prophetess", "Mike Kessling"],
    ),
    (
        "2012 Match Play Championship Day 1 Mike Kessling LS Communing",
        ["Communing", "Yoda, Great Warrior", "Mike Kessling"],
    ),
    ("Mike Kessling", ["2012 Match Play Championship", "Agents Of Black Sun", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Aaron Kinsey DS Endor Operations",
        ["Endor Operations", "Avenger", "Aaron Kinsey"],
    ),
    (
        "2012 Match Play Championship Day 1 Aaron Kinsey LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Luke's Bionic Hand", "Aaron Kinsey"],
    ),
    ("Aaron Kinsey", ["2012 Match Play Championship", "Endor Operations", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Jared DS Hunt Down And Destroy The Jedi",
        ["Hunt Down And Destroy The Jedi", "Battle Droid Squad", "Jared"],
    ),
    (
        "2012 Match Play Championship Day 1 Jared LS Watch Your Step (V)",
        ["Watch Your Step (V)", "Captain Han Solo", "Jared"],
    ),
    ("Jared", ["2012 Match Play Championship", "Hunt Down And Destroy The Jedi", "Watch Your Step (V)"]),
    (
        "2012 Match Play Championship Day 1 Kyle Krueger DS Carbon Chamber Testing",
        ["Carbon Chamber Testing", "IG-88", "Kyle Krueger"],
    ),
    (
        "2012 Match Play Championship Day 1 Kyle Krueger LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Queen Amidala, Ruler Of Naboo", "Kyle Krueger"],
    ),
    ("Kyle Krueger", ["2012 Match Play Championship", "Carbon Chamber Testing", "Plead My Case To The Senate"]),
    (
        "2012 Match Play Championship Day 1 Josh Mack DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Lott Dod", "Josh Mack"],
    ),
    (
        "2012 Match Play Championship Day 1 Josh Mack LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Queen Amidala, Ruler Of Naboo", "Josh Mack"],
    ),
    ("Josh Mack", ["2012 Match Play Championship", "My Lord, Is That Legal?", "Plead My Case To The Senate"]),
    (
        "2012 Match Play Championship Day 1 Sam Marlow DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Sam Marlow"],
    ),
    (
        "2012 Match Play Championship Day 1 Sam Marlow LS Coruscant: Night Club",
        ["Coruscant: Night Club", "Yoda, Master Of The Force", "Sam Marlow"],
    ),
    ("Sam Marlow", ["2012 Match Play Championship", "A Stunning Move", "Coruscant: Night Club"]),
    (
        "2012 Match Play Championship Day 1 Justin Montgomery DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Justin Montgomery"],
    ),
    (
        "2012 Match Play Championship Day 1 Justin Montgomery LS Kashyyyk (V)",
        ["Kashyyyk (V)", "Wookiee (V)", "Justin Montgomery"],
    ),
    ("Justin Montgomery", ["2012 Match Play Championship", "A Stunning Move", "Kashyyyk (V)"]),
    (
        "2012 Match Play Championship Day 1 Tim Murray DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Tim Murray"],
    ),
    (
        "2012 Match Play Championship Day 1 Tim Murray LS Rebel Strike Team (V)",
        ["Rebel Strike Team (V)", "Ewok Celebration", "Tim Murray"],
    ),
    ("Tim Murray", ["2012 Match Play Championship", "A Stunning Move", "Rebel Strike Team (V)"]),
    (
        "2012 Match Play Championship Day 1 Chris O'Hare DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Chris O'Hare"],
    ),
    (
        "2012 Match Play Championship Day 1 Chris O'Hare LS Watch Your Step",
        ["Watch Your Step", "Anger, Fear, Aggression (V)", "Chris O'Hare"],
    ),
    ("Chris O'Hare", ["2012 Match Play Championship", "A Stunning Move", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Joe Pinto DS Spice Mine Operations",
        ["Spice Mine Operations", "Knowledge And Defense (V)", "Joe Pinto"],
    ),
    (
        "2012 Match Play Championship Day 1 Joe Pinto LS Yavin 4 (V)",
        ["Yavin 4 (V)", "Anger, Fear, Aggression (V)", "Joe Pinto"],
    ),
    ("Joe Pinto", ["2012 Match Play Championship", "Spice Mine Operations", "Yavin 4 (V)"]),
    (
        "2012 Match Play Championship Day 1 Mike Pistone DS Imperial Occupation (V)",
        ["Imperial Occupation (V)", "Knowledge And Defense (V)", "Mike Pistone"],
    ),
    (
        "2012 Match Play Championship Day 1 Mike Pistone LS Watch Your Step",
        ["Watch Your Step", "Anger, Fear, Aggression (V)", "Mike Pistone"],
    ),
    ("Mike Pistone", ["2012 Match Play Championship", "Imperial Occupation", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Mike Richards DS Spice Mine Operations",
        ["Spice Mine Operations", "Knowledge And Defense (V)", "Mike Richards"],
    ),
    (
        "2012 Match Play Championship Day 1 Mike Richards LS Restore Freedom To The Galaxy",
        ["Restore Freedom To The Galaxy", "Anger, Fear, Aggression (V)", "Mike Richards"],
    ),
    ("Mike Richards", ["2012 Match Play Championship", "Spice Mine Operations", "Restore Freedom To The Galaxy"]),
    (
        "2012 Match Play Championship Day 1 Chris Schoenthal DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Knowledge And Defense (V)", "Chris Schoenthal"],
    ),
    (
        "2012 Match Play Championship Day 1 Chris Schoenthal LS Watch Your Step",
        ["Watch Your Step", "Anger, Fear, Aggression (V)", "Chris Schoenthal"],
    ),
    ("Chris Schoenthal", ["2012 Match Play Championship", "Hunt Down", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Reid Smith DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Knowledge And Defense (V)", "Reid Smith"],
    ),
    (
        "2012 Match Play Championship Day 1 Reid Smith LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Anger, Fear, Aggression (V)", "Reid Smith"],
    ),
    ("Reid Smith", ["2012 Match Play Championship", "My Lord, Is That Legal?", "Plead My Case To The Senate"]),
    (
        "2012 Match Play Championship Day 1 Pete Srodoski DS Invasion",
        ["Invasion", "Knowledge And Defense (V)", "Pete Srodoski"],
    ),
    (
        "2012 Match Play Championship Day 1 Pete Srodoski LS Yavin 4 (V)",
        ["Yavin 4 (V)", "Anger, Fear, Aggression (V)", "Pete Srodoski"],
    ),
    ("Pete Srodoski", ["2012 Match Play Championship", "Invasion", "Yavin 4 (V)"]),
    (
        "2012 Match Play Championship Day 1 Matt Thornton DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Knowledge And Defense (V)", "Matt Thornton"],
    ),
    (
        "2012 Match Play Championship Day 1 Matt Thornton LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Anger, Fear, Aggression (V)", "Matt Thornton"],
    ),
    ("Matt Thornton", ["2012 Match Play Championship", "My Lord, Is That Legal?", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Marty Terwilliger DS Endor Operations",
        ["Endor Operations", "Knowledge And Defense (V)", "Marty Terwilliger"],
    ),
    (
        "2012 Match Play Championship Day 1 Marty Terwilliger LS Communing",
        ["Communing", "Anger, Fear, Aggression (V)", "Marty Terwilliger"],
    ),
    ("Marty Terwilliger", ["2012 Match Play Championship", "Endor Operations", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Michael Thomas DS A Stunning Move",
        ["A Stunning Move", "Guriadan", "Michael Thomas"],
    ),
    (
        "2012 Match Play Championship Day 1 Michael Thomas LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Traffic Control", "Michael Thomas"],
    ),
    ("Michael Thomas", ["2012 Match Play Championship", "A Stunning Move", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Chris Terwilliger DS Imperial Occupation (V)",
        ["Imperial Occupation", "Juno Eclipse, Black Leader", "Chris Terwilliger"],
    ),
    (
        "2012 Match Play Championship Day 1 Chris Terwilliger LS Center Of Tyranny",
        ["Center Of Tyranny", "Dash Rendar", "Chris Terwilliger"],
    ),
    ("Chris Terwilliger", ["2012 Match Play Championship", "Imperial Occupation", "Center Of Tyranny"]),
    (
        "2012 Match Play Championship Day 1 John Veasey DS Kessel",
        ["Kessel", "I'll Take Them Myself", "Juno Eclipse, Black Leader", "John Veasey"],
    ),
    (
        "2012 Match Play Championship Day 1 John Veasey LS Watch Your Step",
        ["Watch Your Step", "Chewie's AT-ST", "John Veasey"],
    ),
    ("John Veasey", ["2012 Match Play Championship", "Kessel", "Watch Your Step"]),
    (
        "2012 Match Play Championship Day 1 Alex W DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi", "Galen, Secret Apprentice", "Juno Eclipse, Black Leader", "Alex W"],
    ),
    (
        "2012 Match Play Championship Day 1 Alex W LS Quiet Mining Colony",
        ["Quiet Mining Colony", "Booster In Pulsar Skate", "Alex W"],
    ),
    ("Alex W", ["2012 Match Play Championship", "Hunt Down And Destroy The Jedi", "Quiet Mining Colony"]),
    (
        "2012 Match Play Championship Day 1 Chris Westergard DS A Stunning Move",
        ["A Stunning Move", "Galen, Secret Apprentice", "Grievous, Hunter Of Jedi", "Chris Westergard"],
    ),
    (
        "2012 Match Play Championship Day 1 Chris Westergard LS Plead My Case To The Senate",
        ["Plead My Case To The Senate", "Booster In Pulsar Skate", "Chris Westergard"],
    ),
    ("Chris Westergard", ["2012 Match Play Championship", "A Stunning Move", "Plead My Case To The Senate"]),
    (
        "2012 Match Play Championship Day 1 SAN DS My Lord, Is That Legal?",
        ["My Lord, Is That Legal?", "Squabbling Delegates", "Orn Free Taa", "SAN"],
    ),
    (
        "2012 Match Play Championship Day 1 SAN LS Communing",
        ["Communing", "Master Kenobi", "Luke Skywalker, Rebel Hero", "SAN"],
    ),
    ("SAN", ["2012 Match Play Championship", "My Lord, Is That Legal?", "Communing"]),
    (
        "2012 Match Play Championship Day 1 Chris Wirfs DS Imperial Occupation (V)",
        ["Imperial Occupation", "Garindan", "Juno Eclipse, Black Leader", "Chris Wirfs"],
    ),
    (
        "2012 Match Play Championship Day 1 Chris Wirfs LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Let The Wookiee Win", "Chris Wirfs"],
    ),
    ("Chris Wirfs", ["2012 Match Play Championship", "Imperial Occupation", "Yavin 4: Massassi Throne Room"]),
    (
        "2012 Match Play Championship Day 1 Patrick Ziagos DS Bring Him Before Me",
        ["Bring Him Before Me", "Galen, Secret Apprentice", "Patrick Ziagos"],
    ),
    (
        "2012 Match Play Championship Day 1 Patrick Ziagos LS You Can Either Profit By This...",
        ["You Can Either Profit By This", "Let The Wookiee Win", "Patrick Ziagos"],
    ),
    ("Patrick Ziagos", ["2012 Match Play Championship", "Bring Him Before Me", "You Can Either Profit By This"]),
    (
        "2012 Match Play Championship Day 1 light_frank DS Bring Him Before Me",
        ["Bring Him Before Me", "Galen, Secret Apprentice", "light_frank"],
    ),
    (
        "2012 Match Play Championship Day 1 light_frank LS Hidden Base (V)",
        ["Hidden Base", "I'll Try Spinning", "light_frank"],
    ),
    ("light_frank", ["2012 Match Play Championship", "Bring Him Before Me", "Hidden Base"]),
    (
        "2012 Match Play Championship Day 1 Unknown Player DS Imperial Occupation (V)",
        ["Imperial Occupation", "Unknown Player", "Unknown players"],
    ),
    (
        "2012 Match Play Championship Day 1 Unknown Player LS Communing",
        ["Communing", "Unknown Player", "Unknown players"],
    ),
    ("Unknown Player", ["2012 Match Play Championship", "Imperial Occupation", "Communing"]),
    ("Unknown players", ["2012 Match Play Championship", "Unknown Player"]),
    (
        "2012 Match Play Championship Day 2 Aaron Nelson LS Yavin 4: Massassi Throne Room",
        ["Yavin 4: Massassi Throne Room", "Airdog2003", "Aaron Nelson"],
    ),
    (
        "2012 Match Play Championship Day 2 Aaron Nelson DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Airdog2003", "Aaron Nelson"],
    ),
    (
        "2012 Match Play Championship Day 2 Greg Shaw DS A Stunning Move",
        ["A Stunning Move", "Palpatine's Quarters", "U-3PO", "Greg Shaw"],
    ),
    (
        "2012 Match Play Championship Day 2 Greg Shaw LS Communing",
        ["Communing", "Chewbacca's Revenge", "Chewbacca Of Kashyyyk", "Greg Shaw"],
    ),
    (
        "2012 Match Play Championship Day 2 Steve Harpster LS Watch Your Step (V)",
        ["Watch Your Step (V)", "Steve Harpster"],
    ),
    (
        "2012 Match Play Championship Day 2 Steve Harpster DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi (V)", "Steve Harpster"],
    ),
    (
        "2012 Match Play Championship Day 2 Brian Fred LS We'll Handle This",
        ["We'll Handle This", "Captain Yutani With Blaster Cannon", "Brian Fred"],
    ),
    (
        "2012 Match Play Championship Day 2 Brian Fred DS Executor: Meditation Chamber",
        ["Executor: Meditation Chamber", "Brian Fred"],
    ),
    (
        "2012 Match Play Championship Day 2 Steve Baroni DS Hunt Down And Destroy The Jedi (V)",
        ["Hunt Down And Destroy The Jedi (V)", "Blizzard 4", "Steve Baroni"],
    ),
    (
        "2012 Match Play Championship Day 2 Jonny Chu LS Communing",
        ["Communing", "It's Not My Fault!", "Jonny Chu"],
    ),
    (
        "2012 Match Play Championship Day 2 Jonny Chu DS Agents Of Black Sun",
        ["Agents Of Black Sun", "Guri", "Jonny Chu"],
    ),
    (
        "2012 Match Play Championship Day 2 Cole Lepine LS Watch Your Step (V)",
        ["Watch Your Step (V)", "Cole Lepine"],
    ),
    (
        "2012 Match Play Championship Day 2 Cole Lepine DS Imperial Occupation (V)",
        ["Imperial Occupation (V)", "Cole Lepine"],
    ),
    (
        "2012 Match Play Championship Day 2 Kevin Shannon LS Watch Your Step",
        ["Watch Your Step", "Kevin Shannon"],
    ),
    (
        "2012 Match Play Championship Day 2 Kevin Shannon DS Hunt Down And Destroy The Jedi",
        ["Hunt Down And Destroy The Jedi", "Kevin Shannon"],
    ),
]


def parse(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "parse",
            "page": title,
            "prop": "text|revid|displaytitle",
            "format": "json",
            "disablelimitreport": 1,
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def flagged(title: str) -> dict:
    q = urllib.parse.urlencode(
        {
            "action": "query",
            "titles": title,
            "prop": "info|flagged",
            "format": "json",
        }
    )
    req = urllib.request.Request(API + "?" + q, headers={"User-Agent": "swccg-wiki-qa"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = json.loads(r.read().decode("utf-8"))
    pages = data.get("query", {}).get("pages", {})
    return next(iter(pages.values()))


def main() -> None:
    fail = 0
    for title, needles in CHECKS:
        data = parse(title)
        if "error" in data:
            print("FAIL", title, data["error"])
            fail += 1
            continue
        html = data["parse"]["text"]["*"]
        missing = [n for n in needles if n not in html]
        fl = flagged(title)
        latest = fl.get("lastrevid")
        stable = (fl.get("flagged") or {}).get("stable_revid")
        fr = "OK" if latest and stable and int(latest) == int(stable) else f"latest={latest} stable={stable}"
        if missing or fr != "OK":
            print("FAIL", title, "missing", missing, "fr", fr)
            fail += 1
        else:
            print("OK", title, "fr", fr)
    print("TOTAL", fail)


if __name__ == "__main__":
    main()
