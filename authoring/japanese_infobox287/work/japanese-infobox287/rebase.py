import gzip,json,subprocess,sys
from pathlib import Path
import requests
root=Path(__file__).parent
conflicts=json.loads((root/'concurrent-edits.json').read_bytes())
assert all(x.get('conflict') for x in conflicts)
for file in ['heads-before.json','before-renders.json.gz']:
    initial=root/('initial-'+file)
    if not initial.exists():initial.write_bytes((root/file).read_bytes())
heads=json.loads((root/'heads-before.json').read_bytes())
renders=json.load(gzip.open(root/'before-renders.json.gz','rt',encoding='utf8'))
def render(_title,**kwargs):
    response=requests.post('https://wiki.swccg.com/api.php',data=dict(action='parse',format='json',formatversion=2,prop='text|links|images|categories',**kwargs),timeout=90)
    response.raise_for_status();result=response.json();assert 'error' not in result,result;return result['parse']
for row in conflicts:
    title=row['title'];heads[title]=row['page'];renders[title]=render(title,oldid=row['page']['revisions'][0]['revid'])
(root/'heads-before.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
with gzip.open(root/'before-renders.json.gz','wt',encoding='utf8') as f:json.dump(renders,f,ensure_ascii=False)
for script in ['convert.py','set-icons.py']:subprocess.run([sys.executable,str(root/script)],check=True)
drafts={r['title']:r for r in json.loads((root/'drafts.json').read_bytes())}
renders=json.load(gzip.open(root/'drafts-renders.json.gz','rt',encoding='utf8'))
for row in conflicts:
    title=row['title'];renders[title]=render(title,title=title,text=drafts[title]['text'].replace('{{Card\n','{{Card/sandbox\n',1),contentmodel='wikitext')
with gzip.open(root/'drafts-renders.json.gz','wt',encoding='utf8') as f:json.dump(renders,f,ensure_ascii=False)
print('Rebased',len(conflicts),'concurrent Versions updates without discarding changes')
