from pathlib import Path
from PIL import Image,ImageDraw,ImageOps
root=Path(__file__).parent
sheet=Image.new('RGB',(1000,650),'white');draw=ImageDraw.Draw(sheet)
for i,n in enumerate([0,1,2,4,6,7,9,12,14,16]):
    image=ImageOps.exif_transpose(Image.open(root/'icon-faces'/str(n))).convert('RGB')
    crop=image.crop((int(image.width*.82),int(image.height*.13),int(image.width*.99),int(image.height*.29)))
    crop=crop.resize((180,260))
    x=(i%5)*200;y=(i//5)*320
    sheet.paste(crop,(x,y+25));draw.text((x+5,y+4),str(n),fill='black')
sheet.save(root/'badge-details.jpg',quality=95)
