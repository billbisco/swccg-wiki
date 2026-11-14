import json
from pathlib import Path
from urllib.parse import quote
from PIL import Image,ImageDraw
from playwright.sync_api import sync_playwright
root=Path(__file__).parent;old=json.loads((root/'first-family-heads.json').read_bytes())
targets=[('black2-foil','Black 2 (Reflections Foil)',1280,None),('attack-run','Attack Run (Reflections Foil)',1280,None),('21b','2-1B (Too-Onebee) (Reflections Foil)',1280,None),('biggs','Biggs Darklighter (Reflections Foil)',1280,None),('21b-mobile','2-1B (Too-Onebee) (Reflections Foil)',390,None),('black2-before','Black 2',1280,old['Black 2']['revisions'][0]['revid']),('black2-after','Black 2',1280,None)]
rows=[]
with sync_playwright() as p:
    context=p.chromium.launch_persistent_context(str(root/'qa-profile'),channel='chrome',headless=True)
    try:
        page=context.new_page()
        for name,title,width,oldid in targets:
            page.set_viewport_size(dict(width=width,height=1300));url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='')+('?oldid='+str(oldid) if oldid else '')
            page.goto(url,wait_until='networkidle',timeout=60000)
            page.locator('#mw-content-text').evaluate('async el=>await Promise.all([...el.querySelectorAll("img")].map(im=>im.complete?Promise.resolve():new Promise(resolve=>{im.addEventListener("load",resolve,{once:true});im.addEventListener("error",resolve,{once:true})})))')
            page.evaluate('document.fonts.ready')
            checks=page.locator('#mw-content-text').evaluate('el=>({citeErrors:el.querySelectorAll(".mw-ext-cite-error").length,infoboxes:el.querySelectorAll("table.card-infobox").length,brokenImages:[...el.querySelectorAll("img")].filter(x=>!x.naturalWidth).map(x=>x.src)})')
            assert checks['infoboxes']==1 and not checks['citeErrors'] and not checks['brokenImages'],(title,checks)
            file=root/(name+'.png')
            if width<500:page.screenshot(path=str(file),full_page=False)
            else:page.locator('#mw-content-text').screenshot(path=str(file))
            with Image.open(file) as im:im.convert('RGB').save(file.with_suffix('.webp'),quality=80,method=6)
            file.unlink();assert file.with_suffix('.webp').stat().st_size<=500000
            rows.append(dict(title=title,url=url,width=width,file=file.with_suffix('.webp').name,**checks));print(name,flush=True)
    finally:context.close()
(root/'first-visual-verification.json').write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
canvas=Image.new('RGB',(1100,920),'white');draw=ImageDraw.Draw(canvas)
for x,name,label in [(0,'black2-before','Before: original family navigation'),(550,'black2-after','After: foil linked; other content preserved')]:
    im=Image.open(root/(name+'.webp')).convert('RGB');im.thumbnail((540,880));canvas.paste(im,(x,35));draw.text((x+8,10),label,fill='black')
canvas.save(root/'first-navigation-comparison.webp',quality=80,method=6)
