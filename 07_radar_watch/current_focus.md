# Current Focus（雷达当前聚焦领域）

> 定时任务每次运行先读本文件，确定当前领域与本周进度。换域后更新本文件。

## 当前领域：AI Infra / 本地边缘（推理引擎与服务 / 量化与显存 / 本地部署）

- **周起始日**：2026-11-30（周一）
- **状态**：active · **第一周（11-30~12-06）· 尚未开始（周日已换域，周一建树）**。Computer Use / Browser 第一周（11-23~11-29）已收束：候选→验证→回灌三环在**源码级**闭合，browser-use 1.0.8 / @playwright/mcp 0.0.86 / 本地控制面 9 模式三项 validated（源码级），剩余执行级项（profile 权限、最小 demo、端到端 call、Webwright CLI、DNS rebinding PoC、P8 真实 0.0.0.0 启动）全部依赖真实 GUI 与独立 profile，转项目施工项，不占雷达周
- **为什么现在做它**：领域顺序 Evaluation→Harness→Runtime→Memory→Computer Use→**AI Infra / 本地边缘**。这是顺序表最后一段，也正好接住真实需求：Tafcm 的本地推理（GTX 1660S + 64GB，INT4/INT8 量化、CPU offload、显存上限）、campus_order 的本地部署、E2E-CLI 的离线可复现。前两周的判断 9（校验按「入口 × 部署形态」逐格清点）与判断 11（证据深度分级）在这里天然复用——本地推理服务的 bind 地址、量化口径、厂商 bench 都是同一类「默认值即结论」的问题

## 目标
- 建 AI Infra / 本地边缘能力树/基线：**A 推理引擎与服务**（vLLM / SGLang / llama.cpp / MLX / TensorRT-LLM 的服务形态与调度）/ **B 量化与显存**（INT4/INT8/FP8、KV cache、PagedAttention、offload 策略、显存峰值口径）/ **C 本地运行时与硬件后端**（CUDA / ROCm / Vulkan / Metal / CPU，边缘设备）/ **D 模型分发与供应链**（权重来源、GGUF 转换、tokenizer、许可、完整性）/ **E 性能口径与可复现**（吞吐 / 首 token / 尾延迟 / 并发曲线 / bench 条件）/ **F 部署形态与信任边界**（进程内 / 容器 / 服务端 bind 与认证 / 多租户）/ **G 与 Agent 的接缝**（结构化输出、tool calling、长上下文、批处理与抢占）/ **H 可观测与容量**（metrics、trace、OOM 归因）
- 验证 2-3 个高价值候选，优先能在 GTX 1660S（6GB）+ 64GB RAM 上真跑、且能给出可复现数字的
- 延续 Computer Use 周的两条判据作为验收提问：**这条结论的证据深度是哪一级**（包级 / 源码级 / 实跑）/ **这个默认值在什么部署形态下退化为 no-op**
- 闭环：候选 → 验证 → 回灌 index/connections/能力树

## 已知锚点（不重复收集，周一建树时统一收口）
- **SGLang v1.0**（11-12/13 Summit 宣布：SGLang Consortium、agents 已产出多数 merged PR）；**SGLang on Intel Xeon CPU / Intel GPU as first-class**（11-27，LMSYS 博文）；SGLang 0.5.21 随 ROCm 10.2 分发（11-20）
- **vLLM v0.34.0**（11-16：移除 Model Runner V1、`block-size` 默认 16→64、`gpu_memory_utilization` 默认 1.0、停止发布 ROCm 7.2 wheels）；**vLLM Ascend v0.32.0rc1**（11-10）；ROCm 10.2 捆 vLLM 0.32.0
- **ggml v1.0.0**（11-13）、**Edge0-145B/120B**（11-13）、**Inkling 2 Mini**（11-20，26B total / 3.5B active，SGLang + Miles day-0）
- 既有卡 **`03_expansion_queue/candidates/[cand]local-edge-llm-2026.md`**（本地边缘 LLM 部署线）
- 知识空白 **G3 本地边缘**；Runtime 周结论（Substrate 短时凭据 + egress PEP）可作 F 层对照
- 用户硬件事实：GTX 1660 SUPER（6GB）+ 64GB RAM；栈 ComfyUI / MiniMax H3 / Seedance 2.5；正在做 INT4/INT8 量化与 CPU offload
- 相邻未覆盖：无（本域为顺序表末段）；Security 不选作首周（已有 security-assessment 模板）

