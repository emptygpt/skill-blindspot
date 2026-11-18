# Re-audit of ten video skills with version 0.3.0

Date: 2026-11-17. Earlier audit: [What 20 public video skills leave out](../../video-20.md). Earlier re-check: [recheck.md](../recheck.md).

The [re-check](../recheck.md) of the first report found that only 12 of 46 Needed findings were rated at the right level. Version 0.3.0 changed how the audit reads a skill (whole folder, a search of the repository including code before anything is rated Needed, a scope check). This page measures whether that helped.

## Method

- Ten of the twenty skills, chosen because the re-check found overstated Needed findings in them: V01, V04, V06, V07, V08, V11, V14, V16, V17, V19. Together they had 33 Needed findings in the first report, of which the re-check held 10.
- Each skill was audited again from scratch with `blindspot` 0.3.0, one model run per skill (Claude Sonnet), with the helper script. The runs could not see the earlier reports or the re-check.
- Every new Needed finding was then checked against the whole repository by a second model run (Claude Sonnet, two runs of five skills each), with the same three verdicts as before: holds, overstated, wrong. The reviewer also judged the four gaps that the re-check had held as Needed but that the new audits rated lower.

No person checked the verdicts. One maintainer spot-check: V06's copyright finding (the skill does have a 30% change checklist with user confirmation, so overstated is fair) and V11's mix finding (the final mix is handed off with level notes but no skill owns it; this one is a judgement call).

## Result

| | Needed findings | Hold | Overstated | Wrong |
|---|---|---|---|---|
| First report, same ten skills | 33 | 10 (30%) | 23 | 0 |
| Version 0.3.0 | 13 | 8 (62%) | 5 | 0 |

- Fewer Needed findings, and a larger share of them hold. No finding was wrong.
- Of the 10 gaps the first re-check held, 6 were rated Needed again. The other 4 (V01 fact-checking, V04 asset rights, V11 and V16 AI labelling) were placed in a lower band, and the second reviewer agreed with the lower band for all four: V01's skill says facts "must be verified" and keeps a verified-facts section, V04 leaves rights to the user on purpose, and V11 and V16 stop before upload.
- The 5 overstated findings: V04 final-file check (loudness and aspect are partly handled in scripts), V06 originality (a change checklist exists), V06 AI labelling (the skill stops at a file), V07 boundary check (the AI label is set when the project is built), V11 music and final mix (a tool picks and ducks the music bed).

Per-skill Needed counts: V01 0, V04 1, V06 3, V07 2, V08 2, V11 2, V14 2, V16 0, V17 1, V19 0.

## Limits

- The two reviews were different model runs, and they disagree. Of the 6 gaps both rounds rated Needed, the second reviewer held 3 (V06 clip review, V08 fact-checking, V14 render review) and called 3 overstated. Most disagreement is about scope: whether AI labelling belongs to a skill that stops at a file. So 30% and 62% are not measured with the same ruler. The direction is clear; the exact size is not.
- Ten skills and 13 findings is a small sample.
- The V11 run looked at the map's node headings before writing its own list, which breaks the order the skill asks for. It says so in its report.
- Cost: about 89k to 156k tokens per audit, 116k on average, plus about 107k per review run of five skills.

## Files

Reports: [V01](V01.md), [V04](V04.md), [V06](V06.md), [V07](V07.md), [V08](V08.md), [V11](V11.md), [V14](V14.md), [V16](V16.md), [V17](V17.md), [V19](V19.md). Review tables: [review-A](review-A.md) (V01 to V08), [review-B](review-B.md) (V11 to V19).
