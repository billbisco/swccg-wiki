"""2017-2020 hubs."""
from lib import *

def T(y):
    return get_tables(open(f'live_{y}.wiki').read())

PRE17 = ('[https://www.starwarsccg.org/world-championship-2017-in-minnesota/ World Championship 2017 in Minnesota], '
         'starwarsccg.org (pre-event announcement)')

def y2017():
    t = T(2017)
    d = dict(
        pc='[https://www.starwarsccg.org/2017-world-championships/ 2017 World Championship], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261013155910/https://swccg.com/snapshots/pc/2017-world-championships.html Internet Archive].',
        awards=AWARDS, pre=PRE17, wp=WIKIPEDIA)
    ib = infobox(2017, 'Community card Phil A 2017 World Champion.jpg',
                 'Community card depicting Phil Aasen as 2017 World Champion',
                 '10–13 August 2017{{R|pre}}{{R|pc}}',
                 'Bloomington, Minnesota, USA (Minneapolis area)',
                 '[[Open]]', '59 (55 Day 2 finishers and 4 drops){{R|pc}}', '[[Phil Aasen]]', '[[Jonny Chu]]{{R|awards}}')
    lead = ("The '''2017 World Championship''' was the 22nd Star Wars CCG World Championship and the [[Players Committee]]'s "
            "World Championship for 2017, held in Bloomington, Minnesota, from 10 to 13 August 2017.{{R|pre}}{{R|pc}} "
            "The Players Committee awards page gives the site as Minneapolis, MN; Bloomington is a suburb of Minneapolis.{{R|awards}}{{R|wp}} "
            "Fifty-nine players' constructed pairs were published for Day 2 (55 finishers and four drops).{{R|pc}} "
            "[[Phil Aasen]] won the title, defeating [[Jonny Chu]] in the final,{{R|awards}} with Endor Operations and Combat Preparedness (V) on Day 3.{{R|pc}} "
            "[[Mark Walseth]] was enshrined in the Players Committee Hall of Fame on 12 August 2017, during the event weekend.{{R|awards}}")
    res = ("== Results ==\n\nFinal Top 8 (Day 3) order and decks as published.{{R|pc}} The bracket and game scores are not in the published decklist post.\n\n"
           + table('Place', t['Day 3']))
    d2 = ("== Day 2 ==\n\nThe Swiss main event, labelled Day 2 in the published list titles, in the published standings order.{{R|pc}}\n\n"
          + table('Day 2', t['Day 2']))
    other = ("== Other published decklists ==\n\nPublished pairs of the four players listed as drops.{{R|pc}}\n\n"
             + table('Stage', [['Day 2 (drop)'] + r[1:] for r in sorted(t['Drops'], key=lambda r: r[1].split('|')[0].split()[-1])]))
    side = ("== Side events ==\n\n* '''Hall of Fame:''' [[Mark Walseth]] was enshrined in the Players Committee Hall of Fame on 12 August 2017.{{R|awards}}")
    gal = "== Photographs ==\n\n" + gallery([
        ('Community card Mark W 2017 Hall of Fame.jpg', 'Community card depicting Mark Walseth (2017 Hall of Fame)'),
        ('Mark Walseth 2017 Hall of Fame.jpg', 'Mark Walseth, enshrined in the Hall of Fame on 12 August 2017')])
    src = ("== Sources ==\n\n"
           "* [https://www.starwarsccg.org/2017-world-championships/ 2017 World Championship], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261013155910/https://swccg.com/snapshots/pc/2017-world-championships.html Internet Archive]\n"
           f"* {PRE17}\n* {AWARDS}\n* {WIKIPEDIA}")
    body = '\n\n'.join([ib, lead, res, d2, other, side, gal, '== See also ==\n\n' + see_also(2017), src, FOOT, cats(2017)])
    return body, d

