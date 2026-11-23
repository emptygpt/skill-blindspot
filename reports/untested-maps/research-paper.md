# Blindspot report: scientific-writing

Skill under audit: [scientific-writing](https://github.com/K-Dense-AI/claude-scientific-skills/tree/c21d13b3cc2894680229ba9959a53281acb9200e/skills/scientific-writing).

Map: research-paper 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Turns completed study evidence into a manuscript or research report, including revision and submission preparation.
- Verifies evidence, reporting requirements, disclosures and final handoff without automatically submitting.
- Does not conduct or design the underlying study.

## Step 2 list (before opening the map nodes)

- Looked at open-science, manifest and final audit for a cold rerun of the analysis packaged with the paper; saved artifacts and declared verification status are not themselves reproduction.

## Findings

### Needed

None.

### Worth considering

1. **Verify a reproducibility package with a clean rerun** [model+map+trace]

   Map nodes: `computation.validation`, `computation.executable-analysis`, `computation.randomness`, `computation.clean-rerun`, `computation.run-record`.
   Source: [CRediT role descriptors](https://credit.niso.org/contributor-roles-defined/) — Validation.
   Source: [The Turing Way: Research Compendia](https://book.the-turing-way.org/reproducible-research/compendia) — Executable Compendium.
   Source: [Reproducible Research, Kempner Institute Computing Handbook](https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/reproducible_research.html) — 10.4. Randomness and Seeds; 10.5. Documentation of Experiments; 10.6. Testing Reproducibility.
   Why: The paper can link an evidence package and pass manuscript checks before anyone has established that the package reproduces its key outputs.
   Fix: For a computational paper, document entry point, environment and randomness controls, then record an authorized clean rerun or explain why it could not be done.
2. **Connect citations and artifact identifiers to exact inputs** [map]
   Map nodes: `data.interoperability`, `computation.archival-release`, `computation.software-citation`, `computation.specific-release`, `computation.data-version`, `publication.data-citation`, `publication.data-citation-version`.
   Source: [The FAIR Guiding Principles for scientific data management and stewardship](https://www.nature.com/articles/sdata201618) — I1.
   Source: [Reporting standards and availability of data, materials, code and protocols](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards) — Availability and peer review of computer code and algorithm.
   Source: [Software Citation Principles (Published 2016)](https://force11.org/info/software-citation-principles-published-2016/) — 1. Importance; 6. Specificity.
   Source: [The Turing Way: Version Control for Data](https://book.the-turing-way.org/reproducible-research/vcs/vcs-data) — Importance of Version Controlling Data.
   Source: [Joint Declaration of Data Citation Principles (2014)](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) — 1. Importance; 4. Unique Identification.
   Why: Version and access metadata are encouraged; no explicit mapping binds each reused dataset and software artifact to the exact releasable item supporting the result.
   Fix: Where permitted, require accessible machine-readable formats and persistent, version-specific dataset and software citations.
3. **Check model assumptions and threshold language** [map]
   Map nodes: `analysis.thresholds`, `analysis.model-compatibility`.
   Source: [American Statistical Association Releases Statement on Statistical Significance and P-Values (March 7, 2016; six principles)](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) — 1. P-values can indicate how incompatible the data are with a specified statistical model.; 3. Scientific conclusions and business or policy decisions should not be based only on whether a p-value passes a specific threshold..
   Why: The writing checks guard consistency but do not explicitly ask whether reported assumptions and thresholds support the interpretation of the actual measures.
   Fix: Add an interpretation check that flags unsupported model assumptions or thresholds before human approval.
4. **Add venue-specific release and transfer checks** [map]
   Map nodes: `publication.review-history`, `publication.trial-sharing`.
   Source: [Sending the Manuscript to the Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/sending-the-submission.html) — B. Sending the Manuscript to the Journal.
   Source: [Clinical Trials](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/clinical-trial-registration.html) — 3. Data Sharing.

   Why: The review and availability steps are general, so they do not force an explicit decision about sharing a trial’s materials or carrying reviewer responses over when allowed.
   Fix: Check required sharing fields for eligible trial reports and preserve a permitted transfer record on journal changes.

### Minor

1. **Verify optional author identifiers** [map]
   Map nodes: `manuscript.orcid`.
   Source: [Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — a. Title Page.
   Why: The title-page and authorship checks do not mention author identifiers.
   Fix: During venue metadata review, ask authors to confirm any identifiers supplied for submission.

## Unsourced findings

None.

## Evidence limitations

Read the manuscript workflow, its references and checker interfaces as static evidence; no manuscript, study data, sensitive material, target script or actual submission was used. The example manuscript path is a generated working file.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Intake and route requirements | Evidence inventory and reporting checklist | Outline and draft | SKILL.md:75–160 blocks unsupported claims from the outline. |
| Draft and verify | Manuscript and linked claims | Methods, citations and declarations review | SKILL.md:161–250 checks consistency, confidentiality and provenance. |
| Audit and hand off | Approved draft and issue records | Human author or venue | SKILL.md:264–321 requires human approval; executable rerun not required. |

## Map table

| Node | State | Evidence |
|---|---|---|
| design.* | not-applicable | The underlying study is supplied; no new design or registration. |
| ethics.approval | covered | SKILL.md:38–49,220–234; references/imrad_structure.md:49–52 — verify declarations applicable to the supplied study. |
| ethics.publication-consent | covered | SKILL.md:38–49,220–234; references/imrad_structure.md:49–52 — verify declarations applicable to the supplied study. |
| ethics.privacy | covered | SKILL.md:24–73,202–234 — protects material, prevents invented evidence and checks author and AI declarations. |
| ethics.animal-welfare | not-applicable | No conduct or management of animal experiments. |
| ethics.misconduct | covered | SKILL.md:24–73,202–234 — protects material, prevents invented evidence and checks author and AI declarations. |
| ethics.ai-disclosure | covered | SKILL.md:24–73,202–234 — protects material, prevents invented evidence and checks author and AI declarations. |
| data.discovery | covered | SKILL.md:126–146,220–234; references/research_integrity_open_science.md:21–38 — document provenance, access, terms and metadata in evidence records. |
| data.documentation | covered | SKILL.md:126–146,220–234; references/research_integrity_open_science.md:21–38 — document provenance, access, terms and metadata in evidence records. |
| data.access | covered | SKILL.md:126–146,220–234; references/research_integrity_open_science.md:21–38 — document provenance, access, terms and metadata in evidence records. |
| data.interoperability | shallow | references/research_integrity_open_science.md:21–38 — calls for metadata and access but gives no exchange-format or vocabulary decision. |
| data.reuse-terms | covered | SKILL.md:126–146,220–234; references/research_integrity_open_science.md:21–38 — document provenance, access, terms and metadata in evidence records. |
| data.metadata-retention | covered | SKILL.md:126–146,220–234; references/research_integrity_open_science.md:21–38 — document provenance, access, terms and metadata in evidence records. |
| analysis.methods | covered | SKILL.md:147–200; references/imrad_structure.md:36–85 and references/writing_principles.md:20–80 — reconcile methods and results, show denominators, uncertainty, evidence and limitations. |
| analysis.uncertainty | covered | SKILL.md:147–200; references/imrad_structure.md:36–85 and references/writing_principles.md:20–80 — reconcile methods and results, show denominators, uncertainty, evidence and limitations. |
| analysis.exploration | covered | SKILL.md:147–200; references/imrad_structure.md:36–85 and references/writing_principles.md:20–80 — reconcile methods and results, show denominators, uncertainty, evidence and limitations. |
| analysis.complete-outcomes | covered | SKILL.md:147–200; references/imrad_structure.md:36–85 and references/writing_principles.md:20–80 — reconcile methods and results, show denominators, uncertainty, evidence and limitations. |
| analysis.denominators | covered | SKILL.md:147–200; references/imrad_structure.md:36–85 and references/writing_principles.md:20–80 — reconcile methods and results, show denominators, uncertainty, evidence and limitations. |
| analysis.interpretation | covered | SKILL.md:147–200; references/imrad_structure.md:36–85 and references/writing_principles.md:20–80 — reconcile methods and results, show denominators, uncertainty, evidence and limitations. |
| analysis.model-compatibility | shallow | references/imrad_structure.md:36–72; references/writing_principles.md:20–60 — requires verified methods and uncertainty but not these specific checks on interpretation. |
| analysis.hypothesis-probability | not-applicable | No calculation of hypothesis probability; no standalone inference workflow. |
| analysis.thresholds | shallow | references/imrad_structure.md:36–72; references/writing_principles.md:20–60 — requires verified methods and uncertainty but not these specific checks on interpretation. |
| analysis.transparency | covered | SKILL.md:147–200; references/imrad_structure.md:36–85 and references/writing_principles.md:20–80 — reconcile methods and results, show denominators, uncertainty, evidence and limitations. |
| analysis.evidence | covered | SKILL.md:147–200; references/imrad_structure.md:36–85 and references/writing_principles.md:20–80 — reconcile methods and results, show denominators, uncertainty, evidence and limitations. |
| computation.versions | covered | SKILL.md:94–108,220–234; references/research_integrity_open_science.md:63–77 — organize workspace and record artifacts, environment and restricted access. |
| computation.code-access | covered | SKILL.md:94–108,220–234; references/research_integrity_open_science.md:63–77 — organize workspace and record artifacts, environment and restricted access. |
| computation.review-access | covered | SKILL.md:94–108,220–234; references/research_integrity_open_science.md:63–77 — organize workspace and record artifacts, environment and restricted access. |
| computation.archival-release | shallow | references/research_integrity_open_science.md:21–38,63–77; SKILL.md:126–146 — version and identifiers are recorded, but claim-level pointers to exact archived dependency and data releases are not required. |
| computation.software-citation | shallow | references/research_integrity_open_science.md:21–38,63–77; SKILL.md:126–146 — version and identifiers are recorded, but claim-level pointers to exact archived dependency and data releases are not required. |
| computation.specific-release | shallow | references/research_integrity_open_science.md:21–38,63–77; SKILL.md:126–146 — version and identifiers are recorded, but claim-level pointers to exact archived dependency and data releases are not required. |
| computation.validation | shallow | references/research_integrity_open_science.md:63–77; SKILL.md:177–200,264–283 — manifests and checks support verification but do not require a clean executable rerun and a recorded result. |
| computation.environment | covered | SKILL.md:94–108,220–234; references/research_integrity_open_science.md:63–77 — organize workspace and record artifacts, environment and restricted access. |
| computation.project-layout | covered | SKILL.md:94–108,220–234; references/research_integrity_open_science.md:63–77 — organize workspace and record artifacts, environment and restricted access. |
| computation.data-version | shallow | references/research_integrity_open_science.md:21–38,63–77; SKILL.md:126–146 — version and identifiers are recorded, but claim-level pointers to exact archived dependency and data releases are not required. |
| computation.executable-analysis | shallow | references/research_integrity_open_science.md:63–77; SKILL.md:177–200,264–283 — manifests and checks support verification but do not require a clean executable rerun and a recorded result. |
| computation.randomness | shallow | references/research_integrity_open_science.md:63–77; SKILL.md:177–200,264–283 — manifests and checks support verification but do not require a clean executable rerun and a recorded result. |
| computation.clean-rerun | shallow | references/research_integrity_open_science.md:63–77; SKILL.md:177–200,264–283 — manifests and checks support verification but do not require a clean executable rerun and a recorded result. |
| computation.run-record | shallow | references/research_integrity_open_science.md:63–77; SKILL.md:177–200,264–283 — manifests and checks support verification but do not require a clean executable rerun and a recorded result. |
| computation.artifact-package | covered | SKILL.md:94–108,220–234; references/research_integrity_open_science.md:63–77 — organize workspace and record artifacts, environment and restricted access. |
| reporting.selection | covered | SKILL.md:109–125,252–263; references/reporting_guidelines.md:14–97 — routes by study design and records item-level reporting decisions. |
| reporting.consort | covered | SKILL.md:109–125,252–263; references/reporting_guidelines.md:14–97 — routes by study design and records item-level reporting decisions. |
| reporting.prisma | covered | SKILL.md:109–125,252–263; references/reporting_guidelines.md:14–97 — routes by study design and records item-level reporting decisions. |
| reporting.strobe | covered | SKILL.md:109–125,252–263; references/reporting_guidelines.md:14–97 — routes by study design and records item-level reporting decisions. |
| reporting.arrive | covered | SKILL.md:109–125,252–263; references/reporting_guidelines.md:14–97 — routes by study design and records item-level reporting decisions. |
| reporting.stard | covered | SKILL.md:109–125,252–263; references/reporting_guidelines.md:14–97 — routes by study design and records item-level reporting decisions. |
| reporting.qualitative | covered | SKILL.md:109–125,252–263; references/reporting_guidelines.md:14–97 — routes by study design and records item-level reporting decisions. |
| manuscript.structure | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.title-page | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.orcid | absent | No step specifies verifying author identifiers when the venue supports them. |
| manuscript.funding | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.abstract | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.methods | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.references | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.tables | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.figures | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.authorship | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.acknowledgments | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| manuscript.roles | covered | SKILL.md:147–234,236–250; references/imrad_structure.md:7–105; references/journal_policies.md:47–61 — supplies manuscript structure, declarations and verification steps. |
| publication.journal-article | covered | SKILL.md:220–234,302–321; references/journal_policies.md:5–23,47–61 — checks venue requirements, permitted release and availability statements. |
| publication.submission | covered | SKILL.md:220–234,302–321; references/journal_policies.md:5–23,47–61 — checks venue requirements, permitted release and availability statements. |
| publication.permissions | covered | SKILL.md:220–234,302–321; references/journal_policies.md:5–23,47–61 — checks venue requirements, permitted release and availability statements. |
| publication.review-history | shallow | SKILL.md:285–314 — tracks and answers reviewers, but does not specify carrying the permitted history between venues. |
| publication.data-availability | covered | SKILL.md:220–234,302–321; references/journal_policies.md:5–23,47–61 — checks venue requirements, permitted release and availability statements. |
| publication.trial-sharing | shallow | SKILL.md:220–234; references/journal_policies.md:5–23 — general availability and policy checks; no trial-data sharing fields specified. |
| publication.preprints | covered | SKILL.md:220–234,302–321; references/journal_policies.md:5–23,47–61 — checks venue requirements, permitted release and availability statements. |
| publication.rights | covered | SKILL.md:220–234,302–321; references/journal_policies.md:5–23,47–61 — checks venue requirements, permitted release and availability statements. |
| publication.data-citation | shallow | references/research_integrity_open_science.md:21–38,63–77; SKILL.md:126–146 — version and identifiers are recorded, but claim-level pointers to exact archived dependency and data releases are not required. |
| publication.data-citation-version | shallow | references/research_integrity_open_science.md:21–38,63–77; SKILL.md:126–146 — version and identifiers are recorded, but claim-level pointers to exact archived dependency and data releases are not required. |
| publication.revision-plan | covered | SKILL.md:285–299 — records each request and revision decision, reruns audits and obtains approval. |
| publication.reviewer-response | covered | SKILL.md:285–299 — records each request and revision decision, reruns audits and obtains approval. |

counts: covered 50, shallow 16, absent 1, not-applicable 9, undetermined 0

## Excluded by profile

None.
