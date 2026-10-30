"""2021-2023 hubs."""
from lib import *

def T(y):
    return get_tables(open(f'live_{y}.wiki').read())

WRAP21 = ('[https://www.starwarsccg.org/2021-world-championship-wrap-olson-wins-again/ 2021 World Championship Wrap – Olson Wins Again!], '
          'starwarsccg.org (18 October 2021). Preserved copy: [https://web.archive.org/web/20261012175708/https://swccg.com/snapshots/pc/2021-world-championship-wrap-olson-wins-again.html Internet Archive]')
TB21 = '[https://www.starwarsccg.org/2021-worlds-retro-prem-ref-ii-event/ 2021 Worlds Throwback Event], starwarsccg.org'

def y2021():
    t = T(2021)
    tb = get_tables(open('live_throwback.wiki').read())['Finish']
    d = dict(pc='[https://www.starwarsccg.org/2021-world-championships/ 2021 World Championships], starwarsccg.org',
             wrap=WRAP21, awards=AWARDS, tb=TB21)
    ib = infobox(2021, 'Joe Olson 2021 World Championship trophy.jpg', 'Joe Olson, 2021 World Champion',
                 '8–10 October 2021 (main event 9–10 October){{R|wrap}}{{R|awards}}',
                 'Hyatt Regency Crystal City, Arlington, Virginia, USA (Washington, D.C. area){{R|wrap}}', '[[Open]]',
                 '60{{R|wrap}}', '[[Joe Olson]]', '[[Matt Scott]]{{R|wrap}}')
    lead = ("The '''2021 World Championship''' was the 26th Star Wars CCG World Championship, held by the [[Players Committee]] at the Hyatt Regency Crystal City "
            "in Arlington, Virginia, over the weekend of 8–10 October 2021, with four sanctioned events across three days.{{R|wrap}} "
            "(The hub previously gave 7–10 October; the wrap-up gives 8–10 October.) "
            "Sixty players entered the main event.{{R|wrap}} [[Joe Olson]] defended his 2020 title by defeating [[Matt Scott]] in the Final Confrontation, "
            "with Agents Of Black Sun and Qui-Gon Communing;{{R|wrap}}{{R|pc}} it was his fourth straight major win. "
            "He became the sixth player to win two World Championships and the second, after [[Bastian Winkelhaus]], to win in consecutive years.{{R|wrap}} "
            "Olson was inducted into the Players Committee Hall of Fame on 9 October 2021, just before Game 1 of the main event.{{R|wrap}}{{R|awards}}")
    res = ("== Results ==\n\nFinal Top 8 order and Day 2 (Top 8) decks as published.{{R|pc}}\n\n" + table('Place', t['Top 8']) +
           "\n\n=== Top 8 bracket ===\n\n"
           "Every player at 6–2 or better made the cut. [[Jared Napolitano]] finished Day 1 first, followed by the other 7–1 players [[Tom Haid]] and [[Matt Scott]]; "
           "[[Greg Shaw]], [[Barry Alperstein]], [[Robbie Hendon]], [[Casey Anis]] and [[Joe Olson]] (8th on Day 1) completed the Top 8.{{R|wrap}}\n"
           "* '''Quarterfinals:''' Olson def. Shaw; Scott def. Hendon.{{R|wrap}}\n"
           "* '''Semifinals:''' Olson def. Napolitano; Scott def. Alperstein.{{R|wrap}}\n"
           "* '''Final:''' Olson def. Scott.{{R|wrap}}\n\n"
           "The other two quarterfinal results and all game scores were not published.")
    d1 = ("== Day 1 ==\n\nEvery published Day 1 pair (unranked).{{R|pc}}\n\n" + table('Day 1', t['Day 1']))
    side = ("== Side events ==\n\n"
            "* '''Team tournament''' (Friday evening, 18 teams, glass mug trophies): won by \"Stop Batmouse Cold\", [[Dan Tartaglione]] and [[Brad Reinhold]]. "
            "\"Potential Allies\" ([[Charlie Arlandson]] and [[Amar Banger]]) finished second.{{R|wrap}}\n"
            "* '''Consolation''' (Sunday, 28 players): won by [[Anthony Howard]] at 5–1; [[Ryan Jellison]], [[Chris Gogolen]] and [[Sam Tashima]] finished 2nd–4th.{{R|wrap}}\n"
            "* '''Hall of Fame:''' [[Joe Olson]], enshrined 9 October 2021, introduced by [[Phil Aasen]].{{R|wrap}}{{R|awards}}\n"
            "* '''[[2021 Worlds Throwback Event|Throwback Event]]''' (Friday 8 October, six-game Swiss, Premiere–Reflections II cards only): "
            "[[Steve Skilton]] went 6–0 to win, ahead of [[Jared Napolitano]], [[Matt Carulli]] and [[Kevin Elia]]. "
            "The wrap-up gives a field of 15; the published results list 16 pairs.{{R|wrap}}{{R|tb}}\n\n"
            "=== Throwback Event decklists ===\n\n" + table('Finish', tb))
    gal = "== Photographs ==\n\n" + gallery([
        ('2021 World Championship Final Confrontation.jpg', 'Matt Scott and Joe Olson in the Final Confrontation'),
        ('2021 World Championship Top 8.jpg', 'Quarterfinalists: Napolitano, Olson, Haid, Alperstein, Shaw, Scott, Hendon, Anis (photo: Brandon Baity)'),
        ('Tom Haid 2021 World Championship.jpg', 'Tom Haid (crop of the Top 8 photo)'),
        ('2021 World Championship main event room.jpg', 'Players before the start of the main event (photo: Bill Pittman)'),
        ('2021 World Championship Grand In-cake-ador.jpg', 'The "Grand In-cake-ador" sheet cake by Jeffrey Johns'),
        ('2021 World Championship late night gaming.jpg', 'Late night gaming'),
        ('Community card Joe O 2021 Hall of Fame.jpg', 'Community card depicting Joe Olson (2021 Hall of Fame)'),
        ('2021 World Championship banner.png', '2021 World Championship banner'),
        ('2021 World Championship logo.png', '2021 World Championship logo')])
    src = ("== Sources ==\n\n"
           "* [https://www.starwarsccg.org/2021-world-championships/ 2021 World Championship], starwarsccg.org\n"
           f"* {WRAP21}\n* {TB21}\n"
           "* [https://forum.starwarsccg.org/viewforum.php?f=1240 GEMP importable decks], forum.starwarsccg.org\n"
           f"* {AWARDS}")
    body = '\n\n'.join([ib, lead, res, d1, side, gal, '== See also ==\n\n' + see_also(2021, ['[[2021 Worlds Throwback Event]]']), src, FOOT, cats(2021)])
    return body, d

