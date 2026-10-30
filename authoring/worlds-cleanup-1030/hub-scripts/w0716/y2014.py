from lib import *
y=2014
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
defs['finals']='[https://forum.starwarsccg.org/viewtopic.php?t=55897 FINALS], forum.starwarsccg.org (24 August 2014). Preserved copy: [https://web.archive.org/web/20261022033406/https://swccg.com/snapshots/forum/t55897.html Internet Archive]'
defs['day3']='[https://forum.starwarsccg.org/viewtopic.php?t=55887 Day 3], forum.starwarsccg.org (raith, 23 August 2014). Preserved copy: [https://web.archive.org/web/20261022025229/https://swccg.com/snapshots/forum/t55887.html Internet Archive]'
defs['emil']='[https://forum.starwarsccg.org/viewtopic.php?t=55902 World Champions Decklists], forum.starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261022032443/https://swccg.com/snapshots/forum/t55902.html Internet Archive]'
defs['format']='[https://forum.starwarsccg.org/viewtopic.php?t=54863 Worlds Format (card pool)], forum.starwarsccg.org (Keith Brown, 6 June 2014; board "World Championships 2014 - Aug 21-24"). Preserved copy: [https://web.archive.org/web/20261021002720/https://swccg.com/snapshots/forum/t54863.html Internet Archive]'
defs['pdf']='[https://forum.starwarsccg.org/viewtopic.php?t=56104 worlds decklists], forum.starwarsccg.org (PDF scans, 6 September 2014)'
defs['reset']='[https://web.archive.org/web/20141020142523/http://www.starwarsccg.org:80/wp/reset-of-standard-format/ Reset of Standard Format], starwarsccg.org (25 July 2014), Internet Archive copy.'
defs['rb']='[https://www.starwarsccg.org/resources/tournament-decklists/ Tournament Decklists], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261020044435/https://swccg.com/snapshots/pc/tournament-decklists.html Internet Archive]'
d3sec=get(t,'Day 3'); d3=table_rows(d3sec)
def res(p,n): r=deckrow_by_player(d3,n,1); return [p,r[1],r[2],r[3]]
results=[res('1','Emil Wallin'),res('2','Brian Terwilliger'),res('3–4','Angelo Consoli'),res('3–4','Matthew Harrison-Trainor'),
 res('5–8','Matt Sokol'),res('5–8','Chris Terwilliger'),res('5–8','Greg Shaw'),res('5–8','Aaron Kingery')]
after=d3sec[d3sec.index('\n|}')+3:].strip()
ib=infobox(y,None,None,'21–24 August 2014<ref name="format" />','Toronto, Ontario, Canada<ref name="awards" />',
 '[[Premiere - Virtual Block 9.1]]','31<ref name="wp" />','[[Emil Wallin]]','[[Brian Terwilliger]]',2013,2015)
lead="""'''2014 World Championship''' was the 19th Star Wars CCG World Championship, run by the [[Players Committee]] in Toronto, Ontario, on 21–24 August 2014.<ref name="awards" /><ref name="format" /> 31 players took part.<ref name="wp" /> [[Emil Wallin]] defeated [[Brian Terwilliger]] (forum name Brian Twigg) in the final, playing Wookiee Slaving Operation and Mind What You Have Learned on Day 3, and became the third player to win two World Championships after [[Jonny Chu]] and [[Kevin Shannon]] (2012 and 2014).<ref name="finals" /><ref name="awards" /> The main event used [[Premiere - Virtual Block 9.1]]; the Players Committee had decided not to release Virtual Block 9.2 in its July 2014 form and announced a mini, 12-card set for Worlds instead.<ref name="reset" /> A separate [[2014 World Championship Reset Beta|Reset Beta]] side event tried out the post-reset card pool.<ref name="format" />"""
bracket="""Day 3 pairings as posted by raith (seeds in brackets):<ref name="day3" />

* Quarterfinals: (1) [[Emil Wallin]] def. (8) [[Aaron Kingery]] 2–0; (4) [[Angelo Consoli]] def. (5) [[Chris Terwilliger]]; (6) [[Brian Terwilliger]] def. (3) [[Matt Sokol]]; (2) [[Matthew Harrison-Trainor]] def. (7) [[Greg Shaw]]
* Semifinals: Emil Wallin def. Angelo Consoli; Brian Terwilliger def. Matthew Harrison-Trainor
* Final: Emil Wallin def. Brian Terwilliger

Only the Kingery quarterfinal score was posted; the other quarterfinal winners follow from the semifinal line-up.<ref name="day3" /> Live reports: Brian game 1 over MHT by 34 (Mon Cals over walkers); Angelo game 1 by 13 (A Stunning Move over Mind What You Have Learned).<ref name="day3" /> Final, game 1: Emil Light by 6 on time.<ref name="finals" /> The full final score was not posted."""
d2=shorten_refs(get(t,'Day 2')).replace('[[File:2014','[[:File:2014')
rb=table_rows(open('reset_beta.wiki').read().replace('[[Brian Bolletta]]','[[Brian Billetta|Brian Bolletta]]'))
side="""=== Reset Beta ===

The [[2014 World Championship Reset Beta]] was a side event played with the post-reset card pool. [[Keith Brown]] finished first.<ref name="rb" />

"""+mk_table('! Place !! Player !! Dark !! Light',rb)
old=bullets(get(t,'Sources'))
old=[b for b in old if 'hall-of-fame-awards' not in b]
src=merge_sources(old,[SRC_AWARDS,SRC_WP,
 '* [https://web.archive.org/web/20141020142523/http://www.starwarsccg.org:80/wp/reset-of-standard-format/ Reset of Standard Format], starwarsccg.org (25 July 2014), Internet Archive copy',
 '* [https://www.starwarsccg.org/resources/tournament-decklists/ Tournament Decklists], starwarsccg.org. Preserved copy: [https://web.archive.org/web/20261020044435/https://swccg.com/snapshots/pc/tournament-decklists.html Internet Archive]',
 '* Scans posted by JediJer on 6 September 2014 (several were upside down on the forum and are rotated 180° here):<ref name="pdf" /> [[:File:2014 Worlds Day 3.pdf]], [[:File:2014 Worlds Day 2 Part 1.pdf]], [[:File:2014 Worlds Day 2 Part 2.pdf]], [[:File:2014 Worlds Day 2 Part 3.pdf]], [[:File:2014 Worlds Chris Terwilliger Y4.pdf]] (Chris Terwilliger Day 3 Light, deck name Y4)'])
