# 候选对象证据卡 · Transect（长时程 Agent 评测的可观测性 / 可审计性包）

> 状态：`[cand]` ｜ 关联方向：Agent Evaluation / Observability（当前深耕领域，能力树 B 层：执行观测/可审计性）｜ 日期：2026-10-13（Evaluation 周 Day2 增量）

## 一句话定位
基于 **Inspect Scout** 的开源 transcript 分析管道：把长时程（long-horizon）Agent 评测的海量事件/令牌/子代理活动/模型生成行为标签对齐到统一回合时间线，让评估者能理解一次长运行"到底发生了什么"、把每个标签/事件**追溯回源头回合**并导出数据表做跨运行分析——对抗"评测可观测性收缩"。

## 1. 它解决什么问题
- **痛点**：前沿 AI 评测越来越多是开放式、agentic、长时程任务，一次运行 transcript 可达**数百页**、近 **1300 万 token**（论文演示案例）；评测者可可靠推断 agent 行为的"observability envelope"（可观测包络）在收缩。
- **根本张力**：LLM 助手能帮评测者分类/解释 agent 行为，但同时也给人类评估者**显著分析自由度**——这威胁 LLM 转录分析的**可复现性与可审计性**（两个评测者可能得出不同结论且无法对账）。
- **方案**：用户以可复用"评估族配置"（evaluation-family configuration）指定任务上下文 + 行为词汇表，judge 模型与分析设置分离提供；生成可导航报告——事件/令牌使用/sub-agent 活动/模型行为标签对齐在同一回合时间线；审查者快速把握运行叙事、追溯任何标签到源头回合、导出底层数据表做跨运行分析。
- **演示价值**：AI R&D 评测（1300 万 token）中把 agent 工作分成与"研究技能分类"对齐的行为阶段，揭示该运行**高度集中于运营工作与手稿生产、缺乏持续的假设生成阶段**——证明"可观测性工具能产出可审计的、超越直觉的评测结论"。

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **一手证据（FACT）**：arXiv 2610.08364（**2026-10-06 v1 / 10-08 v2**，27 页 5 图，CC-BY 4.0），作者 Toby D. Pilditch / Konstantinos Voudouris / Alexandra Abbas / Cozmin Ududec；明确标注"open source package built on **Inspect Scout**"（UK AISI 的 Inspect 生态扩展）["https://arxiv.org/abs/2610.08364"]
- **时机**：与 10-08 ThinkingBox（执行真相评测，已记日志）、10-10 AgentJudgeBench（LLM-as-Judge 可靠性，A 级卡）同属"评测可信度"热点期——Transect 补的是**评测者侧可审计性**一环，与 AgentJudgeBench（judge 侧可靠性）互补
- **活跃度**：Inspect Scout 为 Inspect（UK AISI，MIT）官方扩展轨道，生态背书强；v1→v2 仅隔 2 天（活跃修正）

## 3. 与我的连接
- **连接的项目**：**Validation 编译器**（Claim→Operationalization→Evidence→Judgment 的"证据可追溯"思想与 Transect 的"标签→源头回合"同构）；**引擎 evaluation 层**（criterion 打分 + 证据保留——可借鉴 Transect 的"评估族配置 + judge 分离 + 可导航报告"资产结构）；**silver-shield**（可信/可审计要求）
- **连接的知识点**：Agent Evaluation 能力树 B 层（执行观测/行为审计）、D 层（判定与打分）；G2 可观测性空白；五维模型 Evaluation 维度
- **潜在收益**：① 引擎 evaluation 层的证据链可升级为"回合时间线 + 标签可追溯"；② 给"评测结论可复现"提供现成工具与数据模型参考；③ 与 AgentJudgeBench 结论（judge 对齐度随难度下降）配套——长时程评测的 judge 输出必须有可追溯结构

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | https://arxiv.org/abs/2610.08364（论文）；Inspect Scout 官方（生态依赖，待定位仓库） |
| 证据等级 | **FACT**（arXiv 一手论文，作者/版本/案例数据明确） |
| 验证方式 | ① 精读论文（对照引擎 evaluation 层：回合时间线/行为标签/溯源模型能否复用）；② 如 Inspect Scout 可安装，跑最小 demo 验证"标签→源头回合"追溯；③ 与 AgentJudgeBench 结论并读，形成"评测可信度双环"（judge 可靠性 + 审计可追溯）验证小结 |
| 预期完成时间 | 2026-10-16（Evaluation 周周五验证窗口，与 AgentJudgeBench 精读并列） |

## 5. 验证结果
> **周五验证（2026-10-16，arXiv v2 摘要精读核验）**：
> - **版本核验**：arXiv 2610.08364 v1（10-06）→ v2（10-08，修正通讯作者地址 typo），27 页 5 图，CC-BY 4.0；作者四人（Toby D. Pilditch 等）
> - **Inspect Scout 生态确认**：摘要原文"open source package built on Inspect Scout"——UK AISI Inspect 官方扩展轨道背书（MIT）
> - **方法确认**：evaluation-family configuration（任务上下文+行为词汇表复用）→ judge 模型与分析设置分离提供 → 可导航报告（事件/token/子代理活动/行为标签对齐到统一回合时间线）→ 标签/事件追溯源头回合 → 导出数据表跨运行分析
> - **演示案例核验**：AI R&D eval 近 1300 万 token；行为阶段划分显示"集中于运营工作与手稿生产、缺乏持续假设生成阶段"
> - **对引擎 eval 层结论**：① 证据链可升级为"回合时间线 + 标签可追溯"数据模型（Validation 编译器 Claim→Evidence→Judgment 同构）；② "评测结论可复现"需要 judge/分析设置与任务上下文分离的资产结构；③ 未定位到公开仓库 URL，未达 validated 门槛（工具可复现性待验证）
> - **三环对比定位**：评测者/transcript 审计环（vs AgentJudgeBench judge 侧 / TestJack 补丁侧）

## 6. 决策
- [ ] 晋升 validated（缺公开仓库复现验证）
- [x] 维持观察（数据模型已验证可借鉴，工具复现留待后续）
- [ ] 拒绝（原因）
