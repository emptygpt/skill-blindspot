# Blindspot report: research-paper-writing

Skill under audit: [research-paper-writing](https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/77e7c2c1ba06f7d71844873147665437a03aac1b/research-paper-writing).

Map: research-paper 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Rewrites and drafts sections of ML/CV/NLP papers (Abstract to Conclusion), tables and figure captions, and runs a reviewer-style self-review.
- Ends at revised section text with an outline, a self-review checklist and a claim-evidence map; it does not run experiments, submit the paper or answer real reviewers.
- Does not design or conduct the study, deposit data or code, or handle venue forms.

## Step 2 list (before opening the map nodes)

- Run-to-run variation (seeds, error bars, significance) for reported comparisons.
- Code, data and model availability statement; software versions and compute.
- Venue paper checklist, double-blind anonymization, page limits.
- Ethics or broader-impact statement; dataset licences and consent.
- Disclosure of AI assistance when the agent rewrites the paper.
- Citation accuracy and a rule against invented numbers or references while drafting.
- Baseline tuning budget and test-set leakage beyond a shared split.
- Funding, author contribution and acknowledgment statements.
- Rebuttal after submission (outside: the skill stops before submission).

## Findings

### Needed

None.

### Worth considering

1. **Report variation across runs and how it was estimated** [model+map]

   Map nodes: `analysis.uncertainty`, `analysis.evidence`, `computation.randomness`.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — iii. Statistics.
   Source: [ASA Statement on Statistical Significance and P-Values (2016)](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) — principles 5 and 6.
   Source: [Reproducible Research, Kempner Institute Computing Handbook](https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/reproducible_research.html) — 10.4. Randomness and Seeds.
   Why: The rigor checks ask whether gains are "meaningful, not just statistically tiny" and "consistent across multiple datasets/settings/metrics", but no table or experiments rule asks for seeds, number of runs, standard deviations or intervals; a searched grep for seed, variance and error bar found none in the guides.
   Fix: In references/experiments.md (table rules and rigor checklist), ask for the number of runs, the spread or interval reported, and the seed policy when results vary between runs.
2. **Check the venue's paper checklist and required statements** [model+map]

   Map nodes: `reporting.selection`, `ethics.ai-disclosure`, `manuscript.funding`, `computation.code-access`, `publication.data-availability`.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — 2. Reporting Guidelines; a. Title Page.
   Source: [ICMJE: Defining the Role of Authors and Contributors](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html) — 4. Artificial Intelligence (AI)-Assisted Technology.
   Source: [Nature Portfolio: Reporting standards and availability of data, materials, code and protocols](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards) — Availability of data; Availability and peer review of computer code and algorithm.
   Why: The self-review covers contribution, clarity, experiments, evaluation and method design only. The skill rewrites the paper with an agent but never mentions a venue checklist, AI-assistance disclosure, funding or competing interests, or where code and data can be obtained. The boundary question is whether these belong to a later submission step; the content of the statements sits in the paper the skill writes.
   Fix: Add a sixth self-review dimension in references/paper-review.md that checks the target venue's checklist and required statements, and lists those the author must supply.
3. **Keep drafted numbers and references traceable to the author's material** [model+map]

   Map nodes: `ethics.misconduct`, `manuscript.references`.
   Source: [ICMJE: Scientific Misconduct](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/scientific-misconduct-expressions-of-concern-and-retraction.html) — B. Scientific Misconduct.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — g. References.
   Why: Claims must be supported or weakened, and the related-work checklist asks whether "citation coverage" is complete, but no step tells the agent not to supply numbers or references it was not given, or to check that each cited work exists and says what the sentence attributes to it.
   Fix: In the Execution Rules of SKILL.md, require that every number and reference in drafted text comes from the author's results or bibliography, and mark the rest as placeholders in the claim-evidence map.
