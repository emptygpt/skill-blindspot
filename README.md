# skill-blindspot

**Find what your agent skill doesn't know it's missing.**

English | [中文](README.zh-CN.md)

Skill linters check format. Skill evals check whether the skill works on the tasks you thought of. Neither tells you about the step you never thought of.

`skill-blindspot` audits an agent skill (a folder with a `SKILL.md`) for missing stages. It asks the model what is missing, then checks the skill against a **domain map** built from knowledge that people have already organised: occupational task databases, textbook and course outlines, official platform documentation, regulation text. You get a node-by-node table of what is covered, shallow or absent, with the lines it found in your skill and a source for every node.

> **Status: early.** The repository is being built in public. The first domain is video production. Nothing here is installable yet. See the roadmap below.

## What we tested first

Before building anything we tested the obvious objection: can you just ask the model what is missing? We removed stages from six public skills in two domains and ran blind checks.

**Asking the model recovered 20 of 24 removed items. The map-guided check recovered 18.** A map does not find more. It gives each finding a source and quoted evidence, and it produces a complete table instead of a top-10 list. Full method and numbers: [docs/validation.md](docs/validation.md).

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
- [ ] `blindspot` skill: ask, map, trace, profile
- [ ] `maps/video.yaml`: first domain map, every node sourced
- [ ] `benchmark/`: the remove-and-recover method and data, so others can test their own approach
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
