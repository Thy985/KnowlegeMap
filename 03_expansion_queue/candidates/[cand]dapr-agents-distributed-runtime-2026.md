# 候选对象证据卡 · Dapr Agents（CNCF Dapr × NVIDIA 分布式 Agent 运行时，Durable Execution）

> 状态：`[cand]` ｜ 关联方向：**Agent Runtime（下一深耕领域，接 TeamMind）**/ 多 Agent 编排 / Memory ｜ 日期：2026-10-20（兜底扫描捕获，非当前深耕领域）

## 一句话定位
Dapr Foundation（CNCF graduated 分布式应用运行时，微软发起）在 NVIDIA 工程协作下正式推出的**开源分布式 Agent 运行时**（`github.com/dapr/dapr-agents`）：把 Dapr 成熟的 **workflow 引擎（durable execution）+ actor 模型 + state store + pub/sub** 搬到多 agent 系统——agent 的每一步推理与工具调用都持久化，进程被杀后从最后完成步骤恢复，不重复执行已完成的 LLM/工具调用，直接面向 K8s 上的大规模 agent swarm。

## 1. 它解决什么问题
- 多 agent 从单节点脚本走向分布式 K8s 集群时的"分布式系统危机"：进程崩溃/重启导致长时程 agent 工作流从头重跑、重复执行已完成的昂贵 LLM/工具调用、状态丢失
- 主流 agent 框架（LangChain/AutoGen/CrewAI 类）在**编排层**解决"谁做什么"，但缺**基础设施层**的可靠执行、持久化状态、actor 并发、服务间 pub/sub——Dapr Agents 用 Dapr sidecar 补齐这层
- TeamMind 这类多 agent 运行时自研要面对的 durable state / 恢复 / 并发问题，Dapr 提供企业级成熟实现

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（官方文档+仓库）**：`github.com/dapr/dapr-agents`（Apache 2.0，Python）；Dapr 官方文档 docs.dapr.io/developing-ai/dapr-agents 已上线 Getting Started（2026-10-14）与 Core Concepts（v1-18）；2026-10-16 Dapr Foundation 与 NVIDIA 正式宣布 launch（集成 NeMo）["https://dailyaiworld.com/public/blogs/dapr-nvidia-launch-dapr-agents-distributed-durable-state"]
- **FACT（核心机制，官方 Getting Started）**：
  - **`DurableAgent`**：LLM+工具包在 workflow-backed 执行模型中，**每步 reasoning/tool call 持久化**
  - **双 state store**：`agent-memory`（会话历史，Redis state store）+ `agent-workflow`（durable execution state，需 `actorStateStore: "true"`）
  - **中断恢复**：`dapr run` 中 Ctrl+C 杀掉进程，重启后按同一 WORKFLOW_ID GET `/agent/instances/{id}`，工作流从最后持久化步骤继续，**不重放已完成的 LLM/工具调用**
  - **AgentRunner**：HTTP 暴露（`POST /agent/run` 返回 WORKFLOW_ID；`GET /agent/instances/{id}` 查状态/结果），支持 pub/sub 驱动的 agent、多 agent workflow、tracing
  - **Dapr sidecar 模式**：provider-agnostic，Dapr Conversation API 支持 Ollama（默认本地）/OpenAI/Anthropic/Mistral，YAML 组件换模型不改代码
  - Diagrid Dev Dashboard 可可视化检查 workflow 执行历史
- **与已覆盖对象不重复**：MS Agent Framework 1.0（Semantic Kernel+AutoGen 统一，编排框架）、OpenCode（headless HTTP coding agent）、Harness-ControlPlane S 卡（NVIDIA OpenShell 等）均为框架/harness 层；**Dapr Agents 是基础设施运行时层（durable workflow/actor/state store）**，是 TeamMind 这类多 agent 运行时的底层对照而非同类竞品

## 3. 与我的连接
- **连接的项目**：
  - **TeamMind（Java 多 Agent 运行时）——最强连接**：durable execution（步骤持久化+崩溃恢复）、actor 模型并发、多 agent pub/sub 编排正是 TeamMind 生产化必须面对的分布式问题；Dapr 提供可参照的成熟设计（即便 Java 侧走自己的实现，Dapr 的双 state store/工作流恢复语义是设计基线）
  - **Tafcm（Dart 本地 LLM）**：Dapr Agents 默认 Ollama 本地推理 + provider-agnostic Conversation API，本地优先路径与 Tafcm 端侧方向一致
  - silver-shield / 引擎：workflow 状态可审计（每步持久化 + Diagrid 可视化）为可观测/审计链提供基础设施层支持
- **连接的知识点**：Harness 六职责中的 **state/observation 职责**（workflow 状态持久化）；Agent Runtime 领域的 durable execution 范式（与 Temporal 式工作流同线，但 Dapr 是 agent 原生 API：DurableAgent/AgentRunner）；Memory 与 execution state 分层（会话记忆 vs 执行状态双 store——**Memory 周的架构参照**）
- **潜在收益**：作为 **Runtime 周（Harness 之后，接 TeamMind）的头号锚点候选**；quickstart 可直接跑通（03_durable_agent_http.py 中断恢复 demo），满足 validated 门槛（公开代码可复现）

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | 官方 Getting Started ["https://docs.dapr.io/developing-ai/dapr-agents/dapr-agents-getting-started/"]；Core Concepts ["https://v1-18.docs.dapr.io/developing-ai/dapr-agents/dapr-agents-core-concepts/"]；仓库 `https://github.com/dapr/dapr-agents`；launch 报道 ["https://dailyaiworld.com/public/blogs/dapr-nvidia-launch-dapr-agents-distributed-durable-state"] |
| 证据等级 | FACT（官方文档+开源仓库+基金会 launch） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① Runtime 周（10-26 起）跑 quickstart `03_durable_agent_http.py`：杀进程→重启→验中断恢复；② 精读 DurableAgent/双 state store/AgentRunner 实现；③ 对照 TeamMind 权限/状态模型产出差异分析 |
| 预期完成时间 | 2026-10 下旬（Runtime 周），当前仅建卡占位 |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [ ] 维持观察
- [ ] 拒绝（原因）
