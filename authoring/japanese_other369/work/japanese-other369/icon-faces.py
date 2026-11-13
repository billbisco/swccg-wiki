from concurrent.futures import ThreadPoolExecutor
import hashlib,json
from pathlib import Path
import requests
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).parent;folder=root/'icon-inspection';folder.mkdir(exist_ok=True)
targets=json.loads((root/'icon-targets.json').read_bytes());prior={r['title']:r for r in json.loads((root/'uniqueness-manifest.json').read_bytes())}
names=sorted({r['images'][0] for r in targets if r['title'] not in prior});info={}
for i in range(0,len(names),40):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join('File:'+x for x in names[i:i+40]),prop='imageinfo',iiprop='url|size'),timeout=60);r.raise_for_status()
    for p in r.json()['query']['pages']:info[p['title'][5:]]=p['imageinfo'][0]
def one(pair):
    i,row=pair
    if row['title'] in prior:return dict(prior[row['title']],icon_number=i)
    name=row['images'][0];path=folder/f'{i:03d}.jpg'
    if not path.exists():
        r=requests.get(info[name]['url'],timeout=60);r.raise_for_status();path.write_bytes(r.content)
    with Image.open(path) as im:width,height=im.size
    return dict(number=None,icon_number=i,title=row['title'],file=str(path.relative_to(root)),source_file='File:'+name,url=info[name]['url'],sha256=hashlib.sha256(path.read_bytes()).hexdigest(),width=width,height=height)
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(one,enumerate(targets,1)))
(root/'icon-inspection-manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
for offset in range(0,len(records),18):
    sheet=Image.new('RGB',(1800,1230),'white');draw=ImageDraw.Draw(sheet)
    for j,row in enumerate(records[offset:offset+18]):
        im=ImageOps.contain(Image.open(root/row['file']).convert('RGB'),(295,365));x=(j%6)*300;y=(j//6)*410
        sheet.paste(im,(x,y+35));draw.text((x+4,y+3),str(row['icon_number'])+' '+row['title'][:35],fill='black')
    sheet.save(root/f'icon-sheet-{offset//18+1:02d}.jpg',quality=92)
print(len(records),'card icon inspections;',len(names),'additional source photos, prior downloads reused')