def y2018():
    t = T(2018)
    d = dict(pc='[https://www.starwarsccg.org/2018-world-championships/ 2018 World Championship], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261013160139/https://swccg.com/snapshots/pc/2018-world-championships.html Internet Archive].',
             awards=AWARDS)
    ib = infobox(2018, None, None, '4–7 October 2018{{R|pc}}', 'Morristown, New Jersey, USA{{R|awards}}', '[[Open]]',
                 '69 (Day 2){{R|pc}}', '[[Bastian Winkelhaus]]', '[[Tom Kelly]]{{R|awards}}')
    lead = ("The '''2018 World Championship''' was the 23rd Star Wars CCG World Championship and the [[Players Committee]]'s "
            "World Championship for 2018, held in Morristown, New Jersey, from 4 to 7 October 2018.{{R|pc}}{{R|awards}} "
            "Sixty-nine constructed pairs were published for Day 2.{{R|pc}} "
            "[[Bastian Winkelhaus]] defeated [[Tom Kelly]] to win the title,{{R|awards}} playing Agents Of Black Sun and Watch Your Step on Day 3.{{R|pc}} "
            "It was Winkelhaus's second World Championship, after 2001.{{R|awards}}")
    res = ("== Results ==\n\nFinal Top 8 (Day 3) order and decks as published.{{R|pc}} The bracket and game scores are not in the published decklist post.\n\n"
           + table('Place', t['Day 3']))
    d2 = ("== Day 2 ==\n\nThe Swiss main event, labelled Day 2 in the published list titles, in the published standings order.{{R|pc}}\n\n"
          + table('Day 2', t['Day 2']))
    src = ("== Sources ==\n\n"
           "* [https://www.starwarsccg.org/2018-world-championships/ 2018 World Championship], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261013160139/https://swccg.com/snapshots/pc/2018-world-championships.html Internet Archive]\n"
           f"* {AWARDS}")
    body = '\n\n'.join([ib, lead, res, d2, '== See also ==\n\n' + see_also(2018), src, FOOT, cats(2018)])
    return body, d

def y2019():
    t = T(2019)
    d = dict(pc='[https://www.starwarsccg.org/2019-worlds/ 2019 World Championship], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261013160304/https://swccg.com/snapshots/pc/2019-worlds.html Internet Archive]',
             awards=AWARDS)
    ib = infobox(2019, 'Bastian Winkelhaus 2019 Hall of Fame.jpg',
                 'Bastian Winkelhaus, Hall of Fame photo from the PC awards page',
                 '20–22 September 2019{{R|pc}}', 'Bochum, Germany{{R|awards}}', '[[Open]]',
                 '69 (Day 2){{R|pc}}', '[[Bastian Winkelhaus]]', '[[Bryan Mischke]]{{R|awards}}')
    lead = ("The '''2019 World Championship''' was the 24th Star Wars CCG World Championship and the [[Players Committee]]'s "
            "World Championship for 2019, held in Bochum, Germany, from 20 to 22 September 2019.{{R|pc}}{{R|awards}} "
            "Sixty-nine constructed pairs were published for Day 2.{{R|pc}} "
            "[[Bastian Winkelhaus]] defeated [[Bryan Mischke]] in the Final Confrontation,{{R|pc}}{{R|awards}} playing Ralltiir Operations (V) and Old Allies on Day 3.{{R|pc}} "
            "He became the first player to win the World Championship in consecutive years and the first three-time champion (2001, 2018, 2019), "
            "and was enshrined in the Players Committee Hall of Fame on 20 September 2019, Day 1 of the event.{{R|awards}}")
    res = ("== Results ==\n\nFinal Top 8 (Day 3) order and decks as published.{{R|pc}} The bracket and game scores are not in the published decklist post.\n\n"
           + table('Place', t['Day 3']))
    d2 = ("== Day 2 ==\n\nThe Swiss main event, labelled Day 2 in the published list titles, in the published standings order.{{R|pc}}\n\n"
          + table('Day 2', t['Day 2']))
    side = "== Side events ==\n\n* '''Hall of Fame:''' [[Bastian Winkelhaus]] was enshrined in the Players Committee Hall of Fame on 20 September 2019. With it he became the only player enshrined in both the Decipher and the Players Committee Halls of Fame.{{R|awards}}"
    gal = "== Photographs ==\n\n" + gallery([
        ('Community card Bastian W 2019 Hall of Fame.jpg', 'Community card depicting Bastian Winkelhaus (2019 Hall of Fame)')])
    src = ("== Sources ==\n\n"
           "* [https://www.starwarsccg.org/2019-worlds/ 2019 World Championship], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261013160304/https://swccg.com/snapshots/pc/2019-worlds.html Internet Archive]\n"
           f"* {AWARDS}")
    body = '\n\n'.join([ib, lead, res, d2, side, gal, '== See also ==\n\n' + see_also(2019), src, FOOT, cats(2019)])
    return body, d

