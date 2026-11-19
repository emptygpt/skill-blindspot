# Maps

| Map | File | Scope | Own nodes |
|---|---|---|---|
| `video` | `video.yaml` | Online video for platforms: explainers, reviews, shorts. From topic to publishing and review of results. Sources: YouTube, Bilibili and Douyin official pages, occupational and course sources, FTC and China ad-law guidance on disclosure. | 118 |
| `video-short` | `video-short.yaml` | Extends `video`. Vertical short-form video of up to about three minutes. Sources are YouTube's and TikTok's ad creative guidance, plus Douyin rules and Bilibili course titles. | 29 |
| `video-long` | `video-long.yaml` | Extends `video`. Horizontal long-form video: chapters, end screens, cards, audience retention. Sources are YouTube's, plus Bilibili course titles and a Douyin rule on sponsored segments. | 22 |
| `writing` | `writing.yaml` | Non-fiction articles published online: blogs, platform articles, columns. From topic to publishing, follow-up, ethics and compliance. | 78 |
| `wechat-article` | `wechat-article.yaml` | Extends `writing`. Articles sent from a WeChat official account: title, cover, summary, original declaration, reprints, platform content rules, sending. | 40 |
| `software` | `software.yaml` | Making a change to software with an AI coding agent: requirements, design, implementation, testing, review, security, dependencies and licences, version control, release, operation, maintenance, docs, and risks specific to agent help. Sources: NIST SSDF, OWASP ASVS 5.0 and Top 10s, Google engineering practices, SemVer, Keep a Changelog, Conventional Commits, GitHub Docs, DORA, WCAG, O*NET, ESCO. The header lists stages no source covers, such as debugging method and refactoring. | 90 |
| `research-paper` | `research-paper.yaml` | Research papers and reproducible analysis: study planning, ethics, FAIR data, analysis, paper writing, reporting guidelines, submission and publication. Owns academic paper writing excluded by `writing`; sources are strongest for biomedical and health research. Research-specific computational environments, data versions, executable compendia, result reproduction, availability and citation are included. Out of scope: grant writing, lab bench protocols, teaching, and general software-engineering practice (version control, code review, testing, CI and dependency/licence hygiene), which belongs to `software`. | 76 |

A map that says `extends: <id>` adds to a base map. Use it when the skill fits the narrower scope.
