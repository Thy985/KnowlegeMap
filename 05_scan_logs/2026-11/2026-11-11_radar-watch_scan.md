# Personal Tech Radar 深耕扫描日志 · 2026-11-11（周三 · Memory 周 Day3）

> 任务类型：只追增量（新 release / 新工具 / 相邻项目）。当前领域 Memory。

## 检索
三路 `general_search`（minimum）+ 全库 `grep -a -ril` 去重（OpenViking / StreamMemBench / MEMTIER / Zep Agent Skills / Zep v4 / me0）。

## 判定
| 对象 | 等级 | 判定 |
|---|---|---|
| **StreamMemBench**（arXiv 2606.14571） | **A** | 并入 S 卡；升为基准批判第 5 条「存储≠会用」 |
| **Zep v4 Context API**（10-14）+ **Agent Skills**（11-05） | **A−** | 并入 S 卡；能力树 A4 行补程序化沉淀信号 |
| **MEMTIER**（2605.03675） | B | 并入 S 卡（Tafcm 本地路线反例参照） |
| **OpenViking**（VLDB 2026） | B | 补记（此前仅作 Hy-Memory 对照名单出现，未单独入库） |
| meko-mem0（10-26） | — | Mem0 数字翻版包装，无新机制，剔除 |
| mcp-memory-service v10.9 / -lite | — | 小工具迭代，B 级以下 |
| me0（MCP 记忆服务，consent scopes/outputSchema） | C | 素材备用，不入库 |

## 要点
- StreamMemBench 四项指标（evidence recall / initial evidence use / feedback incorporation / follow-up reuse）在 8 系统 × 2 backbone 上显示：证据已存储、反馈已局部吸收，仍无法用于后续决策。→ 记忆的最后一公里是行为闭环，LongMemEval 类 recall 基准测不到。
- Zep Agent Skills 把运行轨迹蒸馏为「已验证程序」，声称小模型接近 Opus 5.5；与 Hy-Memory 代码记忆同向 → 赛道从「存什么/怎么检索」转向「经验→可复用技能」（A4 × D3）。

## 落位
- `[cand]agent-memory-2026.md`：Day3 增量段。
- `08_agent_centric/domains/agent-memory.md`：基准批判四条→五条；A4 行补程序化沉淀信号。
- `07_radar_watch/current_focus.md`：周三勾选，周四拆分。
- 06 index 段 + `_INDEX.md` 🔁 行 + 本日志。
- **未新建候选卡、未改 connections。**

## 结论
**Changed**
