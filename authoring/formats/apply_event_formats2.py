"""Apply the researched entries of drafts/event_formats.json (those with refs / format_text / discrepancy) to event pages.
python3 apply_event_formats2.py PKGDIR"""
import json,re,sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import tr_build as T
pk=Path(sys.argv[1]); (pk/'pages').mkdir(parents=True,exist_ok=True); tsv=pk/f"y-{pk.name.replace('pkg','')}.tsv"
H=json.load(open('/tmp/claude-0/fmt/events.json'))['hubs']
rows=[]
def refs_for(t,refs):
    out=''
    for r in refs:
        n=re.search(r'<ref name="([^"]+)"',r)
        if n and (f'<ref name="{n.group(1)}">' in t or f'<ref name="{n.group(1)}" />' in out or f'<ref name="{n.group(1)}">' in out):
            out+=f'<ref name="{n.group(1)}" />'
        else: out+=r
    return out
for x in json.load(open(Path(__file__).with_name('drafts')/'event_formats.json')):
    if not (x.get('refs') or x.get('format_text') or x.get('discrepancy')): continue
    ev=x['event']; t=H.get(ev)
    if not t: print('MISSING',ev); continue
    val=f"[[{x['format']}]]" if x.get('format') else x['format_text']
    line=f"* '''Format:''' {val}{refs_for(t,x.get('refs',[]))}"
    m=re.search(r"^\* '''(?:Format|Environment):'''([^\n]*)$", t, re.M)
    if m and m.group(1).strip():
        print('HAS FORMAT already, skipped:',ev, m.group(1)[:60]); continue
    if m: t=t[:m.start()]+line+t[m.end():]
    elif re.search(r"^== (Format|Details|Event|Info)[^=]*==\s*$", t, re.M):
        sec=re.search(r"^== (Format|Details|Event|Info)[^=]*==\s*$", t, re.M)
        tl=re.search(r"^\* '''Type:'''[^\n]*$", t[sec.end():], re.M)
        k=sec.end()+tl.end() if tl else sec.end()
        t=t[:k]+("\n"+line if tl else "\n\n"+line)+t[k:]
    else:
        lead=t.split('\n==')[0]
        mm=list(re.finditer(r"^\* '''[^']+:'''.*$", lead, re.M))
        if mm: t=t[:mm[-1].end()]+"\n"+line+t[mm[-1].end():]
        else:
            k=t.find('\n\n'); t=t[:k]+"\n\n"+line+t[k:]
    if x.get('discrepancy'):
        r=x.get('refs',[])
        n=re.search(r'<ref name="([^"]+)"',r[0]).group(1) if r else None
        t=T.add_section(t,"Discrepancies",[f"* {x['discrepancy']}"+(f'<ref name="{n}" />' if n else '')],
                        "Where sources disagree, this page keeps the best-supported record and notes the difference here.")
    fn='pages/'+ev.replace(' ','_').replace('/','%2F')+'.wiki'
    (pk/fn).write_text(t,encoding='utf-8'); rows.append(f"{ev}\t{fn}")
open(tsv,'a',encoding='utf-8').write('\n'.join(rows)+'\n'); print(len(rows),'pages ->',tsv)
