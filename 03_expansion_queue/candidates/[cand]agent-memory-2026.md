# 候选证据卡 · [cand] Agent Memory 2026 实现层全景 + 基准批判

> 状态：`[cand]` ｜ 分类：Agent Memory 实现前沿（S4） ｜ 发现：2026-09-01 ｜ 等级：**S**

## 一句话定位
Agent 记忆实现层 2026 已分层成熟（Mem0 抽取式 / Zep 时序知识图谱 / Letta 自编辑记忆 / A-MEM Zettelkasten），且有 MemEval 等独立基准开始给系统排名；同时出现对记忆基准本身可靠性的批判——这正需要我的"证据纪律"来甄别。

## 1. 它是什么 / 解决什么问题
| 框架 | 记忆模型 | 2026 关键动态 |
|---|---|---|
| **Mem0** | 抽取+检索，向量优先 | 2026-04 新算法（单遍分层抽取+多信号检索）：LoCoMo 92.5 / LongMemEval 94.4 / BEAM(1M) 64.1["https://mem0.ai/blog/state-of-ai-agent-memory-2026?ref=swarmsignal.net"] |
| **Zep (Graphiti)** | 时序知识图谱，双时间事实+溯源，框架无关，数据层治理（ABAC/保留/审计） | 面向企业生产；自称 LoCoMo 领先、检索 p50 87ms["https://www.getzep.com/mem0-alternative/"] |
| **Letta** | 自编辑记忆（MemGPT 系），Core/Recall/Archival 三级 | 2026-03 转向"memory-first agent harness"，押注 computer use["https://www.letta.com/blog/our-next-phase"] |
| **A-MEM** | Zettelkasten 动态组织+链接（NeurIPS 2025） | ~1K stars，研究向["https://github.com/Anandesh-Sharma/awesome-agentic-memory"] |
| **MemEval** | 独立评测套件（ProsusAI，2026-08） | 排名：Memory-R1 0.389 / SimpleMem 0.358 / Mem0 0.344 / MemU 0.299 F1["https://github.com/ProsusAI/MemEval"] |

**基准与批判**：三主流基准 LoCoMo（趋于饱和 ~92）/ LongMemEval（ICLR25，更难）/ BEAM（1M/10M token）。**两条关键批判**：① 长上下文模型直接碾压记忆管线（LoCoMo +35.2pp、LongMemEval +33.4pp）——压缩是 lossy 的["https://dreaming.press/posts/how-to-read-an-agent-memory-benchmark.html"]；② LoCoMo 被审计出 1540 题中 99 处得分污染错误（6.4%）["https://essays.bloo-mind.ai/posts/2026-05-20-mem-eval/"]

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
