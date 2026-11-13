# AGENTS.md: how AI agents work tickets here

This file is for every agent that works these tickets: Grok Bot (Chief and Alpha1 to Alpha12), Grok Build, Claude (Code and Desktop), ChatGPT and Codex. People should read [README.md](README.md) first.

## 1. Where things are

- **Tickets:** issues in this repo. The issue types are Epic, Story, Task and Bug. Epics hold their Stories and Tasks as **sub-issues**.
- **Board:** the org Project **SWCCG Work**. Status values are Backlog, Ready, In Progress, In Review, **In Test** (deployed to the Test server and verified working) and Done (deployed to **Play**, our production server). The board also has these fields:
  - **Agent:** Chief, Alpha1 to Alpha12, Grok Build, Claude, ChatGPT or Bill.
  - **Priority**
  - **Area**
  - **Points**
- **Evidence:** screenshots, logs and diffs go in `evidence/<ticket-number>/` in this repo (see [evidence/README.md](evidence/README.md)).
- **Tools:**
  - Grok Bot uses its GitHub connector, or `gh` on the box.
  - Grok Build and Claude Code use `gh` or the GitHub MCP server.
  - ChatGPT uses a GitHub connector. It reviews when asked; it does not claim work.
- **GitHub identity (Bill, 2026-11-08).** Use your assigned reviewer account for new issues, issue edits and assignments, comments, and every SWCCG Work board edit. This includes the initial Story post. Verify the author after issue creation. If the reviewer credential cannot perform the write, report the blocker. Use billbisco for Git and release operations.
  - [GitHub board identity](https://github.com/billbisco/ai-team-skills/blob/main/docs/GITHUB-BOARD-IDENTITY.md) lists the accounts and explains how to scope the credential to each call. Never put a token in a ticket, comment, evidence file, screenshot or chat.

## 2. Ticket workflow (follow [docs/SPEC-PROCESS.md](docs/SPEC-PROCESS.md))

**Hard rule: no coding, page edits or server changes before a ticket is Ready.** Ready means it meets the Definition of Ready in SPEC-PROCESS.md. Before Ready you may do read-only research to answer open questions.

| Step | Who | What | Status |
|---|---|---|---|
| Idea | Bill or anyone | File an **Idea** (one line). It gets the label `needs-ac`. | Backlog |
| Spec | Chief, or the assigned agent | Fill in the spec: user story, requirements, testable AC (Given/When/Then or a checklist), out of scope and open questions. Unknowns become open questions, **never guesses**. | Backlog |
| Plan | The assigned agent | Fill in the plan: approach, repos and files touched, breakdown into sub-issues, risks, and verification for each AC. For an Epic, create `docs/design-log/<issue#>-<slug>.md` with its first entry. | Backlog |
| Ready | Chief; **Bill for Epics** (`READY: approved`) | Check the Definition of Ready: no open questions unanswered, the plan is filled in, and the design log exists for Epics. Remove `needs-ac` / `needs-bill`. | Backlog → Ready |
| Ready (after Bill's answers) | The assigned agent, Chief | Once Bill has answered every open question sufficiently and no clarifications remain, you may move the ticket (Epics too) to Ready yourself: comment `READY: approved (<you>)`, say it comes from Bill's answers, and quote or link where he answered (Bill, 2026-11-03). | Backlog → Ready |
| Claim | The assigned agent | Comment `CLAIM:`, set **Agent** on the board, and assign your reviewer account (section 1), all with your reviewer token. | Ready → In Progress |
| Implement | The assigned agent | Stay within the spec. Work on staging or test pages first. Record every real decision or deviation in the design log (append-only), and mention it in a comment. | In Progress |
| Verify | The assigned agent | Run the area's checks, save evidence to `evidence/<n>/`, and post `PASS-REPORT v1`. On FAIL, fix and post again. | Stays In Progress until deployed (next rows) |
| Review (only when Bill asks) | A *different* agent (Chief, another Alpha, or Claude/ChatGPT) | **Skipped by default:** no peer review unless Bill asks for one (Bill, 2026-11-02). When Bill calls for a review on a ticket, the reviewer comments `REVIEW: PASS` or `REVIEW: CHANGES`. | In Review → deploy to Test, or back to In Progress |
| Test | The assigned agent | After your own `PASS-REPORT v1` with Overall: PASS (and Bill's requested review, if any), deploy to the **Test** server on your own, with no per-deploy OK from Bill. Verify it works there and attach the evidence. If it fails, back to In Progress. | In Progress → **In Test** |
| Play | The assigned agent | Deploy to **Play** (production) on your own, verify it works there, attach the evidence, and close. Test and Play deploys are often done together. Server *configuration* changes still need `needs-bill`. | In Test → **Done** (close) |

Rules:

- **Ticket first (Bill, 2026-11-13).** All SWCCG work has a ticket before the first edit (a stub Idea or Task
  is fine). Small chat asks from Bill that are finished and verified in the same turn are logged on the agent's
  weekly `Quick fixes <agent> <YYYY-Www>` Task. Bill's chat words are that Task's spec, and it closes at week's
  end. Anything else gets its own ticket.
- **Stop note.** Whenever work stops before Done (parked, interrupted, handed off, end of session), the agent
  posts `PROGRESS: (<agent>) stopped` with *Done so far / Stopped at / Next step / Waiting on / Where the work is*,
  after pushing branches (draft PR, `Refs #<n>`). Live but unmerged code is not Done.
- **Unclear AC, or a new unknown found mid-work:** don't guess. Add it to the ticket's **Open questions**, comment `QUESTION @Bill:`, and add the `question` label (plus `blocked` if you can't continue).
- **Anything needing Bill's approval** gets the `needs-bill` label. That covers server **configuration** changes (OS and packages, Docker or compose settings, proxy or web server config, DNS or TLS, firewall or SSH, databases, cron or systemd units, disk layout), spending money, posting publicly, and deleting anything outside the box.
- **Routine app deploys don't need Bill** (Bill, 2026-11-01). After its own passing `PASS-REPORT v1` (no peer review unless Bill asks for one (Bill, 2026-11-02)), the assigned agent merges its own PR and deploys to Test and then to Play on its own, through the existing deploy path, with no per-deploy OK. If the deploy also needs a configuration change, that part needs `needs-bill` first. Stop until Bill answers on the ticket or in chat.
- **Spec changes after Ready:** don't silently edit the spec. Add a design-log entry with the reason, comment `PLAN:` describing the change, and for an Epic get Bill's OK.
- **Linking PRs:** write `Refs #<n>` in a PR, not `Fixes`/`Closes #<n>`. A closing keyword closes the ticket at merge, which marks it Done before it is on Play.
- **One agent per ticket.** Split large work into sub-issues instead of sharing one ticket.
- **Who closes:** the ticket closes once it is verified on Play and the agent's passing `PASS-REPORT v1` is on record (plus `REVIEW: PASS` only where Bill asked for a review). Bill approves Epics at Ready; he is not the tester and does not need to test before Done.

## 3. Definition of done

A ticket is done only when all of these are true:

1. Every acceptance criterion is checked, and each has evidence linked or stored in `evidence/<n>/`.
2. The implementing agent has posted a `PASS-REPORT v1` comment with Overall: PASS.
3. Only where Bill asked for a review on the ticket: a different agent has posted `REVIEW: PASS`. Otherwise no peer review is needed (Bill, 2026-11-02).
4. The area's gates pass:
   - **Wiki:**
     - style lint shows 0 issues;
     - every new citation has a Wayback copy that passes the strict check;
     - the edit is a section edit with basetimestamp, and no other bot's revision was overwritten;
     - before, after and diff screenshots are attached;
     - no personal emails.
   - **GEMP:** the named tests and the full suite are green, and the PR is linked.
   - **Server:** for configuration changes, Bill's approval is on record (routine app deploys need only a passing `PASS-REPORT v1`); health checks pass, the rollback is noted, and the disk rules in the swccg-project skill are followed. **gemp `/tmp` is RAM (tmpfs)** — never put bulky working or handoff files there; use `/mnt/HC_Volume_107153504/work/<agent>-<task>-<YYYYMMDD>/` (Bill 2026-11-09).
   - **CardMaker:** every change to the live CardMaker is also committed and pushed to [billbisco/swccg-cardmaker](https://github.com/billbisco/swccg-cardmaker), with the commit linked. Builds are checked against the card's own era and the pass rule in [docs/design-log/6-virtual-cards-cardmaker.md](docs/design-log/6-virtual-cards-cardmaker.md).
   - **Site, AI-team:** the AC's own evidence. Skill changes are committed to `billbisco/ai-team-skills`.
5. No secrets, tokens, alert topics, personal emails or private IPs appear anywhere in the ticket or its evidence.
6. The implementation results and any deviations are recorded in a comment, and every decision made along the way is in the design log.
7. It was **deployed to Test and verified working** (Status In Test), with evidence.
8. It was **deployed to Play and verified working**, with evidence. Done means on Play. (Areas with no Test server: see the notes under Definition of Done in [docs/SPEC-PROCESS.md](docs/SPEC-PROCESS.md).)

## 4. PASS-REPORT v1 (copy exactly; scripts parse the first line)

```markdown
PASS-REPORT v1 — ticket #123 — agent: Alpha7 — 2026-11-02 14:05 (UTC-4)
| AC | Result | Evidence |
|---|---|---|
| AC1 Section exists at Jokes#X | PASS | https://wiki.swccg.com/index.php?diff=…; evidence/123/after.png |
| AC2 Lint 0 | PASS | style_lint.py output: 0 issues |
| AC3 Wayback strict | PASS | 4/4 refs ok (evidence/123/wayback.txt) |
| AC4 No overwrite of other bots | PASS | basetimestamp 2026-11-02T18:01:22Z, no edit conflict |
Overall: PASS
Visual diff: evidence/123/before.png · evidence/123/after.png · evidence/123/diff.png
```

- **Overall** is exactly one of:
  - `PASS`
  - `FAIL — <which AC>; fixing`
  - `UNSURE — needs Bill on <question>`
- If something failed, start the first line with `FAIL-REPORT v1` instead.
- Times are in UTC-4 (Caracas) unless a value carries its own zone.

## 5. Comment prefixes

Start every comment with one of these words. Comments post as your reviewer account (section 1), and several agents share one account (all Grok agents are DatacardGrok), so **always name yourself** after the prefix, for example `CLAIM: (Alpha7)`.

| Prefix | Meaning | Also do |
|---|---|---|
| `CLAIM:` | I'm taking this ticket. | Set Agent, assign your reviewer account, and move Status to In Progress. |
| `PLAN:` | The plan is filled in, or the spec or plan changed. | Add a design-log entry for any decision. For Epics, wait for Bill's `READY: approved`. |
| `READY: approved` | The Definition of Ready is met. Bill posts it, or an agent posts `READY: approved (<agent>)` once Bill has answered every open question sufficiently and no clarifications remain, citing his answers (Bill, 2026-11-03). | Remove `needs-ac` / `needs-bill` / `question`, and move Status to Ready. |
| `QUESTION @Bill:` | The AC are unclear or a decision is needed. | Add the `question` label, and `blocked` if you can't continue. |
| `HANDOFF @<agent>:` | This needs another agent, for example a GEMP bug found while editing the wiki. | Open a linked issue or sub-issue. The other agent replies `CLAIM:`. |
| `BUG:` | I found a defect. | Open a Bug and link it here. |
| `PROGRESS:` | Status note. Required when work stops before Done (stop-note fields in section 2); otherwise optional, at most one per session. | None. |
| `PASS-REPORT v1` / `FAIL-REPORT v1` | See section 4. | PASS: deploy to Test and Play (no review step unless Bill asked for one). FAIL: keep it at In Progress. |
| `REVIEW: PASS` / `REVIEW: CHANGES` | The second agent's verdict, only on tickets where Bill asked for a review. | PASS: deploy to Test and move Status to In Test once verified. CHANGES: back to In Progress. |

## 6. Screenshots and images (Grok Build can't take pasted images)

- Save images as `evidence/<n>/<short-name>.png` or `.webp`, at 500 KB or less each, and push them to `main`.
- Embed them in a comment with a path relative to the repo, `evidence/<n>/after.png`, or with its blob URL.
- To read the images on a ticket, run `git pull` and open the files by path. **Don't** ask Bill to paste images.
- Never commit screenshots that show secrets, tokens, email addresses or private dashboards.

## 7. Spec process

The full standard is in [docs/SPEC-PROCESS.md](docs/SPEC-PROCESS.md): Idea → Spec → Plan → Tasks → Verify, the Design Log, the Definition of Ready and the Definition of Done. Design logs live in [docs/design-log/](docs/design-log/).
The shared skills that teach this process to every tool live in `billbisco/ai-team-skills` (`swccg-guild-tickets` (formerly ~~`ticket-workflow`~~), `spec-and-verify`). They were added on 2026-11-02 under #2.
