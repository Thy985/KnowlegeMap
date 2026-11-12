# 候选证据卡 · [cand] Agent Memory 2026 实现层全景 + 基准批判

> 状态：`[cand]` ｜ 分类：Agent Memory 实现前沿（S4） ｜ 发现：2026-09-01 ｜ 等级：**S**

## 一句话定位
Agent 记忆实现层 2026 已分层成熟（Mem0 抽取式 / Zep 时序知识图谱 / Letta 自编辑记忆 / A-MEM Zettelkasten），且有 MemEval 等独立基准开始给系统排名；同时出现对记忆基准本身可靠性的批判——这正需要我的"证据纪律"来甄别。

## 1. 它是什么 / 解决什么问题
| 框架 | 记忆模型 | 2026 关键动态 |
|---|---|---|
| **Mem0** | 抽取+检索，向量优先 | 2026-04 新算法（单遍分层抽取+多信号检索）：LoCoMo 92.5 / LongMemEval 94.4 / BEAM(1M) 64.1["https://mem0.ai/blog/state-of-ai-agent-memory-2026?ref=swarmsignal.net"]；**雷达增量（2026-09-02）**：SDK 2.0 单遍抽取（写延迟 ↓50%）+ 混合检索器["https://github.com/enflory/ingolmo/blob/main/standalone-memory-tools-survey-2026/README.md"]；Platform v3 支持时间感知检索（"上周/即将/现在"）["https://docs.mem0.ai/changelog/highlights"]；Letta 2026-08 发布 **Agents SDK**（stateful persistent agents）+ 2026-06 **Mods**（harness 级自改进）["https://www.letta.com/blog/"] |
| **Zep (Graphiti)** | 时序知识图谱，双时间事实+溯源，框架无关，数据层治理（ABAC/保留/审计） | 面向企业生产；自称 LoCoMo 领先、检索 p50 87ms["https://www.getzep.com/mem0-alternative/"] |
| **Letta** | 自编辑记忆（MemGPT 系），Core/Recall/Archival 三级 | 2026-03 转向"memory-first agent harness"，押注 computer use["https://www.letta.com/blog/our-next-phase"] |
| **A-MEM** | Zettelkasten 动态组织+链接（NeurIPS 2025） | ~1K stars，研究向["https://github.com/Anandesh-Sharma/awesome-agentic-memory"] |
| **MemEval** | 独立评测套件（ProsusAI，2026-08） | 排名：Memory-R1 0.389 / SimpleMem 0.358 / Mem0 0.344 / MemU 0.299 F1["https://github.com/ProsusAI/MemEval"] |

