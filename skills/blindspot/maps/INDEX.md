# Maps

| Map | File | Scope | Own nodes |
|---|---|---|---|
| `video` | `video.yaml` | Online video for platforms: explainers, reviews, shorts. From topic to publishing and review of results. Sources: YouTube, Bilibili and Douyin official pages, occupational and course sources. | 107 |
| `video-short` | `video-short.yaml` | Extends `video`. Vertical short-form video of up to about three minutes. Sources are YouTube's, plus Douyin rules and Bilibili course titles. | 24 |
| `video-long` | `video-long.yaml` | Extends `video`. Horizontal long-form video: chapters, end screens, cards, audience retention. Sources are YouTube's, plus Bilibili course titles. | 20 |
| `writing` | `writing.yaml` | Non-fiction articles published online: blogs, platform articles, columns. From topic to publishing, follow-up, ethics and compliance. | 78 |
| `wechat-article` | `wechat-article.yaml` | Extends `writing`. Articles sent from a WeChat official account: title, cover, summary, original declaration, reprints, platform content rules, sending. | 40 |

A map that says `extends: <id>` adds to a base map. Use it when the skill fits the narrower scope.
