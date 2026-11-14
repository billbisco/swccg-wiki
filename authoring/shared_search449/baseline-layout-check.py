import json
from pathlib import Path
from playwright.sync_api import sync_playwright
p=Path(__file__).parent;result={}
with sync_playwright() as pw:
    b=pw.chromium.launch(channel='chrome',headless=True)
    for variant in ['before','pilot']:
        page=b.new_page()
        if variant=='before':page.route('**/js/gemp-016/cards/CardFilter.js?*',lambda r:r.fulfill(body=(p/'CardFilter.before.js').read_bytes(),content_type='application/javascript'))
        page.goto('https://test.swccg.com/deckBuild.html',wait_until='networkidle')
        result[variant]=page.locator('#resetAllFiltersButton').evaluate('x=>{let r=x.getBoundingClientRect(),top=document.elementFromPoint(r.x+r.width/2,r.y+r.height/2);return {x:r.x,y:r.y,width:r.width,height:r.height,clickable:x===top||x.contains(top),topTag:top.tagName,topClass:top.className}}')
        page.close()
    b.close()
(p/'baseline-layout-report.json').write_text(json.dumps(result,indent=2),encoding='utf8')
print(json.dumps(result))
