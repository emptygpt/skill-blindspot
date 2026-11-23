# Blindspot report: exploratory-data-analysis

Skill under audit: [exploratory-data-analysis](https://github.com/K-Dense-AI/claude-scientific-skills/tree/c21d13b3cc2894680229ba9959a53281acb9200e/skills/exploratory-data-analysis).

Map: data-analysis 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Inspects authorized local inputs, profiles supported files, and reports what the diagnostics can and cannot establish.
- Ends at the exploratory report; data transformations are not silently applied.
- Does not conduct confirmatory inference, deploy code, or collect fresh data.

## Step 2 list (before opening the map nodes)

- Looked at required reasoning, scaffold and interpretation for a question-driven plot and a compact, author-facing chart check; a table of diagnostics is not equivalent.

## Findings

### Needed

None.

### Worth considering

1. **Preserve a reproducible record of the exploratory run** [map+trace]
   Map nodes: `data.provenance-log`, `reporting.version-record`, `reporting.reproduction-example`, `reporting.analysis-code`.
   Source: [The AQuA Book (2025 update)](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — Data log; Version control.
   Source: [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) — Provide a simple example or test data set.; Put project source code in the src directory..

   Why: A capability manifest describes the environment and diagnostics yield outputs, but the report handoff does not bind those artifacts to exact inputs and invocation parameters.
   Fix: Record input identity, script or skill revision, options and a minimal offline rerun reference without embedding raw values.
2. **Use a suitable visual when descriptive tables obscure a pattern** [model+map]
   Map nodes: `exploration.relationships`, `visualisation.chart-selection`.
   Source: [O*NET OnLine: Statisticians (15-2041.00)](https://www.onetonline.org/link/details/15-2041.00) — Task 8955: Identify relationships and trends in data, as well as any factors that could affect the results of research..
   Source: [Data visualisation: charts](https://analysisfunction.civilservice.gov.uk/policy-store/data-visualisation-charts/) — Choosing the right chart.
   Why: The checklist requires contextual reasoning; it does not give a decision rule for when a plot would uncover a relationship or distribution missed by summaries.
   Fix: When permitted by data sensitivity, choose a diagnostic visualization that answers the question and verify its axes, units and redaction.
3. **Agree what a useful exploratory report will answer** [map]
   Map nodes: `question.acceptance`, `reporting.audience-results`.
   Source: [The AQuA Book (2025 update)](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — 6.1.1 The commissioner’s responsibilities.
   Source: [O*NET OnLine: Statisticians (15-2041.00)](https://www.onetonline.org/link/details/15-2041.00) — Task 20194: Present statistical and nonstatistical results, using charts, bullets, and graphs, in meetings or conferences to audiences such as clients, peers, and students..
   Why: The scaffold provides outputs and warnings without explicitly connecting completion to a reader's decision or question.
   Fix: State the intended question, what evidence is sufficient, and which findings are unanswerable at the given scope.

### Minor

None.

## Unsourced findings

None.

## Evidence limitations

Static review only. This audit concerns the skill's general, authorized local data workflow; format-specific diagnostics are not executed, and no subject-matter protocol or dataset is audited. The named output report is produced at runtime.


## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Authorize and inventory inputs | Permitted local path and capabilities | Diagnostic selection | SKILL.md:159–175 gates analysis on authorization and support. |
| Run diagnostics | Local summaries and warnings | Contextual analysis | SKILL.md:176–236 requires interpreting output and known limits. |
| Build scaffold and deliver | Exploratory findings | Reader | SKILL.md:237–272 requires a completed interpretation but does not tie it to an exact input/run record. |

## Map table

| Node | State | Evidence |
|---|---|---|
| question.problem | covered | SKILL.md:123–155,176–224 — frames the analytical purpose and chooses diagnostics by support, limits and data shape. |
| question.stakeholders | not-applicable | No commissioning process or new data collection in local profiling. |
| question.acceptance | absent | No explicit user-facing definition of what a sufficient exploratory deliverable answers. |
| data.collection-plan | not-applicable | No commissioning process or new data collection in local profiling. |
| data.source-suitability | covered | SKILL.md:123–155,165–176 — inventories files and calls for missingness, types and quality checks. |
| data.provenance-log | shallow | SKILL.md:165–175,237–249 — manifest and diagnostic outputs exist but there is no consolidated reproducibility record. |
| data.reuse-permission | covered | SKILL.md:15–38,103–121,159–164 — requires local authorization, limits input and defaults to redacted reporting. |
| preparation.preserve-raw | covered | SKILL.md:103–121,123–155 — analysis is read-only with no silent changes. |
| preparation.raw-backup | not-applicable | Read-only profiling; no derived analysis dataset, join or cleaning pipeline is delivered. |
| preparation.quality-checks | covered | SKILL.md:123–155,165–176 — inventories files and calls for missingness, types and quality checks. |
| preparation.outlier-review | covered | SKILL.md:123–155,176–223 — inspect distributions and investigate anomalies rather than silently treating them as errors. |
| preparation.analysis-tables | not-applicable | Read-only profiling; no derived analysis dataset, join or cleaning pipeline is delivered. |
| preparation.record-keys | not-applicable | Read-only profiling; no derived analysis dataset, join or cleaning pipeline is delivered. |
| preparation.transform-log | not-applicable | Read-only profiling; no derived analysis dataset, join or cleaning pipeline is delivered. |
| exploration.relationships | shallow | SKILL.md:123–155,176–223 — relationship-related diagnostic options exist but no systematic choice of pairwise plots for the question. |
| exploration.distributions | covered | SKILL.md:123–155,176–223 — inspect distributions and investigate anomalies rather than silently treating them as errors. |
| analysis.method-fit | covered | SKILL.md:123–155,176–224 — frames the analytical purpose and chooses diagnostics by support, limits and data shape. |
| analysis.sampling-design | not-applicable | No study design, fitted predictive model or comparative modelling. |
| analysis.assumptions-log | covered | SKILL.md:123–155,224–272 — record caveats and separate descriptive evidence and inference. |
| analysis.uncertainty-treatment | covered | SKILL.md:123–155,224–272 — record caveats and separate descriptive evidence and inference. |
| analysis.predictive-validation | not-applicable | No study design, fitted predictive model or comparative modelling. |
| analysis.model-comparison | not-applicable | No study design, fitted predictive model or comparative modelling. |
| visualisation.chart-selection | absent | Report workflow does not ask for a question-driven visual even when a table hides the shape of the data. |
| visualisation.informative-titles | not-applicable | No rendered chart deliverable is defined. |
| visualisation.readable-labels | not-applicable | No rendered chart deliverable is defined. |
| visualisation.bar-baseline | not-applicable | No rendered chart deliverable is defined. |
| visualisation.time-gaps | not-applicable | No rendered chart deliverable is defined. |
| visualisation.colour-encoding | not-applicable | No rendered chart deliverable is defined. |
| visualisation.text-alternative | not-applicable | No rendered chart deliverable is defined. |
| visualisation.text-contrast | not-applicable | No rendered chart deliverable is defined. |
| visualisation.graphic-contrast | not-applicable | No rendered chart deliverable is defined. |
| visualisation.uncertainty-display | not-applicable | No rendered chart deliverable is defined. |
| reporting.audience-results | shallow | SKILL.md:237–249; assets/report_template.md — findings and limits have places in the report, but the workflow does not explicitly tailor the synthesis to its reader. |
| reporting.limited-conclusions | covered | SKILL.md:123–155,224–272 — record caveats and separate descriptive evidence and inference. |
| reporting.analysis-code | shallow | SKILL.md:165–175,237–249 — manifest and diagnostic outputs exist but there is no consolidated reproducibility record. |
| reporting.environment-record | covered | SKILL.md:165–175 — use the capability manifest before interpreting available diagnostics. |
| reporting.version-record | shallow | SKILL.md:165–175,237–249 — manifest and diagnostic outputs exist but there is no consolidated reproducibility record. |
| reporting.reproduction-example | shallow | SKILL.md:165–175,237–249 — manifest and diagnostic outputs exist but there is no consolidated reproducibility record. |
| assurance.proportional-review | covered | SKILL.md:123–155,224–249 — requires reviewing diagnostics and contextualizing limits before report assembly. |
| assurance.verify-validate | covered | SKILL.md:123–155,224–249 — requires reviewing diagnostics and contextualizing limits before report assembly. |
| assurance.code-review | not-applicable | No software change or external sign-off required. |
| assurance.delivery-signoff | not-applicable | No software change or external sign-off required. |
| ethics.personal-data-basis | not-applicable | The generic local workflow and this audit do not establish a China PIPL processing scenario; operator authorization alone does not establish a legal basis. |
| ethics.minimise-personal-data | covered | SKILL.md:15–38,103–121,159–164 — requires local authorization, limits input and defaults to redacted reporting. |
| ethics.deidentification | covered | SKILL.md:15–38,103–121,159–164 — requires local authorization, limits input and defaults to redacted reporting. |

counts: covered 16, shallow 6, absent 2, not-applicable 21, undetermined 0

## Excluded by profile

None.
