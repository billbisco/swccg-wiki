import gzip,json,sys
from pathlib import Path
from urllib.parse import quote
from PIL import Image
from playwright.sync_api import sync_playwright
root=Path(__file__).parent.resolve();mode=sys.argv[1]
titles=json.loads((root/('sample-titles.json' if mode=='sandbox' else 'final-sample-titles.json')).read_bytes())
renders=json.load(gzip.open(root/'drafts-renders.json.gz','rt',encoding='utf8')) if mode=='sandbox' else None
results=[]
with sync_playwright() as driver:
    browser=driver.chromium.launch_persistent_context(str(root/'qa-browser-profile'),channel='chrome',headless=True,viewport={'width':1300,'height':1100})
    try:
        page=browser.new_page()
        for i,title in enumerate(titles,1):
            url='https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe='')
            page.goto(url,wait_until='networkidle',timeout=60000)
            if renders:
                page.locator('#mw-content-text > .mw-parser-output').evaluate('(el,html)=>el.innerHTML=html',renders[title]['text'])
            page.evaluate('document.fonts.ready')
            page.locator('#mw-content-text').screenshot(path=str(root/f'{mode}-{i:02d}.png'))
            with Image.open(root/f'{mode}-{i:02d}.png') as image:image.convert('RGB').save(root/f'{mode}-{i:02d}.webp',quality=78,method=6)
            (root/f'{mode}-{i:02d}.png').unlink()
            checks=page.locator('#mw-content-text').evaluate('el=>({tables:el.querySelectorAll(".card-infobox").length,errors:el.querySelectorAll(".mw-ext-cite-error").length,brokenImages:[...el.querySelectorAll("img")].filter(x=>!x.complete||x.naturalWidth===0).map(x=>x.src),text:el.innerText})')
            results.append(dict(title=title,url=url,file=f'{mode}-{i:02d}.webp',**checks))
            assert checks['tables']==1 and not checks['errors'] and not checks['brokenImages'],results[-1]
            print(mode,i,title,flush=True)
    finally:browser.close()
(root/(mode+'-visual.json')).write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf8')
