"""Durable exact-version queue; no Save Page Now requests or invented captures."""
import hashlib,json,re,sys
from pathlib import Path
from urllib.parse import urlparse
import requests
from source_registry import provenance
root=Path(__file__).parent;stage=sys.argv[1] if len(sys.argv)>1 else None
path=root/'preservation-queue.json';queue=json.loads(path.read_bytes()) if path.exists() else {}
def add(url,kind,title=None,**metadata):
    row=queue.setdefault(url,dict(url=url,kinds=[],titles=[],status='queued; capture not verified',follow_up='https://github.com/swccg-guild/work/issues/412'))
    if kind not in row['kinds']:row['kinds'].append(kind)
    if title and title not in row['titles']:row['titles'].append(title)
    row.update(metadata)
    if urlparse(url).hostname in ['forum.starwarsccg.org','www.starwarsccg.org']:row['route']='staged snapshot required; never submit this live URL to worker'
    else:row.update(route='normal archival worker route',worker_url=url)
for file in root.glob('batch*-citation-urls.json'):
    for url in json.loads(file.read_bytes()):add(url,'inherited citation')
for file in root.glob('batch*-readings.json'):
    for row in json.loads(file.read_bytes()):
        add(row['source_url'],'physical source photograph',row['article'],source_sha256=row['source_sha256'])
        add(provenance(row)['url'],'source collection entry',row['article'])
if (root/'deferred-archive-findings.jsonl').exists():
    for row in map(json.loads,(root/'deferred-archive-findings.jsonl').read_text(encoding='utf8').splitlines()):
        for flag in row['flags']:
            match=re.search(r'https?://\S+',flag)
            if match:add(match[0],'deferred ARCHIVE lint',row['title'])
if stage:
    files=json.loads((root/(stage+'-files-payload.json')).read_bytes());titles=[f['title'] for f in files]
    for i in range(0,len(titles),25):
        response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(titles[i:i+25]),prop='imageinfo',iiprop='url|sha1|timestamp|size|mime'),timeout=60);response.raise_for_status()
        for head in response.json()['query']['pages']:
            if not head.get('imageinfo'):continue
            info=head['imageinfo'][0];file=next(f for f in files if f['title']==head['title']);assert file['sha1']==info['sha1'],head['title']
            version=dict(title=head['title'],timestamp=info['timestamp'],sha1=info['sha1'],sha256=file['sha256'],bytes=info['size'],mime=info['mime'])
            add(info['url'],'public wiki-image original/version',head['title'],wiki_image_version=version)
latest_images={}
for file in root.glob('*-image-captures.jsonl'):
    for row in map(json.loads,file.read_text(encoding='utf8').splitlines()):latest_images[row['url']]=row
for url,row in latest_images.items():
    if row.get('verified'):
        if url in queue:queue.pop(url)
    else:add(url,'public wiki-image original/version',row['title'],wiki_image_version=dict(title=row['title'],timestamp=row['version'],sha1=row['sha1'],sha256=row['image_sha256'],mime=row['mime']))
for file in root.glob('batch*-preservation.json'):
    row=json.loads(file.read_bytes())
    if row.get('url') and not row.get('verified'):add(row['url'],'retained source snapshot',staging_path=row.get('staging_path'))
path.write_text(json.dumps(queue,ensure_ascii=False,indent=2),encoding='utf8')
print(len(queue),'distinct archival queue entries;',sum('wiki_image_version' in r for r in queue.values()),'exact image versions; no capture claimed')
