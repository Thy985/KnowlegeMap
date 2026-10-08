# Workflow Card（工作流卡）

> 存放：`08_agent_centric/workflows/{task_type}_v{n}.md`。可演进资产：历史任务 → v2 并说明 v2 为何更好。
> 工具链是**有向图**（谁产出、谁消费、能否并行、谁互斥、谁前置），不是工具集合。

- task_type：
- version：（v1 → v2 ...）
- goal：
- evolution_reason：（v2 相对 v1 为什么更好——评估分/阶段数/失败模式变化）
- tools（有向序）：

## stages
| stage | goal | tools | depends_on | checkpoint | failure_recovery |
|---|---|---|---|---|---|
| | | | | | |

## 组合理由回顾
- 为什么 A 在前 B 在后？（数据流兼容）
- 删掉 Tool X 会损失什么能力？（Task ↕ Capability ↕ Tool 关系可查询）

## 历史评估
- 历次 evaluation score / failure / regression / reproducibility：
