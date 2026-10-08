# 01 · Agent Domain Model（Mode B 领域模型）

> 设计原则：**Agent 是一等公民**。Task 是 Agent capability discovery 的主要驱动因素。"需要什么"先于"推荐什么"。
> 对应实现：`09_agent_engine/engine/domain.py`（本文件是它的权威规范）。

## 实体关系图（最小闭环）

```
Task ──decompose──▶ Capability Requirements
  │                        │
  │                        ▼
  │              Capability Gap Analysis ◀── Agent.capabilities
  │                        │
  │                        ▼
  │              Tool / Project Discovery
  │                        │
  │                        ▼
  │              Tool Composition ──▶ Selection Reasons
  │                        │
  │                        ▼
  │              Workflow Synthesis
  │                        │
  ▼                        ▼
Execution ──▶ Evaluation ──▶ Agent Operational Memory ──▶ Capability Evolution
                  │
                  └──▶ Evidence（可追溯）
```

## 实体定义

### 1. Agent
| 字段 | 类型 | 说明 |
|---|---|---|
| agent_id | str | 唯一标识 |
| identity | str | 身份声明（如 "pen-test agent"） |
| role | str | 角色（如 "offensive-security specialist"） |
| objective | str | 总体目标 |
| available_tools | list[Tool] | 当前可调用的工具 |
| available_skills | list[Skill] | 当前已沉淀的技能 |
| memory | Memory | 操作记忆（见 §10） |
| environment | dict | 运行环境（os/runtime/网络可达性等） |
| constraints | list[str] | 硬约束（权限/合规/沙箱） |
| autonomy_level | int(0-5) | 自主度（0=人工逐级批准，5=全自主） |
| capabilities | list[Capability] | 已具备能力（含 confidence/evidence） |
| weaknesses | list[str] | 已知弱点（来自 evaluation/failure） |
| task_history | list[TaskRun] | 历史任务执行记录 |
| evaluations | list[Evaluation] | 历史评估 |

### 2. Capability（能力——发现单位）
| 字段 | 说明 |
|---|---|
| capability_id | 如 `browser-interaction` |
| name / description | 名称与定义 |
| prerequisites | 前置能力（依赖图） |
| required_tools | 可实现的工具候选（注意：能力≠工具，一能力多工具） |
| related_projects | 相关开源项目 |
| confidence | 系统对该能力"已掌握"的信心（Agent 侧） |
| evidence | 支撑证据 |
| evaluation_history | 能力级评估历史 |

**Capability 是"需要什么"的答案**——先有 Capability 需求，再谈工具。

### 3. Tool
| 字段 | 说明 |
|---|---|
| name / category | 名称与类别（browser/sandbox/memory/evals/…） |
| interface | CLI / API / SDK / MCP / GUI |
| input / output | 输入输出格式（组合时检查数据流兼容） |
| environment requirements | 运行环境要求 |
| permissions | 所需权限 |
| strengths / weaknesses | 优劣势（结构化） |
| cost | 成本（时间/金钱） |
| reliability | 可靠性信号（来源+统计） |
| security implications | 安全影响（EP-002：权限即边界） |
| automation_friendly | 是否适合 Agent 调用（CLI 原生/结构化输出） |

### 4. Skill（可演进资产）
| 字段 | 说明 |
|---|---|
| name / purpose | 名称与用途 |
| trigger | 触发条件 |
| procedure | 步骤（引用 workflow） |
| required_tools | 依赖工具 |
| prerequisites | 前置能力 |
| evaluation | 评估记录 |
| usage_count / success_rate / last_used | 使用统计（来自 Agent Operational Memory） |

### 5. Workflow（组合产物）
| 字段 | 说明 |
|---|---|
| goal | 目标 |
| stages | 阶段（每个 stage 含 tools/角色/检查点） |
| agent_roles | 参与的 agent 角色 |
| tools | 工具链（有向） |
| dependencies | 阶段依赖 |
| checkpoints | 检查点（质量门） |
| failure_recovery | 失败恢复策略 |
| evaluation | 工作流级评估 |
| version | 版本（v1→v2 演进，记录演进理由） |

### 6. Task（驱动实体）
| 字段 | 说明 |
|---|---|
| task_type | 类型（security-assessment/autonomous-agent/…） |
| objective | 目标（自然语言） |
| constraints | 约束 |
| environment | 环境 |
| desired_output | 期望产出 |
| risk_level | 风险级（low/med/high/critical） |
| evaluation_criteria | 评估标准 |

### 7. Evidence
| 字段 | 说明 |
|---|---|
| source | 来源（URL/实验/观察） |
| type | FACT / DESIGN / OBSERVATION / EXPERIMENT |
| confidence | 置信 |
| timestamp | 时间 |
| supporting_observation | 支撑观察 |

### 8. Evaluation
| 字段 | 说明 |
|---|---|
| criterion | 标准（如 "detection accuracy"） |
| score | 分数（0-1 或 0-100） |
| evidence | 支撑证据 |
| failure | 失败模式（如 false-positive/timeout） |
| regression | 相对上次是否回退 |
| reproducibility | 可复现性 |

### 9. Selection Reason（选择理由——Mode B 与"GitHub 推荐器"的本质区别）
每个 Tool/Skill/Project 选择必须记录多维理由：
`task_fit / capability_coverage / interface_compatibility / automation_friendliness / reliability / maintenance_status / ecosystem_maturity / environment_compatibility / computational_cost / permission_requirements / security_risk / evidence_quality`
形式：`Candidate → Evaluation → Selection`。**Star 数仅作弱信号，不单独构成理由。**

### 10. Memory（区分 Human Memory 与 Agent Operational Memory）
| | Human Memory（06_expansion_index 维护） | Agent Operational Memory（08_agent_centric/memory 维护） |
|---|---|---|
| 关注 | 我知道什么 / 我该学什么 | 我会什么 / 什么工具有效 / 什么工作流有效 |
| 服务 | Human 学习决策 | 未来任务执行 |
| 记录 | 知识对象 + 学习状态 | 工具统计 + 失败模式 + 组合经验 + 工作流版本 |
| 更新 | 雷达扫描 | 任务执行后 Evaluation 回写 |

## 安全边界（Agent-Centric ≠ 无限自治）
- 每个 Task 标注 risk_level；autonomy_level 与 risk 联动（高风险任务要求更高人工批准门槛）。
- Tool 选择的 `permission_requirements` 与 `security_risk` 参与评分与组合决策。
- EP-002「Permission Is Security Boundary」在 Mode B 落地为：**工具权限声明（declared）vs 实际授权（granted）分离，缺口即阻止**。
