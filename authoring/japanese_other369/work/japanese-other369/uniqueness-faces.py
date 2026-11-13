from concurrent.futures import ThreadPoolExecutor
import hashlib,json
from pathlib import Path
import requests
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).parent;folder=root/'inspection';folder.mkdir(exist_ok=True)
targets=json.loads((root/'uniqueness-targets.json').read_bytes())
files=sorted({x['images'][0] for x in targets});info={}
for i in range(0,len(files),40):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join('File:'+x for x in files[i:i+40]),prop='imageinfo',iiprop='url|size'),timeout=60);r.raise_for_status()
    for page in r.json()['query']['pages']:info[page['title'][5:]]=page['imageinfo'][0]
def one(pair):
    i,row=pair;name=row['images'][0];path=folder/f'{i:03d}.jpg'
    if not path.exists():
        r=requests.get(info[name]['url'],timeout=60);r.raise_for_status();path.write_bytes(r.content)
    with Image.open(path) as im:width,height=im.size
    return dict(number=i,title=row['title'],file=str(path.relative_to(root)),source_file='File:'+name,url=info[name]['url'],sha256=hashlib.sha256(path.read_bytes()).hexdigest(),width=width,height=height)
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(one,enumerate(targets,1)))
(root/'uniqueness-manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
for offset in range(0,len(records),18):
    sheet=Image.new('RGB',(1800,1230),'white');draw=ImageDraw.Draw(sheet)
    for j,row in enumerate(records[offset:offset+18]):
        im=Image.open(root/row['file']).convert('RGB');im=ImageOps.contain(im,(295,365))
        x=(j%6)*300;y=(j//6)*410
        sheet.paste(im,(x,y+35));draw.text((x+4,y+3),str(row['number'])+' '+row['title'][:34],fill='black')
    sheet.save(root/f'unique-sheet-{offset//18+1:02d}.jpg',quality=92)
print('Prepared',len(records),'original-face inspections in',(len(records)+17)//18,'numbered sheets')
