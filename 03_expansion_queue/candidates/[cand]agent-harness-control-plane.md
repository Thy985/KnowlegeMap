# 候选证据卡 · [cand] Agent Harness / Control Plane 新范式（Omnigent + MS Agent Framework + Harness 调查）

> 状态：`[cand]` ｜ 分类：Agent Runtime / Harness / 编排（S3/S5） ｜ 发现：2026-09-01 ｜ 等级：**S**

## 一句话定位
2026 年 Agent 工程的重心正从"单一 harness"上移到 **meta-harness / control plane 层**（组合、治理、协作）；Databricks Omnigent 与 Microsoft Agent Framework 1.0 是代表，arXiv 已有以 model-harness 视角拆解 runtime 六职责的综述论文。

## 1. 它是什么 / 解决什么问题
- **Databricks Omnigent**（2026-06-16 开源，Apache 2.0，alpha）：meta-harness，位于你已有的 Claude Code/Codex/Pi/自研 agent 之上，把多 harness 变成可互换部件。三支柱：Composition（组合多模型/harness）、Control（**在 meta-harness 层做有状态上下文策略**，如成本预算/权限，而非 prompt 层）、Collaboration（共享会话 URL 实时协作）。架构 = runner 包裹任何 agent 为统一 API 的沙箱会话 + server 提供策略/共享["https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents"]
- **Microsoft Agent Framework 1.0**（2025-10 GA；Build 2026 发布 Agent Harness、Hosted Agents、CodeAct、多代理编排模式稳定）["https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/"]["https://www.infoq.cn/article/aDEJegvNSKwvue2JZ0yI"]
- **Harness 调查论文**《From Question Answering to Task Completion: A Survey on Agent System and Harness Design》（arXiv 2606.20683）：把执行 harness 拆成 **observation / context / control / action / state / verification 六项耦合职责**，映射任务属性→harness 选择["https://arxiv.org/abs/2606.20683v1"]

## 2. 为什么与我的知识/项目关系密切
- **六职责分解（尤其 verification 是独立职责）与我的"验证编译器 / 五维模型"几乎同构**——我的理论在 2026 年获得学术侧独立印证，可交叉验证
- **TeamMind** 本质就是"项目级 meta-harness"：Omnigent 的控制面/共享会话模式可直接借鉴
- **EP-002 / Permission**：Omnigent 的"策略在 harness 层而非 prompt 层"正是我 EP 原则的工程化表述
- **agent-attention**：Omnigent 的实时共享会话 = 通知/协作的另一种形态

## 3. 证据与活跃度
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（Databricks/MS 官方 + arXiv 一手来源核验） |
| 来源 | https://github.com/omnigent-ai/omnigent ｜ https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents ｜ https://arxiv.org/abs/2606.20683v1 |
| 活跃度 | 极高（Omnigent 2026-06 开源、路线图含 GEPA/MemEx/RLM/Omnigent Server MCP；MS 2026-06 Build GA） |
> **雷达增量（2026-09-18，harness 内 context 工程机制）**：
> - **"Context Engineering Inside the Harness"（MarkTechPost 09-12）**：harness 层四机制击败上下文溢出/目标丢失——**compaction（压缩）、memory strategy（记忆策略）、context budgeting（上下文预算）、todo-state（任务状态跟踪）**，逐一对比 LangChain Deep Agents/Claude Code/Manus/OpenAI Codex/Bedrock AgentCore 的实现与**实际阈值**——context 工程从"prompt 层技巧"下沉为 harness 机制["https://www.marktechpost.com/2026/09/12/context-engineering-inside-the-harness-4-mechanisms-that-beat-context-overflow-and-goal-loss-on-long-horizon-tasks/"]
> - **TrueFoundry 网关层 context 工程（09-11）**：`X-TFY-CONVERSATION-ID` 会话管理把 30 轮运行变成一条可查询时间线（而非 30 条孤立请求）——context 编排下沉到网关层["https://www.truefoundry.com/es/blog/context-engineering-gateway-session-management"]
> - **含义**：① 与 Harness 调查论文"六职责"（observation/context/control…）互证——**context 职责的工程细节（四机制阈值）已在生产 harness 中收敛**；② Omnigent"控制面在 harness 层而非 prompt 层"获得实现级印证；③ TeamMind/自研 harness 可直接对照四机制与阈值做差距分析（compaction 触发阈值/budget 分配）

## 4. 验证计划
- [ ] 精读六职责分解论文，与我五维模型做逐项对照（产出对照卡）
- [ ] 跑 Omnigent quickstart，评估"组合 Claude Code + Codex"对我的实际工作流价值
- [ ] 评估 TeamMind 架构迁移到 meta-harness 模式的成本/收益

## 5. 决策
- [ ] 晋升 validated
- [x] 维持观察（待六职责对照卡）
- [ ] 拒绝
