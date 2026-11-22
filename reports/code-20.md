# Twenty public coding skills, ranked by audited gaps

Audit date: 2026-11-19. Tool: `blindspot` 0.4.1; `software` map 0.1.0 (90 nodes). One audit run per new skill by Devin.

[Independent re-check, scope decisions and consistency notes](code-20/recheck.md).

## Selection and method

The 15 new audits cover multi-stage coding workflows from seven widely used public repositories, with at most three new skills per repository. This was a purposive selection to cover areas the earlier five did not: debugging, finishing a branch, browser testing, MCP server building, PR writing, launch, deprecation, refactoring, differential review, patching, CI repair, security review and threat modeling. It is not a random sample or a prevalence estimate for public skills.

**The code-5 IDs came from a list of 20 that was not published.** The new IDs fill the gaps C02–C20; the earlier C01, C06, C07, C12 and C17 keep their IDs and link to their [original reports](code-5.md). There are 15 new audits, not 20 new runs. The earlier five retain their original audit dates, tools and model attribution; they were not rerun with 0.4.1.

For each new skill, the audit read its workflow, pointed-to prose, called skills and relevant code as data; wrote Scope and an Ask list before mapping; mapped all 90 nodes; traced outputs and checks; and searched the skill folder plus repository root before assigning Needed. Uncalled siblings do not provide coverage. Partial coverage must instruct part of the specific work, not merely a related topic.

## Results

**Ranking:** descending Needed after re-check, then descending absent + shallow nodes; exact ties use ascending ID. The after column counts **only originally Needed findings that held**, not a fresh rerating of every finding. C14-4 and the instruction-boundary part of C16-4 would rise from Worth considering to Needed under the consistency criterion; they are recorded separately and are not added to this column or the 4/1/0 re-check tally.

State counts describe **domain coverage within the declared scope**, not an overall quality score. Different boundaries make these ranks unsuitable as a general ordering of skill quality; in particular, not-applicable is not a failure. The top finding can be Worth considering or Minor when Needed is zero.

