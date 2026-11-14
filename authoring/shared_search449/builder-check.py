"""Exercise the actual classic builder and popup with the public native page."""
import json,sys
from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
p=Path(__file__).parent;phase=sys.argv[1] if len(sys.argv)>1 else 'test'
with sync_playwright() as pw:
    b=pw.chromium.launch(channel='chrome',headless=True)
    c=b.new_context();page=c.new_page();writes=[];requests=[]
    page.on('request',lambda r:requests.append({'method':r.method,'url':r.url}))
    page.goto(f'https://{phase}.swccg.com/gemp-swccg/deckBuild.html',wait_until='networkidle')
    page.locator('#sharedSearchPilot449').wait_for()
    assert page.locator('#formatSelect').input_value()=='anything_goes'
    page.locator('#formatSelect').select_option('premiere')
    page.locator('#setSelect').select_option('2')
    page.locator('#nameInput').fill('Officer Evax');page.locator('#nameInput').dispatch_event('change')
    before=page.locator('#formatSelect,#setSelect,#sideSelect,#productSelect').evaluate_all('xs=>xs.map(x=>[x.id,x.value])')
    with page.expect_popup() as popup:page.locator('#sharedSearchPilot449').click()
    child=popup.value;child.wait_for_function('window.SharedSearchPilot && window.SharedSearchPilot.last')
    assert child.locator('[data-result-id]').count()==1
    assert child.locator('[data-result-id]').first.get_attribute('data-result-id')=='2_98o'
    child.get_by_role('button',name='Reset',exact=True).click()
    # Untrusted source and wrong origin must not change the builder title.
    page.evaluate("window.dispatchEvent(new MessageEvent('message',{origin:location.origin,source:window,data:{type:'swccg-search-pilot-title',title:'REJECT ME'}}))")
    assert page.locator('#nameInput').input_value()=='Officer Evax'
    child.evaluate("opener.postMessage({type:'swccg-search-pilot-title',title:'x'.repeat(121)},location.origin)")
    page.wait_for_timeout(100);assert page.locator('#nameInput').input_value()=='Officer Evax'
    target=child.locator('[data-result-id="1_105o"]')
    target.get_by_role('button',name='Search title in builder',exact=True).click()
    page.wait_for_function("document.querySelector('#nameInput').value==='Rebel Barrier'")
    assert page.locator('#formatSelect,#setSelect,#sideSelect,#productSelect').evaluate_all('xs=>xs.map(x=>[x.id,x.value])')==before
    assert page.locator('#filterTable').count()==1
    png=p/f'builder-{phase}.png';page.screenshot(path=str(png));Image.open(png).save(png.with_suffix('.webp'),quality=83);png.unlink()
    child.close();page.locator('#resetAllFiltersButton').evaluate('x=>x.click()')
    assert page.locator('#formatSelect').input_value()=='anything_goes'
    assert page.locator('#nameInput').input_value()==''
    assert not [r for r in requests if any(x in r['url'].lower() for x in ['/savedeck','/decks/save','/decks/delete'])],requests
    report={'phase':phase,'native_url':page.url,'auth':'public unauthenticated page; real backend requests, no mocks','native_button_and_popup':'PASS','title_roundtrip':'Officer Evax to popup / Rebel Barrier to builder','format_set_side_product_preserved':before,'wrong_source_and_overlength_message_rejected':True,'reset_to_anything_goes':'PASS via DOM click; pre-existing collection pane overlaps reset button at this viewport','requests':requests}
    (p/f'builder-{phase}-report.json').write_text(json.dumps(report,indent=2),encoding='utf8')
    b.close()
print(phase,'native builder entry, real popup, title roundtrip, filter preservation, guards and reset PASS')
