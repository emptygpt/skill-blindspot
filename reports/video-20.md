# What 20 public video skills leave out

Audit date: 2026-11-17. Tool: `blindspot` 0.2.1 with the `video`, `video-short` and `video-long` maps (map version 0.2.1).

We ran `blindspot` on 20 public agent skills for making videos: 8 short-form, 8 long-form or explainer, and 4 general. The 20 were taken from two community lists, [awesome-claude-video-skills](https://github.com/zhuyansen/awesome-claude-video-skills) and [awesome-video-skills](https://github.com/ella-wang-opus/awesome-video-skills). Each one describes a multi-stage workflow. We left out skills that only wrap one tool.

## The short version

The 20 skills are good at making the video. What they skip happens **around** the video: telling viewers that content was made by AI, checking the facts the video states, rights to footage, music and voices, and having someone watch or listen to the final file.

| Gap (needed findings only) | Skills | Example sources in the map |
|---|---|---|
| No AI-content disclosure step | **11 of 20** | Douyin rules "抖音内容标识使用规范" and "AIGC标识的水印与元数据规范"; a video production course syllabus, "Use AI responsibly" |
| Claims in the script are not researched or fact-checked | **8 of 20** | O*NET 27-3041.00 "Verify facts, dates, and statistics"; ESCO "check correctness of information" |
| No rights step for footage, music, cloned voices or real people | **10 of 20** | O*NET "Obtain rights to scripts…" and "Arrange for copyright permissions"; talent releases in two production textbooks |
| Nobody watches or listens to the final file before it is called done or posted | **9 of 20** | O*NET 27-4032.00 "Review assembled films or edited videotapes"; ESCO "mix multi-track recordings" |

46 findings were rated "needed" across the 20 skills, from 0 to 5 per skill. The other 7 were about captions (2), a stage the skill names but never defines (3), and missing narration or audience planning in one skill (2).

The four themes overlap: 19 of the 20 skills have at least one of them. Sponsor and ad disclosure is a separate map node; it is part of the needed findings for V07 (a product-promotion replica) and V20 (UGC-ad formats).

## Per skill

Full report for each skill, with the quoted lines and the complete map table: [reports/video-20/](video-20/).

"Needed" counts findings the auditor judged necessary for the skill's own stated goal. The map is the one the audit used. Each repository was read at its latest commit on the audit date.

| # | Skill | Map | Needed | Top finding |
|---|---|---|---|---|
| V01 | [hassancs91/claude-faceless-shorts-creator](https://github.com/hassancs91/claude-faceless-shorts-creator) `make-short` | short | 3 | Facts are "verified before scripting" with no method, source list or record |
| V02 | [AgriciDaniel/claude-shorts](https://github.com/AgriciDaniel/claude-shorts) | short | 2 | Any input video is clipped with no ownership or guest-consent check |
| V03 | [kurbaitaev/ghost-editor](https://github.com/kurbaitaev/ghost-editor) | short | 1 | AI stills and an AI narrator are used with no platform AI-label step |
| V04 | [ymybxx/SoloMCN](https://github.com/ymybxx/SoloMCN) | short | 3 | AI labels and disclaimers are left to the user "at the final-cut stage", and no later step reminds them |
| V05 | [zoglmk/codex-video-pipeline](https://github.com/zoglmk/codex-video-pipeline) | short | 2 | AI images and TTS are packaged for publishing with no AI-label step |
| V06 | [ninestonelee/youtube-shorts-factory](https://github.com/ninestonelee/youtube-shorts-factory) | short | 5 | Realistic generated drama is published with no AI or fiction disclosure |
| V07 | [fendouai/ViralForge](https://github.com/fendouai/ViralForge) | short | 3 | How the replica and variants are generated and checked is not described |
| V08 | [tmakersas/revid-skills](https://github.com/tmakersas/revid-skills) | short | 4 | A video can be posted publicly without anyone having watched it |
| V09 | [vincentsch/explainroo](https://github.com/vincentsch/explainroo) | long | 1 | Checks cover audio and layout, not whether the narration's claims are true |
| V10 | [iart-ai/explainer-video-skills](https://github.com/iart-ai/explainer-video-skills) | long | 2 | No research or fact-check for the facts and numbers stated |
| V11 | [hassancs91/claude-youtube-editor](https://github.com/hassancs91/claude-youtube-editor) | long | 5 | The final mix is referenced twice but no skill defines it |
| V12 | [SunandBean/paper2video](https://github.com/SunandBean/paper2video) | long | 1 | The final file's audio is never checked (loudness, clipping, pronunciation) |
| V13 | [runesleo/claude-video-kit](https://github.com/runesleo/claude-video-kit) `video-explainer` | long | 1 | A fully generated video has no AI-content disclosure step |
| V14 | [znyupup/knowledge-explainer-skill](https://github.com/znyupup/knowledge-explainer-skill) | long | 4 | Nothing reviews the agent-written script before render |
| V15 | [OnurGumus/codebase-video](https://github.com/OnurGumus/codebase-video) | long | 0 | (worth considering) final loudness is not checked in the skill's steps |
| V16 | [zenstory-ai/video-recap-skills](https://github.com/zenstory-ai/video-recap-skills) | long | 2 | Third-party footage is re-cut with no rights or originality step |
| V17 | [digitalsamba/claude-code-video-toolkit](https://github.com/digitalsamba/claude-code-video-toolkit) | general | 2 | Narration is written from a brief and never researched or checked |
| V18 | [mileson/chaojifeng-video-design](https://github.com/mileson/chaojifeng-video-design) | general | 1 | No AI-content or staged-content disclosure |
| V19 | [kangarooking/director-skills](https://github.com/kangarooking/director-skills) | general | 2 | Likeness of real people is a reminder, not a gate |
| V20 | [LordVayron/video-factory](https://github.com/LordVayron/video-factory) | general | 2 | AI influencer and UGC-ad formats have no ad or AI disclosure |

Several skills are strong in places. V03 and V15 trace every output into a later check. V09 has the fullest coverage of the long-form map. V12 checks facts and licences carefully.

## Where the findings came from

Each finding records which part of the audit surfaced it: the model's own first list, the map, or the trace of outputs between steps.

| Surfaced by | Needed findings |
|---|---|
| Model and map | 27 |
| Model, map and trace | 13 |
| Model and trace, no map node | 4 |
| Map and trace, not the model | 2 |

The model found 44 of the 46 by itself. This matches our [earlier validation](../docs/validation.md): the map rarely finds what the model misses. What the map adds is a source for 42 of the 46 findings, so the author can see which platform rule or task list a finding comes from, and a full table of what the skill already covers.

## Limits

- **One run per skill, by one model.** The audits were run by Claude Sonnet subagents. No person re-checked every finding. We spot-checked two (V04, V17) against the skill text. One summary overstated the skill and was reworded here: V04 does not forbid AI labels. It defers them to the user at the final stage and removes them from generated output.
- **Text only.** No code from these repositories was run. Where a skill relies on an engine or service not in the repository, behaviour was judged from the documentation.
- **Map choice affects the counts.** V10 makes 30–90 second videos but was audited with the long-form map, so many nodes were marked not applicable.
- **"Needed" is a judgment.** It means needed for the skill's own stated goal, not needed for every user. A skill that stops at an MP4 file is not faulted for missing publishing steps.
- **Star counts and dates** came from a community list's snapshot and shallow clones, not live values.

If a finding about your skill is wrong, please open an issue. We will correct it.

## Reproduce

Install the skill, then for each skill: "run blindspot on `<path>` with the `video-short` map" (or `video-long`, `video`). The per-skill reports are in [reports/video-20/](video-20/).
