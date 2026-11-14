"""Correct link capitalization in own foil icon fields; preserve everything else."""
import hashlib,json,sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
root=Path(__file__).parent
prefix=sys.argv[1] if len(sys.argv)>1 else 'icon-link-correction'
titles=[r['proposed_article'] for r in json.loads((root/'manifest.json').read_bytes()) if r['language']=='English']
def fetch(batch):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(batch),prop='revisions',rvprop='ids|timestamp|content',rvslots='main'),timeout=60);r.raise_for_status();return r.json()['query']['pages']
packet=[];proof=[]
with ThreadPoolExecutor(max_workers=3) as pool:
    for batch in pool.map(fetch,[titles[i:i+30] for i in range(0,len(titles),30)]):
        for head in batch:
            if 'revisions' not in head:continue
            rev=head['revisions'][0];old=rev['slots']['main']['content'];code=mw.parse(old)
            cards=[t for t in code.filter_templates(recursive=False) if str(t.name).strip()=='Card']
            if len(cards)!=1 or not cards[0].has('icons'):continue
            value=str(cards[0].get('icons').value);new=value.replace('[[Scomp link]]','[[Scomp Link]]').replace('[[Nav computer]]','[[Nav Computer]]').replace('[[Permanent weapon]]','[[Permanent Weapon]]')
            if new==value:continue
            cards[0].get('icons').value=new
            text=str(code)
            assert text.replace('|icons='+new,'|icons='+value,1)==old
            packet.append(dict(title=head['title'],text=text,before_revid=rev['revid'],before_sha256=hashlib.sha256(old.encode()).hexdigest(),section=0,summary='Correct icon link capitalization to existing concept titles; printed symbols unchanged (#381)'))
            proof.append(dict(title=head['title'],before_revid=rev['revid'],before_icons=value,after_icons=new,all_other_source_exactly_conserved=True))
for name,data in [(prefix+'-packet.json',packet),(prefix+'-conservation.json',proof)]:
    (root/name).write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf8')
print(len(packet),'icon field capitalization corrections; all other source exactly conserved')