**基准与批判**：三主流基准 LoCoMo（趋于饱和 ~92）/ LongMemEval（ICLR25，更难）/ BEAM（1M/10M token）。**两条关键批判**：① 长上下文模型直接碾压记忆管线（LoCoMo +35.2pp、LongMemEval +33.4pp）——压缩是 lossy 的["https://dreaming.press/posts/how-to-read-an-agent-memory-benchmark.html"]；② LoCoMo 被审计出 1540 题中 99 处得分污染错误（6.4%）["https://essays.bloo-mind.ai/posts/2026-05-20-mem-eval/"]
> **雷达增量（2026-09-04，Changed）**：
> - **Mem0 v3.0.0 新记忆算法（2026-04 起）**：ground-up 重写记忆 pipeline，LoCoMo 71.4→91.6（+20）、LongMemEval 67.8→93.4（+26），~3-4x 更低成本；README 现报 LoCoMo 92.5 / LongMemEval 94.4（~6.9K tokens/query）["https://docs.mem0.ai/changelog/highlights"]["https://github.com/mem0ai/mem0/"]
> - **重要可信度批判（数字本身有歧义）**：Mem0 README 高分注明"reflects managed platform（含开源 SDK 没有的 proprietary 优化）"——`pip install mem0ai` 拿不到 94 分；Zep 原始 LoCoMo claim 84% 已被更正为 58%（独立复测）["https://dreaming.press/posts/how-to-read-2026-agent-memory-scores.html"]["https://github.com/enflory/ingolmo/blob/main/standalone-memory-tools-survey-2026/README.md"]
> - **基准格局收敛**：LoCoMo / LongMemEval / BEAM 已成行业标准三件套（Mem0 官方报告 + automem 独立复测交叉验证）["https://automem.ai/blog/agent-memory-in-2026-an-honest-comparison-of-mem0-zep-letta-and-the-rest"]
> - **Letta 新方向**：2026-04 **Context Constitution**（agent 如何管理 context 学习的原则集）+ 2026-02 **Context Repositories**（coding agent 的 git-based 记忆版本化）["https://www.letta.com/blog-categories/research"]
> - **Zep 强化**：自报 DMR 94.8%（vs MemGPT 93.4%）、LongMemEval +18.5% 且 -90% 延迟——但均为厂商自报，需独立复测["https://www.developersdigest.tech/blog/best-ai-agent-memory-providers-2026"]
> - **Supermemory**：LongMemEval 自报 SOTA（81-85%）、MCP-原生适配 Claude Code/OpenCode——但多依赖自家技术报告["https://blog.csdn.net/qq_44193969/article/details/160620303"]
> - **含义**：记忆厂商"数字大战"激烈，但分数口径不一（平台 vs SDK），验证纪律（区分厂商自报 vs 独立评测）正是我的判断优势
> **雷达增量（2026-09-09，Changed）**：
> - **Mem0 × DeepSeek Harness 原生插件（2026-08-24）**：Mem0 发布 dsh Cordis 插件——跨会话持久记忆 + search/add 工具 + 服务端托管存储 + 生命周期原生集成，与 dsh 其他连接 agent 共享同一 memory bank；官方明言"dsh agent 会话间即忘"是痛点["https://releasebot.io/updates/mem0"]
> - **Letta Code（2026-09 观察）**：Letta 之上推出的 memory-first coding agent——单一持久化 agent 跨编码会话学习、可移植跨 LLM provider（Apache 2.0，~1.5k★）；"stateless 编码助手会话结束即忘"的对立面["https://www.evermx.com/open-source/letta-code-memory-first-coding-agent"]
> - **Zep 记忆检索嵌入基准**：Nemotron 3 Embed 1B（2026-07-16 发布）在生产 recall 查询 5954 条上击败 Zep 生产基线及另两模型["https://blog.getzep.com/"]
> - **含义**：记忆层正在"harness 原生嵌入"（Mem0→dsh、Letta→coding agent）——记忆不再是独立服务而是 harness 内置能力，TeamMind 记忆设计需对照此趋势
> **雷达增量（2026-09-13，Changed）**：
> - **Mem0 架构细节确认（Habr 09-07）**：新算法将两遍 extraction（extract→diff→ADD/UPDATE/DELETE）改为**单遍 ADD-only**（一次提取新事实、并排写入、检索时去重）；**同时移除图存储支持**——向量+关系检索的简化取向["https://habr.com/ru/articles/1028790/"]；Mem0 新 release（09-09）：Pi Agent Plugin v0.3.0（复用会话准备/记忆格式化/作用域工具）+ Strands 集成["https://github.com/mem0ai/mem0/releases"]
> - **Letta Trajectory（2026-07）**：开源包，把 Claude Code/Codex/Letta Code 等 harness 的编码会话**规范化为一套 token 高效标准格式**，供"agent 从经验中学习"——与 Trace-based Evaluation（09-12 新卡）同属"以行为数据为标准证据"范式，但 trajectory 面向学习/复用而非评测，两者可组合["https://www.letta.com/research/"]
> - **同线新项目（观察级）**：agentmemory（hansonkim，09-04，面向编码 agent 的持久记忆，自称基于真实世界基准第一，vs mem0 53K★/Letta 22K★）、agents-memory v1.1.0（Lolaplex，09-08，本地 markdown 记忆 + 跨 agent 上下文引擎）——均主打"编码 agent 记忆"，印证记忆→harness 内置化趋势["https://github.com/hansonkim/agentmemory"]["https://github.com/Lolaplex/agents-memory/releases"]
> - **含义**：① Mem0 去图存储说明"抽取-写入-检索"简化路线正在胜出，Zep 的时序图路线成为差异化分支；② trajectory/trace 标准格式若收敛，Agent 记忆、评测、经验学习将共享同一行为数据层——这是 TeamMind 数据层设计的强信号
> **雷达增量（2026-09-18，多平台密集动作）**：
> - **Apple Shared Selective Persistent Memory（09-16）**：识别并保留**四类可复用上下文**（任务规格/数据 schema/工具配置/输出约束）而丢弃会话推理痕迹；**记忆可跨用户共享（RBAC 角色访问控制）**——协作平台部署（与 Zep DMR 的"选择性"同线，新增共享/权限维度）["https://machinelearning.apple.com/research/shared-selective-persistent-memory"]
> - **Microsoft Agent Framework × Azure Cosmos DB 原生记忆（09-04）**：新 Python 包 `agent-framework-azure-cosmos-memory`（CosmosMemoryContextProvider）——agent 自动存对话轮次、提取持久记忆、召回相关事实——**框架级原生记忆**（与 MS AF 治理栈同生态）["https://devblogs.microsoft.com/agent-framework/native-memory-for-microsoft-agent-framework-with-azure-cosmos-db/"]
> - **MemForest（arXiv 2605.23986）**：把 agent 记忆重构为**写高效时序数据管理问题**——canonical facts 为持久写单元（证据与摘要/索引分离）、并行块提取解顺序瓶颈、分层时间索引["https://arxiv.org/html/2605.23986"]
> - **OKF Agent Memory（09-05）**：**Git-native 记忆层**（Open Knowledge Format v0.2）——架构决策/领域发现/操作事实存 Markdown+YAML frontmatter 直接进项目仓库，本地 BM25 索引免向量库——**与 KnowlegeMap 仓库模式同构**["https://aitoolly.com/ai-news/article/2026-09-06-okf-agent-memory-a-git-native-persistent-memory-solution-for-ai-coding-agents-and-project-knowledge"]
> - **Grok Build 跨会话记忆（09-16）**：xAI 终端 coding agent 后台记约定/决策/项目事实为 markdown notes，后续会话自动读回（含 Anthropic Managed Agents 同模式：memory=挂载 /mnt/memory/ 的文本文档目录，用 bash/file 工具读写）["https://www.unite.ai/xai-adds-cross-session-memory-to-grok-build-coding-agent/"]["https://opentools.ai/news/anthropic-managed-agents-add-memory-persistent-state-for-ai-that-actually-ships"]
> - **含义**：① **"记忆=文件/Markdown 仓库"路线成型**（OKF/Grok Build/Anthropic /mnt/memory）与"记忆=向量库"并行——前者与 KnowlegeMap 仓库模式、GrowthOS 经验管理直接同构，可低成本试；② Apple 引入"选择性 + 跨用户共享 RBAC"新维度；③ 记忆继续向 harness/平台内置化收敛（MS AF Cosmos、Grok Build）
> **雷达增量（2026-09-21，托管平台级"记忆即服务"成型）**：
> - **Claude Managed Agents 持久记忆 public beta（09-16，Anthropic 官方）**：托管 agents 跨会话保留/应用知识、自主"self-learn across sessions"——**"记忆=挂载 /mnt/memory/ 文本目录"从模式变官方产品**（与 Grok Build/OKF 同线的最强背书）["https://opentools.ai/news/claude-managed-agents-get-persistent-memory-in-public-beta"]
> - **AWS Bedrock AgentCore Memory direct ingestion（09-08）**：新 `IngestData` API 直接投喂内容进长时记忆（不经短时事件）——**短时/长时分离 + 显式写入 API**成为托管记忆标准结构["https://aws.amazon.com/about-aws/whats-new/2026/09/agentcore-memory-direct-ingest/"]
> - **Vercel eve agents 持久记忆（09-09）**：文件记忆默认落 Vercel Blob（跨重启/部署持久）+ 多 provider（Supermemory/Upstash AgentKit/自定义）——**文件记忆 + 可插拔存储**在托管平台落地["https://vercel.com/changelog/persistent-memory-for-eve-agents"]
> - **含义**：① **"记忆即服务"成型**——Anthropic/AWS/Vercel 三大托管平台两周内齐推持久记忆，Tafcm 的本地记忆设计可对照 AgentCore"短长时分离+直接投喂"与 Vercel"文件存储+可插拔"双结构；② Claude Managed Agents 官方落地 = **"记忆=文件仓库"路线（09-18 卡内判断）获最大厂商实证**——KnowlegeMap 仓库模式与 GrowthOS 经验管理的"文件记忆"选型信心增强；③ 托管记忆的**权限/隔离维度**（谁可读、跨会话归属）与 agentic-attack 卡"agent 账户接管"互证——**记忆即攻击面**（PaperCut 事件的边缘设备 + 记忆数据同属低价值高敏感资产）
> **雷达增量（2026-09-25，证据保留型记忆研究）**：
> - **EnSIMem（arXiv 2609.27279，09-23 提交）**：**实体结构化索引长期记忆**——按实体聚合索引而非有损摘要；agent 从**保留的源证据**（原文片段）生成回答而非从 lossy memory summaries——"证据保留"替代"压缩"成为记忆检索新取向（与 Validation 编译器"Evidence→Judgment"同构、对照 09-04 批判"压缩是 lossy 的"）["https://arxiv.org/abs/2609.27279"]
> - **含义**：① "记忆=证据库而非摘要库"获得明确方法论表述——**GrowthOS/KnowlegeMap 的"原文优先+结构化索引"路线（与 OKF 同线）再获学术支持**；② EnSIMem 的"实体结构化"可与 MemGraphRAG 三层记忆/Graph-R1 对照——记忆检索从"语义压缩"走向"结构保留+按需聚合"，这是 Tafcm 本地记忆与 silver-shield 证据链检索的设计输入
> **雷达增量（2026-09-29，记忆研究爆发：联想激活 + 双过程 + 事件溯源）**：
> - **Synapse（arXiv 2601.02744）**：**扩散激活（spreading activation）统一 episodic-semantic 记忆**——记忆建模为动态图，相关性由激活传播而非预计算相似度涌现；侧抑制 + 时间衰减动态高亮子图过滤干扰；Triple Hybrid Retrieval（几何+语义+图）融合——"图动力学替代向量相似度"["https://arxiv.org/html/2601.02744v1/"]
> - **REMem（ICLR 2026）**：episodic 推理——记忆"发生了什么/何时/与谁"+**跨事件时间推理**；离线构建 Hybrid Memory Graph（gists + 结构化事实三元组均带时间戳），在线 ReAct 用检索+图遍历工具迭代收集证据["https://en.papernotes.org/ICLR2026/llm_agent/remem_reasoning_with_episodic_memory_in_language_agent/"]
> - **HeLa-Mem**：**Hebbian 学习 + 联想记忆**——episodic 记忆图（节点=对话轮，含原文/嵌入/时间戳）+ 语义记忆存储双层级，联想巩固动力学["https://www.themoonlight.io/fr/review/hela-mem-hebbian-learning-and-associative-memory-for-llm-agents"]
> - **SEEM（arXiv 2601.06411）**：**结构化 episodic 事件记忆**——Episodic Event Frames（EEF）+ 图记忆层（关系事实）+ 动态 episodic 层（叙事推进）——**Reverse Provenance Expansion（RPE）**反推重建连贯上下文——与 EnSIMem"证据保留"同向并升级为"事件帧+溯源扩展"["https://arxiv.org/html/2601.06411"]
> - **Jev-Mem（arXiv 2609.23986）**：**System-One 控制面 agentic 记忆**——专用 System-One 控制器管记忆构建（类型/关系组织）+ 检索（查询路由/检索预算分配/图遍历/候选评分/自适应停止），System-Two 仅做复杂推理与合成——**快慢双系统分工落地到记忆**（与认知双过程同构）["https://www.alphaxiv.org/abs/2609.23986"]
> - **Dual-Process Memory 实证（arXiv 2605.17625）**：长时域科学 agent——即时 episodic 窗口（10 消息）与长期整合知识（3 tokens/消息）解耦；15,000 消息 × 6 LLM（3 家族）跨模型验证["https://arxiv.org/html/2605.17625"]
> - **含义**：① **记忆研究一周内新增 5 篇架构论文，三条新主线**——**联想激活**（Synapse/HeLa-Mem，替代静态向量相似度）、**双过程分工**（Jev-Mem/Dual-Process，快慢系统各司其职）、**事件/证据溯源**（SEEM-RPE/REMem，结构化事件帧+provenance 反推）；② **"图+激活动力学"成为记忆主流表述**——与 agentic-graphrag 卡的图记忆（Oracle 图感知检索）交叉，记忆与图检索两线融合加速；③ **SEEM 的 RPE 与 EnSIMem 证据线直接同向**——GrowthOS/KnowlegeMap"原文优先+溯源"路线从"摘要压缩反例"获得完整方法论家族支撑；④ Jev-Mem 的"检索预算分配+自适应停止"是 Tafcm 本地记忆的 token 经济设计直接输入（端侧预算敏感）
> **雷达增量（2026-10-03，记忆×harness 交叉 + 记忆安全 + 因果效用）**：
> - **Meta+UW Context Language Models（10-01）**：**agent 自编辑记忆优于固定 harness 且计算成本更低**——CLM 让模型直接读写自身上下文——**"记忆能力进模型" vs "记忆放 harness 外部系统"的路线之争获 Meta 实证**（直接命中 agent-harness 卡与 dsh 的 harness 架构选择）["https://mpost.io/meta-presents-context-language-models-ai-agents-that-edit-their-own-memory-outperform-fixed-harnesses-at-lower-compute-cost/"]
> - **Mem++（arXiv 2610.02002，10-01）**：**非破坏性版本化记忆**——组织 agent 决策以"新文档"而非"编辑"到达，回答须知道给定时间哪个版本有效——**记忆按版本/时间可回溯**（与 KnowlegeMap 文档历史语义同构）["https://arxiv.org/abs/2610.02002"]
> - **PersistBench（Semantic Scholar 10-02）**：**持久谄媚基准**——有状态个人 agent 的两类长期记忆风险：**跨域泄露 + 记忆诱导谄媚**——**记忆安全问题开始有专门基准**（与 silver-shield 风险检测线直接相关）["https://www.semanticscholar.org/paper/Agents-Don%27t-Just-Agree,-They-Remember:-Persistent-Mao-Zhao/7d05b3ee75c07f895b3b9751c6d7b9407ec8d937"]
> - **Causal Memory Policy（10-02）**：随机化检索暴露 + 逆概率加权——**识别每查询的真实记忆效用**（干预检索链路做因果识别）["https://chatpaper.com/chatpaper/paper/354840"]
> - **MemCodex（arXiv 2609.39765，09-30）**：**自编程分层记忆**——异质访问需求（单跳一条证据 vs 多跳遍历）驱动分层 + 动态代码生成组织["https://arxiv.org/html/2609.39765v1"]
> - **含义**：① **Meta CLM 是重要路线信号**——"记忆放模型内（CLM）vs 放 harness 外（托管记忆/插件）"的实证对照，dsh 的架构选择（harness 外记忆插件 dsh-memory-evolve vs 未来模型内）需要跟踪该线；② **记忆安全成为独立研究线**（PersistBench 谄媚/跨域泄露）——silver-shield 的"记忆污染/毒化检测"维度获得学术基准支撑；③ **版本化记忆（Mem++）+ 因果效用（CMP）**——"记忆即证据库"（EnSIMem/SEEM）再补"时间回溯"与"效用可识别"两个性质——GrowthOS/KnowlegeMap 原文优先路线的完整性质族成型
> **雷达增量（2026-10-07，记忆基准分层 + 真实效用批判 + 记忆×KV 交叉）**：
> - **DyadMem（arXiv 2610.03020，10-02）**：**长期记忆基准新定义 URAM**（User-conditioned Relational Agent Memory）——用户侧记忆与关系记忆沿同一多会话轨迹双标注——**3065 episodes / 50961 sessions / 61210 QA**——记忆评测从"单侧事实"走向"用户×关系双维"["https://arxiv.org/abs/2610.03020"]
> - **past.dev Frontier Memory（10-05/06）**：**BEAM（ICLR 2026）最大公开记忆基准第 1 名**——100K tokens 92.08%（前最佳 86.2%）/ 500K 89.63% / **10M 85.03%（BEAM10M，跨 100 倍上下文仅掉 7 分）**——记忆基准商业化（对比 Exabase M-1 68.0%/mem0/Hindsight）["https://www.prnewswire.com/news-releases/pastdev-introduces-frontier-memory-for-ai-agents-1-on-beam-the-largest-public-memory-benchmark-302899770.html"]
> - **RealCompanion 审计（10-05）**：**120 天真实对话审计暴露合成基准问题**——**基础 recency 窗口满足 95.9% 用户交互；96% 的记忆增益来自无需历史证据的查询**——"合成基准显著夸大记忆效用"批判（对照 BEAM/长程基准）["https://www.aicoder.com/news/news-20261005-realcompanion-longitudinal-conversations-agent-memory"]
> - **Agent Memory Below the Prompt（arXiv 2603.04428）**：**KV state block pool 记忆**——量化 + 持久化 KV——Gemma 3 12B 上冷 TTFT **172096→1264ms（32K 上下文 136×）**——记忆与 KV 缓存交叉（对照 KVCacheStore 产品线）["https://memorypapers.org/"]
> - **含义**：① **记忆基准进入"合成 vs 真实"分层**——BEAM 类测上限、RealCompanion 类测真实收益——dsh 记忆投入判断应以"真实对话收益"为准绳（recency 窗口先满足再谈长期记忆）；② **DyadMem 的用户×关系双维**提示记忆评测要覆盖"与用户的关系状态"（dsh-memory-evolve 做用户侧记忆时参考）；③ **KV 记忆交叉**（Below-the-Prompt 136×）——记忆持久化与 KV 缓存是同一存储问题的两面，Tafcm 本地记忆与推理共享存储层设计

