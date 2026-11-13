import json
from pathlib import Path
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).parent;rows=json.loads((root/'icon-inspection-manifest.json').read_bytes())
for offset in range(0,len(rows),16):
    out=Image.new('RGB',(1440,1180),'white');d=ImageDraw.Draw(out)
    for j,row in enumerate(rows[offset:offset+16]):
        im=Image.open(root/row['file']).convert('RGB');w,h=im.size;x=(j%4)*360;y=(j//4)*295
        left=ImageOps.contain(im.crop((0,h*.62,w*.25,h)),(105,255))
        right=ImageOps.contain(im.crop((w*.55,h*.62,w,h)),(250,255))
        out.paste(left,(x,y+32));out.paste(right,(x+108,y+32));d.text((x+3,y+2),str(row['icon_number'])+' '+row['title'][:37],fill='black')
    out.save(root/f'icon-corners-{offset//16+1:02d}.jpg',quality=95)
