const {chromium}=require('./browser-qa/node_modules/playwright-core');
const fs=require('node:fs/promises');
const path=require('node:path');
const assert=require('node:assert/strict');
const B=path.join(__dirname,'batch2');
(async()=>{
 const report=JSON.parse(await fs.readFile(path.join(B,'browser-checks.json'),'utf8'));
 assert.equal(Object.keys(report.desktop).filter(k=>k!=='guestPreference').length,12);
 assert.equal(Object.keys(report.mobile).filter(k=>k!=='guestPreference').length,12);
 assert.equal(report.desktop.guestPreference.perCardDoesNotRewriteDefault,true);
 assert.equal(report.mobile.guestPreference.persistsAcrossNavigation,true);
 await fs.writeFile(path.join(B,'browser-checks-failed-label.json'),JSON.stringify(report,null,2));
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 try{
  const context=await browser.newContext({viewport:{width:1440,height:1000},serviceWorkers:'block'});
  await context.route('**/*',r=>{const host=new URL(r.request().url()).hostname;return host==='archive.org'||host.endsWith('.archive.org')?r.abort():r.continue();});
  const page=await context.newPage();await page.goto('https://wiki.swccg.com/wiki/BoShek_(V)_(Virtual_Set_1)_(Errata_2)?uselang=fr');
  await page.waitForSelector('.swccg-card-image-choices');
  assert.equal(await page.getByRole('button',{name:'Remasterisé',exact:true}).count(),1);
  assert.ok((await page.locator('.mw-parser-output').textContent()).includes('Adds 3 to power'));
  await page.getByRole('button',{name:'Remasterisé',exact:true}).click();
  assert.equal(await page.locator('.swccg-card-image-choices button[aria-pressed="true"]').textContent(),'Remasterisé');
  const source=await page.locator('.swccg-card-image-stage .card-portrait:not([hidden]) img').getAttribute('src');assert.ok(source.includes('OVS1-01-BoShek-remaster'));
  await page.screenshot({path:path.join(B,'headless-boshek-french-ui.jpg'),fullPage:true});
  report.translatedInterface={locale:'fr',imageLanguage:'en',localizedRemasteredButton:true,englishCardStateUnchanged:true};
  report.harnessCorrection='The generated test initially decoded its UTF-8 French label through the Windows locale. The live response was correctly French. Builder now reads UTF-8 explicitly; corrected literal label/click and unchanged English text/image verified in a fresh isolated browser. All 24 prior desktop/phone card checks remain valid on the same deployment.';
  delete report.error;report.result='PASS';await fs.writeFile(path.join(B,'browser-checks.json'),JSON.stringify(report,null,2));
  console.log(JSON.stringify({result:'PASS',desktopCards:12,mobileCards:12,FrenchUiEnglishCard:'PASS',applicationChanges:0}));
 }finally{await browser.close();}
})().catch(e=>{console.error(e.stack);process.exitCode=1;});
