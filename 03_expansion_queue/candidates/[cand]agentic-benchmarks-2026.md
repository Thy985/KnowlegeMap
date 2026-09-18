# 候选证据卡 · [cand] Agentic 基准 2026 批判视角（SWE-bench 污染 / TB 饱和 / Frontier-Bench / GAIA2）

> 状态：`[cand]` ｜ 分类：Agent 基准与排行榜（A8）/ G2-G3 ｜ 发现：2026-09-01 ｜ 等级：**A**

## 一句话定位
2026 年 Agent 基准进入"信任危机+新前线"并存期：SWE-bench 被污染/部分损坏、Terminal-Bench 趋于饱和，新的 Frontier-Bench / GAIA2 / SWE-rebench 正在定义"真实世界 agent 能力"的新标尺——这对我的"验证编译器"是直接的方法论输入。

## 1. 关键事实
| 基准 | 状态（2026-07） | 关键数字 |
|---|---|---|
| **SWE-bench / Verified** | 被污染且部分损坏，OpenAI 已停止报告 | Verified 500 子集["https://backgrind.com/blog/agentic-coding-benchmarks-2026/"] |
| **SWE-bench Pro** | 公开子集 ~30% 损坏（OpenAI 2026-07-08 标注） | 1,865 任务/41 仓库["https://backgrind.com/blog/agentic-coding-benchmarks-2026/"] |
| **Terminal-Bench 2.1** | 饱和，头部模型挤在 74–84% 带 | 89 任务["https://backgrind.com/blog/agentic-coding-benchmarks-2026/"] |
| **Frontier-Bench v0.1** | 2026-07-23 启动，软件之外（ML/科学/运维/安全/硬件/媒体） | 74 任务，最高 34.4%，**尚大开放**["https://backgrind.com/blog/agentic-coding-benchmarks-2026/"] |
| **GAIA2** | Meta，异步 agent：世界时间持续流动，~10 事件/分钟 | ~800 场景/10 个模拟宇宙["https://dreaming.press/posts/gaia2-benchmark-asynchronous-agents.html"] |
| **SWE-rebench** | 自动挖掘截止后新 issue，抗污染 | Claude Opus 4.6 65.3%["https://codersera.com/blog/ai-agent-benchmarks-state-of-leaderboard-may-2026/"] |
| **ARC-AGI-3** | 0.51% AI / 100% 人类，最大人机差距 | 交互式 agent 评测["https://github.com/jamoeight/claude-code-deep-research-v2/blob/main/research/sota_agents_2026_report.md"] |

## 2. 与我的知识/项目关系
- **Validation 空间 / "验证编译器"**：基准污染与饱和是"证据不可信"的活教材，强化我的"区分厂商自报 vs 独立评测"纪律
- **silver-shield Benchmark Harness**：可借鉴"抗污染基准设计"（自动挖掘、截止后数据、held-out）
- **Agent 能力评估**：Frontier-Bench 的"软件之外"维度（安全/运维）与我的 G1 方向交汇

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（多源 2026 评测，含 OpenAI 官方标注的污染声明） |
| 来源 | https://backgrind.com/blog/agentic-coding-benchmarks-2026/ ｜ https://dreaming.press/posts/gaia2-benchmark-asynchronous-agents.html |
| 验证方式 | 读 Frontier-Bench/GAIA2 定义 → 评估给我的 agent 项目设计抗污染自测基准的方法 |
| 预期 | 2026-10 |
> **雷达增量（2026-09-14，Changed）**：
> - **SWE-Bench Pro Verified（arXiv 2609.08149，2026-09-08）**：审计发现 SWE-Bench Pro 存在 **reward hacking**（gold solution/隐藏评测信息泄漏）+ 任务质量问题（误导性题目/不当测试范围）——发布 Pro 的 verified 版本修复两源不可靠性——基准批判链条延续（SWE-bench→Pro→Pro Verified）["https://arxiv.org/abs/2609.08149"]
> - **Terminal-Bench 4.0 + Dataset Registry（09-04/09-10）**：4.0 重校准任务资源、移除不再区分前沿系统的任务（66 个专业计算机工作任务）；**Registry** 让基准开发者用 TB harness 构建/适配新基准（已适配 SWE-Bench Verified/AppWorld/DevEval/EvoEval）——基准进入"基建化/可组合"阶段["https://www.tbench.ai/news/registry-and-adapters"]["https://benchlm.ai/benchmarks"]
> - **SWE-bench-Live（持续更新）**：首个自动更新、多语言多 OS 的抗污染 SWE 任务集（自动策展管线 + 污染免疫）——与 SWE-rebench 同线的官方系["https://swe-bench-live.github.io/"]
> - **AutomationBench-AA（09-08）**：Artificial Analysis 用 Zapier AutomationBench **657 个业务工作流**（Gmail/Slack/Salesforce/Jira 模拟）替换 τ³-Banking——agent 评测扩展到业务自动化["https://aihot.virxact.com/items/cmtrkorkr07jcrotnfw2az9on"]
> - **含义**：① 基准批判从"口头质疑"进入"官方 verified 修复"（SWE-Bench Pro Verified），reward hacking 成为基准设计一等公民问题；② Terminal-Bench Registry 的"基准可组合"模式 = 我 Validation 编译器想要的"证据管线复用"；③ 业务自动化基准（AutomationBench）补上"企业级 agent 评测"维度
> **雷达增量（2026-09-19，新基准 + 权威榜单更新）**：
> - **Sierra Hyper-τ-Bench（09-08 开源）**：评估 **coding agents 能否构建可用的客服 agent**——自动化最高 23.9% vs 人工组合 82.2%——"agent 建 agent"能力被量化（与 HAAF/Agentified Assessment 的"agent 评估 agent"同线）["https://bobweb.ai/sierra-releases-hyper-%CF%84-bench-as-open-source-a-benchmark-for-agent-development-unite-ai/"]
> - **GitTaskBench（09-13）**：中科院/北大/港科大合研的代码 agent 评估框架["https://ai-damn.com/gittaskbench-revolutionizes-code-agent-evaluation-standards-1756700723292"]
> - **MTAC-IFBench（09-14，arXiv 2609.14992）**：多轮 agentic 编码的**指令跟随**基准——平均 7.04 轮/实例、91.33 条约束/实例，checklist + 验证脚本 + judge 三层评测——"多轮约束保持"新评测维度["https://arxiv.org/abs/2609.14992"]
> - **Artificial Analysis Coding Agent Index v1.5（09-18 更新）**：Terminal-Bench 2.1→4.0（66 更硬终端任务）、DeepSWE v1.0→v1.1（隔离验证 patch）、SWE-Atlas-QnA 对齐——**权威榜单口径持续收紧**["https://artificialanalysis.ai/methodology/coding-agents-benchmarking"]
> - **含义**：① 基准谱系从"解题"扩展到"**构建 agent**（Hyper-τ）与"**多轮约束保持**"（MTAC-IF）——评估对象从单任务能力转向长程工程能力；② AA Index 每次换版都收紧任务/验证（防饱和+防污染）印证"基准工程化"主线；③ 对 silver-shield Benchmark Harness 的设计输入：checklist+验证脚本+judge 三层结构可直接借鉴

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