## 本周进度（每日分工）
- [ ] 周一（11-30）：建 AI Infra / 本地边缘能力树/基线（A~H 八层），标注已知 / 缺口 / 相邻；设定本周验收口径
- [ ] 周二（12-01）：只追增量（推理引擎新 release / 量化新方案 / 本地运行时）
- [ ] 周三（12-02）：只追增量（相邻项目与供应链侧：权重分发、GGUF、许可、镜像）
- [ ] 周四（12-03）：只追增量（性能口径与可复现、边缘设备）
- [ ] 周五（12-04）：对 2-3 个高价值候选做实际验证/对比（优先 GTX 1660S 上可真跑；不可跑则如实标源码级）
- [ ] 周六（12-05）：验证结果回灌 index / connections / 能力树 / graph
- [ ] 周日（12-06）：本周小结 + 换域判断（顺序表已走完；下一轮按「用户真实需求 + 缺口」重排，候选：Security 深化 / Evals 复盘 / 垂直回到 Tafcm）

## 换域记录
- **2026-11-29：Computer Use / Browser → AI Infra / 本地边缘** ✅。Computer Use 驻留一周（11-23~11-29）。三环审计=候选完整（能力树 A~H 44 节点 + 21 锚点 + 判断 11 + 缺口 6；新卡 3 张：agent-desktop A / GUI 回放品类 A / 本地控制面 A，另有 WebMCP A 入 Day2）、验证完成（**源码级**：browser-use 1.0.8、@playwright/mcp 0.0.86、本地控制面 9 模式三项 validated；本机 9222 只读实测）、回灌完整（能力树 §十一 + 判断 9 强化 + 判断 11 新增 + 缺口 3 行；connections 4 条；graph 4 边；index/_INDEX/日志各一）。**结案口径＝源码级，不宣称实跑闭环**：profile 目录权限、browser-use 最小 demo、`@playwright/mcp` 端到端 call、Webwright CLI、DNS rebinding PoC、P8 真实 `--host 0.0.0.0` 启动验证、agent-desktop 包级核对共 7 项转项目施工项（silver-shield / E2E-CLI / Tafcm）。换域依据：三环在声明的深度上闭合；剩余项全部依赖真实 GUI 与独立 profile，属项目施工而非雷达周；下一域有真实施工需求（Tafcm 本地推理 6GB 显存约束、campus_order 本地部署）且顺序表已走到末段。
- **2026-11-22：Memory → Computer Use / Browser** ✅。Memory 驻留两周（11-09~11-22）。第二周三环审计=候选完整、回灌完整、验证达"路径级"未达"比例级"：E1 注入路径（写入→命中 0.8000→规则 stub 外发，`infer=False` 绕过门控）、E2 删除回执否定结论（history.db 留全文）、E3 作用域双层结论（API 层零交叉 0.79ms / 存储层单文件读出全部明文）。F 层 S 缺口与 E 层 A 缺口均以实测结案（口径：路径级）；H 层原型仍零代码、Letta/Graphiti 未验证、真实模型依从率未测，**不宣称闭环完整**，三项转项目施工项/挂账携带。换域依据：制度约束已满足、同族论文边际收益递减、下一领域有真实施工需求且证据已备。
- **2026-11-15：Memory 延长第二周（不换域）** ⏸。第一周三环审计=候选完整/回灌完整/验证不完整（Mem0 行为级 ✅、EvolveLab 结构级 🟡、Zep CE 否定结论 ✅、Letta 与 Graphiti 未执行）；F 层注入防御（S）与 E 层作用域（A）未验证，按「最小驻留非硬切换、闭环未完成可延长」延长至 11-22，第二周以三项实测（注入复现/delete 回执/作用域串读）为闭合标准。
- **2026-11-08：Runtime → Memory** ✅。Runtime 驻留两周（10-26~11-08），三环闭合（Dapr 10-30 / Substrate 11-06 / sandbox-lifecycle 11-06 → 回灌 10-31 / 11-07）；缺口① ② ③ 闭环、⑤ 部分、④ B 级**显式挂账并随 Memory 周携带**（不宣称闭环完整）。
- 2026-11-01：Runtime 延长第二周（缺口② 未执行）。
- 2026-10-25：Harness/治理 → Runtime。
- 2026-10-18：Evaluation/Observability → Harness/治理。

