# skill-blindspot

**Find what your agent skill doesn't know it's missing.**

English | [中文](README.zh-CN.md)

Skill linters check format. Skill evals check whether the skill works on the tasks you thought of. Neither tells you about the step you never thought of.

`skill-blindspot` audits an agent skill (a folder with a `SKILL.md`) for missing stages. It asks the model what is missing, then checks the skill against a **domain map** built from knowledge that people have already organised: occupational task databases, textbook and course outlines, official platform documentation, regulation text. You get a node-by-node table of what is covered, shallow or absent, with the lines it found in your skill and a source for every node.

> **Status: v0.4.2.** The repository includes the skill, eleven domain maps and a Python helper. Published audits cover public video and coding skills. The report format may change.

## First report

[What 20 public video skills leave out](reports/video-20.md). The gaps cluster around the video rather than in it: labelling AI-generated content, rights to footage, music and voices, fact-checking the script, and someone watching the final file.

Then we checked our own report. Of the 46 findings rated Needed, 45 point at a real gap, but only 12 hold at that level: 33 were partly covered in files the audit had not read, or belong in a lower band, and 1 was wrong. [The re-check](reports/video-20/recheck.md) is public, and version 0.3.0 changes how the audit reads a skill because of it. [Re-auditing ten of the skills with 0.3.0](reports/video-20/v0.3/README.md) gave 13 Needed findings instead of 33, and 8 of them held on review (62%, up from 30%). Both reviews were model runs and they do not always agree, so the size of the gain is rough.

## What you get

An excerpt from a real run, on a public skill that edits talking-head reels ([full report](reports/video-20/V03.md)). First, the findings, each tagged with who found it and where the source is:

> **Needed**
> 1. **No label or disclosure step for AI-generated stills, voices and cut-outs** [model+map]
>    Map node: comp.ai-disclosure — source: Video Production Course Online (Self-Paced) syllabus, "M14 Use AI responsibly"
>    Why: Searched for disclosure, label, synthetic. The skill allows "AI stills", an ElevenLabs narrator recipe and AI cut-out effects but only limits what they may show.

Then the full table: every node of the map, with the skill's own lines as evidence.

| Node | State | Evidence |
|---|---|---|
| script.hook | covered | "`textfx` beats `hook` (the first 1.5-3 s)"; QA checks "the first 1.5 s". |
| assets.music-licensing | covered | "library/music/ licensed music beds + manifest" |
| assets.rights-acquisition | shallow | "on Mixkit only clips offered in 2160p carry the free commercial licence"; memes "the user adds them at their own risk". |
| comp.fact-check | shallow | Data Story recipe: "only real numbers, each with its source on screen"; the speaker's other claims are not checked. |
| comp.ai-disclosure | absent | Nothing in the skill corresponds to it. |
| pre.location | not-applicable | Shoot happens before the skill starts. |

The report also lists findings the model raised that no source backs (marked unsourced), and a trace of which step's output feeds which later step.

## Second report

[Five public coding skills](reports/code-5.md), audited with the new `software` map and version 0.3.0. Eight Needed findings, all of which held on a separate re-check, among them a security-audit skill whose agents are never told that the target repository's text is not instructions, and a TDD skill that never says to watch the test fail.

[Fifteen additional coding workflows](reports/code-20.md), audited with 0.4.1 and ranked alongside the earlier five: four of five new Needed findings held on re-check; two understated bands are recorded separately.

## Install

```bash
npx skills add emptygpt/skill-blindspot
```

Or copy `skills/blindspot/` into your agent's skills folder. The maps come with it. Then ask your agent: "run blindspot on `path/to/my-skill` with the video map", or name another map from the table below.

## Maps in this repository

Use them directly. Every node cites its source, so you do not have to search for one. Details and scope: [skills/blindspot/maps/INDEX.md](skills/blindspot/maps/INDEX.md).

