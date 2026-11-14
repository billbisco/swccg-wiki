import json
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
root=Path(__file__).parent;out=[]
with sync_playwright() as p:
    browser=p.chromium.launch(channel='chrome',headless=True)
    try:
        page=browser.new_page(viewport=dict(width=390,height=900));cdp=page.context.new_cdp_session(page);cdp.send('Network.enable');cdp.send('Network.setCacheDisabled',dict(cacheDisabled=True))
        page.goto('https://wiki.swccg.com/wiki/Reflections_III',wait_until='networkidle')
        row=page.locator('table.card-thumbs tr').filter(has=page.locator('td:nth-child(2)>a[title="Seeking An Audience (Reflections III Foil)"]')).first
        cell=row.locator('td').nth(6);cell.evaluate('el=>el.scrollIntoView({block:"start",inline:"start",behavior:"instant"})')
        bounds=cell.bounding_box();assert bounds['x']>=-2 and bounds['x']<390,bounds
        sizes=cell.locator('img').evaluate_all('xs=>xs.map(x=>x.getBoundingClientRect().width)');assert sizes and max(sizes)<=20,sizes
        png=root/'mobile-inline-symbols.png';page.screenshot(path=str(png));Image.open(png).save(root/'mobile-inline-symbols.webp',quality=85);png.unlink()
        out.append(dict(title='Reflections III',width=390,game_text_column_reachable=True,inline_symbol_widths=sizes,screenshot='mobile-inline-symbols.webp'))
        for title in ['Alderaan_(Japanese)','Alderaan_(Dark)_(Japanese)']:
            page.goto('https://wiki.swccg.com/wiki/'+title,wait_until='networkidle');page.locator('.card-rail').first.evaluate('el=>el.scrollIntoView({block:"start",behavior:"instant"})')
            assert page.locator('.card-infobox').count()==1
            page.locator('.card-rail img').evaluate_all('xs=>xs.forEach(x=>x.loading="eager")');page.wait_for_function('()=>[...document.querySelectorAll(".card-rail img")].every(x=>x.complete&&x.naturalWidth)')
            assert page.locator('.card-photo').count()==0
            png=root/(title+'.png');page.screenshot(path=str(png));Image.open(png).save(png.with_suffix('.webp'),quality=82);png.unlink()
            out.append(dict(title=title,width=390,unframed_Japanese_control=True,infobox=True,unbroken_rail_images=page.locator('.card-rail img').count(),screenshot=title+'.webp'))
    finally:browser.close()
(root/'extra-visual-checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print('Mobile game text reachable, icons 20px; both Japanese Alderaan controls PASS')
