import requests,json,re,hashlib
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
p=Path(__file__).parent
def api(**args):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action=args.pop('action','query'),format='json',formatversion=2,**args),timeout=60);r.raise_for_status();j=r.json();assert 'error' not in j,j;return j
allimages=api(list='allimages',aifrom='Icon-set-',ailimit=500,aiprop='url|sha1|size|mime')['query']['allimages'];files=[r for r in allimages if r['name'].lower().startswith('icon-set-')]
def inspect(row):
    title='File:'+row['name'];used=[];cont={}
    while True:
        j=api(titles=title,prop='fileusage|revisions',fulimit=500,rvprop='ids|content',rvslots='main',**cont);h=j['query']['pages'][0];used+=h.get('fileusage',[])
        if 'continue' not in j:break
        cont=j['continue']
    r=requests.get(row['url'],timeout=60);r.raise_for_status();raw=r.content;f=p/'old-wiki-assets'/row['name'];f.parent.mkdir(exist_ok=True);f.write_bytes(raw)
    from PIL import Image
    im=Image.open(f).convert('RGBA');alpha=im.getchannel('A');return dict(row,title=title,sha256=hashlib.sha256(raw).hexdigest(),alpha_range=list(alpha.getextrema()),transparent_corners=all(alpha.getpixel(x)==0 for x in [(0,0),(im.width-1,0),(0,im.height-1),(im.width-1,im.height-1)]),usages=used,usage_count=len(used),mainspace_usages=sum(x['ns']==0 for x in used),file_page=h)
with ThreadPoolExecutor(max_workers=3) as pool:out=list(pool.map(inspect,files))
(p/'wiki-symbol-audit.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
print(len(out),'existing Icon-set assets audited;',sum(x['usage_count'] for x in out),'references;',sum(not x['transparent_corners'] for x in out),'opaque-corner assets')
master=json.loads((p/'symbols/manifest.json').read_bytes());assert master['master_commit']=='a41df94fc32c197757650f03ae64f6c096342124'
gaps=['Verify regular silver and AI gold Coruscant variants against physical scans; existing CardMaker asset is not a default silver replacement.','Verify Tatooine and Theed Palace AI gold variants separately.','Inventory Original Virtual, Legacy, Modern and Reflections Gold original/remaster marks; do not infer them from sphere style.','Choose the card-text presentation after the requested visual pilot; infobox icon+visible name remains the existing rule.','Story286 retains wider missing-infobox coverage;435 must not assert that audit complete.','No Wiki symbols migrated by the pilot exporter. Archive requests entirely held.']
(p/'remaining-gaps.json').write_text(json.dumps(gaps,indent=2),encoding='utf8')
