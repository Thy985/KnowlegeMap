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

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
