# 09_agent_engine · Agent-Centric Engine（可运行最小闭环）

> **定位**：KnowlegeMap 的 Mode B 执行引擎——纯 Python 标准库，无第三方依赖。
> 实现链路：**Task → Capability Extraction → Gap Analysis → Tool/Project Discovery
> → Tool Composition（带理由）→ Workflow → Evaluation → Agent Operational Memory → Capability Evolution**。
> 原则：Agent 是一等公民；"需要什么"先于"推荐什么"；Star 仅弱信号；高风险任务强制 approval 前置（EP-002）。

## 运行

```bash
cd 09_agent_engine

# 端到端测试（Scenario A-F，14 用例）
python3 -m unittest discover -s tests

# CLI 最小闭环（安全测试演示：能力分解→组合→工作流→评估→记忆→资产落盘）
python3 cli.py demo --agent pen-test-agent

# 指定任务
python3 cli.py run --task-type e2e-web-testing \
    --objective "对官网跑端到端回归" --task-id t-001 --write-assets
```

## 模块

| 模块 | 职责 |
|---|---|
| `engine/domain.py` | 一等实体：Agent / Capability / Tool / Skill / Workflow / Task / Evidence / Evaluation / SelectionReason / AgentMemory（12 维选择理由；相似任务按能力画像检索） |
| `engine/knowledge.py` | 种子知识库：26 能力 / 6 任务类型分解规则 / 28 工具，全部带证据锚点（38 候选卡 + star 基准） |
| `engine/discovery.py` | Task 分解 / Gap 分析（含前置传递闭包）/ 能力驱动工具发现 / 未知能力发现 |
| `engine/composition.py` | 候选多维评分 → 互斥组裁决 → 数据流兼容检查 → 有向工具链 + 组合理由 |
| `engine/workflow.py` | 阶段化工作流（checkpoint / failure_recovery / 角色 / 依赖序） |
| `engine/evaluation.py` | criterion 打分 + 能力 confidence 回写（成功 +0.2 / 失败 -0.1 记弱点） |
| `engine/memory.py` | Agent Operational Memory（JSON 持久化；post-task learning；相似任务→历史工作流复用；v1→v2 演进理由） |
| `engine/pipeline.py` | 最小闭环主流程 + 安全边界（approval）+ "删掉 Tool X 损失什么能力"查询 |
| `engine/store.py` | 产物 → 08_agent_centric/ 的 Markdown 资产（tasks/workflows/capabilities/agents） |

## 设计要点（对照升级要求）

1. **双扩展模式**：Mode A（Human-Centric，00-07 资产）未被触碰；Mode B 新增 08/09。
2. **Agent 一等公民**：显式建模 identity/role/objective/tools/skills/memory/environment/constraints/autonomy/capabilities/weaknesses/task_history/evaluations。
3. **任务驱动发现**：先分解能力，再发现工具/项目；`decompose_task` → `gap_analysis` → `discover_for_capability`。
4. **Tool Composition ≠ Tool List**：ComposedChain 是有向链；互斥组（5 组）、数据流兼容表、并行组、排除理由。
5. **选择理由机制**：每个工具带 12 维 SelectionReason；Star 只在 ecosystem_maturity（权重 0.10）。
6. **未知能力发现**：objective 关键词 → 能力域（26 能力关键词表），先发现"不知道需要什么"。
7. **反馈闭环**：evaluation → capability confidence / tool_stats / success&failure patterns / workflow 版本演进。
8. **安全边界**：risk=high/critical → approval_required=True；工具 security_implications 参与评分；沙箱/授权要求显式化。
9. **证据纪律**：所有能力/工具锚点指向 03_expansion_queue/candidates 与 00_bootstrap/00_starred_reference.md（FACT 优先）。

## 测试场景（Scenario A-F）

| 场景 | 输入 | 输出 |
|---|---|---|
| A Human 认知扩展不破坏 | Human 资产 | 00-07 资产完整可读、模板兼容 |
| B Agent Task Expansion | Task + Agent Profile | Required Capabilities + Tools + Workflow + Evaluation |
| C Capability Gap | Task + 已有能力 | 缺失能力（含前置展开） |
| D Tool Composition | 多候选工具 | 组合方案 + 组合理由 + 互斥裁决 |
| E Post-task Learning | 任务结果 + Evaluation | 能力/记忆更新（成功/失败双向） |
| F Repeated Similar Task | 相似新任务 | 复用历史 Workflow v2 + 演进理由 |

## 运行结果示例（demo）

- 安全测试任务 → 8 项能力需求 → 缺口 8 项 → 工具链 `garak → playwright → promptfoo`（组合理由 + 排除 browser-use + 2 处数据流缺口记录）→ 8 阶段工作流 → Evaluation score=0.887 → 记忆落盘 `08_agent_centric/memory/agent_pen-test-agent.json`。
