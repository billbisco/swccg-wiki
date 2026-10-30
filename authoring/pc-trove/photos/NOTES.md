# PC website photo mining: notes (2026-10-30)

## What was searched

**swccgpc.com (all hosts: www, cards., ramapocon., shop.), via Wayback CDX**
- Full URL inventory: 15,566 unique URL keys (CDX pages 0-5; later pages were empty).
- Image captures with an image MIME type: 3,613. About 3,500 are card scans, set icons, forum smilies, ranks or templates, plus 16 avatars (<15 KB). **No player or event photo was ever hosted on swccgpc.com itself.** The only image-like hits were partner logos (jasonmaas.jpg, holotablelogopc.jpg), banners and buttons.
- HTML read: 294 non-forum pages (2002-2004 static News/Events/Archives pages, interior.htm, 2005-2008 PHP-Nuke news, `news/news.php` 2008-2010, Encyclopedia, gallery2 stubs) and 160 forum index/viewforum pages (784 topic titles). I scanned every `<img>` in them.
  - The 2002-2004 site (Worlds 2003 Atlanta and Road to Worlds 2005 pages, among others) is text only.
  - Gallery2 (2007, "Worlds Weekend 2007" topic) only shows "Sorry, this Module isn't active!". The `/gallery/` (2010) captures hold card images only.
  - **One hit:** PHP-Nuke news article sid=88 ("2008 East Nationals Champ - Jan Westergard", July 2008) embeds a flickr photo. That led to the full 11-photo flickr set from that weekend (user brad227lex), downloaded at original size from flickr (still live).
  - Another hit was a news article (sid=61) embedding a 90 px photo of Christoph Stieler on a third-party host. It was never archived.
- Forum topics: 786 topic ids are captured (mostly 2004-2006). Topic 16210 "Tournament Pictures" was **never archived**. I did not fetch all 786 topics. From their titles, the captured ones are mostly YJ and general chat.

**starwarsccg.org (the same PC site under its 2009+ domain)**
- The `news.php` permalinks on swccgpc.com point to www.starwarsccg.org, so I followed the site there. Most of the finds come from it.
- Image CDX: 16,753 image URLs. About 384 non-card images over 12 KB are in wp-content uploads, forum attachments and Joomla banners.
- 105 monthly homepage captures (2009-2019) were fetched. I extracted their slider and banner images and the links each banner points to.
- PC "Awards" page (community/awards/, 2016-04-13) gives the captions for the Hall of Fame photos. The post "World Champion Crowned in Philadelphia" (2015) is the source of chu-desai.jpg.
- The live starwarsccg.org is behind a Cloudflare challenge (403), so the full-size originals could not be pulled.

**Wiki checks**
- I computed the SHA-1 of every kept file and ran `allimages&aisha1`. There were **0 exact duplicates**.
- I also compared by name and by eye against existing File: pages (see "Skipped" below).

## Counts
- Kept: **21 files** (`img/`, `manifest.json`).
  - 3 Worlds champion/runner-up event photos.
  - 1 HOF group photo.
  - 5 player photos.
  - 8 event photos.
  - 4 other or unidentified items.
- Skipped as already on the wiki at the same or better quality, even though the bytes differ:
  - keven.jpg is already `File:Kevin Shannon 2011 Worlds champion banner.jpg`.
  - mpc2011.png is already `File:2011 MPC Kevin Shannon Tom Hollingworth banner.png`.
  - sl-hof, em-hof and cm-hof are already `File:Scott Lingrell / Emil Wallin / Chris Menzel 2015 Hall of Fame.jpg`, and the wiki copies are full 1080 px.
- Skipped as promo art with no players: Worlds 2010/2011/2012/2013 and MPC 2012/2013 banners, NA Continentals 2012, Texas Mini-Worlds 2012, Nationals 2012, design blog and set banners.
- Also skipped:
  - A sandwich photo (forum attachment 3350).
  - A deck screenshot (attachment 9970).
  - A meme gif.
  - Card scans.
  - The tiny "2016 World Championships" video thumbnail (249x170).

