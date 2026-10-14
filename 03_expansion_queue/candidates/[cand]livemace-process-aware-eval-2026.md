# 候选对象证据卡 · LiveMACE（动态市场环境下持久 Agent 的过程感知评测）

> 状态：`[cand]` ｜ 关联方向：Evaluation/Observability 周 · 动态环境/持久 Agent 评测方法论 ｜ 日期：2026-10-15（Evaluation 周 Day4）

## 一句话定位
arXiv 2610.09872（2026-10-07）**LiveMACEBench**：用真实金融市场的自然演化作为持久 LLM Agent 的过程感知测试床，30 天连续评测发现"outcome-capability gap"（实现结果与机制能力之间的差距）。

## 1. 它解决什么问题
- **静态基准的时效问题**：大多数基准是冻结快照，无法评测 agent 在演化环境中的持久适应
- **结果 vs 能力的混淆**：只评最终结果（outcome）无法区分"能力差异"与"环境运气/路径依赖"；LiveMACE 用完整决策轨迹做 mechanism-specific 诊断
- **持久 agent 评测缺失**：长时间连续运行的 agent（memory 累积、规则遵循漂移、多 agent 协作）缺乏评测范式

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **一手证据（FACT）**：arXiv 2610.09872，2026-10-07；30 天真实市场活体评测、5 个前沿模型 × 匹配配置（Tool Use / Persistent Memory / Rule Following / Multi-Agent Collaboration）
- **新颖点**：① 动态演化测试床（真实市场）替代静态基准；② 过程感知（process-aware）诊断：把 realized outcome 与 mechanism 分开评估
- **定位**：方法论论文级证据（未见配套工具），但"动态环境+持久 agent+过程诊断"组合是当前评估设计空白点的直接填补

## 3. 与我的连接
- **连接的项目**：
  - **TeamMind**：多 Agent 协作配置评测（LiveMACE 的多 agent 维度直接对标）
  - **引擎长期任务/持久记忆**：Memory 周（后续）会需要"持久 agent 评测"，此卡是先行参照
- **连接的知识点**：能力树 A 层（评估设计与标准）——静态 vs 动态测试床、outcome-capability gap 是自建基准设计的必答问题；与 AgentJudgeBench（judge 对齐随任务难度下降）同方向但不同层面
- **潜在收益**：① 自建基准时加入"动态演化/持久"维度设计；② outcome vs capability 分离评估作为引擎 eval 层指标设计的参照

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://arxiv.org/abs/2610.09872 |
| 证据等级 | FACT（arXiv，一手；30 天实测数据） |
| 验证方式 | ① 精读论文提取 outcome-capability gap 定义与 mechanism 诊断方法；② 对照引擎 eval 层写出"动态评测"差距清单；③ 关注是否有工具/数据集释出 |
| 预期完成时间 | 周六（10-17）回灌时附带；或留待 Memory 周深化 |

## 5. 验证结果
<!-- 验证后回填 -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察
- [ ] 拒绝（原因）
