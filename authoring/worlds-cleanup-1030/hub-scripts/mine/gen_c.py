"""2024-2026 hubs."""
import json
from lib import *

def T(y):
    return get_tables(open(f'live_{y}.wiki').read())

WRAP24 = ('[https://www.starwarsccg.org/2024-worlds-wrap-up-joe-olson-earns-third-championship-win/ 2024 Worlds Wrap-Up – Joe Olson Earns Third Championship Win], '
          'starwarsccg.org (11 October 2024). Preserved copy: [https://web.archive.org/web/20261012180312/https://swccg.com/snapshots/pc/2024-worlds-wrap-up-joe-olson-earns-third-championship-win.html Internet Archive]')

def y2024():
    t = T(2024)
    d = dict(pc='[https://www.starwarsccg.org/2024-09-world-championships-bochum-germany-19-22-september-2024/ 2024-09 World Championships – Bochum, Germany (19-22 September, 2024)], starwarsccg.org',
             wrap=WRAP24, awards=AWARDS)
    ib = infobox(2024, '2024 World Championship winner and runner-up.jpg', 'Winner Joe Olson and runner-up Emil Wallin',
                 '19–22 September 2024 (main event 21–22 September){{R|wrap}}{{R|awards}}',
                 'Zu den Vier Winden, Bochum, Germany{{R|wrap}}', '[[Open]]', '53{{R|wrap}}', '[[Joe Olson]]', '[[Emil Wallin]]{{R|wrap}}')
    lead = ("The '''2024 World Championship''' was the 29th Star Wars CCG World Championship, held by the [[Players Committee]] at the Zu den Vier Winden bar in Bochum, Germany, "
            "over the weekend of 19–22 September 2024.{{R|wrap}}{{R|pc}} It was the third World Championship held in Europe.{{R|awards}} "
            "The main event on Saturday had 53 players.{{R|wrap}} [[Joe Olson]] defeated [[Emil Wallin]] in the Final Confrontation with Endor Operations and He Is The Chosen One,{{R|wrap}}{{R|pc}} "
            "winning his third World Championship and joining [[Bastian Winkelhaus]] and [[Justin Desai]] as three-time champions.{{R|wrap}} "
            "[[Kevin Jaap]] and [[Hayes Hunter]] were inducted into the Players Committee Hall of Fame during Day 1.{{R|wrap}}{{R|awards}}")
    res = ("== Results ==\n\nFinal Top 8 order and Top 8 decks as published.{{R|pc}}\n\n" + table('Place', t['Top 8']) +
           "\n\n=== Top 8 bracket ===\n\n"
           "After eight Swiss games and four play-in games, [[Timo Dusel]], [[Patrik Csapi]] and Wallin were 7–1; [[Eric Hunter]], Olson, Hayes Hunter and [[Dan Tartaglione]] "
           "finished 6–2, in that order; and [[Jonas Hagen Nørregaard]], the best 5–3 player, took the last place in the cut.{{R|wrap}}\n"
           "* '''Quarterfinals:''' Olson def. Eric Hunter; Hayes Hunter def. Dusel; Wallin def. Tartaglione; Nørregaard def. Csapi.{{R|wrap}}\n"
           "* '''Semifinals:''' Olson def. Hayes Hunter; Wallin def. Nørregaard.{{R|wrap}}\n"
           "* '''Final:''' Olson def. Wallin.{{R|wrap}}\n\n"
           "Game scores were not published. The event was not streamed live; recorded games with commentary were posted to the Players Committee YouTube channel.{{R|wrap}}")
    rows = [['—'] + r[1:] for r in t['Day 1']]
    d1 = ("== Day 1 ==\n\nEvery published Day 1 pair. The source list puts the Top 8 first, in final order, and then everyone else alphabetically, "
          "so it is not the Day 1 standings; the wrap-up gives only the Top 8 records (above).{{R|pc}}{{R|wrap}}\n\n" + table('Day 1', rows))
    side = ("== Side events ==\n\n"
            "* '''Team tournament''' (Friday evening, glass mug trophies): won by [[Emil Wallin]] and [[Brian Fred]].{{R|wrap}}\n"
            "* '''Consolation''' (Sunday, four games, 14 players): won by [[AJ Hatoum]] at 4–0; [[Pär Birgander]] was second.{{R|wrap}}\n"
            "* '''Hall of Fame:''' [[Kevin Jaap]] (presented by [[Chris Menzel]] before the main event) and [[Hayes Hunter]] (presented by his brother [[Eric Hunter]] at a mid-day break), "
            "both enshrined 21 September 2024.{{R|wrap}}{{R|awards}}\n"
            "* [[Tamás Papp]] was tournament director; Kevin Jaap handled prize support.{{R|wrap}}")
    gal = "== Photographs ==\n\n" + gallery([
        ('2024 World Championship Top 8.jpg', 'Top 8, left to right: Wallin, Tartaglione, Olson, Nørregaard, Csapi, Dusel, Eric Hunter, Hayes Hunter'),
        ('Jonas Hagen Norregaard 2024 World Championship.jpg', 'Jonas Hagen Nørregaard (crop of the Top 8 photo)'),
        ('Patrik Csapi 2024 World Championship.jpg', 'Patrik Csapi (crop of the Top 8 photo)'),
        ('Eric Hunter 2024 World Championship.jpg', 'Eric Hunter (crop of the Top 8 photo)'),
        ('2024 World Championship group photo.jpg', 'Players in front of Zu den Vier Winden'),
        ('2024 World Championship prize support.jpg', 'Prize support from Kevin Jaap; Tamás Papp ran the event'),
        ('Kevin Jaap 2024 Hall of Fame.jpg', 'Kevin Jaap, inducted into the Hall of Fame'),
        ('Community card Kevin J 2024 Hall of Fame.jpg', 'Community card depicting Kevin Jaap (2024 Hall of Fame)'),
        ('Community card Hayes H 2024 Hall of Fame.jpg', 'Community card depicting Hayes Hunter (2024 Hall of Fame)'),
        ('2024 World Championship banner.png', '2024 World Championship banner')])
    src = ("== Sources ==\n\n"
           "* [https://www.starwarsccg.org/2024-09-world-championships-bochum-germany-19-22-september-2024/ 2024 World Championship], starwarsccg.org\n"
           f"* {WRAP24}\n"
           "* [https://forum.starwarsccg.org/viewtopic.php?t=84844 GEMP Importable Decklists]\n"
           f"* {AWARDS}")
    body = '\n\n'.join([ib, lead, res, d1, side, gal, '== See also ==\n\n' + see_also(2024), src, FOOT, cats(2024)])
    return body, d

