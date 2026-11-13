from concurrent.futures import ThreadPoolExecutor
import hashlib,json,re
from pathlib import Path
import requests
root=Path(__file__).parent
drafts=json.loads((root/'drafts.json').read_bytes())
receipts=root/'cards-receipts.jsonl'
done={r['title'] for r in map(json.loads,receipts.read_text(encoding='utf8').splitlines())} if receipts.exists() else set()
prior={r['title']:r for r in json.loads((root/'cards-packet.json').read_bytes())} if (root/'cards-packet.json').exists() else {}
remaining=[r for r in drafts if r['title'] not in done]
def get(rows):
    titles='|'.join(r['title'] for r in rows)
    common=dict(action='query',format='json',formatversion=2,titles=titles,prop='revisions',rvprop='ids|timestamp|content',rvslots='main')
    def request(args):
        r=requests.get('https://wiki.swccg.com/api.php',params=args,timeout=60);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
    full={p['title']:p for p in request(common)}
    lead={p['title']:p for p in request(dict(common,rvsection=0))}
    result=[]
    for row in rows:
        t=row['title'];rev=full[t]['revisions'][0];text=rev['slots']['main']['content']
        if rev['revid']!=row['before_revid'] or hashlib.sha256(text.encode()).hexdigest()!=row['before_sha256']:
            result.append(dict(title=t,conflict=True,page=full[t]));continue
        section=0 if lead[t]['revisions'][0]['slots']['main']['content']==text else None
        result.append(dict(row,section=section,summary='Use the shared Card infobox; preserve native text, translations and sources (#287)'))
    return result
out=[prior[t] for t in done]
with ThreadPoolExecutor(max_workers=3) as pool:
    for rows in pool.map(get,[remaining[i:i+40] for i in range(0,len(remaining),40)]):out+=rows
samples=json.loads((root/'sample-titles.json').read_bytes());out.sort(key=lambda r:(r['title'] not in samples,r['title']))
conflicts=[r for r in out if r.get('conflict')]
if conflicts:
    (root/'concurrent-edits.json').write_text(json.dumps(conflicts,ensure_ascii=False,indent=2),encoding='utf8')
    print('Rebase required:',[r['title'] for r in conflicts]);raise SystemExit(2)
(root/'cards-packet.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print('Concurrent-edit guards passed:',len(out),'; atomic whole-source replacements required:',sum(r['section'] is None for r in out))
if done:raise SystemExit(0)
heads=json.loads((root/'heads-before.json').read_bytes());controls=[]
for title,file in [('Template:Card','template-draft.wiki'),('Template:Card/doc','Template-Card-doc.wiki')]:
    rev=heads[title]['revisions'][0];text=(root/file).read_text(encoding='utf8');old=rev['slots']['main']['content']
    row=dict(title=title,text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Support Japanese printed text, translations and printing metadata in the shared card template (#287)')
    if title.endswith('/doc'):
        extension=(root/'doc-section.wiki').read_text(encoding='utf8').strip()
        row.update(section='new',sectiontitle='Language and printing metadata',section_text=extension,text=old.rstrip()+'\n\n== Language and printing metadata ==\n'+extension+'\n')
    controls.append(row)
(root/'production-packet.json').write_text(json.dumps(controls,ensure_ascii=False,indent=2),encoding='utf8')
