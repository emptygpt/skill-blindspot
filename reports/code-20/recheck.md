# Re-check of the coding-skill Needed findings

Date: 2026-11-19. Report: [Twenty public coding skills, ranked](../code-20.md). Procedure: [What to publish](../../docs/recheck.md#what-to-publish).

This was **one separate model pass by Devin in the lead session**, not the auditing run and not a person. The reviewer read the skill folders, called skills and code, and ran `blindspot.py grep` on each skill folder and repository root. The tables below publish that pass's verdicts, including a scope-rules re-check of the eight earlier code-5 Needed findings. They are not a claim that the audit-writing run independently repeated the lead's review.

The review applied scope rules 1–5 to each report's declared boundary. **Holds** means the gap and Needed band are fair; **overstated** means a real gap belongs lower; **wrong** would mean the skill covers it. Original audit tables, counts and bands remain unchanged, as required by the re-check procedure.

## New batch: five originally Needed findings

Result: **4 holds / 1 overstated / 0 wrong**. Four of the five originally Needed findings remain Needed.

| Finding | Map node | Verdict | Band after re-check | Scope rule, if applicable | Reason |
|---|---|---|---|---|---|
| [C04-1](C04.md#needed) | testing.test-the-change | holds | Needed | 1 | The description promises functionality verification, but SKILL.md and all three examples lack an assertion or expected-result step. Running browser actions is not checking their outcome. |
| [C18-1](C18.md#needed) | agent.injected-instructions | holds | Needed | 1 | Security conclusions are drawn from code that may be third-party. The missing reviewer-side instruction/data boundary is the same class as C17-1. |
| [C19-1](C19.md#needed) | agent.wrong-output | overstated | Worth considering | —; band criterion, not an excluded stage | Workflow step 2 normally resolves the current branch's PR. A checkout/PR mismatch arises on the optional explicit-PR input; the missing guard does not make the ordinary workflow unreliable without it. |
| [C19-2](C19.md#needed) | agent.injected-instructions | holds | Needed | 1 | Logs produced by PR branches, possibly forks, enter a plan that leads to code edits. They need an evidence-versus-instruction boundary. |
| [C20-1](C20.md#needed) | agent.injected-instructions | holds | Needed | 1 | Repository material is evidence for a security conclusion. This is consistent with C17-1, not a request for a downstream implementation stage. |

## Earlier code-5: eight Needed findings under scope rules 1–5

Result: **8 holds / 0 overstated / 0 wrong**. Those audits predated the explicit scope rules; applying them does not change these eight bands. C12-1 and C12-2 are inside scope by **rule 1** because their stages are promised in the skill description, even though the body omits them.

| Finding | Map node | Verdict | Band after re-check | Scope rule, if applicable | Reason |
|---|---|---|---|---|---|
| [C06-1](../code-5/C06.md#needed) | requirements.understand-request; requirements.technical-spec; version-control.change-description; review.design-and-function | holds | Needed | 1 | A correctness review needs the intended behavior from the description, issue or specification, not only the diff. |
| [C06-2](../code-5/C06.md#needed) | testing.unit-tests; testing.regression-and-negative; testing.test-the-change | holds | Needed | 1 | Reviewing whether changed behavior has adequate tests belongs inside code review; it does not require executing the tests or extending into deployment. |
| [C07-1](../code-5/C07.md#needed) | testing.test-the-change; testing.automation; agent.wrong-output | holds | Needed | 1 | The promised test-first loop needs observed failure for the right reason and observed passing checks, not merely authored tests. |
| [C12-1](../code-5/C12.md#needed) | version-control.integrate-and-merge | holds | Needed | 1; description-promised stage | Conflict resolution/integration is promised but lacks a procedure. It is not outside the boundary merely because the body omits it. |
| [C12-2](../code-5/C12.md#needed) | — (unsourced; no map node assigned in the audit) | holds | Needed | 1; description-promised stage | Splitting a mixed working tree into atomic commits is promised, but examples of good commit logs do not perform that work. |
| [C12-3](../code-5/C12.md#needed) | agent.limit-agency; version-control.revert; agent.human-oversight | holds | Needed | 1 | Destructive reset and publication operations are part of the instructed Git workflow and need preservation/authority guards. |
| [C17-1](../code-5/C17.md#needed) | agent.injected-instructions | holds | Needed | 1 | Security hunters/verifiers read target-controlled text without declaring it non-authoritative for their own task. |
| [C17-2](../code-5/C17.md#needed) | agent.sensitive-data; security.data-protection | holds | Needed | 1 | Searching for target secrets and writing shareable evidence are inside the audit; captured-environment credential rules do not cover discovered target values. |

## Consistency note: two understated audit findings

The criterion used across the batch for injected-instructions **Needed** is: **the skill's main input is routinely written by others AND it draws a security conclusion or changes code from it**. Generic access to external text alone does not meet this criterion.

| Finding | Map node | Audit band | Consistency verdict | Band the re-check would give | Reason |
|---|---|---|---|---|---|
| [C14-4](C14.md#worth-considering) | agent.injected-instructions | Worth considering | understated | Needed | Third-party PR diffs/comments are the main input to a security review. This meets the same criterion as C18-1. |
| [C16-4](C16.md#worth-considering), instruction-boundary part | agent.injected-instructions | Worth considering | understated | Needed | PR comments and CI logs lead to code changes and pushes. This meets the same criterion as C19-2; the separate sensitive-data concern is not being rerated here. |

These two observations are recorded separately from the five originally Needed findings. They are not added to the published **4/1/0** verdict tally or to the summary's **Needed after re-check** column, which counts only originally Needed findings that held. Audit counts remain unchanged. A full rerating that included these two understated findings would give six Needed in the new batch, not four; that is not the five-finding re-check tally.

## Limits

One model pass, not a human validation or runtime test. The new audits C02–C16 preceded a mid-batch instruction to apply band criteria in both directions; C18–C20 followed it. The two consistency observations are evidence of calibration drift, so the lower Needed rate than code-5 should not be read as a measured improvement in the skills. Apart from these two observations, Worth considering and Minor findings were not systematically re-checked.