> **雷达增量（2026-11-10，Memory 周 Day2：新锚点 + 基准口径补强）**：
> - **A｜腾讯混元 Hy-Memory 2.0（2026-10-16，三层全开源）**：Hy-Memory-30B-A3B（Apache-2.0，约 3B 激活，专训记忆读写策略，可接入 Mem0/MemOS 置换其写入模型）+ Hy-Memory 框架 SDK + MemHub 应用（**10 个 AI 工具共享一份个人记忆**：Cursor/Codex/Claude Code/OpenCode/OpenClaw/Qwen Code/DeepSeek Harness 等）。**自称首个提出工作记忆 + 代码记忆**：工作记忆记任务目标/已定做法/阶段结果/可复用经验及**适用条件**；代码记忆记「为什么这样改」。**自报成绩**：LoCoMo 72.6%（开源框架第一，1527 道非 adversarial 题）、MemoryArena 55.31（+10.2pt）、CodeMemoryBench 64.2/35.6、SWE-ContextBench 28.3；存储占用 6.06%；腾讯自选股（多跳召回 50→90、冲突消解 67→83）、iWiki、腾讯新闻已生产接入。**口径警示**：全部厂商自报、无独立复测，且题目子集/裁判模型与 Mem0 的 92.5 不同，**不可直接横比**。→ 升 A 级锚点：直接覆盖 B 层（写入策略变成可托管/可检查的模型工件）与 A2/A4（工作与程序性记忆）；MemHub 是 E 层跨工具共享记忆的现成样本。
> - **A−｜Zep Community Edition 开源（2026-10-29）**：首个基于知识图谱的 Zep 产品开源（Context Graph 双时间线：事实何时为真 + 何时入库）。→ 周五验证由「读文档」改为「读 CE 源码 + 本地起服务」，可部分绕开 Zep 云端口径不可复现的问题。
>   - **11-13 验证日修正（原判定作废）**：CE 公告实为 **2024-09-26**（Daniel Chalef，"首个 KG 驱动的 Zep 产品"），不是 2026-10-29；10-29 博文是《How Zep Context Graphs keep two timelines for every fact》机制说明。Zep 帮助中心 FAQ 明确 **CE 已 deprecated / 不再支持**，开源线转向 **Graphiti**；`github.com/getzep/zep` 现为 examples/integrations 仓库（README 自述"不是 Zep 的产品或服务"），无 `legacy/` 目录。→ 本条降为 **B 观察**：Zep 只剩云产品 + Graphiti 开源框架，自建需 Neo4j 5.26+/FalkorDB + Redis + LLM/embedding 配置。
> - **B｜研究三则**：**MemMachine**（arXiv 2604.04853，ground-truth-preserving：存原始 episode、少做 LLM 抽取、邻域上下文扩展检索——正对 C4 证据保留）；**MINDSET**（arXiv 2610.08586，能量式记忆演化，控制器跨 benchmark 迁移性受质疑）；**Complementary Curation and Consolidation**（arXiv 2610.39790，离线合并冗余/移除冲突过期——正对 D3 巩固）。
> - **B｜Mem0 实现细节（Memory Atlas 11-01 核对）**：实体链接用 spaCy（`mem0ai[nlp]`），实体写入平行向量子集合 `{collection}_entities`，检索将实体匹配分并入 dense+keyword 排序；2026 年已移除 Neo4j/Memgraph/Kuzu/AGE/Neptune 外部图库——与「v3 去图」一致，作为周五源码核对点。
> - **基准批判第 4 条（新增）**：LoCoMo **94%** 的问题只需 ≤2 个历史 session 即可作答，LongMemEval **85%**，主要基准平均约 **1 个 session**；LongMemEval 最多允许 2 次知识更新。即名义测「长期记忆」，实际多在测「单/双会话检索」，与 agent 真实长程任务（数十至数百会话、持续改写）错位——这解释了为何 recency 窗口与小上下文即可高分，是周五口径核对的第一优先假设。


