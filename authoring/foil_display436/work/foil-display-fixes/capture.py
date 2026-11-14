import json,sys,time
from pathlib import Path
from urllib.parse import quote
from PIL import Image,ImageOps,ImageDraw
from playwright.sync_api import sync_playwright
root=Path(__file__).parent;mode=sys.argv[1];report=[];images=[]
rows=json.loads((root/(('pilot' if mode=='pilot' else 'main')+'-packet.json')).read_bytes())
revids={r['title']:r['revid'] for f in root.glob('*-receipts.jsonl') for r in map(json.loads,f.read_text(encoding='utf8').splitlines())}
titles=[r['title'] for r in rows if not r['title'].startswith('Template:')]
if mode!='pilot':titles=['Reflections','Reflections II: Expanding the Galaxy','Reflections III','Seeking An Audience (Reflections III Foil)','Shmi Skywalker (Reflections III Foil)','Seeking An Audience','Luke Skywalker','Alderaan (Japanese Premiere Light)']
with sync_playwright() as p:
    browser=p.chromium.launch(channel='chrome',headless=True)
    try:
        context=browser.new_context(viewport=dict(width=1280,height=1000));page=context.new_page();cdp=context.new_cdp_session(page);cdp.send('Network.enable');cdp.send('Network.setCacheDisabled',dict(cacheDisabled=True))
        for title in titles:
            if title.startswith('Alderaan'):continue # Japanese dual/control rendered separately by API conservation check.
            for width in ([1280,390] if mode!='pilot' or title in ['Rebel Leadership (Reflections III Foil)','Coruscant: Jedi Council Chamber (Reflections III Foil)'] else [1280]):
                page.set_viewport_size(dict(width=width,height=1000))
                page.goto('https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe=':(),'),wait_until='networkidle',timeout=90000)
                expected=revids.get(title)
                if expected:
                    if page.evaluate('mw.config.get("wgRevisionId")')!=expected:
                        page.goto('https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe=':(),')+'?qa436='+str(expected),wait_until='networkidle',timeout=90000)
                    assert page.evaluate('mw.config.get("wgRevisionId")')==expected,(title,'Stale revision')
                assert page.locator('head').evaluate('el=>el.textContent.includes("card-photo-source")'),(title,'Stale application CSS')
                page.locator('#mw-content-text img').evaluate_all('xs=>xs.forEach(x=>x.loading="eager")')
                page.wait_for_function('()=>[...document.querySelectorAll("#mw-content-text img")].every(x=>x.complete)',timeout=90000)
                result=page.locator('#mw-content-text').evaluate('el=>({broken:[...el.querySelectorAll("img")].filter(x=>!x.naturalWidth).map(x=>x.src),errors:el.querySelectorAll(".mw-ext-cite-error,.error").length,frames:[...el.querySelectorAll(".card-photo")].map(x=>{let v=x.querySelector(".card-photo-viewport"),s=x.querySelector(".card-photo-source"),im=s.querySelector("img"),r=v.getBoundingClientRect(),c=x.querySelector(".card-photo-crop").getBoundingClientRect();return {width:r.width,height:r.height,imageCssWidth:parseFloat(getComputedStyle(im).width),sourceCssWidth:parseFloat(getComputedStyle(s).width),withinViewport:Math.abs(c.width-r.width)<2&&Math.abs(c.height-r.height)<2,original:x.querySelector("small a").href}}),inline:[...el.querySelectorAll("table.card-thumbs td:not(:first-child) img")].map(x=>({width:x.getBoundingClientRect().width,requested:Number(x.getAttribute("width")),source:x.src}))})')
                assert not result['broken'] and not result['errors'],(title,result)
                for f in result['frames']:
                    assert f['withinViewport'] and abs(f['imageCssWidth']-f['sourceCssWidth'])<1,(title,f)
                    assert '/wiki/File:' in f['original']
                assert all(abs(x['width']-x['requested'])<1 for x in result['inline']),(title,result['inline'])
                if mode=='pilot':target=page.locator('.card-photo').first
                elif title in ['Reflections','Reflections II: Expanding the Galaxy','Reflections III']:
                    focus={'Reflections':'Cloud City: Guest Quarters (Reflections Foil)','Reflections II: Expanding the Galaxy':'Gold Squadron 1 (Reflections II Foil)','Reflections III':'Seeking An Audience (Reflections III Foil)'}[title]
                    target=page.locator('table.card-thumbs tr').filter(has=page.locator('td:nth-child(2)>a[title="'+focus+'"]')).first
                else:target=page.locator('.card-rail').first
                target.evaluate('x=>x.scrollIntoView({block:"start",behavior:"instant"})')
                filename=mode+'-'+str(len(report))+'-'+str(width)+'.webp';png=root/(filename+'.png')
                if mode=='pilot':target.screenshot(path=str(png))
                else:page.screenshot(path=str(png))
                with Image.open(png) as im:im.convert('RGB').save(root/filename,quality=82,method=6)
                png.unlink();images.append((title,width,filename));report.append(dict(title=title,width=width,screenshot=filename,revision=page.evaluate('mw.config.get("wgRevisionId")'),**result));print(title,width,'PASS',flush=True)
        context.close()
    finally:browser.close()
(root/(mode+'-visual-checks.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
if mode=='pilot':
    for start in range(0,len(images),6):
        canvas=Image.new('RGB',(1050,900),'#eee');draw=ImageDraw.Draw(canvas)
        for n,(title,width,file) in enumerate(images[start:start+6]):
            x=(n%3)*350;y=(n//3)*450;im=Image.open(root/file);im.thumbnail((335,405));canvas.paste(im,(x+(350-im.width)//2,y+40));draw.text((x+5,y+5),title[:47],fill='black');draw.text((x+5,y+20),str(width),fill='black')
        canvas.save(root/('pilot-contact-'+str(start//6)+'.webp'),quality=85)
