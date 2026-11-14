import json,sys
from pathlib import Path
from urllib.parse import quote
from PIL import Image
from playwright.sync_api import sync_playwright
root=Path(__file__).parent;stage=sys.argv[1];readings=json.loads((root/(stage+'-readings.json')).read_bytes());rows=[]
targets=[(readings[i]['article'],1280) for i in sorted(set([0,1,len(readings)//2,len(readings)-1])) if i<len(readings)]+[(readings[0]['article'],390)]
offset=0
if '--focus' in sys.argv:
    focus=sys.argv[sys.argv.index('--focus')+1];r=next(r for r in readings if r['printed_title']==focus)
    targets=[(r['article'],1280),(r['article'],390)]
    if (root/(stage+'-visual-verification.json')).exists():rows=json.loads((root/(stage+'-visual-verification.json')).read_bytes());offset=len(rows)
with sync_playwright() as p:
    context=p.chromium.launch_persistent_context(str(root/'qa-profile'),channel='chrome',headless=True)
    try:
        page=context.new_page()
        for index,(title,width) in enumerate(targets):
            page.set_viewport_size(dict(width=width,height=1300));url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='');page.goto(url,wait_until='networkidle',timeout=60000)
            page.locator('#mw-content-text').evaluate('async el=>await Promise.all([...el.querySelectorAll("img")].map(im=>im.complete?Promise.resolve():new Promise(resolve=>{im.addEventListener("load",resolve,{once:true});im.addEventListener("error",resolve,{once:true})})))')
            page.evaluate('document.fonts.ready');checks=page.locator('#mw-content-text').evaluate('el=>({citeErrors:el.querySelectorAll(".mw-ext-cite-error").length,infoboxes:el.querySelectorAll("table.card-infobox").length,brokenImages:[...el.querySelectorAll("img")].filter(x=>!x.naturalWidth).map(x=>x.src)})')
            assert checks['infoboxes']==1 and not checks['citeErrors'] and not checks['brokenImages'],(title,checks)
            file=root/(stage+'-visual-'+str(index+offset)+'.png')
            if width<500:page.screenshot(path=str(file),full_page=False)
            else:page.locator('#mw-content-text').screenshot(path=str(file))
            with Image.open(file) as im:im.convert('RGB').save(file.with_suffix('.webp'),quality=80,method=6)
            file.unlink();rows.append(dict(title=title,url=url,width=width,file=file.with_suffix('.webp').name,**checks));print(title,width,flush=True)
    finally:context.close()
(root/(stage+'-visual-verification.json')).write_text(json.dumps(rows,ensure_ascii=False,indent=2),encoding='utf8')
