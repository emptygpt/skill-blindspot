# Blindspot report: spreadsheet

Skill under audit: [OpenAI: spreadsheet](https://github.com/openai/skills/tree/e6afb0d74cc75d220df2faf3dd6c635c2dc6a108/skills/.curated/spreadsheet).

Map: spreadsheet-finance 0.1.0    Profile: none    Date: 2026-11-23

## Scope
- Creates, edits, analyzes and formats `.xlsx`, `.csv` and `.tsv` files with openpyxl and pandas; finance and investment-banking layouts are formatting rules, not a modelling method.
- Starts from a requested file and goal; ends at a saved workbook, recalculated and rendered for review when that tooling is available.
- Does not promise forecasts, valuations, scenario analysis, a findings memo or sharing the file.

## Step 2 list (before opening the map nodes)

- Recalculation and rendering are conditional on available tooling; searched for a fallback check of formula results when neither is available and for a comparison against independently computed values.
- Editing keeps filenames stable; searched for keeping a copy of the original before an in-place edit.
- Searched for input constraints on fillable cells, a consistency scan across copied formulas, and a note on where values are rounded.
- Searched for a notes or cover area that tells the next user what the workbook does and how to use it.

## Findings

### Needed

None.

### Worth considering

1. **Check that results are right, not only that they render** [model+map+trace]
   Map nodes: `checks.test`, `checks.built-in`, `checks.evaluate`, `formulas.consistent`, `formulas.rounding`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 17. Build in checks, controls, and alerts from the outset.; 18. Test and review to reduce the risk of error and identify inefficiencies.; 12. Keep formulas consistent across ranges.
   Source: [Evaluate a nested formula one step at a time](https://support.microsoft.com/en-us/excel/evaluate-a-nested-formula-one-step-at-a-time) — Select Evaluate to examine the value of the underlined reference.
   Source: [ROUND function](https://support.microsoft.com/en-us/excel/functions/round-function) — The ROUND function rounds a number to a specified number of digits.
   Why: SKILL.md:37–47 recalculates "whenever possible" and renders "when rendering tooling is available"; the review looks at layout and visible results, and SKILL.md:94 names off-by-one and range mistakes without a way to find them. Nothing compares outputs with independently computed values, adds a reconciliation cell or says where rounding happens.
   Fix: In the Recalculation and visual review section, add a check of a few key outputs against values computed outside the workbook, a scan for formulas that break the pattern of their row or column, and a fallback when no recalculation tool exists.
2. **Keep a restorable original when editing in place** [model+map]
   Map nodes: `controls.backup-version`, `formulas.sheet-changes`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 19. Ensure there is a regular process of backup and version control. This minimises loss of work and avoids the use of the wrong version.
   Source: [Overview of formulas in Excel](https://support.microsoft.com/en-us/excel/get-started/overview-of-formulas-in-excel) — What occurs when you move, copy, insert, or delete worksheets.
   Why: SKILL.md:11 aims to edit "without breaking formulas, references, or formatting" and SKILL.md:23 keeps filenames stable, but no step keeps the original or compares formulas before and after an edit.
   Fix: In Workflow step 6, keep the input file unchanged (or a copy of it) and compare affected formulas and sheets against it before delivery.
3. **Validate fillable inputs and incoming data** [map]
   Map nodes: `inputs.validation`, `inputs.messages`, `inputs.inherited-validation`, `inputs.quality`.
   Source: [More on data validation](https://support.microsoft.com/en-us/excel/more-on-data-validation) — When is data validation useful?; Data Validation Input and Error Messages; How to update or remove data validation in an inherited workbook.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 10. Seek to control, clean, and optimise data quality and structure prior to using them.
   Why: Input cells are marked by colour (SKILL.md:122) but are not constrained, and analysis (SKILL.md:10) starts without a check of types, blanks or duplicates in the source data. Existing validation rules in an edited workbook are not mentioned.
   Fix: For workbooks with user inputs, add data validation with input and error messages, review existing rules when editing, and check source data before computing on it.
4. **Explain assumptions and how the workbook is used** [map]
   Map nodes: `inputs.assumptions`, `structure.flow`, `structure.guidance`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 6. Tailor the design and documentation to the needs of the audience and dependent processes.; 7. Make the spreadsheet easy to use, providing supporting guidance where helpful.; 9. Structure workbooks with a clear flow of inputs, processes, and outputs.
   Why: Sources are cited (SKILL.md:96–99, 136) and inputs are coloured, but nothing records why an assumption was chosen, where inputs, calculations and outputs sit, or how the next user should operate the file.
   Fix: For financial models, add an assumptions note and a short notes area with purpose, layout and update steps.
5. **Check charts against the point they make** [map]
   Map nodes: `reporting.charts`.
   Source: [Financial and Investment Analysts (13-2051.00), Job Duties Custom List](https://www.onetonline.org/search/task/choose/13-2051.00) — Task ID 21589: Draw charts and graphs, using computer spreadsheets, to illustrate technical reports.
   Why: SKILL.md:12, 33 adds native charts and the render review checks layout, not whether chart type, range, units and labels match the comparison.
   Fix: When adding a chart, check its source range, axis units and labels against the question it answers.
6. **Check what the workbook exposes before handoff** [map]
   Map nodes: `ethics.confidentiality`.
   Source: [Code of Ethics and Standards of Professional Conduct](https://www.cfainstitute.org/standards/professionals/code-ethics-standards) — Standard III(E) Preservation of Confidentiality.
   Why: SKILL.md:40 keeps an internal tool out of explanations, but nothing checks hidden sheets, comments or source values carried into a file meant for another audience.
   Fix: When the output goes to someone other than the requester, review hidden sheets, comments and cited inputs first.

### Minor

1. **Confirm the question and whether a spreadsheet fits** [map]
   Map nodes: `purpose.question`, `purpose.tool-fit`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 4. Determine if a spreadsheet is a suitable tool.; 5. Focus on the purposes of the spreadsheet.
   Why: SKILL.md:18–19 confirms file type and operation and picks a library, not the decision the file supports or whether the data belongs in a spreadsheet.
2. **Design for growth and reuse of results** [map]
   Map nodes: `structure.adaptability`, `formulas.reuse`.
   Source: [20 principles for good spreadsheet practice](https://www.icaew.com/technical/technology/excel-community/20-principles-for-good-spreadsheet-practice-2024-edition) — 8. Design with adaptability in mind to minimise future manual intervention.; 15. Refer to existing calculated results instead of reperforming the calculation.
   Why: Totals sum the cells above (SKILL.md:116, 141); nothing covers adding rows or periods without repairing formulas, or referring to an existing result instead of recomputing it.

## Unsourced findings

None.

## Evidence limitations

The four openpyxl example scripts were listed but not read as instructions; quotes come from SKILL.md. No workbook was created and no command was run.

## Trace

| Step | Produces | Used by | Checked |
|---|---|---|---|
| Confirm file type and goal | Operation (create, edit, analyze, visualize) | Tool choice | SKILL.md:18–19; no question or audience recorded. |
| Build or edit with openpyxl or pandas | Workbook with formulas, formats and citations | Recalculation | SKILL.md:85–145 rules for formulas, citations and formats. |
| Recalculate and render | Cached values and page images | Visual review | SKILL.md:37–47; both conditional on tooling, no fallback for results. |
| Save and clean up | Final file under a stable name | User | SKILL.md:23; no original kept for comparison. |

## Map table

| Node | State | Evidence |
|---|---|---|
| purpose.question | shallow | SKILL.md:18 — "Confirm the file type and goal: create, edit, analyze, or visualize." Names the operation, not the decision it supports. |
| purpose.audience | not-applicable | Builds the requested file; no business case or downstream process review promised. |
| purpose.tool-fit | shallow | SKILL.md:19 — "for analysis and CSV/TSV workflows"; picks a library, not whether a spreadsheet suits the task. |
| purpose.risk | not-applicable | No assurance or criticality assessment in scope. |
| purpose.competence | not-applicable | No staffing or training of workbook users in scope. |
| inputs.quality | shallow | SKILL.md:10 — "Read or analyze tabular data (filter, aggregate, pivot, compute metrics)." No check of source data first. |
| inputs.assumptions | shallow | SKILL.md:98 — "For financial models, cite model inputs in cell comments." SKILL.md:137 — "yellow fill for key assumptions that need attention"; sources, not reasoning. |
| inputs.validation | absent | No data-validation constraints on input cells. |
| inputs.messages | absent | No input or error messages. |
| inputs.inherited-validation | absent | Editing rules cover formatting, not existing validation rules. |
| inputs.sourcing | covered | SKILL.md:97 — "Cite sources inside the spreadsheet using plain-text URLs." SKILL.md:136 — "Cite sources for all raw inputs in cell comments." |
| structure.flow | shallow | SKILL.md:112 — "Headers should be visually distinct from raw inputs and derived cells." Colour marks cell roles; no input-to-output arrangement. |
| structure.layout | covered | SKILL.md:116–117 — "Group related calculations and make totals simple sums of the cells above them." "Add whitespace to separate sections." |
| structure.adaptability | absent | Nothing on extending rows or periods without repairing formulas. |
| structure.conventions | covered | SKILL.md:101–105, 121 — "Preserve existing formatting and style exactly." "Color conventions (if no style guidance)" |
| structure.guidance | absent | No notes area, purpose, owner or operating guidance for the next user. |
| formulas.consistent | absent | Copy behaviour is covered under references; no check that comparable ranges share one formula pattern. |
| formulas.simple | covered | SKILL.md:88 — "Keep formulas simple and legible; use helper cells for complex logic." |
| formulas.constants | covered | SKILL.md:90 — "Prefer cell references over magic numbers" |
| formulas.reuse | absent | Totals sum the cells above; no rule to reference an existing result instead of recomputing it. |
| formulas.references | covered | SKILL.md:91 — "references carefully so copied formulas behave correctly." |
| formulas.sheet-changes | shallow | SKILL.md:11 — "Modify existing workbooks without breaking formulas, references, or formatting." Goal stated, no check after edits. |
| formulas.function-use | covered | SKILL.md:87–89 — "Do not use dynamic array functions like" "Avoid volatile functions like" |
| formulas.errors | covered | SKILL.md:37, 93 — "Recalculate formulas before delivery whenever possible so cached values are present in the workbook." "Guard against" |
| formulas.rounding | absent | SKILL.md:110 sets percentage display only; no calculation rounding rule. |
| checks.built-in | absent | No reconciliation or check cells. |
| checks.test | shallow | SKILL.md:47 — "Review rendered sheets for layout, formula results, clipping, inconsistent styles, and spilled text." Visual review only, when rendering exists. |
| checks.peer-review | not-applicable | Ends at local handoff; no reviewer assigned. |
| checks.evaluate | shallow | SKILL.md:94 — "Check for off-by-one mistakes, circular references, and incorrect ranges." No method for inspecting formula steps. |
| scenarios.cases | not-applicable | No forecasting or scenario analysis promised; IB-style models get layout rules only. |
| scenarios.sensitivity | not-applicable | No forecasting or scenario analysis promised; IB-style models get layout rules only. |
| scenarios.target | not-applicable | No forecasting or scenario analysis promised; IB-style models get layout rules only. |
| scenarios.forecast | not-applicable | No forecasting or scenario analysis promised; IB-style models get layout rules only. |
| analysis.* | not-applicable | No valuation, ratio or statement analysis promised. |
| reporting.charts | shallow | SKILL.md:12, 33 — "Visualize data with charts, summary tables, and sensible spreadsheet styling." "for native Excel charts when needed" |
| reporting.formats | covered | SKILL.md:108, 111, 135 — "Use appropriate number and date formats." "Currencies should use the appropriate currency format." "Always specify units in headers" |
| reporting.results | not-applicable | No separate findings memo or report. |
| reporting.disclosure | not-applicable | No IFRS reporting output. |
| controls.backup-version | shallow | SKILL.md:23 — "Save outputs, keep filenames stable, and clean up intermediate files." No copy of the original kept. |
| controls.protection | not-applicable | No shared or governed workbook deployment. |
| ethics.objectivity | not-applicable | No valuation opinion or recommendation. |
| ethics.misrepresentation | not-applicable | No valuation opinion or recommendation. |
| ethics.confidentiality | absent | Nothing on hidden sheets, comments or sensitive inputs before handoff. |
| ethics.records | not-applicable | No engagement records beyond the delivered file. |

counts: covered 9, shallow 10, absent 10, not-applicable 20, undetermined 0

## Excluded by profile

None.
