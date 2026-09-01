# 候选证据卡 · [cand] Evals 框架选型格局（2026）

> 状态：`[cand]` ｜ 关联方向：Top20 #2（Agent Evals）+ #8（基准） ｜ 日期：2026-09-01

## 一句话定位
2026 年 LLM/Agent 评估框架已分层：promptfoo（prompt 迭代/红队/CI）、DeepEval（Python 单元式断言）、OpenAI Evals（Agent 规模化）、Inspect（安全/能力评测，UK AISI）、Ragas（RAG 专用）、Langfuse（生产可观测+评估）。

## 1. 它解决什么问题
不同评估诉求需要不同框架，选错会增加集成成本；本卡给出按场景的选型地图。

## 2. 为什么现在值得关注（活跃度证据）
- 多份 2026-04~05 横向评测与选型指南发布（andrew.ooo、QASkills、scrolltest、genai.qa 等）["https://andrew.ooo/answers/best-ai-eval-frameworks-april-2026/"]["https://qaskills.sh/blog/llm-evals-comparison-openai-promptfoo-ragas"]["https://scrolltest.com/deepeval-vs-promptfoo-llm-evaluation-framework/"]
- OpenAI 官方正推动从 OpenAI Evals 迁移到 promptfoo 的路线["https://developers.openai.com/cookbook/examples/evaluation/moving-from-openai-evals-to-promptfoo"]
- Inspect（UK AISI 出品，MIT）专注安全/能力评测，与"AI 安全"方向直接相关["https://andrew.ooo/answers/best-ai-eval-frameworks-april-2026/"]

## 3. 选型地图（2026）
| 场景 | 首选 | 备选 | 理由 |
|---|---|---|---|
| Prompt 迭代 / A-B / 回归 | promptfoo | DeepEval | CLI/YAML/CI、50+ 断言、40+ 红队插件 |
| Agent 多步流程评估 | OpenAI Evals | Inspect | Agent 场景支持最佳 |
| Python 研究型 QA / RAG | DeepEval | Ragas | pytest 原生、G-Eval/DAG/QAG |
| 安全 / 能力评测 | Inspect（AISI） | promptfoo 红队 | 安全社区背书 |
| 生产可观测 + 评估 | Langfuse | Phoenix | 开源、与追踪一体 |
| RAG 专用指标 | Ragas | — | Faithfulness/Relevancy 等 |

## 4. 与我的连接
- **连接的项目**：Tafcm（promptfoo 已实测）、silver-shield（DeepEval/Inspect 场景）、dsh-pentest（Inspect 安全评测）
- **连接的知识点**：Validation 空间、Evaluation 维度、AI 安全方向（Inspect）
- **潜在收益**：为不同项目选型提供依据；Inspect 是进入 AI 安全评测的现成入口

## 5. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | 各框架官方文档 + 上述 2026 横向评测 |
| 证据等级 | FACT（官方文档）+ DESIGN（第三方选型观点，已标注） |
| 验证方式 | promptfoo 已实测；DeepEval/Inspect 待各跑一次最小 demo |
| 预期完成时间 | 2026-09 内 |

## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察（作为选型依据 + 后续框架验证队列）
- [ ] 拒绝