WRAP25 = ('[https://www.starwarsccg.org/world-championship-2025-wrap-up-greg-shaw-wins-his-crown/ World Championship 2025 Wrap-Up: Greg Shaw Wins his Crown], '
          'starwarsccg.org (23 October 2025). Preserved copy: [https://web.archive.org/web/20261012161739/https://swccg.com/snapshots/pc/world-championship-2025-wrap-up-greg-shaw-wins-his-crown.html Internet Archive]')
PC25 = ('[https://www.starwarsccg.org/2025-09-world-championship-seattle-washington-october-4-5-2025/ 2025-09 World Championship – Seattle, Washington (October 4-5, 2025)], '
        'starwarsccg.org (6 October 2025). Preserved copy: [https://swccg.com/snapshots/pc/2025-09-world-championship-seattle-washington-october-4-5-2025.html swccg.com snapshot]')

def y2025():
    t = T(2025)
    d = dict(pc=PC25, wrap=WRAP25)
    ib = infobox(2025, 'Greg Shaw 2025 World Championship.jpg', 'Greg Shaw, 2025 World Champion',
                 '3–5 October 2025 (main event 4–5 October){{R|wrap}}{{R|pc}}',
                 'Hampton Inn & Suites, SeaTac, Washington, USA (Seattle area){{R|wrap}}', '[[Open]]', '55{{R|wrap}}',
                 '[[Greg Shaw]]', '[[Joe Olson]]{{R|wrap}}')
    lead = ("The '''2025 World Championship''' was the 30th Star Wars CCG World Championship, held by the [[Players Committee]] at the Hampton Inn & Suites in SeaTac, Washington, "
            "over the weekend of 3–5 October 2025, with four sanctioned events across three days; the main event was played on 4–5 October.{{R|wrap}}{{R|pc}} "
            "The main event had 55 players.{{R|wrap}} Hall of Famer [[Greg Shaw]] defeated [[Joe Olson]] in the Final Confrontation with Shadow Collective and The Force Is Strong In My Family (Luke Saga),{{R|wrap}}{{R|pc}} "
            "winning his first World Championship after finishing runner-up in 2002 and 2003.{{R|wrap}} [[Brian Fred]] was inducted into the Players Committee Hall of Fame on Saturday morning.{{R|wrap}}")
    res = ("== Results ==\n\nFinal Top 8 order and Day 2 (Top 8) decks as published.{{R|pc}}\n\n" + table('Place', t['Top 8']) +
           "\n\n=== Top 8 bracket ===\n\n"
           "Day 1 was eight games of Swiss play with a cut to the Top 8.{{R|wrap}}\n"
           "* '''Quarterfinals:''' Shaw def. [[Patrick Johnson|Pat Johnson]]; [[Brian Fred]] def. [[Benji Chu]]; Olson def. [[Matthew Harrison-Trainor]]; [[Hayes Hunter]] def. [[Sam Tashima]].{{R|wrap}}\n"
           "* '''Semifinals:''' Shaw def. Fred; Olson def. Hunter.{{R|wrap}}\n"
           "* '''Final:''' Shaw def. Olson.{{R|wrap}}\n\n"
           "Game scores were not published. The games were streamed with commentary by [[Dan Tartaglione]] and [[Garrett Larson]] and posted to a "
           "[https://www.youtube.com/playlist?list=PLQSFYZX0M9YQ_9BL8VcsfvHD371AW5aWM YouTube playlist].{{R|wrap}}")
    d1 = ("== Day 1 ==\n\nDay 1 standings and decks in the order published on the Players Committee results page.{{R|pc}}\n\n" + table('Day 1', t['Day 1']))
    side = ("== Side events ==\n\n"
            "* '''Team tournament''' (Friday evening, 11 teams, glass mug trophies): won by team \"Scott Norwood\", [[Brian Fred]] and [[Jonny Chu]]; "
            "[[Mike Turner]] and [[Nathan Davis|Nate Davis]] were second.{{R|wrap}}\n"
            "* '''Cube''' (Friday, 18 players): won by [[Steve Harpster]]; [[Anthony Howard]] was second.{{R|wrap}}\n"
            "* '''Consolation''' (Sunday, 36 players): won at 6–0 by [[Bryan Mischke]] (spelled \"Brian Mischke\" in the wrap-up); [[Jonny Chu]] was second.{{R|wrap}}\n"
            "* '''Hall of Fame:''' [[Brian Fred]], inducted on Saturday morning, presented by his New Allies teammate [[Mike Kessling]].{{R|wrap}}")
    gal = "== Photographs ==\n\n" + gallery([
        ('Brian Fred 2025 Hall of Fame.jpg', 'Brian Fred, inducted into the Hall of Fame'),
        ('Brian Fred with 2025 Hall of Fame award.jpg', 'Brian Fred with his Hall of Fame award'),
        ('Community card Brian F 2025 Hall of Fame.jpg', 'Community card depicting Brian Fred (2025 Hall of Fame)'),
        ('2025 World Championship banner.png', '2025 World Championship banner')])
    live = open('live_2025.wiki').read()
    src = ("== Sources ==\n\n"
           f"* {PC25}\n* {WRAP25}\n"
           "* [https://forum.starwarsccg.org/viewforum.php?f=1563 2025 World Championship Forum], forum.starwarsccg.org\n"
           "* [https://forum.starwarsccg.org/viewtopic.php?p=1440976#p1440976 GEMP importable decks], forum.starwarsccg.org\n"
           "* [https://www.youtube.com/playlist?list=PLQSFYZX0M9YQ_9BL8VcsfvHD371AW5aWM 2025 World Championship YouTube playlist]")
    body = '\n\n'.join([ib, lead, res, d1, side, gal, '== See also ==\n\n' + see_also(2025), src, FOOT, cats(2025)])
    return body, d

