# Blindspot report: document-api-endpoint

Skill under audit: [document-api-endpoint](https://github.com/getsentry/skills/tree/a582c51ee29d0f35e6ac321340796f77d43da733/skills/document-api-endpoint).

Map: tech-docs 0.1.0    Profile: none    Date: 2026-11-23

## Scope

- Adds or repairs Sentry endpoint documentation and request and response schemas, including migration of legacy definitions and optional promotion of a specific operation to public.
- Ends at validated source and generated OpenAPI changes, with a PR note where permissions widen. The downstream SDK release is described, not performed by the skill.
- Does not write a standalone tutorial, consumer quickstart, or documentation site.

## Step 2 list (before opening the map nodes)

- Verify at least one conditional response, not just the ordinary response: the typing guidance distinguishes null and omitted keys, but the runtime verification example only inspects top-level keys.
- Inspect the generated entry as a consumer would see it: the final commands build and validate the spec and examples, but the skill does not explicitly ask for a user-facing reference review.

## Findings

### Needed

None.

### Worth considering

1. **Exercise the response cases that can change the contract** [model+map+trace]
   Map nodes: `api-description.responses`, `api-description.examples`.
   Source: [OpenAPI Specification v3.1.1](https://spec.openapis.org/oas/v3.1.1.html) — Responses Object; Response Object; Header Object; Example Object.
   Why: The skill explicitly compares runtime types with the declaration, and the public guide covers error codes, response examples and pagination. The skill and guide describe optional fields, but neither makes the author choose and exercise the request that triggers a conditional field; a checked default response and a schema-valid fixture can still miss the variant.
   Fix: In Validate, exercise the requests with and without the condition, use representative inputs in the examples, and verify relevant error bodies and headers against the generated operation.
2. **Give the rendered operation a content review, not only a preview** [model+map+trace]
   Map nodes: `doc-planning.readers`, `page-structure.headings`, `api-reference.generated-review`, `doc-review.qa`, `doc-review.ai-generated`.
   Source: [Microsoft Writing Style Guide](https://learn.microsoft.com/en-us/style-guide/welcome/) — Content planning; Scannable content; Reference documentation: review automatically generated documentation and comments; Final publishing review.
   Source: [GitLab, Contribute to the GitLab documentation](https://docs.gitlab.com/development/documentation/) — Workflows: AI-generated documentation.
   Why: The linked guide already gives a local rendering workflow and asks for a PR screenshot, so preview is not missing. It does not say who should check that the rendered summary matches a consumer task, that user-facing details make sense without implementation context, or that links and examples are accurate.
   Fix: Ask the PR reviewer to inspect the rendered operation for the reader's task, title, description, links and accidental internal detail, as well as the schema diff.
3. **Document the replacement when retiring a public operation** [map]
   Map node: `api-reference.deprecations`.
   Source: [OpenAPI Specification v3.1.1](https://spec.openapis.org/oas/v3.1.1.html) — Operation Object: deprecated.
   Source: [AIP-192: Documentation](https://google.aip.dev/192) — Deprecations.
   Why: Promotion may be stacked after a separate retirement change, but the skill does not say to mark the outgoing operation in the contract or explain what to use instead.
   Fix: For the deprecation branch of promotion, call out the generated deprecation marker and link to the replacement, or state that there is none.

### Minor

1. **Keep consumer-facing descriptions consistent and readable** [map]
   Map nodes: `page-structure.links`, `writing-style.guide`, `writing-style.voice`, `writing-style.terminology`, `writing-style.global`, `writing-style.inclusive`, `writing-style.timeless`, `writing-style.code-font`, `doc-accessibility.reading`, `doc-review.edit`.
   Source: [Google developer documentation style guide](https://developers.google.com/style) — Cross-references and linking; Highlights: Use second person and Use active voice; Write for a global audience; Write inclusive documentation; Timeless documentation; Code in text; Write accessible documentation: Ease of reading.
   Source: [O*NET: Technical Writers](https://www.onetonline.org/link/details/27-3042.00) — edit and standardize material prepared by other writers.
   Why: The guide explains vague resource names and where text appears, and the product's response-field guide gives a voice convention for field descriptions. The generation and preview instructions do not include a consistent editorial pass across all changed reference prose.
   Fix: In the rendered review, apply the existing reference style where available and check terminology, readable descriptions, formatting and link labels.
2. **Use unmistakably synthetic sample values** [map]
   Map node: `code-samples.example-values`.
   Source: [Google developer documentation style guide](https://developers.google.com/style) — Example domains and names.
   Source: [RFC 2606](https://www.rfc-editor.org/rfc/rfc2606.txt) — TLDs for Testing, & Documentation Examples.
   Why: The guide illustrates synthetic names and the tooling checks example shape. Neither check tells authors to scrub captured response values before using them as a published example.
   Fix: In the example-authoring step, require synthetic identifiers and reserved address values where applicable; keep captured payloads out of checked-in examples.
3. **Link related operations when they matter to the reader** [map]
   Map node: `api-reference.cross-references`.
   Source: [AIP-192: Documentation](https://google.aip.dev/192) — Cross-references.
   Why: Shared tags and components relate operations for navigation and maintenance but do not direct users to a prerequisite or next operation in the generated reference.
   Fix: When a description depends on another operation, link to that operation's reference entry.
4. **Check user-facing prose and links independently of schema validation** [map]
   Map node: `docs-build.lint`.
   Source: [GitLab, Contribute to the GitLab documentation](https://docs.gitlab.com/development/documentation/) — Documentation testing: Run Vale, markdownlint, or link checks locally.
   Why: Building the spec, validating example JSON and running file-level hooks do not explicitly check prose and cross-links in generated endpoint descriptions.
   Fix: Where tooling is available, include the docs prose and link checks for changed reference text in the validation step.

## Unsourced findings

None.

## Evidence limitations

Static review of the pinned skill and its delegated [public publishing guide](https://github.com/getsentry/develop/blob/26cabd61bbd94ac8cffd05f1cacd03950a5576c7/src/docs/api/public.mdx) (`public.mdx`) and [public API checklist](https://github.com/getsentry/develop/blob/26cabd61bbd94ac8cffd05f1cacd03950a5576c7/src/docs/api/checklist.mdx) (`checklist.mdx`). Checked the referenced build/validation path in [getsentry/sentry at 6cb93e9](https://github.com/getsentry/sentry/tree/6cb93e974574ffd70cc2bc164e3b4dc6dd677446), including the [response-field guide](https://github.com/getsentry/sentry/blob/6cb93e974574ffd70cc2bc164e3b4dc6dd677446/src/sentry/apidocs/README.md#response-fields). No endpoint requests, skill commands, credentials, site previews or releases were used. Described downstream publication is context, not a job the skill asks the author to perform. Product-wide metadata, standalone guides and site operation are intentionally outside the per-endpoint scope.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Identify the route and behavior | Endpoint owner, implementation and observed behavior | Schema decorator and declared types | SKILL.md:8,20–27 directs comparison with runtime and reuse of the owning implementation's types. |
| Write or migrate the definitions | Schema annotations, reusable types and examples; old paths retired | OpenAPI generation | SKILL.md:10–16,32–33 requires a complete per-path migration; method-level tests follow. |
| Validate generated output and runtime | Built spec, example validation and endpoint test results | Change review | SKILL.md:46–52 and public.mdx:360–390 give validation and preview; the conditional-response check and semantic preview criteria are not explicit. |
| Optionally prepare promotion | Changed publication state and PR note on widened scopes | Downstream release | SKILL.md:35–44 scopes the change to the concrete method; release is downstream. |

## Map table

| Node | State | Evidence |
|---|---|---|
| doc-planning.readers | absent | The public consumers are implied, but the workflow does not identify their specific task before writing the description. |
| doc-planning.subject | covered | SKILL.md:8,35–41 — "identify which endpoint class serves the route" defines the subject before any schema work and promotion is per method. |
| doc-planning.gather | covered | SKILL.md:8,20–27 — "Carefully compare what the code does vs declared types" anchors docs in implementation and runtime. |
| doc-planning.topic-types | not-applicable | The artifact is a predetermined endpoint reference, not a docs architecture or topic selection exercise. |
| doc-planning.single-source | covered | SKILL.md:26–33 — "Reuse the existing canonical type" and remove the old parallel definition on migration. |
| doc-planning.docs-with-code | covered | SKILL.md:12–16,32–33 — "migrate every method on the path in one commit" keeps generated documentation changes aligned with the decorated methods. |
| doc-planning.legal-safety | not-applicable | Product-wide legal and usage-warning review is not part of annotation maintenance; the guide's protection of private response fields is accounted for under generated review. |
| doc-planning.project | not-applicable | The skill updates an individual operation, not a documentation project plan. |
| page-structure.order | covered | public.mdx:188–189,202–204 — "Required parameters will automatically be placed at the top" gives consistent parameter order. |
| page-structure.headings | shallow | public.mdx:176–178 — "the title of the endpoint's page" explains the field mapping but does not check its wording against a reader task. |
| page-structure.procedures | not-applicable | End-user procedures are not a deliverable. |
| page-structure.step-results | not-applicable | No end-user procedure to checkpoint. |
| page-structure.links | absent | No link-label guidance for the generated endpoint prose. |
| page-structure.readme | not-applicable | No README deliverable. |
| page-structure.repo-links | not-applicable | The deliverable is an operation generated from source, not linked repository Markdown pages. |
| page-structure.troubleshooting | covered | public.mdx:312–323 — "define your own for more detailed messages" explains how to document endpoint-specific failures. |
| writing-style.guide | absent | The framework guide explains annotation structure, not which prose style to apply to reference descriptions. |
| writing-style.voice | shallow | src/sentry/apidocs/README.md:94–95 — "Write for any API client" guides how authors refer to the reader in field descriptions, not how to handle voice and tense across the operation. |
| writing-style.terminology | shallow | public.mdx:130–135 — "include a description for all resources" calls out unclear resource names without establishing terminology across operations. |
| writing-style.global | absent | No explicit guidance for writing descriptions for readers with different first languages. |
| writing-style.inclusive | absent | No language or example diversity guidance for changed descriptions. |
| writing-style.timeless | absent | No check for dated or release-dependent wording in public reference text. |
| writing-style.code-font | absent | No prose formatting rule for identifiers, parameter names or UI labels. |
| writing-style.dates | not-applicable | Date and number representation in payload schemas is covered under inputs/responses; no date prose is required. |
| api-reference.reference-comments | covered | public.mdx:130–135 — "using the endpoint's docstring" establishes the source of endpoint descriptions. |
| api-reference.method-details | covered | public.mdx:176–220 — "include all possible success and failure HTTP response cases" complements path, query and body documentation. |
| api-reference.docstrings | covered | public.mdx:130–142 — "using the endpoint's docstring" shows where the framework takes the description and supplies a short example. |
| api-reference.reference-titles | covered | public.mdx:143–178 — "will be shown as the title" demonstrates how the endpoint title is supplied to the common template. |
| api-reference.generated-review | shallow | public.mdx:282–286,370–390 — "exclude any private fields from the response schema" and a rendered preview address part of the check, not the quality of generated prose. |
| api-reference.deprecations | shallow | SKILL.md:37–42 — "deprecate the old version in its own change" orders the work but does not say to mark or explain the deprecated operation in the reference. |
| api-reference.cross-references | absent | No direction to link related operations in the generated reference prose. |
| api-reference.guides | not-applicable | No task guides are authored. |
| api-description.design-first | not-applicable | The skill documents or repairs existing behavior rather than designing new APIs. |
| api-description.source-control | covered | SKILL.md:12–16,32–33 — "migrate every method on the path in one commit" combines annotation, migration and code review with generated output. |
| api-description.publish | not-applicable | Making a released spec directly available is downstream, not performed in the authoring workflow. |
| api-description.info | not-applicable | Spec-wide metadata and servers are not edited in a per-operation change. |
| api-description.operations | covered | public.mdx:111–178 — "will be shown as the title of the endpoint's page" explains the title field; the guide supplies tags, descriptions and the operation decorator. |
| api-description.inputs | covered | public.mdx:180–216 — "a serializer that generates body parameters" complements reusable path and query parameter definitions. |
| api-description.responses | shallow | SKILL.md:20–27 — "key only set under a condition" explains the schema distinction; the validation path does not explicitly test both conditional cases or compare operation headers. |
| api-description.examples | shallow | public.mdx:220–245 — "specify the endpoint's sample response" covers realistic response examples and status codes, not representative request values or conditional responses. |
| api-description.security | covered | SKILL.md:37–42 and checklist.mdx:8–10 — "scopes widen" triggers a PR note for regenerated scopes; the delegated checklist covers bearer authentication and permission scopes for promotion. |
| api-description.large | covered | SKILL.md:12–15,26–33 — "Reuse the existing canonical type" avoids duplicate components, and parameters and examples live in shared modules. |
| code-samples.scenarios | not-applicable | No standalone client code examples; operation payload examples are assessed under OpenAPI. |
| code-samples.intro | not-applicable | No runnable consumer sample is delivered. |
| code-samples.copy-run | not-applicable | No runnable consumer sample is delivered. |
| code-samples.output | not-applicable | No runnable consumer sample is delivered; response fixtures are assessed separately. |
| code-samples.style | not-applicable | Does not create reader-facing language-specific code samples. |
| code-samples.placeholders | not-applicable | No copy-and-run client snippet is authored. |
| code-samples.example-values | shallow | public.mdx:235–245 — "actual response body" identifies the example value, with a synthetic team shown but no directive to sanitize captured values. |
| code-samples.tested | covered | SKILL.md:46–52 — "validate-api-examples" checks published response examples against the built schema before handoff. |
| images-media | not-applicable | The preview screenshot is a review artifact, not an image or video added to the consumer documentation. |
| doc-accessibility.reading | shallow | public.mdx:130–135 — "if they are not immediately clear" prompts definitions of unclear resources, not a broader reading-level or plain-language pass. |
| doc-accessibility.structure | not-applicable | The generator supplies the page structure; the skill does not change its templates. |
| doc-accessibility.color | not-applicable | No visual design or template changes. |
| doc-accessibility.page | not-applicable | Site-level language and HTML title markup are not edited; the operation title is assessed separately. |
| docs-build.docs-as-code | covered | SKILL.md:12–16,46–52 — "build-api-docs" produces the reference input from the changed source and is run before handoff. |
| docs-build.lint | shallow | SKILL.md:46–52 — "validate-api-examples" checks schema compatibility; there is no explicit generated-prose or link check. |
| docs-build.publish | covered | public.mdx:370–390 — "To see your changes in the docs locally" introduces a rendered preview of the target documentation site before the PR. |
| docs-build.online-help | not-applicable | No in-product help. |
| docs-build.findable | not-applicable | Site search and metadata are outside the per-operation workflow; tags and page naming are checked separately. |
| docs-build.cms | not-applicable | No CMS editing or publication workflow. |
| doc-review.edit | shallow | public.mdx:130–135,370–390 — "if they are not immediately clear" gives one editorial criterion for descriptions; the PR preview has no consistent style check. |
| doc-review.technical | covered | SKILL.md:20–27,46–52 — "diff the keys and types against your TypedDict" checks the declared behavior, with endpoint tests and generated validation. |
| doc-review.qa | shallow | public.mdx:364–390 — "add a screenshot of the page" records the rendering, without explicitly checking reference accuracy, completeness, links and consumer usefulness. |
| doc-review.ai-generated | shallow | public.mdx:390 — "add a screenshot of the page" gives the reviewer a rendered artifact but does not assign human verification of agent-authored statements and links. |
| doc-review.plagiarism | not-applicable | The prescribed materials are project-owned code and examples, not third-party prose reuse. |
| doc-review.records | covered | SKILL.md:32–42 — "Note in the PR if scopes widen" preserves the reason for permission changes alongside the migration's source history. |
| doc-maintenance.revise | covered | SKILL.md:20–33 — "Correct the declared type to match runtime" explicitly supports updating stale operation contracts. |
| doc-maintenance.feedback | not-applicable | Does not collect or triage ongoing consumer feedback on docs. |
| doc-maintenance.remove | covered | SKILL.md:32–33 — "migrate every method on the path in one commit" removes the superseded path and reference while preserving sibling methods. |
| doc-maintenance.localise | not-applicable | No translated reference deliverable. |

Domain coverage counts: covered 22, shallow 13, absent 8, not-applicable 32, undetermined 0.

## Excluded by profile

None.
