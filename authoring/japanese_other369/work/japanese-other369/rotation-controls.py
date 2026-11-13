from concurrent.futures import ThreadPoolExecutor
import json,re
from pathlib import Path
import requests
from bs4 import BeautifulSoup,Comment
root=Path(__file__).parent;before=root.parent/'japanese-infobox287'
if not (root/'english-control-inputs.json').exists():
    titles=json.loads((before/'english-sample.json').read_bytes());heads=json.loads((before/'heads-before.json').read_bytes())
    inputs=[dict(title=t,text=heads[t]['revisions'][0]['slots']['main']['content']) for t in titles]
    (root/'english-control-inputs.json').write_text(json.dumps(inputs,ensure_ascii=False,indent=2),encoding='utf8')
else:inputs=json.loads((root/'english-control-inputs.json').read_bytes())
def clean(text):
    soup=BeautifulSoup(text,'html.parser')
    for comment in soup.find_all(string=lambda x:isinstance(x,Comment)):comment.extract()
    for el in soup.select('style,script,.mw-editsection,#toc,.toc,.mw-cite-backlink,sup.reference,.mw-ext-cite-error'):el.decompose()
    return str(soup)
def one(row):
    rendered=[]
    for sandbox in [False,True]:
        text=re.sub(r'\{\{\s*Card(?=\s*[|\n])','{{Card/sandbox',row['text'],count=1) if sandbox else row['text']
        r=requests.post('https://wiki.swccg.com/api.php',data=dict(action='parse',format='json',formatversion=2,title=row['title'],text=text,contentmodel='wikitext',prop='text'),timeout=90);r.raise_for_status();j=r.json();assert 'error' not in j,j;rendered.append(clean(j['parse']['text']))
    return dict(title=row['title'],identical=rendered[0]==rendered[1])
with ThreadPoolExecutor(max_workers=4) as pool:out=list(pool.map(one,inputs))
(root/'rotation-english-report.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
assert all(r['identical'] for r in out),[r for r in out if not r['identical']]
print('50/50 fresh English controls identical with the optional rotation sandbox')
