"""Verify a narrow guarded repair without repeating unrelated completed checks."""
import hashlib,json,re,sys,time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from urllib.parse import quote
import requests
from bs4 import BeautifulSoup
sys.path.insert(0,'work/wiki-tools');from publication_policy import lint
root=Path(__file__).parent;prefix=sys.argv[1];rows=json.loads((root/(prefix+'-packet.json')).read_bytes());receipts={r['title']:r for r in map(json.loads,(root/(prefix+'-receipts.jsonl')).read_text(encoding='utf8').splitlines())};heads={}
for i in range(0,len(rows),25):
    response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(r['title'] for r in rows[i:i+25]),prop='revisions|flagged',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);response.raise_for_status();heads.update({h['title']:h for h in response.json()['query']['pages']})
for row in rows:
    title=row['title'];h=heads[title];rev=h['revisions'][0];text=rev['slots']['main']['content'];receipt=receipts[title]
    assert text.rstrip()==row['text'].rstrip() and rev['revid']==receipt['revid'],title
    assert hashlib.sha256(text.encode()).hexdigest()==receipt['sha256'] and not lint(text,title)[0],title
    if h['ns']%2==0:assert receipt['reviewed'] and h.get('flagged',{}).get('stable_revid')==rev['revid'],title
def public(row):
    title=row['title'];url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='')
    for attempt in range(3):
        response=requests.get(url,timeout=60);response.raise_for_status();soup=BeautifulSoup(response.text,'html.parser');match=re.search(r'"wgRevisionId":(\d+)',response.text)
        assert not soup.select('.mw-ext-cite-error'),(title,'Cite error')
        if match and int(match[1])==receipts[title]['revid']:break
        if attempt==0:
            purge=requests.post('https://wiki.swccg.com/api.php',data=dict(action='purge',format='json',formatversion=2,titles=title,forcelinkupdate=1),timeout=60);purge.raise_for_status();assert purge.json()['purge'][0].get('purged'),title
        time.sleep(1)
    assert match and int(match[1])==receipts[title]['revid'],(title,'Public revision stale')
    return dict(title=title,url=url,revid=receipts[title]['revid'],exact_source=True,public_current=True,cite_errors=0,non_archive_lint_flags=0,reviewed=receipts[title]['reviewed'])
with ThreadPoolExecutor(max_workers=3) as pool:report=list(pool.map(public,rows))
(root/(prefix+'-verification.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
published=json.loads((root/'published-heads.json').read_bytes());published.update(heads);(root/'published-heads.json').write_text(json.dumps(published,ensure_ascii=False,indent=2),encoding='utf8');(root/'published-pages.md').write_text('# All changed live pages — story381\n\n'+''.join('* ['+t+'](https://wiki.swccg.com/wiki/'+quote(t.replace(' ','_'),safe='')+')\n' for t in sorted(published)),encoding='utf8')
print(len(report),'narrow repairs checked: exact/current public source, review, Cite and non-archive lint')
