# 候选证据卡 · [cand] Multi-Agent 框架选型终局（LangGraph v1.0 / CrewAI / AG2 维护 / MS Agent Framework）

> 状态：`[cand]` ｜ 分类：多 Agent 编排（S5） ｜ 发现：2026-09-01 ｜ 等级：**B**

## 一句话定位
2026 多 Agent 框架格局收敛：LangGraph（v1.0 GA）成企业生产默认、CrewAI 成低门槛角色编排、AutoGen 更名 AG2 进入维护模式；Microsoft Agent Framework 1.0 是新企业默认候选——为 TeamMind 的"选型与拓扑"决策提供终局参照。

## 1. 关键事实（2026）
| 框架 | 范式 | 生产成熟度 | 2026 状态 |
|---|---|---|---|
| **LangGraph** | 有状态图 + supervisor | 最高 | v1.0 GA；Q1 2026 出现在 34% 的 1000+ 人企业生产架构文档中["https://growthengineer.ai/blog/ai-agent-frameworks-compared"] |
| **CrewAI** | 角色/团队 | 中 | 45.9K stars；学习曲线最低["https://growthengineer.ai/blog/ai-agent-frameworks-compared"] |
| **AutoGen / AG2** | 群聊对话 | 过渡 | 2025 起维护模式；仅遗留研究["https://www.aiplusinfo.com/blog/langgraph-vs-crewai-vs-autogen/"] |
| **Microsoft Agent Framework** | SDK+Runtime（.NET/Python 同一套概念） | 高 | 1.0 于 2025-10 GA；Build 2026 加 Harness/Hosted Agents/CodeAct["https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/"] |
| **Mastra** | TypeScript 类型化 workflow | 中 | TS 侧主导（22-24K stars）["https://alicelabs.ai/en/insights/best-ai-agent-frameworks-2026"] |

## 2. 与我的知识/项目关系
- **TeamMind**：为"选型与拓扑"决策提供 2026 终局数据；但注意 TeamMind 是"组织 CLI agent 团队"（Codex/Claude/Aider），与"框架内多 agent"是不同层次——框架选型需区分
- 与 **A2A 卡** 交叉：LangGraph/CrewAI 构建的 agent 可通过 A2A 互操作
- 与 **Harness 卡** 交叉：框架之上还有 meta-harness 层

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（多源 2026 对比 + 官方） |
| 来源 | https://www.n-ix.com/langgraph-vs-crewai-vs-autogen/ ｜ https://growthengineer.ai/blog/ai-agent-frameworks-compared |
| 验证方式 | 产出 TeamMind 的框架接入评估（是否引入框架、还是保持自研 harness + 协议层） |
| 预期 | 2026-10 |
> **雷达增量（2026-09-16，编排范式变化）**：
> - **OpenClaw 2026.9.2（2026-09-05 发布）**：**默认开启并发 sub-agent 编排（swarms）**——结构化结果 + 实时进度，保留 opt-out/工具限制/独立 Code Mode 开关；同时**权限模型变更：跨 agent 会话访问默认扩大**——"default swarms multiply both productivity and responsibility"["https://openclawnews.tech/openclaw-agent-control-stack-swarms-2026/"]["https://ramadigital.id/en/blog/openclaw-2026-9-2-swarm-default-cross-agent-session-access"]
> - **Swarms v15 'Akira'（2026-09-01）**：**DynamicToolLoader**（工具 schema 目录化延迟加载——50 工具 agent 只发 1 个 schema，抗上下文膨胀）+ 重建真实 agent harness（16 内置工具）+ 多 agent 结构统一 typed chat turns["https://www.swarms.ai/blog/swarms-v15-akira-release"]
> - **SwarmBench（arXiv 2608.30661）**：LLM 能否当 agent swarm orchestrator 的系统评测 + **SwarmExp**（从任务执行积累可复用编排经验）["https://arxiv.org/pdf/2608.30661"]
> - **含义**：① **"swarm 默认开启"成为编排框架新默认**——但权限模型同步扩大（跨 agent 会话访问），对照 09-14 RSAC"coding agent 100% 可注入"，campus_order 升级 OpenClaw 2026.9.2 前需先审权限变更清单；② **动态工具加载**是工具注册表新思路（TeamMind 可参考，控制上下文预算）；③ SwarmBench 补"编排者能力"评测维度（关联 agentic-benchmarks 卡）
> **雷达增量（2026-09-18，OpenClaw 2.0 + 信任模型文档化）**：
> - **OpenClaw 2.0（2026.9.4，09-11 发布）**：更安全回滚（核心/插件变更在隔离候选状态预演后再激活）、插件统一工作空间、cloud 会话可预先准备、**read-only 配置**、慢会话诊断——运营/升级风险面收敛["https://openclaw-lab.ru/news/oficialnye_novosti_openclaw/1-0-3"]["https://raw.githubusercontent.com/openclaw/openclaw/main/appcast.xml"]
> - **OpenClaw SECURITY.md Operator Trust Model 正式化（09-08 更新）**：**单 gateway 不建模为多租户对抗性用户边界**——认证的 Gateway 调用者视为可信操作者；localhost/loopback Control UI + gateway secret 认证会话同属该可信桶——信任模型边界首次文档化（含 Incident Response Plan + NVIDIA/Tencent 安全贡献者）["http://raw.githubusercontent.com/openclaw/openclaw/HEAD/SECURITY.md"]
> - **exec-approvals 默认值（09-17 文档确认）**：Gateway/node host 默认 `full`；**sandbox host 默认 `deny`**——沙箱执行默认拒绝["https://docs.openclaw.ai/pl/tools/exec-approvals"]
> - **含义**：① OpenClaw 信任模型文档化 + 沙箱默认拒绝 = "策略→执行"移动（对应 agent-firewall 品类确定性主线）；② **campus_order 部署需先答"谁能认证访问 gateway"**——单 gateway=可信操作者意味着 gateway 凭据即全权限；③ 2026.9.4 回滚/read-only 增强降低升级风险，升级路径从 2026.9.2 直接评估 2026.9.4
> **雷达增量（2026-09-22，OpenClaw 2026.9.5 发布）**：
> - **OpenClaw 2026.9.5（09-21 报道）**：**Atomic Updates + Plugin Hot Reload + Specialist AI Agent Teams**——onboarding 可一键创建专业 agent 团队（预设四角色：Chief of staff/Researcher/Writer/Reviewer，也可单专业 agent），团队以提案形式呈现由用户确认——**"专业 agent 团队"从手动编排走向引导式创建**["https://theinfobytes.com/openclaw-2026-9-5-atomic-updates-ai-agent-teams"]
> - **含义**：① 2026.9.2 swarms 默认开启 → 2026.9.5 专业团队引导创建——**编排从"能力"走向"开箱即用工作流"**（对照 09-16 SwarmBench"编排者能力"评测维度）；② **plugin hot reload + atomic updates**降低升级/插件迭代风险（campus_order 升级路径可从 2026.9.4 直接评估 2026.9.5）；③ 四角色预设（Chief of staff/Researcher/Writer/Reviewer）与 TeamMind 的"团队运行时"设计直接对照——验证"专家化分工+验证者"模式是行业共识

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
