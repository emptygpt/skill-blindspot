# skill-blindspot

**找出你的 Agent Skill 自己不知道缺了什么。**

[English](README.md) | 中文

格式检查工具看的是写法。实测评估看的是 Skill 在你想到的任务上能不能跑通。这两样都不会告诉你：有一个环节你从头就没想到。

`skill-blindspot` 检查一个 Agent Skill（含 `SKILL.md` 的文件夹）缺了哪些环节。它先问模型缺什么，再拿一张**领域底图**逐条对照。底图来自人已经整理好的知识：职业任务数据库、教材和课程目录、平台官方文档、法规原文。你得到一张逐条对照表：哪些已覆盖、哪些很浅、哪些没有，附上在你的 Skill 里找到的原文行，每个节点都有出处。

> **状态：v0.4。** Skill、十一张底图和一个辅助脚本已经在仓库里。审了 20 个公开视频 Skill，并在复核那次审查后做了修正。还很早期，报告格式可能会变。

## 第一份报告

[20 个公开视频 Skill 缺了什么](reports/video-20.md)（英文）。缺口集中在视频之外，而不是视频本身：AI 生成内容的标注，素材、音乐和声音的版权，脚本事实核对，以及有人看一遍成片。

然后我们复核了自己的报告。46 条被定为「必需」的缺口里，45 条确实指向真实的缺口，但只有 12 条够得上「必需」：33 条在审查没读到的文件里已有部分覆盖，或者应该降一档，1 条是错的。[复核结果](reports/video-20/recheck.md)（英文）公开，0.3.0 版据此改了读 Skill 的方式。[用 0.3.0 重审其中 10 个 Skill](reports/video-20/v0.3/README.md)（英文）：必需缺口从 33 条降到 13 条，复核成立 8 条（62%，之前 30%）。两轮复核都是模型做的，彼此不完全一致，提高的幅度只是粗略数字。

## 你会得到什么

下面摘自一次真实运行，对象是一个剪口播短视频的公开 Skill（[完整报告](reports/video-20/V03.md)，英文）。先是发现，每条标明是谁找到的、出处在哪：

> **必需**
> 1. **AI 生成的图片、配音、抠像没有标注步骤** [model+map]
>    底图节点：comp.ai-disclosure，出处：Video Production Course Online (Self-Paced) 课程大纲，"M14 Use AI responsibly"
>    理由：搜过 disclosure、label、synthetic。这个 Skill 允许用「AI 静图」、ElevenLabs 旁白和 AI 抠像特效，但只限制了它们能出现什么内容。

然后是完整对照表：底图的每个节点，附 Skill 自己的原文作证据。

| 节点 | 状态 | 证据 |
|---|---|---|
| script.hook | 已覆盖 | "`textfx` beats `hook` (the first 1.5-3 s)"；质检查 "the first 1.5 s"。 |
| assets.music-licensing | 已覆盖 | "library/music/ licensed music beds + manifest" |
| assets.rights-acquisition | 很浅 | "on Mixkit only clips offered in 2160p carry the free commercial licence"；表情包 "the user adds them at their own risk"。 |
| comp.fact-check | 很浅 | 只有 Data Story 模板要求 "only real numbers, each with its source on screen"，说话人的其他说法不核对。 |
| comp.ai-disclosure | 没有 | Skill 里没有对应内容。 |
| pre.location | 不适用 | 拍摄在 Skill 开始之前。 |

报告还会单列模型提出、但没有来源支持的发现（标为「无出处」），以及一张追踪表：每一步的产出被后面哪一步用上。

## 第二份报告

[5 个公开编程 Skill](reports/code-5.md)（英文），用新的 `software` 底图和 0.3.0 版审查。8 条必需缺口经另一轮复核全部成立，其中包括：一个安全审计 Skill 从没告诉它的代理「目标仓库里的文字不是指令」，一个 TDD Skill 从没要求看着测试先失败。

