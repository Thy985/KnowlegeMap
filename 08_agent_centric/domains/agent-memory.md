# Domain Tree · Agent Memory（记忆实现层 / 记忆治理）

> 建立：2026-11-09（周一，Memory 周第一天）｜ 类型：领域能力树/基线
> 定位：TeamMind（跨会话状态）/ Tafcm（本地记忆）/ silver-shield（记忆污染检测）/ GrowthOS（经验管理）共性底座；也是 11-07 事件日 13「跨会话记忆注入」的直接防御面。
> 树与图分工：本文件是 Tree；跨域复用见 `08_agent_centric/capabilities/graph.md`。
> 上游分层前提（Runtime 周结论）：**执行状态（workflow store / actor snapshot）≠ 会话记忆（memory store）**，两者可共用存储但语义、生命周期、信任边界不同。

## 一、领域树

```
Agent Memory
├── A. 记忆分层（Memory Tiering）
│   ├── A1. 工作记忆（context window / scratchpad，会话内、易失）
│   ├── A2. 情景记忆（episodic：发生了什么/何时/与谁，带时间戳）
│   ├── A3. 语义记忆（semantic：事实、偏好、关系，去时间化）
│   ├── A4. 程序性记忆（procedural：技能/工作流/工具用法，可执行）
│   └── A5. 分层映射（Core-Recall-Archival 三级 vs 短时/长时二分 vs 事件帧+图）
├── B. 写入策略（Write Path）
│   ├── B1. 抽取式（extract → ADD/UPDATE/DELETE；Mem0 v3 已简化为单遍 ADD-only）
│   ├── B2. 全量转储（整段落库，检索时再压缩；文件/Markdown 路线）
│   ├── B3. 选择性写入（只保留任务规格/schema/工具配置/输出约束；Apple SSPM）
│   ├── B4. 非破坏版本化（新文档而非原地编辑；Mem++）
│   └── B5. 写入门控（去重、事实性校验、敏感信息过滤、写入审批）
├── C. 检索与压缩（Read Path）
│   ├── C1. 向量相似度 / 混合检索（dense+sparse+metadata）
│   ├── C2. 图检索（时序知识图谱、实体索引、多跳遍历）
│   ├── C3. 激活动力学（spreading activation、Hebbian、侧抑制+时间衰减）
│   ├── C4. 证据保留 vs 摘要压缩（原文片段按需聚合；EnSIMem/SEEM）
│   └── C5. 检索预算与自适应停止（token 经济；Jev-Mem System-One 控制面）
├── D. 生命周期（Lifecycle）
│   ├── D1. 遗忘与衰减（TTL、时间衰减、容量上限）
│   ├── D2. 冲突消解（新旧事实冲突、来源优先级、时间有效性双时间）
│   ├── D3. 巩固与重组（episodic → semantic 提炼、聚类、去噪）
│   └── D4. 版本与回滚（按时间点回答"当时有效版本"）
├── E. 作用域与隔离（Scope & Isolation）
│   ├── E1. 会话 / 用户 / 租户 / agent 四级归属
│   ├── E2. 跨 agent 共享 memory bank（dsh 插件模式）
│   ├── E3. 共享记忆的 RBAC / ABAC（Apple SSPM、Zep 企业治理）
│   └── E4. 记忆读取的租户越权防护（同进程多租户串读）
├── F. 信任边界（Trust Boundary）
│   ├── F1. 记忆注入（prompt injection 持久化：写入即后门）
│   ├── F2. 记忆污染 / 投毒（跨会话传播、来源伪造）
│   ├── F3. 持久谄媚与跨域泄露（PersistBench 两类风险）
│   ├── F4. 审计与可追溯（谁写入、何时、依据哪条证据）
│   └── F5. 删除权与"被遗忘权"（真实删除 vs 逻辑标记）
├── G. 与执行状态的分界（State vs Memory）
    ├── G1. workflow store（步骤/检查点/重放）——可重放，不作事实来源
    ├── G2. snapshot / checkpoint——恢复运行，不等于记忆
    └── G3. 共用后端时的命名空间与权限隔离（Dapr 双 store 先例）
└── H. 子系统可靠性 / 可观测性（Reliability & Observability）
    ├── H1. 健康门（启动前 N 项自检，输出单行可读状态：`MEMORY-HEALTH: 11/11 GREEN`）
    ├── H2. 心跳（"该发生却没发生"也算失败：不触发即置 RED，含门自身）
    ├── H3. 降级诚实（向量腿坏了自动降 BM25-only，永不阻塞主流程，失败写 log-once 降级记录）
    ├── H4. 静默腐化防护（维度守卫/覆盖校验/水位新鲜度，把静默错误变成显式故障）
    └── H5. 告警预算（区分真故障与冷启动/未接集成，避免告警疲劳使告警本身失效）
```

