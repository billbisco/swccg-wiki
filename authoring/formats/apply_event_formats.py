"""Add a Format bullet to event pages that lack one, from drafts/event_formats.json (resolved entries only).
Writes pages into a package dir given as argv[1] (appends to its y-*.tsv)."""
import json,re,sys
from pathlib import Path
pk=Path(sys.argv[1]); tsv=next(pk.glob('y-*.tsv'))
H=json.load(open('/tmp/claude-0/fmt/events.json'))['hubs']
done=0
for x in json.load(open(Path(__file__).with_name('drafts')/'event_formats.json')):
    f=x.get('format'); ev=x['event']; t=H.get(ev)
    if not f or not t: continue
    if re.search(r"^\* '''(?:Format|Environment):'''\s*\S", t, re.M) and f"[[{f}" in t: continue
    line=f"* '''Format:''' [[{f}]] (from the card pool legal on the event date)" if x['basis'].startswith('date') else f"* '''Format:''' [[{f}]]"
    if re.search(r"^\* '''(?:Format|Environment):'''\s*$", t, re.M):
        t=re.sub(r"^\* '''(?:Format|Environment):'''\s*$", line, t, count=1, flags=re.M)
    elif re.search(r"^== (Format|Details|Event|Info)[^=]*==\s*$", t, re.M):  # bullets live in a Format/Details section
        sec=re.search(r"^== (Format|Details|Event|Info)[^=]*==\s*$", t, re.M)
        tl=re.search(r"^\* '''Type:'''[^\n]*$", t[sec.end():], re.M)
        k=sec.end()+tl.end() if tl else sec.end()
        t=t[:k]+("\n"+line if tl else "\n\n"+line)+t[k:]
    else:
        m=list(re.finditer(r"^\* '''[^']+:'''.*$", t.split('\n==')[0], re.M))
        if m: t=t[:m[-1].end()]+"\n"+line+t[m[-1].end():]
        else:
            k=t.find('\n\n'); t=t[:k]+"\n\n"+line+t[k:]
    fn='pages/'+ev.replace(' ','_').replace('/','%2F')+'.wiki'
    (pk/fn).write_text(t,encoding='utf-8'); open(tsv,'a',encoding='utf-8').write(f"{ev}\t{fn}\n"); done+=1
print('event pages given a format:',done)
