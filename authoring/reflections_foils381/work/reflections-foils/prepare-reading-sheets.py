"""Inspection-only sheets; preserve/upload the unchanged originals separately."""
import json,sys
from pathlib import Path
from PIL import Image,ImageDraw,ImageOps
root=Path(__file__).parent;stage=sys.argv[1]
selected=json.loads((root/(stage+'-source-manifest.json')).read_bytes())
for i in range(0,len(selected),2):
    images=[]
    for row in selected[i:i+2]:
        im=ImageOps.exif_transpose(Image.open(root/row['local_file'])).convert('RGB')
        w,h=im.size
        if h>=1500 and w<h:im=im.crop((int(.1*w),int(.25*h),int(.95*w),int(.95*h)))
        im.thumbnail((1100,1500));images.append((row,im))
    canvas=Image.new('RGB',(sum(im.width for r,im in images),max(im.height for r,im in images)+55),'white');draw=ImageDraw.Draw(canvas);x=0
    for row,im in images:
        draw.text((x+5,5),row['article'],fill='black');canvas.paste(im,(x,45));x+=im.width
    canvas.save(root/(stage+'-sheet-'+str(i//2+1)+'.webp'),quality=93)
print(len(selected),'originals on',len(range(0,len(selected),2)),'inspection sheets')
