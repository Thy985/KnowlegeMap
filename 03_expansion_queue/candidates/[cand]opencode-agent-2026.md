# 候选证据卡 · [cand] OpenCode（headless HTTP 架构的顶级开源 Coding Agent / Harness）
> 状态：`[cand]` ｜ 分类：Agent Harness / Coding Agent（S3 Harness 关注域） ｜ 发现：2026-09-09（雷达 #8） ｜ 等级：**A**
## 一句话定位
OpenCode 是增长最快的开源 coding agent / harness 之一（**~147k★、650 万月活开发者，2026-01 与 GitHub Copilot 官方合作**），核心差异是 **client/server 架构 + headless Hono HTTP 服务 + Vercel AI SDK**——与 Claude Code / DeepSeek Harness 的单体 CLI 路线不同的"解耦可扩展"路线，是 harness 架构谱系的重要对照样本。
## 1. 它是什么 / 解决什么问题
- 痛点：主流 agent harness（Claude Code 系）是单体终端应用，难以被其他工具/平台嵌入与编排；OpenCode 把 agent 能力做成无头 HTTP 服务，任何客户端（TUI/Desktop/IDE/第三方）可接入["https://agentic-ai.readthedocs.io/en/latest/AgenticFrameworks/ai-coding-agents/"]
- **架构**：client/server 解耦——服务端 headless Hono HTTP server + Vercel AI SDK，客户端（终端 TUI / 桌面 / IDE）只是接入面；MIT 开源
- **生态信号**：2026-01 GitHub Copilot 合作（付费 Copilot 订阅者可认证直连）；147k★/6.5M 月活（2026-04 口径）["https://agentic-ai.readthedocs.io/en/latest/AgenticFrameworks/ai-coding-agents/"]
- 同线对照：**Claw Code**（Claude Code 架构 clean-room 重写，Python+Rust，48k★）、xAI **Grok Build**（Rust 编码 agent+CLI，2026-07 开源）["https://claw-code.codes/"]["https://www.thenextgentechinsider.com/pulse/xai-releases-grok-build-open-source-coding-agent-and-cli"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-09）**：agentic-ai 文档 OpenCode 数据 ✅（147k★/Copilot 合作）、claw-code.codes ✅、awesome-ai-agents-2026 收录 ✅
- 增长速率罕见：开源项目史上最快增长之一，Copilot 合作 = 主流厂商背书
- "headless 化"趋势：与 MCP stateless、harness 服务化同向——agent 能力从"终端应用"走向"可编程服务"
## 3. 与我的连接
- **连接的项目**：**TeamMind**（多运行时编排——OpenCode 的 headless HTTP 接入面是"异构 harness 编排"的直接参考）；**Tafcm**（本地 agent 服务化架构对照）；与 DeepSeek Harness（validated）同赛道不同架构——谱系对照
- **连接的知识点**：Agent Harness 架构（S3）、五维模型 Runtime 维度、Agent 服务化
- **潜在收益**：补上 harness 架构谱系中"解耦服务化"分支；其 Copilot 生态合作模式是 Agent 商业化的参考
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/opencode-ai/opencode ｜ https://agentic-ai.readthedocs.io/en/latest/AgenticFrameworks/ai-coding-agents/ ｜ https://claw-code.codes/ |
| 证据等级 | **FACT（GitHub + 独立文档站数据核验）**（star 数需以 GitHub API 复核为准） |
| 验证方式 | 本机装 OpenCode 跑一个真实任务 → 评估 headless 接入面是否能作为 TeamMind 的外部运行时插件 |
| 预期完成时间 | 2026-09/10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