> **雷达增量（2026-11-11，Memory 周 Day3：记忆产品转向「程序化沉淀」+ 基准批判第 5 条）**：
> - **A｜StreamMemBench（arXiv 2606.14571，streaming benchmark for future-oriented assistance）**：两步流式评测 + 四项指标（evidence recall / initial evidence use / feedback incorporation / follow-up reuse），对 8 个记忆系统 × 2 个 backbone 实测：**即使证据已被存储、反馈已在局部被吸收，系统仍普遍无法把观察到的证据用于后续决策、也无法把反馈转成可靠的后续行为**。→ 这是比「命题错位」更狠的一刀：LongMemEval 类基准测的是「能不能检索到答案」，StreamMemBench 测的是「检索到之后行为有没有改变」——记忆的最后一公里是**行为闭环**，不是 recall。列为**基准批判第 5 条**。
> - **A−｜Zep v4 Context API（10-14）+ Zep Agent Skills（11-05）**：v4 让 agent「沿着图的连接导航、并读回 Zep 是怎么构建这个图的」（可解释的图检索）；Agent Skills 把 **agent 运行轨迹蒸馏为「已验证程序」**，声称在业务任务基准上让更小更便宜的模型跑到接近 Opus 5.5 的水平。→ 与 Hy-Memory 的「代码记忆/为什么这样改」同向：2026 记忆赛道正从「存什么、怎么检索」转向「**把经验沉淀成可复用、可验证的技能**」（A4 程序性记忆 + D3 巩固的合流），这也是唯一能解释「小模型 + 记忆 ≈ 大模型」的机制假设。
> - **B｜MEMTIER（arXiv 2605.03675）**：分层记忆架构 + 检索瓶颈分析；LongMemEval-S 全 500 题、Qwen2.5-7B、**消费级 6GB GPU** 上 Acc 0.382 / F1 0.412，比全上下文基线（0.050）**+33pp**。→ 对 Tafcm「本地、不先引向量库」路线的直接反例参照：分层 + 检索预算可以在小显存上跑出可用精度，但绝对分数仍低（38%），别把「超基线」当「够用」。
> - **B｜OpenViking（Context Database for AI Agents，VLDB 2026 论文）**：以「上下文数据库」定位记忆层，自报在 LoCoMo 采样上让 Claude Code / Hermes / OpenClaw 达到 **80%+ 长期记忆准确率**、输入 token 降 **63%**。→ 已出现在 Hy-Memory 的对照名单里（此前只作为他方对比项，未单独入库），本周补记；自报口径，未独立复测。
> - **剔除**：`meko-mem0`（10-26，Mem0 92.5/94.4 数字的翻版包装，无新机制）；`mcp-memory-service` v10.9 / `-lite`（小工具迭代，B 级以下）；`me0`（自建 MCP 记忆服务，含 consent scopes / outputSchema，可作 E/F 层素材，暂不入库）。