4. **Identify datasets and software, with versions, in the paper** [map]

   Map nodes: `computation.versions`, `computation.environment`, `computation.software-citation`, `computation.specific-release`, `publication.data-citation`, `publication.data-citation-version`.
   Source: [Software Citation Principles (2016)](https://force11.org/info/software-citation-principles-published-2016/) — 1. Importance; 6. Specificity.
   Source: [Joint Declaration of Data Citation Principles (2014)](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) — 1. Importance; 4. Unique Identification; 7. Specificity and Verifiability.
   Source: [The Turing Way: Reproducible Environments](https://book.the-turing-way.org/reproducible-research/renv) — Reproducible Environments.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — iii. Statistics.
   Why: Implementation details cover hyperparameters and normalization only; benchmarks are named as evidence, but nothing asks to cite datasets and frameworks as references, or to state dataset splits or versions and software versions.
   Fix: Extend the Implementation Details paragraph in references/method.md with dataset and software citations and the versions or splits used.
5. **Say how baselines and settings were chosen and tuned** [model+map]

   Map nodes: `analysis.exploration`, `analysis.transparency`.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — iii. Statistics.
   Source: [ASA Statement on Statistical Significance and P-Values (2016)](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) — 4. Proper inference requires full reporting and transparency.
   Why: A fair protocol is a shared split, preprocessing and evaluation; tuning budgets for the proposed method versus baselines, and which ablations were planned versus run after seeing results, are not asked for.
   Fix: Add tuning budget and planned-versus-exploratory analyses to the rigor checklist in references/experiments.md.

### Minor

1. **Statistical wording when a paper reports tests or percentages** [map]

   Map nodes: `analysis.model-compatibility`, `analysis.hypothesis-probability`, `analysis.thresholds`, `analysis.denominators`.
   Source: [ASA Statement on Statistical Significance and P-Values (2016)](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) — principles 1 to 3.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — e. Results.
   Why: ML/CV/NLP method papers seldom report p-values, so this matters only for user studies or significance tests; the guides give no wording rules for them.
2. **Author metadata and contribution statements** [map]

   Map nodes: `manuscript.title-page`, `manuscript.orcid`, `manuscript.authorship`, `manuscript.acknowledgments`, `manuscript.roles`.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — a. Title Page.
   Source: [ICMJE: Defining the Role of Authors and Contributors](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/defining-the-role-of-authors-and-contributors.html) — 2. Who Is an Author?; 3. Non-Author Contributors.
   Source: [CRediT role descriptors](https://credit.niso.org/contributor-roles-defined/) — CRediT role descriptors.
   Why: The skill works on body sections; double-blind ML venues add these only in the camera-ready version, so this is likely intentional.
3. **Reused figures and identifiable people in images** [map]

   Map nodes: `manuscript.figures`, `publication.permissions`, `ethics.privacy`.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — i. Illustrations (Figures).
   Source: [ICMJE: Sending the Manuscript to the Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/sending-the-submission.html) — B. Sending the Manuscript to the Journal.
   Source: [ICMJE: Protection of Research Participants](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/protection-of-research-participants.html) — E. Protection of Research Participants.
   Why: Figure guidance covers layout and captions; it does not mention attribution or permission for reused images, or people who can be identified in teaser and qualitative figures.

## Unsourced findings

- **Double-blind anonymization and page limits.** No map node covers anonymizing a submission or fitting a page limit; no source has been checked.

## Evidence limitations

Read SKILL.md and every file under references/ as static evidence; agents/openai.yaml is interface metadata and was not used as evidence. No paper, experiment log or venue template was used.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Clarify story and mini-outline | Section outline | Paragraph rewrite | SKILL.md:84 requires the outline before prose. |
| Rewrite with section guides | Revised paragraphs with roles | Reverse outlining and claim check | SKILL.md:42–47 maps paragraphs to the thesis. |
| Claim check and adversarial review | Claim-evidence map, items marked pass / needs revision / needs new experiment | Output contract | references/paper-review.md:80–86; a needs-new-experiment item cannot be closed by rewriting and is returned to the author in the claim-evidence map. |

## Map table

| Node | State | Evidence |
|---|---|---|
| design.* | not-applicable | The study and experiments are supplied by the author; the skill writes about them. |
| ethics.approval | not-applicable | Obtaining approval happens in the study, outside the skill. |
| ethics.publication-consent | not-applicable | No patient material; consent is obtained outside the skill. |
| ethics.privacy | absent | No step on identifiable people in text or figures. |
| ethics.animal-welfare | not-applicable | No animal research in the skill's paper types. |
| ethics.misconduct | shallow | SKILL.md:88 "If a claim cannot be supported by results, weaken or remove the claim." — no rule against supplying unsupplied numbers or references. |
| ethics.ai-disclosure | absent | No mention of disclosing AI assistance. |
| data.* | not-applicable | Depositing and describing data happens outside a writing skill. |
| analysis.methods | covered | references/experiments.md:13 "Keep protocol fair (same data split, preprocessing, and evaluation settings)."; references/paper-review.md:70 "Are comparison and ablation protocols clearly documented?" |
| analysis.uncertainty | absent | No seeds, runs, spread or intervals in any guide. |
| analysis.exploration | absent | No planned-versus-exploratory distinction. |
| analysis.complete-outcomes | covered | references/experiments.md:21 "Report both gains and failure modes to show realistic boundaries."; references/paper-review.md:62 "Do we report both strengths and failure cases honestly?" |
| analysis.denominators | absent | No rule on counts behind percentages. |
| analysis.interpretation | covered | references/paper-review.md:59 "Are improvements over strong baselines meaningful, not just statistically tiny?"; references/experiments.md:102 "Are limitations of evaluation scope explicitly stated?" |
| analysis.model-compatibility | absent | No p-value guidance. |
| analysis.hypothesis-probability | absent | No p-value guidance. |
| analysis.thresholds | absent | No p-value guidance. |
| analysis.transparency | shallow | references/paper-review.md:70 "Are comparison and ablation protocols clearly documented?" — protocols, but not tuning budgets or selection of reported results. |
| analysis.evidence | absent | Evidence is judged by gains and consistency, not by uncertainty summaries. |
| computation.versions | absent | No software versions asked for. |
| computation.code-access | absent | No code availability statement. |
| computation.review-access | not-applicable | Supplying code to reviewers happens at submission, outside the skill. |
| computation.archival-release | not-applicable | Depositing code happens outside the skill. |
| computation.software-citation | absent | No instruction to cite software used. |
| computation.specific-release | absent | No software version in citations. |
| computation.validation | not-applicable | Reproducibility checking of outputs is not performed by a writing skill. |
| computation.environment | shallow | references/method.md:184 "Implementation details include hyperparameters (e.g., layer count, feature dimensions), coordinate transforms/normalization, and other practical details." — no environment or package versions. |
| computation.project-layout | not-applicable | Organizing the research compendium happens outside the skill. |
| computation.data-version | not-applicable | Preserving inputs happens in the analysis; stating versions in the paper is under the citation nodes. |
| computation.executable-analysis | not-applicable | No analysis is run or packaged. |
| computation.randomness | absent | No seed or nondeterminism reporting. |
| computation.clean-rerun | not-applicable | No analysis is rerun. |
| computation.run-record | not-applicable | Run records are kept during the experiments, outside the skill. |
| computation.artifact-package | not-applicable | No artifact package is produced. |
| reporting.selection | absent | No venue or study-design checklist is selected or checked. |
| reporting.consort | not-applicable | Randomized trials are outside the ML/CV/NLP papers the skill targets. |
| reporting.prisma | not-applicable | Systematic reviews are outside the ML/CV/NLP papers the skill targets. |
| reporting.strobe | not-applicable | Observational epidemiology is outside the skill's paper types. |
| reporting.arrive | not-applicable | Animal studies are outside the skill's paper types. |
| reporting.stard | not-applicable | Diagnostic accuracy studies are outside the skill's paper types. |
| reporting.qualitative | not-applicable | Qualitative studies are outside the skill's paper types. |
| manuscript.structure | covered | SKILL.md:3 "drafting or revising Abstract, Introduction, Related Work, Method, Experiments, or Conclusion"; SKILL.md:84 "Build a mini-outline before drafting prose." |
| manuscript.title-page | absent | No title or author metadata step. |
| manuscript.orcid | absent | No author identifiers. |
| manuscript.funding | absent | No funding or competing-interest statement. |
| manuscript.abstract | covered | references/abstract.md:99 "Can a reader identify task, challenge, insight/contribution, and results in one pass?"; references/abstract.md:100 "Are all major claims supported by experiments?" |
| manuscript.methods | covered | references/paper-review.md:51 "Can a knowledgeable reader reproduce the method from the paper?"; references/method.md:184 "Put them near the end of Method or in a dedicated Implementation Details section." |
| manuscript.references | shallow | references/related-work.md:41 "Is citation coverage complete for all core claims?" — coverage, not accuracy of each reference. |
| manuscript.tables | covered | references/experiments.md:72 "Label metric direction in column headers"; references/experiments.md:73 "Add units when needed so values are interpretable without guessing." |
| manuscript.figures | shallow | SKILL.md:29 "Use a clean teaser and pipeline figure."; references/experiments.md:59 "Figure captions and table captions are equally important in the writing quality of Experiments." — no attribution for reused figures. |
| manuscript.authorship | absent | No authorship step. |
| manuscript.acknowledgments | absent | No acknowledgment step. |
| manuscript.roles | absent | No contributor roles. |
| publication.journal-article | covered | SKILL.md:9 "Use this skill to rewrite a research paper into a reviewer-friendly, high-clarity draft." |
| publication.submission | not-applicable | The skill stops at self-review before submission. |
| publication.permissions | absent | No permissions for reused material. |
| publication.review-history | not-applicable | Real reviews arrive after submission, outside the skill. |
| publication.data-availability | absent | No data availability statement. |
| publication.trial-sharing | not-applicable | No clinical trials. |
| publication.preprints | not-applicable | Preprint posting is a publication decision outside the skill. |
| publication.rights | not-applicable | Licence agreements come after acceptance. |
| publication.data-citation | shallow | references/related-work.md:41 "Is citation coverage complete for all core claims?" — datasets are not named as items to cite. |
| publication.data-citation-version | absent | No dataset versions or identifiers. |
| publication.revision-plan | not-applicable | Real reviewer comments arrive after submission. |
| publication.reviewer-response | not-applicable | Real reviewer comments arrive after submission. |

counts: covered 8, shallow 6, absent 24, not-applicable 38, undetermined 0

## Excluded by profile

None.
