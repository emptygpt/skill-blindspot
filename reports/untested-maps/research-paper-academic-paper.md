# Blindspot report: academic-paper

Skill under audit: [academic-paper](https://github.com/Imbad0202/academic-research-skills/tree/d103b1005bb8c9f7a597e6a7ed473b75dcf8830e/academic-paper), part of Academic Research Skills (CC BY-NC 4.0).

Map: research-paper 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Multi-agent pipeline that plans, drafts, reviews, revises and formats an academic paper in several disciplines, with citation checking, AI-use disclosure and reviewer-response modes.
- Ends at a formatted manuscript with required statements, cover letter and, in revision modes, a revision roadmap and response letter.
- Does not design or run the study (methodology and preregistration arrive from deep-research), run analyses beyond figure code, or submit the paper.

## Step 2 list (before opening the map nodes)

- Reporting checklist for the study design (CONSORT, PRISMA, STROBE and similar) chosen and checked.
- Preregistration or trial registration carried into Methods.
- Effect sizes, intervals and careful p-value wording in Results.
- Code availability and software versions, not just data availability.
- Author identifiers, affiliations and corresponding author.
- Preprint posting and prior versions disclosed.
- Licence or copyright transfer.
- Permission for reused figures and tables.
- De-identification of participants in text, tables and figures.
- Text recycling and image manipulation checks.
- Dataset and software citations with versions.
- Prior reviews carried to a new venue after rejection.

## Findings

### Needed

None.

### Worth considering

1. **Select and check a study-design reporting guideline** [model+map]

   Map nodes: `reporting.selection`, `reporting.consort`, `reporting.prisma`, `reporting.strobe`, `reporting.arrive`, `reporting.stard`, `reporting.qualitative`, `ethics.animal-welfare`, `publication.trial-sharing`.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — 2. Reporting Guidelines.
   Source: [EQUATOR Network: Reporting Guidelines](https://www.equator-network.org/) — CONSORT; PRISMA; STROBE; ARRIVE; STARD; SRQR.
   Source: [ICMJE: Clinical Trials](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/clinical-trial-registration.html) — 3. Data Sharing.
   Why: The skill offers medicine and other empirical disciplines and makes five statements mandatory. deep-research partly covers this: its research_architect_agent (§7 Reporting Standards, deep-research/agents/research_architect_agent.md:124–131, 223) writes a recommended guideline into the Methodology Blueprint, which academic-paper's intake reads at handoff (agents/intake_agent.md:32). Gaps remain: intake carries only the method from the blueprint (agents/intake_agent.md:55), not the guideline; no phase checks the draft against the checklist; and a cold start without a blueprint never selects one. The full-mode compliance check is RAISE for AI use, not a design checklist.
   Fix: In agents/intake_agent.md, carry the blueprint's recommended guideline forward or ask for one in the Phase 0 interview, then have peer_reviewer_agent check the draft against its items before formatting.
2. **Code, software and dataset identification** [model+map]

   Map nodes: `computation.versions`, `computation.code-access`, `computation.review-access`, `computation.software-citation`, `computation.specific-release`, `computation.randomness`, `publication.data-citation`, `publication.data-citation-version`.
   Source: [Nature Portfolio: Reporting standards and availability of data, materials, code and protocols](https://www.nature.com/nature-portfolio/editorial-policies/reporting-standards) — Availability and peer review of computer code and algorithm.
   Source: [Software Citation Principles (2016)](https://force11.org/info/software-citation-principles-published-2016/) — 1. Importance; 6. Specificity.
   Source: [Joint Declaration of Data Citation Principles (2014)](https://force11.org/info/joint-declaration-of-data-citation-principles-final/) — 1. Importance; 4. Unique Identification.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — iii. Statistics.
   Source: [Reproducible Research, Kempner Institute Computing Handbook](https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/reproducible_research.html) — 10.4. Randomness and Seeds.
   Why: Data availability is mandatory with four templates, but code appears only as optional supplementary material, the Methods template asks which software without versions, and no guide asks to cite datasets or software as references or to state seeds.
   Fix: Add a Code Availability Statement next to the Data Availability Statement in the mandatory list in SKILL.md, and extend the Data Analysis prompt in templates/imrad_template.md to software versions, seeds and dataset and software citations.
3. **Generated figure code is called runnable but is not rerun** [trace+map]

   Map nodes: `computation.clean-rerun`.
   Source: [Reproducible Research, Kempner Institute Computing Handbook](https://handbook.eng.kempnerinstitute.harvard.edu/s2_swe_for_research/reproducible_research.html) — 10.6. Testing Reproducibility.
   Why: visualization_agent states its code runs without modification and its quality step compares plotted values with the source, but no step executes the script in a fresh environment before the figure enters the paper.
   Fix: In Step 6 of agents/visualization_agent.md, run the generated script in a clean environment and compare its output with the figure, or mark the figure as not rerun.
4. **Report all prespecified outcomes and label exploratory analyses** [model+map]

   Map nodes: `analysis.complete-outcomes`, `analysis.exploration`, `analysis.transparency`, `analysis.denominators`.
   Source: [ICMJE: Preparing a Manuscript for Submission to a Medical Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html) — e. Results; iii. Statistics.
   Source: [ASA Statement on Statistical Significance and P-Values (2016)](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) — 4. Proper inference requires full reporting and transparency.
   Why: A preregistration artifact is validated and carried through handoffs, but no drafting or review rule compares reported outcomes with it, labels unplanned analyses or reports deviations; sample size is asked for, but not counts behind percentages.
   Fix: In agents/draft_writer_agent.md, when a preregistration artifact is present, require each registered outcome in Results, a label on unplanned analyses and a deviations paragraph.
5. **P-value wording beyond notation** [map]

   Map nodes: `analysis.model-compatibility`, `analysis.hypothesis-probability`, `analysis.thresholds`.
   Source: [ASA Statement on Statistical Significance and P-Values (2016)](https://www.amstat.org/asa/files/pdfs/p-valuestatement.pdf) — principles 1 to 3.
   Why: The APA guide requires exact p values, effect sizes and intervals, which is good; but the Chinese register rules suggest wording such as reaching statistical significance, and no rule warns against threshold-only conclusions or reading p as the probability a hypothesis is true.
   Fix: Add a short p-value interpretation rule to references/academic_writing_style.md and replace the threshold wording example in agents/draft_writer_agent.md.
6. **Participant privacy, consent to publish and reused material** [model+map]

   Map nodes: `ethics.privacy`, `ethics.publication-consent`, `publication.permissions`.
   Source: [ICMJE: Protection of Research Participants](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/protection-of-research-participants.html) — E. Protection of Research Participants.
   Source: [ICMJE: Sending the Manuscript to the Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/sending-the-submission.html) — B. Sending the Manuscript to the Journal.
   Why: The ethics section asks for approval, consent and data protection as one line; nothing checks quotes, case details or images for identifiable people, asks for consent to publish them, or asks for permission when a figure is adapted from another work.
   Fix: Add identifiability, consent-to-publish and reuse-permission items to the required-sections checklist in agents/formatter_agent.md.

### Minor

1. **Preprints and publication licence** [model+map]

   Map nodes: `publication.preprints`, `publication.rights`.
   Source: [ICMJE: Overlapping Publications](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/overlapping-publications.html) — 3. Preprints.
   Source: [ICMJE: Copyright](https://www.icmje.org/recommendations/browse/publishing-and-editorial-issues/copyright.html) — C. Copyright.
   Why: The cover letter template says the work is not published elsewhere, with no prompt to disclose a preprint of the same paper; licence choice comes up only as open-access fees in the funding guide.
2. **Prior reviews after a rejection** [map]

   Map nodes: `publication.review-history`.
   Source: [ICMJE: Sending the Manuscript to the Journal](https://www.icmje.org/recommendations/browse/manuscript-preparation/sending-the-submission.html) — B. Sending the Manuscript to the Journal.
   Why: Desk-reject recovery picks alternative journals and revision-coach lists transfer after review as a scope, but no step decides whether to send earlier reviews and replies to the new venue.

## Unsourced findings

None.

## Evidence limitations

Read SKILL.md and the agents/, references/ and templates/ files it routes to; examples/ were used only to understand intent, not as evidence. The helper listed 119 referenced paths outside the skill folder (shared/, academic-pipeline/, deep-research/, docs/); in the full repository at the pinned commit, shared/agents/compliance_agent.md and academic-pipeline/agents/integrity_verification_agent.md were searched for reporting guidelines and data or software citation and add none. deep-research/agents/research_architect_agent.md:124–131 and :223 recommend a reporting guideline in the Methodology Blueprint that intake reads at handoff; this is why the reporting-guideline finding is Worth considering rather than Needed. The other outside paths were not read, so evidence there could change absent rows for reporting checklists and citations.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Phase 0 intake | Paper Configuration Record, validated preregistration sidecar | All later phases | SKILL.md:208 requires user confirmation; the sidecar is carried but no later rule reads its outcomes (Worth considering 4). |
| Drafting and visualization | Draft, figure code, captions | Citation check, peer review | agents/visualization_agent.md:17 calls the code runnable; no step runs it (Worth considering 3). |
| Citation check and peer review, max 2 rounds | Flagged citations, review verdict, Acknowledged Limitations | Formatter | SKILL.md:210 caps loops and routes leftovers to the limitations section. |
| Formatting | Manuscript, required statements, cover letter | User | agents/formatter_agent.md:65 delivers the package; statements follow the SKILL.md:641 list. |

## Map table

| Node | State | Evidence |
|---|---|---|
| design.* | not-applicable | The study design arrives from deep-research; this skill writes it up. |
| ethics.approval | covered | SKILL.md:641 "Every paper MUST include: Data Availability Statement, Ethics Declaration"; templates/imrad_template.md:112 "[IRB approval, informed consent, data protection.]" |
| ethics.publication-consent | absent | No consent to publish identifiable material. |
| ethics.privacy | shallow | templates/imrad_template.md:112 "[IRB approval, informed consent, data protection.]" — no check of text, tables or figures for identifiable people. |
| ethics.animal-welfare | absent | No animal-research statement or ARRIVE. |
| ethics.misconduct | covered | SKILL.md:605 "Every citation must be verified via DOI or WebSearch"; agents/citation_compliance_agent.md:146 "Unacceptable: recycling results, discussion, or conclusions from prior publications" |
| ethics.ai-disclosure | covered | SKILL.md:642 "normal `full` / `format-convert` flows include the existing generic AI tool-usage statement" |
| data.* | not-applicable | Data collection, curation and deposit happen outside the skill; the availability statement is under publication. |
| analysis.methods | covered | templates/imrad_template.md:104 "[What analytical methods were applied? Software used?]" |
| analysis.uncertainty | covered | references/apa7_extended_guide.md:160 "Effect sizes: always report"; references/apa7_extended_guide.md:161 "Confidence intervals: 95% CI [lower, upper]" |
| analysis.exploration | shallow | agents/intake_agent.md:45 "Carry the validated" — the preregistration sidecar is carried, but no rule labels exploratory analyses. |
| analysis.complete-outcomes | absent | No rule to report every prespecified outcome. |
| analysis.denominators | shallow | templates/imrad_template.md:92 "Sample size and characteristics." — no counts behind percentages. |
| analysis.interpretation | covered | agents/draft_writer_agent.md:295 "Present an inference or hypothesis only when it follows from identified evidence and is explicitly distinguished from an observed finding"; SKILL.md:643 "explicitly discuss study limitations" |
| analysis.model-compatibility | absent | Only p-value notation rules. |
| analysis.hypothesis-probability | absent | Only p-value notation rules. |
| analysis.thresholds | absent | agents/draft_writer_agent.md:214 suggests significance-threshold wording; no rule against threshold-only conclusions. |
| analysis.transparency | shallow | references/apa7_extended_guide.md:159 "Report exact" p values — no requirement to report all analyses run. |
| analysis.evidence | covered | references/apa7_extended_guide.md:160 "Effect sizes: always report"; references/academic_writing_style.md:74 "RR = 0.60, 95% CI [0.45, 0.80], p = .001" |
| computation.versions | shallow | templates/imrad_template.md:104 "Software used?" — no versions. |
| computation.code-access | shallow | references/journal_submission_guide.md:37 "Data, code, extended analyses" — optional supplementary material, not a code availability statement. |
| computation.review-access | absent | No code access for reviewers. |
| computation.archival-release | not-applicable | Depositing code happens outside the skill. |
| computation.software-citation | absent | No instruction to cite software. |
| computation.specific-release | absent | No software versions in citations. |
| computation.validation | not-applicable | Validating the study's analysis code is outside a writing pipeline. |
| computation.environment | not-applicable | The study's analysis environment is outside the skill. |
| computation.project-layout | not-applicable | No research compendium is organized. |
| computation.data-version | not-applicable | Preserving inputs happens in the analysis; stating versions is under the citation nodes. |
| computation.executable-analysis | covered | agents/visualization_agent.md:17 "generated code is self-contained, commented, and runnable without modification" |
| computation.randomness | absent | No seeds or nondeterminism reporting. |
| computation.clean-rerun | shallow | agents/visualization_agent.md:401 "confirm plotted values match source" — the figure code is not rerun in a clean environment. |
| computation.run-record | not-applicable | Run records belong to the study's analysis. |
| computation.artifact-package | not-applicable | No analysis artifact package is produced. |
| reporting.selection | shallow | references/writing_judgment_framework.md:34 "Adherence to reporting guidelines" — a register note in this skill. deep-research/agents/research_architect_agent.md:223 puts a recommended guideline in the Methodology Blueprint that agents/intake_agent.md:32 reads, but intake extracts only the method (agents/intake_agent.md:55) and no phase checks the draft against the guideline. |
| reporting.consort | absent | No CONSORT. |
| reporting.prisma | shallow | SKILL.md:424 "its protocol and reporting checklist (PRISMA-ScR for a scoping review) stay with the author" — PRISMA appears for AI-use disclosure and scoping reviews only. |
| reporting.strobe | absent | No STROBE. |
| reporting.arrive | absent | No ARRIVE. |
| reporting.stard | absent | No STARD. |
| reporting.qualitative | absent | No SRQR or COREQ, although case-study and qualitative templates exist. |
| manuscript.structure | covered | references/paper_structure_patterns.md:29 "5. Methodology"; references/paper_structure_patterns.md:37 "6. Results/Findings" |
| manuscript.title-page | covered | references/journal_submission_guide.md:30 "Title, authors, affiliations, corresponding author" |
| manuscript.orcid | covered | agents/formatter_agent.md:869 "include ORCID, corresponding author mark, equal contribution statement" |
| manuscript.funding | covered | SKILL.md:641 "Conflict of Interest Statement, Funding Acknowledgment." |
| manuscript.abstract | covered | templates/bilingual_abstract_template.md:28 "Include specific details, numbers, or effect sizes where applicable."; agents/formatter_agent.md:136 "Abstract word limit" |
| manuscript.methods | covered | templates/imrad_template.md:96 "[What data were collected? How? When? By whom?]" |
| manuscript.references | covered | agents/citation_compliance_agent.md:32 "match in-text citations to reference-list entries and vice versa"; agents/citation_compliance_agent.md:34 "every source with a DOI must include it" |
| manuscript.tables | covered | references/apa7_extended_guide.md:129 "Descriptive Title in Italic Title Case"; references/apa7_extended_guide.md:137 "Note. General note. Specific note for a column or cell." |
| manuscript.figures | covered | references/statistical_visualization_standards.md:15 "Figures must be interpretable without reading the text" |
| manuscript.authorship | covered | references/credit_authorship_guide.md:143 "All four conditions must be met" |
| manuscript.acknowledgments | covered | references/credit_authorship_guide.md:154 "should be listed in the Acknowledgments" |
| manuscript.roles | covered | agents/formatter_agent.md:873 "CRediT Author Statement -> use 14 contribution role assignments" |
| publication.journal-article | covered | SKILL.md:3 "12-agent academic paper writing pipeline." |
| publication.submission | covered | agents/formatter_agent.md:65 "deliver all required files (main text, bibliography, figures, cover letter)" |
| publication.permissions | shallow | agents/visualization_agent.md:153 "Adapted from" — attribution in a caption example; no permission step. |
| publication.review-history | shallow | references/mode_selection_guide.md:193 "transfer-after-review" — listed as a scope, with no step on passing earlier reviews to the new venue. |
| publication.data-availability | covered | SKILL.md:641 "Every paper MUST include: Data Availability Statement"; agents/formatter_agent.md:874 "Data Availability Statement -> choose from 4 templates" |
| publication.trial-sharing | absent | No trial registration or data-sharing statement. |
| publication.preprints | absent | No preprint disclosure for the paper itself. |
| publication.rights | absent | No licence or copyright step. |
| publication.data-citation | absent | No instruction to cite datasets. |
| publication.data-citation-version | absent | No dataset identifiers or versions. |
| publication.revision-plan | covered | references/mode_selection_guide.md:190 "Want a Revision Roadmap that classifies, maps, and prioritizes each comment" |
| publication.reviewer-response | covered | templates/revision_tracking_template.md:134 "We have carefully addressed all comments and provide point-by-point" |

counts: covered 25, shallow 11, absent 20, not-applicable 20, undetermined 0

## Excluded by profile

None.
