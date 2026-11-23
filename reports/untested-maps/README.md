# Public skill audits for seven domain maps

Each map is applied to public skills pinned to commits, with a target of three skills per map. These cases exercise the maps; they do not establish accuracy across a domain or rate the audited skills.

| Map and version | Public skill | Needed | Worth considering | Minor |
|---|---|---:|---:|---:|
| [`data-analysis` 0.1.0](data-analysis.md) | [K-Dense-AI: exploratory-data-analysis](https://github.com/K-Dense-AI/claude-scientific-skills/tree/c21d13b3cc2894680229ba9959a53281acb9200e/skills/exploratory-data-analysis) | 0 | 3 | 0 |
| [`data-analysis` 0.1.0](data-analysis-analyze.md) | [Anthropic: analyze](https://github.com/anthropics/knowledge-work-plugins/tree/0e0fcacddcc892eb92a1b7873ff9d68159c47571/data/skills/analyze) | 0 | 5 | 3 |
| [`data-analysis` 0.1.0](data-analysis-jupyter-notebook.md) | [OpenAI: jupyter-notebook](https://github.com/openai/skills/tree/49f948faa9258a0c61caceaf225e179651397431/skills/.curated/jupyter-notebook) | 0 | 3 | 2 |
| [`research-paper` 0.1.0](research-paper.md) | [K-Dense-AI: scientific-writing](https://github.com/K-Dense-AI/claude-scientific-skills/tree/c21d13b3cc2894680229ba9959a53281acb9200e/skills/scientific-writing) | 0 | 4 | 1 |
| [`seo-web` 0.1.0](seo-web.md) | [Corey Haines: seo-audit](https://github.com/coreyhaines31/marketingskills/tree/5b2b400eec1e7e1cec76245a715d0b0d4fd2a9c1/skills/seo-audit) | 0 | 5 | 1 |
| [`spreadsheet-finance` 0.1.0](spreadsheet-finance.md) | [Anthropic: xlsx](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx) | 0 | 5 | 0 |
| [`tech-docs` 0.1.0](tech-docs.md) | [Addy Osmani: documentation-and-adrs](https://github.com/addyosmani/agent-skills/tree/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/documentation-and-adrs) | 0 | 3 | 0 |
| [`wechat-article` 0.1.0, extends `writing` 0.1.0](wechat-article.md) | [JimLiu: baoyu-post-to-wechat](https://github.com/JimLiu/baoyu-skills/tree/bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c/skills/baoyu-post-to-wechat) | 0 | 4 | 0 |

These were static audits by Devin using the [blindspot workflow](../../skills/blindspot/SKILL.md); target skills were not executed. The reports record scope, pre-map observations, the trace and evidence by node. File and line references point into the pinned skills. The first round used paraphrased evidence; the follow-up data-analysis and writing reports include short excerpts checked with `lint --skill`. The WeChat report includes all inherited writing nodes and audits a different skill.

The counts here are findings by severity, not counts of domain coverage or independent re-check results. The first-round audits found no Needed findings to send through a separate re-check.

## Writing

The `writing` map has met the three-audit target. Its cases cover draft planning and research, prose revision, and Markdown formatting; none exercises publication or follow-up.

| Map and version | Public skill | Needed | Worth considering | Minor |
|---|---|---:|---:|---:|
| [`writing` 0.1.0](writing.md) | [JimLiu: baoyu-format-markdown](https://github.com/JimLiu/baoyu-skills/tree/bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c/skills/baoyu-format-markdown) | 0 | 1 | 1 |
| [`writing` 0.1.0](writing-content-research-writer.md) | [ComposioHQ: content-research-writer](https://github.com/ComposioHQ/awesome-claude-skills/tree/044d48b594f060c164f3b20fac9ea01374721bca/content-research-writer) | 0 | 3 | 2 |
| [`writing` 0.1.0](writing-humanizer.md) | [blader: humanizer](https://github.com/blader/humanizer/blob/3e5f816b5609c4002aebb69f12c6476fe3347d0a/SKILL.md) | 0 | 1 | 1 |
