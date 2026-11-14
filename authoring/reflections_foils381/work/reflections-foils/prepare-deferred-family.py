"""Keep live citations, reuse checked captures, queue the rest under Bill's exception."""
import json,re,sys
from pathlib import Path
sys.path.insert(0,'work/wiki-tools')
from publication_policy import lint
root=Path(__file__).parent;stage=sys.argv[1]
known={}
for f in [root/'old-citation-final.json',root/'remaining-verified-worker-receipts.json',*[f for f in root.glob('batch*-citation-final.json') if f.name!=stage+'-citation-final.json']]:
    if f.exists():known.update({u:r for u,r in json.loads(f.read_bytes()).items() if r.get('status')=='verified' and r.get('capture')})
urls=json.loads((root/(stage+'-citation-urls.json')).read_bytes());archives={u:known[u] for u in urls if u in known}
corrections={u:r['preserved_url'] for u,r in archives.items() if r.get('correction')}
def fix(text):
    for old,new in corrections.items():text=text.replace(old,new)
    def additions(part):return list(dict.fromkeys('Preserved copy: ['+r['capture']+' Internet Archive primary-source copy].' for u,r in archives.items() if corrections.get(u,u) in part and r['capture'] not in part))
    result=[]
    for part in re.split(r'(<ref\b[^>]*>.*?</ref>|<ref\b[^>]*/\s*>)',text,flags=re.S):
        if part.startswith('<ref'):
            add=additions(part);result.append(part[:-6].rstrip()+' '+' '.join(add)+'</ref>' if add and part.endswith('</ref>') else part)
        else:
            for line in part.splitlines(keepends=True):
                end='\n' if line.endswith('\n') else '';body=line[:-1] if end else line;add=additions(body);result.append(body+(' '+' '.join(add) if add else '')+end)
    return ''.join(result)
rows=json.loads((root/(stage+'-family-packet.json')).read_bytes());report=[]
for row in rows:
    old=row['text'];row['text']=fix(old)
    row['text']=row['text'].replace('== Notes ==\n* This card has published mistakes listed on the [[Remaster changes list]]','== Remaster changes ==\n* This card has published mistakes listed on the [[Remaster changes list]]')
    if re.search(r'^==[^=]',row['text'],re.M):row.update(section=None,atomic_reason='Navigation and citation/heading repairs span sections; current revision/hash/timestamp guards retain all other text')
    flags=lint(row['text'],row['title'])[0];assert not flags,(row['title'],flags)
    report.append(dict(title=row['title'],non_archive_flags=flags,archive_policy='explicit user-authorized queue; unresolved citations remain live and unaltered'))
for suffix,value in [('family-final-packet',rows),('family-final-lint',report),('citation-final',archives),('citation-corrections',corrections)]:
    (root/(stage+'-'+suffix+'.json')).write_text(json.dumps(value,ensure_ascii=False,indent=2),encoding='utf8')
print(len(rows),'family edits; all non-archive checks pass;',len(urls)-len(archives),'citation URLs deferred, never falsely certified')
