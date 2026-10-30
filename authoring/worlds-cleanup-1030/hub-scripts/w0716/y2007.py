from lib import *
y=2007
t=open(f'live_{y}.wiki').read()
defs=dict(COMMON); defs.update(refdefs(t)); defs['awards']=COMMON['awards']
d3=table_rows(get(t,'Day 3'))
R=lambda n: deckrow_by_player(d3,n)
def res(place,n,note=''):
    r=R(n); return [place,r[0]+note,r[1],r[2]]
hon=R('Mike Honsho')
results=[res('1','Jonny Chu'),res('2','Justin Desai'),res('3–4','Tom Hollingworth'),
 ['3–4','[[Brian Fred]]<ref name="f75427-1300387" />','—','—'],
 res('5–8','Brad Eier'),res('5–8','Angelo Consoli'),res('5–8','Brian Hunter'),res('5–8','Mike Gemme')]
ib=infobox(y,None,None,'5–7 October 2007<ref name="tdl" />','Chicago, Illinois, USA<ref name="awards" />',
 '[[Premiere - Original VS13]]','45<ref name="wp" />','[[Jonny Chu]]','[[Justin Desai]]',2006,2008)
lead=f"""'''2007 World Championship''' was the 12th Star Wars CCG World Championship, run by the [[Players Committee]] in Chicago, Illinois, on 5–7 October 2007. The constructed pool was [[Premiere - Original VS13]].<ref name="tdl" /><ref name="awards" /> 45 players took part.<ref name="wp" /> [[Jonny Chu]] defeated [[Justin Desai]] in the final, playing Bring Him Before Me and Plead My Case To The Senate on Day 3, and became the first player to win two World Championships (2003 and 2007).<ref name="awards" /><ref name="f75427-1300387" /> Desai's team, the [[Kashyyyk Train of Dominance]], won the team championship.<ref name="awards" /> The Day 1, Day 2, Day 3 and Team decklists were published as PDFs.<ref name="tdl" />"""
bracket=shorten_refs(get(t,'Top 8 bracket')).strip().replace('where the Day 3 list above has Mike Honsho','where the Day 3 sheets have Mike Honsho (his lists are under [[#Other published decklists|Other published decklists]])')
d2=shorten_refs(get(t,'Day 2')).strip()
d1=get(t,'Day 1').strip()
team=shorten_refs(get(t,'Team')).strip()
other=mk_table('! Stage !! Player !! Dark !! Light',[['Day 3',hon[0],hon[1],hon[2]]])
gallery='''<gallery>
File:Angelo Consoli 2007 World Championship interview.jpg|[[Angelo Consoli]] interviewed at the 2007 World Championship
File:Justin Carulli 2007 World Championship interview.jpg|[[Justin Carulli]] interviewed at the 2007 World Championship
File:JW Millet 2007 World Championship interview.jpg|[[JW Millet]] interviewed at the 2007 World Championship
File:Phil Johnson 2007 World Championship interview.jpg|[[Phil Johnson]] interviewed at the 2007 World Championship
File:Thomas Whaley 2007 World Championship interview.jpg|[[Thomas Whaley]] interviewed at the 2007 World Championship
</gallery>'''
src=merge_sources(bullets(get(t,'Sources')),[SRC_WP])
page=f"""{ib}
{lead}

== Results ==

Places follow the published Top 8 bracket; semifinal and quarterfinal losers are shown as ties. Decks are the Day 3 lists.

{mk_table('! Place !! Player !! Dark !! Light',results)}

=== Top 8 bracket ===

{bracket}

== Day 2 ==

{d2}

== Day 1 ==

{d1}

== Other published decklists ==

[[Mike Honsho]]'s Day 3 sheets are in the Day 3 PDF, but he is not in the published Top 8 bracket, which has [[Brian Fred]] in that seat.<ref name="f75427-1300387" />

{other}

== Side events ==

=== Team tournament ===

The [[Kashyyyk Train of Dominance]], [[Justin Desai]]'s team, won the 2007 Worlds team championship.<ref name="awards" /> {team}

=== Consolation event ===

A consolation event was held; some of the [[2007 World Championship interviews (transcript)|2007 interviews]] were filmed there. No results have been found.

== Photographs ==

{gallery}

== See also ==

* [[World Championships]]
* [[2006 World Championship]] · [[2008 World Championship]]
* [[Premiere - Original VS13]]
* [[2007 World Championship interviews (transcript)]]
* [[Championships]]
* [[Virtual Sets (2002-2009)]]
* [[Formats]]
* [[List of SWCCG tournaments]]

== Sources ==

{chr(10).join(src)}

{TAIL % y}"""
notes="""# 2007 World Championship — draft notes

Draft: hubs_draft/2007_World_Championship.wiki (live hub unchanged since the local copy; re-fetched 30 Oct 2026).

## What changed
- Standard infobox added (12th edition, PC, 5–7 Oct 2007, Chicago, VS13, 45 players, Chu def. Desai, 2006 · 2008). No champion photo exists, so the image row is omitted. Venue (hotel) not found.
- Lead rewritten: edition, field size, final, winning decks, Chu as first two-time champion, KToD team title.
- `== Format ==` bullet block dropped (its facts are in the infobox and lead).
- New `== Results ==` table in finish order from the forum bracket: 1 Chu, 2 Desai, 3–4 Hollingworth / Brian Fred, 5–8 Eier, Consoli, Hunter, Gemme. Day 3 deck links moved into it.
- Brian Fred row has no decks: the bracket names him, but the Day 3 sheets have Mike Honsho instead. Honsho's two Day 3 lists moved to `== Other published decklists ==`.
- Team table moved under `== Side events ==`; consolation event mentioned (sourced to the interviews page, which is itself sourced to the PC YouTube uploads).
- `== Photographs ==` gallery of the five 2007 interview stills already on the wiki.
- Categories: added [[Category:World Championships]].
- Person links that pointed at redirects now point at the person page (e.g. [[Michael Pistone|Mike Pistone]], [[Patrick Johnson|PMJ]]).

## Facts added (source)
- 45 players: Wikipedia SWCCG article (worlds_facts.json).
- Chu first to win two Worlds (2003, 2007): PC Awards page, Chu HoF blurb.
- KToD (Desai) won the 2007 and 2008 Worlds Team Championship: PC Awards page, Desai HoF blurb ("twice captured the Worlds Team Championship (2007, 2008)").
- Consolation event existed: [[2007 World Championship interviews (transcript)]] (filmed "at the consolation event").

## Deck pages
135 deck pages for 2007 (redirect titles excluded); all 135 linked exactly once (Results 14, Day 2 77, Day 1 12, Other 2, Team 30). Checked by script.

## Unresolved
- Brian Fred vs Mike Honsho in the eighth Day 3 seat.
- Venue hotel; Day 2 / Day 1 standings; team event composition.
"""
write(y,page,defs,notes)
