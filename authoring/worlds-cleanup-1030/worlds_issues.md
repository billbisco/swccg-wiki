# Worlds fact check: issues, gaps, photo candidates

Checked 30 October 2026. Read-only: nothing was edited on the wiki.

Main sources:
- PC Awards and Hall of Fame page, fetched live through FlareSolverr: https://www.starwarsccg.org/community/awards/
- PC Major Event Winners page: https://www.starwarsccg.org/major-event-winners/
- PC decklist and wrap-up posts (URLs per year in worlds_facts.json)
- Forum thread t=75427, page 1 and page 2: https://forum.starwarsccg.org/viewtopic.php?t=75427
- Old swccgpc.com pages on Wayback
- Wikipedia's SWCCG article table
- The wiki API (list=allimages filtered to JPEG/GIF/PNG; the wiki has no CirrusSearch, so `srnamespace=6` search does not support `filemime:`)

## A. Championships index page (Championships.wiki)

1. **2013 champion is blank.** It should be **Justin Desai**, who defeated **Reid Smith** in Boston, MA.
   - Sources: Awards page; Major Event Winners ("2013: J Desai"); the 2022 wrap ("third World Championship title (2013, 2015)"); Wikipedia.
2. **2026 is missing.** It should be **Brian Fred** defeating Justin Desai, in Bloomington, MN, 23–25 October 2026, Open.
   - Sources: PC decklist post https://www.starwarsccg.org/2026-11-swccg-world-championship-bloomington-minnesota-oct-23-25-2026/ and forum t=87037.
