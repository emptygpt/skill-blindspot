# Blindspot report: documentation-and-adrs

Skill under audit: [documentation-and-adrs](https://github.com/addyosmani/agent-skills/tree/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/documentation-and-adrs).

Map: tech-docs 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Produces or updates software documentation: ADRs, inline/API guidance, README, change history and agent notes.
- Ends at local technical and prose checks, not site publishing or support operations.
- Does not prescribe building standalone tutorials or planning a docs portal.

## Step 2 list (before opening the map nodes)

- The verification checklist and OpenAPI example give no clear evidence of checking sample/contract agreement against the running API; there is no dedicated accessibility check for local docs (looked at API, check and verification).

## Findings

### Needed

None.

### Worth considering

1. **Define the reader’s task and checkpoint the quick start** [map]

   Map nodes: `doc-planning.readers`, `page-structure.procedures`, `page-structure.step-results`, `writing-style.voice`.
   Source: [ESCO classification, skills of technical communicator and ICT documentation manager](https://esco.ec.europa.eu) — identify ICT user needs.
   Source: [Google developer documentation style guide](https://developers.google.com/style) — Highlights: Use second person; Procedures; Procedures: Steps with goals.
   Why: The README outline gives a sequence but not how a reader knows each stage worked.
   Fix: Name the reader and expected starting state, and add commands’ expected results and recovery cues.
2. **Verify the API contract and its published examples together** [model+map+trace]
   Map nodes: `api-reference.generated-review`, `api-description.source-control`, `api-description.info`, `api-description.examples`, `api-description.security`, `code-samples.scenarios`, `code-samples.intro`, `code-samples.output`, `code-samples.example-values`.
   Source: [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) — Code examples: Create concise examples that exemplify key development tasks.; Code examples: Show expected output; Reference documentation: If you automatically generate reference documentation and comments from the source code, review the quality and appropriateness of the comments..
   Source: [OpenAPI documentation, Best Practices](https://learn.openapis.org/best-practices.html) — Add OpenAPI Descriptions to Source Control.
   Source: [OpenAPI Specification v3.1.1](https://spec.openapis.org/oas/v3.1.1.html) — Example Object; Info Object; Security Scheme Object.
   Source: [Google developer documentation style guide](https://developers.google.com/style) — Code samples: Introductory statements.
   Source: [RFC 2606: Reserved Top Level DNS Names](https://www.rfc-editor.org/rfc/rfc2606.txt) — TLDs for Testing, & Documentation Examples.
   Why: Inline examples and YAML are shown separately; the final checklist checks parameter and return documentation, not drift among the contract, sample and implementation.
   Fix: Keep the contract with source and verify a representative request, response and authentication expectation against the implementation and generated reference.
3. **Add a documentation-specific quality pass** [model+map]
   Map nodes: `doc-accessibility.reading`, `doc-accessibility.structure`, `doc-review.qa`, `docs-build.lint`, `docs-build.docs-as-code`, `writing-style.code-font`.
   Source: [Write the Docs, Software documentation guide and Docs as code](https://www.writethedocs.org/guide/) — Docs as code.
   Source: [Google developer documentation style guide](https://developers.google.com/style) — Code in text; Write accessible documentation; Write accessible documentation: Ease of reading.
   Source: [ESCO classification, skills of technical communicator and ICT documentation manager](https://esco.ec.europa.eu) — conduct content quality assurance.
   Source: [GitLab, Contribute to the GitLab documentation (Documentation Style Guide, Documentation topic types, Workflows, Documentation testing)](https://docs.gitlab.com/development/documentation/) — Documentation testing.
   Why: The general prose review has no explicit check for meaningful headings, code markup, links or rendered reading order.
   Fix: Review docs alongside code changes and run existing docs lint and link checks where available, plus an accessibility and structure review of one rendered page.

### Minor


None.

## Unsourced findings

None.

## Evidence limitations

The paths in the templates are illustrative project files, not bundled dependencies. This audit read the skill and examples as text; no sample commands were run.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Find existing project conventions | Artifact and format choice | Drafting | SKILL.md:36–44 handles conflicts before using defaults. |
| Draft local documentation | README, ADR, reference or changelog | Technical and prose review | SKILL.md:264–266 checks details and command examples. |
| Check drift and deliver | Reviewed documentation | Project handoff | SKILL.md:268–283,308–320 leaves contract/example agreement implicit. |

## Map table

| Node | State | Evidence |
|---|---|---|
| doc-planning.readers | shallow | SKILL.md:262–266 — names readers during review but does not identify their tasks or knowledge before drafting. |
| doc-planning.subject | covered | SKILL.md:23–48,264–266 — selects artifact by purpose and checks current project conventions and sources. |
| doc-planning.gather | covered | SKILL.md:23–48,264–266 — selects artifact by purpose and checks current project conventions and sources. |
| doc-planning.topic-types | covered | SKILL.md:23–48,264–266 — selects artifact by purpose and checks current project conventions and sources. |
| doc-planning.single-source | not-applicable | Local artifact guidance, not a docs platform, rights review or independent documentation program. |
| doc-planning.docs-with-code | covered | SKILL.md:157–175,268–283 — inline docs live with implementation; compare code and document history. |
| doc-planning.legal-safety | not-applicable | Local artifact guidance, not a docs platform, rights review or independent documentation program. |
| doc-planning.project | not-applicable | Local artifact guidance, not a docs platform, rights review or independent documentation program. |
| page-structure.order | covered | SKILL.md:36–48,201–230 — follow established structure; README includes setup, commands and links to decisions. |
| page-structure.headings | covered | SKILL.md:36–48,201–230 — follow established structure; README includes setup, commands and links to decisions. |
| page-structure.procedures | shallow | SKILL.md:210–214 — ordered quick-start commands without expected results or recovery checks. |
| page-structure.step-results | shallow | SKILL.md:210–214 — ordered quick-start commands without expected results or recovery checks. |
| page-structure.links | not-applicable | No standalone web-page linking workflow; README repository links are accounted for separately. |
| page-structure.readme | covered | SKILL.md:36–48,201–230 — follow established structure; README includes setup, commands and links to decisions. |
| page-structure.repo-links | covered | SKILL.md:36–48,201–230 — follow established structure; README includes setup, commands and links to decisions. |
| page-structure.troubleshooting | covered | SKILL.md:138–150,315 — document observable pitfalls near relevant code. |
| writing-style.guide | covered | SKILL.md:36–44,260–266 — follow conventions and preserve established technical words and source facts. |
| writing-style.voice | shallow | SKILL.md:260–266 — trims promotional and repetitive prose without covering viewpoint and direct instructions. |
| writing-style.terminology | covered | SKILL.md:36–44,260–266 — follow conventions and preserve established technical words and source facts. |
| writing-style.global | not-applicable | The narrowly specified local technical artifacts do not promise localization, inclusive-language review, or date-specific authoring. |
| writing-style.inclusive | not-applicable | The narrowly specified local technical artifacts do not promise localization, inclusive-language review, or date-specific authoring. |
| writing-style.timeless | not-applicable | The narrowly specified local technical artifacts do not promise localization, inclusive-language review, or date-specific authoring. |
| writing-style.code-font | absent | No rule distinguishes inline code identifiers from prose. |
| writing-style.dates | not-applicable | The narrowly specified local technical artifacts do not promise localization, inclusive-language review, or date-specific authoring. |
| api-reference.reference-comments | covered | SKILL.md:138–175,308–315 — inline rationale and API parameters, return types, errors and links to related rationale. |
| api-reference.method-details | covered | SKILL.md:138–175,308–315 — inline rationale and API parameters, return types, errors and links to related rationale. |
| api-reference.docstrings | not-applicable | No Python docstrings, generated page titles, deprecation project or standalone guide is promised. |
| api-reference.reference-titles | not-applicable | No Python docstrings, generated page titles, deprecation project or standalone guide is promised. |
| api-reference.generated-review | shallow | SKILL.md:157–199,308–315 — supplies inline annotations and a contract example, but checks coverage rather than generated render or contract agreement. |
| api-reference.deprecations | not-applicable | No Python docstrings, generated page titles, deprecation project or standalone guide is promised. |
| api-reference.cross-references | covered | SKILL.md:138–175,308–315 — inline rationale and API parameters, return types, errors and links to related rationale. |
| api-reference.guides | not-applicable | No Python docstrings, generated page titles, deprecation project or standalone guide is promised. |
| api-description.design-first | not-applicable | Not designing an API, publishing a catalog or organizing a large contract. |
| api-description.source-control | absent | The contract example has no instruction to keep the spec under version control with related code. |
| api-description.publish | not-applicable | Not designing an API, publishing a catalog or organizing a large contract. |
| api-description.info | shallow | SKILL.md:155–199 — inline example mentions authentication and shows one call; OpenAPI fragment does not model global metadata, concrete payloads or authentication requirements. |
| api-description.operations | covered | SKILL.md:177–199 — attaches contract keys to an HTTP operation and documents model and response cases. |
| api-description.inputs | covered | SKILL.md:177–199 — attaches contract keys to an HTTP operation and documents model and response cases. |
| api-description.responses | covered | SKILL.md:177–199 — attaches contract keys to an HTTP operation and documents model and response cases. |
| api-description.examples | shallow | SKILL.md:155–199 — inline example mentions authentication and shows one call; OpenAPI fragment does not model global metadata, concrete payloads or authentication requirements. |
| api-description.security | shallow | SKILL.md:155–199 — inline example mentions authentication and shows one call; OpenAPI fragment does not model global metadata, concrete payloads or authentication requirements. |
| api-description.large | not-applicable | Not designing an API, publishing a catalog or organizing a large contract. |
| code-samples.scenarios | shallow | SKILL.md:157–174,203–230 — a useful task call and quick start, not a method for contextual and verified example sets. |
| code-samples.intro | shallow | SKILL.md:157–174,203–230 — a useful task call and quick start, not a method for contextual and verified example sets. |
| code-samples.copy-run | covered | SKILL.md:168–172,210–222,264–266 — use concrete examples and check that documented code and commands work. |
| code-samples.output | shallow | SKILL.md:157–174,203–230 — a useful task call and quick start, not a method for contextual and verified example sets. |
| code-samples.style | not-applicable | No dedicated multi-language example library or placeholder-based examples. |
| code-samples.placeholders | not-applicable | No dedicated multi-language example library or placeholder-based examples. |
| code-samples.example-values | shallow | SKILL.md:157–174,203–230 — a useful task call and quick start, not a method for contextual and verified example sets. |
| code-samples.tested | covered | SKILL.md:168–172,210–222,264–266 — use concrete examples and check that documented code and commands work. |
| images-media.* | not-applicable | No images, graphics or video deliverable. |
| doc-accessibility.reading | shallow | SKILL.md:42,201–230 — useful headings and layout, without a specific accessibility review. |
| doc-accessibility.structure | shallow | SKILL.md:42,201–230 — useful headings and layout, without a specific accessibility review. |
| doc-accessibility.color | not-applicable | No rendered portal or custom visual layer. |
| doc-accessibility.page | not-applicable | No rendered portal or custom visual layer. |
| docs-build.docs-as-code | shallow | SKILL.md:268–283 — uses version control to diagnose drift but does not specify reviewing docs alongside the code change. |
| docs-build.lint | absent | Verification has no documented automated docs check. |
| docs-build.publish | not-applicable | Local docs handoff; no site build, hosting, CMS or in-product help. |
| docs-build.online-help | not-applicable | Local docs handoff; no site build, hosting, CMS or in-product help. |
| docs-build.findable | not-applicable | Local docs handoff; no site build, hosting, CMS or in-product help. |
| docs-build.cms | not-applicable | Local docs handoff; no site build, hosting, CMS or in-product help. |
| doc-review.edit | covered | SKILL.md:260–283,308–320 — verify prose and implementation details; document dated changes without rewriting history. |
| doc-review.technical | covered | SKILL.md:260–283,308–320 — verify prose and implementation details; document dated changes without rewriting history. |
| doc-review.qa | shallow | SKILL.md:264–266,308–320 — reviews commands, factual details and ADR coverage, not links or rendered docs systematically. |
| doc-review.ai-generated | not-applicable | Uses project facts and code; not ingesting or publishing externally sourced or generated reference material as a declared stage. |
| doc-review.plagiarism | not-applicable | Uses project facts and code; not ingesting or publishing externally sourced or generated reference material as a declared stage. |
| doc-review.records | covered | SKILL.md:260–283,308–320 — verify prose and implementation details; document dated changes without rewriting history. |
| doc-maintenance.revise | covered | SKILL.md:260–283,308–320 — verify prose and implementation details; document dated changes without rewriting history. |
| doc-maintenance.feedback | not-applicable | No public feedback channel, removal workflow or translated variants. |
| doc-maintenance.remove | not-applicable | No public feedback channel, removal workflow or translated variants. |
| doc-maintenance.localise | not-applicable | No public feedback channel, removal workflow or translated variants. |

counts: covered 23, shallow 16, absent 3, not-applicable 33, undetermined 0


## Excluded by profile

None.
