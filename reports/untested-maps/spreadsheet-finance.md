# Blindspot report: xlsx

Skill under audit: [xlsx](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx).

Map: spreadsheet-finance 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Creates, repairs, reformats and checks spreadsheets; financial models are a named route with conventions.
- Starts with the requested workbook/spec, ends at workbook handoff with formula checks.
- Does not promise a valuation, financial statement filing or investment decision as a separate deliverable.

## Step 2 list (before opening the map nodes)

- Prototype formulas and recalc are explicit; searched checks and financial model guidance for an independent sampled result check after filling the grid and for named stress cases.

## Findings

### Needed

None.

### Worth considering

1. **Check correctness after expanding the model** [model+map+trace]
   Map nodes: `checks.test`, `checks.evaluate`, `checks.built-in`, `scenarios.cases`, `formulas.rounding`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 17. Build in checks, controls, and alerts from the outset.; 18. Test and review to reduce the risk of error and identify inefficiencies..
   Source: [Evaluate a nested formula one step at a time](https://support.microsoft.com/en-us/excel/evaluate-a-nested-formula-one-step-at-a-time) — Select Evaluate to examine the value of the underlined reference..

   Source: [Introduction to What-If Analysis](https://support.microsoft.com/en-us/excel/introduction-to-what-if-analysis) — Use scenarios to consider many different variables.
   Source: [ROUND function](https://support.microsoft.com/en-us/excel/functions/round-function) — The ROUND function rounds a number to a specified number of digits..
   Why: SKILL.md:48–50 checks a small prototype; recalculation reports errors, not whether the final filled ranges or assumptions produce correct outputs.
   Fix: Before handoff, compare sample final outputs against independent expected values, exercise base and stressed inputs when scenarios exist, and define where rounding is applied.
2. **Validate input cells and source values** [map]
   Map nodes: `inputs.quality`, `inputs.validation`, `inputs.messages`, `inputs.inherited-validation`, `structure.flow`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 10. Seek to control, clean, and optimise data quality and structure prior to using them.; 9. Structure workbooks with a clear flow of inputs, processes, and outputs..
   Source: [More on data validation](https://support.microsoft.com/en-us/excel/more-on-data-validation) — Data Validation Input and Error Messages; How to update or remove data validation in an inherited workbook; When is data validation useful?.
   Why: The workbook has designated inputs and example values; it need not reject inputs that can silently distort formulas.
   Fix: For a fillable model, verify source bounds and existing validation, add constraints and useful messages where appropriate, and trace one input through the resulting output.
3. **Protect workbook edits against hard-to-spot loss** [map]
   Map nodes: `formulas.sheet-changes`, `controls.backup-version`.
   Source: [Overview of formulas in Excel](https://support.microsoft.com/en-us/excel/get-started/overview-of-formulas-in-excel) — What occurs when you move, copy, insert, or delete worksheets.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 19. Ensure there is a regular process of backup and version control. This minimises loss of work and avoids the use of the wrong version..
   Why: Saved edits may preserve formulas but disrupt cross-sheet dependencies or unsupported objects; the recalculation copy serves a different purpose.
   Fix: Retain a restorable original and compare affected formulas and workbook features before delivering the edited file.
4. **Check charts as communication, not only as workbook objects** [map]
   Map nodes: `reporting.charts`.
   Source: [Financial and Investment Analysts (13-2051.00), Job Duties Custom List](https://www.onetonline.org/search/task/choose/13-2051.00) — Task ID 21589: Draw charts and graphs, using computer spreadsheets, to illustrate technical reports..
   Why: Chart properties avoid file repair failures but do not check whether chart form, units or labels match the analytical point.
   Fix: When charting, review the rendered chart against its source range and intended comparison.
5. **Check what a workbook exposes before sharing** [map]
   Map nodes: `ethics.confidentiality`.
   Source: [Code of Ethics and Standards of Professional Conduct](https://www.cfainstitute.org/standards/professionals/code-ethics-standards) — Standard III(E) Preservation of Confidentiality.
   Why: Spreadsheet editing can carry forward hidden worksheets, comments or values irrelevant to the recipient.
   Fix: When the requested handoff is to a different audience, confirm it is authorized to receive the workbook contents, including hidden data.


### Minor

None.

## Unsourced findings

None.

## Evidence limitations

Reviewed documented authoring steps and the recalculation path as static evidence; no workbook, financial result or helper execution was part of this audit.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Select operation and tool | Workbook requirements and chosen library | Create or edit | SKILL.md:9–28 ties operations to workbook constraints. |
| Build and prototype | Workbook and sampled formulas | Final recalculation | SKILL.md:48–50 checks a small subset before expansion. |
| Recalculate and deliver | Formula error report and saved workbook | User | SKILL.md:40–58 checks errors; no independent final sampling. |

## Map table

| Node | State | Evidence |
|---|---|---|
| purpose.question | covered | SKILL.md:3,9–14,25 — spreadsheet-only deliverable, tool selection by operation and exact workbook requirements. |
| purpose.audience | not-applicable | Implements the specified artifact; no business case, fitness opinion or assurance engagement. |
| purpose.tool-fit | covered | SKILL.md:3,9–14,25 — spreadsheet-only deliverable, tool selection by operation and exact workbook requirements. |
| purpose.risk | not-applicable | Implements the specified artifact; no business case, fitness opinion or assurance engagement. |
| purpose.competence | not-applicable | Implements the specified artifact; no business case, fitness opinion or assurance engagement. |
| inputs.quality | shallow | SKILL.md:3,9–14 — names cleanup and workbook reads but no general check of source values. |
| inputs.assumptions | covered | SKILL.md:26,98–100 — labels assumptions and records source or user provenance. |
| inputs.validation | shallow | SKILL.md:27–28 — shows users what to enter and preserves existing workbook conventions but does not specify constraints, invalid entries or checks of existing rules. |
| inputs.messages | shallow | SKILL.md:27–28 — shows users what to enter and preserves existing workbook conventions but does not specify constraints, invalid entries or checks of existing rules. |
| inputs.inherited-validation | shallow | SKILL.md:27–28 — shows users what to enter and preserves existing workbook conventions but does not specify constraints, invalid entries or checks of existing rules. |
| inputs.sourcing | covered | SKILL.md:26,98–100 — labels assumptions and records source or user provenance. |
| structure.flow | shallow | SKILL.md:89–100 — distinguishes assumptions and formulas, but lacks an input-to-output layout check. |
| structure.layout | covered | SKILL.md:22,27–28,85–100 — formatting conventions and an input legend for fillable files. |
| structure.adaptability | covered | SKILL.md:24,98–100 — linked assumptions let output respond to edits. |
| structure.conventions | covered | SKILL.md:22,27–28,85–100 — formatting conventions and an input legend for fillable files. |
| structure.guidance | covered | SKILL.md:22,27–28,85–100 — formatting conventions and an input legend for fillable files. |
| formulas.consistent | covered | SKILL.md:24,60–67,77,98–100 — use spreadsheet expressions and compatible functions, with separate and consistent inputs. |
| formulas.simple | covered | SKILL.md:24,60–67,77,98–100 — use spreadsheet expressions and compatible functions, with separate and consistent inputs. |
| formulas.constants | covered | SKILL.md:24,60–67,77,98–100 — use spreadsheet expressions and compatible functions, with separate and consistent inputs. |
| formulas.reuse | not-applicable | No model-library or cross-workbook reuse workflow. |
| formulas.references | covered | SKILL.md:24,60–67,77,98–100 — use spreadsheet expressions and compatible functions, with separate and consistent inputs. |
| formulas.sheet-changes | shallow | SKILL.md:28,75–80 — guards several unsafe edits without a general dependency review. |
| formulas.function-use | covered | SKILL.md:24,60–67,77,98–100 — use spreadsheet expressions and compatible functions, with separate and consistent inputs. |
| formulas.errors | covered | SKILL.md:23,30–58; scripts/recalc.py:455–489 — formula recalculation and typed errors before handoff. |
| formulas.rounding | absent | No rule distinguishes display precision from computational rounding. |
| checks.built-in | absent | No workbook reconciliation or invariant check separate from error evaluation. |
| checks.test | shallow | SKILL.md:40–58 — checks initial formulas and final evaluation errors; a clean but wrong result can still ship. |
| checks.peer-review | not-applicable | Ends with local handoff; no independent reviewer assigned. |
| checks.evaluate | shallow | SKILL.md:40–58 — checks initial formulas and final evaluation errors; a clean but wrong result can still ship. |
| scenarios.cases | shallow | SKILL.md:89,98–100 — labels case inputs but does not run named cases. |
| scenarios.sensitivity | not-applicable | No substantive forecasting or investment analysis required from the authoring tool. |
| scenarios.target | not-applicable | No substantive forecasting or investment analysis required from the authoring tool. |
| scenarios.forecast | not-applicable | No substantive forecasting or investment analysis required from the authoring tool. |
| analysis.* | not-applicable | No substantive forecasting or investment analysis required from the authoring tool. |
| reporting.charts | shallow | SKILL.md:82–83 — ensures chart options work, not that the visual fits the data. |
| reporting.formats | covered | SKILL.md:81,93–96 — apply appropriate units and numeric displays. |
| reporting.results | not-applicable | No separate decision memo or regulated financial report. |
| reporting.disclosure | not-applicable | No separate decision memo or regulated financial report. |
| controls.backup-version | shallow | SKILL.md:40,78 — calculation copy and warning about lost objects; not an explicit rollback copy before a workbook edit. |
| controls.protection | not-applicable | No deployment into a shared, governed workbook workflow. |
| ethics.objectivity | not-applicable | No separate valuation opinion, presentation opinion or assurance records engagement. |
| ethics.misrepresentation | not-applicable | No separate valuation opinion, presentation opinion or assurance records engagement. |
| ethics.confidentiality | absent | No workflow instruction distinguishes shareable workbook contents from sensitive input or hidden data. |
| ethics.records | not-applicable | No separate valuation opinion, presentation opinion or assurance records engagement. |

counts: covered 15, shallow 11, absent 3, not-applicable 20, undetermined 0

## Excluded by profile

None.
