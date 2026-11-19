# 删环节，再找回

[English](README.md)

这是 [验证记录](../docs/validation.md) 中测法的离线工具。只需 Python 3.8+，
仅用标准库，不调用模型或 API。[示例](example/) 是自行编写的虚构材料，
不代表实际找回效果。

## 方法

1. 选一个成熟的公开 skill，记录链接和版本。出题者不看底图，挑一个或多个环节删除，生成答案。
2. 运行 `remove`，只把 `altered/` 交给检查者，不给原文、`removed/`、答案，
   也不通过文件名透露删了什么。另行运行 blindspot；本工具不会运行检查者。
3. 由人工对照修改版和答案评阅报告，填写 CSV，再计分。检查者与评分者分开。

标题按文字精确匹配，区分大小写，不含 `#` 标记。支持 ATX 和 setext 标题，
忽略围栏代码块内的标题。删除范围从标题行到下一个同级或更高级标题之前。
找不到标题、同名标题不唯一、所选段落重叠都会报错。行号是原文件中从 1 开始的
闭区间；答案记录行数和被删 UTF-8 字节的 SHA-256（保留换行符）。
`--file` 相对 skill 文件夹；重复 `--heading` 可选多个段落。
重复 `--node` 是该次调用中每个删除项共用的可选标注，不自动判定找回。
`--source-url` 记录来源链接，答案也记录本地来源路径。

## 离线示例

在仓库根目录运行，工作目录须尚不存在：

```sh
python3 benchmark/bench.py remove benchmark/example/skill --heading Review --out benchmark/work/example
python3 benchmark/bench.py findings benchmark/example/report.md --out benchmark/work/example/template.csv
# 实际测评需人工填写 template.csv；示例使用已填好的 marks.csv。
python3 benchmark/bench.py score benchmark/work/example/key.json benchmark/example/marks.csv --top 10 --out benchmark/work/example/result.json
python3 benchmark/bench.py summary benchmark/work/example/result.json
python3 -m unittest discover -s benchmark -v
```

预期：找回 1/1，前十找回 1/1，误报 1 条。重跑时换一个 `--out`，工具不覆盖
已有工作目录。`findings` 不带 `--out` 时打印 CSV；`score` 打印 JSON，
可同时保存。`summary` 不带路径时读取 `benchmark/data/*.json`。

## 换一个公开 skill

假设本地检出目录为 `/path/to/skill`：

```sh
python3 benchmark/bench.py remove /path/to/skill --heading 'Final review' --file SKILL.md --node review.check --source-url https://github.com/OWNER/REPO/tree/REVISION/skill --out benchmark/work/trial
# 另行让检查者只读取 benchmark/work/trial/altered。
# 将报告保存为 benchmark/work/trial/report.md，再运行：
python3 benchmark/bench.py findings benchmark/work/trial/report.md --out benchmark/work/trial/marks.csv
# 人工填写 marks.csv 的 match 和 verdict 后再计分。
python3 benchmark/bench.py score benchmark/work/trial/key.json benchmark/work/trial/marks.csv --top 10 --out benchmark/work/trial/result.json
python3 benchmark/bench.py summary benchmark/work/trial/result.json
```

这里的路径、标题和 URL 是占位示范，要换成实际检出的版本和标题。
上面的离线示例无需下载或联网。

## 评分规则

`findings` 只读取 `## Findings`，支持 `### Needed`、
`### Worth considering`、`### Minor` 三档，条目为编号加粗标题，可带
`Map node:` 行，格式见 [C07](../reports/code-5/C07.md)。编号应贯穿全部档位，
不能每档从 1 重来。

- `match` 填一个答案 ID（如 `R1`），或留空。一个发现确实对应多个删除项时，
  此格式只能计一个；其余判断另作记录。
- `verdict` 必填 `real` 或 `false`。`real` 是实际缺口；`false` 是修改后的
  skill 已经覆盖的内容。真实缺口可以不匹配答案；误报不能匹配答案。
- 找回率 = 任意排名中找回的不同答案项数 / 答案总项数。重复发现不重复计分。
  空答案的找回率为 `null`。
- 前 N 找回数只计算排名不大于 N 的匹配，默认 N=10，同样去重。
  要测任意排名找回，须提供完整排序列表。
- 误报数是 `false` 行数，不是不匹配答案的行数；另列未找回的答案项。
  未知 ID、无效 verdict、非正数或重复排名都会报错。空发现列表找回零项。

比较另一种方法时，让独立检查者看同一个修改版，例如直接问「缺哪些环节？
最多列十项」。不给答案，也不给另一份报告。转成同样的 Findings 格式，
用同一答案人工标注，分别计分。记录提示词、模型和底图版本、运行次数及评分理由。
重复运行可观察波动，不要把两次平均与一次运行混称为同一种统计。

## 已有数据

[validation-2026-11.json](data/validation-2026-11.json) 转录自
[docs/validation.md](../docs/validation.md)，不是新跑的实验。
运行 `python3 benchmark/bench.py summary` 可打印表格。

| 测试 | 方法 | 前十找回 | 两次运行共有项 |
|---|---|---|---|
| 1：视频 | 仅模型 | 11/12 次机会 | 约 20/30 |
| 1：视频 | 底图引导 | 10/12 次机会 | 约 27/30 |
| 2：EU MDR | 仅模型 | 9/12 次机会 | 约 25/30 |
| 2：EU MDR | 底图引导 | 8/12 次机会 | 约 26/30 |
| 3：两个领域 | 仅模型，两次平均 | 10/12 项 | 未记录 |
| 3：两个领域 | 底图引导，两次平均 | 9/12 项 | 未记录 |
| 3：两个领域 | 组合 skill，一次 | 11/12 项 | 未记录 |

测试 1、2 各删六项，各查两次，所以每种方法各有十二次机会。测试 3 的组合
skill 对这十二个删除项查一次；十一项找回均在各报告前十，报告各有 22–36 项。
JSON 含删除项列表及测试 1 的三个 skill 链接。来源未给测试 2 的 skill 名称
和链接。误报数未记录，用 `null` 而不是零。来源在测试 3 写了「十二个修改版
skill」，但限制部分写六个 skill；保留总计，不臆造逐 skill 明细。

限制：两个领域、六个 skill、十二个删除项、一个模型（Claude Sonnet），
同一人评分并判断两次共有项。法规领域并不十分冷门。测试 2 的底图在主持者
知道删除项后从 63 节点扩为 171 节点（扩图 agent 未见答案），可能有利于底图
方法。组合方法只跑一次，不能据此断言更好。这里没有原始答案和逐次评分，
不能用本工具独立重算这些汇总数。

## 发布什么

发布结果、固定版本的来源链接、删除标题及哈希、方法和提示词、评分及理由。
不发布第三方 skill 原文或修改版。`benchmark/work/` 已忽略，原文和删除文本
只保存在本地；分享答案前检查本地路径。此目录中只有自行编写的虚构示例包含
skill 文本。
