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
