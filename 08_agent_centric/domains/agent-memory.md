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
└── G. 与执行状态的分界（State vs Memory）
    ├── G1. workflow store（步骤/检查点/重放）——可重放，不作事实来源
    ├── G2. snapshot / checkpoint——恢复运行，不等于记忆
    └── G3. 共用后端时的命名空间与权限隔离（Dapr 双 store 先例）
```

## 二、基线：已知 / 缺口 / 相邻未覆盖

### 已知锚点（不重复收集）
| 锚点 | 状态 | 关键事实（含口径警示） |
|---|---|---|
| **Mem0** | [cand] S，周五验证 | v3 单遍 ADD-only 抽取 + 多信号检索；**已移除图存储**；README 92.5 LoCoMo / 94.4 LongMemEval **注明反映托管平台**，开源 SDK 拿不到；v3 相对 v2：LoCoMo 71.4→91.6、LongMemEval 67.8→93.4，成本降 3-4x |
| **Zep / Graphiti** | [cand] S，周五验证 | 时序知识图谱 + 双时间事实 + ABAC/保留/审计；自报 DMR 94.8%；**原 LoCoMo 84% 被独立复测更正为 58%**；**增量（10-29）：Community Edition 开源**（首个图驱动 Zep 产品），周五改为读 CE 源码/本地服务验证 |
| **Hy-Memory 2.0（腾讯混元）** | **A，本周新升锚点**（10-19 曾仅记日志） | 三层全开源：Hy-Memory-30B-A3B（Apache-2.0，记忆读写专用，可换装到 Mem0/MemOS）+ 框架 SDK + MemHub（10 工具共享记忆）。自称首个「工作记忆 + 代码记忆」框架；**自报** LoCoMo 72.6%（开源框架第一，1527 题）/ MemoryArena 55.31 / CodeMemoryBench 64.2·35.6；存储占用 6.06%；腾讯三条业务线生产接入。**口径警示：厂商自报、子集与 Mem0 不同，不可横比** |
| **Letta** | [cand] S，周五验证 | Core-Recall-Archival 自编辑；2026-03 转 memory-first harness；Context Constitution / Context Repositories（git 式版本化）；Letta Code（Apache-2.0） |
| **A-MEM** | [cand] 观察 | Zettelkasten 动态组织 + 链接，NeurIPS 2025，研究向 |
| **MemEval（ProsusAI）** | [cand] 观察 | 独立排名：Memory-R1 0.389 / SimpleMem 0.358 / Mem0 0.344 / MemU 0.299 F1 |
| **平台内置记忆** | 已记日志 | Anthropic Managed Agents `/mnt/memory/` 文本目录（public beta）；AgentCore Memory 短/长时分离 + `IngestData` 直投；MS AF `agent-framework-azure-cosmos-memory`；Vercel eve 文件记忆 + 可插拔存储；Grok Build markdown notes |
| **文件/Git-native 路线** | 已记日志 | OKF Agent Memory（Markdown+YAML frontmatter，本地 BM25）与 KnowlegeMap 仓库同构；Mem0 × dsh 原生插件（跨会话 memory bank） |
| **学术新线（2026-09~11）** | 已记日志 | EnSIMem（证据保留）/ SEEM（事件帧+RPE 溯源）/ Synapse（激活扩散）/ Jev-Mem（双过程+检索预算）/ Mem++（版本化）/ DyadMem（用户×关系双维）/ RealCompanion（真实对话审计）/ Below-the-Prompt（KV 作为记忆，136× 冷 TTFT）/ MemMachine（2604.04853，ground-truth-preserving）/ MINDSET（2610.08586，能量式演化）/ Curation+Consolidation（2610.39790，离线巩固） |
| **基准批判五条** | FACT（二手分析） | ① 长上下文模型碾压记忆管线（LoCoMo +35.2pp / LongMemEval +33.4pp）；② LoCoMo 1540 题中 99 处得分污染（6.4%）；③ RealCompanion：recency 窗口已满足 95.9% 交互，96% 增益来自无需历史的查询；④ **命题错位**（11-10 新增）：LoCoMo 94% 题只需 ≤2 个 session、LongMemEval 85%，平均约 1 个 session，LongMemEval 最多 2 次知识更新——名义「长期记忆」实际测「单/双会话检索」；⑤ **存储≠会用**（11-11 新增，StreamMemBench）：8 系统 × 2 backbone，证据已存储、反馈已局部吸收，仍无法用于后续决策或转成后续行为——测 recall 的基准测不到记忆的最后一公里 |

### 缺口（本领域内、本周重点）
| 缺口 | 证据 | 优先级 |
|---|---|---|
| **基准口径核验**（平台分 vs SDK 分、厂商自报 vs 独立复测） | Mem0 README 自注、Zep 84→58、LoCoMo 6.4% 污染 | **S（周五必做）** |
| **写入策略实证对照**（ADD-only 去图 vs 时序图 vs 文件全量） | Mem0 v3 移除图存储；Zep 反向押注；Anthropic/OKF 文件路线 | **A（周五验证）** |
| **作用域与租户隔离**（含 TeamMind 权限缺口④） | Apple SSPM 共享 RBAC、Zep ABAC、dsh 共享 bank | **A（承接 Runtime 缺口④）** |
| **注入/污染防御可落地形态** | 事件日 13 跨会话注入、PersistBench、OWASP Agent Memory Guard | **S（威胁已实证）** |
| 生命周期（遗忘/冲突/版本化）工程实践 | Mem++ 仅有论文；各厂商 TTL 口径不明 | B |
| 与执行状态共存的命名空间设计 | Dapr 双 store 有先例但无权限对照 | B |

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
| 周五 11-13 | ① `pip install mem0ai` 跑最小 add/search，核对其实际能力边界；② Graphiti 数据模型（节点/边/双时间）读源码；③ Letta 三级记忆 API 表面；④ 基准口径对照表 | 能回答"开源版能否达到自报分"与"三路线各自成本" |
| 周六 11-14 | 回灌 index/connections/能力树/graph | 每条验证结论有落点 |
| 周日 11-15 | 小结 + 换域判断（下一候选 Computer Use / Browser） | 三环闭合才换域 |

## 四、基线判断（本周起点，待验证）
1. **记忆不是一个库，是六个可独立失败的面**：写入、检索、生命周期、作用域、信任边界、与执行状态的分界。只比检索分数会漏掉其余五个。
2. **基准分数不可直接采信**：至少三重口径差——平台 vs SDK、厂商自报 vs 独立复测、合成基准 vs 真实对话（RealCompanion）。任何记忆选型必须先固定口径。
3. **2026 路线三分**：抽取简化（Mem0 去图）/ 时序图治理（Zep）/ 文件仓库（Anthropic `/mnt/memory`、Grok Build、OKF）。文件路线与 KnowlegeMap/GrowthOS 同构，是低成本可试项；图路线是企业治理与多跳关系场景。
4. **记忆已是攻击面**：跨会话注入可持久存活，"写入"等于"植入后门"；记忆模块必须自带来源标注、写入审计与删除权，否则不应接入生产 agent。

## 五、项目映射
- **Tafcm**：recency 窗口优先（RealCompanion 95.9%），文件/Markdown 记忆 + 本地索引，不先引向量库；token 预算按 Jev-Mem 思路设上限与自适应停止。
- **TeamMind**：跨会话状态按 G1/G2/G3 与记忆分离；作用域四级（会话/用户/租户/agent）+ ABAC；承接 Runtime 缺口④，与 dsh credentials seam / MXC 隔离做逐项对照。
- **silver-shield**：F1~F5 作为检测维度（注入、污染、谄媚、审计缺失、删除不彻底），PersistBench 作为基线用例来源。
- **KnowlegeMap / GrowthOS**：证据保留（EnSIMem/SEEM）+ 版本化（Mem++）已被本项目实践验证，可作为"文件即记忆"路线的自身样本。；**2026 产品化信号（11-05 Zep Agent Skills：运行轨迹→已验证程序，小模型接近 Opus 5.5；Hy-Memory 代码记忆记「为什么这样改」）** |
