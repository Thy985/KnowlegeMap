# 候选证据卡 · [cand] promptfoo（Agent Evals 最小试跑已验证）

> 状态：`[cand]` ｜ 关联方向：Top20 #2（Agent Evals） ｜ 日期：2026-09-01

## 一句话定位
promptfoo：MIT 开源、CLI/YAML/CI 驱动的 LLM 评估 + 红队工具，本机已实测可跑通（v0.122.2，eval 2/2 PASS）。

## 1. 它解决什么问题
- 把 LLM 开发从"试错"变成"测试驱动"：prompt/模型变更回归检测、多模型 A/B、红队安全扫描。
- 对 Agent 类项目：可做流水线级回归门禁（CI 集成）。

## 2. 为什么现在值得关注（活跃度证据）
- 1.6M npm 下载量；OpenAI 官方发布《Moving from OpenAI Evals to Promptfoo》迁移 cookbook（2026-06-03）["https://developers.openai.com/cookbook/examples/evaluation/moving-from-openai-evals-to-promptfoo"]
- 当前版本 v0.122.x（本机实测 v0.122.2 可运行），要求 Node ≥22.22.0["https://www.promptfoo.dev/docs/installation/"]
- 2026 年多份横向对比均将其列为"prompt 迭代/红队/CI 回归"首选（MIT 许可）["https://andrew.ooo/answers/best-ai-eval-frameworks-april-2026/"]["https://www.youngju.dev/blog/culture/2026-05-14-agent-evaluation-systems-2026-inspect-ai-promptfoo-phoenix-langsmith-openai-evals-deep-dive-2026"]

## 3. 与我的连接
- **连接的项目**：Tafcm（ADI 诊断接口 → 用 promptfoo 做回归门禁）、silver-shield（Benchmark Harness → 对照）、TeamMind
- **连接的知识点**：Validation 空间（"验证编译器"）、五维模型 Evaluation 维度、可观测性_LLM应用追踪
- **潜在收益**：把"验证编译器"落地为可运行工具链；promptfoo 的 TypeScript 栈与我项目栈匹配

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://www.promptfoo.dev/docs/getting-started/ ｜ GitHub promptfoo/promptfoo |
| 证据等级 | FACT（官方文档 + **本机实测**） |
| 验证方式 | ✅ 已最小试跑（见下）；下一步：接入真实 provider + 用 Tafcm ADI 场景构造回归用例 |
| 预期完成时间 | 2026-09 内 |

## 5. 本机实测记录（2026-09-01）
- 环境：Node v22.23.2 / npm 10.9.8
- 运行：`npx -y promptfoo@latest eval`（echo provider，2 个用例，无 API key）
- 结果：`✓ 2 passed (100%)`，管线完整跑通（config 驱动 → 矩阵输出 → PASS/FAIL）
- 结论：CLI + YAML + CI 化评估在本环境可用，接入真实模型只需配置 provider 与 API key

## 6. 决策
- [ ] 晋升 validated（需补一次"真实 provider + 项目场景"验证）
- [x] 维持观察（已具备升级条件）
- [ ] 拒绝
