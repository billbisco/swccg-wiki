import json
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright
p=Path(__file__).parent;out=[]
with sync_playwright() as pw:
    browser=pw.chromium.launch(channel='chrome',headless=True)
    try:
        page=browser.new_page()
        for width in [1280,390]:
            page.set_viewport_size(dict(width=width,height=1000));page.goto((p/'preview.html').resolve().as_uri(),wait_until='networkidle')
            assert page.locator('img').evaluate_all('xs=>xs.every(x=>x.complete&&x.naturalWidth)'),width
            assert page.locator('.symbol').count()==24,page.locator('.symbol').count()
            page.locator('#search-check').click();result=page.locator('#search-result').inner_text();assert 'A: no explicit symbol label' in result and 'B: explicit searchable label' in result and 'C: explicit searchable label' in result,result
            symbols=page.locator('.symbol').evaluate_all('xs=>xs.map(x=>({width:x.getBoundingClientRect().width,height:x.getBoundingClientRect().height,corner:getComputedStyle(x).borderRadius}))')
            assert all(abs(x['width']-x['height'])<.1 for x in symbols)
            png=p/('preview-'+str(width)+'.png');page.screenshot(path=str(png),full_page=True);Image.open(png).save(png.with_suffix('.webp'),quality=85);png.unlink()
            page.locator('table').evaluate('x=>x.scrollIntoView({block:"start"})');png=p/('symbols-'+str(width)+'.png');page.screenshot(path=str(png));Image.open(png).save(png.with_suffix('.webp'),quality=85);png.unlink()
            page.locator('.choices').evaluate('x=>x.scrollIntoView({block:"start"})');png=p/('choices-'+str(width)+'.png');page.screenshot(path=str(png));Image.open(png).save(png.with_suffix('.webp'),quality=85);png.unlink()
            out.append(dict(width=width,unbroken_images=True,explicit_search_label_test=result,round_symbol_bounds=symbols,preview='preview-'+str(width)+'.webp'))
    finally:browser.close()
(p/'preview-checks.json').write_text(json.dumps(out,indent=2),encoding='utf8');print('1280/390px: all images render, round symbol bounds pass, B/C expose visible searchable symbol labels')
