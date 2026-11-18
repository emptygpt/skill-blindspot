# Five public coding skills, audited with blindspot 0.3

Audit date: 2026-11-17. Tool: `blindspot` 0.3.0 with the `software` map 0.1.0 (90 nodes, every node sourced). One run per skill by a Claude Sonnet subagent. Every Needed finding was then re-checked in a separate pass (Claude Opus, reading and grepping the skill's whole repository, code included). No person checked them.

This is a small run with two purposes: try the new `software` map on popular skills, and see whether 0.3.0 fixes what went wrong in the [video report](video-20.md), where a [re-check](video-20/recheck.md) found that only 12 of 46 Needed findings held at that level.

## Results

| # | Skill | Covered / shallow / absent / n.a. | Needed | Needed findings |
|---|---|---|---|---|
| C01 | [obra/superpowers](https://github.com/obra/superpowers) `subagent-driven-development` | 19 / 9 / 27 / 35 | 0 | None. Candidates were covered by sibling skills it calls, such as the full test run in `finishing-a-development-branch`. |
| C06 | [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills) `code-review-expert` | 18 / 13 / 16 / 43 | 2 | The review never reads the change description, issue or spec, so it cannot check the change does what it is meant to. It never checks whether the diff adds or updates tests. |
| C07 | [mattpocock/skills](https://github.com/mattpocock/skills) `tdd` | 4 / 5 / 2 / 79 | 1 | "Write the failing test first" is never followed by "run it and see it fail for the right reason", or by running the suite after green. The repository's own docs quote a user whose agent skipped exactly this. |
| C12 | [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) `git-workflow-and-versioning` | 10 / 9 / 4 / 67 | 3 | Resolving conflicts and splitting a messy working tree are promised in the description and absent from the body. `git reset --hard HEAD` is advised with no warning that it discards uncommitted work, and nothing says when the agent may push or tag. |
| C17 | [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill) `security-audit` | 28 / 5 / 1 / 56 | 2 | The hunter and verifier agents read the target repository but are never told that its text is evidence, not instructions. Secrets found in the target can be copied into shareable findings and reports; the existing credential rule covers the captured environment only. |

Full reports, with the map table and quoted lines: [reports/code-5/](code-5/).

All 8 Needed findings held on re-check. Several reports also credit what the skill already has instead of calling it absent: C12 notes that force-pushing is listed as a red flag, and C17 quotes its environment-credential rule before explaining why it does not cover secrets found in the target.

## What the map adds here

- Each Needed finding names a public source the author can read: OWASP's Top 10 for LLM Applications (LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM06 Excessive Agency), GitHub Docs on merge conflicts, Google's engineering practices, ESCO and O*NET task statements.
- One Needed finding (C12, splitting a working tree into commits) has no source in the map and is marked unsourced.
- The `software` map has no nodes for debugging method, refactoring or release rollback, because no source we could cite covers them. They are listed in the map's header. Skills in those areas get fewer map-backed findings.

## Did 0.3.0 fix the video problems?

We re-ran two video skills whose Needed findings had failed the re-check.

- **V13** (stops at a local file): the platform AI-label finding, out of scope for this skill, moved from Needed to Worth considering. The new Needed finding, no check that captions match the narration, holds.
- **V20** (drives an engine): the first 0.3.0 run repeated the old mistake. Its AI-label gate lives in engine code, and the helper only read prose files. We added a `grep` command that searches code too and made it a required step before rating anything Needed. The next run found the gate and rated the node covered. Its one Needed finding, no ad disclosure for a UGC ad format whose own file says the ad "must not look like an ad", is a judgment call: the re-check reviewer had rated ad disclosure Minor.

Two re-runs are not a measurement. They show the two failure causes from the re-check, unread files and scope, are now handled by the procedure.

## Cost

The helper writes a worksheet in place of the full map. For these runs it was 21 to 28 KB, 37 to 49 percent of the 58 KB `software.yaml`. Each audit used about 90 to 110 thousand tokens with Claude Sonnet.

## Limits

- Five skills, one run each. The Needed findings were re-checked by a second model pass, not by a person; Worth considering and Minor findings were not re-checked.
- `software` 0.1.0 is new. Its 276 locators were checked against the fetched sources, but the node set has not been used on many skills.
- Code was searched, not run.

If a finding about your skill is wrong, please open an issue.
