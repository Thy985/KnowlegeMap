# Current Focus（雷达当前聚焦领域）

> 定时任务每次运行先读本文件，确定当前领域与本周进度。换域后更新本文件。

## 当前领域：Runtime（Agent 执行运行时 / 分布式运行时）

- **周起始日**：2026-10-26（周一）
- **状态**：active（10-25 周日小结换域决定已作出；10-26 周一 Day1 建能力树/基线 ✅；10-30 周五验证完成 ✅）
- **为什么现在做它**：领域顺序 Evaluation→Harness→Runtime 的下一站；上一领域 Harness/治理 已于 10-24 周六闭环（候选→验证→回灌闭合）；Runtime 与用户项目 **TeamMind（多 Agent 运行时）** 直接相关；Harness 周已验证的执行隔离/身份/凭据外注证据（MXC/Strands Box/Google 侧印证）为 Runtime 提供相邻对照基础。

## 目标
- 建立 Agent Runtime 能力树/基线（已知 vs 缺口 vs 相邻未覆盖）：durable execution / 分布式多 agent 编排 / 状态持久化 / 资源隔离与密度 / 运行时身份与网络策略 / 生命周期（suspend-resume-checkpoint）
- 发现并验证 2-3 个高价值 runtime 工具或方法（候选方向：Dapr Agents 实测、Google Agent Substrate 开源对照、PAP 协议/身份层相邻、durable execution 品类）
- 闭环：候选 → 验证 → 回灌 index/connections/能力树

## 已知锚点（不重复收集）
- **Dapr Agents**（A 候选卡，2026-10-16 CNCF×NVIDIA launch——DurableAgent 步骤持久化+双 state store+崩溃恢复+pub/sub 多 agent 编排；**头号锚点**，仓库 github.com/dapr/dapr-agents，验证 quickstart `03_durable_agent_http.py`）
- **Google Agent Compute Engine + Agent Substrate**（2026-10-22 官方发布，10-24 兜底精读移交——Titanium IPU 硅基隔离 microVM+短时凭据+egress 外注服务凭据+Hyperdisk 持久化+copy-on-write/fast checkpoint；Agent Substrate 开源 K8s 零信任：10x 密度/20 万 agent 基准 500 activations/sec/<500ms suspend-resume/SPIFFE 身份+egress 代理；**二号锚点**，开源满足 validated 门槛）
- Personal Agent Protocol / PAP（A 候选卡——agent-to-business 身份授权开放标准，协议/身份层相邻素材）
- 已验证相邻证据（供对照）：DeepSeek Harness validated（sandbox/approval/credentials seam/session-telemetry）、MXC/Strands Box validated（OS 级隔离+凭证外挂网关=Google egress 外注模式的微软/AWS 侧印证）、Agent Executor（Google 开源 runtime 标准，2026-05-21，旧闻已覆盖）
- 引擎内 evaluation 层 + security-assessment 能力树模板（已有）

## 本周进度（每日分工）
- [x] 周日（10-25）：Harness 周小结完成，**判定换域 → Runtime**（本周历史见下表；新领域周起始 10-26）✅
- [x] 周一（10-26）：**建能力树/基线（agent-runtime.md，A-F 六层）完成** ✅
- [ ] 周二~周四（10-27~10-29）：增量扫描，写候选卡（S/A/B）
- [x] 周五（10-30）：实际验证/对比 2-3 个高价值候选（Dapr Agents 文档全文+包级实测；durable 品类 9 向横向；Infinity 对照）✅
- [x] 周六（10-31）：验证结果回灌 index/connections/能力树 ✅
- [ ] 周日（11-01）：本周小结，判断是否换域

## 换域规则
- 一周是最小驻留，不是硬切换；闭环未完成可延长到第二周。
- 下一领域（候选）：Memory → Computer Use / Browser → AI Infra / 本地边缘（接 Tafcm）。

