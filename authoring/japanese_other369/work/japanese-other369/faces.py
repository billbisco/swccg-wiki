from concurrent.futures import ThreadPoolExecutor
import hashlib,json
from pathlib import Path
import requests
root=Path(__file__).parent
records=json.loads((root/'census.json').read_bytes())
titles=['Death Star (Japanese)','Death Star: Conference Room (Japanese)','Death Star (Japanese Reflections II Foil)','Leia (Japanese ESB Two-Player)','Leia (Japanese Reflections II Foil)','Tantive IV (Japanese)']
selected=[r for r in records if r['title'] in titles]
response=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join('File:'+r['images'][0] for r in selected),prop='imageinfo|revisions',iiprop='url|size|sha1',rvprop='ids|content',rvslots='main'),timeout=60)
response.raise_for_status();pages={p['title']:p for p in response.json()['query']['pages']}
manifest=[]
for i,row in enumerate(selected,1):
    page=pages['File:'+row['images'][0]];info=page['imageinfo'][0];data=requests.get(info['url'],timeout=60).content
    path=root/f'face-{i}.jpg';path.write_bytes(data)
    manifest.append(dict(title=row['title'],file=path.name,source_file=page['title'],url=info['url'],sha256=hashlib.sha256(data).hexdigest(),width=info['width'],height=info['height'],file_source=page['revisions'][0]['slots']['main']['content']))
    print(i,row['title'],info['width'],info['height'],flush=True)
(root/'face-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
