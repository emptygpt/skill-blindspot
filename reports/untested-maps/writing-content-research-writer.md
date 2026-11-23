# Blindspot report: content-research-writer

Skill under audit: [ComposioHQ: content-research-writer](https://github.com/ComposioHQ/awesome-claude-skills/tree/044d48b594f060c164f3b20fac9ea01374721bca/content-research-writer).

Map: writing 0.1.0    Profile: none    Date: 2026-11-23

## Scope

- Starts from a topic or an existing draft. This audit follows the online nonfiction article workflow, not the tutorial workflow.
- The agent helps plan the article, research factual material, and review successive drafts; the writer retains control over revisions.
- Ends at a draft and final editorial feedback. It does not acquire images, release the article, or operate a publication.

## Step 2 list (before opening the map nodes)

- Research advice mentions verifying sources, but neither the citation formats nor the final checklist makes the reviewer check that each source supports the exact final wording.
- The hook step offers data-led openings, but its audience and curiosity checks do not include checking whether a statistic in a proposed opening is still accurate after the rewrite.
- The review identifies grammar and consistency problems but does not require one last read of the modified text after the writer applies the suggestions.

## Findings

### Needed

None.

### Worth considering

1. **Tie consequential claims to checked sources in the final draft** [model+map+trace]
   Map nodes: `research.online-third-party`, `fact.verify`, `fact.statistics`, `fact.corroborate`, `fact.authenticity`, `fact.rumour`, `fact.cite-sources`, `fact.not-misleading`, `comp.ai-accuracy`.
   Sources: [BBC Editorial Guidelines 2025](https://www.bbc.co.uk/editorialguidelines/guidelines) — Accuracy: online and third-party material, corroboration, validating documentary evidence, fact and rumour, Reporting Statistics and Risk, Avoiding Misleading Audiences, and Use of Automated Technology and Artificial Intelligence; [O*NET 30.0](https://www.onetcenter.org/database.html) — 27-3041.00, verification of facts, dates and statistics; [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/) — access to relevant source material.
   Why: SKILL.md:144–147,325,339–345,511–515 calls for credible sources, checks citation completeness and encourages original links. These checks do not establish that the final wording or a suggested hook is supported by the source. The workflow also does not prescribe an independent check when an important claim depends on questionable material.
   Fix: At final review, follow each consequential claim back to its original evidence, record where any figure came from and what it measures, corroborate contested claims where practicable, and qualify or remove claims that cannot be verified.

2. **Carry the audience and content brief through the final review** [map+trace]
   Map nodes: `topic.ideas`, `topic.subject-form`, `topic.brief`, `topic.people-first`, `audience.research`, `draft.complete-coverage`, `revise.requirements`.
   Sources: [O*NET 30.0](https://www.onetcenter.org/database.html) — 27-3041.00, story ideas and audience appeal; 27-3043.05, choosing a suitable form; 27-3043.00, discussing changes to the brief and revising to meet requirements; [Purdue OWL: Prewriting](https://owl.purdue.edu/owl/general_writing/the_writing_process/prewriting/index.html) — talking to the audience; [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — originality and completeness of people-first content.
   Why: SKILL.md:79–89,134–138,296–345,474–480 collects requirements and refines the outline. It does not compare possible angles for the reader, check them with actual readers when assumptions matter, or check that the final draft meets the agreed brief and answers the reader's main questions.
   Fix: Keep a short brief of audience, angle, purpose, form and length; use it to assess candidate angles and check that the final draft fulfils its intended promise.

3. **Distinguish the writer's interpretation and check reuse of third-party material** [map]
   Map nodes: `draft.opinion-labelled`, `rights.permissions`, `rights.attribution`.
   Sources: [SPJ Code of Ethics](https://www.spj.org/spj-code-of-ethics/) — labelling opinion and avoiding plagiarism; [O*NET 30.0](https://www.onetcenter.org/database.html) — 27-3041.00, arranging copyright permissions; [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — adding value beyond rewording sources.
   Why: SKILL.md:144–147,264–294,474–480 supports quoting, attribution and an author viewpoint. A reference list does not make it clear which conclusions are the author's or whether material selected for reuse requires permission.
   Fix: During draft review, distinguish factual claims from interpretation and flag retained third-party material that needs permission or a shorter excerpt.

### Minor

1. **Proofread the version the writer will actually use** [model+map+trace]
   Map nodes: `edit.copyedit`, `edit.proofread-method`.
   Sources: [O*NET 30.0](https://www.onetcenter.org/database.html) — 27-3041.00, reading copy or proof to detect and correct errors; [Purdue OWL: Proofreading](https://owl.purdue.edu/owl/general_writing/the_writing_process/proofreading/index.html) — General Strategies Before You Proofread.
   Why: SKILL.md:323,345,488 assesses mechanics, lists typos and suggests a read-aloud pass. It does not have a separate review of the text after the writer applies edits.

2. **Check the proposed headline against the article** [map]
   Map node: `head.headline`.
   Source: [Google Search Central](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — descriptive, non-exaggerated page titles.
   Why: SKILL.md:337 invites title options without checking that they describe the finished draft without overstating its findings.

## Unsourced findings

None.

## Evidence limitations

The pinned skill contains one file. The draft and research files named in it are files for the writer to create or illustrative names, not unavailable instruction dependencies. No article or research assignment was supplied; the audit evaluates instructions, not the factual accuracy of demonstration articles. No target skill or example was executed.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Establish the brief and develop the outline | Reader, purpose, section plan and research tasks | Research and drafting | SKILL.md:134–138 revisits the outline, but the final review does not reconcile it with the brief. |
| Research and propose an opening | Notes, citations and hook alternatives | Writer's draft | SKILL.md:196–200 checks hook fit, not factual support for the proposed wording. |
| Review sections and preserve voice | Local edits and writer choices | Revised draft | SKILL.md:214–246,249–262 reviews individual edits and tone. |
| Review and polish the whole draft | Editorial feedback, title options and readiness checklist | Writer's final revisions | SKILL.md:296–345 checks evidence sufficiency and citation presence without tracing final wording to the source. |

## Map table

| Node | State | Evidence |
|---|---|---|
| topic.ideas | shallow | SKILL.md:475 — "Brainstorm unique angle"; no comparison of candidate angles for reader appeal. |
| topic.purpose | covered | SKILL.md:85 — "What's your goal?"; prompts for the purpose before outlining. |
| topic.subject-form | shallow | SKILL.md:82–84 — "desired length/format"; asks what the writer wants but does not help decide which form suits an undecided topic. |
| topic.news-judgement | not-applicable | The assessed workflow is not a news assignment. |
| topic.brief | shallow | SKILL.md:135 — "Adjust based on feedback"; iterates with the writer but does not record an agreed brief and changes. |
| topic.people-first | shallow | SKILL.md:475 — "Brainstorm unique angle"; no check that the angle supplies substantive new value to readers. |
| topic.plan-schedule | not-applicable | No commissioning or publication calendar; personal draft deadlines are optional. |
| audience.define | covered | SKILL.md:83,200 — "target audience"; asks who will read it, then checks the proposed hook against that audience. |
| audience.tone-medium | covered | SKILL.md:253–262 — "Match tone"; uses samples and writer feedback to find a suitable register. |
| audience.research | absent | No reader conversations or audience data before the outline. |
| research.background | covered | SKILL.md:128–147 — "Extract key facts"; research tasks derive from missing material in the outline. |
| research.consult-sources | covered | SKILL.md:512–515 — "Link to original sources"; checks sources before citation and favours first-hand records. |
| research.interviews | not-applicable | The workflow gathers existing published material, not new interviews. |
| research.source-network | not-applicable | No ongoing reporter contact network. |
| research.online-third-party | shallow | SKILL.md:145 — "Find credible sources"; no check of site ownership, incentives or provenance. |
| research.notes | covered | SKILL.md:486–487,499 — "Save research separately"; maintains research and citations separately from successive drafts. |
| research.anonymous-sources | not-applicable | No sourcing from confidential informants. |
| research.technical-subject | not-applicable | The separate tutorial workflow is outside this article audit. |
| structure.outline | covered | SKILL.md:94–138 — "Identify research gaps"; gives the writer a section plan with evidence tasks before drafting. |
| structure.main-point | covered | SKILL.md:82,477 — "Develop your thesis"; establishes the central argument. |
| structure.select-material | covered | SKILL.md:217–226 — "Suggested reordering"; checks whether a point belongs where it appears and whether it needs better evidence. |
| structure.length-format | covered | SKILL.md:84,459–464 — "Quick outline (shorter format)"; collects the length and form and adapts the plan to a shorter article format. |
| structure.context | covered | SKILL.md:100–103,118–121 — "Context and background"; puts necessary background in the introduction and makes room for counterarguments. |
| draft.first-draft | covered | SKILL.md:451–457 — "Write body sections"; guides the writer through introduction, reviewed body and conclusion after the outline. |
| draft.complete-coverage | shallow | SKILL.md:317–320 — "Evidence sufficiency"; reviews support but does not check for omitted questions from the reader or outline. |
| draft.first-hand | not-applicable | No testing, visits or first-person reporting are required by this workflow. |
| draft.opinion-labelled | shallow | SKILL.md:478–479 — "Write with strong POV"; encourages a supported viewpoint without separating interpretation from fact for the reader. |
| draft.blog-commentary | covered | SKILL.md:451–457 — "Blog Post Workflow"; gives a dedicated sequence for a blog draft and incremental feedback. |
| draft.press-release | not-applicable | No promotional release is commissioned. |
| revise.rewrite | covered | SKILL.md:216–240 — "Specific Line Edits"; offers rewrites and explains each choice. |
| revise.requirements | shallow | SKILL.md:84 — "desired length/format"; final review does not check this against the completed draft. |
| revise.feedback | covered | SKILL.md:202–246,253–257 — "Respect choices"; the agent offers feedback and the writer decides what to change. |
| revise.structure-cohesion | covered | SKILL.md:312–315 — "Transition quality"; checks structure, pace and how sections connect. |
| revise.consistency | not-applicable | One author and article; no consistency check across a series. |
| fact.verify | shallow | SKILL.md:512 — "Verify sources before citing"; verifies sources, but does not instruct the final reviewer to check facts against them. |
| fact.statistics | shallow | SKILL.md:513 — "Use recent data"; recency is addressed, but figure validation and method are not. |
| fact.corroborate | absent | Balancing views does not require independently checking the same claim. |
| fact.authenticity | absent | No procedure for authenticating the underlying documentary evidence. |
| fact.rumour | shallow | SKILL.md:225,340 — "All claims sourced"; calls for support without distinguishing allegations or provisional claims from established fact. |
| fact.cite-sources | shallow | SKILL.md:512–515 — "Link to original sources"; provides traceable references but no clear treatment for claims it cannot verify. |
| fact.right-of-reply | not-applicable | Does not investigate or approach subjects criticised in a piece. |
| fact.not-misleading | shallow | SKILL.md:196–200,317–320 — "Evidence sufficiency"; checks support but not lost qualifiers or overstatement in the delivered copy. |
| fact.expert-review | not-applicable | Provides writer-facing feedback without coordinating external expert review. |
| edit.copyedit | shallow | SKILL.md:323 — "Grammar and mechanics"; assesses them, but the checklist does not recheck the corrected copy. |
| edit.proofread-method | shallow | SKILL.md:488 — "Read aloud"; a general tip, not a defined check of the final text. |
| edit.second-reader | not-applicable | No second human reviewer or approval handoff. |
| edit.style-standards | not-applicable | Matches the writer's voice, not a separate publisher style guide. |
| head.headline | shallow | SKILL.md:337 — "Options if needed"; suggests titles without checking whether they accurately summarise the finished piece. |
| head.metadata-seo | not-applicable | No discoverability or metadata deliverable. |
| head.byline | not-applicable | No publisher-facing byline metadata. |
| visuals.* | not-applicable | Text-only outline and review, not layout or artwork for publication. |
| rights.permissions | absent | The research step can select third-party quotations, but no instruction checks whether selected material requires permission. |
| rights.attribution | shallow | SKILL.md:287 — "running citations list"; credits sources, but does not check the draft for over-reliance on source wording. |
| rights.own-copyright | not-applicable | No registration or rights administration. |
| rights.commission-terms | not-applicable | No negotiation with a commissioner or publisher. |
| publishing.* | not-applicable | A readiness check is not publication. |
| feedback.* | not-applicable | Scope ends before publication. |
| comp.minimize-harm | not-applicable | Not an investigative assignment deciding whether to identify subjects. |
| comp.privacy | not-applicable | Does not collect unpublished personal information. |
| comp.vulnerable-subjects | not-applicable | No reporting on vulnerable subjects is assigned. |
| comp.conflicts | not-applicable | No commissioned or sponsored reporting. |
| comp.sponsored-disclosure | not-applicable | No paid or gifted relationship in the assessed workflow. |
| comp.stereotypes | not-applicable | No reporting on groups or people is required by the assessed case. |
| comp.law | not-applicable | No legal or release review is assigned; reuse permissions are tracked separately. |
| comp.ai-disclosure | not-applicable | No named destination or content disclosure requirement; the writer retains publication control. |
| comp.ai-accuracy | shallow | SKILL.md:144–147,340 — "All claims sourced"; applies a generic sourcing check to AI-assisted prose without validating AI-suggested claims against the cited material. |
| comp.honest-authorship | not-applicable | Does not create bylines, author bios or credentials. |

counts: covered 16, shallow 18, absent 4, not-applicable 40, undetermined 0

## Excluded by profile

None.
