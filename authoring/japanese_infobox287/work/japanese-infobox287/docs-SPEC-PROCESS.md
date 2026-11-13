# Spec process

This is how every piece of work goes from an idea to done. It's a light mix of two methods:

- **Spec Kit** gives the flow: spec, then plan, then tasks, then verify.
- **Design Log** gives a running decision record for each Epic.

If you know Jira or ADO, read it as: **Idea = a new item; Spec = the description and acceptance criteria; Plan = the breakdown into child items; Verify = the test evidence.**

## The flow

| Step | What it is | Where it lives | Board status |
|---|---|---|---|
| 1. Idea | One line, so it's out of your head | **Idea** issue form, labeled `needs-ac` | Backlog |
| 2. Spec | The *what* and *why*: user story, requirements, acceptance criteria, out of scope, open questions | Issue body, from the **Epic** or **Story** form | Backlog |
| 3. Plan | The *how*: approach, repos and files touched, risks, breakdown | **Plan** section of the issue; for Epics, also the design log | Backlog → **Ready** once the Definition of Ready is met |
| 4. Tasks | Child Stories and Tasks under the Epic | **Sub-issues** | Ready → In Progress |
| 5. Verify | Proof that each acceptance criterion is met | `evidence/<ticket>/`, a `PASS-REPORT v1` comment, then Test and Play deploys (a `REVIEW: PASS` only when Bill asks for one) | In Progress → **In Test** → **Done** (Done = on Play) |

### 2. Spec: what goes in it

- **User story:** "As a <player / editor / Bill>, I want <capability> so that <benefit>."
- **Requirements:** numbered R1, R2 and so on. Each one says what must be true, not how to build it.
- **Acceptance criteria (AC):** numbered AC1, AC2 and so on. Each must be **testable**. Write them as either:
  - Given / When / Then. Example: "Given card 'Tarkin (V)' in CardMaker, when it is built, then title, lore and game text match the PC slip word for word."
  - A checklist item a reviewer can tick from evidence. Example: "Full test suite passes; log in evidence/<n>/tests.txt."
- **Out of scope:** what this ticket deliberately won't do.
- **Open questions:** anything genuinely unknown. **Don't guess; ask.** Each question names who can answer it (`@Bill`). An answer is appended below its question; the question is never deleted.

### 3. Plan: what goes in it

- **Approach:** two to five lines.
- **Repos and files touched**, for example `billbisco/swccg-gemp`, a wiki page, a VPS service.
- **Breakdown:** the list of child Stories and Tasks, linked once created.
- **Risks:** what could break, and what needs `needs-bill` approval (server *configuration* changes, spending, public posts, deletions; routine app deploys after a passing `PASS-REPORT v1` don't).
- **Verification:** how each AC will be proven, mapped one to one to the AC.

## Design log (Epics, and any Story with a real decision)

- **File:** `docs/design-log/<issue#>-<slug>.md`, for example `docs/design-log/5-virtual-legacy-gemp.md`.
- **Append-only.** Never edit or delete an old entry. If a decision changes, add a new entry that supersedes the old one.
- **Each entry:**

```markdown
### YYYY-MM-DD — <decision in one line>
- **Decision:** what we decided
- **Why:** the reason, with evidence or links
- **Alternatives considered:** what else we looked at and why not
- **Who:** who decided (Bill / Chief / agent name)
- **Status:** proposed | decided | superseded by <date>
```

- Link the design log from the Epic, and mention new entries in a ticket comment.

## Definition of Ready (the gate to Ready)

A ticket can move to **Ready** only when:

1. The spec is complete: user story, requirements, testable AC and out of scope.
2. **No open questions are unanswered.** Unanswered questions mean the ticket stays in Backlog with `needs-ac`, or `needs-bill` if Bill must decide.
3. The plan is filled in, including how each AC will be verified.
4. **Epics: Bill approves.** He comments `READY: approved` or moves the Epic to Ready himself. Stories and Tasks under an approved Epic can be moved to Ready by Chief.
5. For Epics, the design log exists with at least one entry.

**Agents may move a ticket to Ready themselves after Bill's answers** (Bill, 2026-11-03: "if I answer all the questions appropriately and sufficiently. And there are no further questions or clarifications, go ahead and just move a ticket to Ready as part of the process"). When every open question has Bill's answer appended, no clarification is left, and items 1, 3 and 5 hold, the agent comments `READY: approved (<agent>)`, says it comes from Bill's answers (quote them or link where he answered), and moves the ticket, Epics included, to Ready. This counts as Bill's approval for item 4.

**No coding, page edits or server changes happen before Ready.** Research and read-only investigation to answer open questions is fine.

## Definition of Done

**Done means deployed to Play** (our production server, the final step). The path is: passing `PASS-REPORT v1` → deploy to the **Test** server and verify it works (**In Test**) → deploy to **Play** and verify → **Done**. Test and Play deploys often happen together. Bill usually does **not** test; the agents do, and the evidence proves it.

A ticket is **Done** only when:

1. Every AC is checked, each with evidence in `evidence/<ticket>/` or a link to it (diff, PR, test log, screenshot).
2. The implementing agent has posted a `PASS-REPORT v1` comment with Overall: PASS (format in [AGENTS.md](../AGENTS.md)).
3. Only if Bill asked for a review on the ticket: a second agent has posted `REVIEW: PASS`. By default there is no peer review (Bill, 2026-11-02).
4. It is **deployed to Test and verified working** there, with evidence (Status **In Test**).
5. It is **deployed to Play and verified working** there, with evidence. Then it is closed and Status is **Done**.
6. Any decisions made along the way are recorded in the design log.

Notes:

- **Areas without a separate Test server** (wiki pages, skills, docs): "Test" is the staging or sandbox copy where one exists (for example a wiki sandbox page); otherwise the live change is verified directly and the ticket goes In Progress → Done once the evidence shows it live.
- **Bill's role:** Bill approves Epics at Ready (`READY: approved`) and answers `needs-bill` questions. He is not the tester.
- **Deploys need no per-deploy OK from Bill** (Bill, 2026-11-01). Once the agent's own `PASS-REPORT v1` passes (no peer review unless Bill asks for one (Bill, 2026-11-02)), the assigned agent deploys it to Test, verifies it, then deploys it to Play and verifies it.
- **Routine app deploy vs. server configuration change.** These are different things:
  - A **routine app deploy** ships the reviewed change through the existing deploy path, for example a GEMP build, the live CardMaker or the site. That includes the CardMaker repo push. It needs no approval beyond a passing `PASS-REPORT v1`.
  - A **server configuration change** still needs Bill's approval (`needs-bill`) before it is made on Test or Play. That covers the OS and packages, Docker or compose settings, web server or proxy config, DNS or TLS, firewall or SSH, databases, cron or systemd units, disk layout, and anything that costs money.
  - If a ticket needs both, get Bill's OK for the configuration part first.
  - Spending, public posts and deletions outside the box still need `needs-bill` too.

An Epic is Done when all of its sub-issues are Done **and** its own AC are met on Play.
