# 候选证据卡 · [cand] hermes-agent（Nous Research 开源 Agent 框架）
> 状态：`[cand]` ｜ 分类：Agent Framework / Open-Source（S5） ｜ 发现：2026-09-02（雷达） ｜ 等级：**B**（实测后评估是否升 A）
## 一句话定位
Nous Research 的 hermes-agent（MIT，~217k★）：2026 年增长最猛的开源 Agent 框架之一，五层洋葱架构 + ~50 内置工具（terminal/file/browser/search/code-exec/image-gen/TTS/transcription/**MCP client**/subagent delegation/cron），内置多后端浏览器自动化（Browser Use / Browserbase / Firecrawl），Skills/Memory 设计与 Claude Code 几乎同源。
## 1. 它是什么 / 解决什么问题
- 提供开箱即用的 agent harness（含 browser automation、MCP、cron、子代理），解决"快速起步一个能干活、能上网、能记忆、能自学的 agent"的工程门槛["https://github.com/NousResearch/hermes-agent"]
- **一手核验（2026-09-02）**：GitHub `NousResearch/hermes-agent` ✅（官方 README + 文档 + CONTRIBUTING）、官方文档 hermes-agent.nousresearch.com ✅、独立技术评测 gist ✅
- **关键数据修正**：雷达卡当时记 ~57k★（2026-04 快照），实测最新 ~217k★（v0.18.2，2026-07-07）——增长速度远超预期
- 架构：五层洋葱（Foundation 基座/LLM 提供商适配、Model tools、Toolsets…）；Memory = 文件化 MEMORY.md + USER.md（含注入/外泄扫描）；Skills = Markdown+YAML（自我改进）["https://gist.github.com/michaeloboyle/10461598db36066e4c366413d5416f83"]
## 2. 为什么现在值得关注（活跃度证据）
- ~217k★（2026-09-01 快照），2026-02 发布，版本已迭代到 v0.18+，release 频繁（v2026.3.17 含 CDP /browser connect、Vercel AI Gateway、Centralized Provider Router）["https://newreleases.io/project/github/NousResearch/hermes-agent/release/v2026.3.17"]
- 多提供商：Nous Portal / OpenRouter(200+) / Anthropic / Bedrock / Azure AI Foundry / HF / Copilot / 本地(llama.cpp/MLX/vLLM)["https://www.intraview.ai/explore/NousResearch/hermes-agent/story"]
- 进入 ClawBench 等 harness 评测基准（一等公民）["https://github.com/reacher-z/ClawBench/issues/70"]
## 3. 与我的连接
- **连接的项目**：OpenClaw 生态对照（campus_order）、agent 框架选型（multiagent-framework-2026.md）、MCP 生态（内置 MCP client）、agent-attention（通知/cron 能力对照）
- **连接的知识点**：Agent Framework 格局、Skills 体系（与我的 Claude Code Skills 资产直接同构）、Memory 实现（文件化 vs Mem0 抽取式对照）
- **潜在收益**：纳入"开源 agent 框架格局"对照样本；其 MCP client + Skills 自改进 + 记忆注入扫描的设计值得精读
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/NousResearch/hermes-agent ｜ https://hermes-agent.nousresearch.com/ ｜ https://newreleases.io/project/github/NousResearch/hermes-agent |
| 证据等级 | **FACT（官方 GitHub + 官方文档 + release 记录核验通过）** |
| 验证方式 | 读 README/架构/源码（memory 注入扫描、skills 自改进、MCP client）→ 对照 OpenClaw 能力边界 → 判断是否纳入框架选型对比 |
| 预期完成时间 | 2026-09 内 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
