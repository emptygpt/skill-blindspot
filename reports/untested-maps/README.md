# Public skill audits for seven domain maps

Each map was applied to public skills pinned to commits. These cases exercise the maps; they do not establish accuracy across a domain or rate the audited skills.

| Map and version | Public skill | Needed | Worth considering | Minor |
|---|---|---:|---:|---:|
| [`data-analysis` 0.1.0](data-analysis.md) | [K-Dense-AI: exploratory-data-analysis](https://github.com/K-Dense-AI/claude-scientific-skills/tree/c21d13b3cc2894680229ba9959a53281acb9200e/skills/exploratory-data-analysis) | 0 | 3 | 0 |
| [`research-paper` 0.1.0](research-paper.md) | [K-Dense-AI: scientific-writing](https://github.com/K-Dense-AI/claude-scientific-skills/tree/c21d13b3cc2894680229ba9959a53281acb9200e/skills/scientific-writing) | 0 | 4 | 1 |
| [`spreadsheet-finance` 0.1.0](spreadsheet-finance.md) | [Anthropic: xlsx](https://github.com/anthropics/skills/tree/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx) | 0 | 5 | 0 |
| [`tech-docs` 0.1.0](tech-docs.md) | [Addy Osmani: documentation-and-adrs](https://github.com/addyosmani/agent-skills/tree/8c99fa36d90068c82d547f7c12a9d67a3e95f4ee/skills/documentation-and-adrs) | 0 | 3 | 0 |
| [`wechat-article` 0.1.0, extends `writing` 0.1.0](wechat-article.md) | [JimLiu: baoyu-post-to-wechat](https://github.com/JimLiu/baoyu-skills/tree/bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c/skills/baoyu-post-to-wechat) | 0 | 4 | 0 |
| [`writing` 0.1.0](writing.md) | [JimLiu: baoyu-format-markdown](https://github.com/JimLiu/baoyu-skills/tree/bf1ff076e25f8da4a339eb1c8cf03361fea5ea4c/skills/baoyu-format-markdown) | 0 | 1 | 1 |

## seo-web

| Map and version | Public skill | Needed | Worth considering | Minor |
|---|---|---:|---:|---:|
| [`seo-web` 0.1.0](seo-web.md) | [Corey Haines: seo-audit](https://github.com/coreyhaines31/marketingskills/tree/5b2b400eec1e7e1cec76245a715d0b0d4fd2a9c1/skills/seo-audit) | 0 | 5 | 1 |
| [`seo-web` 0.1.0](seo-web-claude-seo-schema.md) | [AgriciDaniel: seo-schema](https://github.com/AgriciDaniel/claude-seo/tree/468ed5b0d9e3249394783710e54abb02837e326b/skills/seo-schema) | 0 | 2 | 0 |
| [`seo-web` 0.1.0](seo-web-geohub-seo.md) | [GEOHub: seo](https://github.com/yaojingang/GEOHub/tree/2210f7f22153cfdf721905c2ac86318db97401b1/skills/seo) | 0 | 8 | 4 |

These were static audits by Devin using the [blindspot workflow](../../skills/blindspot/SKILL.md); target skills were not executed. The reports record scope, pre-map observations, the trace and evidence by node. File and line references point into the pinned skill or its delegated files. The first-round reports paraphrase evidence; the two later SEO reports include short evidence quotes. The WeChat report includes all inherited writing nodes, while the separate writing audit uses a different skill.

The counts are findings by severity, not domain coverage scores or independent re-check results. The audits found no Needed findings to send through a separate re-check.
