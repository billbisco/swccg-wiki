from concurrent.futures import ThreadPoolExecutor
import collections
import json
from pathlib import Path
import random
import re
import sys

import requests
from bs4 import BeautifulSoup
sys.path.insert(0,'work')
from audit_wiki_card_titles import get,collect
sys.path.insert(0,'work/wiki-tools')
from style_lint import lint

root=Path(__file__).parent
cards=collect('Cards')
targets=[r['title'] for r in cards if 'Japanese' in r['title'] or ('Mara Jade' in r['title'] and 'Talon Karrde' in r['title'])]
assert len(targets)==794,(len(targets),[x for x in targets if 'Japanese' not in x])
english=random.Random(287).sample(sorted(r['title'] for r in cards if r['title'] not in targets),50)
titles=sorted(set(targets+english+['Template:Card','Template:Card/sandbox','Template:Card/doc','Template:Set icon','Template:Set page','SWCCG Wiki:Style guide']))
def fetch(batch):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(format='json',formatversion=2,action='query',titles='|'.join(batch),prop='revisions',rvprop='ids|timestamp|content',rvslots='main'),timeout=45)
    response.raise_for_status();result=response.json();assert 'error' not in result,result.get('error')
    return result['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=4) as pool:
    for result in pool.map(fetch,[titles[i:i+40] for i in range(0,len(titles),40)]):
        heads.update({p['title']:p for p in result})
(root/'heads-before.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
(root/'targets.json').write_text(json.dumps(sorted(targets),ensure_ascii=False,indent=2),encoding='utf8')
(root/'english-sample.json').write_text(json.dumps(english,ensure_ascii=False,indent=2),encoding='utf8')
headers=collections.Counter();sections=collections.Counter();sets=collections.Counter();flags=[];templated=[]
for title in targets:
    text=heads[title]['revisions'][0]['slots']['main']['content']
    if re.search(r'\{\{\s*Card\s*[|\n]',text):templated.append(title)
    soup=BeautifulSoup(text,'html.parser')
    for row in soup.select('table.card-infobox tr'):
        cells=row.find_all(['th','td'],recursive=False)
        if len(cells)==2:
            label=cells[0].get_text(' ',strip=True)
            headers[label]+=1
            if label=='Set':sets[cells[1].get_text(' ',strip=True)]+=1
    headings=re.findall(r'<h2>(.*?)</h2>|(?m:^==\s*([^=]+)\s*==)',text)
    sections.update(a or b.strip() for a,b in headings)
    findings=lint(text,title)[0]
    if findings:flags.append(dict(title=title,flags=findings))
assert not templated,('Already migrated; reconcile',templated[:10])
report=dict(targets=len(targets),english_sample=50,headers=dict(headers),sections=dict(sections),sets=dict(sets),lint=flags)
(root/'baseline-summary.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
print(json.dumps(dict(targets=len(targets),headers=dict(headers),sections=dict(sections),sets=dict(sets),lint_pages=len(flags)),ensure_ascii=False))
for title in ['Template:Card','Template:Card/doc','Template:Card/sandbox']:
    (root/(title.replace(':','-').replace('/','-')+'.wiki')).write_text(heads[title]['revisions'][0]['slots']['main']['content'],encoding='utf8')
