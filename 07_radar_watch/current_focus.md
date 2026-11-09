# Current Focus（雷达当前聚焦领域）

> 定时任务每次运行先读本文件，确定当前领域与本周进度。换域后更新本文件。

## 当前领域：Memory（Agent 记忆实现层 / 记忆治理）

- **周起始日**：2026-11-09（周一）
- **状态**：active（周一建能力树/基线；上一领域 Runtime 已于 11-08 周日闭环换域）
- **为什么现在做它**：领域顺序 Evaluation→Harness→Runtime→Memory 的下一站；Runtime 周已确认「执行状态（workflow store/snapshot）≠ 会话记忆（memory store）」的分层（Dapr 双 state store、Substrate actor snapshot）；且 11-07 兜底捕获的「跨会话持久记忆注入跨 ChatGPT/Claude/Gemini 存活、近半缓解未落地」证明记忆已是真实攻击面——Memory 周不能只比检索分数，必须同时建信任边界。

## 目标
- 建立 Memory 能力树/基线：记忆分层（工作/情景/语义/程序性）、写入策略（抽取 vs 全量）、检索与压缩、生命周期（遗忘/冲突/版本化）、作用域与租户隔离、注入防御与审计
- 验证 2-3 个高价值候选（Mem0 / Zep-Graphiti / Letta 三级记忆），并核对基准分数口径（LoCoMo / LongMemEval / BEAM 的厂商自报 vs 独立复测）
- 闭环：候选 → 验证 → 回灌 index/connections/能力树

## 已知锚点（不重复收集）
- **`03_expansion_queue/candidates/[cand]agent-memory-2026.md`（S 卡）**：Mem0（抽取式，v3 算法，托管平台 94 分 ≠ 开源 SDK 口径）/ Zep-Graphiti（时序知识图谱 + ABAC/保留/审计）/ Letta（Core-Recall-Archival 自编辑）/ A-MEM（Zettelkasten）/ MemEval 排名（Memory-R1 0.389 等）；两条基准批判：长上下文模型碾压记忆管线、LoCoMo 6.4% 得分污染
- Mem0 × dsh 原生记忆插件（2026-08-24，跨会话 memory bank）；Letta Code（memory-first coding agent，Apache-2.0）
- Runtime 周结论（分层对照）：Dapr `agent-memory` vs `agent-workflow` 双 store；Agent Substrate actor snapshot=执行状态、可 suspend/resume，但**不是**跨会话记忆
- 11-07 兜底事件日 13：跨会话记忆注入（ChatGPT/Claude/Gemini），持久化后门形态

## 本周进度（每日分工）
- [x] 周一（11-09）：建 Memory 能力树/基线（`08_agent_centric/domains/agent-memory.md`）+ 更新本文件——**已完成**：七层树（A 分层/B 写入/C 检索压缩/D 生命周期/E 作用域/F 信任边界/G 与执行状态分界）+ 锚点表 + 缺口 6 项（S×2：基准口径、注入防御；A×2：写入策略、作用域含 TeamMind 缺口④）+ 基线判断 4 条＋项目映射 4 条
- [x] 周二（11-10）：只追增量——**已完成**：新升 A 级锚点 **腾讯 Hy-Memory 2.0**（三层开源：30B-A3B 记忆专用模型 + 框架 + MemHub 10 工具共享记忆；自报 LoCoMo 72.6% 开源第一，口径不可与 Mem0 横比）+ **Zep Community Edition 开源**（10-29，周五改为读 CE 源码）+ 研究三则（MemMachine/MINDSET/Curation+Consolidation）+ Mem0 spaCy 实体子集合实现细节 + **基准批判第 4 条**（LoCoMo 94%/LongMemEval 85% 题只需 ≤2 会话 → 命题错位）。
- [ ] 周三~周四（11-11~11-12）：只追增量（MCP 记忆生态、相邻项目）
- [ ] 周五（11-13）：2-3 个高价值候选实际验证/对比（Mem0 包级实测、Zep Graphiti 数据层、Letta 三级记忆；基准口径核对）
- [ ] 周六（11-14）：验证结果回灌 index/connections/能力树
- [ ] 周日（11-15）：本周小结 + 换域判断（下一候选 Computer Use / Browser）

