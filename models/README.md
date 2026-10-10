# models/ —— 范文拆解卡

起草前读对应卡：先看好的长什么样，再动笔。每张卡 = 名篇结构骨架 + 文风特征 + 合成示范稿（标注非原书内容）。

## 内置卡（8 文体全覆盖）

| 文件 | 文体 | 对应章节 | 文体筛 |
|------|------|---------|--------|
| [official-document.md](official-document.md) | 规范性公文 | ch06 | rubrics/official.md |
| [speech-leadership.md](speech-leadership.md) | 领导讲话稿 | ch07 | rubrics/speech.md |
| [research-report.md](research-report.md) | 调研报告 | ch08 | rubrics/research.md |
| [duty-report.md](duty-report.md) | 述职报告 | ch09 | rubrics/speech.md（述职节） |
| [briefing-speech.md](briefing-speech.md) | 汇报稿/发言稿/对照检查 | ch10 | rubrics/speech.md（汇报发言节） |
| [essay.md](essay.md) | 随笔/杂文 | ch11 | rubrics/essay-selfmedia.md（随笔节） |
| [wechat-article.md](wechat-article.md) | 自媒体/公众号 | ch11 | rubrics/essay-selfmedia.md（自媒体节） |

## local/ —— 本地范文（不入仓库）

`models/local/` 放你自己积累的真实范文，已被 .gitignore 排除。约定：

1. **命名**：`<文体>-<标识>.md`，如 `speech-leadership-王局长退休讲话.md`。
2. **每篇范文配拆解**（同文件末尾）：骨架（块结构）、文风（3 个特征）、金句位、可复用点。
3. **优先级**：起草同一文体时，local 真实范文优先于内置卡——真实范文永远比合成示范值钱。
4. **版权**：范文只放本地自用；仓库内置卡坚持"提取结构，不抄原文"（最长引述不超 31 字红线）。
