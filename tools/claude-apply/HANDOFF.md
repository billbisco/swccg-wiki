# Handoff: Versions navigators (#1325) and Errata tables (#638)

Written by Claude on 25 Nov 2026 so another agent (Grok Build or anyone) can continue without asking. Bill's three launch-critical wiki tracks are on his dashboard (link on [#1325](https://github.com/swccg-guild/work/issues/1325)). Track 2: every card family has a correct shared Versions navigator. Track 3: an Errata comparison table wherever it makes sense.

## State (25 Nov 2026, evening UTC)

**Track 2 is done:** the census (3,786 families) shows 0 open gaps ([evidence/1325 at b9dfa77](https://github.com/swccg-guild/work/tree/b9dfa77c6e9eab1189e946779ef2d0ac3c4d9c10/evidence/1325)). #1325, #1341–#1348, #576, #596 and #1353 are closed. Decided splits and rulings live in `rulings.tsv`, which census.py reads; add a row there for every new evidence-based ruling, so decided cases stay out of gaps.tsv.

| Ticket | What | State |
|---|---|---|
| #1350 | Small card-data fixes + 11 Dantooine decklist relinks | Done 25 Nov (closed) |
| #1356 | #1350 follow-ups: fold 127 same-words slips, transcription-error wording, dated decklist relinks | Open: agents r1356a–d drafting |
| #1351 | 274 version chains the errata generator refused | Open: about 1,100 saves done. The 25 Nov rerun (`errgen/rr2.sh`) cleared all but 41 families: 13 have redirect chain pages (agent r1351r1) and 28 have unsourced order (agent r1351u) |
| #677 | Virtual Block 3 errata (ChatGPT) | Open, not ours |
| #715, #716 | Planned/independent sets pilot; final errata reconcile | Open |
| #1349 | Wiki 2 MB upload limit (server setting) | Bill |
| #527 | Premiere Virtual Set 1 navigators/edition names (Grok Build) | Census shows no navigator gaps; edition-name part not checked |

To keep track 2 at 0: re-run `census.py --refresh` after new card pages appear, and draft any gap with navgen plus the pipeline below.

## Tools (this folder; generators in ../errgen and ../navgen)

- `navgen/navgen.py`: drafts navigators from the census (`--ticket N` or `--family "<label>"`). `render_template()` and `member_edit()` are the house pattern (Theed Palace #1303). Completing an EXISTING navigator: see `build_complete_example.py` (used for #1347); keep the template title, add missing members, re-render.
- `navgen/check_nav.py <draftdir>`: checks a draft group (members only change `|versions=`, every member transcludes, no unexpected byte changes).
- `errgen/errgen.py --origin-set "Virtual Set N" --era "Virtual Modern" --out DIR --keep-stamp-only [--family "Name [Side type]"]`: Errata tables. Refuses instead of guessing; reasons in `refused.tsv`.
- `errgen/census638.py`: errata census. `census.py --refresh` (in swccg-guild/work `evidence/1325`): navigator census (~6 min).
- `navbrief.md`: the brief given to each drafting agent (rules, ordering, output format).
- `qa.py <dir with apply.tsv>`: purges, then parses every page; reports cite errors and red links. Pre-existing card-text red links (Setup, Dark Jedi Master, Personal Force, Scoundrel, New Republic, Lost or Starting Interrupt, Skywalker) are known and not ours.
- `reffix.py <draftdir>`: if an old inline list held `<references />`, adds `|has_refs=1` so the reference list still shows. Run before every apply.

## Apply pipeline (on Bill's linked PC; PC VM device calls die after ~60 s, so everything is short rounds)

Draft group format: `apply.tsv` (Title<TAB>drafts/<dir>/<file>), `base_revids.json` (live revid, 0 = new page), one `.wiki` per page ("/" → "%2F").

1. Container → PC: `tar czf /mnt/user-data/outputs/X.tgz <dir>`, then `device_commit_files` to `~/.grok/claude-agent/X.tgz`.
2. Split into groups in `/tmp/batches`: `~/w/tools/eset.py X.tgz <dir> <ticket>` makes `e<ticket>t` (templates) and `e<ticket>m0..` (15 members each). For navigator groups, use the same split with your own prefix.
3. Add an edit summary for the prefix in `~/w/tools/step.sh` (the `case $g in` block; every summary names the ticket).
4. Apply: put the group names in a file, then run `~/w/tools/rounds.sh <file> 3` repeatedly. It runs at most 10 groups at a time; more parallel sign-ins get HTTP 429. Templates go first. `~/w/tools/st.sh <groups>` shows done/total and any non-OK row. `apply_guarded.py` uses baserevid, so it never overwrites a newer edit.
5. Backup: `backup_api.py <titles-file> "<msg>"` with GH_TOKEN from `~/.grok/claude-agent/github-token.env`. Use ≤130 titles per call. Template-heavy chunks are slow, so run them alone. It retries 422 (main moves because other sessions commit) up to 6 times.
6. QA in the container: `python3 qa.py <dir>`. Fix every cite error before reporting.
7. Report on the ticket with `~/ais/shared/swccg-guild-tickets/board_as_claude.py comment|status|close <n>` (posts as HolocronClaude; read SKILL.md there). Every list item is a link. Then close done tickets and update the dashboard (`~/w/index.html` → scp to gemp `/var/www/swccg.com/launch-UHuWqnjq8oS2hNTY7Kxfbjg0i9wJ/index.html`, keeping a .bak).

## Moves and deletions (no redirects as a fix, Bill 25 Nov)

- **Moves:** Holocron Claude has `move` and `suppressredirect`. Use `~/w/tools/mvpages.py <tsv old\tnew\texpected_revid> "<reason>"` (in this folder). It moves the Talk page too, leaves no redirect, refuses on drift, and prints the new latest revid. Use that revid as the base for any draft applied to the new title. A move onto an existing title only works if that title is a one-revision redirect back to the source; otherwise delete it first.
- **Deletions:** the bot has no `delete` right. Run the MediaWiki maintenance script on the VPS from the PC VM. Copy `~/.grok/claude-agent/ssh/id_ed25519` to `/tmp/gk` (chmod 600), then:
  `scp -i /tmp/gk list.txt root@2.28.125.5:/tmp/x.txt && ssh -i /tmp/gk root@2.28.125.5 'docker cp /tmp/x.txt swccg_wiki:/tmp/x.txt && docker exec swccg_wiki php maintenance/run.php deleteBatch -u "Holocron Claude" -r "<reason, ticket>" /tmp/x.txt'`
  Only delete a page with zero remaining links (check its real wikitext, not just `list=backlinks`, which lags), and back up the deleted title's last content first.

## Rules learned the hard way

- Never let a shared template reuse a member page's `<ref name=…>`. Member pages define the same names with slightly different text, which causes "defined multiple times" cite errors. errgen now prefixes `errgen-`.
- `card_params` must not split on `|` inside `<gallery>`/`<ref>`.
- Playtest printings are not published text states (no Errata column). Some pages count them in "version N of M" and some don't.
- A Virtual slip printed over two host cards goes in both hosts' navigators (Alter ruling, #1348).
- Unknown dates: make the best evidence-based reading and log the question on [[Mysteries]] with {{Mystery}} (Bill's rule).
- Bill approves doing what needs doing. Don't ask him step by step. File tickets for anything unfinished.