## 历史聚焦记录
| 领域 | 周起始 | 状态 | 产出 |
|---|---|---|---|
| Evaluation / Observability | 2026-10-12 | ✅ 已闭环（10-18 换域） | 能力树 agent-evaluation.md（A-E 五层+§六回灌）｜候选卡：AgentJudgeBench/Transect/求索 4.0/ReviewBench/TestJack/LiveMACE｜三环方法论+评测隔离 C1/C4+引擎 eval 建议 5 条｜graph 5 边+connections 6 条 |
| Harness / 治理 | 2026-10-19 | ✅ 已闭环（10-25 换域） | 能力树 agent-harness-governance.md（A-F 六层：Harness 架构/执行隔离/权限策略/运行时防御/威胁模型/评测闭环）｜已知锚点：dsh validated + Harness-ControlPlane S 卡 + MXC A 卡 + Agent 防火墙 A 卡｜Day2 新卡：Strands Box A（MXC 对照线）+ 越权事件集群 A + agent-aegis B｜Day3：Archon CVE-2026-111322 并入事件集群卡第 4 类证据线；Sentry/Warden/mcpkernel/Vaikora B 级记日志｜Day4：Anthropic 官方 alignment assessment（Mythos 5 PyPI 完整攻击链+biased reasoning）+ OpenAI 官方 Misalignment Report（BIP-44 钱包派生）并入事件集群卡，内因性 vs 外因性机制分类｜Day5（周五验证）：Strands Box/MXC/事件集群三卡晋升 validated（官方博客全文精读+MXC×Box 双对照+三链精读（Mythos 5 PyPI 链/BIP-44 链/Archon RCE 链）+内因性 vs 外因性映射 E 层）；agent-aegis 实测 1.0.0 维持观察；Archon CVSS 修正 4.0 9.3｜**Day6（周六回灌）：能力树 E 层新增 E6 生产越权事件基准+E7 模型内因性越权（Mythos 5 biased reasoning 量化 79% vs 1%/BIP-44 钱包派生）、B1/B5 标注 validated、3 项验证缺口标记已回灌；graph 新增 4 边（containment-policy/policy-engine/trust-identity/runtime-guardrail）；connections 3 条升级 ✅；候选决策：3 卡 validated+agent-aegis 维持观察——Harness 周闭环完成**｜**周日（10-25）小结：闭环完整（候选→验证→回灌闭合），判定换域 → Runtime（接 TeamMind）；兜底移交领域内重大事件并入参考——OpenAI 监控对抗事件（Sol/Astra 弱化监控+虚假否认，E7 第三种形态补强）/Google Agent Compute Engine+Agent Substrate（Titanium IPU 硅基隔离+SPIFFE，Runtime 周二号锚点）；php2shell 验证计划待 Runtime 周内跟进** |
| Runtime | 2026-10-26 | active（10-25 换域决定，10-26 Day1 建基线 ✅，10-30 周五验证 ✅，10-31 周六回灌 ✅） | 能力树 agent-runtime.md（A-F 六层：Durable Execution/分布式多 Agent 编排/状态持久化/资源隔离密度/运行时身份网络策略/生命周期）｜**Day1（10-26）：基线完成**——已知锚点：Dapr Agents（A 卡头号）+ Google Agent Compute Engine/Agent Substrate（二号）+ PAP（相邻）+ dsh/MXC/Strands Box 已验证对照；缺口 5 项（Dapr 实测/Substrate 复现/durable 品类横向/TeamMind 权限对照/Agent Mesh 身份层）；相邻未覆盖：Memory/Computer Use/本地边缘｜Day2~4（10-27~29）：durable 品类 B 卡（9 向，10-27）+ Day3 并入 Dapr v1.19/Diagrid wrapper/DBOS/Mastra 1.79 四增量（10-28）+ AWS Infinity B 卡（第三条并发挂起路线，10-29）｜**Day5（10-30 周五验证）**：Dapr Agents **晋升 validated**（官方 Getting Started/Core Concepts 全文精读——`Agent` deprecated 仅 `DurableAgent` 推荐、event sourcing 重放+ContextAwareLogger、actorStateStore 必需、中断恢复步骤确认；pip 实测 dapr-agents 1.1.0 API 表面完整；环境缺 Docker 未实跑中断 demo，按 Harness 周先例判定）；durable 品类 **9 向横向对照表**产出（基础设施运行时/harness 包装/serverless 平台/并发挂起四层位；步骤持久化 vs 挂起恢复两派；TeamMind 启示：Java 首选 Restate，Dapr 为自研设计基线）；Infinity 维持观察（research early release）｜**Day6（10-31 周六回灌）**：能力树锚点表 Dapr 改 validated、缺口①（Dapr 实测）与缺口③（durable 品类横向）标记已闭环、缺口②（Substrate 复现）留待后续；graph 新增 3 边（durable-state/checkpoint-recovery/suspend-resume）；connections Dapr 连接升级 ✅ 已验证 + durable 品类 9 向对照回灌 + Infinity 补连接行 🟡｜待周日 11-01 小结并判断是否换域 |