## 二、基线：已知 / 缺口 / 相邻未覆盖

### 已知锚点（不重复收集）
| 锚点 | 状态 | 关键事实（含口径警示） |
|---|---|---|
| **Mem0** | [cand] S，周五验证 | v3 单遍 ADD-only 抽取 + 多信号检索；**已移除图存储**；README 92.5 LoCoMo / 94.4 LongMemEval **注明反映托管平台**，开源 SDK 拿不到；v3 相对 v2：LoCoMo 71.4→91.6、LongMemEval 67.8→93.4，成本降 3-4x；**11-13 本地实测（`mem0ai 2.2.1`）**：假 LLM/假 embedder + qdrant 本地路径跑通 `add`→`get_all` 2 条→`search` top **0.837**；代码级确认**单遍 `ADDITIVE_EXTRACTION_PROMPT`**、依赖表**无任何图库**、`expiration_date` TTL 已进 OSS、`timestamp` 仅平台；**`add()` 回执 `{"results": []}` 与 docstring 不符（写入成功但回执空）** |
| **Zep / Graphiti** | [cand] S；**CE 开源判定已作废（11-13 修正）** | 时序知识图谱 + 双时间事实 + ABAC/保留/审计，检索 p50 87ms；自报 DMR 94.8%；**原 LoCoMo 84% 被独立复测更正为 58%**。**修正**：CE 公告实为 **2024-09-26**（Daniel Chalef，"首个 KG 驱动 Zep 产品"，底层即 Graphiti），且帮助中心 FAQ 明确 **CE 已 deprecated、不再支持**；`getzep/zep` 仓库自述"不是 Zep 产品"、只有 examples/integrations、无 `legacy/`；10-29 博文是《How Zep Context Graphs keep two timelines for every fact》。→ **开源线只剩 Graphiti**（自建需 Neo4j 5.26+/FalkorDB + Redis），产品线只剩云 + BYOC。产品增量：v4 Context API（10-14，沿图导航 + 读回图构建方式）、Zep Agent Skills（11-05，轨迹→已验证程序） |
| **Hy-Memory 2.0（腾讯混元）** | **A，本周新升锚点**（10-19 曾仅记日志） | 三层全开源：Hy-Memory-30B-A3B（Apache-2.0，记忆读写专用，可换装到 Mem0/MemOS）+ 框架 SDK + MemHub（10 工具共享记忆）。自称首个「工作记忆 + 代码记忆」框架；**自报** LoCoMo 72.6%（开源框架第一，1527 题）/ MemoryArena 55.31 / CodeMemoryBench 64.2·35.6；存储占用 6.06%；腾讯三条业务线生产接入。**口径警示：厂商自报、子集与 Mem0 不同，不可横比** |
| **Letta** | [cand] S，周五验证 | Core-Recall-Archival 自编辑；2026-03 转 memory-first harness；Context Constitution / Context Repositories（git 式版本化）；Letta Code（Apache-2.0） |
| **A-MEM** | [cand] 观察 | Zettelkasten 动态组织 + 链接，NeurIPS 2025，研究向 |
| **MemEval（ProsusAI）** | [cand] 观察 | 独立排名：Memory-R1 0.389 / SimpleMem 0.358 / Mem0 0.344 / MemU 0.299 F1 |
| **平台内置记忆** | 已记日志 | Anthropic Managed Agents `/mnt/memory/` 文本目录（public beta）；AgentCore Memory 短/长时分离 + `IngestData` 直投；MS AF `agent-framework-azure-cosmos-memory`；Vercel eve 文件记忆 + 可插拔存储；Grok Build markdown notes |
| **文件/Git-native 路线** | 已记日志 | OKF Agent Memory（Markdown+YAML frontmatter，本地 BM25）与 KnowlegeMap 仓库同构；Mem0 × dsh 原生插件（跨会话 memory bank） |
| **学术新线（2026-09~11）** | 已记日志 | EnSIMem（证据保留）/ SEEM（事件帧+RPE 溯源）/ Synapse（激活扩散）/ Jev-Mem（双过程+检索预算）/ Mem++（版本化）/ DyadMem（用户×关系双维）/ RealCompanion（真实对话审计）/ Below-the-Prompt（KV 作为记忆，136× 冷 TTFT）/ MemMachine（2604.04853，ground-truth-preserving）/ MINDSET（2610.08586，能量式演化）/ Curation+Consolidation（2610.39790，离线巩固） |
| **SIx Harness《Memory as Infrastructure》** | **A，11-12 新升锚点** | arXiv 2609.05510（Mike Helwig，独立研究者，MIT）：**月级真实运营记录**，非基准论文——单条 Claude Code 会话线连续 **8 个月**、驱动 **633,446 行** / 1,936 文件 + 448 份设计文档。系统五件：本地 SQLite（FTS5/BM25 + sqlite-vec，embedding 走本地 Ollama，**无云无 API key**）/ anti-recurrence store（记"已决定"与"试过并否决"，**154 决策 + 186 死路 → 仅 59 + 47 入册**）/ precision-gated injection（意图门→IDF 罕见词门→每会话阻尼→三类块）/ **11 项健康门 + 每 hook 心跳 + 告警预算**（`MEMORY-HEALTH: 11/11 GREEN`）/ 约定模板（resume anchor、不变量文件、append-only ledger）。数字：**78,933 次 hook 调用、85 次失败全部记录零静默**（最后 20 天为 0）、10 天精度埋点零误报、3 起生产事故从读数追到结构性修复。**四类失败**：知识丢失（compaction 摘掉"为什么"）/ 重复劳动（三个会话各自重提议已建成且休眠的子系统）/ 上下文退化（"学到的噪音"比没有更糟）/ **静默记忆死亡**（索引/embedding/hook 悄悄坏掉，所有人继续信任）。**局限：N=1、无对照组、自报** |
| **MemEvolve / EvolveLab** | **A−，11-12 新记（2025-12 论文，ICML'26 接收）** | 把**记忆架构本身**当进化对象：内层 agent 在固定记忆下积累经验，外层用任务表现做适应度**元进化**。设计空间拆 Encode / Store / Retrieve / Manage，并把 **12 个代表性记忆系统**统一重实现为 **EvolveLab**（11-13 源码核对：`providers/` 共 **13 个** = 12 基线 + Evolver 自身；统一 `BaseMemoryProvider.provide_memory(MemoryRequest)` / `take_in_memory(TrajectoryData)`）。成绩：SmolAgent / Flash-Searcher 最高 **+17.06%**，TaskCraft 上演化架构跨基准/跨 backbone 仍 +2.0~9.09%。价值：①「记忆架构无全局最优、须按任务域自适应」有实验支撑；② EvolveLab 可作横向对照台（门槛：API keys + GAIA/WebWalkerQA/xBench；本轮**仅结构验证未跑行为**） |
| **基准/口径批判六条** | FACT（二手分析） | ① 长上下文模型碾压记忆管线（LoCoMo +35.2pp / LongMemEval +33.4pp）；② LoCoMo 1540 题中 99 处得分污染（6.4%）；③ RealCompanion：recency 窗口已满足 95.9% 交互，96% 增益来自无需历史的查询；④ **命题错位**（11-10 新增）：LoCoMo 94% 题只需 ≤2 个 session、LongMemEval 85%，平均约 1 个 session，LongMemEval 最多 2 次知识更新——名义「长期记忆」实际测「单/双会话检索」；⑤ **存储≠会用**（11-11 新增，StreamMemBench）：8 系统 × 2 backbone，证据已存储、反馈已局部吸收，仍无法用于后续决策或转成后续行为——测 recall 的基准测不到记忆的最后一公里；**11-12 由 SIx Harness 以「retrieved-but-unused」独立佐证**（信息就在上下文里、就是没被用），两条证据来自完全不同的场景（合成基准 vs 8 个月真实工作流）；⑥ **口径穿透到回执层**（11-13 新增，Mem0）：`add()` docstring 承诺返回 `{"results":[{"id","memory","event":"ADD"}]}`，实测返回 **`{"results": []}`** 而数据确实已落库——不只分数，**连写入回执都与平台口径不同**；工程上必须以 `get_all` / 向量库状态为写入确认 |

