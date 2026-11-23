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
| [`spreadsheet-finance` 0.1.0](spreadsheet-finance-spreadsheet.md) | [OpenAI: spreadsheet](https://github.com/openai/skills/tree/e6afb0d74cc75d220df2faf3dd6c635c2dc6a108/skills/.curated/spreadsheet) | 0 | 6 | 2 |
| [`spreadsheet-finance` 0.1.0](spreadsheet-finance-dcf-model.md) | [Anthropic financial-services: dcf-model](https://github.com/anthropics/financial-services/tree/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f/plugins/vertical-plugins/financial-analysis/skills/dcf-model) | 0 | 5 | 4 |
| [`tech-docs` 0.1.0](tech-docs.md) | [Addy Osmani: documentation-and-adrs](https://github.com/addyosmani/agent-skills/tree/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/documentation-and-adrs) | 0 | 3 | 0 |
| [`wechat-article` 0.1.0, extends `writing` 0.1.0](wechat-article.md) | [JimLiu: baoyu-post-to-wechat](https://github.com/JimLiu/baoyu-skills/tree/bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c/skills/baoyu-post-to-wechat) | 0 | 4 | 0 |
| [`writing` 0.1.0](writing.md) | [JimLiu: baoyu-format-markdown](https://github.com/JimLiu/baoyu-skills/tree/bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c/skills/baoyu-format-markdown) | 0 | 1 | 1 |

These were static audits by Devin using the [blindspot workflow](../../skills/blindspot/SKILL.md); target skills were not executed. The reports record scope, pre-map observations, the trace and evidence by node. File and line references point into the pinned skills. The first round used paraphrased evidence; the Anthropic and OpenAI data-analysis reports and the OpenAI and Anthropic financial-services spreadsheet-finance reports include short, verified excerpts. The WeChat report includes all inherited writing nodes, while the separate writing audit uses a different skill.

The counts here are findings by severity, not counts of domain coverage or independent re-check results.
