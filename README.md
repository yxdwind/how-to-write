# 怎样写作 (how-to-write)

![Release](https://img.shields.io/github/v/release/yxdwind/how-to-write) ![License](https://img.shields.io/github/license/yxdwind/how-to-write) ![Agent Skills](https://img.shields.io/badge/Agent-Skills-blue)

> 从《怎样写作》（任仲然著，党建读物出版社，"机关工作实务丛书"第三本）提炼的 Agent 技能库——不是书的摘要，而是一套"方法论 + 工序 + 自检 + 评测"的可执行写作系统。

## 这是什么

一个符合 Agent Skills 标准、跨工具兼容的 skill 目录（Claude Code / OpenClaw / Codex / Cursor / Cline / CodeBuddy / ZCode 等；安装脚本自动探测，其余工具手动复制 SKILL.md 目录即可）。四层结构：

**方法论层**（全书十二讲拆解）

- **命名框架与原则**——保留作者原话表述
- **可执行的操作步骤**——每讲的方法都写成"何时用 / 怎么做"
- **反面模式**——作者反复警示的错误做法及原因
- **实例拆解**——书中经典案例的压缩重述
- **决策速查表**——把作者的判断逻辑浓缩成一眼可查的规则

**工序层**（强制写作工序）

- 起草任务五步走：**接稿问诊 → 立意送审 → 备料盘点 → 按文体成稿 → 交付前自检**（落地原书"提纲早出手、初稿晚出手""三分写七分改"）
- 红线：数据、事实、引文必须溯源到用户材料或注明来源，查不到出处的标【待核实】——禁止编造

**范文与自检层**

- **7 张范文拆解卡，八文体全覆盖**——原书实例的结构骨架 + 文风特征 + 一篇按原书标准写的合成示范稿
- **5 张交付前自检筛**——通用筛 12 项（立意/数据/语言）+ 公文、讲话稿、调研、随笔自媒体四张文体筛，逐项过筛再交付

**评测层**（基准评测，防退化）

- 任务简报 + 硬指标/盲评评分表 + 跑分全记录；改 skill 后跑回归
- 评测结论诚实口径见下方[质量与评测](#质量与评测)

双用途设计：

1. **给 AI 用**——写公文、讲话稿、调研报告、述职报告、汇报发言、随笔杂文、自媒体文章，或修改润色文稿时，按本 skill 的工序和方法论干活
2. **给自己用**——按讲次或主题快速检索书中观点与方法

## 安装

**方式一 · Agent Skills 标准（推荐）**

```bash
npx skills add yxdwind/how-to-write -g
```

**方式二 · 安装脚本（自动探测 Claude Code / OpenClaw / Codex / Cursor / Cline 等已装目录）**

```powershell
# Windows PowerShell
irm https://raw.githubusercontent.com/yxdwind/how-to-write/main/install.ps1 | iex
```

```bash
# macOS / Linux
curl -fsSL https://raw.githubusercontent.com/yxdwind/how-to-write/main/install.sh | bash
```

**方式三 · 手动**

```bash
git clone https://github.com/yxdwind/how-to-write.git
# 把仓库目录（含 SKILL.md）复制到你的 AI 技能目录，
# 如 ~/.agents/skills/how-to-write 或 ~/.claude/skills/how-to-write
```

更新已装的 skill：`npx skills update how-to-write`，或重跑安装脚本（加 -Force/--force 覆盖）。固定版本下载见 [Releases](https://github.com/yxdwind/how-to-write/releases)。

## 使用案例

一句话调用示例（完整实战见 [examples/](examples/) 目录）：

| 你说 | AI 会做什么 |
|------|------------|
| "周四的季度会讲话稿，20 分钟，先给准备清单再出粗纲" | 问诊清单→立意卡送审→备料盘点→成稿→双筛自检（[案例1](examples/example-1-leadership-speech.md)） |
| "调研材料在这，按真实深高写成调研报告" | 定类型→挑干货→并列结构→修改检查单（[案例2](examples/example-2-research-report.md)） |
| "年底述职，把我的流水账重构成 10 分钟口播版" | 三属性校准+三胜法重构+十二字开头（[案例3](examples/example-3-duty-report.md)） |
| "三份发言稿：汇报提纲/学习发言/对照检查，逐个过" | 先决性改造+三个结合+对照检查五点（[案例4](examples/example-4-briefing-and-review.md)） |
| "这篇文稿给我做一次到位的修改，别当校对员" | 四层顺序+两个基准+何其芳12项过筛+求准标红（[案例5](examples/example-5-revision.md)） |
| "按自媒体方法写篇公众号文，标题开篇金句都要" | 读范文卡→成稿→M1–M6 逐项自检+金句密度检查（[案例6](examples/example-6-wechat-article.md)） |

## 目录结构

```
how-to-write/
├── SKILL.md              # 核心框架 + 强制工序入口 + 讲次索引 + 主题索引（入口文件）
├── workflow.md           # 强制写作工序：五步走（问诊→送审→备料→成稿→自检）执行细则
├── chapters/             # 十二讲逐章拆解（按需加载）
│   ├── ch01-writing-is-not-hard.md          # 第一讲 写作其实并不难
│   ├── ch02-thinking-logic-patterns.md      # 第二讲 思维 逻辑 规律
│   ├── ch03-conception-outline.md           # 第三讲 立意 构思 提纲
│   ├── ch04-material-structure-language.md  # 第四讲 材料 结构 语言
│   ├── ch05-narration-argument-exposition.md # 第五讲 叙述 议论 说明
│   ├── ch06-official-document-writing.md    # 第六讲 规范性公文的写法
│   ├── ch07-leadership-speech-writing.md    # 第七讲 领导讲话稿的写法
│   ├── ch08-research-report-writing.md      # 第八讲 调研报告的写法
│   ├── ch09-duty-report-writing.md          # 第九讲 述职报告的写法
│   ├── ch10-briefing-speech-writing.md      # 第十讲 汇报稿和发言稿的写法
│   ├── ch11-essay-column-wechat-writing.md  # 第十一讲 随笔、杂文及自媒体写作
│   └── ch12-revision-experience.md          # 第十二讲 修改文稿文章经验谈
├── models/               # 范文拆解卡（起草前读）：名篇骨架+文风+合成示范稿
│   ├── official-document.md                 # 规范性公文（ch06 实例）
│   ├── speech-leadership.md                 # 领导讲话稿（ch07 实例）
│   ├── research-report.md                   # 调研报告（ch08 实例）
│   ├── duty-report.md                       # 述职报告（ch09 实例）
│   ├── briefing-speech.md                   # 汇报稿/发言稿（ch10 实例）
│   ├── essay.md                             # 随笔/杂文（ch11 实例）
│   ├── wechat-article.md                    # 自媒体/公众号（ch11 实例）
│   └── local/                               # 本地范文（.gitignore，不入仓库）
├── rubrics/              # 交付前自检筛（交付前逐项过筛）
│   ├── general.md                           # 通用筛 12 项：立意/数据/语言
│   ├── official.md                          # 公文筛：三要点+分体规则+三大病
│   ├── speech.md                            # 讲话稿筛：含述职、汇报发言节
│   ├── research.md                          # 调研报告筛：真实深高+工序 9 项
│   └── essay-selfmedia.md                   # 随笔/自媒体筛
├── evals/                # 基准评测（改 skill 后跑回归）
│   ├── README.md                            # 评测方法与判定规则
│   ├── scoring.md                           # 评分表：硬指标 60 + 盲评 40 + 双轨分解
│   ├── briefs/                              # 任务简报（3 个文体）
│   └── runs.log.md                          # 跑分记录（4 轮 + 对照实验全数据）
├── examples/             # 六个完整实战案例（讲话稿/调研报告/述职/汇报/修改/自媒体）
├── glossary.md           # 全书术语表
├── patterns.md           # 方法与模式全集
├── cheatsheet.md         # 决策速查表（当…就…判断规则+阈值+危险信号）
├── overview.html         # 可视化总览页
└── README.md
```

## 用法

**Agent 里**（OpenClaw / Claude Code 等，将本目录放入技能目录后）：

- 直接说"用怎样写作这个 skill 起草一份讲话稿"→ 走五步工序：先问清场合时长听众 → 立意卡给你确认 → 备料盘点 → 成稿 → 末尾附自检报告
- 问具体主题，如"调研报告怎么开头""述职报告忌讳什么"→ 自动定位到对应讲次细读
- 问"ch12"→ 加载第十二讲（修改文稿文章经验谈）

**人读**：从 [SKILL.md](SKILL.md) 的索引进入，按需点开各讲。

## 质量与评测

仓库内置了一套基准评测（[evals/](evals/)）：同一任务简报分别用"带本 skill"与"不带"两种方式生成，匿名盲评打分（硬指标 60 + 软评 40），改 skill 后跑回归。目前已跑 4 轮 + 1 次对照实验，全部数据公开在 [runs.log.md](evals/runs.log.md)。

**诚实口径的结论**：

- **流程验证通过**：评测方法本身跑通了——盲评抓出过基线卷编造引语（逐处核数）、抓出过 skill 卷字数不达标，暴露的问题都回流成了筛规则修复（如 S2 时长筛"简报指定时长优先"）。
- **对照实验的关键发现**：给基线只加一句中性要求（"文末附自查报告"），其产出即可达到很高的溯源纪律水平——**"有无溯源纪律"主要取决于"是否被要求自查"，不是装不装本 skill 的差别**。本 skill 的真实增量在于：把自查固化为不可跳过的工序、提供文体筛的专业检查项（时长基准/建议对应/定性限定）与范文对标。
- **效果声明未下**：单任务分差波动大（−14 ~ +32），3 个简报只够流程验证；"装了平均好多少"的量化结论待简报库扩充（每文体 ≥3 个独立任务）后再下。

**版权与忠实度**：三线审计（通用体检 + 原书忠实度 + 发布就绪）完成，12 章对原书覆盖度 85%–92%，与原书最长公共子串 31 字（单句级），无段落级抄录；详见 [AUDIT_REPORT.md](AUDIT_REPORT.md)。

## 生成方式

方法论层由 OpenClaw book-to-skill 流水线生成：213 页扫描版 PDF → OCR 全文提取（AutoClaw OCR）→ 结构分析 → 逐章提炼 → 安全扫描。提炼遵循"提取结构，不抄原文"原则，框架命名保留作者原话。

工序、范文卡、自检筛、评测为 v1.1.x 质量工程阶段增设：三层设计对应写作质量的三类瓶颈——只给规则不给工序则流程失控，只给工序不给范文则口吻跑偏，只交付不自检则编造与超时无法拦截。

## 相关技能

**机关工作实务丛书**（任仲然）三部曲：

- [how-to-run-meetings](https://github.com/yxdwind/how-to-run-meetings) —— 《怎样开会》
- [how-to-research](https://github.com/yxdwind/how-to-research) —— 《怎样调研》
- how-to-write（本仓库） —— 《怎样写作》

延伸阅读：

- [smart-notes](https://github.com/yxdwind/smart-notes) —— 《卡片笔记写作法》（申克·阿伦斯）提炼的卡片笔记方法论技能

## 版权说明

《怎样写作》版权归作者及出版社（党建读物出版社）所有。本仓库仅包含对书中方法论的提炼与转述（合理使用）：不含成段原文，仅保留框架命名与短句引述。仓库自身内容（提炼、组织、示例、代码）以 [MIT 许可](LICENSE) 发布。
