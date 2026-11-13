from concurrent.futures import ThreadPoolExecutor
import hashlib,json,re
from pathlib import Path
import requests
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).parent;folder=root/'recovered';folder.mkdir(exist_ok=True)
rows=[r for r in json.loads((root/'recovered-source-leads.json').read_bytes()) if not r['live_title'].startswith('2-1B')]
def one(pair):
    i,row=pair;path=folder/f'{i:02d}.jpg'
    if not path.exists():
        response=requests.get(row['asset'],timeout=60);response.raise_for_status();path.write_bytes(response.content)
    with Image.open(path) as im:w,h=im.size
    return dict(number=i,title=row['live_title'],uid=row['uid'],url=row['asset'],gallery=row['gallery'],file=str(path.relative_to(root)),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),width=w,height=h)
with ThreadPoolExecutor(max_workers=3) as pool:records=list(pool.map(one,enumerate(rows,1)))
(root/'recovered-face-manifest.json').write_text(json.dumps(records,ensure_ascii=False,indent=2),encoding='utf8')
for offset in range(0,len(records),3):
    out=Image.new('RGB',(1500,900),'white');d=ImageDraw.Draw(out)
    for i,row in enumerate(records[offset:offset+3]):
        im=ImageOps.contain(Image.open(root/row['file']).convert('RGB'),(490,850));out.paste(im,(i*500,30));d.text((i*500+4,4),str(row['number'])+' '+row['title'][:60],fill='black')
    out.save(root/f'recovered-sheet-{offset//3+1}.jpg',quality=95)
for r in records:print(r['number'],r['title'],r['width'],r['height'])
