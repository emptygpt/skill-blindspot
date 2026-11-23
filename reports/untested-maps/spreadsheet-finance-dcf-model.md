# Blindspot report: dcf-model

Skill under audit: [Anthropic financial-services: dcf-model](https://github.com/anthropics/financial-services/tree/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/vertical-plugins/financial-analysis/skills/dcf-model).

Map: spreadsheet-finance 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Builds a discounted cash flow equity valuation in Excel: data retrieval, historical analysis, projections, WACC, terminal value, equity bridge and sensitivity tables.
- Starts from a company identifier and growth assumptions; ends at a recalculated two-sheet workbook (DCF and WACC) handed to the user.
- Does not promise IFRS statements, a transaction impact analysis or an investment recommendation.

## Step 2 list (before opening the map nodes)

- A three-case model with sensitivity grids depends on every case assumption reaching the projections; traced each scenario assumption to the formulas that use it.
- Valuation sanity checks (terminal value share of EV, terminal growth vs WACC) should use one threshold and run before delivery; compared the thresholds in SKILL.md, TROUBLESHOOTING.md and the validation script.
- The description promises executive summaries; searched the deliverable for them.
- A valuation handed to someone else needs its range and its assumption owners visible; searched for how the output states uncertainty.

## Findings

### Needed

None.

### Worth considering

1. **Make the case margins drive the projections** [trace+map]
   Map nodes: `formulas.constants`, `structure.adaptability`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 14. Avoid using fixed values within formulas.; 8. Design with adaptability in mind to minimise future manual intervention.
   Why: The Bear/Base/Bull blocks set an EBIT margin per year (SKILL.md:382–392, 474–488) and sensitivity table 2 varies it (SKILL.md:363), but the operating expense build writes fixed rates into formulas and labels them correct (SKILL.md:715, 949), and EBIT margin is described as a result of the opex build (SKILL.md:172). As written, changing the case or the margin axis need not move EBIT, which contradicts the rule that only inputs and drivers are hardcoded (SKILL.md:47–48).
   Fix: In Step 4 and Section 4, drive opex or EBIT from the consolidated case column and replace the fixed-rate examples with references to assumption cells.
2. **Use one set of valuation checks and run them** [trace+map]
   Map nodes: `checks.built-in`, `checks.evaluate`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 17. Build in checks, controls, and alerts from the outset.
   Source: [Evaluate a nested formula one step at a time](https://support.microsoft.com/en-us/excel/evaluate-a-nested-formula-one-step-at-a-time) — Select Evaluate to examine the value of the underlined reference.
   Why: The terminal value share of EV is 50–70% at SKILL.md:310 and 1261, a warning above 75% at 311, above 80% at 743, and 40–80% in scripts/validate_dcf.py:216–221; SKILL.md never runs that script. Checks are a list of spot checks (SKILL.md:1147, 1234–1235), with no check cells left in the workbook.
   Fix: State one threshold, run scripts/validate_dcf.py (or add equivalent check cells for TV share, g < WACC and the equity bridge) after recalculation, and fix what it flags before delivery.
3. **Deliver or drop the promised executive summary** [trace+map]
   Map nodes: `reporting.results`.
   Source: [Financial and Investment Analysts (13-2051.00), Job Duties Custom List](https://www.onetonline.org/search/task/choose/13-2051.00) — Task ID 21600: Present oral or written reports on general economic trends, individual corporations, and entire industries.
   Why: The description promises Excel models with executive summaries; the deliverable is a DCF sheet and a WACC sheet (SKILL.md:795, 1135) and no step writes a summary of value, range and key drivers.
   Fix: Add a summary block or sheet with implied price, the Bear/Base/Bull range and the top drivers, or remove the promise from the description.
4. **Show the valuation range and who set the assumptions** [map]
   Map nodes: `ethics.objectivity`, `ethics.misrepresentation`.
   Source: [Code of Ethics and Standards of Professional Conduct](https://www.cfainstitute.org/standards/professionals/code-ethics-standards) — Standard I(B) Independence and Objectivity; Standard I(C) Misrepresentation.
   Why: Growth rates can come from the user or consensus (SKILL.md:782), and SKILL.md:1153 asks to flag uncertainties without saying where; the output leads with one implied price per share (SKILL.md:327).
   Fix: Next to the implied price, show the case and sensitivity range and note which assumptions came from the user, consensus or the model.
5. **Constrain the case selector** [map]
   Map nodes: `inputs.validation`, `inputs.messages`.
   Source: [More on data validation](https://support.microsoft.com/en-us/excel/more-on-data-validation) — When is data validation useful?; Data Validation Input and Error Messages.
   Why: Every case formula keys off one selector cell, but its allowed values are only checked after a failure (TROUBLESHOOTING.md:37); no data validation or message is set on it.
   Fix: Add list validation (1, 2, 3) with an input message on the selector cell when building Section 3.

### Minor

1. **Say where results are rounded** [map]
   Map nodes: `formulas.rounding`.
   Source: [ROUND function](https://support.microsoft.com/en-us/excel/functions/round-function) — The ROUND function rounds a number to a specified number of digits.
   Why: Formats show per-share values to cents (SKILL.md:900), but nothing says whether the share price or bridge is rounded in calculation or only in display.
2. **Document use, audience and versions in the workbook** [map]
   Map nodes: `purpose.audience`, `structure.guidance`, `controls.backup-version`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 6. Tailor the design and documentation to the needs of the audience and dependent processes.; 7. Make the spreadsheet easy to use, providing supporting guidance where helpful.; 19. Ensure there is a regular process of backup and version control. This minimises loss of work and avoids the use of the wrong version.
   Why: The model aims to be client-ready (SKILL.md:615) and versions are saved (SKILL.md:1159), but who uses the model, how to switch cases and which file is current are not written into the workbook.
3. **Interpret the ratios the history computes** [map]
   Map nodes: `analysis.ratios`.
   Source: [Financial Analysis Techniques (2026 refresher reading, public overview)](https://www.cfainstitute.org/insights/professional-learning/refresher-readings/2026/financial-analysis-techniques) — calculate and interpret activity, liquidity, solvency, and profitability ratios;
   Why: Step 2 lists return metrics (SKILL.md:116) but does not say how they inform the projections.
4. **Check user-provided data before sharing** [map]
   Map nodes: `ethics.confidentiality`.
   Source: [Code of Ethics and Standards of Professional Conduct](https://www.cfainstitute.org/standards/professionals/code-ethics-standards) — Standard III(E) Preservation of Confidentiality.
   Why: User-provided financials and estimates (SKILL.md:1244) go into cell comments and the model with no check of what may leave with the file.

## Unsourced findings

None.

## Evidence limitations

Recalculation uses recalc.py, which is not in this skill folder; its checks were not read, so formulas.errors rests on the stated rule only. scripts/validate_dcf.py was read for its thresholds only and was not run. No model was built.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Retrieve and validate data | Historical inputs, market data | Projections, WACC, equity bridge | SKILL.md:93–107; user confirms raw inputs. |
| Case blocks and consolidation column | Per-year case drivers incl. EBIT margin | Projections and sensitivity grids | SKILL.md:372–409; opex examples use fixed rates, so the margin driver is not traced to EBIT. |
| FCF, WACC, discounting, terminal value | EV, equity value, implied price | Sensitivity tables, user | SKILL.md:175–356; TV thresholds differ across files. |
| Sensitivity tables | Three 5×5 grids | User | SKILL.md:358–366, 531–594; center cell equals base case. |
| Recalculate and deliver | Two-sheet workbook | User | SKILL.md:81–83; validate_dcf.py not run. |

## Map table

| Node | State | Evidence |
|---|---|---|
| purpose.question | covered | SKILL.md:3 "Use when users need to value a company"; SKILL.md:782 "Revenue growth rates for projection period" |
| purpose.audience | shallow | SKILL.md:615 — "Not professional or client-ready" names the bar, not the users or downstream needs. |
| purpose.tool-fit | covered | SKILL.md:21 "If running inside Excel (Office Add-in / Office JS environment):"; SKILL.md:22 "If generating a standalone .xlsx file (no live Excel session):" |
| purpose.risk | not-applicable | No assurance or criticality assessment in scope. |
| purpose.competence | not-applicable | No staffing or training of model users in scope. |
| inputs.quality | covered | SKILL.md:103 "Verify net debt vs net cash (critical for valuation)"; SKILL.md:105 "Validate historical margins are consistent with business model" |
| inputs.assumptions | covered | SKILL.md:1150 — "Explain reasoning behind key inputs" |
| inputs.validation | shallow | TROUBLESHOOTING.md:37 — "Verify case selector cell contains 1, 2, or 3" after failure; no validation rule. |
| inputs.messages | absent | No input or error messages on input cells. |
| inputs.inherited-validation | not-applicable | Builds a new model; no inherited workbook. |
| inputs.sourcing | covered | SKILL.md:70 "Every blue input must have a comment"; SKILL.md:97 "Data Sources Priority:" |
| structure.flow | covered | SKILL.md:923 "Section 2: Market Data (NOT case dependent)"; SKILL.md:932 "Section 3: DCF Scenario Assumptions"; SKILL.md:995 "Section 6: Discounting & Valuation" |
| structure.layout | covered | SKILL.md:87 — "Show assumptions horizontally across projection years within each block" |
| structure.adaptability | shallow | SKILL.md:48 — "The model must flex when the user changes an assumption." Fixed-rate opex formulas do not flex with the case. |
| structure.conventions | covered | SKILL.md:873 — "Font color tells you WHAT it is (input/formula/link)." |
| structure.guidance | shallow | SKILL.md:1152 — "Describe any non-standard approaches" without a place in the workbook or operating notes. |
| formulas.consistent | covered | SKILL.md:993 "Test one column, then copy across."; SKILL.md:1145 "Similar calculations follow similar patterns" |
| formulas.simple | covered | SKILL.md:409 — "The consolidation column approach centralizes logic" |
| formulas.constants | shallow | SKILL.md:47 "The only hardcoded numbers permitted are" yet SKILL.md:715 "=E29*0.15" is marked correct. |
| formulas.reuse | covered | SKILL.md:560 — "Reference the main DCF calculation but substitute these values." |
| formulas.references | covered | SKILL.md:89 — "Verify formulas reference correct scenario block cells" |
| formulas.sheet-changes | covered | SKILL.md:654 — "Lock row layout FIRST, then write formulas" |
| formulas.function-use | covered | SKILL.md:531 — "Do not use Excel's Data Table feature" |
| formulas.errors | covered | SKILL.md:83 — "Zero formula errors required" |
| formulas.rounding | absent | Display formats only; no calculation rounding rule. |
| checks.built-in | shallow | SKILL.md:1147 — "Sum checks and balance checks where applicable" with no check cells specified. |
| checks.test | covered | SKILL.md:1144 "Enter sample numbers to verify formulas"; SKILL.md:1235 "Change case selector - does the consolidation column update properly?" |
| checks.peer-review | covered | SKILL.md:1158 — "Have someone else check formulas" |
| checks.evaluate | shallow | SKILL.md:1234 "Test one FCF formula"; SKILL.md:1234 "does it reference the correct assumption rows?" Spot check only. |
| scenarios.cases | covered | SKILL.md:86 — "Create separate blocks for Bear/Base/Bull cases" |
| scenarios.sensitivity | covered | SKILL.md:362 — "Shows enterprise value sensitivity to discount rate and perpetuity growth" |
| scenarios.target | not-applicable | No target-result solve requested. |
| scenarios.forecast | covered | SKILL.md:137 "Growth Rate Framework:"; SKILL.md:143 "Revenue(Year N) = Revenue(Year N-1) × (1 + Growth Rate)" |
| analysis.impact | not-applicable | No transaction or decision impact analysis. |
| analysis.valuation | covered | SKILL.md:251 "Cash flows assumed to occur mid-year"; SKILL.md:327 "Implied Price per Share" |
| analysis.ratios | shallow | SKILL.md:116 — "ROIC, ROE trends" listed without interpretation. |
| analysis.comparisons | covered | SKILL.md:106 — "Cross-check revenue growth rates with industry benchmarks" |
| analysis.statements | not-applicable | Uses filed statements; prepares none. |
| analysis.ifrs18 | not-applicable | No IFRS statement preparation. |
| reporting.charts | not-applicable | No charts in the specified deliverable. |
| reporting.formats | covered | SKILL.md:900 — "ALWAYS specify units in headers" |
| reporting.results | shallow | SKILL.md:3 "outputs professional Excel models with executive summaries" vs SKILL.md:795 "Main valuation model with sensitivity analysis at bottom" |
| reporting.disclosure | not-applicable | No IFRS reporting output. |
| controls.backup-version | shallow | SKILL.md:1159 — "Save versions as work progresses" without naming or a current-version rule. |
| controls.protection | not-applicable | No shared or governed workbook deployment. |
| ethics.objectivity | absent | Nothing on who sets assumptions or keeping them independent of a wanted price. |
| ethics.misrepresentation | shallow | SKILL.md:1153 — "Highlight areas with limited visibility" without saying where the output shows it. |
| ethics.confidentiality | absent | Nothing on user-provided data leaving with the file. |
| ethics.records | covered | SKILL.md:69 — "Source: [System/Document], [Date], [Reference], [URL if applicable]" |

counts: covered 24, shallow 11, absent 4, not-applicable 10, undetermined 0

## Excluded by profile

None.
