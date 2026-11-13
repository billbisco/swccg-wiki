import gzip,json,sys
from pathlib import Path
from urllib.parse import quote
from PIL import Image
from playwright.sync_api import sync_playwright
root=Path(__file__).parent.resolve();mode=sys.argv[1]
if mode=='sandbox':
    targets=[('rotation-dark','Hoth: Echo Command Center (War Room) (Dark) (Japanese)',1280),('rotation-light','Hoth: Echo Command Center (War Room) (Japanese)',1280),('fx7','FX-7 (Effex-Seven) (Japanese)',1280),('rotation-mobile','Hoth: Echo Command Center (War Room) (Japanese)',390)]
    renders=json.load(gzip.open(root/'phase3-sandbox-previews.json.gz','rt',encoding='utf8'))
else:
    targets=[('2-1b','2-1B (Too-Onebee) (Japanese)',1280),('fx7','FX-7 (Effex-Seven) (Japanese)',1280),('r3-t6','R3-T6 (Arthree-Teesix) (Japanese)',1280),('brainiac','Brainiac (Japanese)',1280),('squadron','Y-wing Assault Squadron (Japanese)',1280),('arcona','Arcona (Japanese)',1280),('creature','Wampa (Japanese)',1280),('rotation-dark','Hoth: Echo Command Center (War Room) (Dark) (Japanese)',1280),('rotation-light','Hoth: Echo Command Center (War Room) (Japanese)',1280),('hoth-set','Hoth (Japanese)',1280),('mobile','FX-7 (Effex-Seven) (Japanese)',390),('rotation-mobile','Hoth: Echo Command Center (War Room) (Japanese)',390)]
    renders=None
oldids={}
if mode=='before':
    targets=[('2-1b','2-1B (Too-Onebee) (Japanese)',1280),('fx7','FX-7 (Effex-Seven) (Japanese)',1280),('creature','Wampa (Japanese)',1280)]
    for stage in ['phase1','phase2','phase3']:
        for title,p in json.loads((root/(stage+'-heads.json')).read_bytes()).items():oldids.setdefault(title,p['revisions'][0]['revid'])
results=[]
with sync_playwright() as driver:
    context=driver.chromium.launch_persistent_context(str(root/'qa-profile'),channel='chrome',headless=True)
    try:
        page=context.new_page()
        for name,title,width in targets:
            page.set_viewport_size(dict(width=width,height=1300));url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='')
            if mode=='before':url+='?oldid='+str(oldids[title])
            page.goto(url,wait_until='networkidle',timeout=60000)
            page.locator('#mw-content-text').wait_for()
            if renders:page.locator('#mw-content-text > .mw-parser-output').evaluate('(el,html)=>el.innerHTML=html',renders[title]['text'])
            page.locator('#mw-content-text').evaluate('async el=>await Promise.all([...el.querySelectorAll("img")].map(im=>im.complete?Promise.resolve():new Promise(resolve=>{im.addEventListener("load",resolve,{once:true});im.addEventListener("error",resolve,{once:true})})))')
            page.evaluate('document.fonts.ready')
            data=page.locator('#mw-content-text').evaluate('el=>({citeErrors:el.querySelectorAll(".mw-ext-cite-error").length,brokenImages:[...el.querySelectorAll("img")].filter(x=>!x.complete||!x.naturalWidth).map(x=>x.src),rotation:[...el.querySelectorAll(".card-image-rotation")].map(x=>{let im=x.querySelector("img"),r=im.getBoundingClientRect();return {width:r.width,height:r.height,transform:getComputedStyle(x.firstElementChild).transform}})})')
            assert not data['citeErrors'] and not data['brokenImages'],(title,data)
            if name.startswith('rotation'):assert data['rotation'] and data['rotation'][0]['width']>data['rotation'][0]['height'],data
            png=root/(mode+'-'+name+'.png')
            if width<500:page.screenshot(path=str(png),full_page=False)
            elif name=='hoth-set':page.locator('#Card_list').scroll_into_view_if_needed();page.screenshot(path=str(png),full_page=False)
            else:page.locator('#mw-content-text').screenshot(path=str(png))
            with Image.open(png) as im:im.convert('RGB').save(png.with_suffix('.webp'),quality=80,method=6)
            png.unlink();assert png.with_suffix('.webp').stat().st_size<=500000
            results.append(dict(title=title,url=url,width=width,file=png.with_suffix('.webp').name,**data));print(mode,name,title,flush=True)
    finally:context.close()
(root/(mode+'-visual.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
