# 候选证据卡 · [cand] AgentJudgeBench（LLM-as-Judge 可靠性基准）
> 状态：`[cand]` ｜ 分类：Agent Evaluation / Judge 评测（G2，S2 核心） ｜ 发现：2026-10-10（雷达） ｜ 等级：**A**
## 一句话定位
一个 3,808 实例的 LLM-as-Judge 评测基准（arXiv 2608.26623，2026-08-27）：以 BFCL 风格 tool-calling 轨迹 + 程序化验证的 ground-truth 为底，系统量化"LLM 当 judge 评 agent"的可靠性边界。
## 1. 它解决什么问题
- **Judge 不可信问题**：LLM-as-judge 广泛用于 agent 评测（我的引擎 evaluation 层、silver-shield、promptfoo 同线），但 judge 对齐度（与人类/ground-truth 的一致性）此前无系统基准
- 结论：**judge 对齐度随任务难度单调下降，无 ground-truth 时退化快 1.5x**；hard 且无 ground-truth 时 judge 精度崩塌——"难任务上的自我评测不可靠"被量化
- 反直觉发现：**喂 judge ground-truth 反而可能损害对齐**（over-reliance）——评测设计不是"给的信息越多越好"
- 构成：3,808 BFCL 风格记录、6 种 DAG 拓扑、3 档难度；5 个生成器（3B–70B open-weight + GPT-5.4）+ 6 个 judge（20B→frontier）
## 2. 为什么现在值得关注（活跃度证据）
- 2026-08-27 arXiv 首发（2608.26623），多站 09 月初报道（Lilys AI 09-07 / ChatPaper）；与本周 agent 工程 digest（dev.to 10-08 "The Agent Harness Goes Platform-Native"）并列引用
- 定位：与已记录的 Agentic CLEAR（09-04，A）、HAAF（09-10，A）、ThinkingBox（10-08，执行真相）同属"评测可靠性"主线，但**切入点是 judge 本身**——补上"评测者的评测"环节["https://arxiv.org/pdf/2608.26623"]["https://dev.to/felipe0liveira/the-agent-harness-goes-platform-native-and-the-guardrails-scramble-to-keep-up-j13"]
## 3. 与我的连接
- **连接的项目**：**引擎 evaluation 层**（criterion 打分 + 证据保留——judge 可靠性直接决定打分可信度）；silver-shield（风险判定可视为 judge 任务）；Validation 编译器（"证据→判断"的可靠性理论层）
- **连接的知识点**：Agent Evaluation（G2/S2）、HAAF 场景流形、ThinkingBox 执行真相、promptfoo 本机验证经验
- **潜在收益**：① 给引擎 evaluation 层加"judge 校准"约束（关键结论不依赖单一 LLM 打分）；② 下周一 Evaluation 周（10-12 起）的核心候选对象
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/abs/2608.26623（arXiv 全文） |
| 证据等级 | FACT（arXiv 全文可读；多站独立转述） |
| 验证方式 | 精读全文 → 提取难度分层/ground-truth 条件设计 → 对照引擎 evaluation 层设计 judge 校准实验（计划纳入 Evaluation 周） |
| 预期完成时间 | 2026-10-13 前（Evaluation 周周二/周三） |
## 5. 验证结果
<!-- 验证后回填 -->
> **雷达增量（2026-10-10，Changed）**：
> - 同周线确认：dev.to 10-08 agent 工程 digest 将其列为本周重点（AgentJudgeBench + AgentSeer 可观测框架 + HAL 标准化 harness 三连）——"评测者可靠性 + 评测可观测 + 评测基础设施"成 2026 Q4 评估主线
> - 相邻对象记日志不建卡：**AgentSeer**（arXiv 2509.04802，可观测框架把执行 span 转知识图谱追踪漏洞——Evaluation 周素材）、**HAL Holistic Agent Leaderboard**（Princeton Sayash Kapoor，数百 VM 并行评估 harness，模型×scaffold×基准三维分析——Evaluation 周素材）
## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察（纳入 Evaluation 周验证计划）
- [ ] 拒绝（原因）
