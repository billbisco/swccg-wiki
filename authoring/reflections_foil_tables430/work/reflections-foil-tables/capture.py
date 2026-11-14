"""Native desktop/mobile table and empty-image fixture checks; no detached browser."""
import json,sys
from pathlib import Path
from urllib.parse import quote
from PIL import Image
from playwright.sync_api import sync_playwright
import requests
from bs4 import BeautifulSoup
root=Path(__file__).parent;mode=sys.argv[1];report=[]
def save(page,file,locator=None):
    png=root/(file+'.png')
    if locator:locator.screenshot(path=str(png))
    else:page.screenshot(path=str(png))
    with Image.open(png) as im:im.convert('RGB').save(png.with_suffix('.webp'),quality=80,method=6)
    png.unlink()
with sync_playwright() as p:
    context=p.chromium.launch_persistent_context(str(root/'qa-profile'),channel='chrome',headless=True)
    try:
        page=context.new_page()
        cdp=context.new_cdp_session(page);cdp.send('Network.enable');cdp.send('Network.setCacheDisabled',dict(cacheDisabled=True))
        if mode=='fixture':
            text='''== Scan request preview ==
{| class="wikitable"
! Empty image field !! Missing image file
|-
| {{Card scan request|card=Luke Skywalker (Reflections Foil)}} || {{#ifexist:File:430-QA-absent-image.png|WRONG: file unexpectedly exists|{{Card scan request|card=Luke Skywalker (Reflections Foil)}}}}
|}
'''
            response=requests.post('https://wiki.swccg.com/api.php',data=dict(action='parse',format='json',formatversion=2,title='User:Memory Core ChatGPT/Scan request preview',text=text,prop='text'),timeout=60);response.raise_for_status();html=response.json()['parse']['text'];soup=BeautifulSoup(html,'html.parser');markers=soup.select('.card-scan-request');assert len(markers)==2 and 'WRONG:' not in soup.get_text()
            for marker in markers:
                assert 'Scan requested' in marker.get_text() and marker.find('a',string='Contribute a scan')
                assert marker.select('span[aria-hidden="true"]')
            (root/'scan-request-fixture.html').write_text(html,encoding='utf8')
            page.set_viewport_size(dict(width=1000,height=600));page.goto('https://wiki.swccg.com/wiki/Template:Card_scan_request',wait_until='networkidle')
            page.locator('#mw-content-text').evaluate('(el,html)=>el.innerHTML=html',html);save(page,'scan-request-fixture',page.locator('#mw-content-text'))
            report.append(dict(empty_image_marker=True,nonexistent_image_marker=True,text_label=True,upload_and_discussion_links=True,native_preview_not_saved_as_missing_card=True,file='scan-request-fixture.webp'))
        else:
            titles=['Reflections'] if mode=='pilot' else ['Reflections II: Expanding the Galaxy','Reflections III']
            focuses={'Reflections':'Rendezvous Point (Reflections Foil)','Reflections II: Expanding the Galaxy':'Brainiac (Japanese Reflections II Foil)','Reflections III':'Darth Maul (AI) (Reflections III Foil)'}
            if mode=='focus':titles=list(focuses)
            for title in titles:
                for width in ([1280] if mode=='focus' else [1280,390]):
                    page.set_viewport_size(dict(width=width,height=1200));page.goto('https://wiki.swccg.com/wiki/'+quote(title.replace(' ','_'),safe=':(),'),wait_until='networkidle',timeout=60000)
                    expected=max(r['revid'] for f in root.glob('*-receipts.jsonl') for r in map(json.loads,f.read_text(encoding='utf8').splitlines()) if r['title']==title)
                    assert page.evaluate('mw.config.get("wgRevisionId")')==expected,(title,'Browser is not showing the saved revision')
                    page.locator('img').evaluate_all('imgs=>imgs.forEach(im=>im.loading="eager")')
                    page.wait_for_function('()=>[...document.querySelectorAll("#mw-content-text img")].every(im=>im.complete)',timeout=60000)
                    result=page.locator('#mw-content-text').evaluate('el=>({brokenImages:[...el.querySelectorAll("img")].filter(im=>!im.naturalWidth).map(im=>im.src),citeErrors:el.querySelectorAll(".mw-ext-cite-error").length,foilTables:[...el.querySelectorAll("table.card-thumbs")].filter(t=>t.caption&&t.caption.textContent.includes("Side foils (")).length})')
                    assert not result['brokenImages'] and not result['citeErrors'] and result['foilTables']==2,(title,result)
                    result['rotated_bounds']=page.locator('table.card-thumbs div[style*="rotate(-90deg)"]').evaluate_all('els=>els.map(el=>{let a=el.querySelector("img").getBoundingClientRect(),b=el.parentElement.getBoundingClientRect();return {withinCell:a.left>=b.left-2&&a.right<=b.right+2&&a.top>=b.top-2&&a.bottom<=b.bottom+2,imageWidth:a.width,cellWidth:b.width}})')
                    assert all(r['withinCell'] for r in result['rotated_bounds']),(title,'Rotated image extends outside cell',result['rotated_bounds'])
                    page.locator('#Foil_cards').evaluate('el=>el.scrollIntoView({block:"start",behavior:"instant"})')
                    result['foil_heading_top']=page.locator('#Foil_cards').evaluate('el=>el.getBoundingClientRect().top')
                    assert -2<=result['foil_heading_top']<150,(title,width,result)
                    if mode=='focus':
                        row=page.locator('table.card-thumbs tr').filter(has=page.locator('td:nth-child(2) > a[title="'+focuses[title]+'"]')).first
                        row.evaluate('el=>el.scrollIntoView({block:"start",behavior:"instant"})');result['focused_article']=focuses[title]
                    file=title.split(':')[0].replace(' ','-')+'-'+str(width)+('-focus' if mode=='focus' else '');save(page,file)
                    report.append(dict(title=title,width=width,file=file+'.webp',**result));print(title,width,flush=True)
        (root/(mode+'-visual-checks.json')).write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf8')
    finally:context.close()
