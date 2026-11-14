import hashlib,json,re
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import requests
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).parent;folder=root/'photos';folder.mkdir(exist_ok=True)
rows=json.loads((root/'photo-candidates.json').read_bytes())
labels=['2-1B','4-LOM','ALL WINGS REPORT IN','ARTOO','ATTACK RUN','BANE MALAR','BEN KENOBI','BIB FORTUNA','BIGGS DARKLIGHTER','BLACK 2']
selected=[]
for label in labels:
    options=[r for r in rows if r['product']=='Reflections' and r['caption_title'].upper()==label]
    assert options,label
    chosen=next((r for r in options if r['source_html']=='ri-robert.html'),options[0]);selected.append(chosen)
def one(pair):
    i,row=pair;file=folder/f'ri-{i:03d}.jpg'
    if not file.exists():
        r=requests.get(row['url'],timeout=90);r.raise_for_status();file.write_bytes(r.content)
    with Image.open(file) as im:w,h=im.size
    return dict(row,number=i,local_file=str(file.relative_to(root)),sha256=hashlib.sha256(file.read_bytes()).hexdigest(),width=w,height=h)
with ThreadPoolExecutor(max_workers=3) as pool:out=list(pool.map(one,enumerate(selected,1)))
(root/'first-face-manifest.json').write_text(json.dumps(out,ensure_ascii=False,indent=2),encoding='utf8')
for offset in range(0,len(out),2):
    canvas=Image.new('RGB',(1500,1700),'white');d=ImageDraw.Draw(canvas)
    for x,r in enumerate(out[offset:offset+2]):
        im=ImageOps.contain(Image.open(root/r['local_file']).convert('RGB'),(740,1660));canvas.paste(im,(x*750,30));d.text((x*750+5,5),str(r['number'])+' '+r['caption_title'],fill='black')
    canvas.save(root/f'first-face-sheet-{offset//2+1}.webp',quality=90,method=6)
for r in out:print(r['number'],r['caption_title'],r['width'],r['height'])
