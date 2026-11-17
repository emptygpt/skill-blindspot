# skill-blindspot

**找出你的 Agent Skill 自己不知道缺了什么。**

[English](README.md) | 中文

格式检查工具看的是写法。实测评估看的是 Skill 在你想到的任务上能不能跑通。这两样都不会告诉你：有一个环节你从头就没想到。

`skill-blindspot` 检查一个 Agent Skill（含 `SKILL.md` 的文件夹）缺了哪些环节。它先问模型缺什么，再拿一张**领域底图**逐条对照。底图来自人已经整理好的知识：职业任务数据库、教材和课程目录、平台官方文档、法规原文。你得到一张逐条对照表：哪些已覆盖、哪些很浅、哪些没有，附上在你的 Skill 里找到的原文行，每个节点都有出处。

> **状态：v0.1。** Skill 和第一张底图（视频制作，86 个带来源的节点）已经在仓库里，在 12 个删过环节的 Skill 上测过。还很早期，报告格式可能会变。

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

细分底图在通用底图之上扩展：只写新增的节点，并列出不适用的通用节点。每个文件开头都列了**还没有收**的环节，原因是没找到来源。视频底图引用了 YouTube、TikTok、B 站和抖音的官方页面，以及美国 FTC 和《互联网广告管理办法》，抖音创作者学习中心没有读到。

想补节点或加底图，见 [docs/map-format.md](docs/map-format.md)（英文）。提 PR 前运行 `python3 scripts/check_maps.py`。

## 我们先测了什么

动手之前，我们先测了最直接的质疑：直接问模型缺什么，不就行了？我们从两个领域的 6 个公开 Skill 里删掉环节，做了盲测。

**直接问模型，24 个被删项找回 20 个。带底图的检查找回 18 个。** 底图不会找到更多。它给每条缺口配上出处和原文证据，并且给出完整的对照表，不只是前 10 条。完整做法和数字见 [docs/validation.md](docs/validation.md)（英文）。

同样 12 个被删项，合并后的 Skill 跑一次找回 11 个。

所以这个工具两样都用：模型负责发现，底图负责给依据、给对照表，并记下你故意不做的条目。

## 怎么工作

1. **问。** 模型凭自己对这个领域的了解，列出它认为 Skill 缺的环节。
2. **对照。** 底图的每个节点逐条对照 Skill，标成四种状态之一：已覆盖、很浅、没有、故意不做，并引用原文行作证据。底图是一棵 YAML 树，每个节点有编号、上级、来源、链接和许可。没有来源的节点不许进底图。
3. **追踪。** 顺着每一步的产出，看后面有没有步骤用到它。这能找到底图里没列的缺口。
4. **个人档案。** 缺口不是都要补。不适用于你的条目，写进一个小的档案文件，理由可写可不写，下次检查会照办。公共底图对所有人相同，个人档案只记你自己的情况。

「公共目录加个人档案」的分法在其他行业有成熟先例，例如 NIST 网络安全框架的档案机制，以及 OSCAL 的目录和档案。

## 它不做什么

- 不给 Skill 打分，不评价好坏。
- 不替你生成缺失的部分。
- 不代替在真实任务上运行 Skill。

## 路线图

- [x] 验证：带出处的底图，比直接问「缺什么」找到的更多吗？没有。见 [docs/validation.md](docs/validation.md)
- [x] `blindspot` Skill v0.1：问、对照、追踪、个人档案（[skills/blindspot/SKILL.md](skills/blindspot/SKILL.md)）
- [x] 底图：`video`、`video-short`、`video-long`、`writing`、`wechat-article`，每个节点都有来源
- [ ] 更多底图：小说（短篇、长篇），以及 YouTube 之外的视频平台
- [ ] `benchmark/`：「删环节再找回」的测法和数据，别人可以拿来测自己的方法
- [ ] 报告：公开的视频 Skill 最常缺哪些环节
- [x] 第二个领域（写作），以及做底图的说明：[docs/map-format.md](docs/map-format.md)

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

最有价值的贡献是领域知识：补一个带来源的节点，或者改正一个已有节点。第一张底图发布时会写明格式。

## 许可

代码：MIT。领域底图沿用各来源的许可，逐节点标注。