### 缺口（本领域内、本周重点）
| 缺口 | 证据 | 优先级 |
|---|---|---|
| **基准口径核验**（平台分 vs SDK 分、厂商自报 vs 独立复测） | Mem0 README 自注、Zep 84→58、LoCoMo 6.4% 污染；**11-13 实测再增一层：`add()` 回执为空而数据已落库** | **S（周五已完成）** |
| **写入策略实证对照**（ADD-only 去图 vs 时序图 vs 文件全量） | Mem0 v3 移除图存储并经本地实测确认；Zep 反向押注（但 CE 已 deprecated，只剩 Graphiti 自建）；Anthropic/OKF 文件路线 | **A（周五已完成）** |
| **作用域与租户隔离**（含 TeamMind 权限缺口④） | Apple SSPM 共享 RBAC、Zep ABAC、dsh 共享 bank | **A（承接 Runtime 缺口④）** |
| **注入/污染防御可落地形态** | 事件日 13 跨会话注入、PersistBench、OWASP Agent Memory Guard | **S（威胁已实证）** |
| 生命周期（遗忘/冲突/版本化）工程实践 | Mem++ 仅有论文；各厂商 TTL 口径不明 | B |
| 与执行状态共存的命名空间设计 | Dapr 双 store 有先例但无权限对照 | B |
| **记忆子系统可靠性**（健康门/心跳/降级可见/告警预算） | SIx Harness 11 项健康门 + 85 次失败零静默；本项目与 Tafcm 均无对应实现 | **A（能力树已补 H 层，落地待做）** |
| **写入/删除的回执语义**（怎么确认真的写进去 / 真的删干净） | Mem0 `add()` 空回执；事件日 18 供应商侧留存证明"删了主库≠删干净" | B |

