# 候选证据卡 · [cand] Agentic GraphRAG / 记忆增强图检索（MemGraphRAG / Graph-R1 / A-RAG）
> 状态：`[cand]` ｜ 分类：RAG 系统化（G2）/ Context Engineering 相邻 ｜ 发现：2026-09-05（雷达 #4） ｜ 等级：**A**
## 一句话定位
2026 年 RAG 从"静态检索"走向"agent 主动遍历"的收敛点：MemGraphRAG（KDD'26，记忆增强多 Agent 图构建）、Graph-R1（首个端到端 RL 的 agentic GraphRAG）、A-RAG（分层检索接口）——把"图结构 + agent 决策 + 记忆"三件事合流，直接命中我的 **RAG 系统化缺口（G2，KB 仅 1 篇）**。
## 1. 它是什么 / 解决什么问题
- 痛点：传统 GraphRAG 构建成本高、一次性固定检索、依赖长上下文推理与 prompt 设计；向量检索无法自动完成多跳关系推理（如"CEO 母校的知名校友"需三步推理）["https://blog.csdn.net/weixin_48053866/article/details/164149407"]
- **MemGraphRAG**（XMUDeepLIT，KDD'26）：三层记忆（unstructured passages / extracted facts / abstract schemas）+ 分层索引图 + 多 Agent 组协同构建，记忆感知的分层检索，多个基准超越 SOTA["https://github.com/xmudeeplit/memgraphrag"]["https://arxiv.org/html/2606.00610v1"]
- **Graph-R1**：轻量知识超图构建 + 检索建模为多轮 agent-环境交互 + 端到端 RL 奖励优化；Qwen2.5-7B 上 F1 57.82（StandardRAG 32.05 / Search-R1 46.19）["https://openreview.net/forum?id=YXnFGsSkCC"]["https://www.alphaxiv.org/overview/2507.21892"]
- **A-RAG**：分层检索接口（keyword/sentence/chunk 三级），优于 Graph-RAG 与 Workflow RAG，高效 test-time scaling["https://www.arxiv.org/pdf/2602.03442"]
- 溯源向：Agentic GraphRAG 的 traversal context + provenance（cited entities/relationships/text units 检查）["https://arxiv.org/html/2605.15109v1"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-05）**：MemGraphRAG GitHub（MIT，KDD'26 接收）✅ + arXiv 2606.00610 ✅；Graph-R1 OpenReview（2026-05）✅ + arXiv 2507.21892 ✅
- 2026-08 期刊已见 GraphRAG 医学实证（用药安全验证优于常规 RAG：0.545 vs 0.443）["https://www.frontiersin.org/journals/medicine/articles/10.3389/fmed.2026.1898857/full"]
- 企业实证：半导体厂商 4000 万内部文档 GraphRAG 部署，实体幻觉 8.7%→1.2%（第三方报告，需谨慎）["https://ragaboutit.com/5-enterprise-graphrag-wins-that-slash-hallucination-by-62/"]
## 3. 与我的连接
- **连接的项目**：**GrowthOS（个人经验管理）**——三层记忆结构与经验组织直接同构；**TeamMind**——多 Agent 图构建的编排思路；**silver-shield**——知识库检索升级；**AI Company OOS**——知识图谱式组织记忆
- **连接的知识点**：RAG 系统化缺口（G2）、Context Engineering（上下文编排）、Agent Memory（S4，记忆×检索融合）、五维模型 Tool/Memory 维度
- **潜在收益**：补 RAG 缺口的最短路径；MemGraphRAG 的"记忆层 + 多 Agent 构建"可直接映射到 GrowthOS 的知识组织；Graph-R1 的"检索即 agent 交互"思路与我的 Context Engineering 哲学一致
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/xmudeeplit/memgraphrag ｜ https://arxiv.org/html/2606.00610v1 ｜ https://openreview.net/forum?id=YXnFGsSkCC ｜ https://www.arxiv.org/pdf/2602.03442（A-RAG） |
| 证据等级 | **FACT（GitHub 仓库 + arXiv/OpenReview 全文核验通过）** |
| 验证方式 | 读 MemGraphRAG 源码 → 在小语料上跑三层记忆 + 多 Agent 构建 → 对比普通 RAG 的多跳问答 → 评估 GrowthOS 接入 |
| 预期完成时间 | 2026-09/10 |
> **雷达增量（2026-09-17，agent 化 RAG 管线 + 运行时图修复）**：
> - **Agent-Enhanced Heterogeneous Graph RAG（arXiv 2609.00761，2026-09-01 + ACM DL）**：把 RAG 三阶段显式 agent 化——**query-aware 检索 agent**（分析查询类型选图遍历策略）+ **sufficiency-aware 重排 agent**（评估证据完整性、自适应扩展子图）+ **graph-grounded 验证 agent**（输出前校验实体/关系/属性正确性）——"验证 agent"范式与我的 Validation 编译器（Evidence→Judgment）同构["https://arxiv.org/abs/2609.00761"]
> - **Cognition on Graph（第 4 代 Agentic RAG，09-16 报道）**：**Runtime Graph Repair**（运行时实时修复缺失连接）+ 文本语义×图拓扑双向协同；规模化到 **50 亿词/14 亿图边**——从静态检索走向动态认知推理["https://latestllm.com/articles/beyond-graphrag-exploring-runtime-graph-repair-and-agentic-rag-mu3whkxj"]
> - **Neo4j NODES AI 2026（09-04）**：Agentic GraphRAG 产业化——多 agent 自动推断 schema、构建 KG、按查询结构与风险信号在向量/图检索间自适应路由（无手工 schema）["https://neo4j.com/videos/nodes-ai-2026-agentic-graphrag-autonomous-knowledge-graph-construction-and-adaptive-retrieval-2/"]
> - **含义**：① "RAG 管线每一步都可 agent 化 + 验证 agent 兜底"成为新共识——silver-shield 知识库检索可直接采用"检索→重排→验证"三段 agent 化设计；② **运行时图修复**解决"图构建不完整则检索失败"的静态缺陷——对 GrowthOS 大规模经验库有价值；③ Neo4j 下场说明该范式已过研究验证、进入企业路线图
> **雷达增量（2026-09-23，无锚实体 + 文档结构化 + 检索产品化）**：
> - **AnchorRAG（arXiv 2509.01238，多 agent 协作 KG RAG）**：**无需预定义 anchor 实体**——predictor agent 提取关键词+语义匹配候选实体 → 多 retriever agent 并行图遍历——解决"开放世界查询"下 anchor 缺失问题["https://arxiv.org/html/2509.01238"]
> - **DocNavRAG（arXiv 2608.01565，09-16 更新）**：**文档结构化图 RAG + 状态化证据构建**——多粒度层级图（保留原始段落为证据单元）+ 文档内外主题水平链接 + agentic 检索控制器自适应导航，training-free["https://arxiv.org/html/2608.01565v1"]
> - **Azure AI Search Agentic Retrieval（09-18）**：**LLM query planning（preview）**多查询管线——复杂问题拆子查询、跨专有/外部内容覆盖，服务 agent-to-agent 工作流——**检索产品化到微软官方**["https://learn.microsoft.com/en-gb/azure/search/agentic-retrieval-overview"]
> - **AWS Unified KG RAG（09-14，Apache-2.0）**：**GraphRAG + LightRAG 同栈**开源部署（统一知识图谱 RAG 栈）["https://aws.amazon.com/blogs/opensource/unified-knowledge-graph-rag-on-aws-graphrag-and-lightrag-on-one-stack/"]
> - **含义**：① Agentic GraphRAG 三线并进——**无 anchor 泛化**（AnchorRAG）、**文档结构保持**（DocNavRAG，贴近企业文档场景）、**云厂商检索产品化**（Azure/AWS）——范式全面进入工程可用期；② "验证 agent"仍是共同骨架（对照 Validation 编译器）；③ silver-shield/GrowthOS 的 RAG 选型可对照 Azure 的"query planning 拆子查询"作为多跳检索参考实现
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