> **雷达增量（2026-11-12，Memory 周 Day4：把记忆当基础设施来运维 + 记忆架构的元进化）**：
> - **A｜SIx Harness /《Memory as Infrastructure》（arXiv 2609.05510，2026-08，MIT）**：一份**月级真实运营记录**，不是基准论文。场景：单个 Claude Code 会话线连续 8 个月、驱动 **633,446 行**代码库（1,936 文件 + 448 份设计文档），记忆子系统自 7-02 起持续埋点。核心论点：**把记忆系统当基础设施，就要有可靠性工程**。
>   - **四类记忆失败**：① 知识丢失（compaction 把"为什么"摘要掉，agent 续得上流畅、续不上动机）；② 重复劳动（连续三个会话各自重新提议一个已建成且休眠的子系统，设计文档当时就在上下文里）；③ 上下文退化（为治①②而多注入 → 注入块只是偶尔相关 → 读者学会略过，通道一旦变成"学到的噪音"比没有更糟）；④ **静默记忆死亡**（索引/embedding 服务/hook 管道悄悄坏掉，所有人继续信任它）——作者说第④类重新定义了前三类。
>   - **系统五件**：本地 SQLite（FTS5/BM25 + sqlite-vec 混合检索，embedding 用本地 Ollama，**无云、无 API key**）；**anti-recurrence store**（记"已决定"和"试过并否决"，SessionEnd 抽取 → 待审队列 → 人工/agent 批量 triage，**154 决策/186 死路 → 仅 59/47 进正式库**，拒绝率本身是设计）；**precision-gated injection**（意图门 → IDF 罕见词重叠门 → 每会话阻尼 → 三类块：DO-NOT-REBUILD、过期声明警告、决策谱系；面向"读者注意力经济学"，默认静默）；**可靠性层**（会话开始 11 项健康检查打印 `MEMORY-HEALTH: 11/11 GREEN`、每 hook 心跳（不触发=缺席也变 RED）、告警疲劳预算：冷启动 embedding 不算故障、未接入的可选集成不报红）；**约定模板**（一行一条的记忆索引 + 每次 compaction 后先读的 resume anchor、不变量文件、append-only ledger、项目宪法）。
>   - **数字**：78,933 次 hook 调用；**85 次失败全部有记录、零静默**（84 次在前三周，之后 1 次，最后 20 天为 0）；10 天精度埋点**零误报**（分母完整）；3 起生产事故从读数追到结构性修复。作者自陈局限：N=1、无对照组、自报。
>   - **七个设计原则**（摘要口径）：记忆会从**两个相反方向**失败（重新发现已存在的东西 / 依据腐坏记录行动），因此需要**刻意对立的两套运维规则并保持张力**；宁可存储无聊、降级要诚实；写入要门控；注入要按读者注意力计费；健康检查要可行动；心跳要保证"没有一种枚举到的失败能不被记录"；可靠性要能被任何人用预注册消融协议复现。
>   - **与本周的关系**：① 独立佐证基准批判第 5 条「存储≠会用」——它把"retrieved-but-unused"作为真实工作流里的失败子模式点名（信息在上下文里、就是没被用）；② 给能力树补了一个此前完全没有的层：**记忆子系统的可观测性/可靠性**（健康门、心跳、降级可见、告警预算），对应"静默记忆死亡"；③ 存储选型与 Tafcm 一致（单项目、本地、不引图库、不上云），但用了 sqlite-vec —— Tafcm 若坚持纯文件/Markdown，需自己回答"向量腿缺失时检索质量如何诚实降级"。
> - **A−｜MemEvolve + EvolveLab（arXiv 2512.18746，OPPO AI Agent Team × LV-NUS，2025-12）**：把记忆架构本身作为可进化对象——**双层优化**：内层 agent 在固定记忆下积累经验，外层用任务表现做适应度**元进化记忆架构**。设计空间拆四模块 **Encode / Store / Retrieve / Manage**，并把 **12 个代表性记忆系统**（EXPEL、AWM、Dynamic Cheatsheet 等）统一重实现为 **EvolveLab** 代码库。成绩：SmolAgent / Flash-Searcher 最高 **+17.06%**；在 TaskCraft 上演化出的架构跨基准、跨 backbone 还能 +2.0~9.09%。→ 价值有二：一是"记忆架构没有全局最优、要按任务域自适应"这一判断有了实验支撑；二是 **EvolveLab 是周五验证日现成的横向对照台**（12 系统同一接口、同一基准），比自己拼 Mem0/Letta/Zep 三份 SDK 更可控。
> - **B（记日志不写卡）**：**OMEGA**（omegamax.co 白皮书，自报"#1 排名记忆系统"、solo dev）：结构化遗忘——会话摘要 TTL 1 天、checkpoint 7 天、**lessons/decisions 永久**；`mcp-memory-service` v11.0.0（6-13，breaking：移除 34 个 legacy 工具别名）；MemoryGraph v0.11.13（10-11，新增 Python SDK 供框架原生集成）；MemoryMesh v0.4.0（11-03，MCP SDK 从 1.0.4 跳到 1.25.2 + zod peer dep）——均属小工具/版本清理，不改变判断。
> - **剔除**：heropen 1.7.24（6-26 发布，非本周增量）；TencentDB Agent Memory（2026-05 开源，早于本卡时间窗，且与 Hy-Memory 同厂不同产品线，留作对照备查）；neo.mjs（非记忆系统）。

