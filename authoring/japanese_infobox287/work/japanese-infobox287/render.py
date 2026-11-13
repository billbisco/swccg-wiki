from concurrent.futures import ThreadPoolExecutor
import gzip
import json
import re
from pathlib import Path
import sys
import requests

root=Path(__file__).parent
mode=sys.argv[1]
heads=json.loads((root/'heads-before.json').read_bytes())
if mode=='before':
    titles=json.loads((root/'targets.json').read_bytes())+json.loads((root/'english-sample.json').read_bytes())
    jobs=[dict(title=t,oldid=heads[t]['revisions'][0]['revid']) for t in titles]
else:
    rows=json.loads((root/'drafts.json').read_bytes())
    if mode=='samples':
        titles=json.loads((root/'sample-titles.json').read_bytes())
        jobs=[r for r in rows if r['title'] in titles]
    elif mode=='drafts':jobs=rows
    elif mode in ['english-sandbox','english-before']:
        jobs=[dict(title=t,text=heads[t]['revisions'][0]['slots']['main']['content']) for t in json.loads((root/'english-sample.json').read_bytes())]
    else:raise ValueError(mode)
def render(job):
    params=dict(format='json',formatversion=2,action='parse',prop='text|links|images|categories')
    if 'text' in job:
        text=job['text'] if mode=='english-before' else re.sub(r'\{\{\s*Card(?=\s*[|\n])','{{Card/sandbox',job['text'],count=1)
        params.update(title=job['title'],text=text,contentmodel='wikitext')
    else:params.update(oldid=job['oldid'])
    response=requests.post('https://wiki.swccg.com/api.php',data=params,timeout=90)
    response.raise_for_status();result=response.json();assert 'error' not in result,(job['title'],result.get('error'))
    return job['title'],result['parse']
results={}
with ThreadPoolExecutor(max_workers=4) as pool:
    for title,result in pool.map(render,jobs):
        results[title]=result
        if len(results)%100==0:print(mode,len(results),'of',len(jobs),flush=True)
with gzip.open(root/(mode+'-renders.json.gz'),'wt',encoding='utf8') as f:json.dump(results,f,ensure_ascii=False)
errors=[t for t,p in results.items() if 'cite-error' in p['text']]
(root/(mode+'-cite-errors.json')).write_text(json.dumps(errors,ensure_ascii=False,indent=2),encoding='utf8')
print(mode,len(results),'rendered;',len(errors),'Cite errors',flush=True)
