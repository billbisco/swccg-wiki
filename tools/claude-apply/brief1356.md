You are preparing wiki drafts for the SWCCG encyclopedia (swccg.com/wiki), ticket swccg-guild/work#1356. Nothing you do writes to the wiki; Holocron Claude (the main session) applies your drafts. Bill's goals: truth, accuracy, completeness. No redirects as a fix: repoint links, and list a true duplicate for deletion (delete.tsv).

## Rules (binding; read first)
- /mnt/user-data/uploads/gythe/.grok/grok-skills/shared/swccg-wiki-core-rules/SKILL.md and .../shared/swccg-wiki/SKILL.md; team notes: billbisco/ai-team-skills shared/swccg-wiki/team-notes.md (fetch via raw.githubusercontent.com if not under the uploads mount).
- Bill's version rules: a family is same side + name + type + picture. A re-made image (same words, new render/art/mark) is its own version (23 Nov); only a 180° turn is not. A same-words PC slip (a crop of an existing card image on a release/errata sheet) is a NOTE on the version whose image it reprints, not its own page (17 Nov). Number versions by release order and record the printed mark as printed (12 Nov). Do not invent errata. Unknown facts go to [[Mysteries]] via {{Mystery}}.
- Verify by looking at images (download from swccg.com/wiki/Special:FilePath/<file>, compare pixels/crops); never decide from titles alone.
- Keep each page byte-for-byte except your intended change. Keep every <ref> a page still uses; if a version list moves into a note, keep its sources.
- Previous worked example: /home/claude/r1350/rulings.md (Kelnacca, Captain Khurgee, Sacrifice For Something Bigger) and /home/claude/r1350/ drafts.

## Network
The container reaches swccg.com and GitHub only. Use the wiki API read-only (https://swccg.com/wiki/api.php) and action=parse with text= to preview drafts for cite errors. For web.archive.org or res.starwarsccg.org use mcp__remote-devices__device_bash (Bill's PC VM, ≤50 s per call, scratch in /tmp).

## Output (folder given below)
- apply.tsv: Title<TAB>drafts/<folder>/<file>.wiki, navigator templates first; base_revids.json {title: live revid you built on; null for a new page}; one .wiki per page.
- delete.tsv: Title<TAB>reason<TAB>links repointed (only pages with zero remaining links after your drafts, excluding the page's own Talk page).
- moves.tsv if a move keeps history better than delete+create: old<TAB>new<TAB>source revid.
- rulings.md: every decision with links and the evidence (file names compared), a "Team notes" section naming whose edit caused each error, and anything unresolved.
Report counts at the end. Keep going until your scope is complete.