## Best finds (champions and runners-up first)
1. **2010, Dan Kim (champion, a gap year).** `Dan Kim 2010 Worlds champion banner.png`, the PC homepage banner "Meet your 2010 World Champion! Dan Kim". Two men are in it. The "Dan Kim" label sits over the man on the right; the other man is not named. This would be the first photo of Dan Kim.
2. **2014, Emil Wallin (champion) and Brian Terwilliger (runner-up).** `Emil Wallin and Brian Terwilliger 2014 Worlds champion banner.jpg`, a banner with both finalists holding trophies. The right-hand man matches Emil's HOF photo, so Brian is presumably on the left (please confirm). This is an actual-event photo to replace the HOF stand-in on World Championships.
3. **2015, Justin Desai (champion) and Jonny Chu (runner-up).** `Justin Desai and Jonny Chu 2015 Worlds champion banner.jpg`, the featured image of the PC post naming both. The left-hand man matches "Jonny Chu, second from left" in the 2013 HOF class photo, so Justin is presumably on the right (please confirm). The left ~450 px is a grey gradient, so crop it.
4. 2013 HOF inaugural class: Kevin Shannon, Jonny Chu, Justin Desai and Angelo Consoli, in that order from the PC captions. It is only 300x225. The wiki already has the per-person crops but not the group shot.
5. Steve Baroni, 2012 MPC champion (banner).
6. Scott Lingrell with his Lifetime Achievement Award (2011 award; only a 197x300 thumbnail is archived).
7. **2008 US East Nationals**, 8 flickr originals (3264x2448). They show Jan Westergard (champion) with the trophy glass and banner, and the final Westergard vs Justin Desai (runner-up). Also a top-4 "Desai v Hollingworth" shot, which Hollingworth is not stated, plus a sealed side event, a hall/banner view and a Worlds 2008 Day 2 bye card. The flickr licence is **All Rights Reserved**; whether to upload them is Bill's call. There is no wiki page for 2008 US East Nationals yet; the wiki has only 2007 US East Nationals.

## Unidentified, worth Bill's eyes
- Forum attachment 2588: a restaurant dinner photo with several players. Hi-res, no caption.
- Forum attachment 3321: Leia/Han cosplay pair at a table.
- Forum attachment 2586: a replica lightsaber prize in a case with an SWCCG plaque.
- 2020 Endor Grand Prix: three photos with file-name hints only ("hayes-bfred", "jellisons"). The embedding post was not found, so I left them unnamed.
- MPC promo banner: a play-hall crowd photo, event/year not stated.

## Gaps (Worlds champion years still without an event photo after this pass)
- 2004 Brandon Schele, 2005 Drew Scott, 2006 Nate Meeker: nothing.
  - The PC site of that era (static HTML, then PHP-Nuke) carried no photos.
  - The 2005-2006 forum topics that might have had photos were mostly not captured.
- 2003 and 2007 Jonny Chu, 2008 Kevin Shannon, 2009 Brian Hunter, 2012 Emil Wallin, 2016 Tom Haid, 2018 Bastian Winkelhaus: no new event photo found.
- 2013 Justin Desai: the 2013 Worlds champion banner `wp/wp-content/uploads/Worldchamp.jpg` (Aug-Dec 2013 homepage, linked to forum t=52082) **was never archived**; it only exists as a 2023 redirect. `images/banners/Worldchamp.jpg` is also uncaptured.
- 2016 Worlds: the "Worlds-Banner-2017" and event-video images were not archived.
- Runners-up without photos: everyone except Brian Terwilliger (2014) and Jonny Chu (2015) found here.

## Pages and galleries not archived (dead ends)
- starwarsccg.org Phoca Gallery albums (world-championships-2011, mpc2007, mpc2010, mpc2011, fallensith-2011, ramapocon-99): only 2-3 KB thumbnails are captured; the large images and album pages are not.
- Joomla article "world-2010-winner" (id=259) is not archived.
- The 2010 front-page slideshow photo `components/com_fpslideshow/images/img_0114_1.jpg` (2010 MPC results slide) is not archived.
- swccgpc.com forum topic 16210 "Tournament Pictures" and the 2008 forum (Worlds/Nationals threads) are mostly not archived.
- Full-size originals of the HOF and banner images (`HOF-Inagural-Class.jpg`, `sl-hof.jpg`, `sl-la.png`, `chu-desai` at larger size) are not captured, and the live site blocks fetching.

## Possible next steps
- Fetch all 786 captured swccgpc.com forum topics (about 70 time-boxed calls) and the starwarsccg.org phpBB topics (f=889, the 2015 Worlds forum, and others) for embedded external photos.
- Ask the community (or Scott Lingrell / the PC) for the originals of Worldchamp.jpg (2013) and the Phoca Worlds 2011 gallery.

PC work dir: `~/.grok/claude-agent/pctrove/photos/`. It holds the CDX dumps, fetched HTML (html/, fhtml/, hp/, ctx/), raw/ and raw2/ images, flickr/ and the stage tars. Nothing was deleted there (deletion is not permitted).
