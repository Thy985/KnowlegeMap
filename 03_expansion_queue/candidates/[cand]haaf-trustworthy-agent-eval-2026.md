# 候选证据卡 · [cand] HAAF 可信度评估范式（"Beyond Benchmark Islands" + Agentified Evaluation 趋势）
> 状态：`[cand]` ｜ 分类：Agentic 评测方法论（S2 核心研究域） ｜ 发现：2026-09-10（雷达 #9） ｜ 等级：**A**
## 一句话定位
2026 评测方法论出现"范式升级"信号：**HAAF（Holographic Agent Assessment Framework，arXiv 2603.14987）** 批判现有 agent 基准是"孤岛"（Benchmark Islands），提出在**场景流形**（任务类型×工具接口×交互动态×社会语境×风险级别）上表征 agent 可信度的系统性框架；同线 **HarnessEval-W**（arXiv 2608.16859）把"评测本身 agent 化"（assessor agent 而非固定 rubric）——与我 Agentic CLEAR/Validation 编译器的评测方法论直接互补。
## 1. 它是什么 / 解决什么问题
- 痛点：现有 agent 基准（AgentBench/WebArena/SWE-bench 等 15+）各自为岛，分数不可迁移；评测方法而非模型能力才是主要瓶颈["https://arxiv.org/html/2603.14987v1"]
- **HAAF 四组件**：① 静态认知与政策分析 ② 交互沙箱仿真 ③ 社会伦理对齐评估 ④ **分布感知代表性采样引擎**（联合优化覆盖率与风险敏感度）——在场景流形上刻画可信度而非单点分数["https://arxiv.org/html/2603.14987v1"]
- **HarnessEval-W（2026-09-01）**：把 harness 范式引入世界模型评测——评估者作为 agent 控制任务执行、解释输出、赋分（而非 brute-force 固定指标），产生可核查的推理链["https://arxiv.org/html/2608.16859"]
- 同线：Agentified Assessment（评估即 agent，arXiv 2603.02788）、AgentSearchBench（Agent-as-a-Judge + 树状 rubric，长程实时 web 任务）["https://arxiv.org/html/2603.02788v4"]["https://openreview.net/notes/edits/attachment?id=cmBQ0ow7kh&name=pdf"]
- 行业侧：Microsoft Foundry agent evaluators（unit-test 式 Pass/Fail，system vs process 双评估）["https://learn.microsoft.com/en-us/azure/foundry/concepts/evaluation-evaluators/agent-evaluators?view=foundry"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-10）**：arXiv 2603.14987 ✅（HAAF 全文）、2608.16859 ✅、2603.02788 ✅、OpenReview AgentSearchBench ✅
- 方法论共识成形：多个独立团队 2026 年同期提出"评测 agent 化 / 代表性采样 / 评估即 agent"——不是单一项目而是趋势
- 与主流"分数竞赛"（LoCoMo/LongMemEval 等）形成对照：从"更高分"转向"评估本身如何可信"
## 3. 与我的连接
- **连接的项目**：**Validation 编译器**（Claim→Evidence→Judgment——HAAF 的场景流形采样 = Evidence 收集的代表性理论）；**silver-shield**（可信度分级评估——HAAF 的风险敏感采样直接可用）；**Agentic CLEAR**（同域方法论对照：CLEAR 是具体基准，HAAF 是元框架）
- **连接的知识点**：Agentic 评测（S2 核心）、五维模型 Evaluation 维度、基准批判方法论（已用于记忆基准批判）
- **潜在收益**：给 Validation 编译器补"代表性评估"理论层；与 Agentic CLEAR 卡构成"基准 + 元框架"互补对
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/html/2603.14987v1 ｜ https://arxiv.org/html/2608.16859 ｜ https://openreview.net/notes/edits/attachment?id=cmBQ0ow7kh&name=pdf |
| 证据等级 | **FACT（arXiv 全文核验通过）** |
| 验证方式 | 精读 HAAF 采样引擎设计 → 对照 silver-shield 风险分级场景 → 评估将"场景流形"思想引入 Validation 编译器评测章节 |
| 预期完成时间 | 2026-09/10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
