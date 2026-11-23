# Blindspot report: jupyter-notebook

Skill under audit: [OpenAI's jupyter-notebook](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook).

Map: data-analysis 0.1.0    Profile: none    Date: 2026-11-23

## Scope

- Audits the experiment mode: turn a question, supplied code or notes into a runnable analytical notebook with results and a next decision.
- Starts at intent and template selection, ends at a notebook with an execution check when feasible, and covers analytical data already available to the user or generated in the notebook.
- Does not evaluate tutorial mode, a standalone chart or publication workflow, new data collection, or production models.

## Step 2 list (before opening the map nodes)

- Looked for exact input versions and dependency versions beyond a seed and a Python version.
- Looked for checks verifying expected input shape and values, beyond a top-to-bottom execution check.
- Looked for an interpretation that records what the experiment does not establish; the template prompts for failure modes and a next decision.

## Findings

### Needed

None.

### Worth considering

1. **Bind reproducibility to the actual notebook run** [model+map+trace]
   Map nodes: `data.provenance-log`, `reporting.environment-record`, `reporting.version-record`.
   Source: [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — Data log; Version control.
   Source: [Good enough practices in scientific computing](https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005510) — Make dependencies and requirements explicit.
   Why: The experiment baseline addresses repeatable random choices and the helper sets Python metadata, but neither records exact input artifacts or the environment that actually executed the delivered notebook.
   Fix: In setup and the final handoff, record the notebook revision, input IDs or fingerprints, actual kernel and package versions, and parameters used to produce the saved results.
2. **Validate the data and the answer, not just execution** [model+map+trace]
   Map nodes: `data.source-suitability`, `preparation.quality-checks`, `preparation.outlier-review`, `exploration.distributions`, `assurance.verify-validate`, `assurance.code-review`.
   Source: [O*NET: Statisticians](https://www.onetonline.org/link/details/15-2041.00) — Task 8959 (evaluate sources); Task 8957 (prepare data and check inaccuracies).
   Source: [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — 8.2.1 Verification and validation; 8.2.2 Data validity and data considerations; 8.2.3 Assurance of code.
   Why: A clean run confirms execution order and state, but a notebook can run successfully with the wrong input population, duplicate observations or incorrect calculations. The sample summarises a generated series; it does not establish when to examine unusual values in real data.
   Fix: Before analysis on supplied data, check source suitability, expected input shape, distributions and unusual values; before delivery, check key calculations against a known case or invariant and compare the resulting answer with the objective.
3. **Explain what the experiment can and cannot support** [model+map]
   Map nodes: `analysis.sampling-design`, `analysis.assumptions-log`, `analysis.uncertainty-treatment`, `reporting.limited-conclusions`.
   Source: [O*NET: Statisticians](https://www.onetonline.org/link/details/15-2041.00) — Task 8966 (develop and test designs and methods).
   Source: [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — Assumptions log; 8.4 Treatment of uncertainty; 9.2.2 Communication.
   Why: The plan names hypotheses and metrics, and the results prompt for failure modes, but neither says when the design supports an inference, how sensitive it is to choices, or what should not be concluded.
   Fix: When the notebook makes an inferential claim, record and justify its design and assumptions, assess relevant uncertainty, and state which conclusions the evidence does not support.

### Minor

1. **Clarify the acceptance test for a notebook handed to another reader** [map]
   Map nodes: `question.stakeholders`, `question.acceptance`.
   Source: [O*NET: Data Scientists](https://www.onetonline.org/link/details/15-2051.00) — Task 1001554 (interview stakeholders).
   Source: [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government) — 6.1.1 The commissioner’s responsibilities.
   Why: The workflow records the audience and desired objective but does not say to confirm their constraints or the intended use when the requester and reader differ.
   Fix: When handed to another reader, confirm the intended use and success criteria before scaffolding.
2. **Scale the final check to the use of the notebook** [map]
   Map node: `assurance.proportional-review` — [The AQuA Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government), 3.1 Factors for determining appropriate assurance.
   Why: The checklist varies with execution capability, not with the consequences of a wrong result.
   Fix: Add an independent calculation or review for findings likely to inform a consequential decision.

## Unsourced findings

None.

## Evidence limitations

Static review of the pinned skill, its references, notebook templates, and scaffold helper. The scaffold, notebooks and code examples were not executed. The experiment template uses generated data; findings about supplied inputs concern the instructions for adapting that workflow, not observed failures on an actual dataset.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Define intent and pick mode | Objective, audience, success criteria and experiment mode | Scaffold and experiment plan | No confirmation with an external reader before scaffolding. |
| Scaffold and fill | Notebook, configuration, baseline and analytical cells | Execution and interpretation | Baseline is run before complexity is added; exact inputs and environment are not bound to the run. |
| Record results | Metrics, observations and next decision | Notebook reader | Results are located beside code; no prescribed check that data and derived quantities support the objective. |
| Validate and hand off | Executable notebook or local validation instructions | Reader who runs or reviews the notebook | Top-to-bottom run checks execution, not the correctness of each result. |

## Map table

| Node | State | Evidence |
|---|---|---|
| question.problem | covered | references/experiment-patterns.md:5 — "state the question and the success criteria" before setup. |
| question.stakeholders | shallow | SKILL.md:37–39 — "Capture the objective, audience" without instructions to ask about the reader's needs or constraints. |
| question.acceptance | shallow | references/experiment-patterns.md:5 — "the success criteria" are stated, but the workflow does not say to agree them and the intended use. |
| data.collection-plan | not-applicable | The experiment mode starts with existing inputs or generates example values; it does not design primary data collection. |
| data.source-suitability | absent | No instruction assesses whether supplied inputs are suitable for the question. |
| data.provenance-log | absent | The configuration cell does not require tracking input source, ownership or reliability. |
| data.reuse-permission | not-applicable | Scoped to generated or user-supplied inputs, with no acquisition of third-party datasets or redistribution. |
| preparation.preserve-raw | not-applicable | The workflow structures a notebook, not a raw-data storage or cleaning project. |
| preparation.raw-backup | not-applicable | It does not manage backups of original inputs. |
| preparation.quality-checks | absent | No check of expected data shape, keys, completeness or valid ranges. |
| preparation.outlier-review | absent | No step screens unusual values and investigates their cause; the template's summary statistics do not prescribe a review. |
| preparation.analysis-tables | not-applicable | The workflow produces notebook cells and a results summary, not an analysis-ready dataset. |
| preparation.record-keys | not-applicable | No required join or related-table preparation. |
| preparation.transform-log | covered | SKILL.md:58–60; references/quality-checklist.md:5–6 — "Keep each code cell focused on one step"; execute in order without hidden state, preserving the sequence as code. |
| exploration.relationships | not-applicable | The experiment path does not prescribe trend or relationship investigation; it also applies to runnable baselines without these outputs. |
| exploration.distributions | shallow | assets/experiment-template.ipynb — "statistics.fmean(values)" is paired with extrema as a sample summary, not a check against expectations before selecting a method. |
| analysis.method-fit | covered | SKILL.md:22–25; references/experiment-patterns.md:7–8 — "If the request is exploratory, analytical, or hypothesis-driven" choose the experiment pattern, which plans metrics and a baseline before adding complexity. |
| analysis.sampling-design | shallow | references/experiment-patterns.md:7 — "list hypotheses, sweeps, and metrics" outlines the design but does not check its validity for inference. |
| analysis.assumptions-log | absent | No record of assumptions, justifications, or decisions about them. |
| analysis.uncertainty-treatment | absent | No guidance on sensitivity analysis or uncertainty of estimated results. |
| analysis.predictive-validation | not-applicable | No prescribed predictive-model validation workflow. |
| analysis.model-comparison | not-applicable | No candidate model selection stage is required. |
| visualisation | not-applicable | The experiment output prescribes notebook code with compact metrics and tables, not chart creation. |
| reporting.audience-results | covered | SKILL.md:39,58–61; references/experiment-patterns.md:9 — "summarize findings in markdown near the relevant code" with concise structured metrics. |
| reporting.limited-conclusions | shallow | assets/experiment-template.ipynb — "Surprises or failure modes" prompts for unexpected results but does not require limits on interpretation. |
| reporting.analysis-code | covered | SKILL.md:58–61,72–75 — "Fill the notebook with small, runnable steps" keeps the analysis code with the delivered results. |
| reporting.environment-record | shallow | SKILL.md:89–98; scripts/new_notebook.py:57–61 — "Optional Python packages for local notebook execution" identifies tooling; template metadata is not an inventory of the executed environment. |
| reporting.version-record | absent | No link between saved outputs and exact notebook and input versions. |
| reporting.reproduction-example | covered | references/experiment-patterns.md:6–8; assets/experiment-template.ipynb — "smallest runnable example" is illustrated by a fixed-seed synthetic baseline. |
| assurance.proportional-review | shallow | references/quality-checklist.md:5 — "as much as the environment allows" scales the run check to execution capability, not to analytical risk. |
| assurance.verify-validate | shallow | references/quality-checklist.md:5–6 — "avoid hidden state from prior runs" verifies execution independence, not fitness of the output for the question. |
| assurance.code-review | shallow | SKILL.md:72–75 — "Run the notebook top-to-bottom" can catch runtime errors but is not review of analytical logic. |
| assurance.delivery-signoff | not-applicable | Hand-off is the validated notebook or local validation instructions, not approval by a commissioner. |
| ethics | not-applicable | The audited experiment baseline is synthetic; the workflow neither calls for processing identifiable data nor prescribes release of such data. |

Domain coverage (node counts):

counts: covered 6, shallow 9, absent 7, not-applicable 23, undetermined 0

## Excluded by profile

None.