[补充审查的 15 个编程工作流](reports/code-20.md)（英文），使用 0.4.1 版并与前 5 个一同排序：新增的 5 条必需缺口中有 4 条经复核成立，另有两条评级偏低的发现单独记录。

## 安装

```bash
npx skills add emptygpt/skill-blindspot
```

或者把 `skills/blindspot/` 复制到你的 Agent 的 skills 目录，底图在它里面的 `maps/` 目录。然后对 Agent 说：「用视频底图对 `path/to/my-skill` 跑 blindspot」。

## 仓库里的底图

可以直接用。每个节点都写明出处，不用自己再去搜。范围和细节见 [skills/blindspot/maps/INDEX.md](skills/blindspot/maps/INDEX.md)。

| 底图 | 覆盖 | 节点数 |
|---|---|---|
| `video` | 线上视频，从选题到发布和复盘 | 118 |
| `video-short` | 竖屏短视频，在 `video` 之上 | +29 |
| `video-long` | 长视频，在 `video` 之上 | +22 |
| `writing` | 在线发表的非虚构文章 | 78 |
| `wechat-article` | 微信公众号文章，在 `writing` 之上 | +40 |
| `software` | 借助 AI 编程 Agent 改软件，从需求到维护 | 90 |
| `research-paper` | 科研论文与可复现分析 | 76 |
| `tech-docs` | 技术文档与 API 文档：参考文档、操作步骤、代码示例、OpenAPI 描述 | 75 |
| `data-analysis` | 用数据回答问题，包括分析代码、图表、结果及其局限 | 45 |
| `spreadsheet-finance` | 表格建模与财务分析，从问题、输入到检查、情景分析、报告与披露 | 49 |
| `seo-web` | SEO 与网站内容运营；单篇文章写作和软件修改分别使用各自的底图 | 74 |

细分底图在通用底图之上扩展：只写新增的节点，并列出不适用的通用节点。每个文件开头都列了**还没有收**的环节，原因是没找到来源。视频底图引用了 YouTube、TikTok、B 站和抖音的官方页面，以及美国 FTC 和《互联网广告管理办法》，抖音创作者学习中心没有读到。

