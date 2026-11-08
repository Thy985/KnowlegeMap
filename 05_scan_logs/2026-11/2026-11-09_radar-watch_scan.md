# Personal Tech Radar 深耕扫描日志 · 2026-11-09（周一 · Memory 周 Day1）

> 任务类型：周一建领域能力树/基线（不追增量、不做新检索轰炸）。
> 输入：`07_radar_watch/current_focus.md`（Memory 周目标 6 项）、`03_expansion_queue/candidates/[cand]agent-memory-2026.md`（S 卡）、Runtime 能力树 §八（执行状态 ≠ 会话记忆）。

## 1. 动作
- 新建 `08_agent_centric/domains/agent-memory.md`：七层领域树（A 记忆分层 / B 写入策略 / C 检索与压缩 / D 生命周期 / E 作用域隔离 / F 信任边界 / G 与执行状态分界）。
- 基线锚点表：Mem0、Zep-Graphiti、Letta、A-MEM、MemEval、平台内置（Anthropic /mnt/memory、AgentCore Memory、MS AF Cosmos、Vercel eve、Grok Build）、文件/Git-native（OKF、Mem0×dsh）、学术新线（EnSIMem/SEEM/Synapse/Jev-Mem/Mem++/DyadMem/RealCompanion/Below-the-Prompt）。
- 缺口 6 项，优先级：基准口径核验 S、注入/污染防御 S、写入策略对照 A、作用域隔离 A（含 TeamMind 缺口④）、生命周期 B、执行状态共存 B。
- 更新 `current_focus.md` 周一进度；更新 `06_expansion_index/README.md` 与 `_INDEX.md`。

## 2. 基线判断（本周起点）
1. 记忆是六个可独立失败的面，不是单一检索库。
2. 基准分数有三重口径差（平台 vs SDK、自报 vs 独立复测、合成 vs 真实对话），选型前必须固定口径。
3. 路线三分：抽取简化（Mem0 去图）/ 时序图（Zep）/ 文件仓库（Anthropic、Grok、OKF）；文件路线与 KnowlegeMap 同构。
4. 记忆即攻击面：写入=潜在后门，必须有来源标注、审计、删除权。

## 3. 未做（按计划留到后续）
- 周二~四增量扫描；周五 Mem0/Graphiti/Letta 实测与基准口径核对；周六回灌。

## 4. 结论
**New**：Memory 能力树建立，六层基线 + 6 缺口可验证；本周闭环路径明确。