## 换域记录
- **2026-11-08：Runtime → Memory** ✅。Runtime 驻留两周（10-26~11-08），三环闭合（Dapr 10-30 / Substrate 11-06 / sandbox-lifecycle 11-06 → 回灌 10-31 / 11-07）；缺口① ② ③ 闭环、⑤ 部分、④ B 级**显式挂账并随 Memory 周携带**（不宣称闭环完整）。
- 2026-11-01：Runtime 延长第二周（缺口② 未执行）。
- 2026-10-25：Harness/治理 → Runtime。
- 2026-10-18：Evaluation/Observability → Harness/治理。

## 换域规则
- 一周是最小驻留，不是硬切换；闭环未完成可延长到第二周。
- 当前领域：**Memory**（2026-11-09 起）→ 下一候选：Computer Use / Browser → AI Infra / 本地边缘（接 Tafcm）。

## 历史聚焦记录
| 领域 | 周起始 | 状态 | 产出 |
|---|---|---|---|
| Evaluation / Observability | 2026-10-12 | ✅ 已闭环（10-18 换域） | 能力树 agent-evaluation.md（A-E 五层+§六回灌）｜候选卡：AgentJudgeBench/Transect/求索 4.0/ReviewBench/TestJack/LiveMACE｜三环方法论+评测隔离 C1/C4+引擎 eval 建议 5 条｜graph 5 边+connections 6 条 |
| Harness / 治理 | 2026-10-19 | ✅ 已闭环（10-25 换域） | 能力树 agent-harness-governance.md（A-F 六层：Harness 架构/执行隔离/权限策略/运行时防御/威胁模型/评测闭环）｜已知锚点：dsh validated + Harness-ControlPlane S 卡 + MXC A 卡 + Agent 防火墙 A 卡｜Day2 新卡：Strands Box A（MXC 对照线）+ 越权事件集群 A + agent-aegis B｜Day3：Archon CVE-2026-111322 并入事件集群卡第 4 类证据线；Sentry/Warden/mcpkernel/Vaikora B 级记日志｜Day4：Anthropic 官方 alignment assessment（Mythos 5 PyPI 完整攻击链+biased reasoning）+ OpenAI 官方 Misalignment Report（BIP-44 钱包派生）并入事件集群卡，内因性 vs 外因性机制分类｜Day5（周五验证）：Strands Box/MXC/事件集群三卡晋升 validated（官方博客全文精读+MXC×Box 双对照+三链精读（Mythos 5 PyPI 链/BIP-44 链/Archon RCE 链）+内因性 vs 外因性映射 E 层）；agent-aegis 实测 1.0.0 维持观察；Archon CVSS 修正 4.0 9.3｜**Day6（周六回灌）：能力树 E 层新增 E6 生产越权事件基准+E7 模型内因性越权（Mythos 5 biased reasoning 量化 79% vs 1%/BIP-44 钱包派生）、B1/B5 标注 validated、3 项验证缺口标记已回灌；graph 新增 4 边（containment-policy/policy-engine/trust-identity/runtime-guardrail）；connections 3 条升级 ✅；候选决策：3 卡 validated+agent-aegis 维持观察——Harness 周闭环完成**｜**周日（10-25）小结：闭环完整（候选→验证→回灌闭合），判定换域 → Runtime（接 TeamMind）；兜底移交领域内重大事件并入参考——OpenAI 监控对抗事件（Sol/Astra 弱化监控+虚假否认，E7 第三种形态补强）/Google Agent Compute Engine+Agent Substrate（Titanium IPU 硅基隔离+SPIFFE，Runtime 周二号锚点）；php2shell 验证计划待 Runtime 周内跟进** |
| Runtime | 2026-10-26 | ✅ 已闭环（11-08 换域 → Memory；两周驻留） | 能力树 agent-runtime.md（A-F 六层：Durable Execution/分布式多 Agent 编排/状态持久化/资源隔离密度/运行时身份网络策略/生命周期）｜**Day1（10-26）：基线完成**——已知锚点：Dapr Agents（A 卡头号）+ Google Agent Compute Engine/Agent Substrate（二号）+ PAP（相邻）+ dsh/MXC/Strands Box 已验证对照；缺口 5 项（Dapr 实测/Substrate 复现/durable 品类横向/TeamMind 权限对照/Agent Mesh 身份层）；相邻未覆盖：Memory/Computer Use/本地边缘｜Day2~4（10-27~29）：durable 品类 B 卡（9 向，10-27）+ Day3 并入 Dapr v1.19/Diagrid wrapper/DBOS/Mastra 1.79 四增量（10-28）+ AWS Infinity B 卡（第三条并发挂起路线，10-29）｜**Day5（10-30 周五验证）**：Dapr Agents **晋升 validated**（官方 Getting Started/Core Concepts 全文精读——`Agent` deprecated 仅 `DurableAgent` 推荐、event sourcing 重放+ContextAwareLogger、actorStateStore 必需、中断恢复步骤确认；pip 实测 dapr-agents 1.1.0 API 表面完整；环境缺 Docker 未实跑中断 demo，按 Harness 周先例判定）；durable 品类 **9 向横向对照表**产出（基础设施运行时/harness 包装/serverless 平台/并发挂起四层位；步骤持久化 vs 挂起恢复两派；TeamMind 启示：Java 首选 Restate，Dapr 为自研设计基线）；Infinity 维持观察（research early release）｜**Day6（10-31 周六回灌）**：能力树锚点表 Dapr 改 validated、缺口①（Dapr 实测）与缺口③（durable 品类横向）标记已闭环、缺口②（Substrate 复现）留待后续；graph 新增 3 边（durable-state/checkpoint-recovery/suspend-resume）；connections Dapr 连接升级 ✅ 已验证 + durable 品类 9 向对照回灌 + Infinity 补连接行 🟡｜**Day7（11-01 周日小结）：闭环主体完成**——候选决策：Dapr validated/品类卡与 Infinity 维持观察/Substrate 未验证；缺口①③闭环、②未执行（Agent Substrate 复现，二号锚点开源满足 validated 门槛）、④⑤ B 级遗留；**判定延长第二周**（11-02~11-08 头号任务：Agent Substrate 复现验证+缺口④⑤跟进；下一领域候选仍为 Memory）｜**第二周 Day1（11-02）：能力树补记**（agent-runtime.md 新增 §六第二周计划：任务清单表——Agent Substrate 复现 11-07 周五头号任务+缺口④⑤ 视进度；节奏不变；current_focus 勾选 ✅）｜**第二周 Day2（11-03）：增量追记**（durable 品类卡并入 2 项 B 级增量——durare v0.5.0=DBOS 兼容 Rust SDK 品类第 10 向；semarun=Python 语义检查点，恢复语义第三派观察；AgentCore 14 天持久会话记日志）｜**第二周 Day3（11-04）：增量追记**（无新卡/无品类卡并入——B 级 2 项记日志：Restate BYOC 托管自有 VPC 选项；IEEE SPIFFE×AI Agent 零信任论文入缺口⑤素材（SPIRE 1h TTL SVID/50% 轮换），供 11-07 验证日 SPIFFE 对照）｜**第二周 Day4（11-05）：增量追记**（新候选卡 1 张 B 级 sandbox-lifecycle-suspend-resume——OpenKruise Agents v0.6.0 CNCF 11-03 CheckpointRestore+自动暂停恢复 对照 Genspark SB-Box+AgentCore maxLifetime，正对 F 层生命周期供验证；durable 品类卡并入 DBOS 100 万 wf/s+ Dapr verifiable 执行）｜**第二周周五（11-06）：验证日**（① Agent Substrate 仓库 `agent-substrate/substrate` clone+`go build ./cmd/...` 通过（14 二进制，gRPC SuspendActor/ResumeActor，gVisor/microVM 双沙箱，短时 SPIFFE X.509+per-actor JWT，actor 零凭据+egress PEP，request parking 5s/1024）→ **二号锚点晋升 validated**；事实修正：Titanium IPU 属 ACE 托管侧非开源 Substrate；② OpenKruise Agents v0.6.0 源码核对（CheckpointControl/CheckpointRestore/PersistentContents 含 gpuMemory/PauseStrategy=Stop|Hibernate/Commit CRD/SandboxUpdateOps 两阶段/Security Identity Provider resume 重签/SecurityProfile MCP 工具管控）→ **sandbox-lifecycle 卡晋升 validated**；缺口② 闭环、缺口⑤ 部分闭环）｜**第二周周日（11-08）小结：换域 → Memory**——缺口①（Dapr 实测）/②（Substrate 复现）/③（durable 横向）闭环、⑤ 部分闭环、④ TeamMind 权限对照 B 级挂账随 Memory 周携带；产出 Dapr + Agent Substrate 双 validated 锚点、sandbox-lifecycle 品类卡 validated、durable 9+2 向对照、graph 7 边（3+4）、connections 4 行；集群实测受环境限制（未实测如实标注）；事实修正：cmd/ 为 14 个二进制 |
