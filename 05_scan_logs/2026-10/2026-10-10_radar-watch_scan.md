# 扫描日志 · 2026-10-10（Personal Tech Radar 第 38 次 · 通用过渡期全量）

> 任务：深耕扫描（一周一域）｜ 日期：周六 00:30
> 当前领域：Evaluation/Observability（scheduled，10-12 周一开始；10-09~10-11 通用全量过渡期）
> 周六"回灌"分工：本周无验证结果（领域未开始），执行通用全量扫描。

## 扫描范围
general_search 通用全量：Agent Evals 框架/基准 + Agent Harness/Runtime 新变化 + Flutter 本地 agent 生态。

## 结果

### 新建卡（1）
- **AgentJudgeBench**（arXiv 2608.26623，2026-08-27）——**A 级**，分类 Agent Evaluation/Judge 评测。
  - 3,808 BFCL 风格实例、6 DAG 拓扑、3 档难度；5 生成器 + 6 judge
  - 关键发现：judge 对齐度随难度单调下降，无 ground-truth 退化快 1.5x；hard+无 ground-truth 精度崩塌；喂 ground-truth 反损对齐（over-reliance）
  - 与引擎 evaluation 层（criterion 打分）/ silver-shield / Validation 编译器直接相关；纳入 Evaluation 周验证计划（10-13 前精读）
  - 来源：https://arxiv.org/pdf/2608.26623 ｜ dev.to digest（10-08）

### 追加增量（1）
- **flutter-local-llm 卡**（Flutter 本地 agent 框架新生态）：
  - **dart_agent_core 2.0.4**（2026-06-27）：mobile-first local-first，完整 agentic loop + evals + skill system + 上下文压缩
  - **flutter_agentic**：7 provider 统一 API + ReAct + on-device Gemma/GGUF
  - **flutter_local_agent_kit 1.0.2**：offline-first，llamadart 本地推理 + RAG + ReAct + Material 3 Chat UI
  - 含义：Flutter 侧"本地推理→本地 agent"最后一层补齐，Tafcm 直接候选；dart_agent_core 自带 evals 与 Evaluation 周交叉

### 记日志不建卡（Evaluation 周素材）
- **AgentSeer**（arXiv 2509.04802）：可观测框架，执行 span → 知识图谱追踪漏洞——评估×可观测交叉，留待 Evaluation 周
- **HAL Holistic Agent Leaderboard**（Princeton Sayash Kapoor）：数百 VM 并行评估 harness，模型×scaffold×基准三维分析——评估基础设施，留待 Evaluation 周
- **MLflow/DeepEval/Phoenix 等 2026 评测框架榜单**（MLflow 09-11 / Confident AI 10-05）：已知框架格局的厂商综述，无新对象
- **MS Agent Framework Python 1.16.0**（08-27，OTel provider 编程配置）：已知对象小增量，不建卡
- **Flutter Agent Harness v1.0.536**（undercodenews 10-09）：来源弱，与 flutter 卡增量重叠，不单列

## 去重确认
AgentJudgeBench / AgentSeer / HAL / dart_agent_core / flutter_agentic / flutter_local_agent_kit 均不在 06_expansion_index 去重基准与 00_starred_reference 中 → 均为首次发现。

## 结论
**New**（AgentJudgeBench 建卡）+ **Changed**（flutter-local-llm 卡增量）。候选卡 38→39。
