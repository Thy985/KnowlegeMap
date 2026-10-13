# 候选对象证据卡 · ReviewBench（GitHub 官方 AI 代码审查离线基准）

> 状态：`[cand]` ｜ 关联方向：Agent Evaluation / 代码审查基准（当前深耕领域·增量）｜ 日期：2026-10-14（深耕 Day3）

## 一句话定位
GitHub 官方（GitHub Blog）发布的 AI 代码审查**离线评测基准**：按 1 亿+ 真实 PR 的语言/仓库规模/PR 规模分布建模，多源 golden set + 统一评估 rubric + 资深工程师独立验证。

## 1. 它解决什么问题
- **AI code review 缺可靠离线基准**：以往缺少可复现、有统一标尺的 code review 评测集 → ReviewBench 补齐
- **分布代表性**：遵循 1 亿+ 真实 GitHub PR 的语言、仓库规模、PR 规模分布，避免小样本/偏差集
- **评估一致性**：多源 golden set + 一致 rubric，资深工程师独立验证，保证评分可靠

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **一手证据（FACT）**：GitHub Blog 2026-10-05 官方文章（github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/），"available for you to use today"
- **来源权威**：GitHub 官方（Copilot 团队）
- **活跃度**：10-05 发布，基准已开放使用
- **新颖点**：与去重基准中的 Pullfrog/OpenCodeReview（代码审查**工具**）不同——这是**评测基准本身**，且其方法论（真实 PR 分布建模 + 多源 golden set + 独立验证）正是能力树"自建基准方法论"缺口的高质量范例

## 3. 与我的连接
- **连接的知识点**：能力树 E 层（自建基准方法论）——规模分布建模、多源 golden set、独立验证三步法可直接迁移
- **连接的项目**：Validation 编译器（rubric 一致性设计可对照）；dsh 相关代码质量链路；如果 User 做代码审查类 Agent，这是首个可靠基线
- **潜在收益**：① 自建评估集的方法论模板（分布→golden set→rubric→独立验证）；② 与 AI code review 工具类候选（OpenCodeReview）形成"基准+工具"配对验证

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/（2026-10-05） |
| 证据等级 | **FACT**（GitHub 官方） |
| 验证方式 | ① 精读博客获取数据集规模/构成/golden set 来源；② 若仓库公开，抽样检查 rubric 与样例；③ 将"分布建模+多源 golden set+独立验证"方法论写入能力树 E 层笔记 |
| 预期完成时间 | 2026-10-16 周五验证可选（与 AgentJudgeBench/Transect 并列或后续） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察
- [ ] 拒绝（原因）
