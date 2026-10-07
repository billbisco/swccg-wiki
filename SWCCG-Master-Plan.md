# swccg.com — Master Plan Brief

Internal working brief for the Star Wars CCG site. Pair with the Grok skill `swccg-project`.

## One-sentence mission

Make swccg.com the place you learn, look up, and play Star Wars CCG as Decipher published it — and as later communities modified it — without collapsing those layers into one “current” card.

## Product shape

| Face | Job |
| --- | --- |
| Landing | Why the game matters, how to start, news |
| Wiki | Sets, cards, rules, championships, rulings, history |
| Forums | Talk, decks, organized play this site runs |
| Play | Own GEMP-class instance, cards linked to the wiki |

One identity: local username/password (required for regions that block Google/Apple/Discord) plus optional Google, Apple, Discord SSO.

Shared card corpus and shared images. No second copy of Vader’s art in the wiki and another in the client.

Pattern to study: LOTR-TCG wiki + GEMP-LOTR + Player’s Council site + forums.

## Principles

1. Versioned text. Printed / Decipher errata / PC errata / virtual / house, each sourced.
2. Rulings live on the card page, not only in a PDF or a forum thread.
3. Formats pick a ruleset + a text snapshot. Bots train on one snapshot at a time.
4. Mods are fine when marked. Unmarked overwrite is the thing this project exists to stop.
5. Fan project. Not Lucasfilm. Not a drop-in replacement announcement for the Players Committee.

## Phases

0. Charter, legal posture, source inventory, honest landing page  
1. Corpus + wiki IA + Premiere as the proof set + rulebooks as HTML  
2. SSO + forums  
3. Own play instance + one historical format + wiki hover  
4. Tested heuristic bots on that format  
5. Short Shandalar-like campaign as the new-player engine  
6. Official JP/ES as artifacts, then new translations labeled unofficial  

Do not start 4–6 before 1 is real.

## Honest constraints

- Disney/Lucasfilm still own the IP. GEMP’s MIT license covers engine code, not art or names.
- `swccg-card-json` and Scomp are the live PC layer. Ingesting them without a printed-text pass produces another current-only database.
- GEMP implements cards in Java, one behavior at a time. Historical variants and AI training are not a config flag today.
- The PC already has the players, the events, and twenty-five years of volunteer infrastructure. Winning is “better archive + better on-ramp,” not a flame war.

## Immediate next decisions

1. Public tone toward the PC  
2. Whether Phase 1 wiki is MediaWiki (LOTR parity) or something else  
3. Who owns corpus work vs site work among existing coding bots  
4. Where card scans will live (do not assume Holotable’s CDN)