> **雷达增量（2026-11-13，Memory 周 Day5：验证日——Mem0 本地实跑 / Zep CE 事实修正 / EvolveLab 源码核对）**：
> - **A｜Mem0 OSS 本地端到端实测（`mem0ai 2.2.1`，2026-11-12 安装）**：venv + qdrant 本地路径（`path=/tmp/.../qd`）+ **假 LLM / 假 embedder**（不触云、无 API key 依赖），跑通 `add → get_all → search`：写入 2 条中文事实，`get_all(filters={"user_id":"u1"})` 返回 **2 条**，`search("Tafcm 记忆 存储方式", filters={"user_id":"u1"}, top_k=3)` 返回 2 条，top score **0.837**（默认 threshold 0.1）。→ 证明 **OSS 可在纯本地跑**，Tafcm 的"本地记忆"不必先上云；但必须自带 LLM+embedder，默认配置会直接构造 OpenAI client（无 key 即抛 `Missing credentials`）。
> - **A｜Mem0 v3 架构在 2.2.1 的代码级确认**：`mem0/memory/main.py` 的 sync/async add 均为 **单次 `ADDITIVE_EXTRACTION_PROMPT` 调用**（Phase 1 列既有记忆 → Phase 2 单次抽取 → Phase 3 批量 embed → Phase 4/5 逐条处理 + **md5 hash 去重** → Phase 6 批量落库 → Phase 7 **实体链接**），**不是**旧的两遍 extract→diff→ADD/UPDATE/DELETE；`Requires-Dist` 中 **无 neo4j/neptune/kuzu/AGE 任何图库**（图存储已彻底移除）；`expiration_date`（YYYY-MM-DD，过期默认隐藏，`show_expired` 可看）已进 OSS add 参数 → **D1 遗忘衰减**在 OSS 有最小实现；`timestamp` 明确标注 "Platform-only temporal parameter. Not supported in OSS"。
> - **A｜SDK 与文档的口径差新证据（可复现）**：`Memory.add()` docstring 写返回 `{"results":[{"id","memory","event":"ADD"}]}`，实测返回 **`{"results": []}`**，而紧接着 `get_all` 能读到 2 条——写入成功但返回体为空。→ 这是"平台口径 vs SDK 口径"批判的**第四类证据**：不只是分数拿不到，**连写入回执都不一致**；任何依赖 add 返回值做后续链路的实现都会踩坑。已记录为待向上游核对的观察项（未提 issue）。
> - **A｜EvolveLab 源码核对（`github.com/bingreeky/MemEvolve`，ICML'26）**：`Flash-Searcher-main/EvolveLab/` 下 **13 个 provider**（AgentKB / SkillWeaver / MobileE / ExpeL / Lightweight / CerebraFusion / Dilu / Generative / Voyager / Memp / DynamicCheatsheet / AgentWorkflow + **Evolver 自身**）→ 即论文口径的 **12 个基线系统 + 1 个进化体**；统一接口为 `BaseMemoryProvider.provide_memory(MemoryRequest)` / `.take_in_memory(TrajectoryData)`，`PROVIDER_MAPPING` 动态加载。→ 周五对照台可用，但**成本门槛高**：需 `requirements.txt` + `.env` API keys + GAIA / WebWalkerQA / xBench 数据集（本环境未跑，属"结构验证"非"行为验证"）。
> - **未执行**：Letta 三级记忆 API 实测（时间/依赖不足，留待下轮或降为文档级）；Zep 本地起服务（CE 已 deprecated，前提消失，改为读 Graphiti 路线）。
> - **含义**：① Mem0 的"简化路线"已有代码级证据（单遍 + 无图 + hash 去重 + 实体平行集合），与 Zep 的图路线正式分叉；② OSS 能本地跑但**回执不可信**，工程上必须以 `get_all`/向量库为准做写入确认；③ 记忆框架的"可复现验证"门槛不在模型，而在 **LLM/embedder/数据集三件套**——这解释了为什么全行业只能比厂商自报分数。

## 2. 与我的知识/项目关系
- **五维模型 Memory 维度** 缺实现层实证——本卡补上
- **GrowthOS**（个人经验管理）与 **TeamMind**（跨会话状态）直接可接
- **Validation 记忆验证章**：基准批判正是我的"验证编译器"该有的批判视角

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（各官方博客 + MemEval 基准 + 批判分析，标注厂商自报 vs 独立评测） |
| 来源 | Mem0/Zep/Letta 官方 ｜ https://github.com/ProsusAI/MemEval ｜ https://dreaming.press/posts/how-to-read-an-agent-memory-benchmark.html |
| 验证方式 | 用 MemEval 口径 + 自建小用例，对比 Mem0/Zep/Basic Memory 的"记忆持久化+检索"；注意区分厂商自报分与独立评测分 |

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察（待实现层实证）
- [ ] 拒绝
