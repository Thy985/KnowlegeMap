# Current Focus（雷达当前聚焦领域）

> 定时任务每次运行先读本文件，确定当前领域与本周进度。换域后更新本文件。

## 当前领域：Computer Use / Browser（浏览器与桌面操作层 / 真实环境执行）

- **周起始日**：2026-11-23（周一）
- **状态**：active · **第一周（11-23~11-29）· Day1 基线已建**（能力树 `08_agent_centric/domains/agent-computer-use.md`：A~H 八层 44 节点 / 锚点 12 行 / 基准批判 5 条 / 判断 7 条 / 缺口 6 项）——Memory 两周（11-09~11-22）已收束：E 层作用域与 F 层注入路径均完成确定性实测并结案（路径级，非比例级），故换域；Memory 的 H 层原型仍零代码，已转项目施工项，不占雷达周
- **为什么现在做它**：领域顺序 Evaluation→Harness→Runtime→Memory→**Computer Use / Browser**→AI Infra/本地边缘。Memory 两周已产出可交接的三条判据（动作门控位置 > 强度 / 判定依据必须外部 / 回执可核验），正好是真实环境执行的判定框架；且 Tafcm / campus_order / E2E-CLI 都直接依赖浏览器自动化，`[cand]computer-browser-use-2026`、`[cand]browser-harness-2026`、`[cand]webwright-2026` 三张卡已在队；事件侧 Windows-MCP 无认证（CVE-2026-48989）、Mendix MCP 监听 9.2（CVE-2026-112136）已证明"本地控制面裸露"是可远程触发的真实风险，真实环境操作面比记忆面更缺边界。

## 目标
- 建立 Computer Use / Browser 能力树/基线：环境表示（DOM/无障碍树/像素）、动作空间与 grounding、感知与自验证（成功判据来自执行事实而非页面文案）、会话与状态（登录态/cookie/会话恢复）、隔离与凭据（浏览器 profile / 桌面会话 / 本地端口）、信任边界（不可信页面输入 vs 可信指令）、人机交接（确认点与中断）、可观测与回放（轨迹/截图/动作日志）
- 验证 2-3 个高价值候选（browser-use / Playwright MCP / Webwright / Browser Harness），优先能本地实跑、且能对照"动作门控位置"与"回执可核验"的
- 闭环：候选 → 验证 → 回灌 index/connections/能力树
- 延续 Memory 周的三条判据作为验收提问：执行通道是否唯一 / 成功判据来自哪里 / 动作回执能否核验

## 已知锚点（不重复收集）
- **`03_expansion_queue/candidates/[cand]computer-browser-use-2026.md`（S 卡）**：Computer/Browser Use GA 格局、browser-use 生态、真实环境操作基线；连接 campus_order / E2E-CLI / agent-attention
- **`03_expansion_queue/candidates/[cand]browser-harness-2026.md`（A 卡）**：Browser Harness（浏览器控制面 / EP-002 权限边界）
- **`03_expansion_queue/candidates/[cand]webwright-2026.md`（A 卡）**：MS Research Webwright（脚本化浏览器 / 可复现验证）
- **`03_expansion_queue/candidates/[cand]agentic-attack-2026.md`（S 卡）**：事件日 22 的 CVE-2026-48989（Windows-MCP 无认证 + 通配 CORS → 浏览器可触发的本地 RCE）、事件日 24 的 CVE-2026-112136（Mendix MCP 监听 9.2）——本周直接作为"本地控制面"证据复用
- **Memory 周交接（`agent-memory.md` §十 10.5）**：三条判据（动作门控位置 / 判定依据外部 / 回执可核验）；E3 结论"API 层强制 scope、存储层单文件"可类比 browser profile 的隔离层
- Runtime 周结论：Agent Substrate 短时 SPIFFE + egress PEP、零凭据执行——桌面/浏览器会话的凭据外注可对照
- 相邻未覆盖：AI Infra / 本地边缘（接 Tafcm 本地推理）；Evaluation 已闭环（动作成功率的评测口径按需引用）

