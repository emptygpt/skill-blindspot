# Blindspot report: doc-coauthoring

Skill under audit: [doc-coauthoring](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/doc-coauthoring).

Map: tech-docs 0.1.0    Profile: none    Date: 2026-11-23

## Scope

- Audits the technical design/specification use of the collaborative drafting workflow, including intake, iterative section editing, independent reader review and final handoff.
- Ends at a reviewed shared document, artifact or Markdown file. It does not implement the design or build and publish a documentation site.
- Generic proposals are not scored separately; an API reference, README or runnable tutorial is not a required deliverable.

## Step 2 list (before opening the map nodes)

- Check important technical claims against primary evidence: the reader test works from the document alone, and final review suggests fact checks without prescribing how to verify claims.
- Make a final accessibility pass: intake checks image alternatives in an existing shared document, but the drafting and final review steps do not revisit newly added images or heading structure.

## Findings

### Needed

None.

### Worth considering

1. **Verify important technical claims against a primary source before handoff** [model+map+trace]
   Map nodes: `doc-review.technical`, `doc-review.ai-generated`, `doc-review.qa`.
   Source: [GitLab, Contribute to the GitLab documentation](https://docs.gitlab.com/development/documentation/) — Workflows: Developer responsibilities; Workflows: AI-generated documentation.
   Source: [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) — Final publishing review.
   Why: Reader testing reveals what a reader can infer, but the fresh reader gets no independent technical evidence. Final review recommends checking details without requiring that a feature owner verify high-impact claims, resolve discrepancies and confirm the result.
   Fix: In Final Review, separate comprehension from accuracy: have a technical owner check the spec's consequential claims and links against agreed requirements, code or other primary evidence before marking it ready.
2. **Check navigation and accessibility on the final draft, not just during intake** [model+map+trace]
   Map nodes: `page-structure.headings`, `page-structure.links`, `images-media.alt-text`, `doc-accessibility.structure`.
   Source: [Google developer documentation style guide](https://developers.google.com/style) — Headings and titles; Cross-references and linking: Write descriptive link text; Diagrams, figures, and other images: Alt text; Write accessible documentation.
   Source: [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — 1.1.1 Non-text Content; 1.3.1 Info and Relationships; 2.4.4 Link Purpose (In Context); 2.4.6 Headings and Labels.
   Why: The scaffold supplies section headings, and intake covers missing image alternatives in a shared document. The final review is not explicit about heading hierarchy, semantic markup, descriptive link labels or image alternatives added or changed while drafting.
   Fix: Before handoff, check the final structure, link labels and text alternatives for every informative figure.

### Minor

1. **Turn template and editing preferences into a short style check** [map]
   Map nodes: `writing-style.guide`, `writing-style.voice`, `writing-style.terminology`, `writing-style.global`, `writing-style.inclusive`, `writing-style.code-font`, `writing-style.dates`, `doc-accessibility.reading`, `doc-review.edit`.
   Source: [Google developer documentation style guide](https://developers.google.com/style) — Highlights (voice and dates); Write for a global audience; Write inclusive documentation; Code in text; Write accessible documentation: Ease of reading.
   Source: [O*NET: Technical Writers](https://www.onetonline.org/link/details/27-3042.00) — editing and standardizing material prepared by other writers.
   Why: The co-author learns the user's preferences and trims filler, but the workflow does not establish a baseline for technical terms, voice, inclusive and plain language, formatting or dates across sections.
   Fix: Agree on a style guide at intake and use it when reviewing the whole document.
2. **Keep shared sources and decisions traceable** [map]
   Map nodes: `doc-planning.single-source`, `doc-review.plagiarism`, `doc-review.records`.
   Source: [GitLab, Contribute to the GitLab documentation](https://docs.gitlab.com/development/documentation/) — Documentation Style Guide: Documentation is the single source of truth (SSoT); Documentation Style Guide: Plagiarism.
   Source: [O*NET: Technical Writers](https://www.onetonline.org/link/details/27-3042.00) — maintaining records and files of work and revisions.
   Why: Intake gathers related documents and curation asks for reasons, but the final handoff only optionally links the conversation. It does not distinguish primary references from duplicated material or preserve the reasons that guided major edits.
   Fix: Link primary sources rather than reproduce them, attribute any approved reuse, and keep a short decision record with the deliverable.
3. **Make the drafting handoff explicit** [map]
   Map node: `doc-planning.project`.
   Source: [ESCO classification, skills of technical communicator and ICT documentation manager](https://esco.ec.europa.eu) — manage content development projects.
   Why: The workflow has review stages and an owner, and it collects schedule constraints. It does not turn them into agreed checkpoints or distinguish technical sign-off from drafting feedback.
   Fix: For a multi-reviewer spec, agree who approves the result and by when before drafting starts.

## Unsourced findings

None.

## Evidence limitations

Static review of the pinned skill, which has no bundled references or profile. The two Markdown names suggested in the skill are outputs, not missing inputs. No connected documents were accessed and no artifact editing or reader tests were run. API/reference authoring, product release and docs-site maintenance are intentionally outside the selected technical-specification scope.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Gather audience, purpose, constraints and sources | Shared design context | Scaffold and section questions | SKILL.md:88–102 checks readiness by whether questions can focus on trade-offs. |
| Curate and draft each section | A complete draft reflecting the co-author's choices | Whole-document review and independent reader test | SKILL.md:170–240 records selections as edits and checks flow; decisions are not explicitly preserved in the handoff. |
| Test realistic reader questions | Comprehension problems and revisions | Refinement and final review | SKILL.md:255–286,329–331 loops back when the reader reports difficulty. |
| Hand off the document | Reviewed design/specification | Document owner | SKILL.md:333–348 suggests checking facts and links but does not make the results a completion gate. |

## Map table

| Node | State | Evidence |
|---|---|---|
| doc-planning.readers | covered | SKILL.md:36–38 — "Who's the primary audience?" pairs readership with intended impact before drafting. |
| doc-planning.subject | covered | SKILL.md:36–40,154–160 — "what should be included" is settled with the co-author first at document level, then for each section. |
| doc-planning.gather | covered | SKILL.md:56–63,76–97 — "Technical architecture or dependencies" is requested along with related materials; clarification follows intake. |
| doc-planning.topic-types | covered | SKILL.md:36–45,118–128 — "the type of document and template" determines the scaffold for the chosen artifact. |
| doc-planning.single-source | absent | Intake and editing never distinguish canonical references from duplicated content. |
| doc-planning.docs-with-code | not-applicable | The design document is handed off before implementation or release. |
| doc-planning.legal-safety | not-applicable | No product-use instructions or claim of legal or compliance review in this technical-design workflow. |
| doc-planning.project | shallow | SKILL.md:61,338 — "Timeline pressures or constraints" are gathered, but named reviewers and milestones are not agreed. |
| page-structure.order | covered | SKILL.md:118–128,223–236 — "If the document structure is clear" the workflow keeps it; otherwise proposes sections and later checks cross-section flow. |
| page-structure.headings | shallow | SKILL.md:139,148 — "all section headers" establishes a scaffold without rules for labels or hierarchy. |
| page-structure.procedures | not-applicable | A user procedure is not a required spec deliverable. |
| page-structure.step-results | not-applicable | No reader-facing procedures to checkpoint. |
| page-structure.links | shallow | SKILL.md:339,346 — "double-checking any facts, links, or technical details" acknowledges links without checking link purpose or labels. |
| page-structure.readme | not-applicable | No README deliverable. |
| page-structure.repo-links | not-applicable | The Markdown fallback is a standalone file, not a set of repository pages. |
| page-structure.troubleshooting | not-applicable | No operational troubleshooting page. |
| writing-style.guide | shallow | SKILL.md:36–47,202–211 — "a template or specific format" and user preferences inform edits; no explicit style guide. |
| writing-style.voice | absent | No direction on reader address, tense or voice in the deliverable. |
| writing-style.terminology | shallow | SKILL.md:225–231 — "Flow and consistency across sections" prompts a broad pass but not a terminology and abbreviation check. |
| writing-style.global | shallow | SKILL.md:217,225–231 — "Whether every sentence carries weight" checks concision without checking plain language or idioms. |
| writing-style.inclusive | absent | No inclusive-language pass. |
| writing-style.timeless | not-applicable | A design spec can intentionally describe planned work; it is not evergreen product guidance. |
| writing-style.code-font | absent | No conventions for how the spec should format code or identifiers. |
| writing-style.dates | absent | No guidance for formatting dates or numbers. |
| api-reference | not-applicable | A design specification is not an API reference. |
| api-description | not-applicable | No machine-readable API contract is produced. |
| code-samples | not-applicable | No executable examples are required by the specification workflow. |
| images-media.select | not-applicable | Image production and selection are not workflow deliverables. |
| images-media.alt-text | shallow | SKILL.md:49–52 — "Check for images without alt-text" applies at intake for an existing shared doc, not at final review. |
| images-media.captions | not-applicable | Figure creation is not prescribed. |
| images-media.quality | not-applicable | Image production is not prescribed. |
| images-media.video | not-applicable | No recordings or video deliverables. |
| doc-accessibility.reading | shallow | SKILL.md:225–231,273 — "ambiguity, false assumptions, contradictions" catches comprehension problems without checking reading level or plain language. |
| doc-accessibility.structure | shallow | SKILL.md:139–148 — "all section headers" gives sections but no accessibility check for their hierarchy, lists or tables. |
| doc-accessibility.color | not-applicable | No visual or site design deliverable. |
| doc-accessibility.page | not-applicable | No published web page is produced. |
| docs-build | not-applicable | Handoff is a document, not a site, help surface or docs build. |
| doc-review.edit | shallow | SKILL.md:205–219 — "until user is satisfied with the section" drives substantive edits but not review against editorial standards. |
| doc-review.technical | shallow | SKILL.md:336–340 — "double-checking any facts, links, or technical details" is advised, without a technical-owner review or a method. |
| doc-review.qa | shallow | SKILL.md:233–240,329–340 — "overall coherence, flow, completeness" structures QA but no final check confirms factual accuracy, working links and formatting. |
| doc-review.ai-generated | shallow | SKILL.md:338–342 — "they own this document and are responsible for its quality" encourages human review without requiring verification of significant claims before handoff. |
| doc-review.plagiarism | absent | Sourced intake is explicit; attribution and permitted reuse are not. |
| doc-review.records | shallow | SKILL.md:172,346 — "Request brief justifications" captures decisions during curation without requiring a stable record. |
| doc-maintenance.revise | not-applicable | The workflow hands off the current design document, not a maintained product documentation set. |
| doc-maintenance.feedback | not-applicable | Pre-handoff feedback is part of reader review; no post-handoff feedback operation is prescribed. |
| doc-maintenance.remove | not-applicable | No retired feature pages. |
| doc-maintenance.localise | not-applicable | No translated deliverables. |

Domain coverage counts: covered 5, shallow 14, absent 6, not-applicable 50, undetermined 0.

## Excluded by profile

None.
