# Re-checking a report

A re-check is a second pass over the findings of a finished report, done before or after it is published. It tests whether each finding holds at its band. [reports/video-20/recheck.md](../reports/video-20/recheck.md) is an example.

## What the reviewer reads

- The report, including its `Scope` lines.
- The whole repository of the skill: every file in the skill folder, other skills it calls, and code it runs. Use `blindspot.py grep` on the skill folder and the repository root.

## Scope

Use the [scope rules](../skills/blindspot/SKILL.md#scope-rules) in `SKILL.md`, applied to the report's `Scope` lines. Do not judge with a boundary of your own. If you think the `Scope` lines are wrong, say so in a note on the finding and give the boundary you would use. Then give the verdict under the report's boundary.

## Verdicts

- **holds**: the gap is real and the band is fair for the skill's scope.
- **overstated**: the gap is partly covered elsewhere in the repository, it is real but belongs in a lower band, or the stage is outside the scope. Give the band it should have. When the reason is scope, name the scope rule by number.
- **wrong**: the skill covers it. Quote the file and line.

## What to publish

- One row per finding: finding id, map node, verdict, band after re-check, and the scope rule number where one applied.
- The counts of each verdict, and who or what did the re-check (a person, or the model and number of runs).
- Leave the original report's counts unchanged. Link the re-check from the top of the report.
