# Blindspot report: seo-audit

Skill under audit: [seo-audit](https://github.com/coreyhaines31/marketingskills/tree/5b2b400eec1e7e1cec76245a715d0b0d4fd2a9c1/skills/seo-audit).

Map: seo-web 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Diagnoses technical and content-related organic search issues from site and search evidence, then prioritizes fixes.
- Includes conditional local/international guidance and targeted ranking work when the linked guidance is selected.
- Does not generally deploy fixes, manage paid search or run an ongoing reporting service.

## Step 2 list (before opening the map nodes)

- Looked at intake, tools and report format for date/segment comparability in traffic-drop investigations and a clear distinction between sampling/access limitations and verified negatives.

## Findings

### Needed

None.

### Worth considering

1. **Make coverage and verification limits visible in the report** [model+map+trace]

   Map nodes: `crawl-index.noindex`, `crawl-index.robots-limits`, `page-experience.mobile-access`, `media.image-discovery`, `links.crawlable`, `measurement.inspect`, `measurement.actions`, `measurement.sitemaps`.
   Source: [Block Search indexing with noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) — Implementing noindex.
   Source: [Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) — Understand the limitations of a robots.txt file.
   Source: [Mobile site and mobile-first indexing best practices](https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing) — Make sure that Google can access and render your content.
   Source: [Google image SEO best practices](https://developers.google.com/search/docs/appearance/google-images) — Help us discover and index your images.
   Source: [Link best practices for Google](https://developers.google.com/search/docs/crawling-indexing/links-crawlable) — Make your links crawlable.
   Source: [Reports at a glance](https://support.google.com/webmasters/answer/9133276?hl=en) — Manual actions report; Sitemaps report; URL Inspection tool.
   Why: Static versus rendered evidence is explicit for schema but the general template does not separate crawl samples from indexed views, access limitations or manual actions.
   Fix: Split live and indexed evidence; verify directives, representative rendered resources, sitemap errors and actions, and label unavailable access separately from negatives.
2. **Define comparable baselines when diagnosing a traffic drop** [model+map]
   Map nodes: `measurement.kpis`, `content-ops.move-monitor`.
   Source: [Search Marketing Strategists (13-1161.01), O*NET OnLine](https://www.onetonline.org/link/summary/13-1161.01) — Task 20326: Identify appropriate Key Performance Indicators (KPIs) and report key metrics from digital campaigns..
   Source: [How to move a site](https://developers.google.com/search/docs/crawling-indexing/site-move-with-url-changes) — Use Search Console to monitor traffic.
   Why: Rankings-push and local guidance handle comparisons in their own routes, but intake of a general drop does not establish a matched date window or segmentation.
   Fix: Compare like-for-like query, page, device and market segments and record any migration, market or measurement discontinuity.
3. **Turn page and query overlap into an actionable recommendation** [map]
   Map nodes: `strategy.terms`, `strategy.content-strategy`, `content-ops.consolidate`, `content-ops.redirects`, `on-page.stale-titles`, `content-ops.freshness`.
   Source: [Search Engine Optimization (SEO) Starter Guide](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) — Expect your readers' search terms.
   Source: [Search Marketing Strategists (13-1161.01), O*NET OnLine](https://www.onetonline.org/link/summary/13-1161.01) — Task 20321: Create content strategies for digital media..
   Source: [How to specify a canonical URL with rel="canonical" and other methods](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls) — Use redirects.
   Source: [Redirects and Google Search](https://developers.google.com/search/docs/crawling-indexing/301-redirects) — Overview of redirect types.
   Source: [Influencing your title links in search results](https://developers.google.com/search/docs/appearance/title-link) — Obsolete <title> elements.
   Source: [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) — Avoid creating search engine-first content.
   Why: The checklist spots broad overlap and stale pages without explicitly connecting query roles, current content and the right consolidation signal.

   Fix: For overlapping pages, identify intended roles and current search snippets, then document whether to refresh, merge or redirect and why.
4. **Check rich-result suitability, not just detection** [map]
   Map nodes: `structured-data.eligibility`, `structured-data.vocabulary`, `structured-data.format`, `structured-data.visible-content`, `structured-data.complete`.
   Source: [Introduction to structured data markup in Google Search](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) — How structured data works in Google Search; Supported formats.
   Source: [Getting started with schema.org using Microdata](https://schema.org/docs/gs.html) — 2a. schema.org types and properties.
   Source: [General structured data guidelines](https://developers.google.com/search/docs/appearance/structured-data/sd-policies) — Completeness; Content.
   Why: The script-free audit workflow can see markup but does not spell out how to check applicability and eligible fields against visible content.
   Fix: Compare the rendered markup with an eligible search feature and its required properties, and distinguish a valid result from a guarantee of display.
5. **Review outbound links and spam evidence when applicable** [map]
   Map nodes: `links.sponsored`, `links.ugc`, `links.nofollow`, `compliance.spam`, `compliance.affiliate-value`.
   Source: [Qualify your outbound links to Google](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links) — rel="nofollow"; rel="sponsored"; rel="ugc".
   Source: [Spam policies for Google web search](https://developers.google.com/search/docs/essentials/spam-policies) — Spam policies for Google web search; Thin affiliation.
   Why: Useful-content and link-quality checks do not explicitly cover sponsored or user-supplied links and site-specific spam causes.
   Fix: For affected sites, sample relationship attributes and compare thin affiliate or spam patterns against the search engine’s public rules.

### Minor

1. **Check intentional snippet restrictions** [map]
   Map nodes: `on-page.snippet-controls`.
   Source: [Control your snippets in search results](https://developers.google.com/search/docs/appearance/snippet) — How to prevent snippets or adjust snippet length.
   Why: Descriptive metadata is covered, but directive-level snippet restrictions can change what searchers see.
   Fix: Check a sample of important pages for unexpected restriction or suppression.

## Unsourced findings


None.

## Evidence limitations

Audited text and bundled references without running the target workflow or inspecting a website. Search Console, browser and crawl exports are task inputs, not bundled evidence. Related skills listed for separate tasks are not credited as part of the generic audit.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Scope and get access | Target, priorities and baseline | Audit checks | SKILL.md:19–34,479–485 asks about access without enforcing matched comparisons. |
| Collect site and search evidence | Technical and content observations | Findings | SKILL.md:40–51 uses rendered verification for markup; other checks vary by tool. |
| Prioritize and deliver | Evidence, recommendation and impact | Site owner | SKILL.md:417–444 requires evidence per issue but does not name a limitations or sampling field. |

## Map table

| Node | State | Evidence |
|---|---|---|
| strategy.intent | covered | SKILL.md:19–34,53–59,274–281,315–325 — start from goals and search intent, then check technical eligibility. |
| strategy.terms | shallow | SKILL.md:274–287,315–325 — checks intent, variations and overlap; gives limited site-level decisions about distinct page roles. |
| strategy.competitors | covered | SKILL.md:479–485; references/rankings-push.md:5–30 — use search performance and top competing results to diagnose ranking opportunities. |
| strategy.content-strategy | shallow | SKILL.md:274–287,315–325 — checks intent, variations and overlap; gives limited site-level decisions about distinct page roles. |
| strategy.eligibility | covered | SKILL.md:19–34,53–59,274–281,315–325 — start from goals and search intent, then check technical eligibility. |

| crawl-index.discover | covered | SKILL.md:66–89 — checks crawl rules, discovery paths, sitemap recency and indexable membership. |
| crawl-index.render | covered | SKILL.md:40–51,459–475 — requires rendered or validator evidence rather than a static fetch for markup. |
| crawl-index.robots | covered | SKILL.md:66–89 — checks crawl rules, discovery paths, sitemap recency and indexable membership. |
| crawl-index.robots-limits | shallow | SKILL.md:68–76,99–104 — flags accidental blocks and noindex but does not explicitly explain directive visibility or privacy limits. |
| crawl-index.noindex | shallow | SKILL.md:68–76,99–104 — flags accidental blocks and noindex but does not explicitly explain directive visibility or privacy limits. |
| crawl-index.sitemap | covered | SKILL.md:66–89 — checks crawl rules, discovery paths, sitemap recency and indexable membership. |
| crawl-index.sitemap-build | covered | SKILL.md:66–89 — checks crawl rules, discovery paths, sitemap recency and indexable membership. |
| site-structure.urls | covered | SKILL.md:80–111,152–160,182–211 — checks directory and link architecture, duplicate variants and aligned locale signals. |
| site-structure.directories | covered | SKILL.md:80–111,152–160,182–211 — checks directory and link architecture, duplicate variants and aligned locale signals. |
| site-structure.duplicates | covered | SKILL.md:80–111,152–160,182–211 — checks directory and link architecture, duplicate variants and aligned locale signals. |
| site-structure.canonical | covered | SKILL.md:80–111,152–160,182–211 — checks directory and link architecture, duplicate variants and aligned locale signals. |
| site-structure.canonical-signals | covered | SKILL.md:80–111,152–160,182–211 — checks directory and link architecture, duplicate variants and aligned locale signals. |
| on-page.titles | covered | SKILL.md:238–272 — reviews descriptive and unique titles, headings and summaries. |
| on-page.main-heading | covered | SKILL.md:238–272 — reviews descriptive and unique titles, headings and summaries. |
| on-page.stale-titles | shallow | SKILL.md:238–242,389–394; references/title-tags.md:60–83 — reviews rewriting and outdated pages, not a specific content-date mismatch check. |
| on-page.descriptions | covered | SKILL.md:238–272 — reviews descriptive and unique titles, headings and summaries. |
| on-page.snippet-controls | absent | No audit step reviews which snippet restrictions are intentional. |
| structured-data.eligibility | shallow | SKILL.md:40–51,382–385,406–410,461–467 — finds and validates markup and calls out missing schema, but the audit offers little checking of content applicability and specific feature requirements. |
| structured-data.vocabulary | shallow | SKILL.md:40–51,382–385,406–410,461–467 — finds and validates markup and calls out missing schema, but the audit offers little checking of content applicability and specific feature requirements. |
| structured-data.format | shallow | SKILL.md:40–51,382–385,406–410,461–467 — finds and validates markup and calls out missing schema, but the audit offers little checking of content applicability and specific feature requirements. |
| structured-data.visible-content | shallow | SKILL.md:40–51,382–385,406–410,461–467 — finds and validates markup and calls out missing schema, but the audit offers little checking of content applicability and specific feature requirements. |
| structured-data.complete | shallow | SKILL.md:40–51,382–385,406–410,461–467 — finds and validates markup and calls out missing schema, but the audit offers little checking of content applicability and specific feature requirements. |
| structured-data.validation | covered | SKILL.md:40–51,459–475 — requires rendered or validator evidence rather than a static fetch for markup. |
| page-experience.review | covered | SKILL.md:113–142,459–464 — checks field experience and layout, navigation and content parity. |

| page-experience.cwv | covered | SKILL.md:113–142,459–464 — checks field experience and layout, navigation and content parity. |
| page-experience.field | covered | SKILL.md:113–142,459–464 — checks field experience and layout, navigation and content parity. |
| page-experience.mobile | covered | SKILL.md:113–142,459–464 — checks field experience and layout, navigation and content parity. |
| page-experience.mobile-parity | covered | SKILL.md:113–142,459–464 — checks field experience and layout, navigation and content parity. |
| page-experience.mobile-access | shallow | SKILL.md:135–142,202–211 — checks mobile readiness and locale access, not crawler visibility of mobile resources by default. |
| page-experience.ads | not-applicable | No advertising-specific task or named ad-funded site is part of the general workflow. |
| international.alternates | covered | SKILL.md:162–234 — checks alternates, reciprocal links, codes and fallback by locale. |
| international.hreflang | covered | SKILL.md:162–234 — checks alternates, reciprocal links, codes and fallback by locale. |
| international.codes | covered | SKILL.md:162–234 — checks alternates, reciprocal links, codes and fallback by locale. |
| international.fallback | covered | SKILL.md:162–234 — checks alternates, reciprocal links, codes and fallback by locale. |
| media.image-discovery | shallow | SKILL.md:68–84,289–312 — checks general access and broken links but not whether key images and destination links exist in the rendered crawlable view. |
| media.image-context | covered | SKILL.md:120–127,289–298 — checks filenames, alt text, size and loading. |
| media.image-performance | covered | SKILL.md:120–127,289–298 — checks filenames, alt text, size and loading. |
| media.video-pages | not-applicable | Does not promise a video-search audit. |
| media.video-thumbnails | not-applicable | Does not promise a video-search audit. |
| media.video-files | not-applicable | Does not promise a video-search audit. |
| links.crawlable | shallow | SKILL.md:68–84,289–312 — checks general access and broken links but not whether key images and destination links exist in the rendered crawlable view. |
| links.internal | covered | SKILL.md:80–84,300–312 — looks for orphan pages, helpful internal destinations and descriptive link text. |
| links.anchors | covered | SKILL.md:80–84,300–312 — looks for orphan pages, helpful internal destinations and descriptive link text. |
| links.sponsored | absent | No relationship-attribute check for outbound links in the site audit. |
| links.ugc | absent | No relationship-attribute check for outbound links in the site audit. |
| links.nofollow | absent | No relationship-attribute check for outbound links in the site audit. |
| content-ops.portfolio-review | covered | SKILL.md:274–287,331–362 — evaluates useful content and evidence quality at page level. |
| content-ops.people-first | covered | SKILL.md:274–287,331–362 — evaluates useful content and evidence quality at page level. |

| content-ops.freshness | shallow | SKILL.md:238–242,389–394; references/title-tags.md:60–83 — reviews rewriting and outdated pages, not a specific content-date mismatch check. |
| content-ops.consolidate | shallow | SKILL.md:99–111,182–211 — spots duplicates and redirect issues but does not guide every consolidation or temporary/permanent redirect decision. |
| content-ops.remove | not-applicable | Does not implement a retirement or plan a migration; does diagnose reported moves. |
| content-ops.redirects | shallow | SKILL.md:99–111,182–211 — spots duplicates and redirect issues but does not guide every consolidation or temporary/permanent redirect decision. |
| content-ops.move-map | not-applicable | Does not implement a retirement or plan a migration; does diagnose reported moves. |
| content-ops.move-monitor | shallow | SKILL.md:19–34,73–78,479–485; references/rankings-push.md:5–19 — provides goals, traffic baseline and sitemap submission; lacks a general traffic-drop comparison and processing-error checklist. |
| measurement.kpis | shallow | SKILL.md:19–34,73–78,479–485; references/rankings-push.md:5–19 — provides goals, traffic baseline and sitemap submission; lacks a general traffic-drop comparison and processing-error checklist. |
| measurement.performance | covered | SKILL.md:479–485; references/rankings-push.md:5–30 — use search performance and top competing results to diagnose ranking opportunities. |
| measurement.indexing | covered | SKILL.md:92–105,459–465 — compares expected against observed index coverage. |
| measurement.inspect | absent | No dedicated indexed/live comparison using URL Inspection or manual-action check in the general index diagnostic. |
| measurement.sitemaps | shallow | SKILL.md:19–34,73–78,479–485; references/rankings-push.md:5–19 — provides goals, traffic baseline and sitemap submission; lacks a general traffic-drop comparison and processing-error checklist. |
| measurement.actions | absent | No dedicated indexed/live comparison using URL Inspection or manual-action check in the general index diagnostic. |
| compliance.spam | shallow | SKILL.md:274–287,331–362 — checks thinness and useful content but does not explicitly ground the verdict in search spam rules. |
| compliance.scaled | not-applicable | Does not plan a scaled publishing or link-acquisition campaign. |
| compliance.link-spam | not-applicable | Does not plan a scaled publishing or link-acquisition campaign. |
| compliance.affiliate-value | shallow | SKILL.md:274–287,331–362 — checks thinness and useful content but does not explicitly ground the verdict in search spam rules. |
| compliance.affiliate-disclosure | not-applicable | No site monetization or jurisdiction-specific advertising compliance engagement. |
| compliance.page-disclosure | not-applicable | No site monetization or jurisdiction-specific advertising compliance engagement. |
| compliance.cn-identification | not-applicable | No site monetization or jurisdiction-specific advertising compliance engagement. |
| compliance.cn-internet | not-applicable | No site monetization or jurisdiction-specific advertising compliance engagement. |
| compliance.cn-affiliate | not-applicable | No site monetization or jurisdiction-specific advertising compliance engagement. |

counts: covered 34, shallow 21, absent 6, not-applicable 13, undetermined 0


## Excluded by profile

None.