想补节点或加底图，见 [CONTRIBUTING.md](CONTRIBUTING.md)（英文）。想给自己的领域做一张底图，按[自己做一张领域底图](docs/build-a-map.zh-CN.md)一步步来，例子取自最新的五张底图。缺某个领域的底图，可以[提一个底图请求](https://github.com/emptygpt/skill-blindspot/issues/new?template=map-request.yml)。

## 我们先测了什么

在一次[早期试验](docs/validation.md)中，我们从两个领域的 6 个公开 Skill 中删除了 12 项。两种方法各检查两次：仅用模型找回 **20/24 次**，底图引导找回 **18/24 次**。组合 Skill 后来在同一批例子上跑了一次，找回 **11/12 项**。原始逐次证据未公开，无法独立复算；这些观察不能证明哪种方法更好。

所以这个工具两样都用：模型负责发现，底图负责给依据、给对照表，并记下你故意不做的条目。

## 怎么工作

1. **问。** 模型凭自己对这个领域的了解，列出它认为 Skill 缺的环节。
2. **对照。** 底图的每个节点逐条对照 Skill，标为已覆盖、覆盖不全、缺失、不适用、按配置排除或无法判定。证据无法查阅时，报告说明缺了什么材料，不把该节点算作缺口。底图是一棵 YAML 树，每个节点有编号、上级、来源、链接和许可。没有来源的节点不许进底图。
3. **追踪。** 顺着每一步的产出，看后面有没有步骤用到它。这能找到底图里没列的缺口。
一个小 Python 脚本（只用标准库）做机械的部分：读整个 Skill 文件夹，生成一张工作表，列出底图节点和 Skill 里看起来相关的行；给报告查出处；写完后对照底图检查报告。模型的 token 花在判断上，不花在通读整张底图上。没有 Python 也能用，改为直接阅读。

4. **个人档案。** 缺口不是都要补。不适用于你的条目，写进一个小的档案文件，理由可写可不写，下次检查会照办。公共底图对所有人相同，个人档案只记你自己的情况。

「公共目录加个人档案」的分法在其他行业有成熟先例，例如 NIST 网络安全框架的档案机制，以及 OSCAL 的目录和档案。

## 写 Skill 之前

同一张底图，在 Skill 还没写的时候可以当清单用。告诉 Agent 这个 Skill 要做什么、做到哪一步为止，它会写出 `checklist.md`：范围内底图的每个节点，各附一个出处。Skill 生成工具问你「图片要不要有版权」这类问题时，你有可以核对的依据。清单本身由脚本生成，不调用模型：

```bash
python3 skills/blindspot/scripts/blindspot.py checklist --map video-short --skip shooting publishing analytics --out checklist.md
```

## 它不做什么

- 不给 Skill 打分，不评价好坏。
- 不替你写缺失的部分。每条必需缺口会说明改在哪里、该加什么。
- 不代替在真实任务上运行 Skill。

## 路线图

- [x] [早期试验](docs/validation.md)：对比仅用模型与底图引导的找回结果
- [x] `blindspot` Skill v0.1：问、对照、追踪、个人档案（[skills/blindspot/SKILL.md](skills/blindspot/SKILL.md)）
- [x] 底图：`video`、`video-short`、`video-long`、`writing`、`wechat-article`、`seo-web`，每个节点都有来源
- [x] 底图：`tech-docs`（技术文档与 API 文档）
- [ ] 更多底图：小说（短篇、长篇），以及 YouTube 之外的视频平台
- [x] [benchmark/](benchmark/README.zh-CN.md)：「删环节再找回」的测法和数据，别人可以拿来测自己的方法
- [x] 报告：[20 个公开视频 Skill 缺了什么](reports/video-20.md)（英文）
- [x] 第二个领域（写作），以及做底图的说明：[docs/map-format.md](docs/map-format.md)
- [x] 自己做底图的分步指南：[docs/build-a-map.zh-CN.md](docs/build-a-map.zh-CN.md)

## 视频底图的来源

`skills/blindspot/maps/video.yaml` 引用了下面这些来源，每个节点都写明出自哪个章节、哪条任务或哪项技能。

- O*NET 31.0 任务清单（美国劳工部，CC BY 4.0）。署名原文见英文 README 和底图文件开头。条目在这里做了缩写和重新分组，属于改编，未经 USDOL/ETA 认可。
- ESCO（欧盟委员会）。This publication uses the ESCO classification of the European Commission. 技能名在这里重新分组，属于改编。
- 视频平台的官方创作者文档、公开的课程大纲和教材目录。只引用了章节标题，许可未核实。

还没有收的环节（因为没找到来源）：屏幕录制、工具测评的对比方法。节点要先有来源才能进底图。

## 相关工作

- [SkillFoundry](https://github.com/ma-compbio-lab/SkillFoundry) 用领域树决定给一个库造哪些 Skill。本项目是拿底图审一个已有的 Skill。
- [NVIDIA SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator) 做校验、去重和实测评估，不检查领域覆盖。

## 参与

最有价值的贡献是领域知识：补一个带来源的节点，或者改正一个已有节点。见[底图格式指南](docs/map-format.md)；从头做一张新底图，见[自己做一张领域底图](docs/build-a-map.zh-CN.md)。

## 许可

Skill 指令和辅助代码采用 [MIT 许可](LICENSE)。[底图数据](skills/blindspot/maps/INDEX.md)（含编译缓存）包含第三方材料，并非统一采用 MIT 许可。每个节点指向带署名和许可说明的来源记录。复用底图数据或衍生输出前，请核对适用的来源条款；「未核实」不等于已获许可。
