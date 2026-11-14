from pathlib import Path
from PIL import Image,ImageDraw
p=Path(__file__).parent;files=sorted((p/'faces').glob('*'))
for start in range(0,len(files),6):
    canvas=Image.new('RGB',(1200,1240),'#e4e8ec');d=ImageDraw.Draw(canvas)
    for n,f in enumerate(files[start:start+6]):
        im=Image.open(f).convert('RGB');im.thumbnail((375,565));x=(n%3)*400+10;y=(n//3)*620+35;canvas.paste(im,(x,y));d.text((x,y-25),f.name[:49],fill='black')
    canvas.save(p/('face-sheet-'+str(start//6)+'.webp'),quality=92)
print(len(files),'full source faces on three review sheets')
