import json
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).parent
rows=[r for r in json.loads((root/'psa-originals.json').read_bytes()) if 'local_file' in r and r['product']=='Reflections'][:10]
(root/'batch2-source-manifest.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
for offset in range(0,len(rows),2):
    canvas=Image.new('RGB',(1500,1080),'white');d=ImageDraw.Draw(canvas)
    for x,r in enumerate(rows[offset:offset+2]):
        im=ImageOps.exif_transpose(Image.open(root/r['local_file'])).convert('RGB');w,h=im.size
        crop=(int(.1*w),int(.25*h),int(.95*w),int(.95*h)) if h/w>1.55 and h>1500 else (0,0,w,h)
        im=ImageOps.contain(im.crop(crop),(740,1040));canvas.paste(im,(750*x,30));d.text((750*x+5,5),str(offset+x+1)+' '+r['label'],fill='black')
    canvas.save(root/f'batch2-sheet-{offset//2+1}.webp',quality=92,method=6)
for i,r in enumerate(rows,1):print(i,r['article'],r['local_file'])