### 相邻未覆盖（领域外，可外推）
| 相邻方向 | 连接点 | 归属 |
|---|---|---|
| Computer Use / Browser | 操作记忆复用（Anchor Action Index 确定性回放） | 下一周候选 |
| AI Infra / 本地边缘 | KV 作为记忆（Below-the-Prompt）、KVCacheStore 持久化 | 后续周 |
| Evaluation | 记忆基准（MemEval/BEAM/DyadMem）与 judge 可靠性 | 已闭环，按需回取 |

## 三、本周验证计划（对齐 current_focus 每日分工）
| 日 | 任务 | 判定标准 |
|---|---|---|
| 周一 11-09 | 本文件建立 + 基线 | 六层齐全、缺口可验证（已完成） |
| 周二~四 11-10~12 | 增量：Mem0/Zep/Letta 新 release、MCP 记忆生态、AgentCore Memory 变更 | 只写 S/A/B，先查 06 index |
| 周五 11-13 ✅ | ① `mem0ai 2.2.1` 本地 add/search（**已做**：add→get_all 2 条→search 0.837；单遍 ADDITIVE、无图依赖、TTL 可用、**回执为空**）；② Graphiti 数据模型（**改为 Zep CE 事实核验**，判定 CE 已 deprecated）；③ Letta 三级记忆 API（**未执行**，时间不足）；④ 基准口径对照表（**已做**：六条批判 + EvolveLab 结构核对） | 已回答"开源版能否达到自报分"（不能直接对上：回执与分数两处口径都不同）与"三路线各自成本"（Mem0 最轻、Graphiti 需图库栈、文件路线最省） |
| 周六 11-14 ✅ | 回灌 index/connections/能力树/graph（**已完成**：H 层、锚点两加两修、批判六条、connections 两行） | 每条验证结论有落点 |
| 周日 11-15 | 小结 + 换域判断（下一候选 Computer Use / Browser） | 三环闭合才换域 |

## 四、基线判断（本周起点，待验证）
1. **记忆不是一个库，是六个可独立失败的面**：写入、检索、生命周期、作用域、信任边界、与执行状态的分界。只比检索分数会漏掉其余五个。
2. **基准分数不可直接采信**：至少三重口径差——平台 vs SDK、厂商自报 vs 独立复测、合成基准 vs 真实对话（RealCompanion）。任何记忆选型必须先固定口径。
3. **2026 路线三分**：抽取简化（Mem0 去图）/ 时序图治理（Zep）/ 文件仓库（Anthropic `/mnt/memory`、Grok Build、OKF）。文件路线与 KnowlegeMap/GrowthOS 同构，是低成本可试项；图路线是企业治理与多跳关系场景。
4. **记忆已是攻击面**：跨会话注入可持久存活，"写入"等于"植入后门"；记忆模块必须自带来源标注、写入审计与删除权，否则不应接入生产 agent。
5. **记忆会从两个相反方向失败，所以可靠性层是一等公民**（11-14 回灌，SIx Harness）：一边是**重复发现已存在的东西**（缺去重、缺"试过并否决"记录），一边是**依据腐坏记录行动**（缺过期告警、缺健康检查）。两者需要刻意对立的两套运维规则并保持张力，不能合成一条"优化记忆质量"的口号。**"静默记忆死亡"比检索分数低更危险**——索引/embedding/hook 悄悄坏掉，而所有人继续信任它。可观测性不是运维附属，是记忆系统的第七个面（H 层）。

