# 自己做一张领域底图

[English](build-a-map.md) | 中文

这份指南讲怎么做一张新的领域底图：从选领域，到检查脚本通过。字段说明见 [map-format.md](map-format.md)（英文），这里讲方法。例子都来自最近加入的五张底图：[`seo-web`](../skills/blindspot/maps/seo-web.yaml)、[`spreadsheet-finance`](../skills/blindspot/maps/spreadsheet-finance.yaml)、[`data-analysis`](../skills/blindspot/maps/data-analysis.yaml)、[`tech-docs`](../skills/blindspot/maps/tech-docs.yaml) 和 [`research-paper`](../skills/blindspot/maps/research-paper.yaml)。对照着这几个文件读：下面每个例子都能在里面找到。

| 底图 | 来源数 | 分组数 | 节点数 |
|---|---|---|---|
| `seo-web` | 29 | 12 | 74 |
| `spreadsheet-finance` | 13 | 10 | 49 |
| `data-analysis` | 8 | 9 | 45 |
| `tech-docs` | 15 | 11 | 75 |
| `research-paper` | 23 | 8 | 76 |

## 1. 选领域

一张底图描述一类工作的环节和要点，用来检查做这类工作的 Skill 的领域覆盖。开始之前：

- **先看已有的底图。** 读 [maps/INDEX.md](../skills/blindspot/maps/INDEX.md)，或者运行 `python3 skills/blindspot/scripts/blindspot.py maps`。如果已有底图覆盖了这类工作的大部分，做一张 `extends` 它的细分底图比新做一张通用底图省事（见第 5 步）。
- **写工作，不写工具。** 五张底图都在 `scope` 字段里写明是哪类工作、哪些不在范围内。`data-analysis` 是 "Answering a question with data"（用数据回答问题）；`spreadsheet-finance` 是 "Building or changing a spreadsheet model or financial analysis"（搭建或修改表格模型、财务分析）。
- **先确认有来源。** 所有底图的规则都是：没有来源的节点不进底图。如果这个领域找不到职业数据库条目、标准、法规、教材或课程目录、官方文档，底图就会是空的。先找来源，再写节点。
- **提一个[底图请求](https://github.com/emptygpt/skill-blindspot/issues/new?template=map-request.yml)**，免得两个人做同一张。新底图不应该需要改 `SKILL.md`（见 [CONTRIBUTING.md](../CONTRIBUTING.md)，英文）。

## 2. 找来源，逐个节点写出处

从来源到节点，不要反过来。先列出来源说从业者要做什么，再分组。

**五张底图用到的来源类型：**

| 类型 | 底图里的例子 |
|---|---|
| 职业数据库 | O*NET 任务条目：`data-analysis` 的 D1 *Data Scientists (15-2051.00)* |
| 技能分类 | ESCO 技能名：`tech-docs` 引用了 "identify ICT user needs" |
| 专业团体指引 | `spreadsheet-finance` 引用的 ICAEW *20 principles for good spreadsheet practice* |
| 政府方法指引 | `data-analysis` 引用的 *The AQuA Book* |
| 官方文档 | `seo-web` 引用的 Google web.dev *Web Vitals* |
| 规范或标准 | `tech-docs` 引用的 OpenAPI Specification v3.1.1 和 WCAG 2.2 |
| 同行评审论文 | `data-analysis` 引用的 Wilson et al. (2017), *Good enough practices in scientific computing* |
| 法规 | `data-analysis` 引用的《中华人民共和国个人信息保护法》条款 |

**来源要自己读过。** 打开页面，确认那段文字确实在。凭记忆想到的、或者模型建议的来源，在你读到之前都不算来源。

**来源在文件的 `sources` 列表里只记一次**，六个字段都要有：`id`、`title`、`publisher`、`url`（HTTP 或 HTTPS）、`retrieved`（`YYYY-MM-DD` 格式日期）和 `licence`。例如 `seo-web` 里的：

```yaml
- id: W1
  title: "Web Vitals"
  publisher: "Google web.dev"
  url: "https://web.dev/articles/vitals"
  retrieved: '2026-11-19'
  licence: "CC BY 4.0 (page content); code samples Apache 2.0"
```

许可没有核实，就写 `not verified`，并说明引用了什么。`spreadsheet-finance` 对 ICAEW 就是这样写的：`not verified; only titles, headings and short statements cited`。

**每个节点都用 `ref` 和 `locator` 写出处。** `locator` 必须是来源里真实出现的文字，读者可以拿去搜。五张底图里的写法：

- O*NET 任务条目，带 Task ID：`'Task 21831: Identify business problems or management objectives that can be addressed through data analysis.'`（`data-analysis` 的 `question.problem`）；
- 带编号的原则：`'6. Tailor the design and documentation to the needs of the audience and dependent processes.'`（`spreadsheet-finance` 的 `inputs.assumptions`）；
- 标题：`"Core Web Vitals"`（`seo-web` 的 `page-experience.cwv`）；
- 对象名或准则名：`"Security Scheme Object"`（`tech-docs` 的 `api-description.security`）；
- ESCO 技能名：`identify ICT user needs`（`tech-docs` 的 `doc-planning.readers`）。

一个节点可以引用多个来源。节点的 `title` 和 `description` 用自己的话写。只引用标题和简短的句子，许可不允许的来源不要抄正文。

**署名。** 来源的许可要求署名时，把署名写在文件开头的 "Licence and attribution" 部分，`data-analysis` 和 `spreadsheet-finance` 里的 O*NET 署名就是例子。来源要求相同方式共享时也写在这里：`tech-docs` 只引用了 CC BY-SA 的 GitLab 文档的标题，并说明从中派生的部分按相同条款共享。

## 3. 读不到的来源，列为「还没有收」

有些来源读不到：要登录、标准要付费、服务器报错或返回空页面。不要引用它们，也不要凭你以为它们写了什么去写节点。改为在文件开头的 "Not yet covered" 列表里加一条，写明原因，方便别人以后找来源。你认为应该在底图里、但读过的来源都不支持的环节，也写进这个列表。

五张底图里的例子：

- `seo-web`：ESCO 的搜索引擎优化专家职业页面 "returned a temporary-issue shell"，Bing 指南的网址 "returned an application shell"，两者都没有引用。
- `data-analysis`：ASA 伦理指南的页面和 PDF "returned HTTP 403"，EUR-Lex 的 GDPR 页面 "returned empty responses"；文件开头还写明个人信息保护法的节点不能代替 GDPR。
- `spreadsheet-finance`：XBRL 规范 "returned no readable content"，所以标签和报送校验没有收。
- `tech-docs`：ISO/IEC/IEEE 26514 和 26515 是付费标准，ISO 页面读不到。
- `research-paper`：COPE 核心实践的网址返回的是会员行为准则，所以更正和撤稿流程没有收。

同一批底图里还有两个习惯：

- 同样的内容有可读的版本，就引用那个版本并写明。`research-paper` 引用了 ASA 公开发布的 2016 年原则，因为期刊文章返回 HTTP 403。
- 能读到但故意不用的来源，写明原因。`tech-docs` 写了 "Not used on purpose: Diataxis (licence not found, as in the software map)"。

## 4. 和已有底图划清边界

一个 Skill 常常要对照不止一张底图，所以底图要写明相邻的工作归谁。边界写在两处：`scope` 字段（"Out of scope: ..."），以及文件开头，写出另一张底图的名字，必要时写出它的节点编号。

- `data-analysis` 把分析代码（SQL、Python、R 的 notebook 和脚本）作为分析产物留在本图，把搭建生产软件、数据管道和机器学习服务交给 `software`，把撰写和发布包含结果的文章交给 `writing`。
- `spreadsheet-finance` 把备忘录的文字质量交给 `writing`，把 VBA、Python、Office Script 代码的工程实践交给 `software`，保留表格特有的要点，例如工作簿变更控制和公式审计。
- `seo-web` 把单篇文章的内容交给 `writing`，把代码修改、安全、测试和发布交给 `software`。它点明了和 `writing` 的 `head.metadata-seo` 重叠的地方，自己只管站点层面的决定。
- `tech-docs` 有一段 "Boundaries with other maps"。它列出 `software` 里已经在问「改动有没有同步更新文档」的节点（`documentation.technical-docs`、`documentation.review-docs`），以及负责版本号和更新日志的节点（`release.versioning`、`release.breaking-changes`、`release.changelog`），并写明一个任务既是代码修改又要写文档时，两张底图都要对照。
- `research-paper` 接下了 `writing` 底图列为不在范围内的学术论文写作，把通用的软件工程实践（版本控制、代码评审、测试、CI）留给 `software`。

同一个来源适合两张底图时，两张都可以引用，只要每个节点讲的是本图的工作。`tech-docs` 写明了有些 O*NET 27-3042.00 和 ESCO 技术写作者的条目被 `tech-docs` 和 `writing` 同时引用。

## 5. 通用底图还是细分底图

这五张都是通用底图。一个已有领域里更窄的一类工作，可以做成细分底图，像 `video-short`、`video-long` 扩展 `video`，`wechat-article` 扩展 `writing`。细分底图：

- 在 `map` 下写 `extends: <id>`；
- 只列通用底图里没有的来源，也可以引用通用底图的来源；
- 在 `exclude` 下列出不适用的通用节点，每条附一句理由（`video-short` 排除 `pre.budget` 的理由是 "Phone-based short-form is normally made without a production budget to estimate."）；
- 加上自己的分组和节点，每个节点都要有自己的来源。

两种写法的 YAML 见 [map-format.md](map-format.md)（英文）。

## 6. 写文件

新建 `skills/blindspot/maps/<id>.yaml`，文件名必须和 `map.id` 一致。五张底图的结构相同，照着写：

1. 开头的注释：本图的规则、范围和边界、许可和署名、"Not yet covered"。
2. `map`：`id`、`title`、`version`、`updated`、`scope`。
3. `sources`：每个来源一条记录。
4. `groups`：每组有 `id`（小写字母、数字和连字符，以字母开头）和 `title`，下面是 `nodes`。节点编号是组编号、一个点、一个短名，例如 `question.problem`。

每个节点要有 `id`、`title`、`description`，`sources` 里至少一条。`applies_when` 可选，用于只在某些情况下才相关的节点。`keywords` 也可选：一组词，辅助脚本的 `prepare` 命令在把 Skill 的行和节点配对时也会搜这些词。`tech-docs` 用了它，例如 `doc-planning.readers` 上的 `audience` 和 `user needs`。

然后把底图登记到大家找得到的地方：在 [maps/INDEX.md](../skills/blindspot/maps/INDEX.md)、[README.md](../README.md) 和 [README.zh-CN.md](../README.zh-CN.md) 的底图表格里各加一行。

## 7. 运行检查

装好 PyYAML，在仓库根目录运行检查脚本：

```bash
python3 -m pip install pyyaml
python3 scripts/check_maps.py
```

它逐张检查底图，每张输出一行，例如 `ok   data-analysis: 45 nodes`。以下情况会失败（不止这些）：

- `map.id` 和文件名不一致，或者缺 `title`、`version`、`updated`、`scope`；
- 来源记录缺六个字段之一，`url` 不是 HTTP(S)，或者 `retrieved` 不是 `YYYY-MM-DD` 日期；
- 来源、分组或节点编号在本图或它的通用底图里重复；
- 节点没有来源、引用了未定义的来源编号，或者 `locator` 为空；
- `extends` 指向不存在的底图或形成循环，或者 `exclude` 写了不存在的通用节点。

辅助脚本读的是 `skills/blindspot/maps/maps.json`，所有底图的编译副本。YAML 检查通过后，写出新副本再检查一次：

```bash
python3 scripts/check_maps.py --write
python3 scripts/check_maps.py      # 最后一行应为 "ok   maps.json is up to date"
```

不要手改 `maps.json`。合并时它冲突了，随便取一边，再运行一次 `--write`。

然后用辅助脚本试一下这张底图，它只用标准库：

```bash
python3 skills/blindspot/scripts/blindspot.py maps
python3 skills/blindspot/scripts/blindspot.py checklist --map <id> --groups
python3 skills/blindspot/scripts/blindspot.py sources --map <id> <node-id>
python3 skills/blindspot/scripts/blindspot.py prepare <a-skill-folder> --map <id> --out worksheet.md
```

拿这个领域里一个真实的 Skill 跑 `prepare`，看节点的标题、描述和关键词能不能找到你预期的那些行。每次推送和拉取请求都会在 Python 3.8 和 3.12 上运行同样的 `check_maps.py`、单元测试和这些冒烟测试（[check-maps.yml](../.github/workflows/check-maps.yml)）。

## 8. 提拉取请求

在描述里列出来源和网址，写明哪些要登录、要付费或读不到。文件里的 "Not yet covered" 列表要保持最新。见 [CONTRIBUTING.md](../CONTRIBUTING.md)（英文）。

## 清单

- [ ] 看过已有底图；写好范围和不在范围内的内容
- [ ] 每个来源都读过，六个字段齐全
- [ ] 每个节点都有出处，`locator` 在来源里真实存在
- [ ] 许可要求署名的，已写在文件开头
- [ ] 读不到或找不到的来源，列在 "Not yet covered"
- [ ] 和相邻底图的边界，写在 `scope` 和文件开头
- [ ] 在 `maps/INDEX.md`、`README.md` 和 `README.zh-CN.md` 里各加一行
- [ ] 先 `python3 scripts/check_maps.py --write`，再 `python3 scripts/check_maps.py` 通过
