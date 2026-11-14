"""Inspection-only regular/AI/original-foil comparisons; no source pixels edited."""
import hashlib,json,sys
from pathlib import Path
import requests
from PIL import Image,ImageDraw,ImageOps
sys.path.insert(0,'work/japanese-infobox287/vendor');import mwparserfromhell as mw
root=Path(__file__).parent;folder=root/'artwork-reference';folder.mkdir(exist_ok=True)
manifest=[r for r in json.loads((root/'manifest.json').read_bytes()) if r['product']=='Reflections III' and r['alternate_image']]
sources=json.loads((root/'psa-originals.json').read_bytes())+list(map(json.loads,(root/'swca-originals-results.jsonl').read_text().splitlines()));rows=[]
def fetch(titles,prop,**more):
    r=requests.get('https://wiki.swccg.com/api.php',params=dict(action='query',format='json',formatversion=2,titles='|'.join(titles),prop=prop,**more),timeout=60);r.raise_for_status();return r.json()['query']['pages']
titles=[t for r in manifest for t in [r['label'],r['label']+' (AI)']];heads={p['title']:p for p in fetch(titles,'revisions',rvprop='ids|timestamp|content',rvslots='main')}
for index,m in enumerate(manifest):
    source=next(r for r in sources if r.get('article')==m['proposed_article']);panels=[];record=dict(article=m['proposed_article'],source_photo=source['local_file'],source_sha256=source['sha256'],references=[])
    for title in [m['label'],m['label']+' (AI)']:
        head=heads[title];text=head['revisions'][0]['slots']['main']['content'];t=next(t for t in mw.parse(text).filter_templates(recursive=False) if str(t.name).strip()=='Card');name=str(t.get('image').value).strip();file=fetch(['File:'+name],'imageinfo',iiprop='url|sha1|timestamp')[0];info=file['imageinfo'][0];data=requests.get(info['url'],timeout=60);data.raise_for_status();path=folder/(str(index)+'-'+str(len(panels))+Path(name).suffix);path.write_bytes(data.content);record['references'].append(dict(title=title,revid=head['revisions'][0]['revid'],file=file['title'],url=info['url'],sha256=hashlib.sha256(data.content).hexdigest(),version=info['timestamp']));im=Image.open(path).convert('RGB');im.thumbnail((420,800));panels.append((title,im))
    im=ImageOps.exif_transpose(Image.open(root/source['local_file'])).convert('RGB');w,h=im.size
    if h>=1500 and w<h:im=im.crop((int(.1*w),int(.25*h),int(.95*w),int(.95*h)))
    im.thumbnail((620,800));panels.append(('Actual Reflections III foil',im));canvas=Image.new('RGB',(sum(i.width for _,i in panels)+40,max(i.height for _,i in panels)+65),'white');draw=ImageDraw.Draw(canvas);x=10
    for label,im in panels:draw.text((x,8),label,fill='black');canvas.paste(im,(x,55));x+=im.width+10
    file=root/('artwork-comparison-'+str(index+1)+'.webp');canvas.save(file,quality=92);record['comparison']=file.name;rows.append(record);print(index+1,m['proposed_article'],flush=True)
(root/'artwork-comparisons.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