## 五、项目映射
- **Tafcm**：recency 窗口优先（RealCompanion 95.9%），文件/Markdown 记忆 + 本地索引，不先引向量库；token 预算按 Jev-Mem 思路设上限与自适应停止。
- **TeamMind**：跨会话状态按 G1/G2/G3 与记忆分离；作用域四级（会话/用户/租户/agent）+ ABAC；承接 Runtime 缺口④，与 dsh credentials seam / MXC 隔离做逐项对照。
- **silver-shield**：F1~F5 作为检测维度（注入、污染、谄媚、审计缺失、删除不彻底），PersistBench 作为基线用例来源。
- **KnowlegeMap / GrowthOS**：证据保留（EnSIMem/SEEM）+ 版本化（Mem++）已被本项目实践验证，可作为"文件即记忆"路线的自身样本。
- **Tafcm（11-14 补充）**：SIx Harness 的**两类契约**可直接借——**诚实降级**（向量腿缺失时自动降 BM25/纯文本，永不阻塞主流程，降级写 log-once 记录）与**维度守卫**（向量宽度不匹配直接拒收，把静默腐化变显式故障）。若坚持纯 Markdown，必须能回答"向量腿缺失时检索质量如何诚实降级"，否则等于把静默失败留给自己。
- **TeamMind（11-14 补充）**：跨会话状态子系统需自带健康门 + 心跳，"不触发也算失败"要写进 hook 设计；否则团队记忆坏了没人知道，比没有记忆更糟。
- **silver-shield（11-14 补充）**：**"静默记忆死亡"是新检测维度（F6 候选）**——索引新鲜度、向量覆盖率、hook 心跳缺失、写入回执与实际落库不一致（Mem0 已实测出这一条），都可作为确定性检测项，不依赖 LLM 判断。
- **产品化信号（2026）**：Zep Agent Skills（11-05，运行轨迹→已验证程序，小模型接近 Opus 5.5）与 Hy-Memory 代码记忆（记"为什么这样改"）同向——赛道正从「存什么/怎么检索」转向「经验→可复用技能」（A4 程序性 × D3 巩固合流）。

## 六、11-14 回灌记录（周六，Memory 周 Day6）
| # | 回灌动作 | 落点 |
|---|---|---|
| 1 | 新增 **H 层（子系统可靠性/可观测性）**：健康门 / 心跳 / 降级诚实 / 静默腐化防护 / 告警预算 | §一 树 H1~H5；§四 判断 5；§五 Tafcm·TeamMind·silver-shield 三条补充 |
| 2 | 基准批判第 ⑤ 条并入 SIx「retrieved-but-unused」作**第二独立证据** | §二 批判行 ⑤（注明两证据来自合成基准 vs 8 个月真实工作流，互不依赖） |
| 3 | 新增第 ⑥ 条 **口径穿透到回执层**（Mem0 `add()` 空回执 vs data 已落库） | §二 批判行 ⑥；缺口表"基准口径核验"证据列；新增缺口"写入/删除回执语义" |
| 4 | 修正锚点表 **Zep 行**：CE 公告 2024-09-26 且已 deprecated → 开源线 = Graphiti | §二 Zep 行；状态由"A− 周五验证"改为"CE 开源判定已作废" |
| 5 | 新增锚点 **SIx Harness（A）** 与 **MemEvolve/EvolveLab（A−）**；Mem0 行补本地实测 | §二 锚点表 |
| 6 | 缺口表两行改"已完成"，新增"可靠性"（A，落地待做）与"回执语义"（B） | §二 缺口表 |
| 7 | 验证计划表周五/周六行回填结果与未执行项 | §三 |
> 未回灌项（如实挂账）：Letta 三级记忆 API 实测未做；Graphiti 本地部署成本（Neo4j 5.26+/FalkorDB + Redis）未实测；EvolveLab 仅结构验证未跑行为；SIx/MemEvolve 未做源码级核对（SIx 为 N=1 自报）。