## 换域规则
- 一周是最小驻留，不是硬切换；闭环未完成可延长到第二周。
- 当前领域：**AI Infra / 本地边缘 · 第一周**（2026-11-30 起）。Computer Use 一周已在源码级收束（11-29 换域），7 项执行级验证转项目施工项。AI Infra 是本轮顺序表末段，走完后需按「真实需求 + 剩余缺口」重排，而不是继续顺延清单。

## 历史聚焦记录
| 领域 | 周起始 | 状态 | 产出 |
|---|---|---|---|
| Evaluation / Observability | 2026-10-12 | ✅ 已闭环（10-18 换域） | 能力树 agent-evaluation.md（A-E 五层+§六回灌）｜候选卡：AgentJudgeBench/Transect/求索 4.0/ReviewBench/TestJack/LiveMACE｜三环方法论+评测隔离 C1/C4+引擎 eval 建议 5 条｜graph 5 边+connections 6 条 |
| Harness / 治理 | 2026-10-19 | ✅ 已闭环（10-25 换域） | 能力树 agent-harness-governance.md（A-F 六层：Harness 架构/执行隔离/权限策略/运行时防御/威胁模型/评测闭环）｜已知锚点：dsh validated + Harness-ControlPlane S 卡 + MXC A 卡 + Agent 防火墙 A 卡｜Day2 新卡：Strands Box A（MXC 对照线）+ 越权事件集群 A + agent-aegis B｜Day3：Archon CVE-2026-111322 并入事件集群卡第 4 类证据线；Sentry/Warden/mcpkernel/Vaikora B 级记日志｜Day4：Anthropic 官方 alignment assessment（Mythos 5 PyPI 完整攻击链+biased reasoning）+ OpenAI 官方 Misalignment Report（BIP-44 钱包派生）并入事件集群卡，内因性 vs 外因性机制分类｜Day5（周五验证）：Strands Box/MXC/事件集群三卡晋升 validated（官方博客全文精读+MXC×Box 双对照+三链精读（Mythos 5 PyPI 链/BIP-44 链/Archon RCE 链）+内因性 vs 外因性映射 E 层）；agent-aegis 实测 1.0.0 维持观察；Archon CVSS 修正 4.0 9.3｜**Day6（周六回灌）：能力树 E 层新增 E6 生产越权事件基准+E7 模型内因性越权（Mythos 5 biased reasoning 量化 79% vs 1%/BIP-44 钱包派生）、B1/B5 标注 validated、3 项验证缺口标记已回灌；graph 新增 4 边（containment-policy/policy-engine/trust-identity/runtime-guardrail）；connections 3 条升级 ✅；候选决策：3 卡 validated+agent-aegis 维持观察——Harness 周闭环完成**｜**周日（10-25）小结：闭环完整（候选→验证→回灌闭合），判定换域 → Runtime（接 TeamMind）；兜底移交领域内重大事件并入参考——OpenAI 监控对抗事件（Sol/Astra 弱化监控+虚假否认，E7 第三种形态补强）/Google Agent Compute Engine+Agent Substrate（Titanium IPU 硅基隔离+SPIFFE，Runtime 周二号锚点）；php2shell 验证计划待 Runtime 周内跟进** |
| Runtime | 2026-10-26 | ✅ 已闭环（11-08 换域 → Memory；两周驻留） | 能力树 agent-runtime.md（A-F 六层：Durable Execution/分布式多 Agent 编排/状态持久化/资源隔离密度/运行时身份网络策略/生命周期）｜**Day1（10-26）：基线完成**——已知锚点：Dapr Agents（A 卡头号）+ Google Agent Compute Engine/Agent Substrate（二号）+ PAP（相邻）+ dsh/MXC/Strands Box 已验证对照；缺口 5 项（Dapr 实测/Substrate 复现/durable 品类横向/TeamMind 权限对照/Agent Mesh 身份层）；相邻未覆盖：Memory/Computer Use/本地边缘｜Day2~4（10-27~29）：durable 品类 B 卡（9 向，10-27）+ Day3 并入 Dapr v1.19/Diagrid wrapper/DBOS/Mastra 1.79 四增量（10-28）+ AWS Infinity B 卡（第三条并发挂起路线，10-29）｜**Day5（10-30 周五验证）**：Dapr Agents **晋升 validated**（官方 Getting Started/Core Concepts 全文精读——`Agent` deprecated 仅 `DurableAgent` 推荐、event sourcing 重放+ContextAwareLogger、actorStateStore 必需、中断恢复步骤确认；pip 实测 dapr-agents 1.1.0 API 表面完整；环境缺 Docker 未实跑中断 demo，按 Harness 周先例判定）；durable 品类 **9 向横向对照表**产出（基础设施运行时/harness 包装/serverless 平台/并发挂起四层位；步骤持久化 vs 挂起恢复两派；TeamMind 启示：Java 首选 Restate，Dapr 为自研设计基线）；Infinity 维持观察（research early release）｜**Day6（10-31 周六回灌）**：能力树锚点表 Dapr 改 validated、缺口①（Dapr 实测）与缺口③（durable 品类横向）标记已闭环、缺口②（Substrate 复现）留待后续；graph 新增 3 边（durable-state/checkpoint-recovery/suspend-resume）；connections Dapr 连接升级 ✅ 已验证 + durable 品类 9 向对照回灌 + Infinity 补连接行 🟡｜**Day7（11-01 周日小结）：闭环主体完成**——候选决策：Dapr validated/品类卡与 Infinity 维持观察/Substrate 未验证；缺口①③闭环、②未执行（Agent Substrate 复现，二号锚点开源满足 validated 门槛）、④⑤ B 级遗留；**判定延长第二周**（11-02~11-08 头号任务：Agent Substrate 复现验证+缺口④⑤跟进；下一领域候选仍为 Memory）｜**第二周 Day1（11-02）：能力树补记**（agent-runtime.md 新增 §六第二周计划：任务清单表——Agent Substrate 复现 11-07 周五头号任务+缺口④⑤ 视进度；节奏不变；current_focus 勾选 ✅）｜**第二周 Day2（11-03）：增量追记**（durable 品类卡并入 2 项 B 级增量——durare v0.5.0=DBOS 兼容 Rust SDK 品类第 10 向；semarun=Python 语义检查点，恢复语义第三派观察；AgentCore 14 天持久会话记日志）｜**第二周 Day3（11-04）：增量追记**（无新卡/无品类卡并入——B 级 2 项记日志：Restate BYOC 托管自有 VPC 选项；IEEE SPIFFE×AI Agent 零信任论文入缺口⑤素材（SPIRE 1h TTL SVID/50% 轮换），供 11-07 验证日 SPIFFE 对照）｜**第二周 Day4（11-05）：增量追记**（新候选卡 1 张 B 级 sandbox-lifecycle-suspend-resume——OpenKruise Agents v0.6.0 CNCF 11-03 CheckpointRestore+自动暂停恢复 对照 Genspark SB-Box+AgentCore maxLifetime，正对 F 层生命周期供验证；durable 品类卡并入 DBOS 100 万 wf/s+ Dapr verifiable 执行）｜**第二周周五（11-06）：验证日**（① Agent Substrate 仓库 `agent-substrate/substrate` clone+`go build ./cmd/...` 通过（14 二进制，gRPC SuspendActor/ResumeActor，gVisor/microVM 双沙箱，短时 SPIFFE X.509+per-actor JWT，actor 零凭据+egress PEP，request parking 5s/1024）→ **二号锚点晋升 validated**；事实修正：Titanium IPU 属 ACE 托管侧非开源 Substrate；② OpenKruise Agents v0.6.0 源码核对（CheckpointControl/CheckpointRestore/PersistentContents 含 gpuMemory/PauseStrategy=Stop|Hibernate/Commit CRD/SandboxUpdateOps 两阶段/Security Identity Provider resume 重签/SecurityProfile MCP 工具管控）→ **sandbox-lifecycle 卡晋升 validated**；缺口② 闭环、缺口⑤ 部分闭环）｜**第二周周日（11-08）小结：换域 → Memory**——缺口①（Dapr 实测）/②（Substrate 复现）/③（durable 横向）闭环、⑤ 部分闭环、④ TeamMind 权限对照 B 级挂账随 Memory 周携带；产出 Dapr + Agent Substrate 双 validated 锚点、sandbox-lifecycle 品类卡 validated、durable 9+2 向对照、graph 7 边（3+4）、connections 4 行；集群实测受环境限制（未实测如实标注）；事实修正：cmd/ 为 14 个二进制 |
| Memory | 2026-11-09 | ✅ 已收束（11-22 换域 → Computer Use / Browser；两周驻留，路径级结案） | 能力树 `agent-memory.md` A~H 八层（H=可靠性/健康门/心跳/降级诚实/静默腐化防护/告警预算）｜锚点 13 行（Mem0/Zep→Graphiti/Hy-Memory 2.0/Letta/A-MEM/MemEval/SIx A/MemEvolve A−/批判六条）｜判断 5 条｜缺口 6+2｜验证：Mem0 OSS 2.2.1 本地实跑 ✅（add 空回执 vs get_all 2 条、search 0.837、单遍 ADDITIVE、无图库依赖、expiration_date TTL）、EvolveLab 13 providers 结构级 🟡、Zep CE 判定推翻 ✅（公告 2024-09-26 且 deprecated，开源线 Graphiti）｜回灌：H 层 + 批判⑤⑥ + 2 锚点 + 缺口 2 完成 2 新增 + connections 2 行 + graph 3 边（memory-reliability/honest-degradation/write-receipt-verification）｜日志 深耕 7 + 兜底 7｜**第二周 Day1（11-16）**：F 层 F1.1~F5.2 + E 层 E4.1~E4.3 + §八 + S 卡 trust-boundary｜Day3（11-18）：Mem0×Graphiti 对照（精度差显著/成本更省）+ guard 集群 C｜Day4（11-19）：PoEM A + 来源绑定三件套 A−（§8.7）｜Day5（11-20）：三项确定性实测（E1 注入路径 / E2 删除回执失败 / E3 作用域双层）→ §8.5.1｜Day6（11-21）：回灌 §九（三改写 / 四读数 / 判断 6-7 / 落点 3 / connections 2 / graph 2）｜**Day7（11-22）小结：E/F 两缺口路径级结案，判定换域 → Computer Use / Browser；不宣称闭环完整**（H 层零代码、Letta/Graphiti 未验证、模型依从率未测） |
| Computer Use / Browser | 2026-11-23 | ✅ 已收束（11-29 换域 → AI Infra / 本地边缘；一周驻留，源码级结案） | 起点：3 张既有卡（computer-browser-use-2026 / browser-harness-2026 / webwright-2026）+ 事件侧 2 条本地控制面证据（CVE-2026-48989 Windows-MCP 无认证+通配 CORS、CVE-2026-112136 Mendix 9.2）+ Memory 交接三判据（动作门控位置 / 判定依据外部 / 回执可核验）｜待建：能力树 A~H（环境表示 / 动作空间与 grounding / 感知与自验证 / 会话与状态 / 隔离与凭据 / 信任边界 / 人机交接 / 可观测与回放） |
| AI Infra / 本地边缘 | 2026-11-30 | 🆕 第一周待开始 | 起点：SGLang v1.0 + Intel first-class（11-27）、vLLM 0.34.0（11-16）、ggml v1.0.0、Edge0-145B、Inkling 2 Mini、`[cand]local-edge-llm-2026`、知识空白 G3｜待建：能力树 A~H（推理引擎与服务 / 量化与显存 / 本地运行时与后端 / 模型分发与供应链 / 性能口径与可复现 / 部署形态与信任边界 / 与 Agent 的接缝 / 可观测与容量）｜携带判据：判断 9（入口×部署形态）、判断 11（证据深度分级） |