| Rank | ID | Skill | Covered / shallow / absent / n.a. | Needed (as audited) | Needed after re-check | Top finding |
|---|---|---|---|---|---|---|
| 1 | [C12](code-5/C12.md) | [addyosmani/agent-skills: git-workflow-and-versioning](https://github.com/addyosmani/agent-skills/tree/main/skills/git-workflow-and-versioning) | 10 / 9 / 4 / 67 | 3 | 3 | Promised conflict/splitting stages are missing; destructive Git actions lack guards. |
| 2 | [C06](code-5/C06.md) | [sanyuan0704/sanyuan-skills: code-review-expert](https://github.com/sanyuan0704/sanyuan-skills/tree/main/skills/code-review-expert) | 18 / 13 / 16 / 43 | 2 | 2 | The review lacks intended-behavior input and changed-test adequacy checks. |
| 3 | [C17](code-5/C17.md) | [cloudflare/security-audit-skill: security-audit](https://github.com/cloudflare/security-audit-skill) | 28 / 5 / 1 / 56 | 2 | 2 | Target-controlled instructions and discovered secrets can enter security reports. |
| 4 | [C04](code-20/C04.md) | [anthropics/skills: webapp-testing](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/webapp-testing) | 2 / 5 / 6 / 77 | 1 | 1 | Browser actions and screenshots lack an expected-outcome check. |
| 5 | [C18](code-20/C18.md) | [getsentry/skills: security-review](https://github.com/getsentry/skills/tree/a582c51ee29d0f35e6ac321340796f77d43da733/skills/security-review) | 12 / 9 / 2 / 67 | 1 | 1 | Repository text lacks a boundary against directing the security reviewer. |
| 6 | [C07](code-5/C07.md) | [mattpocock/skills: tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) | 4 / 5 / 2 / 79 | 1 | 1 | The test-first loop does not require observed red, green and suite results. |
| 7 | [C19](code-20/C19.md) | [openai/skills: gh-fix-ci](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/gh-fix-ci) | 6 / 5 / 2 / 77 | 2 | 1 | CI log text can redirect code repair; optional explicit-PR checkout binding is conditional. |
| 8 | [C20](code-20/C20.md) | [openai/skills: security-threat-model](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/security-threat-model) | 9 / 2 / 1 / 78 | 1 | 1 | Repository evidence lacks a boundary against directing the threat analyst. |
| 9 | [C05](code-20/C05.md) | [anthropics/skills: mcp-builder](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/mcp-builder) | 18 / 24 / 13 / 35 | 0 | 0 | Agree the consumer, transport and security baseline before selecting tools. |
| 10 | [C01](code-5/C01.md) | [obra/superpowers: subagent-driven-development](https://github.com/obra/superpowers/tree/main/skills/subagent-driven-development) | 19 / 9 / 27 / 35 | 0 | 0 | Security checks wait for final review rather than the task implementer/reviewer. |
| 11 | [C10](code-20/C10.md) | [addyosmani/agent-skills: shipping-and-launch](https://github.com/addyosmani/agent-skills/tree/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/shipping-and-launch) | 38 / 16 / 2 / 34 | 0 | 0 | Bind rollout and rollback to a retained, identifiable artifact. |
| 12 | [C13](code-20/C13.md) | [addyosmani/agent-skills: code-simplification](https://github.com/addyosmani/agent-skills/tree/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/code-simplification) | 15 / 13 / 2 / 60 | 0 | 0 | Existing passing tests may not demonstrate behavioral equivalence. |
| 13 | [C08](code-20/C08.md) | [mattpocock/skills: diagnosing-bugs](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/diagnosing-bugs) | 16 / 11 / 3 / 60 | 0 | 0 | Verify affected existing behavior beyond the single reproduced symptom. |
| 14 | [C11](code-20/C11.md) | [addyosmani/agent-skills: deprecation-and-migration](https://github.com/addyosmani/agent-skills/tree/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/deprecation-and-migration) | 20 / 11 / 2 / 57 | 0 | 0 | Demonstrate backfill equivalence and recovery before removing old schema paths. |
| 15 | [C02](code-20/C02.md) | [obra/superpowers: systematic-debugging](https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging) | 21 / 9 / 3 / 57 | 0 | 0 | Presence-only credential reporting exists, but broader diagnostic redaction is unspecified. |
| 16 | [C16](code-20/C16.md) | [getsentry/skills: iterate-pr](https://github.com/getsentry/skills/tree/a582c51ee29d0f35e6ac321340796f77d43da733/skills/iterate-pr) | 10 / 10 / 2 / 68 | 0 | 0 | Bind clean feedback/checks to complete current-head data; input-trust band is understated. |
| 17 | [C03](code-20/C03.md) | [obra/superpowers: finishing-a-development-branch](https://github.com/obra/superpowers/tree/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch) | 5 / 5 / 3 / 77 | 0 | 0 | Confirm the tested workspace is the tree Git will integrate. |
| 18 | [C14](code-20/C14.md) | [trailofbits/skills: differential-review](https://github.com/trailofbits/skills/tree/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/differential-review/skills/differential-review) | 5 / 6 / 2 / 77 | 0 | 0 | Adaptive scope shortcuts conflict with the final coverage promise; input-trust band is understated. |
| 19 | [C15](code-20/C15.md) | [trailofbits/skills: patching-bugs](https://github.com/trailofbits/skills/tree/149d7b21f4067765b82e67029730b42d228ef4b4/plugins/patching-bugs/skills/patching-bugs) | 25 / 4 / 1 / 60 | 0 | 0 | Extend proof execution limits across main build and proof-of-concept paths. |
| 20 | [C09](code-20/C09.md) | [mattpocock/skills: pr](https://github.com/mattpocock/skills/tree/5863806dd4e15c63174bee4e7515a4256792ecfa/skills/engineering/pr) | 0 / 2 / 2 / 86 | 0 | 0 | Explain motivation and distinguish measured evidence from illustrative pseudocode. |

The new batch had **5 Needed findings in 15 skills; 4 held, 1 was overstated and none was wrong**. The earlier five had **8 Needed; all 8 still hold** under scope rules 1–5. Original report counts and bands are unchanged. The two understated consistency findings are additional observations, not part of those five originally Needed findings; including them in a complete new-band tally would yield six rather than four for the new batch.

## Intentionally skipped

Some areas were not applicable on purpose, rather than overlooked:

- C09 `pr` ends at PR-body text: **86 n.a.** It does not implement changes, execute tests, open/merge the PR, deploy or perform rollback.
- C04 browser testing ends at browser automation/evidence: application fixes and production deployment are outside its boundary.
- C14 differential review and C18 security review end at findings/advice: implementing remediation, merge and deployment are not imported.
- C20 threat modeling ends at a model document: enumerating controls does not mean implementing or exhaustively auditing authentication, cryptography, dependencies or production operations.
- C03 branch finishing starts with implemented work; original feature design/implementation and production operations are not its job.

A skill can record deliberate exclusions in `.blindspot.yaml`; none of the selected skills had one. These reports therefore use profile `none` and zero profile-excluded nodes. A scope-based n.a. row is not a profile exclusion.

## Cross-skill patterns

Counts below were recomputed from all 20 report map tables with a small temporary analysis script **outside the repository**. Group rows in the older reports were expanded to individual map nodes; table counts were checked against each report's YAML. These are original audit states, not re-check severity counts.

- **Instruction/data separation — `agent.injected-instructions`: absent in 17/20**, covered only in C15; n.a. in C07 and C12. The consistency criterion for Needed is that the skill's main input is routinely written by others **and** it draws a security conclusion or changes code from it. Thus absent does not automatically mean Needed. Map source: OWASP Top 10 for LLM Applications 2025, **LLM01:2025 Prompt Injection**, and Top 10 for Agentic Applications 2026, **ASI01 – Agent Goal Hijack** ([LLM source](https://genai.owasp.org/llm-top-10/), [agentic source](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)).
- **Sensitive agent inputs/outputs — `agent.sensitive-data`: 11 absent + 6 shallow = 17/20**; one covered, two n.a. Application privacy/logging advice is not automatically a rule for the agent's own snippets, prompts or reports. Map source: OWASP **LLM02:2025 Sensitive Information Disclosure** ([source](https://genai.owasp.org/llm-top-10/)); NIST AI 600-1 **2.4 Data Privacy / 2.9 Information Security** ([source](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)).
- **Authority bounds — `agent.limit-agency`: 1 absent + 14 shallow = 15/20**; three covered, two n.a. Approval and stop conditions often provide real but incomplete limits on tool privileges, workspace ownership or publication. Map source: OWASP **LLM06:2025 Excessive Agency** ([source](https://genai.owasp.org/llm-top-10/)); agentic **ASI02 – Tool Misuse / ASI03 – Identity & Privilege Abuse** ([source](https://genai.owasp.org/2025/12/09/owasp-top-10-for-agentic-applications-the-benchmark-for-agentic-security-in-the-age-of-autonomous-ai/)).
- **Test environment/data — `testing.environment-and-data`: 1 absent + 7 shallow = 8/20**; two covered, ten n.a. This pattern concerns reproducible platforms and resettable/representative data, not an obligation for writing-only or review-only skills to run tests. Map source: O*NET 31.0 **tasks 14656 and 14655** ([source](https://www.onetcenter.org/database.html)); DORA **Test data management** ([source](https://dora.dev/capabilities/)).

All map-source names and locators above came from `blindspot.py sources --map software <node>`. They supply named practices/risk categories, not experimental proof of these findings.

## Pinned snapshots for the 15 new audits

| Repository | Commit |
|---|---|
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | `8c99fa36d90068c82d547f7c12a9d67a3e95f4ee` |
| [anthropics/skills](https://github.com/anthropics/skills) | `e4bb5d960d87126ff3b3a8af1a104b7db67560ba` |
| [getsentry/skills](https://github.com/getsentry/skills) | `a582c51ee29d0f35e6ac321340796f77d43da733` |
| [mattpocock/skills](https://github.com/mattpocock/skills) | `5863806dd4e15c63174bee4e7515a4256792ecfa` |
| [obra/superpowers](https://github.com/obra/superpowers) | `22f0b463e7a5e579904dd6211a520321035526f7` |
| [openai/skills](https://github.com/openai/skills) | `49f948faa9258a0c61caceaf225e179651397431` |
| [trailofbits/skills](https://github.com/trailofbits/skills) | `149d7b21f4067765b82e67029730b42d228ef4b4` |

The earlier five reports did not record commit SHAs. Their links preserve that limitation rather than implying that the new snapshot dates apply retrospectively.

## Calibration and other limits

- **Uneven band calibration:** code-5 had 8 Needed in five skills; the new batch has 5 in 15, four after re-check. C02–C16 were written before a mid-batch instruction to apply band criteria in both directions; C18–C20 followed it. The C14/C16 consistency notes are evidence of drift. The rates cannot establish that the new skills have fewer serious gaps.
- **One audit run per skill; model re-check, not a person.** Devin in the lead session made one separate pass over the Needed findings, reading skill folders, called skills and code and grepping folder plus root. Worth considering and Minor findings were not systematically rerated beyond the two stated consistency observations.
- **Static evidence only:** audited code and commands were searched/read, not run. External documents linked by the audited skills were not fetched as workflow coverage; local guides and explicit instructions form the coverage evidence. A limited live CLI-contract lookup during C19 analysis was used to reject a suspected helper exit-code issue, not to establish workflow coverage or a runtime finding.
- **Incomplete implementation inspection:** report-specific limits still apply, including unavailable optional helpers and C15's non-exhaustive review of downstream proof/presentation implementations. A stated workflow obligation is not proof of runtime enforcement.
- **Map limits remain:** the earlier code-5 observation about missing step-level debugging, refactoring and release-rollback methods still applies. Nearby map nodes for initial diagnosis, defect repair, version-control reverts or deployment do not supply a complete method for those workflows.
- **No validation reversal:** these are additional source-backed domain-coverage audits, not a controlled comparison with a plain missing-items prompt. Nothing here changes [docs/validation.md](../docs/validation.md), its result, or the earlier code-5 findings. The new aggregate counts combine reports with different scopes and audit-era calibration; the separate re-check explains band differences rather than rewriting the original reports.

If a finding about your skill is wrong, please open an issue.