## 本周进度（每日分工）
- [x] 周一（11-23）：建 Computer Use / Browser 能力树/基线（`08_agent_centric/domains/agent-computer-use.md`）+ 更新本文件 ✅（八层 44 节点；锚点 12；批判 5；判断 7；缺口 6（S1/A2/B3）；Day1 意外收获＝browser-use 1.0 架构级重写并入 S 卡）——A 环境表示 / B 动作空间与 grounding / C 感知与自验证 / D 会话与状态 / E 隔离与凭据 / F 信任边界 / G 人机交接 / H 可观测与回放；锚点表 3 张既有卡 + 事件侧 2 条；缺口 5-6 项，至少 1 项 S
- [ ] 周二（11-24）：只追增量（browser-use / Playwright MCP / Webwright / Browser Harness 新 release 与活跃变化）
- [ ] 周三（11-25）：只追增量（相邻：desktop CUA、无障碍树 vs 像素 grounding、动作重放与确定性）
- [ ] 周四（11-26）：只追增量（安全：本地监听/通配 CORS/浏览器 profile 串用/凭据泄露/沙箱逃逸）
- [ ] 周五（11-27）：2-3 个高价值候选实际验证/对比（优先 browser-use 本地实跑、Playwright MCP 源码核对；无 GUI 则降级为"包级 + 源码级"并如实标注）
- [ ] 周六（11-28）：验证结果回灌 index/connections/能力树/graph
- [ ] 周日（11-29）：小结 + 换域判断（下一候选 AI Infra / 本地边缘，接 Tafcm）；若验证环未闭合，按"最小驻留"延长

## 换域记录
- **2026-11-22：Memory → Computer Use / Browser** ✅。Memory 驻留两周（11-09~11-22）。第二周三环审计=候选完整、回灌完整、验证达"路径级"未达"比例级"：E1 注入路径（写入→命中 0.8000→规则 stub 外发，`infer=False` 绕过门控）、E2 删除回执否定结论（history.db 留全文）、E3 作用域双层结论（API 层零交叉 0.79ms / 存储层单文件读出全部明文）。F 层 S 缺口与 E 层 A 缺口均以实测结案（口径：路径级）；H 层原型仍零代码、Letta/Graphiti 未验证、真实模型依从率未测，**不宣称闭环完整**，三项转项目施工项/挂账携带。换域依据：制度约束已满足、同族论文边际收益递减、下一领域有真实施工需求且证据已备。
- **2026-11-15：Memory 延长第二周（不换域）** ⏸。第一周三环审计=候选完整/回灌完整/验证不完整（Mem0 行为级 ✅、EvolveLab 结构级 🟡、Zep CE 否定结论 ✅、Letta 与 Graphiti 未执行）；F 层注入防御（S）与 E 层作用域（A）未验证，按「最小驻留非硬切换、闭环未完成可延长」延长至 11-22，第二周以三项实测（注入复现/delete 回执/作用域串读）为闭合标准。
- **2026-11-08：Runtime → Memory** ✅。Runtime 驻留两周（10-26~11-08），三环闭合（Dapr 10-30 / Substrate 11-06 / sandbox-lifecycle 11-06 → 回灌 10-31 / 11-07）；缺口① ② ③ 闭环、⑤ 部分、④ B 级**显式挂账并随 Memory 周携带**（不宣称闭环完整）。
- 2026-11-01：Runtime 延长第二周（缺口② 未执行）。
- 2026-10-25：Harness/治理 → Runtime。
- 2026-10-18：Evaluation/Observability → Harness/治理。

## 换域规则
- 一周是最小驻留，不是硬切换；闭环未完成可延长到第二周。
- 当前领域：**Computer Use / Browser · 第一周**（2026-11-23 起）→ 下一候选：AI Infra / 本地边缘（接 Tafcm）。Memory 两周已收束（路径级结案），其 H 层原型与 Letta/Graphiti 验证转项目任务，不占雷达周。

