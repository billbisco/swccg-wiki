from concurrent.futures import ThreadPoolExecutor
import json,requests
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).parent
details=json.loads((root/'conversion-details.json').read_bytes())
rows=[r for r in details if r['params'].get('gemp_id','').startswith('1404_')]
names=['File:'+r['params']['image'] for r in rows]
result=requests.get('https://wiki.swccg.com/api.php',params=dict(format='json',formatversion=2,action='query',titles='|'.join(names),prop='imageinfo',iiprop='url'),timeout=30).json()['query']['pages']
urls={p['title']:p['imageinfo'][0]['url'] for p in result}
def fetch(pair):
    i,row=pair;url=urls['File:'+row['params']['image']]
    response=requests.get(url,timeout=30);response.raise_for_status()
    path=root/'icon-faces'/('premium-'+str(i));path.write_bytes(response.content)
    return dict(title=row['title'],file=row['params']['image'],url=url,path=str(path))
with ThreadPoolExecutor(max_workers=4) as pool:manifest=list(pool.map(fetch,enumerate(rows)))
for start in [0,4]:
    sheet=Image.new('RGB',(1400,1500),'white');draw=ImageDraw.Draw(sheet)
    for j,row in enumerate(manifest[start:start+4]):
        image=ImageOps.exif_transpose(Image.open(row['path'])).convert('RGB');image.thumbnail((680,705))
        x=(j%2)*700;y=(j//2)*750
        sheet.paste(image,(x,y+32));draw.text((x+8,y+8),row['title'],fill='black')
    sheet.save(root/('premium-sheet-'+str(start//4)+'.jpg'),quality=90)
(root/'premium-face-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf8')
print(len(manifest),'Japanese premium faces for direct badge check')