WRAP22 = ('[https://www.starwarsccg.org/2022-world-championship-wrap-desai-wins-third-title/ 2022 World Championship Wrap – Desai Wins Third Title], '
          'starwarsccg.org (22 October 2022). Preserved copy: [https://web.archive.org/web/20261012180004/https://swccg.com/snapshots/pc/2022-world-championship-wrap-desai-wins-third-title.html Internet Archive]')

def y2022():
    t = T(2022)
    d = dict(pc='[https://www.starwarsccg.org/2022-swccg-world-championship/ 2022 SWCCG World Championship], starwarsccg.org. Preserved copy: [https://swccg.com/snapshots/pc/2022-swccg-world-championship.html swccg.com snapshot]',
             wrap=WRAP22, awards=AWARDS, gemp='[https://forum.starwarsccg.org/viewtopic.php?t=81726 GEMP Importable Decklists], forum.starwarsccg.org')
    ib = infobox(2022, 'Justin Desai 2022 World Championship.jpg', 'Justin Desai, 2022 World Champion (photo: Dan Tartaglione)',
                 '14–16 October 2022 (main event 15–16 October){{R|wrap}}',
                 'Hyatt Regency Peachtree (as named in the wrap-up), Atlanta, Georgia, USA{{R|wrap}}', '[[Open]]',
                 '51{{R|wrap}}', '[[Justin Desai]]{{R|awards}}', '[[Matthew Harrison-Trainor]]{{R|wrap}}')
    lead = ("The '''2022 World Championship''' was the 27th Star Wars CCG World Championship, held by the [[Players Committee]] in Atlanta, Georgia, "
            "over the weekend of 14–16 October 2022, with four sanctioned events across three days.{{R|wrap}} "
            "(The hub previously gave 13–16 October.) The main event had 51 players.{{R|wrap}} "
            "[[Justin Desai]] defeated [[Matthew Harrison-Trainor]] in the Final Confrontation with Moment Of Triumph (V) and The Galaxy May Need A Legend,{{R|wrap}}{{R|pc}} "
            "winning his third World Championship (after 2013 and 2015) and joining [[Bastian Winkelhaus]] as the only three-time champions.{{R|wrap}}")
    res = ("== Results ==\n\nFinal Top 8 order and Top 8 decks as published.{{R|pc}}\n\n" + table('Place', t['Top 8']) +
           "\n\n=== Top 8 bracket ===\n\n"
           "[[Joe Olson]] was the only player at 7–1 after Day 1. Nine players finished 6–2, in order: Desai, [[Ryan Jellison]], [[Greg Shaw]], [[Kyle Krueger]], "
           "[[Hayes Hunter]], Harrison-Trainor, [[Jeremy DiPaolo]], [[Chris Wirfs]] and [[Sam Tashima]]. In two play-in games DiPaolo beat Wirfs and Harrison-Trainor beat Tashima.{{R|wrap}}\n"
           "* '''Quarterfinals:''' Desai def. Krueger; Harrison-Trainor def. Shaw.{{R|wrap}}\n"
           "* '''Semifinals:''' Desai def. Hunter; Harrison-Trainor def. Olson.{{R|wrap}}\n"
           "* '''Final:''' Desai def. Harrison-Trainor.{{R|wrap}}\n\n"
           "The other two quarterfinal results and all game scores were not published.")
    import json
    d1 = ("== Day 1 ==\n\nDay 1 standings in the order published on the Players Committee results page.{{R|pc}}\n\n" + table('Day 1', json.load(open('day1_2022.json'))))
    side = ("== Side events ==\n\n"
            "* '''Team tournament''' (Friday evening, 12 teams, glass mug trophies): won by [[Justin Desai]] and [[Steve Baroni]] (\"Kashyyyk Train of Dominance\"); "
            "[[Matthew Harrison-Trainor]] and [[Matt Lutz]] (\"Drs. Matt\") were second. [[Dan Tartaglione]] directed the event.{{R|wrap}}\n"
            "* '''Consolation''' (Sunday): won by [[Jonny Chu]] at 5–1; [[Ryan Sersen]] was second. [[Bill Kafer]] directed the event.{{R|wrap}}\n"
            "* '''Throdo's Cube Spectacular''' (Friday, draft and four games, 28 players): won by [[Phil Aasen]] ahead of teammate [[Cal Aldred]]; organized by [[Jonathan Murray]].{{R|wrap}}\n"
            "* '''Main-event teams:''' players were assigned to teams for an \"event within the event\" based on main event performance.{{R|wrap}}")
    gal = "== Photographs ==\n\n" + gallery([
        ('2022 World Championship Top 8.jpg', 'Top 8, left to right: Desai, Harrison-Trainor, Shaw, DiPaolo, Olson, Hunter, Krueger, Jellison (photo: Dan Tartaglione)'),
        ('Matthew Harrison-Trainor 2022 World Championship.jpg', 'Runner-up Matthew Harrison-Trainor (crop of the Top 8 photo)'),
        ('Ryan Jellison 2022 World Championship.jpg', 'Ryan Jellison (crop of the Top 8 photo)'),
        ('Kyle Krueger 2022 World Championship.jpg', 'Kyle Krueger (crop of the Top 8 photo)'),
        ('2022 World Championship team placards.jpg', 'Team placards for the main event team competition (photo: Dan Tartaglione)'),
        ('2022 World Championship banner.jpg', '2022 World Championship banner'),
        ('2022 World Championship logo.jpg', '2022 World Championship logo')])
    src = ("== Sources ==\n\n"
           "* [https://www.starwarsccg.org/2022-swccg-world-championship/ 2022 World Championship], starwarsccg.org\n"
           "* [https://forum.starwarsccg.org/viewtopic.php?t=81726 GEMP Importable Decklists]\n"
           f"* {WRAP22}\n* {AWARDS}")
    body = '\n\n'.join([ib, lead, res, d1, side, gal, '== See also ==\n\n' + see_also(2022), src, FOOT, cats(2022)])
    return body, d

