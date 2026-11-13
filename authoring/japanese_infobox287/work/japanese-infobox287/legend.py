import json,re,sys
from pathlib import Path
import requests
from PIL import Image,ImageDraw
sys.path.insert(0,'work')
from audit_wiki_card_titles import get,pages
root=Path(__file__).parent
labels=["Anakin's Lightsaber","Obi-Wan's Lightsaber",'Brainiac','Wedge Antilles',"Mara Jade, The Emperor's Hand"]
heads=pages(labels)
print({t:re.findall(r'(?m)^\|(?:set|set_icon)=.*',p['revisions'][0]['slots']['main']['content']) for t,p in heads.items() if 'revisions' in p})
names=['File:Icon-set-premium.png','File:Icon-set-Hoth.png','File:Icon-set-A-New-Hope.png','File:Icon-set-Reflections-II.png','File:Icon-set-Special-Edition.png','File:Icon-set-Death-Star-II.png']
result=get(action='query',titles='|'.join(names),prop='imageinfo',iiprop='url')['query']['pages']
sheet=Image.new('RGB',(900,400),'#e4e8ec');draw=ImageDraw.Draw(sheet)
for i,page in enumerate(result):
    draw.text(((i%3)*300+5,(i//3)*200+5),page['title'],fill='black')
    if page.get('missing'):continue
    path=root/('legend-'+str(i)+'.png')
    response=requests.get(page['imageinfo'][0]['url'],timeout=30);response.raise_for_status();path.write_bytes(response.content)
    image=Image.open(path).convert('RGBA');image.thumbnail((130,130));sheet.paste(image,((i%3)*300+70,(i//3)*200+40),image)
sheet.save(root/'icon-legend.png')
(root/'legend-files.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf8')
