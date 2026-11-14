const {chromium}=require('./browser-qa/node_modules/playwright-core');
const fs=require('node:fs/promises');
const path=require('node:path');
const assert=require('node:assert/strict');
const crypto=require('node:crypto');
const ROOT=path.resolve(__dirname,'batch2');
const pages=Object.fromEntries(require('./batch2/inventory.json').map(r=>[r.key,r.canonical.replaceAll(' ','_')]));
const report={desktop:{},mobile:{},archiveRequestsMade:0,archiveRequestsBlocked:0,desktopControl:false,separateHeadlessProfile:true};
async function guard(context){await context.route('**/*',route=>{const host=new URL(route.request().url()).hostname;if(host==='archive.org'||host.endsWith('.archive.org')){report.archiveRequestsBlocked++;return route.abort();}return route.continue();});}
async function ready(page){await page.waitForSelector('.swccg-card-image-choices');await page.waitForFunction(()=>[...document.querySelectorAll('.card-rail img')].filter(i=>i.getClientRects().length).every(i=>i.complete&&i.naturalWidth>0));}
async function state(page){return page.evaluate(()=>{const rail=document.querySelector('.card-rail'),stage=rail.querySelector('.swccg-card-image-stage'),slip=rail.querySelector(':scope > .card-portrait'),controls=rail.querySelector('.swccg-card-image-choices'),info=rail.querySelector('table');const rect=e=>{const r=e.getBoundingClientRect();return {top:r.top,bottom:r.bottom,width:r.width,height:r.height}};return {width:innerWidth,screenWidth:screen.width,pageWidth:document.documentElement.scrollWidth,viewport:document.querySelector('meta[name="viewport"]').content,stage:rect(stage),slip:rect(slip),controls:rect(controls),info:rect(info),buttonHeights:[...controls.querySelectorAll('button')].map(b=>b.getBoundingClientRect().height),pressed:[...controls.querySelectorAll('button')].map(b=>({text:b.textContent,pressed:b.getAttribute('aria-pressed')})),visibleFullCards:stage.querySelectorAll('.card-portrait:not([hidden])').length,text:document.querySelector('.mw-parser-output').textContent,slipFile:slip.querySelector('a').getAttribute('href')};});}
(async()=>{
 const browser=await chromium.launch({executablePath:'C:/Program Files/Google/Chrome/Application/chrome.exe',headless:true});
 try{
  for(const mode of ['desktop','mobile']){
   const mobile=mode==='mobile';const context=await browser.newContext({viewport:{width:mobile?390:1440,height:mobile?844:1000},screen:{width:mobile?390:1440,height:mobile?844:1000},isMobile:mobile,hasTouch:mobile,deviceScaleFactor:1,serviceWorkers:'block'});await guard(context);
   const page=await context.newPage();page.on('pageerror',e=>{report.pageErrors??=[];report.pageErrors.push(e.message);});
   for(const [key,title]of Object.entries(pages)){
    await page.goto('https://wiki.swccg.com/wiki/'+title);await ready(page);
    await page.getByRole('button',{name:'Original',exact:true}).click();const before=await state(page);
    await page.evaluate(phone=>phone?document.querySelector('.card-nav').scrollIntoView({block:'start'}):window.scrollTo(0,0),mobile);
    await page.screenshot({path:path.join(ROOT,`headless-${key}-${mode}-original.jpg`),fullPage:!mobile});
    await page.getByRole('button',{name:'Remastered',exact:true}).click();await ready(page);const after=await state(page);
    await page.evaluate(phone=>phone?document.querySelector('.card-nav').scrollIntoView({block:'start'}):window.scrollTo(0,0),mobile);
    await page.screenshot({path:path.join(ROOT,`headless-${key}-${mode}-remastered.jpg`),fullPage:!mobile});
    report[mode][key]={...after,text:undefined,articleTextSha256:crypto.createHash('sha256').update(after.text).digest('hex'),textConserved:before.text===after.text,stageHeightConserved:before.stage.height===after.stage.height,slipConserved:before.slipFile===after.slipFile};
    assert.equal(before.text,after.text);assert.equal(before.stage.height,after.stage.height);assert.equal(before.slipFile,after.slipFile);assert.equal(after.visibleFullCards,1);assert.ok(after.stage.bottom<=after.slip.top+.1);assert.ok(after.slip.bottom<=after.controls.top);assert.ok(after.controls.bottom<=after.info.top);
    if(mobile){assert.equal(after.width,390);assert.ok(after.pageWidth<=390);assert.equal(after.viewport,'width=device-width, initial-scale=1');assert.ok(after.buttonHeights.every(n=>n>=36));}
    await page.getByRole('button',{name:'Original',exact:true}).focus();await page.keyboard.press('ArrowRight');assert.equal(await page.locator('.swccg-card-image-choices button[aria-pressed="true"]').textContent(),'Remastered');await page.keyboard.press('Home');assert.equal(await page.locator('.swccg-card-image-choices button[aria-pressed="true"]').textContent(),'Original');
   }
   await page.getByRole('combobox',{name:'Card images',exact:true}).selectOption('remastered');await page.getByRole('button',{name:'Save default',exact:true}).click();await page.getByRole('status').filter({hasText:'Default saved'}).waitFor();await page.goto('https://wiki.swccg.com/wiki/'+pages.boshek);await ready(page);assert.equal(await page.locator('.swccg-card-image-choices button[aria-pressed="true"]').textContent(),'Remastered');await page.getByRole('button',{name:'Original',exact:true}).click();assert.equal(await page.getByRole('combobox',{name:'Card images',exact:true}).inputValue(),'remastered');await page.reload();await ready(page);assert.equal(await page.locator('.swccg-card-image-choices button[aria-pressed="true"]').textContent(),'Remastered');report[mode].guestPreference={persistsAcrossNavigation:true,perCardDoesNotRewriteDefault:true};
   await context.close();
  }
  const translated=await browser.newContext({viewport:{width:1440,height:1000}});await guard(translated);const page=await translated.newPage();await page.goto('https://wiki.swccg.com/wiki/'+pages.boshek+'?uselang=fr');await ready(page);assert.equal(await page.getByRole('button',{name:'Remasterisé',exact:true}).count(),1);assert.ok((await page.locator('.mw-parser-output').textContent()).includes('Adds 3 to power'));report.translatedInterface={locale:'fr',imageLanguage:'en',localizedRemasteredButton:true,englishCardStateUnchanged:true};await page.screenshot({path:path.join(ROOT,'headless-boshek-french-ui.jpg'),fullPage:true});await translated.close();
  assert.equal(report.archiveRequestsBlocked,0);report.result='PASS';
 }catch(error){report.result='FAIL';report.error=error.stack;throw error;}
 finally{await fs.writeFile(path.join(ROOT,'browser-checks.json'),JSON.stringify(report,null,2));await browser.close();}
 console.log(JSON.stringify({result:report.result,desktopCards:Object.keys(report.desktop).filter(x=>x!=='guestPreference'),mobileCards:Object.keys(report.mobile).filter(x=>x!=='guestPreference'),translatedInterface:report.translatedInterface,archiveRequestsMade:0,separateHeadlessProfile:true}));
})().catch(e=>{console.error(e.message);process.exitCode=1;});
