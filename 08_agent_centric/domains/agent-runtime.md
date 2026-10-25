# Domain Tree · Agent Runtime（Agent 执行运行时 / 分布式运行时）

> 建立：2026-10-26（周一，Runtime 周第一天）｜ 类型：领域能力树/基线
> 定位：命中"高效、可信、可控"的 **Execution 维度**；承接 Harness/治理 周已验证的执行隔离/身份/凭据外注证据（MXC/Strands Box/Google 侧印证）；直接对应 **TeamMind（Java 多 Agent 团队运行时）** 与 Tafcm（本地优先）。
> 树与图分工：本文件是 **Tree**（层级组织与任务分解）；跨域复用/依赖见 `08_agent_centric/capabilities/graph.md`（Capability Graph，agent-runtime 领域能力已登记：agent-memory/failure-recovery/multi-agent-orchestration/protocol-interop/scheduling/self-improvement/state-persistence）。
> JIT 原则：不建百科，只展开与任务相关、且当前缺失的分支。

## 一、领域树（Agent Runtime）

```
Agent Runtime（Agent 执行运行时）
├── A. Durable Execution 与失败恢复
│   ├── A1. DurableAgent 步骤持久化（Dapr Agents：每步 reasoning/tool call 持久化，崩溃后从最后完成步骤恢复，不重放已完成 LLM/工具调用）
│   ├── A2. 双 state store 分层（agent-memory 会话历史 vs agent-workflow 执行状态——执行状态与记忆分离，Memory 周架构参照）
│   ├── A3. workflow-backed 执行模型（workflow 引擎 + actor 模型 + Dapr sidecar，provider-agnostic：Ollama 默认本地/OpenAI/Anthropic/Mistral 可换）
│   ├── A4. durable-harness 品类（Vercel durable-harness 10-21 开源：包装 Pi/OpenCode/Claude Code/Codex，session 存 durable log；Notion Gen-6 10-22：queue-backed worker loop 24h 无人值守——durable execution 10 月下旬主流化信号）
│   └── A5. 长时程生命周期（跨系统重启存活、sleep-cycle 级任务）
├── B. 分布式多 Agent 编排
│   ├── B1. pub/sub 多 agent 编排（Dapr pub/sub：事件驱动 agent 通信）
│   ├── B2. AgentRunner HTTP 接口（POST /agent/run 返回 WORKFLOW_ID；GET /agent/instances/{id} 查状态/结果）
│   ├── B3. actor 模型并发（virtual actor：pod 崩溃/迁移后 rehydrate 完整执行状态，零手动恢复逻辑）
│   ├── B4. 协议层互操作（A2A agent 间 / MCP 工具 / PAP agent-to-business 三协议格局）
│   └── B5. TeamMind 对照（Java 多 Agent 团队运行时：权限模型 vs dsh/MXC 对照——Harness 周遗留 B 缺口）
├── C. 状态持久化与存储
│   ├── C1. 多后端 state store（Redis / PostgreSQL / Cassandra）
│   ├── C2. 执行状态 vs 会话记忆分层（agent-workflow vs agent-memory；Memory 周深化）
│   ├── C3. Hyperdisk 持久化（Google Agent Compute Engine：agent 状态盘）
│   └── C4. checkpoint-restore（copy-on-write 内存共享 + fast checkpoint：thinking 阶段暂停 microVM）
├── D. 资源隔离与密度
│   ├── D1. Titanium IPU 硅基隔离（Google Agent Compute Engine：硬件级隔离边界，独立 guest kernel+root，Cloud Hypervisor）
│   ├── D2. microVM / gVisor 双选择（Agent Substrate：K8s 零信任运行时）
│   ├── D3. 10x 计算密度（Agent Substrate 基准：20 万 agent / 500 activations/sec / <500ms suspend-resume）
│   ├── D4. 生产评估信号（Dapr launch 报道：400 分布式 multi-agent 工作流生产评估）
│   └── D5. 本地优先路径（Dapr Conversation API 默认 Ollama 本地——Tafcm 端侧方向一致）
├── E. 运行时身份与网络策略
│   ├── E1. SPIFFE 身份（Agent Substrate：workload identity）
│   ├── E2. 短时凭据（每 microVM 独立短时凭据 + 密码学验证 ID）
│   ├── E3. egress 外注服务凭据（Google Agent Compute Engine：egress 外注——Strands Box→MXC→Google 跨厂商共识的运行时侧落地）
│   ├── E4. egress 代理网络策略（Agent Substrate 零信任网络）
│   └── E5. 治理扩展（Agent Gateway / Registry / Identity；端点本地治理 preview；token 成本治理模型路由；OTel agentic 语义约定）
└── F. 生命周期管理
    ├── F1. suspend-resume（<500ms suspend/resume：Agent Substrate 基准）
    ├── F2. 崩溃恢复（Dapr：重启按同一 WORKFLOW_ID 续跑，Ctrl+C 中断恢复 demo）
    ├── F3. 伸缩与调度（actor 迁移、K8s 调度、10x 密度）
    └── F4. 可观测（tracing / Diagrid Dev Dashboard workflow 执行历史 / OTel 语义约定）
```

## 二、基线：已知 vs 缺口 vs 相邻未覆盖

