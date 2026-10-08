# 00 · Architecture Gap Report（KnowlegeMap 双扩展模式升级）

> 日期：2026-10-08 ｜ 前置分析（实现前必读）｜ 关联：[README](../README.md) / [07_radar_watch](../07_radar_watch/README.md)

## 0. 扫描结论：现有系统是什么

KnowlegeMap 不是传统软件系统，而是**纯 Markdown 资产系统**：无代码执行层，无数据库，无 API。"系统"由三层构成：

| 层 | 载体 | 职责 |
|---|---|---|
| 资产层 | `00_bootstrap/` ~ `06_expansion_index/` | 知识地图 / 候选卡 / 连接 / 索引 / 日志 |
| 流程层 | `07_radar_watch/README.md`（七步契约） | 由 LLM 按契约执行的运行规范 |
| 模板层 | `99_templates/`（候选卡/日志） | 数据结构约定 |

现有数据流（Human-Centric Cognitive Expansion）：

```
Input(Human 知识状态/项目画像)
 → Analysis(Bootstrap 六维结论 + 去重基准)
 → Discovery(general_search 定向扫描)
 → Retrieval(web_fetch 一手来源精读)
 → Recommendation(S/A/B/C 分级候选卡)
 → Reasoning("为什么值得进入视野" + 与项目连接)
 → Output(候选卡 + 扫描日志)
 → Persistence(03_expansion_queue / 04_connections / 05_scan_logs / 06_expansion_index)
```

## 1. 现有系统为什么天然偏向 Human？

1. **输入假设是"我"**：所有入口都问"我的边界/我的盲区/我该学什么"（`01_personal_tech_map`、`02_knowledge_gap_map` 全是 Human 认知状态）。
2. **推荐对象是"知识对象"**：候选卡回答"这个外部对象为什么值得进入**我的**视野"。
3. **价值度量是"学习"**：状态机 `[cand] → [validated] → [dropped]` 是**学习侧的验证状态**（是否 ≥2 条独立证据 + 真机验证），不是执行侧的成败。
4. **持久化主体是 Human 认知索引**：`06_expansion_index` 的字段是"首次发现/来源/与我的项目关系/是否已深入研究/是否已实际验证"——全部以 Human 为坐标。
5. **反馈回路是知识更新**：雷达增量追的是"对象的新进展"，不是"Agent 能力的新统计"。

**一句话**：`Input / Output / State / Value` 四个主环节都锚定 Human，Agent 从未被建模。

## 2. 哪些模型/接口绑定了 Human-Centric 逻辑？

| 绑定点 | 位置 | 绑定内容 |
|---|---|---|
| 候选卡模板 | `99_templates/candidate_card.md` | "与我的连接"、"我的项目"、"我的盲区"字段 |
| 索引 schema | `06_expansion_index/README.md` | "与我的项目关系 / 是否已深入"（Human 学习坐标） |
| 连接模型 | `04_connections/README.md` | 外部对象 ↔ 项目（Human 资产坐标） |
| 流程契约 | `07_radar_watch/README.md` | "Personal Tech Radar"、五档结论向 Human 汇报 |
| 状态机 | `[cand]/[val]/[drop]/[observe]` | 学习验证状态 |

**结论**：这些模板/索引**不应删除**（Mode A 必须保留），但 Mode B 需要自己的模板与索引，不能复用 Human 坐标的 schema。

## 3. Task 在当前系统里是什么？

- **不存在实体**。最接近的是：雷达轮次的"聚焦主题"（作为搜索 query 的来源）、`02_active_research` 的研究主题（Human 研究线）。
- 没有 `task_type / objective / constraints / environment / desired_output / risk_level / evaluation_criteria` 任何结构化字段。
- **缺口**：Task 必须成为 Mode B 的**一级驱动实体**。

## 4. Agent 在当前系统里是什么？

- **不存在实体**。出现过的"agent"含义有三：
  1. 雷达自己（执行者，未建模）；
  2. 用户的项目（Tafcm/TeamMind 等，是"被连接的项目"而非"被建模主体"）；
  3. 外部研究对象（agentic-attack 等卡的主题）。
- **没有** identity/role/capabilities/available_tools/memory/constraints/autonomy_level/task_history/evaluations 任何字段。
- **缺口**：Agent 必须成为一等公民，显式建模。

## 5. Tool / Skill / Capability 是否已经存在？

**部分隐式存在，全部无显式模型**：

- Tool：候选卡主题（browser-harness、e2b-sandbox、promptfoo…）——有"证据来源/验证状态"，**无** interface/input-output/权限/成本/可靠性/安全影响等结构化属性。
- Skill：只有外部研究对象（Agentic Skills Top 10）——**无** 本系统侧的 skill 注册（trigger/procedure/required_tools/success_rate/usage_count）。
- Capability：**完全不存在**。"发现"直接落在项目/知识点层面，没有中间层。
- **缺口**：Capability 是 Mode B 的**发现单位**；Tool/Skill 是 Capability 的实现载体。三者都必须显式化。

