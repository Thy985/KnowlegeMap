# 08_agent_centric · Agent-Centric 资产层（Mode B）

> **定位**：与 00-07 的 Human-Centric 资产平行的第二主体资产层。
> Human 是一等公民（00-07）；**Agent 也是一等公民（本层）**。
> 本层只存放"为完成任务而发现的能力/工具/工作流"资产，不重复 03 的知识候选。

## 目录

| 子目录 | 内容 | 写入方 |
|---|---|---|
| [capabilities/](capabilities/README.md) | 能力注册表（能力=发现单位，含前置依赖/工具候选/证据） | `cli.py` 导出 + 手工 |
| [tools/](tools/README.md) | 工具卡（多维 Selection Reason + 证据锚点） | 手工 / 雷达发现 |
| [skills/](skills/README.md) | 技能卡（procedure / trigger / 成功率的可演进资产） | 手工 |
| [agents/](agents/README.md) | Agent 档案（能力/弱点/自主度/任务史） | `cli.py` 导出 |
| [tasks/](tasks/README.md) | Agent Task 卡（Task→Capability→Tool→Workflow→Eval 全链路） | `cli.py` 导出 |
| [workflows/](workflows/README.md) | 工作流卡（版本化 + 演进理由 v1→v2） | `cli.py` 导出 |
| [evaluations/](evaluations/README.md) | 评估卡（criterion/score/failure/regression） | 引擎回写 |
| [memory/](memory/README.md) | Agent Operational Memory（JSON：tool_stats/workflow_versions/task_log/失败模式） | `MemoryStore` 写入 |
| [docs/](docs/README.md) | 架构文档（Gap Report / Domain Model） | 本次升级 |

## 数据流（最小闭环）

```
Task → Capability 分解 → Gap 分析 → 工具/项目发现 → Tool Composition（带理由）
     → Workflow（阶段/依赖/检查点/恢复）→ Evaluation → Agent Operational Memory
     → Capability Evolution（成功/失败反向塑造）
```

## 与 00-07（Human 层）的关系
- 共享：Evidence（候选卡/star 证据纪律）、Discovery、Evaluation、Memory 思想。
- 区分：Human Memory=06_expansion_index（我知道什么/该学什么）；Agent Memory=memory/（我会什么/什么工具有效/什么失败模式高频）。
- 不互相覆盖：03 的知识候选 → 供 Human 学习；本层的能力/工具/工作流 → 供 Agent 执行。
