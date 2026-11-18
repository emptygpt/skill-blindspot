# Re-check of the 46 "Needed" findings

Date: 2026-11-17. Report: [What 20 public video skills leave out](../video-20.md).

After publishing the report we checked every finding rated Needed against the **whole** repository of each skill: references, docs, templates, recipe files, and the names and comments of scripts. The original audits read `SKILL.md` and the files it points to; most did not read the rest. Two reviewers (one model run each, ten skills per reviewer) gave each finding one verdict:

- **holds**: the gap is real and Needed is a fair band for the skill's scope
- **overstated**: the gap is partly covered somewhere else in the repository, or it is real but belongs in a lower band, or the stage is outside what the skill does
- **wrong**: the skill covers it

Result: **12 hold, 33 overstated, 1 wrong.** 45 of the 46 point at a real gap. 12 of the 46 were rated at the right level.

The one wrong finding: V20 said realistic synthetic people and voices go out with no AI label. The engine blocks delivery until the label is recorded (`engine/studio.mjs`, the `deliver` step). The report did not read the engine.

Typical overstated findings: a skill that stops at a local file was told it lacks a platform AI-label step (V13); a sub-skill already records the source and licence of every sound effect (V11); a user-approval gate before the mix sat in a sub-skill (V01) or a human review checklist in the app (V04). In V05 the final checks were in `SKILL.md` itself, so not every miss came from unread files: some were misreadings.

What changed in `blindspot` 0.3.0 because of this:

- A helper script reads every prose file in the skill folder and lists the code files, so the audit sees more than `SKILL.md`.
- Before a finding is rated Needed, the audit must search the whole folder and check that the stage is inside the skill's scope.

| Finding | Map node | Re-check | Band after re-check |
|---|---|---|---|
| V01-1 | comp.fact-check | holds | Needed |
| V01-2 | asm.review-revision | overstated | Worth considering |
| V01-3 | comp.ai-disclosure | overstated | Worth considering |
| V02-1 | assets.rights-acquisition | overstated | Worth considering |
| V02-2 | captions.accuracy-accessibility | overstated | Worth considering |
| V03-1 | comp.ai-disclosure | overstated | Worth considering |
| V04-1 | comp.ai-disclosure | overstated | Worth considering |
| V04-2 | assets.rights-acquisition | holds | Needed |
| V04-3 | pub.precheck | overstated | Worth considering |
| V05-1 | comp.ai-disclosure | holds | Needed |
| V05-2 | asm.review-revision | overstated | Worth considering |
| V06-1 | comp.ai-disclosure | holds | Needed |
| V06-2 | assets.copyright-fair-use | holds | Needed |
| V06-3 | edit.review-footage | holds | Needed |
| V06-4 | sound.narration-recording | overstated | Worth considering |
| V06-5 | captions.silent-viewing | overstated | Minor |
| V07-1 | edit.workflow | overstated | Worth considering |
| V07-2 | topic.subject-research | overstated | Worth considering |
| V07-3 | assets.music-licensing | overstated | Worth considering |
| V08-1 | asm.review-revision | overstated | Worth considering |
| V08-2 | comp.fact-check | holds | Needed |
| V08-3 | assets.music-licensing | overstated | Worth considering |
| V08-4 | ana.tracking | overstated | Minor |
| V09-1 | comp.fact-check | overstated | Worth considering |
| V10-1 | topic.subject-research | holds | Needed |
| V10-2 | sound.narration-recording | overstated | Worth considering |
| V11-1 | sound.mix | holds | Needed |
| V11-2 | comp.ai-disclosure | holds | Needed |
| V11-3 | assets.rights-acquisition | overstated | lower than Needed |
| V11-4 | comp.fact-check | overstated | lower than Needed |
| V11-5 | long.open-close-key-moments | overstated | lower than Needed |
| V12-1 | sound.mix | overstated | lower than Needed |
| V13-1 | comp.ai-disclosure | overstated | lower than Needed |
| V14-1 | comp.fact-check | overstated | lower than Needed |
| V14-2 | script.narration | overstated | lower than Needed |
| V14-3 | asm.review-revision | holds | Needed |
| V14-4 | topic.focus | overstated | lower than Needed |
| V16-1 | assets.rights-acquisition | overstated | lower than Needed |
| V16-2 | comp.ai-disclosure | holds | Needed |
| V17-1 | topic.subject-research | overstated | lower than Needed |
| V17-2 | pre.releases | overstated | lower than Needed |
| V18-1 | comp.ai-disclosure | overstated | lower than Needed |
| V19-1 | pre.releases | overstated | lower than Needed |
| V19-2 | comp.ai-disclosure | overstated | lower than Needed |
| V20-1 | comp.ai-disclosure | wrong | covered in engine code; Minor at most |
| V20-2 | assets.music-licensing | overstated | lower than Needed |