| Map | Covers | Nodes | Public skill audits |
|---|---|---|---|
| `video` | Online video, from topic to publishing and review | 118 | [4 audits](reports/video-20.md) |
| `video-short` | Short-form vertical video, on top of `video` | +29 | [8 audits](reports/video-20.md) |
| `video-long` | Long-form video, on top of `video` | +22 | [8 audits](reports/video-20.md) |
| `writing` | Non-fiction articles published online | 78 | [3 audits](reports/untested-maps/README.md#writing) |
| `wechat-article` | WeChat official account articles, on top of `writing` | +40 | [3 audits](reports/untested-maps/README.md#wechat-article) |
| `software` | Making a change to software with an AI coding agent, from request to maintenance | 90 | [20 audits](reports/code-20.md) |
| `research-paper` | Research papers and reproducible analysis | 76 | 3 audits: [scientific writing](reports/untested-maps/research-paper.md), [paper writing](reports/untested-maps/research-paper-research-paper-writing.md), [academic paper](reports/untested-maps/research-paper-academic-paper.md) |
| `tech-docs` | Technical and API documentation: reference, procedures, code samples, OpenAPI descriptions | 75 | 3 audits: [ADRs](reports/untested-maps/tech-docs.md), [co-authoring](reports/untested-maps/tech-docs-doc-coauthoring.md), [API endpoints](reports/untested-maps/tech-docs-document-api-endpoint.md) |
| `data-analysis` | Answering questions with data, including analysis code, charts and results with limits | 45 | [3 audits](reports/untested-maps/) |
| `spreadsheet-finance` | Spreadsheet modeling and financial analysis, from question and inputs to checks, scenarios, reports and disclosure | 49 | [3 audits](reports/untested-maps/) |
| `seo-web` | SEO and website content operations; article writing and software changes use their own maps | 74 | [Provisional (1/3)](reports/untested-maps/seo-web.md) |

Provisional maps have not yet met the three-audit target. See the [public skill audit index](reports/untested-maps/).

The narrower maps extend a base map: they add nodes and list base nodes that do not apply. Each file's header lists what is **not yet covered** because no source was found. The video maps cite YouTube, TikTok, Bilibili and Douyin official pages, the US FTC and a Chinese advertising regulation. Douyin's creator learning centre could not be read.

To add a node or a map, see [CONTRIBUTING.md](CONTRIBUTING.md). To build a map for your own domain, follow [Build your own domain map](docs/build-a-map.md), which uses the five newest maps as worked examples. Missing a domain? [Ask for a map](https://github.com/emptygpt/skill-blindspot/issues/new?template=map-request.yml).

## What we tested first

In a [historical pilot](docs/validation.md), we removed twelve items from six public skills in two domains. Each of two methods checked them twice: model-only recovered **20/24 chances**, and map-guided recovered **18/24**. The combined skill later recovered **11/12 items** in one run on the same examples. The original per-run evidence is unavailable for independent rescoring; these observations do not establish whether one method is better.

So this tool uses both. The model finds gaps. The map supplies the evidence, the table and a place to record what you skip on purpose.

## How it works

1. **Ask.** The model lists what it thinks the skill is missing, from its own knowledge of the domain.
2. **Map.** Each node is checked against the skill and marked covered, shallow, absent, not applicable, excluded by profile, or undetermined. If evidence is unavailable, the report names it without counting the node as a gap. The map is a YAML tree. Every node carries an id, a parent, a source, a link and a licence. A node with no source is not allowed in.
3. **Trace.** Each step's output is followed to see whether a later step uses it. This finds gaps that no map lists.
A small Python script (standard library only) does the mechanical parts: it reads the whole skill folder, builds a worksheet of map nodes with the skill lines that look related, fetches sources for the report, and checks the finished report against the map. The model's tokens go to judgement, not to reading the full map. Without Python the skill still works, by reading.

4. **Profile.** Not every gap should be filled. You record what does not apply to you, with an optional reason, in a small profile file. The next run respects it. The public map stays the same for everyone and your profile holds what is specific to you.

The split between a shared catalogue and a personal profile follows established practice in other fields, such as profiles in the NIST Cybersecurity Framework and catalogues and profiles in OSCAL.

## Before you write a skill

The same maps work as a checklist before a skill exists. Tell the agent what the skill will do and where it stops, and it writes `checklist.md`: every node of the map inside that boundary, each with a source, so the questions a skill builder asks you ("do you need rights to the images?") have something to check against. No model call is needed for the list itself:

```bash
python3 skills/blindspot/scripts/blindspot.py checklist --map video-short --skip shooting publishing analytics --out checklist.md
```

## What it is not

- It does not score your skill or say it is good.
- It does not write the missing parts for you. Each Needed finding says where a fix belongs and what it should add.
- It does not replace running your skill on real tasks.

## Roadmap

- [x] [Historical pilot](docs/validation.md): compare model-only and map-guided recovery
- [x] `blindspot` skill v0.1: ask, map, trace, profile ([skills/blindspot/SKILL.md](skills/blindspot/SKILL.md))
- [x] Maps: `video`, `video-short`, `video-long`, `writing`, `wechat-article`, `seo-web`, every node sourced
- [x] Map: `software` and reports on five coding skills ([code-5](reports/code-5.md)) and fifteen additional workflows ([code-20](reports/code-20.md))
- [x] Map: `tech-docs` (technical and API documentation)
- [ ] More maps: fiction (short story, novel), and video platforms beyond YouTube
- [x] [benchmark/](benchmark/): the remove-and-recover method and data, so others can test their own approach
- [x] Report: [what 20 public video skills leave out](reports/video-20.md)
- [x] Second domain (writing) and a guide for building a map: [docs/map-format.md](docs/map-format.md)
- [x] Step-by-step guide to building your own map: [docs/build-a-map.md](docs/build-a-map.md)

## Sources for the video map

`skills/blindspot/maps/video.yaml` cites these. Each node names the section, task statement or skill it comes from.

- O*NET 31.0 task statements. This product includes information from the O*NET 31.0 Database by the U.S. Department of Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 license. O*NET® is a trademark of USDOL/ETA. The statements are shortened and regrouped here, and USDOL/ETA has not endorsed this adaptation.
- ESCO. This publication uses the ESCO classification of the European Commission. Skill names are regrouped here, so the map is an adaptation.
- Official creator documentation from video platforms, and published course and textbook outlines. Only section titles are cited. Their licences are not verified.

Not yet covered because no source was found: screen recording, and comparison method for tool reviews. A node needs a source before it goes in.

## Related work

- [SkillFoundry](https://github.com/ma-compbio-lab/SkillFoundry) uses a domain tree to decide which skills to build for a library. This project audits one existing skill against a map.
- [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) validates, deduplicates and evaluates skills. It does not check domain coverage.

## Contributing

The most useful contribution is domain knowledge: a missing node with a source, or a correction to an existing one. See the [map format guide](docs/map-format.md), and [Build your own domain map](docs/build-a-map.md) for a whole new map.

## Licence

The skill instructions and helper code are [MIT-licensed](LICENSE). The [map data](skills/blindspot/maps/INDEX.md), including the compiled cache, contains third-party material and is not uniformly MIT-licensed. Each node links to source records with attribution and licence notes. Check the applicable source terms before reusing map data or derived outputs; “not verified” is not permission.
