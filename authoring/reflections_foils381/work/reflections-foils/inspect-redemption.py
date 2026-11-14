import json
from pathlib import Path
from PIL import Image
root=Path(__file__).parent;r=next(r for r in json.loads((root/'batch7-source-manifest.json').read_bytes()) if r['label']=='Redemption')
im=Image.open(root/r['local_file']);w,h=im.size;crop=im.crop((round(.12*w),round(.32*h),round(.93*w),round(.47*h)));crop.resize((crop.width*2,crop.height*2)).save(root/'redemption-lore-reading.png')
