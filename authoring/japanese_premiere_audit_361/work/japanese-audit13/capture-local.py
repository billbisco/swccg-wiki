import json
import sys
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright

root=Path('work/japanese-audit13').resolve()
old=json.loads((root/'census.json').read_bytes())[0]['revid']
targets=[
('before',f'https://wiki.swccg.com/index.php?title=2X-3KPR_(Tooex)_(Japanese)&oldid={old}',1200,1500),
('diff',f'https://wiki.swccg.com/index.php?title=2X-3KPR_(Tooex)_(Japanese)&diff=299853&oldid={old}',1200,1500),
('after','https://wiki.swccg.com/wiki/2X-3KPR_(Tooex)_(Japanese)',1200,1500),
('location','https://wiki.swccg.com/wiki/Alderaan_(Japanese)',1200,1500),
('translation','https://wiki.swccg.com/wiki/Ponda_Baba_(Japanese)#Translation_of_Japanese_Text',1200,1500),
('mobile','https://wiki.swccg.com/wiki/2X-3KPR_(Tooex)_(Japanese)',390,1500),
]
with sync_playwright() as driver:
    context=driver.chromium.launch_persistent_context(str(root/'qa-browser-profile'),channel='chrome',headless=True)
    try:
        page=context.new_page()
        for name,url,width,height in targets:
            if len(sys.argv)>1 and name!=sys.argv[1]:continue
            page.set_viewport_size(dict(width=width,height=height))
            page.goto(url,wait_until='networkidle',timeout=45000)
            page.evaluate('document.fonts.ready')
            png=root/(name+'.png')
            page.screenshot(path=str(png),full_page=name not in ['mobile','diff'])
            with Image.open(png) as image:image.save(root/(name+'.webp'),format='WEBP',quality=82,method=6)
            assert (root/(name+'.webp')).stat().st_size<500000
            png.unlink()
            print(name,page.title(),flush=True)
            if name=='mobile':
                page.locator('#Translation_of_Japanese_Text').scroll_into_view_if_needed()
                page.screenshot(path=str(root/'mobile-lower.png'))
                with Image.open(root/'mobile-lower.png') as image:image.save(root/'mobile-lower.webp',format='WEBP',quality=82,method=6)
                (root/'mobile-lower.png').unlink()
    finally:context.close()
