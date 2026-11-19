# Validation: does a sourced domain map find more gaps than just asking the model?

Short answer: **no.** In our tests a plain "what is this skill missing?" prompt recovered removed stages slightly more often than a map-guided check. What the map added was a source for every finding and a full node-by-node table. This page reports what we ran and what we saw.

## Method

For offline preparation, scoring and recorded data, see [benchmark/](../benchmark/).

1. Take public agent skills. A setter agent removes two stages or requirements from each one and writes an answer key. The setter never sees the map.
2. Two kinds of checker read the altered skill. Neither sees the original or the answer key. Each works in its own folder.
   - **Model only:** list up to 10 missing stages from your own knowledge of the domain.
   - **Map-guided:** go through every node of a sourced domain map, mark it covered, shallow or absent with evidence, then check whether each step's output is used by a later step, then list up to 10 gaps.
3. Each checker runs twice per skill. A person scores the top-10 lists against the answer key.

All checkers used the same model (Claude Sonnet).

## Test 1: video production

- Skills: [Aaryan-Kapoor/video-production-skill](https://github.com/Aaryan-Kapoor/video-production-skill), [Alisa0808/vox-director](https://github.com/Alisa0808/vox-director), [HeyChengC/wallstreet-explainer](https://github.com/HeyChengC/wallstreet-explainer)
- Map: about 70 nodes drawn from official creator documentation and published course and textbook outlines
- Removed: audio-visual sync, final quality check, background music, captions, opening hook design, fact checking

| | Model only | Map-guided |
|---|---|---|
| Removed stages in the top 10 (12 chances) | 11 | 10 |
| Items shared between two runs on the same skill (of 30) | about 20 | about 27 |

## Test 2: EU Medical Device Regulation compliance

Chosen as a less familiar domain with an authoritative text.

- Skills: three public MDR 2017/745 skills by different authors
- Map: 171 nodes taken from the regulation text on EUR-Lex, each with its article or annex reference
- Removed: qualification of the clinical evaluator, vigilance reporting timelines, effect of combination devices on classification, person responsible for regulatory compliance, change control for off-the-shelf software and updates, interoperability and fail-safe behaviour

| | Model only | Map-guided |
|---|---|---|
| Removed items in the top 10 (12 chances) | 9 | 8 |
| Items shared between two runs on the same skill (of 30) | about 25 | about 26 |

## What we learned

1. **The model already knows most of what is missing.** Across both tests it recovered 20 of 24. Asking is cheap and works.
2. **A map cannot find what is not in the map.** Two removed items came from guidance documents and industry standards, not from the regulation text. The map-guided checker missed them.
3. **A map can crowd out what the model knows.** One item was found by the model-only checker in both runs and by the map-guided checker in neither. A long map takes the checker's attention.
4. **A top-10 list loses findings.** In the video test the map-guided checker marked the opening hook as shallow in its table in both runs, and left it out of its top 10 in both runs. The table is the useful output.
5. **A step-to-step check finds gaps no map lists.** The audio-visual sync gap was found by asking whether each step's output is used by a later step.
6. **Consistency was better with a map in one domain and equal in the other.**

What the map reliably added: a source for each finding, quoted evidence from the skill, and a complete table that can be reviewed and compared between runs.

## Test 3: the combined skill (v0.1)

We then wrote the `blindspot` skill to combine the three checks: the model lists gaps first, the map is opened afterwards, each step's output is traced, and the results are merged without cutting the list to a fixed length. We ran it once on the same twelve altered skills. The video map was rebuilt as `skills/blindspot/maps/video.yaml` (86 nodes) with nodes added from O*NET and ESCO, including audio-visual sync and final review.

| | Model only (average of two runs) | Map-guided (average of two runs) | Combined skill (one run) |
|---|---|---|---|
| Removed items recovered, of 12 | 10 | 9 | 11 |

The one item nobody recovered in any run was the qualification of the clinical evaluator. It comes from guidance outside the regulation text and is not in the map.

The combined reports are long: 22 to 36 findings per skill, sorted into three bands. All eleven recovered items appeared within the first ten findings. One run is not enough to claim the combined skill is better than asking the model. It is enough to say it is not worse, and it adds sources, evidence and a full table.

## What this changes

The tool is built as a combination. The model lists gaps first. The map then supplies the node-by-node table with sources, and a profile records what you leave out on purpose. The step-to-step check stays.

## Limits

- Small sample: two domains, six skills, twelve removed items, one model.
- One person scored the results, and judged which items in two runs were the same.
- The regulation domain is not truly obscure.
- In test 2 the map was widened from 63 to 171 nodes to match the scope of the skills, after the names of the removed items were known to the person running the test. The agent that widened it did not see them. This could favour the map-guided method. It still did not win.
