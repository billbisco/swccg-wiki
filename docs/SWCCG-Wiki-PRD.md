# SWCCG Wiki Product Document (living)

**Canonical for humans and implementers.** Update this file when the owner answers a question or changes scope. Do not treat chat as the source of truth.

| Field | Value |
| --- | --- |
| Product | wiki.swccg.com |
| Owner | User (one-person shop) + Grok as Principal Product Manager |
| Status | Bot-ready for Phase 1 wiki rails (WP-W0, WP-W1) and card template (WP-W2). Interview closed 2026-09-19. |
| Last updated | 2026-09-19 |
| Phase alignment | Phase 0–1 of `phased-roadmap.md` |
| Audience for this file | Owner, Grok Build, Grok Bots, later editors |

Related skill files: `vision.md`, `landscape.md`, `data-model.md`, `legal-and-community.md`, `infra.md`, `phased-roadmap.md`.

---

## 1. One-sentence job

wiki.swccg.com is the premiere, sourced, versioned encyclopedia of Star Wars CCG — Decipher history first, later Players Committee / virtual / GEMP layers labeled — tightly coupled to the swccg.com play engine so cards, images, decklists, and accounts are not duplicated.

## 2. Why it exists (problem)

Today the game’s knowledge is scattered and flattened:

| Place | What it is good at | What it fails at |
| --- | --- | --- |
| Wikipedia | High-level history | Card-level depth, strategy, decklists, rulings |
| Wookieepedia | Star Wars fiction | Game mechanics, versions, play |
| starwarsccg.org / Scomp | Current organized play + current-text search | Historical text layers, readable rules, championship narrative |
| swccgdb.com | Decklists / some commentary | Versioned rulings, shared identity with play |
| Stephenskilton decktech archives | Historical decktech | Durability, integration, hover/import |
| GEMP @ gemp.starwarsccg.org | Playing the current game | Wiki, history, SSO, extra formats |
| PDF rulebooks + forum threads | Authoritative when you already know where to look | Search, citation, onboarding |

The wiki wins if a player can learn the game, look up any card in any era, understand why a ruling exists, import a championship deck, and click through to play — without leaving the swccg.com identity.

## 3. Non-goals (v1 unless owner overrides)

- Replacing PC Worlds or claiming to be the official committee.
- Hotlinking Holotable / res.starwarsccg.org as if those binaries were ours.
- Collapsing all card text into one “current Oracle” string.
- Unattended AI publish of historical gametext.
- Shipping a second always-on full GEMP stack on the same 8 GB box just to demo hover-links.

Public copy stays: premier information and play site. Not “the replacement committee.” Internal success metric can still be “people learn and play here.” See `legal-and-community.md`.

## 4. Product principles (wiki-specific)

1. **Three Decipher-era truths, then later variants.** Every printed Decipher card stores at least: (a) as-printed, pre-Decipher-errata; (b) Decipher errata where one exists; (c) later PC errata as a labeled variant. PC rules and PC errata are not “the card.” They are a popular, well-documented later ruleset. The wiki exists so those layers do not collapse.
2. **One corpus, many views.** Wiki pages render the shared card corpus and image store. GEMP, search, and decklists consume the same IDs.
3. **Cite or archive.** Every imported fact has a source URL. If the source is fragile (including starwarsccg.org behind Cloudflare), snapshot it to archive.org and/or archive.today as part of ingest.
4. **Label what is not Decipher.** Virtual cards, PC reversals, AI-drafted strategy, inferred text.
5. **Suggest freely, publish when trusted.** Any logged-in player can propose. Only trusted editors (and the owner) change live gold pages. That is the spam control.
6. **Play is one click away.** Deck pages offer human decklist view + GEMP-importable text. Card pages deep-link into play with a format query.
7. **People pages are sourced or first-party.** Historical pages need a citation. Our own finished play.swccg.com events publish the GEMP username + deck automatically.

