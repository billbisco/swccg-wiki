import sys; sys.path.insert(0,'/home/claude/swccg-wiki/authoring')
import tr_build as T, decktech_batch as db
from pathlib import Path
P=Path('/tmp/claude-0/tr-batch-01pkg'); A=Path('/home/claude/swccg-wiki/authoring')
def fn(t): return 'pages/'+t.replace(' ','_')+'.wiki'
def rd(t): return (P/fn(t)).read_text(encoding='utf-8')
def wr(t,s,new=False):
    (P/fn(t)).write_text(s,encoding='utf-8')
    if new:
        for f in [P/'y-tr-batch-01.tsv',A/'y-tr-batch-01.tsv']:
            open(f,'a',encoding='utf-8').write(f"{t}\t{fn(t)}\n")
def d(i): return T.load('decktech/'+i)
def R(i): return f'<ref name="tr-{i}" />'
def Rf(i): return T.ref(d(i))
def tl(i): return T.page_title(d(i))
def addrows(t,rows,anchor='\n|}',after_head='== Results',lead_old=None,lead_new=None):
    s=rd(t); k=s.find(anchor,s.find(after_head)); assert k>0,t
    s=s[:k]+''.join('\n|-\n'+r for r in rows)+s[k:]
    if lead_old: assert lead_old in s,(t,lead_old); s=s.replace(lead_old,lead_new,1)
    wr(t,s)

# Bochum
addrows('2000 Bochum Grand Slam',[
 f"| 2nd || [[Martin Schumacher]]{Rf('d220')}",
 f"| 3rd || Jan-Willem Sipkes{R('d220')}",
 f"| about 18th || [[Koen Meijssen]]{R('d220')}",
 f"| about 20th || [[Johan van der Meer]]{R('d220')}"],
 lead_old='== Results ==\n', lead_new="== Results ==\n\nPlaces below 1st come from [[Koen Meijssen]]'s tournament report ([["+tl('d220')+"|report]]), which gives 66 players; Meijssen gives his own and van der Meer's places as approximate. Schumacher lost the final to Winkelhaus.\n")
# Boston
s=rd('2000 Boston Grand Slam')
s=s.replace('\n|}', f"\n|-\n| 11th of 40 || [[Paul Maholick]]{Rf('d494')}\n|}}",1)
k=s.find('\n== ',s.find('== Results')+5)
s=s[:k]+"\n\n=== Location discrepancy ===\n[[Paul Maholick]]'s tournament report ([["+tl('d494')+"|report]]) places this Grand Slam in Milford, Massachusetts, on 8 April 2000, with 40 players."+R('d494')+" Decipher's Grand Slam 2000 list names it Boston.<ref name=\"gs00\" /> It is the only Massachusetts Grand Slam of April 2000, so the report is filed here; until there is more evidence the wiki keeps Decipher's name."+s[k:]
wr('2000 Boston Grand Slam',s)
# Atlanta DPC
addrows('2001 Atlanta DPC',[
 f"| 5–3 record || [[Matt Mathison]]{Rf('d2816')} || — || —",
 f"| 5–3 record || [[John Camp]]{R('d2816')} || — || —",
 f"| 5–3 record || Chris Work{R('d2816')} || — || —"])
# Vegas DPC
addrows('2002 Vegas DPC',[f"| 3–3 record || [[Matt Lush]]{Rf('d3660')} || — || —"],after_head='== Published lists')
# Houston DPC
addrows('2002 Houston DPC',[
 f"| Top 4 || Chris McClure{Rf('d3841')} || — || —",
 f"| Top 4 || Thomas McGee{R('d3841')} || — || —",
 f"| 3–3 record || [[Jacob Taylor]]{R('d3841')} || — || —"],after_head='== Published lists')

# New hub: 2000 Alabama State Championship
a=d('d642')
rows=[("1st","[[Andy McClure]]"),("2nd","Stephen Lanza"),("3rd","[[Rob Ronnlund]]"),("4th","Kyle Matusevic"),("5th","Chris McClure"),("6th","Barry Dekale (the report adds a question mark)"),("7th","[[Chris Bentley]]"),("8th","Clay Wilburn")]
tab="\n".join(f"|-\n| {f} || {p}{Rf('d642') if i==0 else R('d642')}" for i,(f,p) in enumerate(rows))
wr('2000 Alabama State Championship',f"""'''2000 Alabama State Championship''' was a Star Wars CCG state championship held in Birmingham, Alabama, on 29 April 2000. [[Andy McClure]] won it, going 5–1 with a Dark Scum And Villainy ISB deck and a Light Profit deck.

* '''Date:''' 29 April 2000
* '''Site:''' Birmingham, Alabama
* '''Format:''' [[Premiere - Endor]]
* '''Winner:''' [[Andy McClure]]

== Results ==

Results below come from Andy McClure's tournament report, which lists the top eight.

{{| class="wikitable"
! Finish !! Player
{tab}
|}}

McClure won again at the [[2001 Alabama State Championship]].

== Tournament reports ==

Players' own reports from this event.

{T.report_bullet(a,True)}

== See also ==

* [[2001 Alabama State Championship]]
* [[List of SWCCG tournaments]]
* [[Tournament reports]]

== References ==
<references />

[[Category:Tournaments]]
[[Category:2000]]
""",new=True)
# New hub: 2001 New York State Championship
n=d('d2349')
wr('2001 New York State Championship',f"""'''2001 New York State Championship''' was a Star Wars CCG state championship played on 19 May 2001 at the Altered States store in New York.{Rf('d2349')} [[Brian Terwilliger]] and a player named Pete played the final; the report that records the event does not say who won.

* '''Date:''' 19 May 2001
* '''Site:''' Altered States, New York
* '''Format:''' [[Premiere - Reflections II]]
* '''Winner:''' unknown

== Results ==

Results below come from Josh Paterniti's tournament report.

{{| class="wikitable"
! Finish !! Player
|-
| finalist || [[Brian Terwilliger]]{R('d2349')}
|-
| finalist || Pete (surname not given){R('d2349')}
|-
| 5–1, 10 (+76); missed the final on differential || [[Josh Paterniti]]{R('d2349')}
|}}

== Tournament reports ==

Players' own reports from this event.

{T.report_bullet(n,True)}

== See also ==

* [[List of SWCCG tournaments]]
* [[Tournament reports]]

== References ==
<references />

[[Category:Tournaments]]
[[Category:2001]]
""",new=True)
# List of SWCCG tournaments
L=db.live_text("List of SWCCG tournaments")
k=L.find("| 2001-05 || [[2001 Tulsa Open]]"); assert k>0
L=L[:k]+"| 2001-05 || [[2001 New York State Championship]] || 19 May 2001 || Altered States, New York || [[Premiere - Reflections II]] || —\n|-\n"+L[k:]
k=L.find("| 2000-04 || [[2000 Virginia State Championship]]"); assert k>0
L=L[:k]+"| 2000-04 || [[2000 Alabama State Championship]] || 29 April 2000 || Birmingham, Alabama || [[Premiere - Endor]] || [[Andy McClure]]\n|-\n"+L[k:]
wr("List of SWCCG tournaments",L,new=True)
print('ok')
