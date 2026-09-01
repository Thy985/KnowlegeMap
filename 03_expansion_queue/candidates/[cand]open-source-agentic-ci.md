# 候选证据卡 · [cand] 开源 Agentic CI（Pullfrog AI / 阿里 OpenCodeReview）

> 状态：`[cand]` ｜ 分类：Agentic CI 工业化（A7） ｜ 发现：2026-09-01 ｜ 等级：**B**

## 一句话定位
CodeRabbit 类托管 AI 代码审查出现开源替代：Pullfrog（Zod 作者出品，纯 GitHub Actions 运行）与阿里 OpenCodeReview（21K stars，token 成本约为 Claude Code 的 1/9）——与我自研的 AgenticCI 资产直接对照。

## 1. 它是什么 / 解决什么问题
- **Pullfrog AI**（Colin McDonnell/Zod 作者）：模型无关、agent 化、纯 GitHub Actions 跑，PR 审查 + issue 分流 + CI 修复，无托管第三方；400+ stars（2025 末预览起）["https://www.infoq.com/news/2026/05/pullfrog-ai-github/"]
- **阿里 OpenCodeReview**：21K stars，token 成本约 Claude Code 的 1/9；对 Java 的 NPE/线程安全等通用 agent 易漏项做专项审查；支持 CI/CD 集成["https://blog.csdn.net/Number241/article/details/164015815"]
- 格局参考：Qodo Merge（开源自托管，最高基准 F1 60.1%）、Greptile（整仓上下文）、DeepSource/Kodus-AI（AST+LLM 混合）["https://baeseokjae.github.io/posts/coderabbit-alternatives-comparison-2026/"]

## 2. 与我的知识/项目关系
- **AI Code Review 资产族 / AgenticCI**：外部开源产品可对照验证我的自研方案（成本、假阳性、Java 专项）
- **Tafcm/silver-shield 的 CI 门禁**：可试用 Pullfrog（GitHub Actions 内跑）或自建 OpenCodeReview
- 证据纪律：Qodo Merge 60.1% F1 提供"基准可量化"的参照

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（InfoQ + 多源评测） |
| 来源 | https://www.infoq.com/news/2026/05/pullfrog-ai-github/ ｜ https://baeseokjae.github.io/posts/coderabbit-alternatives-comparison-2026/ |
| 验证方式 | 在 KnowlegeMap 或一个小项目试跑 Pullfrog/OpenCodeReview，与我自研方案对比 |
| 预期 | 2026-10 |

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
