from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import requests
from PIL import Image,ImageOps,ImageDraw

root=Path(__file__).parent
rows=json.loads((root/'drafts.json').read_bytes())
details={r['title']:r for r in json.loads((root/'conversion-details.json').read_bytes())}
selected=[r for r in rows if r['set'].startswith('Reflections') or not r['is_ja']]
names=['File:'+details[r['title']]['params']['image'] for r in selected]
result=requests.get('https://wiki.swccg.com/api.php',params=dict(format='json',formatversion=2,action='query',titles='|'.join(names),prop='imageinfo',iiprop='url|sha1|size'),timeout=45).json()
files={p['title']:p['imageinfo'][0] for p in result['query']['pages']}
(root/'icon-faces').mkdir(exist_ok=True)
def fetch(pair):
    n,row=pair
    name='File:'+details[row['title']]['params']['image'];info=files[name]
    response=requests.get(info['url'],timeout=40);response.raise_for_status()
    path=root/'icon-faces'/str(n)
    path.write_bytes(response.content)
    return dict(title=row['title'],file=name,url=info['url'],sha256=hashlib.sha256(response.content).hexdigest(),path=str(path),number=n)
with ThreadPoolExecutor(max_workers=4) as pool:manifest=list(pool.map(fetch,enumerate(selected)))
(root/'icon-face-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
for start in range(0,len(manifest),4):
    sheet=Image.new('RGB',(1400,1200),'white');draw=ImageDraw.Draw(sheet)
    for i,row in enumerate(manifest[start:start+4]):
        face=ImageOps.exif_transpose(Image.open(row['path'])).convert('RGB')
        # Keep the full upper printed area, where these Decipher symbols appear.
        face=face.crop((0,0,face.width,round(face.height*.52)))
        face.thumbnail((680,555))
        x=(i%2)*700;y=(i//2)*600
        sheet.paste(face,(x,y+32));draw.text((x+8,y+8),str(row['number'])+' '+row['title'],fill='black')
    sheet.save(root/('icon-sheet-'+str(start//4)+'.jpg'),quality=90)
print(len(manifest),'printing faces downloaded for symbol verification')