## 5. Users and jobs-to-be-done

| Persona | Job | Success looks like |
| --- | --- | --- |
| New player | Understand what the game is and how a card works | Card page + linked rule anchors; no PDF hunt |
| Returning Decipher player | Find original text and 1996–2001 Worlds | Set history + championship pages with decklists |
| Current PC player | Look up current text, virtual cards, recent decks | Labeled PC layer + importable lists |
| Deck builder | Study and load a list | Hover tooltips + GEMP import |
| Editor / old-head | Add strategy, correct a ruling, source a story | Low-friction edit, visible attribution |
| Owner | Keep the lights on alone | Spam contained; bots draft; owner publishes gold |

## 6. Information architecture

URL host: `wiki.swccg.com` (locked in `infra.md`).

Suggested top nav:

- Play (→ play.swccg.com or current play.swccggemp.com until cutover)
- Cards
- Sets
- Rules
- Formats
- Championships & events
- Decks
- People
- History
- GEMP
- Contribute

### 6.1 Page types

| Type | Example title | Must contain |
| --- | --- | --- |
| Card | `Luke Skywalker (Premiere)` plus a canonical `card_uid` landing that lists siblings | All text versions oldest→newest with diffs; printings; images from our store; rulings+citations; trip-ups; pulls; strategy (community); format legality; “play this” links |
| Set | `Premiere` | Release date, designers, size, themes, design notes, card checklist, sealed/limited notes |
| Rulebook / CRD | `Decipher CRD 2001-xx` / `PC Advanced Rulebook rN` | Transcribed sections with anchors; PDF cited; archive snapshot |
| Ruling | Per-card and per-concept | Question, answer, date, source, which text layer it applies to |
| Format | `decipher-ds2-2001`, `pc-standard-YYYY-MM` | Ruleset snapshot, card-version map, banned list, deck size |
| Championship | `World Championship 1996` | Location, field, top cut, narrative, decklist links, sources |
| Decklist | `1996 Worlds — Raphael Asselin Light` | Player, event, side, date, format, sourced list, hover cards, GEMP import block, commentary |
| Person | Designers; champions; notable contributors | Role, years, sourced achievements; privacy rules TBD |
| Org | `Players Committee` | Neutral history, what they run, how this site differs, links out |
| Platform | `GEMP` | Origin, Ketura/LOTR lineage, this instance vs PC instance |
| Concept | Destiny, Force drain, Sense/Alter | Rules anchors + famous cards |

