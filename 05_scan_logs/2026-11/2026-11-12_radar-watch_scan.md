# Personal Tech Radar 深耕扫描日志 · 2026-11-12（00:30，Memory 周 Day4）

> 任务类型：周四，只追增量（ nuevos release / 新工具 / 相邻项目）。不做全量重扫。

## 检索
三路 `general_search`（minimum：记忆开源新发布 / Letta 更新 / MCP 记忆生态）+ 2 次 `web_fetch` 全文（arXiv 2609.05510、arXiv 2512.18746）+ `grep -a -ril` 去重（SIx Harness / MemEvolve / EvolveLab / OMEGA / claude-mem / silent memory / MemoryGraph，全部未命中）。

## 判定
| 对象 | 等级 | 判定 |
|---|---|---|
| **SIx Harness《Memory as Infrastructure》**（arXiv 2609.05510，2026-08，MIT） | **A** | 并入 S 卡 Day4 段（不新建卡） |
| **MemEvolve + EvolveLab**（arXiv 2512.18746，2025-12） | **A−** | 并入 S 卡 Day4 段 |
| OMEGA 白皮书（TTL 结构化遗忘，自报 #1） | B | 记日志 |
| mcp-memory-service v11.0.0 / MemoryGraph v0.11.13 / MemoryMesh v0.4.0 | B/C | 记日志，不写 |
| heropen 1.7.24 / TencentDB Agent Memory / neo.mjs | — | 剔除（非本周增量 / 早于时间窗 / 非记忆系统） |

## 要点
- SIx 的**四类失败**比任何基准分数都更接近真实使用：知识丢失（compaction 摘要掉"为什么"）、重复劳动（三个会话重复提议已建成子系统，文档就在上下文里）、上下文退化（多注入 → 通道变成学到的噪音）、**静默记忆死亡**（索引/embedding/hook 悄悄坏掉而无人知）。作者主张：第④类才是元失败。
- 可靠性层三件套：**11 项健康门**（每次会话开始一行 `MEMORY-HEALTH: 11/11 GREEN`，全部判定为阈值算术、不让模型参与）、**每 hook 心跳**（不触发也是一种失败，缺席会被转成 RED，包括门自己的缺席）、**告警疲劳预算**（冷启动 embedding 不算故障、未接入的可选集成不报红）。
- anti-recurrence store 的**拒绝率是设计**：154 决策 / 186 死路，只有 59 / 47 经 triage 入册——"什么都收"的反重复库会变成第③类噪音通道。
- injection 采用**确定性门控**（意图门 → IDF 罕见词门 → 会话阻尼），理由是零延迟 + 每个判定可由 IDF 算术重建；默认静默，注入要"按读者注意力计费"。
- 「retrieved-but-unused」被点名为真实工作流里的失败子模式 → 与 11-11 的 StreamMemBench（基准批判⑤）互为独立佐证：**存储与检索都不是最后一公里，行为闭环才是**。
- MemEvolve：记忆架构无全局最优，需按任务域元进化；EvolveLab 把 12 个系统统一到 Encode/Store/Retrieve/Manage 四模块 + 同一基准，**周五验证可直接用作对照台**，比拼三份厂商 SDK 更可控。

## 证据限制
- SIx 为 **N=1、无对照组、自报**，作者明确标注；78,933 / 85 / 零误报等数字均由作者自述（有 numbers appendix 查询口径）。
- MemEvolve 为 2025-12 论文（非本周新发布，属补记），成绩为作者自报，未独立复测。
- OMEGA 的"#1 排名"为白皮书自报，未取得排名口径。
- SIx / MemEvolve 均未做源码级核对（周五如选 EvolveLab 对照台再 clone）。

## 落位
- `[cand]agent-memory-2026.md` Day4 段（插在 `## 2. 与我的知识/项目关系` 之前）。
- 06 index Day4 段、`_INDEX.md` 🔁 行、`current_focus.md` 周四勾选 + 周六回灌待办。
- 能力树 `agent-memory.md` **未改**（可靠性/可观测性层留到周六回灌统一落位）。
- 未新建卡、未改 connections。

## 结论
**Changed**