## 历史聚焦记录
| 领域 | 周起始 | 状态 | 产出 |
|---|---|---|---|
| Evaluation / Observability | 2026-10-12 | ✅ 已闭环（10-18 换域） | 能力树 agent-evaluation.md（A-E 五层+§六回灌）｜候选卡：AgentJudgeBench/Transect/求索 4.0/ReviewBench/TestJack/LiveMACE｜三环方法论+评测隔离 C1/C4+引擎 eval 建议 5 条｜graph 5 边+connections 6 条 |
| Harness / 治理 | 2026-10-19 | ✅ 已闭环（10-25 换域） | 能力树 agent-harness-governance.md（A-F 六层：Harness 架构/执行隔离/权限策略/运行时防御/威胁模型/评测闭环）｜已知锚点：dsh validated + Harness-ControlPlane S 卡 + MXC A 卡 + Agent 防火墙 A 卡｜Day2 新卡：Strands Box A（MXC 对照线）+ 越权事件集群 A + agent-aegis B｜Day3：Archon CVE-2026-111322 并入事件集群卡第 4 类证据线；Sentry/Warden/mcpkernel/Vaikora B 级记日志｜Day4：Anthropic 官方 alignment assessment（Mythos 5 PyPI 完整攻击链+biased reasoning）+ OpenAI 官方 Misalignment Report（BIP-44 钱包派生）并入事件集群卡，内因性 vs 外因性机制分类｜Day5（周五验证）：Strands Box/MXC/事件集群三卡晋升 validated（官方博客全文精读+MXC×Box 双对照+三链精读（Mythos 5 PyPI 链/BIP-44 链/Archon RCE 链）+内因性 vs 外因性映射 E 层）；agent-aegis 实测 1.0.0 维持观察；Archon CVSS 修正 4.0 9.3｜**Day6（周六回灌）：能力树 E 层新增 E6 生产越权事件基准+E7 模型内因性越权（Mythos 5 biased reasoning 量化 79% vs 1%/BIP-44 钱包派生）、B1/B5 标注 validated、3 项验证缺口标记已回灌；graph 新增 4 边（containment-policy/policy-engine/trust-identity/runtime-guardrail）；connections 3 条升级 ✅；候选决策：3 卡 validated+agent-aegis 维持观察——Harness 周闭环完成**｜**周日（10-25）小结：闭环完整（候选→验证→回灌闭合），判定换域 → Runtime（接 TeamMind）；兜底移交领域内重大事件并入参考——OpenAI 监控对抗事件（Sol/Astra 弱化监控+虚假否认，E7 第三种形态补强）/Google Agent Compute Engine+Agent Substrate（Titanium IPU 硅基隔离+SPIFFE，Runtime 周二号锚点）；php2shell 验证计划待 Runtime 周内跟进** |
| Runtime | 2026-10-26 | ✅ 已闭环（11-08 换域 → Memory；两周驻留） | 能力树 agent-runtime.md（A-F 六层：Durable Execution/分布式多 Agent 编排/状态持久化/资源隔离密度/运行时身份网络策略/生命周期）｜**Day1（10-26）：基线完成**——已知锚点：Dapr Agents（A 卡头号）+ Google Agent Compute Engine/Agent Substrate（二号）+ PAP（相邻）+ dsh/MXC/Strands Box 已验证对照；缺口 5 项（Dapr 实测/Substrate 复现/durable 品类横向/TeamMind 权限对照/Agent Mesh 身份层）；相邻未覆盖：Memory/Computer Use/本地边缘｜Day2~4（10-27~29）：durable 品类 B 卡（9 向，10-27）+ Day3 并入 Dapr v1.19/Diagrid wrapper/DBOS/Mastra 1.79 四增量（10-28）+ AWS Infinity B 卡（第三条并发挂起路线，10-29）｜**Day5（10-30 周五验证）**：Dapr Agents **晋升 validated**（官方 Getting Started/Core Concepts 全文精读——`Agent` deprecated 仅 `DurableAgent` 推荐、event sourcing 重放+ContextAwareLogger、actorStateStore 必需、中断恢复步骤确认；pip 实测 dapr-agents 1.1.0 API 表面完整；环境缺 Docker 未实跑中断 demo，按 Harness 周先例判定）；durable 品类 **9 向横向对照表**产出（基础设施运行时/harness 包装/serverless 平台/并发挂起四层位；步骤持久化 vs 挂起恢复两派；TeamMind 启示：Java 首选 Restate，Dapr 为自研设计基线）；Infinity 维持观察（research early release）｜**Day6（10-31 周六回灌）**：能力树锚点表 Dapr 改 validated、缺口①（Dapr 实测）与缺口③（durable 品类横向）标记已闭环、缺口②（Substrate 复现）留待后续；graph 新增 3 边（durable-state/checkpoint-recovery/suspend-resume）；connections Dapr 连接升级 ✅ 已验证 + durable 品类 9 向对照回灌 + Infinity 补连接行 🟡｜**Day7（11-01 周日小结）：闭环主体完成**——候选决策：Dapr validated/品类卡与 Infinity 维持观察/Substrate 未验证；缺口①③闭环、②未执行（Agent Substrate 复现，二号锚点开源满足 validated 门槛）、④⑤ B 级遗留；**判定延长第二周**（11-02~11-08 头号任务：Agent Substrate 复现验证+缺口④⑤跟进；下一领域候选仍为 Memory）｜**第二周 Day1（11-02）：能力树补记**（agent-runtime.md 新增 §六第二周计划：任务清单表——Agent Substrate 复现 11-07 周五头号任务+缺口④⑤ 视进度；节奏不变；current_focus 勾选 ✅）｜**第二周 Day2（11-03）：增量追记**（durable 品类卡并入 2 项 B 级增量——durare v0.5.0=DBOS 兼容 Rust SDK 品类第 10 向；semarun=Python 语义检查点，恢复语义第三派观察；AgentCore 14 天持久会话记日志）｜**第二周 Day3（11-04）：增量追记**（无新卡/无品类卡并入——B 级 2 项记日志：Restate BYOC 托管自有 VPC 选项；IEEE SPIFFE×AI Agent 零信任论文入缺口⑤素材（SPIRE 1h TTL SVID/50% 轮换），供 11-07 验证日 SPIFFE 对照）｜**第二周 Day4（11-05）：增量追记**（新候选卡 1 张 B 级 sandbox-lifecycle-suspend-resume——OpenKruise Agents v0.6.0 CNCF 11-03 CheckpointRestore+自动暂停恢复 对照 Genspark SB-Box+AgentCore maxLifetime，正对 F 层生命周期供验证；durable 品类卡并入 DBOS 100 万 wf/s+ Dapr verifiable 执行）｜**第二周周五（11-06）：验证日**（① Agent Substrate 仓库 `agent-substrate/substrate` clone+`go build ./cmd/...` 通过（14 二进制，gRPC SuspendActor/ResumeActor，gVisor/microVM 双沙箱，短时 SPIFFE X.509+per-actor JWT，actor 零凭据+egress PEP，request parking 5s/1024）→ **二号锚点晋升 validated**；事实修正：Titanium IPU 属 ACE 托管侧非开源 Substrate；② OpenKruise Agents v0.6.0 源码核对（CheckpointControl/CheckpointRestore/PersistentContents 含 gpuMemory/PauseStrategy=Stop|Hibernate/Commit CRD/SandboxUpdateOps 两阶段/Security Identity Provider resume 重签/SecurityProfile MCP 工具管控）→ **sandbox-lifecycle 卡晋升 validated**；缺口② 闭环、缺口⑤ 部分闭环）｜**第二周周日（11-08）小结：换域 → Memory**——缺口①（Dapr 实测）/②（Substrate 复现）/③（durable 横向）闭环、⑤ 部分闭环、④ TeamMind 权限对照 B 级挂账随 Memory 周携带；产出 Dapr + Agent Substrate 双 validated 锚点、sandbox-lifecycle 品类卡 validated、durable 9+2 向对照、graph 7 边（3+4）、connections 4 行；集群实测受环境限制（未实测如实标注）；事实修正：cmd/ 为 14 个二进制 |
| Memory | 2026-11-09 | ✅ 已收束（11-22 换域 → Computer Use / Browser；两周驻留，路径级结案） | 能力树 `agent-memory.md` A~H 八层（H=可靠性/健康门/心跳/降级诚实/静默腐化防护/告警预算）｜锚点 13 行（Mem0/Zep→Graphiti/Hy-Memory 2.0/Letta/A-MEM/MemEval/SIx A/MemEvolve A−/批判六条）｜判断 5 条｜缺口 6+2｜验证：Mem0 OSS 2.2.1 本地实跑 ✅（add 空回执 vs get_all 2 条、search 0.837、单遍 ADDITIVE、无图库依赖、expiration_date TTL）、EvolveLab 13 providers 结构级 🟡、Zep CE 判定推翻 ✅（公告 2024-09-26 且 deprecated，开源线 Graphiti）｜回灌：H 层 + 批判⑤⑥ + 2 锚点 + 缺口 2 完成 2 新增 + connections 2 行 + graph 3 边（memory-reliability/honest-degradation/write-receipt-verification）｜日志 深耕 7 + 兜底 7｜**第二周 Day1（11-16）**：F 层 F1.1~F5.2 + E 层 E4.1~E4.3 + §八 + S 卡 trust-boundary｜Day3（11-18）：Mem0×Graphiti 对照（精度差显著/成本更省）+ guard 集群 C｜Day4（11-19）：PoEM A + 来源绑定三件套 A−（§8.7）｜Day5（11-20）：三项确定性实测（E1 注入路径 / E2 删除回执失败 / E3 作用域双层）→ §8.5.1｜Day6（11-21）：回灌 §九（三改写 / 四读数 / 判断 6-7 / 落点 3 / connections 2 / graph 2）｜**Day7（11-22）小结：E/F 两缺口路径级结案，判定换域 → Computer Use / Browser；不宣称闭环完整**（H 层零代码、Letta/Graphiti 未验证、模型依从率未测） |
| Computer Use / Browser | 2026-11-23 | 🆕 第一周进行中 | 起点：3 张既有卡（computer-browser-use-2026 / browser-harness-2026 / webwright-2026）+ 事件侧 2 条本地控制面证据（CVE-2026-48989 Windows-MCP 无认证+通配 CORS、CVE-2026-112136 Mendix 9.2）+ Memory 交接三判据（动作门控位置 / 判定依据外部 / 回执可核验）｜待建：能力树 A~H（环境表示 / 动作空间与 grounding / 感知与自验证 / 会话与状态 / 隔离与凭据 / 信任边界 / 人机交接 / 可观测与回放） |