F = 'https://forum.starwarsccg.org/viewtopic.php?t='
def fr(t, title):
    return f'[{F}{t} {title}], Star Wars CCG Players Committee forum'

def y2026():
    t = T(2026)
    picks = [p for p in json.load(open('../w26_extra/photos.json'))['photos'] if p.get('pick')]
    d = dict(pc='[https://www.starwarsccg.org/2026-11-swccg-world-championship-bloomington-minnesota-oct-23-25-2026/ 2026-11 SWCCG World Championship – Bloomington, Minnesota (Oct. 23-25, 2026)], starwarsccg.org',
             t8='[https://forum.starwarsccg.org/viewtopic.php?t=87037 2026 World Championship Top 8], forum.starwarsccg.org',
             sched=fr(86982, 'Schedule of Events (2026 World Championship)'),
             venue=fr(86751, 'forum topic 86751 (venue details)'),
             team=fr(87034, 'Team Tournament updates (2026 World Championship)'),
             conso=fr(87038, 'Consolation Tournament Pairings (2026 World Championship)'),
             prize=fr(87025, 'Prize Support (2026 World Championship)'),
             wc25=WRAP25,
             yt='[https://www.youtube.com/playlist?list=PLTVa1kgaeLRA 2026 World Championship], YouTube playlist, Star Wars CCG channel (11 videos, checked 30 October 2026)',
             slack1='Players Committee Slack, #announcements, imrahil327, 24 October 2026: "58 players for the 2026 World Championship!"',
             slack2='Players Committee Slack, #announcements, imrahil327, 25 October 2026: "Congrats to our newest World Champion, @retwin316!"',
             slack3='Players Committee Slack, #announcements, DTartagOne, 27 October 2026 (Holotheatre announcement)',
             photo='Photo file page: [[:File:2026 World Championship Stream Team.jpg]] (from the shared "Worlds 2026 Photos & Videos" Google Drive folder)')
    ib = infobox(2026, '2026 World Championship Brian Fred champion.jpg', 'Brian Fred with the World Championship trophy',
                 '23–25 October 2026 (main event 24–25 October){{R|sched}}',
                 'Hyatt Regency Bloomington by Mall of America, Bloomington, Minnesota, USA{{R|sched}}{{R|venue}}',
                 '[[Open]] (Virtual Set 27 legal)', '58{{R|t8}}{{R|slack1}}', '[[Brian Fred]]', '[[Justin Desai]]{{R|pc}}')
    lead = ("The '''2026 World Championship''' was the 31st Star Wars CCG World Championship, held by the [[Players Committee]] at the Hyatt Regency Bloomington by Mall of America "
            "in Bloomington, Minnesota, from 23 to 25 October 2026; the main event was played on 24–25 October.{{R|sched}}{{R|venue}} "
            "Fifty-eight players entered, and all 58 played all eight Swiss games.{{R|t8}}{{R|slack1}} "
            "[[Brian Fred]] defeated [[Justin Desai]] in the Final Confrontation with ISB Operations and Diplomatic Mission To Alderaan,{{R|pc}}{{R|t8}}{{R|slack2}} "
            "a year after his Hall of Fame induction at the [[2025 World Championship]].{{R|wc25}} "
            "Fred also won the Friday team tournament with [[Phil Aasen]].{{R|team}}")
    res = ("== Results ==\n\nFinal Top 8 order and Sunday (Top 8) decks as published.{{R|pc}}\n\n" + table('Place', t['Top 8']) +
           "\n\n=== Top 8 bracket ===\n\n"
           "The main event was eight Swiss games on Saturday 24 October (strength-of-schedule tiebreak), then a Top 8 of match play on Sunday with 1:15 games. "
           "Quarterfinal pairings were drawn at random, top four against bottom four; the higher seed chose which side to play first, and the bracket was re-seeded "
           "to the Day 1 standings after the quarterfinals.{{R|sched}}\n\n"
           "'''Day 1 seeds''': 1 [[Greg Shaw]] 8–0; 2 [[Drew Lichtenstein]] 7–1; 3 Desai 6–2; 4 [[Joe Horbey]] 6–2; 5 [[Joe Olson]] 6–2; 6 [[Dennis Reinhardt]] 6–2; "
           "7 Fred 6–2; 8 [[Bryan Mischke]] 6–2.{{R|t8}} Mischke and [[Chris Wirfs]] (9th, 6–2) played a game for the eighth seat; its result was not posted, "
           "but Mischke made the Top 8 and Wirfs is listed 9th.{{R|t8}}{{R|pc}}\n\n"
           "The organizer posted one game of each match; the second games and the match totals were not posted. "
           "Margins are differentials; lost piles in brackets.{{R|t8}}\n"
           "* '''Quarterfinals:''' Desai (Dark) def. Reinhardt by 20 (19–44) in the posted game, and Desai advanced. "
           "Lichtenstein (Light) def. Olson by 19 (14–31), and Lichtenstein advanced. "
           "Shaw (Dark) def. Mischke by 3 (34–33), and Shaw advanced. "
           "Horbey (Dark) def. Fred by 13 (27–35), but Fred advanced.{{R|t8}}\n"
           "* '''Semifinals''' (re-seeded): Desai (Dark) def. Lichtenstein by 20 (21–36), and Desai advanced. "
           "Shaw (Light) def. Fred by 9 (18–28), but Fred advanced; his game 2 against Shaw is in the YouTube playlist.{{R|t8}}{{R|yt}}\n"
           "* '''Final:''' Fred (Light) def. Desai by 5 (28–46) in game 1. Game 2 was not posted. Fred won the title.{{R|t8}}{{R|slack2}}\n\n"
           "The Top 8 was streamed live on twitch.tv/swccgpc and twitch.tv/tashi_station_,{{R|t8}} with [[Dan Tartaglione]] and [[Garrett Larson]] as the stream team.{{R|photo}} "
           "Eleven games from the weekend were posted to a YouTube playlist; the final is not among them.{{R|yt}}")
    d1 = ("== Day 1 ==\n\nDay 1 standings and lists as published.{{R|pc}}\n\n" + table('Day 1', t['Day 1']))
    side = ("== Side events ==\n\n"
            "* '''Team tournament''' (Friday 23 October, teams of two, one player on each side, three games, cumulative differential; 11 teams): won by The Unholy Alliance, "
            "[[Phil Aasen]] and [[Brian Fred]], with 12 points (+92) without dropping a game, for the mini obelisk trophies. "
            "Hong Kong Danger Duo were second (8, +39) and Team S&C third (8, +9).{{R|sched}}{{R|team}}\n"
            "* '''Consolation''' (Sunday, six Swiss games, about 27 players): won by [[Patrick Johnson|Pat Johnson]], undefeated, ahead of [[Carson Stockman]], "
            "[[Sam Tashima]] and [[AJ Hatoum]].{{R|conso}}\n"
            "* '''Other events:''' a Friday Cube event (\"Throdo's Cube Spectacular!\") and Retro (Premiere–Death Star II) events were also scheduled; their results were not posted on the forum.{{R|sched}}{{R|prize}}\n"
            "* '''Holotheatre:''' Brian Fred joined deadbody and DTartagOne for a special [[Holotheatre]] episode on twitch.tv/swccgpc on Monday 2 November 2026.{{R|slack3}}")
    gal = "== Photographs ==\n\n" + gallery([(p['suggested_wiki_file_name'], p['description']) for p in picks] +
                                           [('2026 World Championship Team Tournament Obelisks.jpg', 'The Unholy Alliance (Phil Aasen and Brian Fred) with their team tournament obelisks.')])
    live = open('live_2026.wiki').read()
    sec = dict(sections(live))
    src = ("== Sources ==\n\n" + sec['Sources'].strip() + "\n"
           + '\n'.join('* ' + fr(n, ttl) for n, ttl in [(86982, 'Schedule of Events'), (86751, 'forum topic 86751 (venue details)'), (87034, 'Team Tournament updates'),
                                                         (87038, 'Consolation Tournament Pairings'), (87025, 'Prize Support'), (87044, 'Congrats BFred')])
           + "\n* [https://www.youtube.com/playlist?list=PLTVa1kgaeLRA 2026 World Championship YouTube playlist]"
           + "\n* Players Committee Slack, #announcements, 24–27 October 2026")
    body = '\n\n'.join([ib, lead, res, d1, side, gal, '== See also ==\n\n' + see_also(2026), src, FOOT, cats(2026)])
    return body, d

YEARS = {2024: y2024, 2025: y2025, 2026: y2026}
