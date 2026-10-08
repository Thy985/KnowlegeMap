# Evaluation Card（评估卡）

> 存放：`08_agent_centric/evaluations/`。评估服务于任务侧（criterion 打分）与能力侧（confidence 回写）。
> 失败与成功都必须反向塑造能力模型（Capability Evolution）。

- task_id / run_id：
- criterion：（detection-accuracy / false-positive-rate / evidence-completeness / reproducibility / ...）
- score：（0-1）
- failure：（失败模式：false-positive / timeout / missing-evidence / flaky / ...）
- regression：（相对上次是否回退）
- reproducibility：（0-1）
- evidence：（来源 / type / supporting_observation）

## 能力侧影响
- 哪些 capability confidence 变化（≥0.6 成功 +0.2；失败 -0.1 并记入 weaknesses）：
- 沉淀到 Agent Operational Memory 的 tool_stats / success_patterns / failure_patterns：
