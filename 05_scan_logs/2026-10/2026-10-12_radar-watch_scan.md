# 扫描日志 · 2026-10-12（Personal Tech Radar 第 40 次 · Evaluation 周 第一天）

> 任务：深耕扫描（一周一域）｜ 日期：周一 00:30
> 当前领域：Evaluation / Observability（**active，本周正式开始**）
> 周一分工：建该领域能力树/基线，更新 current_focus.md

## 今日动作（建基线，非增量扫描）
按周一分工执行"建领域能力树/基线"，未做全量搜索（周一不追增量，避免重复收集基础资料）。

### 产出 1：领域能力树/基线（新建）
- **`08_agent_centric/domains/agent-evaluation.md`** —— Evaluation/Observability 领域树：
  - **五层结构**：A 评估设计与标准 / B 执行观测 / C 评测执行（Harness）/ D 判定与打分 / E 学习与演进
  - **基线三表**：已知锚点（promptfoo·DeepSeek Harness·引擎 evaluation 层·OTel GenAI·Trace-based·框架格局·Agentic Benchmarks·HAAF）｜ 缺口（**评测环境隔离设计** S 级、LLM-as-Judge 可靠性、主流基准实证、自建基准方法论、执行真相观测、可观测后端）｜ 相邻未覆盖（Harness 治理/Runtime/Memory/Computer Use 各归下周）
  - **周五验证计划**（3 候选）：AgentJudgeBench 精读对比 / 评测隔离设计落地检查（DeepSeek Harness·silver-shield）/ promptfoo Agent Evals 扩展实测
  - **JIT 原则**：不建百科，只展开任务相关缺失分支；leaf 映射扁平能力（agent-evaluation/assertion/evidence-collection/observability 等）

### 产出 2：current_focus.md 更新
- 状态 scheduled → **active**
- 周一 checkbox 勾选；目标 1（建能力树）标记完成
- 历史记录表补 10-12 产出

### 产出 3：domains/README.md 同步
- Agent Evaluation 分支加指针指向领域树文件

## 去重确认
周一为基线建设，未引入新对象；全部引用既有锚点与候选卡（39 张候选 + 2 validated），无重复收集。

## 结论
**New（领域基线建立）**——Evaluation 周正式启动；无新候选卡（周一不分推增量，待周二起）。