Card title collision policy: display title is not the primary key. Personas, both-sides titles, and virtual retitles (e.g. Jabba's Prize (V) → The Mythrol) use `card_uid` + redirects.

### 6.0 Set navigation (locked)

The Sets index is three bands, in this order, with labels a new visitor cannot miss:

1. **Decipher sets** — one list in [CardGuide Star Wars CCG](https://cardguide.fandom.com/wiki/Star_Wars_CCG) product order. Do **not** split “official numbered expansions” vs “premium products.” Owner exception 2026-09-20: there is no Death Star II Sealed Deck; list **Death Star II Starter Decks** (exclusive Admiral Ackbar / Admiral Piett) with Death Star II. Unmarked as to publisher beyond “Decipher.”
2. **Current Virtual Sets** — Players Committee virtual sets from the 2014 Reset onward (Set 0, Set 1, …). Every set hub and card page carries a **Players Committee / Virtual** badge. These are not Decipher cards.
3. **Virtual Legacy** — PC virtual cards from 2002 through the 2014 Reset (early numbered virtual sets and later virtual blocks). Badge plus a short note that Legacy is not the current Standard pool.

A Decipher printing and its later `(V)` sibling are **two pages** (or one page with two set memberships — implementer pick, but the visitor must see two set homes). Cross-link both ways. Lead image and lead gametext on a Decipher card page stay Decipher. Virtual text does not replace the lead.

### 6.2 Card page contract (implementer checklist)

From `data-model.md`, plus wiki UX:

- Lead is **Decipher**: name, uniqueness dots, side, type, set, collector number, rarity, hosted **original scan** (not a PC slip unless the card is virtual-only)
- Version sections, oldest to newest, never overwritten:
  1. **As printed** — pre-Decipher-errata. Source: scan + OCR/review, or contemporaneous checklist. `layer: printed`
  2. **Decipher errata** — only if Decipher published one. Date, CRD/PDF cite, diff vs printed. `layer: decipher_errata`
  3. **PC errata** — labeled *Players Committee errata (not Decipher)*. Date, PC source + archive, diff vs the Decipher layer it changed. `layer: pc_errata`
  4. **Virtual sibling** — if a (V) or retitled virtual exists, link out to that virtual-set page. Do not replace the Decipher lead.
- Each version: title, gametext, lore, stats, icons, effective dates, source, archive link
- Rulings list must say **which layer** they apply to
- “How this card trips people up”
- Strategy (pending-revision; not gold corpus)
- Pulls / pulled-by
- Appearances in featured decklists
- Play links with `format` so the engine loads the matching sibling
- Language: English gold first. Template must not assume a single string field named `text`. See §6.4

### 6.4 Future languages (constraint now, work later)

Not in the wiki live bar. It still dictates schema and templates today.

- Official historical printings to ingest as artifacts: English (complete), Japanese Takara (Premiere / ANH / Hoth and checklist appearances), Spanish Premiere.
- New languages (Italian, German, modern Spanish, others) are **unofficial translations** of gold English, labeled as such.
- Pipeline later (Phase 6): original scan stays the art; title, lore, and gametext are laid onto blank frames (or HTML overlay) per `version_id` + `lang`. Never bake translated words into the scan file.
- Wiki UI can later switch `lang`. Card IDs do not change.
- Do not invent printed-era foreign text. If we lack a scan of a JP/ES card, mark `needs_scan`.

Public voice on PC layers: accurate and cool, not sneering. Internal model: PC errata = popular house rules / organized-play mods of Decipher’s game. On-wiki label: “Players Committee errata — not published by Decipher.”

### 6.3 Decklist page contract

- Metadata: event, date, player, placing, side, format, source + archive
- Default view: grouped decklist (locations, characters, starships, effects, interrupts, etc.)
- Hover / tap: card preview from corpus (title, image, active version for that format)
- Alternate view: raw GEMP-importable text (copy button)
- Optional commentary / decktech
- Deep link back to event page and player page

## 7. Integration with GEMP and the rest of swccg.com

| Surface | Behavior |
| --- | --- |
| GEMP right-click / hover | Open wiki card page for that `card_uid` (format-aware sibling when possible) |
| Wiki card / deck | “Play” and “Import to GEMP” |
| Tournaments | When we ingest an event, create/update event + player + deck pages |
| Images | Single object store; wiki File: pages may proxy or describe, they do not keep a second binary tree |
| Auth | Same identity as GEMP on swccg.com (local username/password + Google / Apple / Discord). Local accounts required for regions that block those IdPs |
| Search | Wiki full-text plus a Scomp-class card search over the corpus (filters: side, type, set, destiny, icons, layer) |

Do not scrape live PC GEMP private endpoints. Public pages and published decklists only, with archive snapshots.

## 8. Content program (what “premiere” means in practice)

Priority order for filling pages (proposed, not locked):

1. Schema + card template + Premiere as the proof set (matches Phase 1).
2. Set hub pages for every Decipher set (even if cards are stubs).
3. Rulebook / CRD transcription with anchors.
4. Worlds 1996–2001 as flagship history (narrative + lists + sources).
5. Remaining Decipher cards set-by-set.
6. Designers and design-decision pages where sources exist.
7. PC org page + GEMP page + virtual card namespace.
8. Modern events and decklists (ingest policy TBD).
9. Strategy density on high-traffic cards.
10. Replacement depth for Scomp / swccgdb / decktech archives.

Sourcing rule: if we cannot cite it, it is marked `needs_source` or it does not go in the gold sections.

## 9. Contribution and security (locked direction)

**Publish model (locked):** suggestions only until trusted.

| Role | Can do |
| --- | --- |
| Anonymous | Read. No edits. |
| Logged-in (same swccg.com identity) | Edit a draft tab / pending revision. Cannot make that revision public. |
| Trusted editor | Review pending revisions. Accept, reject, or amend. Publish live. |
| Owner / bureaucrat | Appoint trusted, protect pages, block, run ingest jobs. |

Gold pages = card corpus fields, rulings, rulebooks, set facts, championship facts, first-party tournament results after they are written by the event job.

Community commentary (strategy, trip-ups, decktech prose) lives in the same pending-revision flow. It is not a backdoor onto the live article.

**Trusted-editor rule (locked):** owner appoints. Also earned after **10 accepted pending revisions** and no spam-class rejects. Revocable. Play-count gating waits until play.swccg.com events exist.

**Draft UX (locked):** FlaggedRevs or Approved Revs — player edits a draft tab. AI may write into the pending queue only, never onto the public revision.

**Cheap defense stack (locked as the default build list):**

- MediaWiki
- No anonymous edits
- SSO + local password accounts; email confirm for local
- ConfirmEdit on register and on first external link in a suggestion
- AbuseFilter throttles and “new page that is mostly URLs” blocks
- StopForumSpam + title blacklist
- Rate limits
- Suggestion queue so a bot flood does not rewrite cards even if an account exists
- FlaggedRevs or Approved Revs as the draft-tab mechanism (locked)

Do not enable CheckUser unless the owner later asks. Privacy cost is real on a one-person shop.

## 10. Technical notes for implementers

- Platform **locked:** MediaWiki (LOTR wiki is the UX pattern; templates, categories, VisualEditor). Gold card fields render from the shared corpus; strategy and commentary stay suggestion-gated wikitext.
- Host: same Hetzner CX33 as landing + current GEMP experiment. Budget RAM. PHP-FPM + MariaDB; images off to object storage as soon as volume hurts the 80 GB disk.
- Card body should be template-driven from corpus JSON/SQL, not 2,000 hand-wikitext gametext copies. Strategy and commentary stay wikitext.
- Ingest jobs write corpus first; wiki render second.
- Archive step is part of ingest, not a nice-to-have.
- Right-click integration is a GEMP client change in Phase 3; wiki must stabilize card URLs in Phase 1.
- **Card URL (locked):** canonical `/wiki/Card/{card_uid}` (or `/wiki/Card/PRE-041` if `card_uid` is that code). Human titles (`Luke_Skywalker_(Premiere)`) are redirects. GEMP and ingest store the ID.
- **Skin (locked):** shared chrome with swccg.com landing (same header, footer, fonts, “fan project / not official” line). MediaWiki content well inside that chrome. Do not invent a separate starfield brand.
- **Deck import (locked):** each decklist page is one side. One copy box in the paste format GEMP’s importer already accepts. Championship pairs are two pages plus an event hub that links both.
- **Worlds sources (locked):** public pages first, snapshot to archive.org and/or archive.today, then write. Owner files overlay later if they appear. No private stash is a live-bar dependency.

## 10a. Launch checklist (wiki publicly “live”)

Construction banner comes down only when all of the following are true:

- [ ] Engine is MediaWiki at wiki.swccg.com, SSO wired enough that a local account can file a suggestion
- [ ] Premiere: every card has hosted scan, reviewed printed layer, current PC layer, template, rulings stub
- [ ] Every later official Decipher card has at least a stub (title, set, collector number, side, type, image if we have it, empty sections)
- [ ] Rulebooks exist as wiki pages with section anchors — live bar is the **core three**: last widely used Decipher Rulebook (v2.0, Nov 1998, confirm at ingest), last Decipher Current Rulings Document, current PC Advanced Rulebook. Other CRDs/ARBs are hub entries + archived PDFs until transcribed.
- [ ] Worlds 1996–2001 hub pages exist with sourced narrative and decklist pages where lists are known
- [ ] Decklist template: grouped human view + hover preview + GEMP-importable block
- [ ] Pages exist for: Players Committee (neutral), GEMP origin + this instance
- [ ] Virtual navigation: Decipher sets first; **Current Virtual Sets** (post-2014 Reset) below; **Virtual Legacy** (2002–2014) below that. PC badge on every virtual page.
- [ ] Every Current Virtual card has at least a stub (name, set, number, PC badge, image if hosted). Virtual Legacy = set hubs + checklists, not a required stub-per-card at launch.
- [ ] Ingest path for external sources: snapshot archive.org and/or archive.today, then curated import
- [ ] Player-page policy implemented as in §10b

Not launch blockers (do after live if needed):

- Scomp-class dedicated card search (MediaWiki search + category/set indexes can ship first)
- GEMP right-click / hover into the wiki (Phase 3 play client). Card URLs must still be stable now so that hook is cheap later.

## 10b. Player pages (locked)

Two pipes, one page type (`Player:<gemp_username>` or `Person:<display>` with redirects).

1. **Historical / external events** — page only if sourced (championships, published lists, designer credits). Cite and archive. Do not scrape a living person’s unused GEMP handle into a biography.
2. **First-party events on play.swccg.com** — when a tournament completes and lists are shared, publish:
   - GEMP username
   - event + placing if we store it
   - deck used (decklist page + player page link)
   - If that username already has a page, append the new event. The page is a running tournament log, not a social profile.

No auto-bio, no harvested email, no “also known as” unless sourced or entered by the player.

---

## 11. Success metrics

- Time-to-answer: “what did this card say in 1998 vs now?”
- Championship pages with sourced decklists for 1996–2001
- Premiere cards: printed + current PC layer + scan + rulings stub
- Inbound clicks from our GEMP to wiki, and wiki “import” clicks back
- Editor accounts that are real players, not spam
- Citations other sites start using
- Traffic and games on swccg.com — not “PC Worlds attendance went down”

## 12. Decision log (locked this interview)

| ID | Decision | Rationale |
| --- | --- | --- |
| D1 | MediaWiki at wiki.swccg.com | LOTR pattern, templates, cheap anti-spam, contribution history. Owner chose “recommend and lock.” |
| D2 | Suggestions only until trusted | One-person shop cannot police live edits. Open memory still exists via the queue. |
| D3 | Launch bar = Premiere complete + all later Decipher stubs + rulebook pages + Worlds 1996–2001 + decklist/import + PC/virtual/GEMP origin pages | Premiere is the quality bar; stubs prevent a one-set museum; history and modern layer both present. |
| D4 | GEMP hover and Scomp-class search are post-live | URLs must be stable now; the client hook waits for Phase 3. |
| D5 | External modern events: archive, then curated import | Cloudflare-fragile sources; no blind nightly scrape. |
| D6 | Player pages: sourced historical notables + automatic first-party tournament log keyed by GEMP username | Completeness for *our* events without doxxing every handle on the internet. |
| D7 | Trusted = owner appoint + 10 accepted pending revisions | Owner stays bureaucrat; queue creates a measurable path. No play-gate yet. |
| D8 | Draft-tab editing (FlaggedRevs / Approved Revs) | Feels like a wiki; publish stays gated. |
| D9 | Live rulebooks = core three | Decipher Rulebook v2.0 (Nov 1998, confirm at ingest), last Decipher CRD, current PC Advanced Rulebook. |
| D10 | Virtual cards are their own sets, listed under Decipher sets | Current Virtual vs Virtual Legacy. PC authorship is visually obvious. (V) overlays still cross-link to the Decipher printing. |
| D11 | AI drafts only enter the pending queue | Public strategy/trip-ups are human-accepted. |
| D12 | Current Virtual: stub per card. Virtual Legacy: hubs + checklists | Standard-era lookup is complete; Legacy is labeled history until we grind it. |
| D13 | Canonical card URL is the stable ID; human titles redirect | GEMP and bots must not depend on pretty titles. |
| D14 | One GEMP-paste copy box per deck page; one side per page | Matches how GEMP imports. Event hubs link the pair. |
| D15 | Wiki chrome matches swccg.com landing | One product, not a bolted-on encyclopedia skin. |
| D16 | Worlds 1996–2001 from public sources + archives | No owner-file gate. |
| D17 | Rails first | wiki.swccg.com exists (banner on) while Premiere corpus is built. |
| D18 | Main Page is a directory / start-here | Magazine stays on swccg.com. |
| D19 | Designers hub + sourced individual pages in the live bar | Credits only. |
| D20 | Store as-printed, Decipher-errata, and PC-errata as separate version rows | PC text is a labeled variant, not the Oracle. |
| D21 | Templates and corpus are i18n-ready; translations are a later phase | Art = original scan. Words = per-language overlay. Official JP/ES are artifacts, not the only future languages. |

## 13. Open questions (still)

- Exact Decipher CRD edition to treat as “last” (ingest lists candidates; owner confirms)
- Hover preview tech on deck pages (MediaWiki gadget vs small JS service reading the corpus)
- Public-page wording sharpness for PC errata: default badge is “Players Committee errata — not published by Decipher.” Do not use “houserules” on public pages unless the owner later asks.

## 14. Work packages (for Grok Build / bots)

Do not start Phase 3 GEMP hover. Do not treat swccg-card-json as Decipher printed text. Archive every external URL you ingest.

| WP | Deliverable | Exit test | Depends on |
| --- | --- | --- | --- |
| WP-W0 | nginx + TLS for wiki.swccg.com, MediaWiki on the existing Hetzner box, shared header/footer with swccg.com, construction banner, SSO stub or local account login | `https://wiki.swccg.com` loads inside site chrome; anonymous cannot edit | `infra.md` |
| WP-W1 | Namespaces, templates, FlaggedRevs/Approved Revs, ConfirmEdit, AbuseFilter starter rules, trusted group | Logged-in user can save a pending revision; it is not public until trusted accepts | WP-W0 |
| WP-W2 | Card template + `/wiki/Card/{card_uid}` + title redirects + PC/Virtual badge + three Decipher-card layers (printed / Decipher errata / PC errata) | Premiere sample that actually *had* Decipher errata and later PC errata shows three strings and two diffs. Template fields are keyed by `version_id` + `lang` even if only `en` ships | corpus schema |
| WP-W3 | Premiere ingest: hosted scans, OCR → review queue, JSON PC layer aligned | Every Premiere card meets the live-bar card contract | WP-W2 |
| WP-W4 | Stubs for all remaining Decipher cards | Set hubs list every card; missing image/text marked | WP-W2 |
| WP-W5 | Sets index with three bands (Decipher / Current Virtual / Virtual Legacy) | New visitor can tell PC virtual from Decipher in one glance | WP-W2 |
| WP-W6 | Stub every Current Virtual card; Legacy set hubs + checklists | Current Virtual titles resolve; Legacy is not empty | WP-W5 |
| WP-W7 | Core three rulebooks as pages with section anchors + archived PDF citations | Deep link to a section works | WP-W0 |
| WP-W8 | Worlds 1996–2001 hubs + decklist template (grouped list, hover if cheap, GEMP paste box) from public sources after archive snapshot | 1996 page cites archived sources and at least the champion pair where lists exist | WP-W2 |
| WP-W9 | PC org page, GEMP origin page (Ketura / LOTR lineage / this instance vs gemp.starwarsccg.org) | Neutral tone; no official-sounding claims | WP-W0 |
| WP-W10 | First-party tournament hook (spec only until play events exist): finished event → deck pages + `Player:<gemp_username>` append | Written as an API/job contract, not necessarily running | identity + GEMP |

Default next build slice (locked): **WP-W0 + WP-W1** while Premiere corpus work proceeds, then WP-W2.

Also in the live bar (add to WP-W9 or a small WP-W11): Designers hub + sourced individual pages; Main Page as directory / start-here (Sets, Rules, Worlds, How to play, Decipher vs PC vs this site).

---

## Interview log

### 2026-09-19 — interview closed

Owner: “that was it regarding my feedback on the PRD.” Status → bot-ready for WP-W0/W1/W2. Reopen only on an explicit change.

### 2026-09-19 — owner note on layers + i18n

- Must store pre-Decipher-errata, Decipher-errata, and PC-errata separately. Historically accurate. Owner framing: PC rules/errata are popular houserules/mods of the Decipher game.
- Future: translate wiki + dynamic card text on original scans for languages that never had a print run (IT, DE, ES, …). Official printings were EN + some JP (and ES Premiere as artifact). Schema/templates must not be English-only even though Phase 6 is later.

### 2026-09-19 — round 5 answers

- Sequence: rails first (MediaWiki + chrome + draft-tab + banner) while Premiere corpus proceeds.
- Main Page: directory + start here.
- Designers: hub + sourced name pages in the live bar.

### 2026-09-19 — round 4 answers

- Virtual depth: recommend and lock → stub every Current Virtual card; Legacy = hubs + checklists.
- Card URLs: recommend and lock → stable ID canonical, human titles redirect.
- Import: one GEMP-paste copy box; one side per deck page.
- Skin: match swccg.com landing chrome.
- Worlds sources: public + archive. No private-stash gate.

### 2026-09-19 — round 3 answers

- Trusted editors: recommend and lock → appoint + 10 accepted pending revisions.
- Edit UX: draft tab (pending revision).
- Rulebooks in live bar: core three.
- Virtual cards: own sets. Current Virtual and Virtual Legacy sit below Decipher sets. PC authorship must be obvious.
- AI prose: pending queue only.

### 2026-09-19 — round 2 answers

- Engine: recommend and lock → MediaWiki.
- Publish: suggestions only until trusted.
- Live bar: Premiere complete; stubs for every later Decipher card; rulebooks as pages; Worlds 1996–2001; decklist pages + GEMP import; PC + virtual + GEMP origin pages. Not live-bar: Scomp search, GEMP hover.
- External events: archive then curated import.
- Player pages: start from notable/sourced; when play.swccg.com tournaments complete and lists are shared, publish GEMP username + deck and append to that username’s page.

### 2026-09-19 — intake from owner

Goals stated:

1. Premiere information site (better than Wikipedia / Wookieepedia / smattering on swccg.org).
2. Integrate wiki with SWCCG GEMP: shared images/card data; right-click to wiki; ingest tournaments and decklists; hover previews; GEMP-importable lists.
3. Full Decipher historical layer (sets, cards, designers, Worlds 1996–2001) in the spirit of wiki.lotrtcgpc.net.
4. Modern layer: PC page, virtual cards, GEMP origin page.
5. Sourced + archived (archive.org / archive.today), including PC site.
6. Shared SSO with swccg.com GEMP; contribution open enough to keep memory alive.
7. Cheap anti-spam so a one-person shop survives.
8. Wiki as foothold so people play *this* GEMP.
9. Make swccgdb, Stephenskilton decktech archives, and Scomp-class lookup unnecessary here.

Public stance already locked in `legal-and-community.md`: do not wage a calendar war; host PC Standard as one format; measure our traffic and games.
