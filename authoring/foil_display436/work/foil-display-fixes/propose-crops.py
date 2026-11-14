"""Measure physical card rectangles for display; never alter historical originals."""
import json,math
from pathlib import Path
import cv2,numpy as np
from PIL import Image,ImageDraw
root=Path(__file__).parent;prior=Path('work/reflections-foils')
records=[r for r in json.loads((prior/'uploaded-images.json').read_bytes()) if 'PSA' in r['name']]
proposals=[]
for row in records:
    path=prior/row['local_file'];im=Image.open(path);raw=np.array(im.convert('RGB'));h,w=raw.shape[:2];scale=1000/h
    small=cv2.resize(raw,(round(w*scale),1000));gray=cv2.cvtColor(small,cv2.COLOR_RGB2GRAY)
    edges=cv2.Canny(gray,40,100);edges=cv2.morphologyEx(edges,cv2.MORPH_CLOSE,np.ones((3,3),np.uint8))
    contours,_=cv2.findContours(edges,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE);candidates=[]
    for c in contours:
        x,y,cw,ch=cv2.boundingRect(c);ratio=cw/ch;area=cw*ch/(small.shape[0]*small.shape[1])
        if not(.64<ratio<.80 and .30<area<.57 and .23<y/1000<.42 and (y+ch)/1000>.82):continue
        # A complete card edge spans its full rectangle, unlike art/text boxes.
        rect=cv2.minAreaRect(c);rectarea=rect[1][0]*rect[1][1]
        if rectarea<=0:continue
        fill=cv2.contourArea(c)/rectarea
        if fill<.85:continue
        score=abs(math.log(ratio/(63/88)))+abs(area-.43)*2+(1-fill)*.2
        candidates.append((score,x,y,cw,ch,area,fill))
    if candidates:
        best=min(candidates);_,x,y,cw,ch,area,fill=best
        # Retain the physical card's rounded edge with a small safety margin.
        left=max(0,math.floor(x/scale)-3);top=max(0,math.floor(y/scale)-3);right=min(w,math.ceil((x+cw)/scale)+3);bottom=min(h,math.ceil((y+ch)/scale)+3)
        proposal=dict(file=row['name'],local_file=str(path),source_width=w,source_height=h,x=left,y=top,w=right-left,h=bottom-top,confidence_score=best[0],candidate_count=len(candidates))
    else:proposal=dict(file=row['name'],local_file=str(path),source_width=w,source_height=h,needs_measurement=True)
    proposals.append(proposal)
(root/'crop-proposals.json').write_text(json.dumps(proposals,indent=2),encoding='utf8')
for batch in range(math.ceil(len(proposals)/25)):
    page=Image.new('RGB',(1250,1600),'#dde3e8');d=ImageDraw.Draw(page)
    for j,r in enumerate(proposals[batch*25:(batch+1)*25]):
        x=(j%5)*250;y=(j//5)*320;d.text((x+4,y+2),str(batch*25+j)+' '+r['file'].split('-PSA')[0][-28:],fill='black')
        im=Image.open(r['local_file']).convert('RGB');thumb=im.copy();thumb.thumbnail((65,270));page.paste(thumb,(x+4,y+25))
        if not r.get('needs_measurement'):
            crop=im.crop((r['x'],r['y'],r['x']+r['w'],r['y']+r['h']));crop.thumbnail((175,270));page.paste(crop,(x+72,y+25));d.text((x+75,y+296),f"score {r['confidence_score']:.3f}",fill='black')
        else:d.text((x+75,y+100),'MEASURE',fill='red')
    page.save(root/f'crop-sheet-{batch}.webp',quality=86)
print(len(proposals),'holder images;',sum(r.get('needs_measurement',False) for r in proposals),'require manual measurement')