OLSON20 = ('[https://www.starwarsccg.org/joe-olson-wins-the-25th-star-wars-ccg-world-championship/ Joe Olson wins the 25th Star Wars CCG World Championship], '
           'starwarsccg.org. Preserved copy: [https://swccg.com/snapshots/pc/joe-olson-wins-the-25th-star-wars-ccg-world-championship.html swccg.com snapshot] (21 October 2026)')

def y2020():
    t = T(2020)
    d = dict(pc='[https://www.starwarsccg.org/2020-world-championships/ 2020 World Championships], starwarsccg.org', wrap=OLSON20, awards=AWARDS)
    ib = infobox(2020, 'Joe Olson 2020 Player of the Year.jpg', 'Joe Olson with his Players Committee trophy (2020 Player of the Year)',
                 'Day 1 5–6 December, Day 2 12 December, Day 3 13 December 2020{{R|pc}}',
                 'Online, on [[GEMP]] (play.starwarsccg.org){{R|wrap}}', '[[Open]]',
                 '97 (Day 1); 32 on Day 2; 8 on Day 3{{R|wrap}}', '[[Joe Olson]]', '[[Quirin Fürgut]]{{R|wrap}}')
    lead = ("The '''2020 World Championship''' was the 25th Star Wars CCG World Championship. Because of the COVID-19 pandemic the "
            "[[Players Committee]] moved it online to [[GEMP]], where it ran over four days in December 2020 and hosted 335 games.{{R|wrap}} "
            "Day 1 (5–6 December) was a six-game event with 97 players in four heats; the 32 players who went 4–2 or better played four more games on Day 2 (12 December); "
            "and the top eight played three rounds of match play on Day 3 (13 December).{{R|pc}}{{R|wrap}} "
            "[[Joe Olson]] defeated [[Quirin Fürgut]] in the Final Confrontation{{R|wrap}}{{R|awards}} with Hunt Down And Destroy The Jedi (V) and He Is The Chosen One.{{R|pc}}")
    res = ("== Results ==\n\nFinal Top 8 (Day 3) order and decks as published.{{R|wrap}}{{R|pc}}\n\n" + table('Place', t['Day 3']) +
           "\n\n=== Top 8 bracket ===\n\nDay 3 was three rounds of match play.{{R|wrap}} Only the final (Olson def. Fürgut) was reported; "
           "the quarterfinal and semifinal pairings and the game scores were not published. A replay of the Final Confrontation was posted on "
           "[https://www.youtube.com/watch?v=ixple-70RZE YouTube].{{R|wrap}}")
    d2 = ("== Day 2 ==\n\nThe 32 players who went 4–2 or better on Day 1, in the published standings order.{{R|pc}}{{R|wrap}}\n\n" + table('Day 2', t['Day 2']))
    d1 = ("== Day 1 ==\n\nEvery published Day 1 pair (unranked). The wrap-up gives 97 Day 1 players; the decklist post lists 98 Day 1 entries.{{R|wrap}}{{R|pc}}\n\n"
          + table('Day 1', t['Day 1']))
    src = ("== Sources ==\n\n"
           "* [https://www.starwarsccg.org/2020-world-championships/ 2020 World Championship], starwarsccg.org\n"
           f"* {OLSON20}\n"
           "* [https://www.starwarsccg.org/joe-olson-wins-the-25th-star-wars-ccg-world-championship/ GEMP importable decks] (linked from the PC article)\n"
           f"* {AWARDS}")
    body = '\n\n'.join([ib, lead, res, d2, d1, '== See also ==\n\n' + see_also(2020, ['[[GEMP]]']), src, FOOT, cats(2020)])
    return body, d

YEARS = {2017: y2017, 2018: y2018, 2019: y2019, 2020: y2020}
