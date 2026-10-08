# Agent Task Card（Mode B · 任务卡）

> 由引擎 `09_agent_engine/cli.py run --task-type ... --objective ...` 生成，或手工填写入 `08_agent_centric/tasks/`。
> 用途：把一次 Agent Task Expansion 的完整链路（能力→工具→组合→工作流→评估）沉淀为可追溯资产。

- task_id：
- task_type：（security-assessment / e2e-web-testing / long-running-autonomous-agent / local-mobile-ai-assistant / multi-agent-team / agent-eval-harness）
- objective：
- risk_level：（low / med / high / critical）——high 及以上强制 approval 前置（EP-002）
- desired_output：
- constraints：
- evaluation_criteria：

## Required Capabilities（任务→能力分解）

## Capability Gap（已有 vs 需求）
- missing：

## Tool Discovery（能力驱动）
| capability | candidate tools |

## Tool Composition（组合理由）
- 工具链（有向序）：
- 每个工具的多维 Selection Reason（task_fit / coverage / automation / structured / reliability / eco / 权限 / 风险）：
- 排除候选与原因：
- 数据流缺口（需转换环节）：

## Workflow（v1 / v2 ...）
- stages（goal / tools / depends_on / checkpoint / failure_recovery）
- evolution_reason（v2 相对 v1 为什么更好）：

## Evaluation
- score / failure / reproducibility / evidence：

## Memory Update
- 工具统计 / 成功失败模式 / 环境失败：
