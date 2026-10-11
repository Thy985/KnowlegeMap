# Domain Tree · Agent Evaluation / Observability（评估与可信验证）

> 建立：2026-10-12（周一，Evaluation 周第一天）｜ 类型：领域能力树/基线
> 定位：横向能力——TeamMind / silver-shield / agent-attention / 引擎自身都需要；命中"高效、可信、可控"主线。
> 树与图分工：本文件是 **Tree**（层级组织与任务分解）；跨域复用/依赖见 `08_agent_centric/capabilities/graph.md`（Capability Graph）。
> JIT 原则：不建百科，只展开与任务相关、且当前缺失的分支。

## 一、领域树（Agent Evaluation / Observability）

```
Agent Evaluation / Observability
├── A. 评估设计与标准（Evaluation Design）
│   ├── A1. 任务分解与评估准则定义（criterion 定义）
│   ├── A2. 测试集 / 基准构建（benchmark 方法论）
│   ├── A3. Ground Truth 建立（程序化验证 vs LLM-judge 对照）
│   └── A4. 难易度分层与任务类型覆盖
├── B. 执行观测（Observability）
│   ├── B1. Trace / Span 捕获（OTel GenAI 标准）
│   ├── B2. 执行真相观测（过程级 vs 结果级，ThinkingBox 类）
│   ├── B3. 语义事件与会话级可观测
│   └── B4. Agent 行为审计（trace → 知识图谱，AgentSeer 类）
├── C. 评测执行（Harness）
│   ├── C1. 评测环境隔离设计（网络 / 凭据 / 外部目标三隔离）★ 10-11 重大事件
│   ├── C2. Harness 编排与并行执行（HAL 类：模型 × scaffold × 基准）
│   ├── C3. 确定性断言与程序化验证
│   └── C4. fail-closed 网络策略（eval 默认不出网）
├── D. 判定与打分（Scoring）
│   ├── D1. LLM-as-Judge 可靠性（AgentJudgeBench 类）
│   ├── D2. 程序化 scorer / 断言
│   ├── D3. Judge 对齐度与 ground-truth 依赖管理
│   └── D4. 结果聚合与报告（result aggregation）
└── E. 学习与演进（Feedback Loop）
    ├── E1. 回归检测与长期漂移（regression / drift）
    ├── E2. 评测结果回灌能力模型（capability update）
    ├── E3. Skill / Workflow 版本演进（usage/success/failure 统计）
    └── E4. 验证资产沉淀（evidence + reproducibility）
```

## 二、基线：已知 vs 缺口 vs 相邻未覆盖

### 已知（系统已覆盖，不重复收集）
| 锚点 | 状态 | 说明 |
|---|---|---|
| promptfoo | **validated**（本机 eval 2/2 PASS） | Agent Evals 断言/评测，S 级 |
| DeepSeek Harness | **validated**（v0.2.1-alpha.1 增量） | Harness 骨架，S 级 |
| 引擎 evaluation 层 | 已实现 | criterion 打分 + 证据保留（09_agent_engine/evaluation.py） |
| OTel GenAI 可观测标准 | [cand] A | OTel/Langfuse 官方（otel-genai-observability.md） |
| Trace-based Agent Eval | [cand] | 轨迹驱动评测方法（trace-based-agent-eval-2026.md） |
| Evals 框架格局 | [cand] A | 2026 横向评测（evals-framework-landscape.md） |
| Agentic Benchmarks | [cand] | SWE-bench/GAIA/MLE-bench 格局（agentic-benchmarks-2026.md） |
| HAAF 可信 Agent Eval | [cand] | 可信评估方法（haaf-trustworthy-agent-eval-2026.md） |

### 缺口（本领域内未覆盖，Evaluation 周重点）
| 缺口 | 证据 | 优先级 |
|---|---|---|
| **评测环境隔离设计**（网络/凭据/外部目标三隔离，fail-closed） | 10-11 重大事件：OpenAI 暂停训练 + Anthropic 切断 eval live internet | **S（本周一级节点）** |
| **LLM-as-Judge 可靠性方法**（对齐度、ground-truth 依赖、over-reliance） | AgentJudgeBench（A 级卡，10-13 前精读） | A |
| 主流 Agent 基准实证（SWE-bench/GAIA/MLE-bench 未实测） | Knowledge Gap Map G2 | A |
| 自建评估基准方法论 | Knowledge Gap Map G2 | B |
| 执行真相观测（过程级 vs 结果级） | ThinkingBox（10-08 已记日志） | B |
| 可观测后端工程化（trace 存储/查询/审计链） | Knowledge Gap Map G2 | B |

### 相邻未覆盖（本领域外、可外推）
| 相邻方向 | 与 Evaluation 的连接 | 归属周 |
|---|---|---|
| Harness / 控制面治理（VeriHarness/AgentVerify/Specula） | eval harness 是治理面的一部分 | 下一域（Harness/治理） |
| Agent Runtime 状态持久化/失败恢复 | eval 需在长运行场景下验证 | Runtime 周（接 TeamMind） |
| Agent Memory 评测（MemEval 等） | 记忆能力需评估基准 | Memory 周 |
| Computer Use 评测 | browser agent 需要专用 eval | Computer Use/Browser 周 |

## 三、本周验证计划（周五 10-16 用，2-3 个高价值候选）
1. **AgentJudgeBench 精读**（10-13 前完成精读 → 周五出对比结论）：judge 对齐度 vs 任务难度、ground-truth 依赖——对照引擎 evaluation 层设计建议
2. **评测隔离设计落地检查**：对照 DeepSeek Harness / silver-shield 验证计划，加入隔离性检查项（网络/凭据/外部目标三隔离）
3. **promptfoo Agent Evals 扩展实测**：从已有 2/2 PASS 扩展到 agent 场景断言（可选，视 AgentJudgeBench 结论）

## 四、任务视图（Capability Tree 动态实例化锚点）
- 任务类型 `agent-evaluation-task` → 实例化本领域树，JIT 只展开缺失分支
- 引擎映射：leaf `maps_to` 扁平能力（agent-evaluation / assertion / evidence-collection / reporting / result-aggregation / self-improvement / observability / monitoring），见 `08_agent_centric/capabilities/README.md`

## 五、回灌目标（周六 10-17）
- 更新 `08_agent_centric/capabilities/graph.md`（补 evaluation 相关跨域边）
- 更新 `04_connections/README.md`
- 候选 → validated / dropped 决策
