# Blindspot report: analyze

Skill under audit: [Anthropic's analyze](https://github.com/anthropics/knowledge-work-plugins/tree/0e0fcacddcc892eb92a1b7873ff9d68159c47571/data/skills/analyze).

Map: data-analysis 0.1.0    Profile: none    Date: 2026-11-23

## Scope

- Answers data questions at three levels: metric lookup, multi-dimensional analysis, and a formal stakeholder report.
- Starts with a user's question, uses an existing warehouse or user-supplied extracts, and ends at an answer or report, optionally with a chart.
- Includes SQL and checks on derived results. Does not commission new data collection, train predictive models, or operate a production dashboard.

## Step 2 list (before opening the map nodes)

- Looked for a way to confirm the business definition, denominator and decision before pulling data; the intake extracts fields and selects output format.
- Looked for a record tying the returned answer to exact queries and inputs; the query is explicitly handed over for quick answers but not other output tiers.
- Looked for an escalation when a failed validation changes the answer; the workflow asks for investigation and a caveat but does not say when to re-run or withhold the result.

## Findings

### Needed

None.

### Worth considering

1. **Confirm the metric and evidence needed before querying** [model+map]
   Map nodes: `question.stakeholders`, `question.acceptance`, `data.source-suitability`.
   Source: [O*NET: Data Scientists](https://www.onetonline.org/link/details/15-2051.00) — Task 1001554 (interview stakeholders).
   Source: [O*NET: Statisticians](https://www.onetonline.org/link/details/15-2041.00) — Task 8959 (evaluate sources).
   Source: [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — 6.1.1 The commissioner’s responsibilities.
   Why: A syntactically valid query can use the wrong population or denominator. Finding matching columns and checking plausible results do not settle those choices.
   Fix: For ambiguous or consequential requests, confirm the metric definition and intended use with the requester, and check that data coverage, freshness and granularity support them.
2. **Carry the exact analysis into the report handoff** [model+map+trace]
   Map nodes: `data.provenance-log`, `preparation.transform-log`, `analysis.assumptions-log`, `reporting.analysis-code`, `reporting.environment-record`, `reporting.version-record`.
   Source: [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) — Record all the steps used to process data; Put project source code in the src directory; Make dependencies and requirements explicit.
   Source: [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — Data log; Assumptions log; Version control.
   Why: The quick-answer path hands over its query, but a description of methodology in the formal report does not tie its numbers to the exact queries, chart code, inputs or assumptions that produced them.
   Fix: For full analyses and reports, link a rerun record with the exact query and chart artefacts, dated or versioned inputs, dialect and dependencies, and consequential assumptions.
3. **Make failed checks change the delivery decision** [model+map+trace]
   Map nodes: `preparation.quality-checks`, `assurance.proportional-review`, `assurance.verify-validate`, `assurance.code-review`.
   Source: [O*NET: Statisticians](https://www.onetonline.org/link/details/15-2041.00) — Task 8957 (prepare data and check inaccuracies).
   Source: [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — 3.1 Factors for determining appropriate assurance; 8.2.1 Verification and validation; 8.2.3 Assurance of code.
   Why: The listed checks catch some bad results, but pre-analysis checks depend on results looking unexpected and investigation does not explicitly lead back to corrected queries or block delivery of an unreliable answer.
   Fix: Check key inputs before aggregation, choose extra checks for high-impact requests, and make material failures trigger query review and revalidation or an explicitly inconclusive result.
4. **Separate robust patterns from ones that depend on an analytical choice** [map]
   Map nodes: `preparation.outlier-review`, `exploration.relationships`, `exploration.distributions`, `analysis.uncertainty-treatment`, `visualisation.uncertainty-display`.
   Source: [O*NET: Statisticians](https://www.onetonline.org/link/details/15-2041.00) — Task 8955 (identify relationships and factors affecting results).
   Source: [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — 8.2.2 Data validity and data considerations; 8.4 Treatment of uncertainty.
   Source: [Data visualisation: charts](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/) — Communicating quality and uncertainty in charts.
   Why: Trend and outlier detection are prescribed and the chart skill can show intervals, but the workflow does not tell the analyst to check distributions before method selection or see whether conclusions survive a changed assumption or unusual point.
   Fix: For consequential comparisons, inspect distributions, investigate influential observations, and show the impact of plausible choices on the conclusion and chart.
5. **Check what can be retrieved and shared** [map]
   Map nodes: `data.reuse-permission`, `ethics.minimise-personal-data`, `ethics.deidentification`.
   Source: [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) — Make the license explicit.
   Source: [Personal Information Protection Law of the PRC](http://www.npc.gov.cn/npc/c2/c30834/202108/t20210820_313088.html) — Articles 6 and 73 (purpose limitation and definitions).
   Why: The workflow narrows selected fields to the query but does not check permissions for derived outputs, reduce identifiers in reports or interactive hover fields, or distinguish reversible pseudonyms from anonymised data. The customer-table example makes this relevant without establishing that Chinese law applies.
   Fix: Before retrieval and before sharing, confirm the permitted purpose and audience, minimise identifiers, and assess whether small groups or hover fields can identify people.

### Minor

1. **Carry missing periods into the chart** [map+trace]
   Map node: `visualisation.time-gaps` — [Data visualisation: charts](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/), Breaks in time series.
   Why: Validation looks for gaps but the delegated line-chart pattern does not specify how to make them visible.
   Fix: Break the line across missing periods and annotate relevant series changes.
2. **Check chart contrast rather than assuming the palette passes** [map]
   Map nodes: `visualisation.text-contrast`, `visualisation.graphic-contrast`.
   Source: [WCAG 2.2](https://www.w3.org/TR/WCAG22/) — 1.4.3 Contrast (Minimum); 1.4.11 Non-text Contrast.
   Why: The chart skill calls for readable text and sufficient mark/background contrast, but gives no contrast-ratio check.
   Fix: Check text and necessary graphic elements separately against the applicable contrast requirements.
3. **Make the charting input reusable for a rerun** [map]
   Map node: `reporting.reproduction-example` — [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510), Provide a simple example or test data set.
   Why: The chart guide's examples depend on an existing dataframe, rather than providing a small representative input for reproducing a delivered chart.
   Fix: When a formal report includes code and source data cannot travel, provide a small safe sample or synthetic equivalent with a rerun instruction.

## Unsourced findings

None.

## Evidence limitations

Static review of the pinned workflow, connector documentation, and the called SQL and chart skills. No warehouse, user data, or generated report was accessed; no queries or chart code were run. Unqualified line references below refer to the audited skill; delegated file references use the skill folder name.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Interpret the request | Complexity, data requirements, output format | Retrieval and reporting | No explicit confirmation of ambiguous metric definitions before retrieval. |
| Retrieve data | Query results or supplied extract | Analysis | Query failures loop back to SQL; surprising successful results trigger a sanity check. |
| Analyse and validate | Metrics, comparisons, flagged issues | Answer or report | Checks include reconciliation, but there is no explicit return to a corrected query or decision to withhold. |
| Present and chart | Answer, evidence and optional chart | Requester | Quick answers include SQL; full reports do not explicitly retain an exact rerun record. Chart guidance does not carry the time-gap check into the rendering. |

## Map table

| Node | State | Evidence |
|---|---|---|
| question.problem | covered | SKILL.md:23,25–30 — "Parse the user's question" and classify the work. |
| question.stakeholders | absent | No clarification with stakeholders about priorities or constraints. |
| question.acceptance | shallow | SKILL.md:29–30 — "Output format" is selected, but criteria for an acceptable answer are not agreed. |
| data.collection-plan | not-applicable | Uses existing data, not newly collected data. |
| data.source-suitability | shallow | SKILL.md:36,40 — "find relevant tables and columns" checks relevance, not whether the source represents the intended population. |
| data.provenance-log | shallow | SKILL.md:84 — "approach and data sources" documents sources at report time but not an input-by-input log. |
| data.reuse-permission | absent | No permission or licence check for inputs or derived deliverables. |
| preparation.preserve-raw | not-applicable | The workflow reads an existing warehouse or supplied extract; it instructs no overwrites or standalone cleaning stage. |
| preparation.raw-backup | not-applicable | The skill does not manage the originals or their backups. |
| preparation.quality-checks | shallow | SKILL.md:40,62–66 — "If results look unexpected" is the only check before analysis; detailed checks run after analysis. |
| preparation.outlier-review | shallow | SKILL.md:54,68 — "outliers, and anomalies" are identified, but the workflow does not connect investigation to a treatment decision. |
| preparation.analysis-tables | covered | SKILL.md:29,36–38,53–55 — "Calculate relevant metrics, aggregations, and comparisons" using data selected for required dimensions. |
| preparation.record-keys | covered | sql-queries/SKILL.md:344–375 — the cohort example joins on "c.user_id = a.user_id" and counts distinct users. |
| preparation.transform-log | shallow | SKILL.md:74,79,84 — "Include the query used" is required only for quick answers, not as a record of all processing. |
| exploration.relationships | shallow | SKILL.md:54–55 — "Compare across dimensions" explores relationships, without a check for factors that might change the interpretation. |
| exploration.distributions | absent | No instruction to inspect distributions before choosing an approach; the histogram recipe is for communicating data. |
| analysis.method-fit | covered | SKILL.md:25–30,53–56 — "break the problem into sub-questions" on complex requests; work scales from a lookup to comparisons across dimensions. |
| analysis.sampling-design | not-applicable | No sampling or experimental study is designed. |
| analysis.assumptions-log | absent | Reporting caveats does not require logging assumptions, rationale or review decisions. |
| analysis.uncertainty-treatment | absent | No workflow step tests how uncertainty changes results; plotting intervals is not evaluating them. |
| analysis.predictive-validation | not-applicable | No predictive model workflow. |
| analysis.model-comparison | not-applicable | No comparison of candidate predictive models. |
| visualisation.chart-selection | covered | data-visualization/SKILL.md:13–29 — "Choose by Data Relationship" maps relationships to chart types. |
| visualisation.informative-titles | covered | data-visualization/SKILL.md:254–255 — "Title states the insight" and subtitles supply context. |
| visualisation.readable-labels | covered | data-visualization/SKILL.md:256,303 — "Axes are labeled with units" and label legibility is checked. |
| visualisation.bar-baseline | covered | data-visualization/SKILL.md:269 — "Bar charts start at zero". |
| visualisation.time-gaps | shallow | SKILL.md:65 — "unexpected gaps" are checked but there is no instruction to break the rendered line. |
| visualisation.colour-encoding | covered | data-visualization/SKILL.md:279–281 — "pattern fills, different line styles" provide non-colour cues. |
| visualisation.text-alternative | covered | data-visualization/SKILL.md:286–287 — "alt text describing the chart's key finding" and an accompanying table. |
| visualisation.text-contrast | shallow | data-visualization/SKILL.md:301 — "Text is readable at standard zoom level" checks readability, not minimum contrast. |
| visualisation.graphic-contrast | shallow | data-visualization/SKILL.md:292 — "contrast between data elements and background" is requested without a check threshold. |
| visualisation.uncertainty-display | covered | data-visualization/SKILL.md:272 — "Error bars, confidence intervals, or ranges" when the data are uncertain. |
| reporting.audience-results | covered | SKILL.md:72–87 — "Executive summary with key takeaways" for formal readers, with simpler forms for quick answers. |
| reporting.limited-conclusions | covered | SKILL.md:68,79,86 — "Caveats, limitations, and data quality notes" in formal reports; flag issues identified in validation. |
| reporting.analysis-code | shallow | SKILL.md:74 — "Include the query used" for quick answers only; no equivalent requirement for full analyses and chart artefacts. |
| reporting.environment-record | absent | Dialect examples are not a record of what environment produced a deliverable. |
| reporting.version-record | absent | No link from result to exact input snapshot or query/chart revision. |
| reporting.reproduction-example | shallow | data-visualization/SKILL.md:76 — "df.groupby('category')" assumes an existing input; no small reproducer is required for the delivered analysis. |
| assurance.proportional-review | shallow | SKILL.md:25–28,60–68 — "Complexity level" changes the output, not the validation plan or scrutiny applied. |
| assurance.verify-validate | shallow | SKILL.md:62–68 — "Do subtotals sum to totals correctly?" checks implementation outcomes without an explicit test against the intended question. |
| assurance.code-review | shallow | SKILL.md:39,66 — "debug and retry" on failure; checks on results do not explicitly review whether successful query joins and filters implement the intended logic. |
| assurance.delivery-signoff | not-applicable | Ends at delivery to the requester, not formal approval. |
| ethics.personal-data-basis | not-applicable | No China PIPL processing scenario is established by this general-purpose workflow. |
| ethics.minimise-personal-data | shallow | SKILL.md:29 — "Which tables, metrics, dimensions, and time ranges are needed" narrows the scope, without explicitly minimising identifiers. |
| ethics.deidentification | absent | No decision about whether or how to de-identify customer information before reporting. |

Domain coverage (node counts):

counts: covered 13, shallow 16, absent 8, not-applicable 8, undetermined 0

## Excluded by profile

None.
