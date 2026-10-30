from lib import *
y=2013
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
d3sec=get(t,'Day 3'); d3=table_rows(d3sec)
def res(p,n):
    r=deckrow_by_player(d3,n); return [p,r[0],r[1] or '—',r[2] or '—']
results=[res('1','Justin Desai'),res('2','Reid Smith')]+[res('3–8',n) for n in ['Steve Baroni','Vikram Bali','Jonny Chu','Kevin Shannon','Emil Wallin']]
d3note=d3sec[d3sec.index('\n|}')+3:].strip()
ib=infobox(y,'Justin Desai 2013 Hall of Fame.jpg','Justin Desai, from the 2013 Hall of Fame class photo',
 '9–11 August 2013 (Day 1 9 August, Day 2 10 August, Day 3 11 August)<ref name="tdl" />','Boston, Massachusetts, USA<ref name="awards" />',
 '[[Premiere - Virtual Block 8.3]]','60<ref name="wp" />','[[Justin Desai]]','[[Reid Smith]]',2012,2014).replace('|280px]]','|130px]]')
lead="""'''2013 World Championship''' was the 18th Star Wars CCG World Championship, run by the [[Players Committee]] in Boston, Massachusetts, on 9–11 August 2013.<ref name="awards" /><ref name="tdl" /> The constructed pool was [[Premiere - Virtual Block 8.3]]. 60 players took part.<ref name="wp" /> [[Justin Desai]] defeated [[Reid Smith]] in the final, playing Imperial Occupation and It Is The Future You See (V) on Day 3.<ref name="awards" /> On 10 August, Day 2 of the event, the Players Committee enshrined its first Hall of Fame class: [[Jonny Chu]], [[Angelo Consoli]], Desai and [[Kevin Shannon]]; Desai won the title the next day.<ref name="awards" /> Decklists survive for all three days.<ref name="tdl" />"""
d2=get(t,'Day 2'); d1=get(t,'Day 1')
other=[['Day 1','[[Ross Littauer]]','—','[[2013 Worlds Day 1 Ross Littauer LS Diplomatic Mission To Alderaan|Diplomatic Mission To Alderaan]]']]
side="""=== Hall of Fame ===

The inaugural Players Committee Hall of Fame class was enshrined on 10 August 2013, during the World Championship: [[Jonny Chu]], [[Angelo Consoli]], [[Justin Desai]] and [[Kevin Shannon]].<ref name="awards" /> Hall of Famers receive an automatic berth into Day 2 of every later World Championship.<ref name="awards" />"""
gallery=['File:Justin Desai 2013 Hall of Fame.jpg|[[Justin Desai]], 2013 World Champion, enshrined in the Hall of Fame on 10 August 2013',
 'File:Kevin Shannon 2013 Hall of Fame.jpg|[[Kevin Shannon]], Hall of Fame class of 2013',
 'File:Angelo Consoli 2013 Hall of Fame.jpg|[[Angelo Consoli]], Hall of Fame class of 2013',
 "File:Community card Jonny C 2013 Hall of Fame.jpg|Community card ''Jonny C'' (2013 Hall of Fame)",
 "File:Community card Justin D 2013 Hall of Fame.jpg|Community card ''Justin D'' (2013 Hall of Fame)",
 "File:Community card Kevin S 2013 Hall of Fame.jpg|Community card ''Kevin S'' (2013 Hall of Fame)",
 "File:Community card Angelo C 2013 Hall of Fame.jpg|Community card ''Angelo C'' (2013 Hall of Fame)"]
src=merge_sources(bullets(get(t,'Sources')),[SRC_AWARDS,SRC_WP])
intro=("Desai and Smith are placed from the published final.<ref name=\"awards\" /> The order of the other Day 3 players has not been found, so they are shown as 3–8. "
 "Only seven Day 3 players are known; the eighth has not been identified. Decks are the Day 3 lists. "+d3note)
page=assemble(y,ib,lead,intro,results,None,[('Day 2',d2),('Day 1',d1)],
 "[[Ross Littauer]] has two Day 1 Light Side pages; the Day 1 table links Infiltration, and this second list is placed here.",other,side,gallery,
 see(y,'Premiere - Virtual Block 8.3',['[[Formats]]']),src)
notes="""# 2013 World Championship — draft notes

Draft: hubs_draft/2013_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox (18th edition, PC, 9–11 Aug 2013 with day dates, Boston MA, [[Premiere - Virtual Block 8.3]], 60 players, Desai def. Reid Smith, 2012 · 2014). Image: File:Justin Desai 2013 Hall of Fame.jpg at 130px (the file is only 130×390, so 280px would upscale it).
- Blank Site and Winner filled (Bill's correction / worlds_issues.md): champion Justin Desai, runner-up Reid Smith, Boston.
- Lead rewritten; the old wording "held … in [[Legacy Open]]" removed. [[Legacy Open]] replaced by [[Premiere - Virtual Block 8.3]] (pool_map.tsv) everywhere.
- `== Results ==`: 1 Desai, 2 R. Smith, 3–8 Baroni, Bali, Chu, Shannon, Wallin (order unknown); the eighth Day 3 player is not identified (said in the text). Vikram Bali's blank Dark cell now shows "—".
- `== Side events ==` → Hall of Fame: inaugural class (Chu, Consoli, Desai, Shannon) enshrined 10 Aug 2013 (Day 2), plus the Day 2 berth rule.
- `== Photographs ==`: the three 2013 HoF portraits and four 2013 HoF community cards already on the wiki. The class group photo (HOF-Inagural-Class) is not on the wiki; there is no Jonny Chu 2013 HoF crop.
- The unlisted deck [[2013 Worlds Day 1 Ross Littauer LS Diplomatic Mission To Alderaan]] added under `== Other published decklists ==`.
- Added Awards and Wikipedia to Sources; [[Category:World Championships]] added.

## Facts added (source)
- Champion, runner-up, Boston: PC Awards page champions list (and Bill's correction).
- 60 players: Wikipedia.
- HoF class and 10 Aug 2013 date; Day 2 berth for Hall of Famers: PC Awards page.

## Deck pages
143 deck pages; all linked exactly once (checked). Was 142 on the live hub (Ross Littauer DMTA unlinked).

## Unresolved
- The eighth Day 3 player; Top 8 bracket and places 3–8; venue (hotel).
- Ross Littauer has two Day 1 Light pages (Infiltration, Diplomatic Mission To Alderaan) — one may be a transcription duplicate or a Day 2 list; check the Day 1 PDF.
- Pool: legacy_notes.md lists a "9.1 Preview" set first headlined 9 Jul 2013 and used at this Worlds; pool_map.tsv says 8.3, which I followed.
"""
write(y,page,defs,notes)
