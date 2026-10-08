# KnowlegeMap · 个人技术世界的边界模型

> **定位**：这不是我的知识库，而是我的"知识边界探测器"。
> 飞书知识库（辰星 · Personal Engineering OS）回答"**我已经知道什么**"；
> 本仓库回答"**我的边界之外正在发生什么、哪些值得进入**"——作为未来 3 个月的 **External Knowledge Expansion Layer**。

---

## 仓库角色（与内库的分工）

| 层 | 载体 | 职责 |
|---|---|---|
| 内库（系统掌握） | 飞书 · 辰星 Personal Engineering OS | 系统化知识、工程资产、原则、项目复盘 |
| **本仓库（边界探索）** | **KnowlegeMap** | 发现 → 筛选 → 验证 → 连接，不重复沉淀已知 |
| 中间层（待验证） | 飞书 · Validation / Tactics | 把本仓库验证过的对象转成可复现的结论 |

**核心原则**：不重复收集已系统掌握的领域；只找"相邻但未覆盖"的高价值对象；宁缺毋滥；一切候选以一手证据（官方文档 / 源码 / 论文 / Release）为准。

---

## 目录导航

```
KnowlegeMap/
├── 00_bootstrap/              ← 首次 Bootstrap 基础资产（本次已生成）
│   ├── 00_bootstrap_overview.md           Bootstrap 总结
│   ├── 01_personal_tech_map.md            Personal Tech Map
│   ├── 02_knowledge_gap_map.md            Knowledge Gap Map
│   ├── 03_project_landscape.md            Project Landscape
│   ├── 04_top20_expansion.md              Top 20 Expansion Directions（评分矩阵）
│   └── 05_auto_exploration_strategy.md    未来自动探索策略
├── 01_known_territory/        ← 已知领域边界索引（标记覆盖深度，禁止重复收集）
├── 02_active_research/        ← 正在研究的主题（含"关注但未系统化"的）
├── 03_expansion_queue/        ← 探索队列（inbox → candidates → validated）
├── 04_connections/            ← 外部技术 ↔ 现有项目/知识的连接地图
├── 05_scan_logs/              ← 探索扫描日志（时间线）
├── 08_agent_centric/          ← Agent-Centric 资产层（Mode B：能力/工具/技能/Agent/任务/工作流/评估/记忆）
├── 09_agent_engine/           ← Agent-Centric 引擎（可运行最小闭环，纯 Python 标准库）
└── 99_templates/              ← 候选卡 / 扫描日志 / Agent 系列模板
```

完整索引见 [_INDEX.md](_INDEX.md)。

---

## 双扩展模式（2026-10-08 架构升级）

本仓库同时支持两个主体的一等公民：

| | Mode A：Human-Centric Cognitive Expansion | Mode B：Agent-Centric Task Expansion |
|---|---|---|
| 一等公民 | **Human**（00-07 资产层，保持原样） | **Agent**（08 资产层 + 09 引擎） |
| 输入 | 我目前知道什么 / 我的认知缺口 | **我要完成什么任务** |
| 输出 | 学习/知识扩展建议 | Required Capabilities + Tools + Composition + Workflow + Evaluation + Memory |
| 驱动 | 认知缺口 → 知识发现 | **任务 → 能力需求 → 能力缺口 → 工具/项目发现 → 组合 → 执行 → 评估 → 能力演化** |
| 共享 | 证据纪律（FACT 优先）、Discovery/Evaluation/Memory 思想、开源知识 | 同左 |

- Human 层：`00_bootstrap → 06_expansion_index`（既有流程未改）。
- Agent 层：`09_agent_engine/`（`python3 -m unittest discover -s tests`，14 用例）→ 资产落 `08_agent_centric/`。
- 原则：**"需要什么"先于"推荐什么"**；Tool Composition 必须解释组合理由；Star 仅弱信号；Agent-Centric ≠ 无限自治（高风险任务强制 approval，EP-002）。

---

## 当前状态（Bootstrap 完成 · 2026-09-01 · Mode B 升级 2026-10-08）

- ✅ 第一阶段：飞书知识库分析完成（7 个知识空间，约 400+ 文档节点）
- ✅ 第二阶段：GitHub 分析完成（14 个公开仓库 + 内库项目 Hub）
- ✅ 第三阶段：Personal Tech Map 建立
- ✅ 第四阶段：Top 20 Expansion Directions（六维评分）
- ✅ 第五阶段：本仓库目录与索引初始化
- ✅ Mode B：双扩展模式架构 + Agent Domain Model + 可运行引擎（Scenario A-F 端到端测试全通过）
- ⏭ 下一步：按 `00_bootstrap/05_auto_exploration_strategy.md` 持续扫描；按需用 `09_agent_engine/cli.py` 驱动任务级能力发现

---

## 快速入口

- [Personal Tech Map](00_bootstrap/01_personal_tech_map.md) —— 我的知识世界长什么样
- [Knowledge Gap Map](00_bootstrap/02_knowledge_gap_map.md) —— 我的盲区在哪
- [Project Landscape](00_bootstrap/03_project_landscape.md) —— 我在做什么项目
- [Top 20 Expansion Directions](00_bootstrap/04_top20_expansion.md) —— 接下来该探索什么
- [探索策略](00_bootstrap/05_auto_exploration_strategy.md) —— 怎么持续探索
- [Agent-Centric 资产层](08_agent_centric/README.md) —— Agent 侧能力/工具/工作流资产
- [Agent-Centric 引擎](09_agent_engine/README.md) —— 最小闭环运行方式与测试

---

*License: MIT*
