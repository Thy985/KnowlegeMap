# Personal Tech Radar 深耕日志 · 2026-11-17（周二，Memory 第二周 Day2）

> 分工：只追增量。今日主题自然收敛为 **F 层防御的良性代价**——11-16 建了 8 层防御栈，今天补上"这些防御在没攻击时做了什么、代价多少"。

## 一、检索
- 3 路 `general_search`（Memory 框架 release / memory poisoning 论文 / memory benchmark 与平台）+ 3 篇 arXiv 摘要级 `web_fetch`（2611.09721、2609.22818、2606.04329）。
- 全库 `grep` 去重：MemoryDojo / MemPoison / Price of Safety / MemMorph / DolphinBench / Cognee / AMA-Bench 均未命中；Mem0、Letta、Graphiti 旧行已存在，仅取新事实。

## 二、判定表

| # | 对象 | 关键事实 | 判定 |
|---|---|---|---|
| 1 | **The Price of Safety**（arXiv 2609.22818 v3，11-04 修订） | 半份 LoCoMo（5 段 / 750 轮 / 255 问，每条件 3 次）；sanitization 与 provenance **零触发**；LLM 异常检测 **9/2,250（0.4%）**；读时 reranker 丢 **2.2%** 记忆、**14.9% 问题少一条**、盲审 50 条仅 2 条合理；token +0/1.5/3.0/4.5%；准确率无显著变化；v3 主动修正 v2 模型错配 | **A｜锚点 + §8.6** |
| 2 | **MemoryDojo**（arXiv 2611.09721，11-06） | 155 条多会话轨迹 / 4 领域 / **5 个记忆系统**；全部可被污染，下游影响随架构显著不同；memory-aware poison 优化可提升效果 | **A−｜锚点合并** |
| 3 | **From Untrusted Input to Trusted Memory / MPBench**（arXiv 2606.04329 v2） | 4 条写入通道、9 个结构性弱点、6 类攻击；**写入/检索越激进越易被利用**；现有 prompt-injection 防御覆盖不到记忆污染 | **A−｜锚点合并** |
| 4 | **MemPoison**（ACM CCS 2026，11-14） | 既有攻击假设"直接落库"，忽略选择性抽取/改写；本文专攻该环节植后门 | **A−（未读全文）｜卡内记为待核** |
| 5 | **MemMorph**（二手评述） | 污染长期记忆以劫持**工具选择**（benign vs poisoned CoT），穿过记忆更新存活 | B+｜只记日志 |
| 6 | **DolphinBench**（Mem0 首页） | 厂商自建 benchmark，主张测"agent 在真实任务上是否按记忆行动" | B｜只记日志（厂商自报，方法论未读） |
| 7 | Memos 26.11.1 / Cognee 1.2.2.dev4 / AMA-Bench | Memos 是笔记应用（同名不同物）；Cognee、AMA-Bench 未构成新方向 | 不写 |

## 三、落位
1. `agent-memory.md`：锚点表新增 1 行（F 层防御代价集群）；缺口表新增「防御的良性代价与误伤率」（A）；**新增 §8.6**（防御真实代价表 + 对 8.2 的三条修订 + 项目落点补充）。
2. S 卡 `[cand]agent-memory-trust-boundary-2026.md` 新增 **§5.1**（5 项证据 + 4 条含义 + 验证计划加观测项）。
3. 06 index / connections / _INDEX / 本日志。

## 四、核心判断
1. **零触发 ≠ 有效**：sanitization 和 provenance 在 750 轮良性流量里一次没动，最可能的解释是没接进执行路径或恒判良性——这类防御不能计入"已防护"。
2. **读时按相关性删记忆会伤良性请求**：2.2% 丢弃导致 14.9% 问题少一条，盲审只有 4% 的丢弃站得住。scope/ownership gate 只判归属才有稳定收益（MemLeak 1.4ms 恢复 1.00/5 是正例）。
3. **攻击效果与架构强绑定**：MemoryDojo 跨 5 个系统差异显著，Trojan Hippo 的 85–100% 不能外推；换后端必须重测。
4. **写入门控可被绕过但成本更高**：MemPoison 说明选择性抽取不是免费防线，但绕过难度高于直接注入——方向对，不能宣称闭环。
5. **防御指标要成对报告**：ASR + 良性触发率 + 扣留率 + token 开销；只报 ASR 的防御视为未评估。

## 五、限制
- 全部为 arXiv 摘要级 / 二手评述，未读全文、未复现；MemPoison 仅 ACM 摘要片段；DolphinBench 仅官网一句话。
- Price of Safety 的样本是半份 LoCoMo（对话型），不是 agent 长程轨迹，外推到 Tafcm/TeamMind 需保留折扣。

## 结论
**Changed**（新增 A 级锚点与 §8.6，改写防御验收口径；无新建卡）
