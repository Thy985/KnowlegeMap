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

## 4. 验证计划
- [ ] 精读六职责分解论文，与我五维模型做逐项对照（产出对照卡）
- [ ] 跑 Omnigent quickstart，评估"组合 Claude Code + Codex"对我的实际工作流价值
- [ ] 评估 TeamMind 架构迁移到 meta-harness 模式的成本/收益

## 5. 决策
- [ ] 晋升 validated
- [x] 维持观察（待六职责对照卡）
- [ ] 拒绝