3. **2018 and 2019 both say Bastian Winkelhaus. This is correct.**
   - 2018: def. Tom Kelly in Morristown. 2019: def. Bryan Mischke in Bochum.
   - He is the first back-to-back champion and the first three-time champion ('01, '18, '19).
   - Sources: Awards page and Hall of Fame blurb; 2018 and 2019 PC decklist posts; 2021 wrap.
4. **2016 Tom Haid is correct.** He defeated Reid Smith in Princeton.
   - Sources: Awards page; Major Event Winners; 2016 PC decklist post; Wikipedia; 2021 wrap ("Tom Haid (2016 World Champion)").
5. **Format column is blank for 2003–2006.**
   - The hubs say VS5 (2003) and VS6 (2004–2006). None of these cutoffs is confirmed; 2006 is marked "probably".
6. **Inconsistent sourcing.** The Virtual Modern section cites [[List of SWCCG tournaments]] as its source instead of the Awards page. The Awards page lists 1996–2024 and covers 2015–2024.
7. **Missing columns.** The index has no runner-up, site or field size columns. All of them are now in worlds_facts.json.

## B. Hub and List-page errors or blanks

- **2002, city conflict.** The Awards page and Wikipedia say "DecipherCon – Virginia Beach, VA". The hub says Chesapeake Conference Center (Decipher photos are titled "DecipherCon 2002 Chesapeake Conference Center"). Recommendation: keep Chesapeake and add a note that the PC list says Virginia Beach.
- **2003, top 8 has an official source.** The hub says "No official top 8 has been found". In fact the PC news of 5 September 2003 lists the full top 8 with deck pairs. Source: https://web.archive.org/web/20031008101333/http://www.swccgpc.com/interior.htm
  - The same news item says Chu won with **Combat / Senate**. The hub lists only his Day 2 TDIGWATT / Local Uprising (V) lists.
  - The same news says the event was at Dragon*Con, Atlanta.
- **2004, dates.** The hub has "Dates: 2004". They are **19–22 August 2004** at Gen Con Indianapolis. Source: https://web.archive.org/web/20040710155145/http://www.swccgpc.com/interior.htm
  - Places 3–8 are still unknown (forum t=75427 also says they are missing).
- **2005, dates not found.** Gen Con Indy 2005 ran 18–21 August 2005, but no SWCCG source confirmed the Worlds days.
- **2006, venue.** The PC news of 16 June 2006 says "PasTimes in Chicago is working with us in order to provide a new date. August date conflicted…" Source: https://web.archive.org/web/20060617215932/http://www.swccgpc.com/
  - The final date was not found.
  - Wikipedia gives a field of 34.
  - Meeker's winning decks are not on the wiki.
- **2007–2012, venues not found.** Only the cities are known.
- **2013 hub.** Site and Winner are blank.
  - The Day 3 table has only 7 players. The 8th is unidentified; Matthew Harrison-Trainor's sheets are bound into the Day 3 PDF, but those are his Day 2 sheets.
  - The city is Boston, MA (Awards page, Wikipedia). The hotel was not found.
  - Field: 60 (Wikipedia).
  - The inaugural Hall of Fame class (Chu, Consoli, Desai, Shannon) was enshrined 10 August 2013, during this Worlds. The hub does not mention it.
- **2014.** Field 31 (Wikipedia). The hub has no field size.
- **2015 hub.** It omits runner-up Jonny Chu.
  - It omits the HoF class of 8 August 2015 (Lingrell, Menzel, Wallin).
  - Field: 61.
  - Top-8 order conflict for 3rd and 4th: the PC list order is Sokol 3rd, Olson 4th. Sokol's HoF blurb says "4th place finish in 2015". The 2020 Olson article says "2015-3rd". So the order is Olson 3rd, Sokol 4th, and the PC list is unreliable for those two places.
- **2016 hub.** It omits runner-up Reid Smith. Field: 62 (PC list count; matches Wikipedia).
- **2017.** The Awards page and PC pre-event post say Minneapolis; the hub and Wikipedia say Bloomington. Both are true; Bloomington is a Minneapolis suburb.
  - The hub omits Mark Walseth's HoF enshrinement (12 August 2017).
  - Field: 59.
- **2018 hub.** It omits runner-up Tom Kelly.
- **2019 hub.** The Format block has no Winner line.
  - The hub omits Bastian Winkelhaus's HoF enshrinement on 20 September 2019 (Day 1).
  - Field: 69.
- **2020.** The wrap says 97 Day 1 players; the PC decklist post lists 98 Day 1 entries. Use 97, as the wrap states it.
- **2021, dates.** The hub and List say 7–10 October; the wrap says "the weekend of October 8th–10th".
  - Venue: Hyatt Regency Crystal City (missing from hub).
  - Hall of Fame: Joe Olson (enshrined 9 October 2021).
  - Team event: Tartaglione & Reinhold.
- **2022, dates.** The hub and List say 13–16 October; the wrap says October 14–16.
  - Venue per wrap: "Hyatt Regency Peachtree", Atlanta.
  - Runner-up Matthew Harrison-Trainor is missing from the hub lead.
  - Team event: Desai & Baroni.
- **2023, dates.** The wrap says August 10–13; the PC decklist page and hub say 11–13.
  - Venue: Hyatt Regency Morristown.
  - The PC decklist page spells "Brian Mischke" for Bryan Mischke.
- **2024.** Venue: Zu den Vier Winden, Bochum. Hall of Fame: Kevin Jaap and Hayes Hunter (21 September 2024). Field: 53.
- **2025.** The PC decklist post title says "Seattle, Washington (October 4-5)". The wrap says Hampton Inn & Suites, SeaTac, 3–5 October. Both fit (constructed play was 4–5 October).
- **2026, dates.** The List page has "24–25 October 2026" (constructed days); the hub has 23–25.
  - Venue (missing from hub): Hyatt Regency Bloomington by Mall of America, from forum t=86751.
  - Team event: "Unholy Alliance", Phil Aasen & Brian Fred, from forum t=87034.
  - Field: 58 Day 1 lists; 59 were registered (forum t=86988).
  - No wrap-up article yet.
- **Field-size disagreements:**
  - 1996: 38 per InQuest #22 (hub) vs 32 per Wikipedia.
  - 2000: Wikipedia's 72 vs about 170 on Day 1 and 70 on Day 2 (hub).

## C. Stale PC sources (not wiki errors, but cite with care)

- The **Awards page World Champions list stops at 2024.** It is missing 2025 Greg Shaw def. Joe Olson and 2026 Brian Fred def. Justin Desai.
- The Hall of Fame list is missing **Brian Fred (2025)**, even though the 2025 wrap links to the Awards page.
- **Major Event Winners** still shows "2024: TBD" and ends there.
- Forum t=75427's main tables are screenshot attachments (file ids 19576–19580, August 2023). They are behind Cloudflare and have no Wayback copy, so they could not be read. Only the text replies (1996–2011 brackets) were used.

## D. Photos

**Already on the wiki** (the exact File: titles are in worlds_facts.json `photos_on_wiki`). Every year 1996–2002 has event photos. After that:
- 2011 has only the Kevin Shannon homepage banner.
- 2013, 2015, 2017 and 2019 have only HoF portraits, plus Phil Aasen's community card for 2017.
- 2020 has Joe Olson's POY trophy photo.
- 2021–2025 have full wrap-up photo sets.

**No photo of any kind** for 2003, 2004, 2005, 2006, 2008, 2009, 2010, 2012, 2014, 2016, 2018 or 2026.

**Many hubs do not use photos that exist.** Hubs 2013, 2015, 2017, 2019 and 2020 have no image. Hub 2011 does not use File:Kevin Shannon 2011 Worlds champion banner.jpg. Hub 2001 already uses its photos.

**Photos on the PC site but not on the wiki:**
- 2013 inaugural HoF class group photo (Chu, Consoli, Desai, Shannon), from the Awards page: https://res.starwarsccg.org/wp/wp-content/uploads/HOF-Inagural-Class-300x225.jpg. There is no "Jonny Chu 2013 Hall of Fame" file.
- Joe Olson HoF photo (2021): http://res.starwarsccg.org/wp/wp-content/uploads/2022/JoeOlsonHoF.jpg
- Hayes Hunter HoF photo (2024): https://s3.us-east-2.amazonaws.com/res.starwarsccg.org/wp/wp-content/uploads/2024/hayeshof2.jpg
- Bastian Winkelhaus HoF / three-titles photo: http://res.starwarsccg.org/wp/wp-content/uploads/2022/bastian3WC.jpg. Check whether this is the source of File:Bastian Winkelhaus 2019 Hall of Fame.jpg.
- Matt Sokol and Chris Gogolen HoF (April 2019; not a Worlds event): https://res.starwarsccg.org/wp/wp-content/uploads/11025-225x300.jpeg
- Scott Lingrell HoF (2015 Worlds): https://res.starwarsccg.org/wp/wp-content/uploads/sl-hof-300x300.jpg. The wiki has a "Scott Lingrell 2015 Hall of Fame.jpg"; check whether it came from this image.

Every 2021–2025 wrap-up image is already on the wiki, matched by name and source.

**2026:** no PC wrap-up yet, so no photos. Re-check later at https://www.starwarsccg.org/ and in the forum thread "Congrats BFred" (t=87044).

**Still to try:** Wayback copies of the 2012–2016 starwarsccg.org homepage banners, which may hold champion photos like the 2011 keven.jpg banner. The 2012–2014 Joomla homepages fetched here (sw_2013*) were near-empty shells, so this was not followed up.

## E. Not found (open questions)

- Exact dates for 2005 and 2006.
- Venues (hotels) for 2003–2020, except 2009 (Clarion Hotel, Princeton) and 2020 (online).
- 2004 places 3–8.
- 2012 top 8.
- The eighth 2013 Day 3 player.
- Team-event winners for 2002–2020.
- Meeker's 2006 winning decks.