page=assemble(y,ib,lead,'Places follow the Day 3 bracket below; semifinal and quarterfinal losers are shown as ties. Decks are the Day 3 lists. '+after,
 results,bracket,[('Day 2',d2)],None,[],side,None,
 see(y,'Premiere - Virtual Block 9.1',['[[2014 World Championship Reset Beta]]','[[2014 Virtual Card Pool Reset]]','[[Formats]]']),src)
notes="""# 2014 World Championship — draft notes

Draft: hubs_draft/2014_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (19th edition, PC, 21–24 Aug 2014, Toronto, [[Premiere - Virtual Block 9.1]], 31 players, Wallin def. B. Terwilliger, 2013 · 2015). No photo exists for 2014.
- Format: [[Legacy Open]] replaced by [[Premiere - Virtual Block 9.1]] (pool_map.tsv) everywhere. One sentence added: the PC decided not to release 9.2 in its July 2014 form and announced a mini 12-card set for Worlds — cited to the 25 July 2014 "Reset of Standard Format" post (legacy_notes.md §1 and raw/art_all.txt: "9.2 will not be released in its current form. We are planning on releasing a mini, 12 card set for Worlds.").
  - Context not put on the page: the 6 June 2014 forum post (t=54863, already cited) said "The existing card pool (plus tentatively 9.2) will be legal for Worlds"; the PC slips page captured 24 Aug 2014 shows no 9.2 PDF. Whether the 11-card 9.2 PDF (14 Jul 2014) = the promised Worlds mini set, and was legal at Worlds, is still open.
- `== Results ==`: 1 Wallin, 2 B. Terwilliger, 3–4 Consoli / Harrison-Trainor, 5–8 Sokol, C. Terwilliger, Shaw, Kingery (from raith's Day 3 pairings + semifinal line-up + finals thread). The seed table became the Results table; seeds are in the bracket.
- `=== Top 8 bracket ===` rebuilt from the same posts (quarterfinal pairings by seed; winners other than Wallin–Kingery follow from the semifinal line-up — said on the page). Old `== Finals ==` text merged into it.
- `== Scans ==` list moved into Sources (file links now colon links, so the PDFs are not embedded); Day 2 scan links also changed to colon links.
- `== Side events ==` → Reset Beta: summary plus the 13-row results table copied from [[2014 World Championship Reset Beta]] so all 26 Reset Beta deck pages are linked from this hub (they were not before).
- Lead: Wallin's second title (2012, 2014) as the third two-time champion after Chu and Shannon.
- The dead `hall-of-fame-awards` ref/source replaced by the Awards page. See also trimmed of the long player list; standard links added.

## Facts added (source)
- 31 players: Wikipedia. Toronto, Ontario, Canada: PC Awards page. Third two-time champion: derived from the PC Awards champions list (Chu 2003/2007, Shannon 2008/2011, Wallin 2012/2014) — verify you are happy with a derived "third".
- Day 3 seeds and pairings: forum t=55887 (raith, 23 Aug 2014).

## Deck pages
103 deck pages for 2014 (77 main event + 26 Reset Beta); all linked exactly once (checked). Previously the 26 Reset Beta decks were not on this hub.

## Unresolved
- 9.2 legality at Worlds 2014 (see above). Venue (hotel). Chris Terwilliger's Day 2 Dark list was never published.
"""
write(y,page,defs,notes)