## 6. Discovery 当前到底在发现"知识"还是"能力"？

**发现的是知识对象（项目/范式/协议）**。证据：
- 搜索 query 是领域关键词（"agent memory"、"MCP"），不是"为了完成 X 任务需要什么"；
- 产出是候选卡（对象级），不是"能力需求 → 能力缺口 → 工具组合"；
- 连接是"对象 ↔ 我的项目"，不是"能力 ↔ 工具 ↔ 工作流"。
- **缺口**：Mode B 需要**能力驱动的发现**——先发现"需要什么能力"（含未知能力），再发现实现该能力的工具/项目。

## 7. 当前是否有 Evaluation / Evidence / Feedback Loop？

| 机制 | 现状 | 缺口 |
|---|---|---|
| Evidence | ✅ 候选卡有 FACT/DESIGN 分级 + 一手来源 URL | 无 execution-time evidence（任务执行产生的观察） |
| Evaluation | ⚠️ 只有学习侧验证状态（[val] 需 ≥2 证据） | 无任务侧 Evaluation（criterion/score/failure/regression） |
| Feedback Loop | ⚠️ 只有知识增量反馈（雷达增量） | 无"任务成败反向塑造 Agent 能力模型"的回路 |
| Memory | ⚠️ 只有 Human 认知索引（06） | 无 Agent Operational Memory（什么工具有效/什么失败模式高频） |

## 8. 哪些设计可以复用？

1. **候选卡的证据纪律**（FACT/DESIGN + 一手来源 + 验证计划）→ 直接复用于 Tool/Capability/Workflow 卡。
2. **04_connections 的连接思想**（对象 ↔ 项目）→ 扩展为 Task ↔ Capability ↔ Tool ↔ Skill ↔ Workflow ↔ Evaluation 的连接。
3. **06_expansion_index 的生命周期/去重思想** → 复用于 Agent Operational Index（工具统计、工作流版本）。
4. **05_scan_logs 的时间线日志** → 复用于任务执行日志。
5. **00_starred_reference（35 star 基准）与 38 张候选卡** → 作为种子知识库的**真实证据来源**（Capability→Tool 映射不凭空造，从卡提取）。
6. **07_radar_watch 的"宁缺毋滥 + 证据分级"原则** → 作为 Mode B 发现层的价值阈值纪律。

## 9. 哪些设计必须重构/新建？

| 项 | 动作 | 原因 |
|---|---|---|
| Agent Domain Model | 新建 | 不存在 |
| Capability / Tool / Skill / Workflow / Task / Evidence / Evaluation 模型 | 新建 | 不存在 |
| Task→Capability 分解层 | 新建 | 现无"任务驱动"入口 |
| Capability Gap 分析 | 新建 | 无"已有能力 vs 需求能力"对照 |
| Tool Composition（组合理由/数据流/互斥/前置） | 新建 | 现只有对象级推荐，无组合级推理 |
| Agent Operational Memory | 新建 | 与 Human Memory（06）完全区分 |
| 任务经验沉淀（相似任务→历史工作流） | 新建 | 无 Task-Learning 回路 |
| 可运行引擎 | 新建 | 现有系统无代码执行层 |
| 链路可视化/可查询 | 新建 | 数据模型须为图状/显式关系 |

## 10. 双模式架构（决策）

```
KnowlegeMap/
├── 00_bootstrap ~ 07_radar_watch    ← Mode A（Human-Centric）资产，原样保留
├── 08_agent_centric/                ← NEW：Mode B（Agent-Centric）资产层
│   ├── capabilities/ tools/ skills/ agents/ tasks/ workflows/ evaluations/ memory/
│   └── docs/                        ← 领域模型文档 + 本报告
├── 09_agent_engine/                 ← NEW：可运行引擎（Python 标准库）
│   ├── engine/（domain/store/knowledge/discovery/composition/workflow/evaluation/memory/pipeline）
│   ├── cli.py  tests/               ← 端到端测试（Scenario A-F）
├── 99_templates/                    ← + agent 模板（task/capability/tool/workflow/agent/evaluation）
├── _INDEX.md  README.md             ← 更新为双模式入口
```

**关键原则落地**：
- Human 是 Mode A 一等公民（不动现有逻辑）；Agent 是 Mode B 一等公民（显式建模，非黑盒）。
- 共享层：Evidence 纪律 / 连接思想 / 去重机制 / 种子知识库（38 卡 + 35 star）。
- 隔离层：状态机（学习验证 vs 执行成败）、索引坐标（Human 认知 vs Agent 操作）、Memory（Human Memory vs Agent Operational Memory）。
- 安全：Agent-Centric ≠ 无限自治——Tool 选择显式考虑 risk/permission/approval/execution-environment（EP-002 原则在 Mode B 落地）。
