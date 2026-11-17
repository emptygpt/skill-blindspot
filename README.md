# skill-blindspot

**Find what your agent skill doesn't know it's missing.**

English | [中文](README.zh-CN.md)

Skill linters check format. Skill evals check whether the skill works on the tasks you thought of. Neither tells you about the step you never thought of.

`skill-blindspot` audits an agent skill (a folder with a `SKILL.md`) for missing stages. It asks the model what is missing, then checks the skill against a **domain map** built from knowledge that people have already organised: occupational task databases, textbook and course outlines, official platform documentation, regulation text. You get a node-by-node table of what is covered, shallow or absent, with the lines it found in your skill and a source for every node.

> **Status: v0.1.** The skill and the first map (video production, 86 sourced nodes) are here. It has been tested on twelve altered skills. It is early and the report format may change.

## Install

```bash
npx skills add emptygpt/skill-blindspot
```

Or copy `skills/blindspot/` into your agent's skills folder. The maps come with it. Then ask your agent: "run blindspot on `path/to/my-skill` with the video map", or name another map from the table below.

## Maps in this repository

Use them directly. Every node cites its source, so you do not have to search for one. Details and scope: [skills/blindspot/maps/INDEX.md](skills/blindspot/maps/INDEX.md).

| Map | Covers | Nodes |
|---|---|---|
| `video` | Online video, from topic to publishing and review | 118 |
| `video-short` | Short-form vertical video, on top of `video` | +29 |
| `video-long` | Long-form video, on top of `video` | +22 |
| `writing` | Non-fiction articles published online | 78 |
| `wechat-article` | WeChat official account articles, on top of `writing` | +40 |

The narrower maps extend a base map: they add nodes and list base nodes that do not apply. Each file's header lists what is **not yet covered** because no source was found. The video maps cite YouTube, TikTok, Bilibili and Douyin official pages, the US FTC and a Chinese advertising regulation. Douyin's creator learning centre could not be read.

To add a node or a map, see [docs/map-format.md](docs/map-format.md). Run `python3 scripts/check_maps.py` before opening a pull request.

## What we tested first

Before building anything we tested the obvious objection: can you just ask the model what is missing? We removed stages from six public skills in two domains and ran blind checks.

**Asking the model recovered 20 of 24 removed items. The map-guided check recovered 18.** A map does not find more. It gives each finding a source and quoted evidence, and it produces a complete table instead of a top-10 list. Full method and numbers: [docs/validation.md](docs/validation.md).

On the same twelve items the combined skill recovered 11 in a single run.

So this tool uses both. The model finds gaps. The map supplies the evidence, the table and a place to record what you skip on purpose.

## How it works

1. **Ask.** The model lists what it thinks the skill is missing, from its own knowledge of the domain.
2. **Map.** Each node of the domain map is checked against the skill and marked covered, shallow, absent or excluded on purpose, with the quoted lines as evidence. The map is a YAML tree. Every node carries an id, a parent, a source, a link and a licence. A node with no source is not allowed in.
3. **Trace.** Each step's output is followed to see whether a later step uses it. This finds gaps that no map lists.
4. **Profile.** Not every gap should be filled. You record what does not apply to you, with an optional reason, in a small profile file. The next run respects it. The public map stays the same for everyone and your profile holds what is specific to you.

The split between a shared catalogue and a personal profile follows established practice in other fields, such as profiles in the NIST Cybersecurity Framework and catalogues and profiles in OSCAL.

## What it is not

- It does not score your skill or say it is good.
- It does not generate the missing parts for you.
- It does not replace running your skill on real tasks.

## Roadmap

- [x] Validation: does a sourced map find more than a plain "what is missing?" prompt? It does not. See [docs/validation.md](docs/validation.md)
- [x] `blindspot` skill v0.1: ask, map, trace, profile ([skills/blindspot/SKILL.md](skills/blindspot/SKILL.md))
- [x] Maps: `video`, `video-short`, `video-long`, `writing`, `wechat-article`, every node sourced
- [ ] More maps: fiction (short story, novel), and video platforms beyond YouTube
- [ ] `benchmark/`: the remove-and-recover method and data, so others can test their own approach
- [ ] Report: what public video skills most often leave out
- [x] Second domain (writing) and a guide for building a map: [docs/map-format.md](docs/map-format.md)

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

The most useful contribution will be domain knowledge: a missing node with a source, or a correction to an existing one. The map format will be documented when the first map lands.

## Licence

Code: MIT. Domain maps will carry the licence of their sources and be marked per node.
