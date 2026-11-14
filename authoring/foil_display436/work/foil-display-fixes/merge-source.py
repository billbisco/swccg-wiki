import json,subprocess
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import requests
p=Path(__file__).parent;heads=json.loads((p/'published-heads.json').read_bytes());titles=list(heads)
def check(ts):
    j=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(ts),prop='revisions',rvprop='ids'),timeout=60).json()
    for h in j['query']['pages']:assert h['revisions'][0]['revid']==heads[h['title']]['revisions'][0]['revid'],(h['title'],'Concurrent live change')
with ThreadPoolExecutor(max_workers=3) as pool:list(pool.map(check,[titles[i:i+35] for i in range(0,len(titles),35)]))
subprocess.run(['python',str(p/'store.py'),'wiki'],check=True)
head=(p/'wiki-commit.txt').read_text().strip()
subprocess.run(['gh','pr','merge','41','-R','billbisco/swccg-wiki','--merge','--match-head-commit',head],check=True)
r=subprocess.check_output(['gh','pr','view','41','-R','billbisco/swccg-wiki','--json','state,mergedAt,mergeCommit,headRefOid,url'])
receipt=json.loads(r);assert receipt['state']=='MERGED'
(p/'merge-receipt.json').write_bytes(r);print(r.decode())