### 已知（系统已覆盖，不重复收集）
| 锚点 | 状态 | 说明 |
|---|---|---|
| Dapr Agents（CNCF × NVIDIA） | [cand] **A**（头号锚点） | 开源分布式 Agent 运行时（github.com/dapr/dapr-agents）：DurableAgent 步骤持久化 + 双 state store + actor + pub/sub；**验证计划：quickstart `03_durable_agent_http.py` 中断恢复实测**（卡内 §4 已定） |
| Google Agent Compute Engine + Agent Substrate | 官方一手精读（10-24 兜底移交，**二号锚点**） | Titanium IPU 硅基隔离 microVM + 短时凭据 + egress 外注 + Hyperdisk + copy-on-write/fast checkpoint；Agent Substrate 开源 K8s 零信任（10x 密度/500 activations/sec/<500ms suspend-resume/SPIFFE+egress 代理），开源满足 validated 门槛 |
| Personal Agent Protocol / PAP | [cand] A（协议/身份层相邻） | OAuth-based agent-to-business 身份授权（poppy.json 发现+agent 自标识+客户授权）；v0.1 规范 10 月内交付 |
| DeepSeek Harness (dsh) | **validated**（S） | credentials seam/sandbox/approval/session-telemetry——Runtime 相邻对照（seam 迁移参考） |
| Microsoft Execution Containers / MXC | **validated**（A） | OS 级执行隔离（AppContainer/Seatbelt/Bubblewrap/MicroVM 四后端）——运行时隔离对照 |
| Strands Box（AWS） | **validated**（A） | OS 级行为遏制沙箱 + 凭证外挂网关——egress 外注微软/AWS 侧印证 |
| Agent Harness / Control Plane 范式 | [cand] S | Omnigent + MS Agent Framework（1.0 GA 10-13）+ 六职责——编排/控制面相邻 |
| OpenCode | 已知 | headless HTTP coding agent；10-17 API key 泄露事件（B+ 级教训：凭证集中存储攻击面，对照 egress 外注） |
| Vercel durable-harness + durable agent state stack（10-20/21 开源）｜Notion Gen-6（10-22） | 兜底 10-25 B 级移交 | durable execution 主流化信号：agent logic/execution environment/persistence 三层分离（Vercel）；queue-backed worker loop 24h 无人值守（Notion）——**周五验证对照池** |

### 缺口（本领域内未覆盖，Runtime 周重点）
| 缺口 | 证据 | 优先级 |
|---|---|---|
| Dapr Agents 实际验证（quickstart 中断恢复 demo 跑通 + 双 state store 语义核对） | Dapr 卡 §4 验证计划 | **A（周五 10-30 优先）** |
| Agent Substrate 开源复现对照（K8s 部署/SPIFFE/egress 代理/密度基准是否可复现） | 官方博客一手；开源仓库待 clone | A（周五候选） |
| durable execution 品类横向（Dapr vs Vercel durable-harness vs Notion Gen-6：步骤持久化粒度/恢复语义/部署形态） | 10-25 兜底移交信号 | A（周五对照池） |
| TeamMind 权限模型 vs dsh/MXC 对照（Harness 周遗留 B 缺口） | 03_project_landscape；Harness 能力树缺口节 | B（Runtime 周内顺带） |
| Agent Mesh 身份层落地（Harness C3 缺口：MXC Entra coming soon 未落地） | Harness 能力树缺口节 | B（Runtime 侧 SPIFFE 是候选答案，Agent Substrate 可对照） |

### 相邻未覆盖（本领域外、可外推）
| 相邻方向 | 与 Runtime 的连接 | 归属周 |
|---|---|---|
| Memory 实现层 | 执行状态（agent-workflow）vs 会话记忆（agent-memory）分层 | Memory 周 |
| Computer Use / Browser | browser-harness / 浏览器权限治理 | Computer Use/Browser 周 |
| 本地 / 边缘 AI | Dapr 本地 Ollama 默认、Tafcm 离线优先 | AI Infra/本地边缘（接 Tafcm） |
| Agent Evaluation / Observability | Runtime 可观测（tracing/OTel 语义约定）回灌评测隔离 C1/C4 | 已闭环（Evaluation 周） |

## 三、本周验证计划（周五 10-30 用，2-3 个高价值候选）
1. **Dapr Agents quickstart 实测**（`03_durable_agent_http.py`）：杀进程→重启→验中断恢复不重放已完成调用；核对双 state store 配置（agent-memory vs agent-workflow）
2. **Agent Substrate 开源对照**：clone/文档级核对架构（SPIFFE/egress 代理/密度基准），判断本地 K8s 复现可行性
3. **durable execution 品类横向**：Dapr Agents vs Vercel durable-harness vs Notion Gen-6 三向对照（步骤持久化粒度/恢复语义/部署形态/适用场景）

## 四、任务视图（Capability Tree 动态实例化锚点）
- 任务类型 `agent-runtime-task` → 实例化本领域树，JIT 只展开缺失分支
- 引擎映射：graph.md 已登记 agent-runtime 领域能力（agent-memory / failure-recovery / multi-agent-orchestration / protocol-interop / scheduling / self-improvement / state-persistence）

## 五、回灌目标（周六 10-31）
- 更新 `08_agent_centric/capabilities/graph.md`（runtime 相关跨域边：durable-state / runtime-identity / lifecycle-management 等）
- 更新 `04_connections/README.md`（Dapr Agents → TeamMind 等连接升级）
- 候选决策：Dapr Agents → validated？（验证完成后）；Agent Substrate → 建卡/升卡；durable-harness 品类 → 决策
