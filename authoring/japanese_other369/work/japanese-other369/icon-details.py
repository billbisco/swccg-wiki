import json
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
import requests
root=Path(__file__).parent
titles=['Icon-pilot-Light.png','Icon-pilot-Dark.png','Icon-warrior.png','Icon-nav-computer.png','Icon-scomp-link.png']
r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join('File:'+x for x in titles),prop='imageinfo',iiprop='url'),timeout=60);r.raise_for_status()
canvas=Image.new('RGB',(1100,1200),'white');draw=ImageDraw.Draw(canvas)
for i,p in enumerate(r.json()['query']['pages']):
    if 'imageinfo' not in p:continue
    data=requests.get(p['imageinfo'][0]['url'],timeout=30).content;file=root/('legend-'+str(i)+'.png');file.write_bytes(data)
    im=ImageOps.contain(Image.open(file).convert('RGBA'),(100,100));canvas.paste(im,(i*220,25),im);draw.text((i*220,5),p['title'][5:],fill='black')
manifest=json.loads((root/'icon-inspection-manifest.json').read_bytes())
chosen=[2,6,9,11,12,18,19,20,35]
for j,n in enumerate(chosen):
    row=manifest[n-1];im=Image.open(root/row['file']).convert('RGB');w,h=im.size
    # Inspection crop only: bottom text/statistics and printed symbols, original photo retained.
    im=im.crop((0,h*.64,w,h));im=ImageOps.contain(im,(355,290));x=(j%3)*365;y=160+(j//3)*340
    canvas.paste(im,(x,y+22));draw.text((x+4,y),str(n)+' '+row['title'][:40],fill='black')
canvas.save(root/'icon-details.jpg',quality=95)
