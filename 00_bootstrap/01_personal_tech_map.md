# 01 · Personal Tech Map

> 数据来源：飞书知识库（7 个知识空间，约 400+ 节点）+ GitHub（14 公开仓库）+ 对话历史画像。
> 生成时间：2026-09-01（Bootstrap 第三阶段产物）。
> 用途：明确"我的边界"在哪，才能定义"边界之外"是什么。

---

## 1. Core Domains（已系统掌握）

按知识库沉淀密度与工程实证深度排序（★ 越多 = 越系统）：

| 领域 | 掌握内容 | 证据密度 | 代表性资产 |
|---|---|---|---|
| **AI Engineering · Agent Systems** | Agent 五维分析模型（本质/架构/Runtime/Memory/Tool/Orchestration/Evaluation）、Context Engineering、控制面演化 | ★★★★★ | 架构手册 8 篇 + 案例；EP 原则 27 条 |
| **Human-Agent Collaboration** | AI Programming 规范设计（CLAUDE.md/AGENTS.md/Rules/Hooks/Skills）、17 篇 Agent Workflow、Multi-Agent 编排、Prompt 工程 | ★★★★★ | Agent Workflow 实操方法论全集 |
| **Software Engineering（AI 放大）** | 架构 Review、AI 代码调试/测试/CI-CD/部署/CR/安全/性能审查 | ★★★★ | AI Code Review 资产族（AgenticCI/HOL/混合审查） |
| **AI Tools 生态** | Claude / Codex / Cursor / Hermes / OpenClaw 五大平台（设计哲学/权限边界/记忆/HOL/能力边界） | ★★★★★ | 工具档案 ×5 + 选型指南 |
| **ML 实验方法论** | 实验设计、可复现、数据集、标签噪声、Data-Centric AI、错误分析、训练配方、数据增强、集成、Backbone、论文写作 | ★★★★ | ML 实验科学 13 篇体系（Weather 项目实证） |
| **Validation · 系统可信度验证** | Claim→Operationalization→Evidence→Judgment→Done 验证编译器、行为/实验/Agent 系统/长期验证 | ★★★★ | Validation 独立知识空间（11 章） |
| **知识组织方法论** | 新领域接入 Protocol（Domain/Knowledge/Evidence/Practice）、工程资产六步法、原则 Registry、项目复盘 | ★★★★ | 知识库整理准则 + 商业领域首个验证 |
| **Thinking & Learning** | AI 时代工程师模型、置信度校准、可迁移能力、系统思维 | ★★★ | 判断力/学习方法体系 |
| **团队协作方式** | OKR / Design Doc / Code Review / Postmortem、微型→中大型团队、异步协作 | ★★★ | 团队协作空间 |

## 2. Active Research（正在研究）

| 研究主题 | 状态 | 验证点 |
|---|---|---|
| **Agent 工程原则验证实验** | 进行中（14 条已归档） | Knowledge Consistency(A)、Evolution(A−)、State/Context(B)、Interface/Composition(C) |
| **Validation 编译器落地** | 体系成型，逐模块验证中 | 运行时行为/记忆/上下文/状态机/长期漂移 |
| **AI Company OOS V2.1** | Level 4 已定义，Level 5 待实验 | Cloud/Local 双域、首个 Cloud→Local→Cloud 实验未启动 |
| **商业领域接入（新领域 Protocol 首个验证）** | Phase 0/1 进行中 | 概念卡/问题卡/原则/框架/证据/SOP 六层 |
| **Migration & Validation** | Claude→Codex 迁移已产出 | 共性原则 vs 工具特异性差异 |
| **Tactics 素材归并** | Raw 47 条 → Processed 归并中 | 技法/战术/模式/剧本四层 |

## 3. Active Projects（活跃项目，详见 03_project_landscape.md）

- **Tafcm**（Dart）—— 移动端 Typora 级 Markdown/公式写作工具，Phase 3.12，最活跃
- **silver-shield**（Python）—— 老年人诈骗风险数字孪生与协同预警（MVP RC + v2 设计）
- **TeamMind**（Java）—— 项目级多 Agent 团队运行时
- **weather-recognition**（ML）—— 证据追踪式天气分类实证研究（已完成）
- **agent-attention**（TS）—— Agent 通知基础设施
- **GrowthOS**（TS）—— 个人经验管理系统
- 内库 Hub：FormulaFix / dsh / dsh-pentest（骨架，待填充）

## 4. Adjacent Domains（相邻但基本未覆盖）

> 这些领域与我的核心（Agent 工程 / AI 安全）只隔一层，是最可能的"知识边界之外"入口。

| 相邻领域 | 与核心的连接点 | 当前覆盖 |
|---|---|---|
| **AI Security / Red Teaming / Adversarial ML** | 我的 GitHub 定位"AI安全、网络攻防"，但 KB 仅 OWASP+生成代码审查 | ❌ 近乎空白（最大缺口） |
| **MCP / Agent 协议生态** | 我有完整 Tool System 知识，但未接 MCP 标准 | ⚠️ 未系统化 |
| **Agent Evaluation / Evals** | 五维模型有 Evaluation 维度，缺主流框架实证 | ⚠️ 部分 |
| **Agent Memory 实现前沿**（Mem0/Letta/Zep/A-MEM） | 五维模型有 Memory 维度，缺实现层对比 | ⚠️ 部分 |
| **LLM 可观测性 / 追踪** | KB 有单篇"LLM 应用追踪"，缺体系 | ⚠️ 部分 |
| **本地 / 边缘 AI** | Tafcm 离线优先、silver-shield 边缘感知都依赖它 | ❌ 空白 |
| **LLM Fine-tuning / 对齐** | ML 方法论有训练配方，但未到 LLM 层 | ❌ 空白 |
| **RAG 系统化**（GraphRAG/Agentic RAG） | KB 只有"混合检索避免盲区" | ⚠️ 弱 |
| **AI 原生产品 / Agentic UX** | TeamMind/campus_order 需要产品化视角 | ❌ 空白 |
| **去中心化 AI / 联邦学习** | 对话历史关注过，知识库未接入 | ❌ 空白 |
| **Robotics × LLM / 具身智能** | multi_arm_line_ws 项目孤悬，无知识支撑 | ❌ 空白 |

## 5. Knowledge Gaps（知识缺口，详见 02_knowledge_gap_map.md）

五大类缺口：**声明未覆盖**（AI 安全/攻防）、**已启动未深化**（商业/可观测性/RAG）、**项目需要而 KB 无**（MCP/Evals/边缘 AI/移动工程）、**兴趣未接入**（去中心化 AI/机器人）、**方法论可外推**（形式化验证/组织科学×AI）。

## 6. Potential Expansion Directions（详见 04_top20_expansion.md）

Top 3：**MCP 生态**、**AI Red Teaming / Agent 安全**、**Agent Evaluation 框架**——都与现有项目直接相连、与知识体系强相关、活跃且可验证。

---

## 一句话总结

> 我在"**怎么让 AI Agent 高效、可信、可控地干活**"这个主线上已经相当深（工程方法论 + 验证体系 + 组织 OS 三层），
> 但我的 GitHub 定位所承诺的"**AI 安全与攻防**"目前是知识体系的**最大空白**——这是最值得优先扩展的方向。
