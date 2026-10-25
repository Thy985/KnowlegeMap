# 深耕扫描日志 · 2026-10-26（Personal Tech Radar · Runtime 周 Day1 · 建能力树/基线）

> 周一分工：建该领域能力树/基线（对照 Tech Map 标注已知/缺口/相邻未覆盖），更新 current_focus.md。不做增量扫描、不建新卡。

## 领域聚焦
- **当前领域**：Runtime（Agent 执行运行时 / 分布式运行时），周起始 2026-10-26（10-25 周日小结换域决定）
- **领域定位**：命中"高效、可信、可控"Execution 维度；承接 Harness/治理 周已验证证据（MXC/Strands Box/Google egress 外注）；直接对应 TeamMind（Java 多 Agent 团队运行时）

## 建树产出：`08_agent_centric/domains/agent-runtime.md`

### 领域树 A-F 六层
| 层 | 主题 | 核心内容 |
|---|---|---|
| A | Durable Execution 与失败恢复 | DurableAgent 步骤持久化 / 双 state store（agent-memory vs agent-workflow）/ workflow-backed 执行模型 / durable-harness 品类（Vercel/Notion 主流化信号）/ 长时程生命周期 |
| B | 分布式多 Agent 编排 | pub/sub 编排 / AgentRunner HTTP 接口 / actor 模型并发 / 协议层互操作（A2A/MCP/PAP）/ TeamMind 对照 |
| C | 状态持久化与存储 | 多后端 state store（Redis/PG/Cassandra）/ 执行状态 vs 会话记忆分层 / Hyperdisk / copy-on-write+fast checkpoint |
| D | 资源隔离与密度 | Titanium IPU 硅基隔离 / microVM+gVisor 双选择 / 10x 密度（20 万 agent/500 activations/sec）/ 400 生产工作流信号 / 本地优先（Ollama 默认） |
| E | 运行时身份与网络策略 | SPIFFE / 短时凭据 / **egress 外注（Strands Box→MXC→Google 共识的运行时侧落地）** / egress 代理 / 治理扩展（Gateway/Registry/Identity/OTel） |
| F | 生命周期管理 | suspend-resume（<500ms）/ 崩溃恢复（WORKFLOW_ID 续跑）/ 伸缩调度 / 可观测（Diagrid tracing） |

### 基线三栏
- **已知锚点 8 项**：Dapr Agents（A 卡头号）、Google Agent Compute Engine/Substrate（二号）、PAP（相邻）、dsh validated、MXC validated、Strands Box validated、Harness-ControlPlane S 卡、OpenCode（含 10-17 泄露 B+ 教训）
- **缺口 5 项**：① Dapr quickstart 实测（A，周五优先）② Agent Substrate 开源复现对照（A）③ durable execution 品类横向（Dapr vs Vercel vs Notion，A）④ TeamMind 权限模型 vs dsh/MXC 对照（B，Harness 周遗留）⑤ Agent Mesh 身份层落地（B，SPIFFE 候选答案）
- **相邻未覆盖**：Memory（执行状态 vs 会话记忆分层）、Computer Use/Browser、本地边缘 AI（Dapr 本地 Ollama → Tafcm）

## 文件变更
- **新建** `08_agent_centric/domains/agent-runtime.md`（领域树+基线+周五验证计划+任务视图+周六回灌目标）
- **修改** `07_radar_watch/current_focus.md`（周一 ✅；历史表 Runtime 行补 Day1 产出）
- **修改** `_INDEX.md`（追加本日志行）

## 结论
**New**（Runtime 周 Day1：新领域能力树/基线建立完成——A-F 六层 + 8 已知锚点 + 5 缺口 + 周五验证计划就绪；未做增量扫描，未建新卡）
