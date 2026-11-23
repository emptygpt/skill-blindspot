# Blindspot report: baoyu-format-markdown

Skill under audit: [baoyu-format-markdown](https://github.com/JimLiu/baoyu-skills/tree/bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c/skills/baoyu-format-markdown).

Map: writing 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Takes supplied prose, plans a formatting pass, prepares article metadata, and returns Markdown plus a change summary.
- The body is not rewritten; some routes only apply typography.
- Commissioning, original reporting, hosting, publication and follow-up are out of scope.

## Step 2 list (before opening the map nodes)

- The workflow guards the author's wording but does not identify a final source-to-output check for dropped meanings or Markdown breakage (looked at completion, typography and preservation).

## Findings

### Needed

None.

### Worth considering

1. **Verify the formatted output against the input** [model+map+trace]
   Map nodes: `edit.copyedit`, `edit.proofread-method`, `comp.ai-accuracy`, `fact.not-misleading`.
   Source: [BBC Editorial Guidelines 2025](https://www.bbc.co.uk/editorialguidelines/guidelines) — Avoiding Misleading Audiences.
   Source: [O*NET 30.0 Database, task statements for writing-related occupations (27-3043.00, 27-3043.05, 27-3041.00, 27-3042.00, 27-3023.00, 27-3031.00)](https://www.onetcenter.org/database.html) — 27-3041.00 task: Read copy or proof to detect and correct errors in spelling, punctuation, and syntax..
   Source: [Purdue OWL: Proofreading](https://owl.purdue.edu/owl/general_writing/the_writing_process/proofreading/index.html) — General Strategies Before You Proofread.

   Source: [BBC Editorial Guidelines 2025 (section index and Section 3: Accuracy, Guidelines)](https://www.bbc.co.uk/editorialguidelines/guidelines) — Use of Automated Technology and Artificial Intelligence.
   Why: The change report follows formatting, but the agent does not reread the generated metadata and Markdown side by side with the source to catch altered qualifiers or broken blocks.
   Fix: After typography, check the diff for unintended changes, review rendered structure, and confirm title and summary claims against the source.

### Minor

1. **Make the SEO handoff explicit when requested** [map]
   Map nodes: `head.metadata-seo`.
   Source: [ESCO classification, skills of journalist, blogger, advertising copywriter, newspaper editor, web content manager, writer and technical communicator](https://esco.ec.europa.eu) — keywords in digital content.
   Why: The generated slug and previews cover part of discoverability, but SKILL.md:151–163 does not ask about the actual search wording or destination.
   Fix: When search metadata is requested, check it against the publication's audience and constraints; otherwise describe the fields as previews.

## Unsourced findings

None.

## Evidence limitations

Read the bundled title reference and relevant helper code as evidence. No user preferences or article were supplied; preference files and sample article names are inputs, not missing bundled dependencies. No target code was executed.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Read and choose mode | Input and edit mode | Plan or direct typography | SKILL.md:63–89 branches by input and user choice. |
| Plan and package | Formatting plan and metadata | Body edit and save | SKILL.md:91–185 binds body formatting to the plan. |
| Save and run typography | Markdown artifact | Completion message | SKILL.md:187–244 has no final source comparison. |


## Map table

| Node | State | Evidence |
|---|---|---|
| topic.* | not-applicable | The input is an existing article; no commissioning, first draft or research. |
| audience.* | not-applicable | The input is an existing article; no commissioning, first draft or research. |
| research.* | not-applicable | The input is an existing article; no commissioning, first draft or research. |
| structure.outline | covered | SKILL.md:93–109 — the formatting plan identifies the argument and proposes section boundaries. |
| structure.main-point | covered | SKILL.md:93–109 — the formatting plan identifies the argument and proposes section boundaries. |
| structure.select-material | not-applicable | No substantive cut, rewrite, editorial round or cross-piece edit. |
| structure.length-format | not-applicable | No substantive cut, rewrite, editorial round or cross-piece edit. |
| structure.context | not-applicable | No substantive cut, rewrite, editorial round or cross-piece edit. |
| drafting.* | not-applicable | The input is an existing article; no commissioning, first draft or research. |
| revise.rewrite | not-applicable | No substantive cut, rewrite, editorial round or cross-piece edit. |
| revise.requirements | not-applicable | No substantive cut, rewrite, editorial round or cross-piece edit. |
| revise.feedback | not-applicable | No substantive cut, rewrite, editorial round or cross-piece edit. |
| revise.structure-cohesion | covered | SKILL.md:165–185 — the formatting pass turns the plan into hierarchy, lists and tables. |
| revise.consistency | not-applicable | No substantive cut, rewrite, editorial round or cross-piece edit. |
| fact.verify | not-applicable | Underlying reporting and sourcing are outside the formatting job. |
| fact.statistics | not-applicable | Underlying reporting and sourcing are outside the formatting job. |
| fact.corroborate | not-applicable | Underlying reporting and sourcing are outside the formatting job. |
| fact.authenticity | not-applicable | Underlying reporting and sourcing are outside the formatting job. |
| fact.rumour | not-applicable | Underlying reporting and sourcing are outside the formatting job. |
| fact.cite-sources | not-applicable | Underlying reporting and sourcing are outside the formatting job. |
| fact.right-of-reply | not-applicable | Underlying reporting and sourcing are outside the formatting job. |
| fact.not-misleading | shallow | SKILL.md:169–185 — guards the source wording but does not check whether new emphasis or headings change the overall impression. |
| fact.expert-review | not-applicable | Underlying reporting and sourcing are outside the formatting job. |
| edit.copyedit | shallow | SKILL.md:108–112,183,197–212 — fixes and automation are described, but no final reading pass. |
| edit.proofread-method | shallow | SKILL.md:108–112,183,197–212 — fixes and automation are described, but no final reading pass. |
| edit.second-reader | not-applicable | No external editorial approval, publisher style guide or author entry is part of this job. |
| edit.style-standards | not-applicable | No external editorial approval, publisher style guide or author entry is part of this job. |
| head.headline | covered | SKILL.md:127–149; references/title-formulas.md:36–49 — candidates are grounded in the supplied text, with truthful direct options. |
| head.metadata-seo | shallow | SKILL.md:119–125,151–163 — slug and descriptive metadata; no search-term check. |
| head.byline | not-applicable | No external editorial approval, publisher style guide or author entry is part of this job. |
| visual.select | not-applicable | Existing cover may be carried forward; no image sourcing, generation or editing. |
| visual.captions | not-applicable | Existing cover may be carried forward; no image sourcing, generation or editing. |
| visual.edit-integrity | not-applicable | Existing cover may be carried forward; no image sourcing, generation or editing. |
| visual.layout | covered | SKILL.md:165–185 — the formatting pass turns the plan into hierarchy, lists and tables. |
| rights.* | not-applicable | No rights transaction, upload, release or published feedback. |
| publishing.* | not-applicable | No rights transaction, upload, release or published feedback. |
| feedback.* | not-applicable | No rights transaction, upload, release or published feedback. |
| comp.minimize-harm | not-applicable | Not a reporting or release step; no named channel or publication policy. |
| comp.privacy | not-applicable | Not a reporting or release step; no named channel or publication policy. |
| comp.vulnerable-subjects | not-applicable | Not a reporting or release step; no named channel or publication policy. |
| comp.conflicts | not-applicable | Not a reporting or release step; no named channel or publication policy. |
| comp.sponsored-disclosure | not-applicable | Not a reporting or release step; no named channel or publication policy. |
| comp.stereotypes | not-applicable | Not a reporting or release step; no named channel or publication policy. |
| comp.law | not-applicable | Not a reporting or release step; no named channel or publication policy. |
| comp.ai-disclosure | not-applicable | Not a reporting or release step; no named channel or publication policy. |
| comp.ai-accuracy | shallow | SKILL.md:160–163 — requires concrete text-based summaries but has no verification pass against the input. |
| comp.honest-authorship | covered | SKILL.md:169–177 — do not supply new statements or rewrite the author's claims. |

counts: covered 6, shallow 5, absent 0, not-applicable 67, undetermined 0


## Excluded by profile

None.
