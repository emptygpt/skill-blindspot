# Blindspot report: seo-schema

Skill under audit: [AgriciDaniel/claude-seo: seo-schema](https://github.com/AgriciDaniel/claude-seo/tree/468ed5b0d9e3249394783710e54abb02837e326b/skills/seo-schema).

Map: seo-web 0.1.0    Profile: none    Date: 2026-11-23

## Scope

- Detects and validates Schema.org markup or drafts JSON-LD for a supplied page or entity, including appropriate rich-result types.
- Starts from page content or entity facts; ends at a schema report or a JSON-LD snippet for the caller.
- Does not deploy markup, run an overall search audit, or verify search performance after deployment.

## Step 2 list (before opening the map nodes)

- Looked for rendered-DOM extraction, browser execution or a static-versus-rendered fallback; found a source fetch and advice on server-rendering Product markup, not an actual second extraction path.
- Looked for comparison of marked-up facts with the visible page beyond reviews, and for a named test wired into delivery; found truthfulness and generic validation instructions, plus a page disclosure requirement for incentivized reviews.
- Looked for a distinction between an implementable artifact and a draft with unresolved placeholders; found explicit permission to use placeholders and a generic validation step.

## Findings

### Needed

None.

### Worth considering

1. **Distinguish source-only detection from a rendered-page check** [model+map+trace]\
   Map node: `crawl-index.render` — source: Google Search Central, *SEO Starter Guide*, “Check if Google can see your page the same way a user does”.\
   Why: The URL path in `scripts/parse_html.py:950–979` parses the HTTP body; the HTML fallback in SKILL.md:19–20 also uses source. SKILL.md:56 considers injected markup when recommending delivery for Product offers, but the no-markup branch at line 183 can report an absence without knowing whether scripts add markup.\
   Fix: In Detection, add a rendered check when initial markup is missing or differs, or label the conclusion as limited to the fetched HTML.
2. **Check general markup-to-page agreement, not just review disclosure** [model+map]\
   Map node: `structured-data.visible-content` — source: Google Search Central, *General Structured Data Guidelines*, “Content”.\
   Why: SKILL.md:84–90 ties type choice to the page, demands verifiable facts, and requires visible incentive disclosures. It does not require validating the actual values against visitor-facing content for general entities, such as the price and availability of an offer. The delegated types reference's validation checklist checks values' form, not their agreement with the page.\
   Fix: In Validation and Generation, compare key marked-up values against the visible page and flag unverified or conflicting values separately from syntax errors.

### Minor

None.

## Unsourced findings

- **Separate draft placeholders from deployable output** [model+trace]. SKILL.md:87 permits labeled placeholders and line 166 describes the generated artifact as ready for use. The delegated validation checklist rejects placeholder text; the output routine does not specify how to convey a blocked or draft artifact to the caller. Mark placeholder-bearing output as draft until the missing values are verified. No map source checked for this handoff requirement.

## Evidence limitations

- Static review only: the report does not test a live page, tool invocation, or search feature. The pinned checkout includes the named templates, type and deprecation references, and the URL parser.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Detect markup | Extracted types and parse errors from a supplied page | Validation and recommendations | SKILL.md:19–29 and the URL parser inspect the response body, not an executed DOM. |
| Validate markup and select target types | Validity issues, type status and candidate replacements | Report or generation | SKILL.md:31–79 checks type, syntax and required fields; page-value agreement is partial. |
| Generate and verify snippets | JSON-LD from supplied or page facts | Caller implementing the recommendation | SKILL.md:83–90 validates before presentation but allows labeled placeholders. |
| Deliver artifacts | Report and optional generated code | Caller | SKILL.md:163–176 gives a results table and recommendations but no draft status for unresolved fields. |

## Map table

| Node | State | Evidence |
|---|---|---|
| strategy | not-applicable | Does not plan search demand or site strategy. |
| crawl-index.discover | not-applicable | Takes an already supplied page, not a discovery plan. |
| crawl-index.render | shallow | SKILL.md:56 “initial server-rendered HTML” — advises on visibility of volatile markup but does not inspect a rendered result. |
| crawl-index.robots | not-applicable | Does not audit or configure site crawl policy. |
| crawl-index.robots-limits | not-applicable | Does not advise on site crawl restrictions or removal. |
| crawl-index.noindex | not-applicable | Does not choose page indexing exclusions. |
| crawl-index.sitemap | not-applicable | Does not plan discovery inventory. |
| crawl-index.sitemap-build | not-applicable | Does not maintain discovery inventory. |
| site-structure | not-applicable | Does not design or consolidate site URLs. |
| on-page | not-applicable | Does not edit or audit headings, titles, descriptions or snippet controls. |
| structured-data.eligibility | covered | SKILL.md:34 “supported rich result types” and :84 “Identify page type from content analysis” — matches content to supported features and distinguishes unsupported uses. |
| structured-data.vocabulary | covered | SKILL.md:85 “Select appropriate schema type(s)” and :86 “required + recommended properties” — selects types and attributes by entity and page type. |
| structured-data.format | covered | SKILL.md:29 “recommend JSON-LD as primary format” — selects a supported format and recognizes Microdata and RDFa during detection. |
| structured-data.visible-content | shallow | SKILL.md:87 “truthful, verifiable data” and :90 “prominently disclosed on the page” — explicit page-facing review disclosure, but no general markup-to-visible-data comparison. |
| structured-data.complete | covered | SKILL.md:33 “required properties per schema type” — checks feature-specific required fields and calls for them on generation. |
| structured-data.validation | covered | SKILL.md:88 “Validate output before presenting”; delegated `schema-types.md:131–132` names “Google Rich Results Test” and “Schema.org Validator”. The report identifies fixes for the caller rather than deploying them. |
| page-experience | not-applicable | No usability or performance audit. |
| international | not-applicable | No alternate-page design or locale audit. |
| media | not-applicable | Can write image and video markup, but does not plan media delivery or audit watch-page, thumbnail or file retrieval. |
| links | not-applicable | Does not audit navigational or outbound links. |
| content-ops | not-applicable | No portfolio, removal, or migration work. |
| measurement | not-applicable | No search-performance or index-coverage monitoring. |
| compliance | not-applicable | No site-wide spam, affiliate or advertising audit; the review-specific rule is accounted for under markup visibility. |

counts: covered 5, shallow 2, absent 0, not-applicable 67, undetermined 0

## Excluded by profile

None.
