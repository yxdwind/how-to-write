# 怎样写作 (how-to-write)

> 从《怎样写作》（任仲然著，党建读物出版社，"机关工作实务丛书"第三本）提炼的 Agent 技能库——不是书的摘要，而是一套可执行的写作方法论工具箱。

## 这是什么

一个 OpenClaw / Claude Code / Copilot CLI / Amp 兼容的 skill 目录，把全书十二讲的写作方法论拆解为：

- **命名框架与原则**——保留作者原话表述
- **可执行的操作步骤**——每讲的方法都写成"何时用 / 怎么做"
- **反面模式**——作者反复警示的错误做法及原因
- **实例拆解**——书中经典案例的压缩重述
- **决策速查表**——把作者的判断逻辑浓缩成一眼可查的规则

双用途设计：

1. **给 AI 用**——写公文、讲话稿、调研报告、述职报告、汇报发言、随笔杂文、自媒体文章，或修改润色文稿时，按本 skill 的方法论干活
2. **给自己用**——按讲次或主题快速检索书中观点与方法

## 使用案例

一句话调用示例（完整实战见 [examples/](examples/) 目录）：

| 你说 | AI 会做什么 |
|------|------------|
| "周四的季度会讲话稿，20 分钟，先给准备清单再出粗纲" | 三个吃透清单→粗纲→初稿→五度自检（[案例1](examples/example-1-leadership-speech.md)） |
| "调研材料在这，按真实深高写成调研报告" | 定类型→挑干货→并列结构→修改检查单（[案例2](examples/example-2-research-report.md)） |
| "年底述职，把我的流水账重构成 10 分钟口播版" | 三属性校准+三胜法重构+十二字开头（[案例3](examples/example-3-duty-report.md)） |
| "三份发言稿：汇报提纲/学习发言/对照检查，逐个过" | 先决性改造+三个结合+对照检查五点（[案例4](examples/example-4-briefing-and-review.md)） |
| "这篇文稿给我做一次到位的修改，别当校对员" | 四层顺序+两个基准+何其芳12项过筛+求准标红（[案例5](examples/example-5-revision.md)） |
| "按自媒体方法写篇公众号文，标题开篇金句都要" | 吸引力标题×5+经典开篇定调+淘金句不过火（[案例6](examples/example-6-wechat-article.md)） |

## 目录结构

```
how-to-write/
├── SKILL.md              # 核心框架 + 讲次索引 + 主题索引（入口文件）
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
├── examples/             # 六个完整实战案例（讲话稿/调研报告/述职/汇报/修改/自媒体）
├── glossary.md           # 全书术语表
├── patterns.md           # 方法与模式全集
├── cheatsheet.md         # 决策速查表（最实用的一层）
├── overview.html         # 可视化总览页
└── README.md
```

## 用法

**Agent 里**（OpenClaw / Claude Code 等，将本目录放入技能目录后）：

- 直接说"用怎样写作这个 skill 起草一份工作总结"→ 加载核心框架
- 问具体主题，如"调研报告怎么开头""述职报告忌讳什么"→ 自动定位到对应讲次细读
- 问"ch12"→ 加载第十二讲（修改文稿文章经验谈）

**人读**：从 [SKILL.md](SKILL.md) 的索引进入，按需点开各讲。

## 生成方式

由 OpenClaw book-to-skill 流水线生成：213 页扫描版 PDF → OCR 全文提取（AutoClaw OCR）→ 结构分析 → 逐章提炼 → 安全扫描。提炼遵循"提取结构，不抄原文"原则，框架命名保留作者原话。

## 机关工作实务四部曲

- [how-to-run-meetings](https://github.com/yxdwind/how-to-run-meetings) —— 《怎样开会》（任仲然）
- [how-to-research](https://github.com/yxdwind/how-to-research) —— 《怎样调研》（任仲然）
- how-to-write（本仓库）—— 《怎样写作》（任仲然）
- [smart-notes](https://github.com/yxdwind/smart-notes) —— 《卡片笔记写作法》（申克·阿伦斯）

## 版权说明

本书版权归原作者、译者及出版社（党建读物出版社）所有。本仓库仅包含对书中方法论的提炼与转述（合理使用），不包含原文文本。