def y2023():
    t = T(2023)
    live = open('live_2023.wiki').read()
    import re
    defs = dict(re.findall(r'<ref name="(\w+)">(.*?)</ref>', live))
    d = dict(pc=defs['pc'], wrap=defs['wrap'], gemp=defs['gemp'], awards=AWARDS)
    ib = infobox(2023, 'Hayes Hunter 2023 World Championship.jpg', 'Hayes Hunter, 2023 World Champion',
                 '10–13 August 2023 (main event 12–13 August){{R|wrap}}',
                 'Hyatt Regency, Morristown, New Jersey, USA{{R|wrap}}', '[[Open]]',
                 '69{{R|wrap}}', '[[Hayes Hunter]]', '[[Casey Anis]]{{R|wrap}}')
    lead = ("The '''2023 World Championship''' was the 28th Star Wars CCG World Championship, held by the [[Players Committee]] at the Hyatt Regency in Morristown, New Jersey, "
            "over the weekend of 10–13 August 2023, with five sanctioned events across three days.{{R|wrap}} The PC decklist page gives 11–13 August.{{R|pc}} "
            "The main event had 69 players.{{R|wrap}} [[Hayes Hunter]] won his first World Championship, defeating [[Casey Anis]] in the Final Confrontation "
            "with Tatooine: Desert Landing Site SSA (V) and Obi-Wan Communing.{{R|wrap}}{{R|pc}} "
            "[[Greg Shaw]] was inducted into the Players Committee Hall of Fame on Saturday morning, 12 August 2023.{{R|wrap}}{{R|awards}}")
    res = ("== Results ==\n\nFinal Top 8 order and Top 8 decks as published.{{R|pc}}\n\n" + table('Place', t['Top 8']) +
           "\n\n=== Top 8 bracket ===\n\n"
           "[[Bryan Mischke]] and [[Anthony Howard]] finished Day 1 at 7–1. Ten players finished 6–2, in order: Anis, Hunter, [[Conor Britain]], [[Joe Olson]], "
           "[[Ryan Jellison]], [[Bill Kafer]], [[Brian Fred]], [[Wayne Cullen]], [[Scott Lingrell]] and [[Jonny Chu]]. In four play-in games Chu beat Britain, "
           "Olson beat Lingrell, Jellison beat Cullen and Fred beat Kafer.{{R|wrap}}\n"
           "* '''Quarterfinals:''' Hunter def. Olson; Jellison def. Mischke; Anis def. Chu; Fred def. Howard.{{R|wrap}}\n"
           "* '''Semifinals:''' Hunter def. Jellison; Anis def. Fred.{{R|wrap}}\n"
           "* '''Final:''' Hunter def. Anis.{{R|wrap}}\n\n"
           "Game scores were not published. The PC decklist page spells the 5th-place finisher \"Brian Mischke\".{{R|pc}}")
    sec = dict(sections(live))
    d1intro = sec['Day 1'].split('{|')[0].strip()
    d1 = ("== Day 1 ==\n\n" + d1intro.replace('<ref name="wrap" />', '{{R|wrap}}').replace('<ref name="pc" />', '{{R|pc}}') + "\n\n" + table('Day 1', t['Day 1']))
    side = ("== Side events ==\n\n"
            "* '''Team tournament''' (Friday evening, 16 teams, glass mug trophies): won by [[Justin Desai]] and [[Jonny Chu]] (\"Kashyyyk Train of Dominance\"); "
            "[[Scott Lingrell]] and [[Bill Bacheler]] were second.{{R|wrap}}\n"
            "* '''Retro event''' (Friday, Premiere–Death Star II, 8 players): won by [[Garrett Larson]] (Hidden Base mains and Ralltiir Operations); "
            "[[Joe Horbey]] was second (TRM and ISB scum).{{R|wrap}}\n"
            "* '''Consolation''' (Sunday, 36 players): won by [[Cory Lauer]] at 6–0; [[Greg Shaw]] was second and took the deckbox prize for the best Jawa-format deck.{{R|wrap}}\n"
            "* '''Hall of Fame:''' [[Greg Shaw]], enshrined 12 August 2023, presented by Bill Kafer, with his parents in attendance.{{R|wrap}}{{R|awards}}")
    gal = "== Photographs ==\n\n" + gallery([
        ('2023 World Championship Top 8.jpg', 'Top 8, left to right: Mischke, Chu, Fred, Anis, Jellison, Howard, Hunter, Olson'),
        ('Bryan Mischke 2023 World Championship.jpg', 'Bryan Mischke (crop of the Top 8 photo)'),
        ('Greg Shaw 2023 Hall of Fame.jpg', 'Greg Shaw, inducted into the Players Committee Hall of Fame'),
        ('Community card Greg S 2023 Hall of Fame.jpg', 'Community card depicting Greg Shaw (2023 Hall of Fame)'),
        ('2023 World Championship group photo.jpg', 'Group photo'),
        ('2023 World Championship logo.png', '2023 World Championship logo')])
    src = ("== Sources ==\n\n" + sec['Sources'].strip() + f"\n* {AWARDS}")
    body = '\n\n'.join([ib, lead, res, d1, side, gal, '== See also ==\n\n' + see_also(2023), src, FOOT, cats(2023)])
    return body, d

YEARS = {2021: y2021, 2022: y2022, 2023: y2023}
