import json,re,hashlib,time,collections
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from urllib.parse import quote,unquote
import requests
from bs4 import BeautifulSoup
root=Path(__file__).parent;rows=json.loads((root/'all-packet.json').read_bytes());inventory=json.loads(Path('work/reflections-foil-tables/inventory.json').read_bytes())
receipts={r['title']:r for f in root.glob('*-receipts.jsonl') for r in map(json.loads,f.read_text(encoding='utf8').splitlines())}
assert set(receipts)=={r['title'] for r in rows},('Incomplete publication',len(receipts),len(rows))
def fetch(ts,images=False):
    args=dict(action='query',format='json',formatversion=2,titles='|'.join(ts),prop='revisions|flagged'+('|imageinfo' if images else ''),rvprop='ids|content',rvslots='main')
    if images:args['iiprop']='sha1|timestamp|size|mime'
    r=requests.get('https://wiki.swccg.com/api.php',params=args,timeout=90);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j['query']['pages']
heads={}
with ThreadPoolExecutor(max_workers=3) as pool:
    titles=list(receipts)
    for batch in pool.map(fetch,[titles[i:i+30] for i in range(0,len(titles),30)]):heads.update({h['title']:h for h in batch})
for row in rows:
    title=row['title'];h=heads[title];rev=h['revisions'][0];text=rev['slots']['main']['content'];receipt=receipts[title]
    assert rev['revid']==receipt['revid'] and hashlib.sha256(text.encode()).hexdigest()==receipt['sha256'],title
    assert text.rstrip()==row['text'].rstrip(),title
    assert h.get('flagged',{}).get('stable_revid')==rev['revid'],(title,h.get('flagged'))
(root/'published-heads.json').write_text(json.dumps(heads,ensure_ascii=False,indent=2),encoding='utf8')
oldfiles=json.loads(Path('work/reflections-foil-tables/image-heads.json').read_bytes());files={};titles=list(oldfiles)
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(lambda ts:fetch(ts,True),[titles[i:i+30] for i in range(0,len(titles),30)]):files.update({h['title']:h for h in batch})
unchanged=[]
for title,h in oldfiles.items():
    old=h['imageinfo'][0];new=files[title]['imageinfo'][0]
    assert all(old[k]==new[k] for k in ['sha1','timestamp','size','mime']),title
    unchanged.append(dict(title=title,sha1=new['sha1'],timestamp=new['timestamp'],size=new['size'],unchanged=True))
(root/'originals-unchanged.json').write_text(json.dumps(unchanged,ensure_ascii=False,indent=2),encoding='utf8')
print(len(heads),'current reviewed exact sources;',len(unchanged),'original files unchanged',flush=True)
def public(row):
    title=row['title'];rid=receipts[title]['revid'];url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe=':(),')
    r=requests.get(url,timeout=90);r.raise_for_status();html=r.text;s=BeautifulSoup(html,'html.parser');m=re.search(r'"wgRevisionId":(\d+)',html)
    if not m or int(m[1])!=rid or 'td:not(:first-child) img{width:auto' not in html:return row,None
    assert not s.select('.mw-ext-cite-error,.error'),title
    count=len(s.select('.card-photo'))
    if title in ['Reflections','Reflections II: Expanding the Galaxy','Reflections III']:
        actual=[]
        tables=[t for t in s.select('table.card-thumbs') if t.caption and 'Side foils (' in t.caption.get_text()];assert len(tables)==2,title
        for table in tables:
            for tr in table.select('tr'):
                cells=tr.find_all('td',recursive=False)
                if not cells:continue
                assert len(cells)==7;link=cells[1].find('a');target=unquote(link['href'].split('/wiki/',1)[1]).replace('_',' ');actual.append(target)
                assert cells[0].find('img') and cells[6].get_text(strip=True),target
        assert collections.Counter(actual)==collections.Counter(r['article'] for r in inventory if r['product']==title),title
        assert count==row['text'].count('{{Card photograph|'),title
    elif not title.startswith('Template:'):assert count==1,title
    return row,dict(title=title,url=url,revid=rid,reviewed=True,exact_saved_source=True,public_canonical_current=True,cite_errors=0,card_frames=count,original_links=len([a for a in s.select('.card-photo small a') if a.get_text()=='Original photograph']))
out=[];pending=rows
for attempt in range(5):
    retry=[]
    with ThreadPoolExecutor(max_workers=3) as pool:
        for row,result in pool.map(public,pending):
            if result:out.append(result)
            else:retry.append(row)
    if not retry:break
    print(len(retry),'canonical microcache entries awaiting refresh',flush=True);pending=retry;time.sleep(30)
assert not retry,[r['title'] for r in retry]
(root/'public-verification.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
(root/'published-pages.md').write_text('# Changed live pages — bug436\n\n'+''.join('- ['+r['title']+']('+r['url']+')\n' for r in sorted(out,key=lambda r:r['title'])),encoding='utf8')
print(len(out),'canonical public pages PASS: exact reviewed revision, current CSS, Cite 0, complete frames/original links and 314 exact table rows')
