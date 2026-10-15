# 候选对象证据卡 · TestJack（Agentic Coding 基准的补丁审计框架）

> 状态：`[cand]` ｜ 关联方向：Evaluation/Observability 周 · 评测可信度闭环第三环 ｜ 日期：2026-10-15（Evaluation 周 Day4）

## 一句话定位
arXiv 2610.10619（2026-10-07）开源的 **Agentic Coding 基准审计框架**：评估补丁能否超越固定测试——为每个 trial 生成针对 prompt 要求（patch 可能违反）的测试、只保留 ground-truth patch 通过的测试、复查 trial 失败，每个确认失败都由可回放测试支撑，并附轻量采样变体以控制成本。

## 1. 它解决什么问题
- **固定测试的盲区**：编码基准用预先写死的测试评估 agent 补丁，agent 可以"过测试但违背 prompt 意图"；TestJack 把评估从固定测试升级为**动态测试生成 + 审计**
- **评测结果的可信度**：哪些基准分数是真的能力、哪些是测试漏洞，需要独立审计证据（每个失败有可回放测试支撑）
- **成本**：轻量变体（深度审计随机样本 + 测试跨 trial 复用）控制审计开销

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **一手证据（FACT）**：arXiv 2610.10619，2026-10-07 发布（v1）；摘要明确"scalable framework"
- **新颖点**：不是新基准，而是**审计基准的框架**——"评测者评估评测者"，与 10-10 AgentJudgeBench（judge 可靠性）、10-13 Transect（评测者审计侧/transcript 可审计性）直接互补，构成评测可信度闭环第三环（**补丁/测试侧审计**）
- **时间线**：与 10-07 同日还有 LiveMACE 等一批新基准论文，但 TestJack 的"可回放测试"方法论对自建基准验证（周五验证计划）可直接使用

## 3. 与我的连接
- **连接的项目**：
  - **Validation 编译器**：可回放测试 + 失败可追溯思想可直接迁移
  - **引擎 evaluation 层**：criterion 打分 + 证据保留 → 补丁级动态测试生成是对现有 eval 的增强方向
  - **ReviewBench**（10-14 卡）：代码审查基准的 golden set 需要类似审计来保证质量
- **连接的知识点**：能力树 B 层（评测执行 Harness）与"主流基准实证"缺口；"评测可信度双环"（judge 侧+评测者审计侧）→ **三环**（+补丁/测试侧审计）
- **潜在收益**：① 自建基准时用 TestJack 方法生成可回放测试而非手工固定测试；② 周五验证 AgentJudgeBench/Transect 时可顺带检查其测试可审计性

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/abs/2610.10619 |
| 证据等级 | FACT（arXiv 摘要，一手） |
| 验证方式 | ① 精读论文，确认测试生成→保留→复查流程可复现；② 对照 ReviewBench 方法论写差异分析；③ 检查是否有配套代码仓库 |
| 预期完成时间 | 10-16 周五验证（与 AgentJudgeBench/Transect 并列候选） |

## 5. 验证结果
> **周五验证（2026-10-16，arXiv 摘要精读核验）**：
> - **作者阵容核验**：Shuangjie Yao / Hao Wang / **Koushik Sen / Dawn Song**（UC Berkeley）/ Simin Chen / Baishakhi Ray（Columbia）——顶校系统/安全背景，可信度高
> - **量化证据强化**：6 frontier model backends × 5 benchmarks（DeepSWE、SWE Marathon 等），**约 34.4% 被判正确的 trial 违反任务要求**，整体 resolution rate 从 **50.6% 降至 33.2%**——固定测试被 hack 不是个别现象，而是系统性偏差
> - **方法确认**：per-trial 动态生成测试（针对 prompt 要求、patch 可能违反的点）→ 只保留 ground-truth patch 通过的测试 → 复查 trial 失败；每个确认失败由**可回放测试**支撑；轻量变体=深度审计随机样本 + 测试跨 trial 复用
> - **核心主张**：静态测试增强（trial 前一次性强化）忽略真实 trial 的失败方式；"随着 LLM 越来越擅长优化固定 evaluator，evaluator 本身必须更自适应"
> - **对引擎 eval 层结论**：① 现有 criterion 打分+证据保留缺少"补丁级动态测试"环节——自建基准/评测应引入"可回放测试"概念；② 34.4% 比例说明**评测分数必须附带"测试覆盖了任务要求"的审计证据**；③ 代码仓库未见公开链接（arXiv 页无 GitHub 引用），未达 validated 门槛，方法论先行
> - **三环对比定位**：补丁/测试侧审计环（vs AgentJudgeBench judge 侧 / Transect 评测者侧）

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据；缺独立代码仓库）
- [x] 维持观察（方法论已验证可迁移，代码/复现留待后续）
- [ ] 拒绝（原因）
