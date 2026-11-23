# Blindspot report: GEOHub seo

Skill under audit: [yaojingang/GEOHub: seo](https://github.com/yaojingang/GEOHub/tree/2210f7f22153cfdf721905c2ac86318db97401b1/skills/seo).

Map: seo-web 0.1.0    Profile: none    Date: 2026-11-23

## Scope

- Turns a natural-language SEO request into a read-only, evidence-bounded work plan with one selected mode.
- Includes plans for technical, keyword, incident, migration, experimentation and international or commerce work and hands off evidence collection.
- Ends at a brief, plan and evidence/quality artifacts. The planner does not produce site findings or execute changes; implementation requests reach an authorization gate.

## Step 2 list (before opening the map nodes)

- Looked for matching action requirements and missing-evidence logic; found separate lists, with the migration and experiment inventories not checked by the missing-evidence logic.
- Looked for specific directive interpretation and an explanation of what blocks crawling versus indexing; found high-level layering and a check for robots controls.
- Looked for sample/period comparison, an indexed/live inspection procedure and monitoring checkpoints; found segmenting and generic monitoring, not those procedures.
- Looked for instructions to validate locale codes and a fallback; found a reciprocal-hreflang check but not those two checks.

## Findings

### Needed

None. This is a planning workflow; the omissions below do not make it generate unsupported site findings or perform unauthorized changes.

### Worth considering

1. **Make crawl and indexing decisions testable** [model+map]\
   Map nodes: `crawl-index.render` — *SEO Starter Guide*, “Check if Google can see your page the same way a user does”; `crawl-index.robots`, `crawl-index.robots-limits` — *Introduction to robots.txt*, “What is a robots.txt file used for?” and “Understand the limitations of a robots.txt file”; `crawl-index.noindex` — *Block Search indexing with noindex*, “Implementing noindex”.\
   Why: The method and common action distinguish these layers but stop before saying how to test a crawler's view or distinguish an intentional crawl block from an index exclusion.\
   Fix: In the common technical stage, ask for an engine-specific rendered view where available, applicable robots rules, and evidence that crawlers can read any intended noindex directive.
2. **Plan a sitemap inventory and processing check together** [map]\
   Map nodes: `crawl-index.sitemap`, `crawl-index.sitemap-build` — *Learn about sitemaps*, “Do I need a sitemap?” and “Build a sitemap”; `measurement.sitemaps` — *Reports at a glance*, “Sitemaps report”.\
   Why: The planner asks for existing artifacts and alignment during migration, not a comparison of intended URLs with sitemap entries and processing errors.\
   Fix: Specify sitemap need, intended indexable URLs, and a post-submission processing check in discovery and migration plans.
3. **Add preferred-destination decisions to migration and variant plans** [map]\
   Map nodes: `site-structure.duplicates` — *SEO Starter Guide*, “Reduce duplicate content”; `site-structure.canonical`, `content-ops.consolidate` — *How to specify a canonical URL*, “Reasons to specify a canonical URL” and “Use redirects”; `content-ops.redirects` — *Redirects and Google Search*, “Overview of redirect types”.\
   Why: The action plan aligns signals, but it does not say how to choose a surviving page when several URLs serve the same content or when a redirect is temporary.\
   Fix: Ask the variant and migration steps to group equivalent URLs and record preferred destinations and permanent or temporary redirect intent per mapping.
4. **Distinguish a feature eligibility check from a syntax check** [map]\
   Map nodes: `structured-data.eligibility` — *Introduction to structured data markup in Google Search*, “How structured data works in Google Search”; `structured-data.complete` — *General structured data guidelines*, “Completeness”; `structured-data.validation` — *Getting started with schema.org using Microdata*, “Testing your markup”.\
   Why: The method separates syntax and eligibility, but the technical or commerce action does not ask for a validator result or evidence that the actual page meets feature requirements.\
   Fix: Where markup matters, ask for separate syntax test results and a check of the chosen feature's required fields and page fit.
5. **Request mobile and field experience evidence explicitly** [map]\
   Map nodes: `page-experience.review` — *Understanding page experience in Google Search results*, “Self-assess your content's page experience”; `page-experience.cwv`, `page-experience.field` — *Web Vitals*, “Core Web Vitals” and “Field tools to measure Core Web Vitals”; `page-experience.mobile`, `page-experience.mobile-parity`, `page-experience.mobile-access` — *Mobile site and mobile-first indexing best practices*, “Create a mobile-friendly site”, “Make sure that content is the same on desktop and mobile” and “Make sure that Google can access and render your content”.\
   Why: The method separates lab from field performance and the schema can label field evidence, but neither the method nor the actions prescribe real-user measures or mobile checks.\
   Fix: Add optional technical-audit tasks for field loading, responsiveness and layout stability, plus mobile navigation, content parity and crawler access.
6. **Extend reciprocal hreflang review to the locale set** [model+map]\
   Map nodes: `international.alternates`, `international.codes`, `international.fallback` — *Tell Google about localized versions of your page*, “Methods for indicating your alternate pages”, “Supported language and region codes” and “Use the x-default value for unmatched languages”.\
   Why: The checklist names an inventory and reciprocal links but does not require grouping equivalents, checking codes, or reviewing the fallback.\
   Fix: Ask the international stage for a page-to-locale matrix, valid codes, and a designated fallback where appropriate.
7. **Give selected media search surfaces their own evidence requests** [map+trace]\
   Map nodes: `media.image-discovery`, `media.image-context`, `media.image-performance` — *Google image SEO best practices*, “Help us discover and index your images”, “Use descriptive filenames, titles, and alt text” and “Optimize for speed and quality”; `media.video-pages`, `media.video-thumbnails`, `media.video-files` — *Video SEO best practices*, “Create a dedicated watch page for each video”, “Provide a high-quality video thumbnail” and “Allow Google to fetch your video files”.\
   Why: `_surfaces` can set an image or video surface, but `_action_plan` receives only the mode; picking a media surface does not make the plan request media evidence.\
   Fix: For those surfaces, add image discovery, description and delivery checks or watch-page, thumbnail and file-fetch checks as applicable.
8. **Turn incident and migration monitoring into comparable checks** [model+map]\
   Map nodes: `content-ops.move-monitor` — *How to move a site*, “Use Search Console to monitor traffic”; `measurement.performance`, `measurement.indexing`, `measurement.inspect`, `measurement.actions` — *Reports at a glance*, “Performance reports: Web Search”, “Page indexing report”, “URL Inspection tool” and “Manual actions report”.\
   Why: Incident mode scopes segments and asks for first-party evidence; migration calls for monitoring. Neither specifies comparable windows and measures, coverage or exclusion checks, indexed-versus-live inspection or a manual-actions check when investigating sudden losses.\
   Fix: Name the reports, comparable dates and measures, and which observed changes should trigger an individual URL or manual-actions investigation.

### Minor

1. **Make keyword research feed explicit content priorities** [map]\
   Map nodes: `strategy.terms` — *SEO Starter Guide*, “Expect your readers' search terms”; `strategy.competitors`, `strategy.content-strategy` — *Search Marketing Strategists*, O*NET tasks 16186 and 20321; `content-ops.people-first` — *Creating helpful, reliable, people-first content*, “Avoid creating search engine-first content”.\
   Why: The method starts with intent and the planner assigns page roles, but neither asks for vocabulary variants or competitor and trend evidence to prioritize the pages that serve a distinct need. This matters more for a site plan than a one-off keyword assignment.\
   Fix: Offer evidence-backed priority and query-variant checks in keyword-map mode when the request covers a site or portfolio.
2. **Add optional page and internal-link checks for broader audits** [map]\
   Map nodes: `on-page.titles`, `on-page.main-heading`, `on-page.stale-titles` — *Influencing your title links in search results*, “Best practices for influencing title links”, “No clear main title” and “Obsolete <title> elements”; `on-page.descriptions` — *Control your snippets in search results*, “Create unique descriptions for each page on your site”; `links.crawlable`, `links.internal`, `links.anchors` — *Link best practices for Google*, “Make your links crawlable”, “Internal links: cross-reference your own content” and “Write good anchor text”.\
   Why: The method mentions page meaning and internal architecture and the runtime checks internal discovery. It does not ask for page-specific titles, current headings/descriptions, or evidence that internal links are crawlable, descriptive and useful. These checks may not be needed for narrowly scoped incident plans.\
   Fix: Add a page and internal-link sample to the technical-audit mode when the request includes on-page or architecture work.
3. **Tie the measurement plan to the stated objective** [map]\
   Map node: `measurement.kpis` — *Search Marketing Strategists*, O*NET task 20326.\
   Why: The plan captures the business outcome and experiment baseline but does not select measures that indicate whether the outcome was achieved.\
   Fix: Ask the scope or experiment stage to name the metric, baseline, and comparison period for each agreed objective.
4. **Make policy review conditional on the requested SEO work** [map]\
   Map node: `compliance.spam` — *Spam policies for Google web search*, “Spam policies for Google web search”.\
   Why: The skill excludes link spam and defers to official documentation, but does not ask a general technical or incident plan to check relevant spam policies when a risky practice is in evidence.\
   Fix: Add a conditional policy check keyed to the provider and the site practice being investigated.

## Unsourced findings

- **Reconcile the requested evidence with the missing-evidence ledger** [model+trace]. The migration, experiment and international/commerce actions name required inventories in `seo.py:84–86`; `_missing` at lines 93–101 does not check them. The plan still requests them, but the ledger and quality warnings may omit them, and the Markdown view prints objectives, not the required evidence lists. Derive the ledger and the Markdown requests from the selected action's evidence requirements or explicitly mark untracked requirements. No map source checked for consistency across plan artifacts.

## Evidence limitations

- Static audit of the pinned checkout, including the method, example, wrapper, delegated planner and brief schema. No target scripts, live sites or authenticated Search Console queries were run.
- The runtime intentionally emits no site findings. Assessment of planning steps does not establish what an analyst might later do with the artifacts.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Normalize request | Brief and evidence references | Runtime validation and mode selection | Brief is schema-checked before and after normalization and duplicate evidence IDs are rejected. |
| Select mode and surface | Plan route and search-surface tags | Action plan and analyst | The mode drives actions, but media surface tags do not change them. |
| Issue the plan and collect named evidence | Actions, requirements, ledger and coverage notes | Analyst gathering evidence or rerunning the plan | The ledger does not check all requirements; missing requirements can be lost in the Markdown handoff. |
| Deliver and gate implementation | Quality report, manifest and authorization status | Caller and any later implementer | Artifacts are validated before publishing to the run folder; the planner itself neither asserts site findings nor runs writes against the site. |

## Map table

| Node | State | Evidence |
|---|---|---|
| strategy.intent | covered | `seo-method.md:11` “map intent and expected page type before clustering”; `seo.py:82` requires query or SERP evidence for the mapping. |
| strategy.terms | shallow | `seo.py:82` “Map real search intent and page roles” — the mapping calls for query evidence but not variants for readers with different vocabulary. |
| strategy.competitors | absent | No comparison of demand trends or competitors in the keyword-map mode. |
| strategy.content-strategy | shallow | `seo.py:82` “search intent and page roles” — assigns page roles but does not specify which gaps to prioritize across the site. |
| strategy.eligibility | covered | `seo.py:78–79` “Check crawler access, URL discovery” and “index eligibility” — scopes status, discovery and rendered evidence before further planning. |
| crawl-index.discover | covered | `seo.py:78` “status paths, and internal discovery” — asks for HTTP, robots and sitemap artifacts to explain how URLs are found. |
| crawl-index.render | shallow | `seo.py:79` “Separate fetched HTML, rendered DOM” — gathers render evidence but does not call for a search-engine view or comparison with visitor-facing content. |
| crawl-index.robots | shallow | `seo.py:78` “robots controls” — requests the artifact without specifying user-agent or critical-resource rule checking. |
| crawl-index.robots-limits | shallow | `seo-method.md:13` “robots access, index directives” — distinguishes layers without explaining why a crawl block does not remove a URL or protect private data. |
| crawl-index.noindex | shallow | `seo-method.md:13` “index directives” — names the layer without asking which exclusions are intentional or whether bots can read them. |
| crawl-index.sitemap | shallow | `seo.py:78` “robots and sitemap artifacts” — gathers existing evidence without defining whether a sitemap is needed or what should be in it. |
| crawl-index.sitemap-build | shallow | `seo.py:84` “align redirects, canonicals, hreflang, sitemaps” — asks for alignment during a move without giving a URL membership or upkeep check. |
| site-structure.urls | not-applicable | Maps existing URLs during a move but does not design naming conventions. |
| site-structure.directories | not-applicable | Does not design a taxonomy or directory hierarchy. |
| site-structure.duplicates | shallow | `seo.py:86` “variants, pagination” — identifies variant cases to review, not how to compare duplicate content or decide its handling. |
| site-structure.canonical | shallow | `seo-method.md:13` “canonical preference” — distinguishes preference from other signals but does not say how to choose a preferred duplicate. |
| site-structure.canonical-signals | covered | `seo.py:84` “align redirects, canonicals, hreflang, sitemaps” — makes alignment a migration task tied to both URL inventories. |
| on-page.titles | absent | The page-meaning stage has no title-quality or uniqueness check. |
| on-page.main-heading | absent | The page-meaning stage does not compare the main heading with the title. |
| on-page.stale-titles | absent | The page-meaning stage does not check dated titles against current page facts. |
| on-page.descriptions | absent | The page-meaning stage does not request an inventory or check for distinct descriptions. |
| on-page.snippet-controls | not-applicable | Does not plan suppression or shortening of search snippets. |
| structured-data.eligibility | shallow | `seo-method.md:13` “structured-data syntax, search-feature eligibility” — requires treating eligibility separately but gives no feature-to-page decision. |
| structured-data.vocabulary | not-applicable | Does not select Schema.org types and attributes for implementation. |
| structured-data.format | not-applicable | Does not produce or choose an implementation format for markup. |
| structured-data.visible-content | not-applicable | Commerce mode checks visible facts but does not promise reconciling actual JSON-LD values with them. |
| structured-data.complete | shallow | `seo-method.md:13` “search-feature eligibility” — scopes feature eligibility without requiring the selected feature's mandatory fields as evidence. |
| structured-data.validation | shallow | `seo-method.md:13` “structured-data syntax” — distinguishes syntax from eligibility, but no validator or output is requested. |
| page-experience.review | shallow | `seo-method.md:7` “technical delivery”; `seo-method.md:13` “lab performance, field performance” — makes performance a layer but does not plan a landing-page usability review. |
| page-experience.cwv | shallow | `seo-brief.schema.json:28` “web_vitals_field” — can take Web Vitals evidence but does not request separate loading, responsiveness and stability measures. |
| page-experience.field | shallow | `seo-method.md:13` “lab performance, field performance” — separates the evidence classes without naming a real-user source or assessment window. |
| page-experience.mobile | absent | No mobile usability checks in the landing-page or technical plan. |
| page-experience.mobile-parity | absent | No request to compare important content across mobile and desktop versions. |
| page-experience.mobile-access | absent | No check for resource access with a mobile crawler. |
| page-experience.ads | not-applicable | Does not promise an ad-placement review. |
| international.alternates | shallow | `seo.py:86` “locale or product inventory” — asks for an inventory but does not pair each page with its locale equivalents. |
| international.hreflang | covered | `seo.py:86` “reciprocal hreflang” — asks for a bidirectional check against locale inventory; migration mode also aligns alternate signals. |
| international.codes | absent | No requirement to verify language and region code syntax. |
| international.fallback | absent | No instruction for reviewing an unmatched-language destination where there is a fallback. |
| media.image-discovery | absent | The planner labels image search as a surface but does not request rendered or crawl evidence for important images specifically. |
| media.image-context | absent | No check for image descriptions or landing-page context in an image-search plan. |
| media.image-performance | absent | No image size/quality evidence in an image-search plan. |
| media.video-pages | absent | The planner labels video search as a surface but does not check whether the video is the page's main purpose. |
| media.video-thumbnails | absent | No thumbnail stability, quality or retrieval checks in a video-search plan. |
| media.video-files | absent | No media-file fetchability checks in a video-search plan. |
| links.crawlable | shallow | `seo.py:78` “internal discovery” — requests discoverability evidence without distinguishing crawlable destinations from JavaScript-only navigation. |
| links.internal | shallow | `seo-method.md:7` “internal architecture” and `seo.py:78` “internal discovery” — this raises architecture but does not guide how to connect related pages or target orphans. |
| links.anchors | absent | No inspection of whether anchor text describes where links lead. |
| links.sponsored | not-applicable | Does not plan paid outbound links, including in commerce mode. |
| links.ugc | not-applicable | Does not design policies for user-submitted outbound links. |
| links.nofollow | not-applicable | Does not decide what outbound links to endorse. |
| content-ops.portfolio-review | not-applicable | Maps keyword intent to page roles but does not assess the portfolio for substantive updates. |
| content-ops.people-first | shallow | `seo-method.md:11` “map intent and expected page type before clustering” — ties recommendations to intent but does not evaluate whether proposed page sets offer distinct benefits to readers. |
| content-ops.freshness | not-applicable | Does not plan page date changes or a content refresh program. |
| content-ops.consolidate | shallow | `seo.py:84` “Build URL mappings and align redirects” — makes consolidation possible but does not say how to choose the surviving duplicate destination. |
| content-ops.remove | not-applicable | The migration mode plans a move, not permanent removals of retired content. |
| content-ops.redirects | shallow | `seo.py:84` “align redirects, canonicals” — requests alignment without choosing temporary versus permanent responses. |
| content-ops.move-map | covered | `seo.py:84` “Build URL mappings” from “old and new URL inventory” — makes the mapping part of the plan before any move. |
| content-ops.move-monitor | shallow | `seo-method.md:11` “before evidence, rollback, verification, and platform-processing lag”; `seo.py:84` says “monitoring” — no post-move traffic comparison or escalation timing is specified. |
| measurement.kpis | shallow | `seo.py:77` “Confirm outcome, market, language” and :85 “baseline and treatment inventory” — scopes outcomes but does not connect them to chosen search KPIs. |
| measurement.performance | shallow | `seo.py:83` “Segment page, query, market, device, search type, and time” — requests a first-party export but does not specify which measures to compare. |
| measurement.indexing | shallow | `seo.py:97` “indexation outcome evidence” — asks for property evidence without a target-vs-indexed inventory or exclusion review. |
| measurement.inspect | absent | No plan for comparing indexed and live URL Inspection views. |
| measurement.sitemaps | shallow | `seo.py:78` “sitemap artifacts” — checks the artifact, not property-level submission status or processing errors. |
| measurement.actions | absent | No manual-actions report check or remediation handoff in incident mode. |
| compliance.spam | shallow | SKILL.md:3 “link spam” and `seo-method.md:9` “official provider documentation governs mutable platform rules” — forbids link spam but does not direct an audit against applicable spam policies. |
| compliance.scaled | not-applicable | Does not design or approve a scaled publishing campaign. |
| compliance.link-spam | not-applicable | Explicitly excludes link spam and does not plan acquisition or link placement. |
| compliance.affiliate-value | not-applicable | Commerce mode looks at product facts and variants, not affiliate publishing. |
| compliance.affiliate-disclosure | not-applicable | Does not plan affiliate relationships or disclosures. |
| compliance.page-disclosure | not-applicable | Does not review sponsored page templates or consumer disclosures. |
| compliance.cn-identification | not-applicable | Can scope a Chinese market, but does not review advertising. |
| compliance.cn-internet | not-applicable | Does not review ad presentation or pop-ups. |
| compliance.cn-affiliate | not-applicable | Does not review shopping-link advertisements. |

counts: covered 6, shallow 28, absent 19, not-applicable 21, undetermined 0

## Excluded by profile

None.
