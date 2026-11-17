# skill-blindspot

**Find what your agent skill doesn't know it's missing.**

English | [中文](README.zh-CN.md)

Skill linters check format. Skill evals check whether the skill works on the tasks you thought of. Neither tells you about the step you never thought of.

`skill-blindspot` compares an agent skill (a folder with a `SKILL.md`) against a **domain map** built from knowledge that people have already organised: occupational task databases, textbook and course outlines, official platform documentation. It reports which parts of the domain your skill covers, which it only touches, and which it never mentions. Every finding links to its source.

> **Status: early.** The repository is being built in public. The first domain is video production. Nothing here is installable yet. See the roadmap below.

## Why

When you write a skill, you and the model both work inside the frame you started with. The model will polish what is there. It rarely tells you that a whole stage is absent. A video skill can have a careful scripting step and no step for clearing the rights to the footage it uses.

Asking a model "what is missing?" gives an answer drawn from the model's own prior, with no source and no way to compare two runs. A domain map is a text file. It can be reviewed, versioned, diffed and corrected by people who know the field.

## How it works

1. **Domain map.** A YAML tree of the stages and concerns of a domain. Every node carries an id, a parent, a source, a link and a licence. A node with no source is not allowed in. The model may merge synonyms and adjust granularity. It may not add knowledge.
2. **Match.** For each node, the tool looks for evidence in the skill and quotes the lines it found. Each node gets one of four states: covered, shallow, absent, or excluded on purpose.
3. **Profile.** Not every gap should be filled. You record what does not apply to you, with an optional reason, in a small profile file. The next run respects it. The public map stays the same for everyone and your profile holds what is specific to you.

The split between a shared catalogue and a personal profile follows established practice in other fields, such as profiles in the NIST Cybersecurity Framework and catalogues and profiles in OSCAL.

## What it is not

- It does not score your skill or say it is good.
- It does not generate the missing parts for you.
- It does not replace running your skill on real tasks.

## Roadmap

- [ ] Validation: does a sourced map find removed stages that a plain "what is missing?" prompt does not? Results will be published here either way.
- [ ] `maps/video.yaml`: first domain map, every node sourced
- [ ] `blindspot` command line tool: skill folder + map in, Markdown and JSON report out
- [ ] Report: what public video skills most often leave out
- [ ] Second domain (writing) and a guide for building a map for a new domain

## Sources for the video map

Planned sources. Licences are checked before any data is added to this repository.

- O*NET task statements (U.S. Department of Labor, CC BY 4.0)
- ESCO occupations and skills (European Commission)
- Official creator documentation from video platforms
- Published course and textbook outlines
- Stages observed in public video skills

## Related work

- [SkillFoundry](https://github.com/ma-compbio-lab/SkillFoundry) uses a domain tree to decide which skills to build for a library. This project audits one existing skill against a map.
- [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) validates, deduplicates and evaluates skills. It does not check domain coverage.

## Contributing

The most useful contribution will be domain knowledge: a missing node with a source, or a correction to an existing one. The map format will be documented when the first map lands.

## Licence

Code: MIT. Domain maps will carry the licence of their sources and be marked per node.
