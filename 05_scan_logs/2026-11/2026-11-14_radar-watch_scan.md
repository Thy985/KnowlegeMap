# Personal Tech Radar 回灌日志 · 2026-11-14（周六，Memory 周 Day6）

> 分工：周六把本周验证结果回灌 index / connections / 能力树 / graph。**不追新资讯**（本周增量已在 Day2~Day5 收口）。

## 回灌动作（7 项）

| # | 动作 | 依据 | 落点 |
|---|---|---|---|
| 1 | 能力树新增 **H 层 子系统可靠性/可观测性**（H1 健康门 / H2 心跳 / H3 降级诚实 / H4 静默腐化防护 / H5 告警预算） | SIx Harness（arXiv 2609.05510）：11 项健康门、每 hook 心跳、`MEMORY-HEALTH: 11/11 GREEN`、85 次失败零静默、告警疲劳预算 | `agent-memory.md` §一 树 + §四 判断 5 |
| 2 | 基准批判 ⑤ 并入 SIx「retrieved-but-unused」作第二独立证据 | StreamMemBench（合成基准，8 系统×2 backbone）+ SIx（8 个月真实工作流）两条互不依赖的链 | §二 批判行 ⑤ |
| 3 | 新增批判 ⑥「口径穿透到回执层」 | 11-13 实测：`add()` docstring 承诺返回写入结果，实测 `{"results": []}`，而 `get_all` 有 2 条 | §二 批判行 ⑥；缺口表 |
| 4 | Zep 锚点行修正 | CE 公告 2024-09-26、FAQ「deprecated and no longer supported」、`getzep/zep` 自述"不是 Zep 产品" | §二 Zep 行（状态改"CE 开源判定已作废"） |
| 5 | 新增锚点 SIx Harness（A）、MemEvolve/EvolveLab（A−）；Mem0 行补本地实测 | 11-12 增量 + 11-13 验证 | §二 锚点表 |
| 6 | 缺口表：两行改"已完成"，新增"可靠性落地"A 与"回执语义"B | 同上 | §二 缺口表 |
| 7 | connections 新增 2 行 + Zep 修正注 | Mem0 本地可跑（Tafcm/TeamMind/silver-shield 三个连接面）、EvolveLab 作对照台 | `04_connections/README.md` |

## 能力树新增 H 层的理由（为什么它不是运维附录）
SIx 的四类失败里，前三类（知识丢失 / 重复劳动 / 上下文退化）都能靠改策略缓解，只有第四类**静默记忆死亡**不行——索引、embedding 服务、hook 管道悄悄坏掉，而所有人继续信任它。这类失败不会出现在任何 benchmark 上，也不会被"再调一次检索参数"发现。所以可靠性必须是能力树的一层，而不是上线后才补的监控：健康门要在启动时说话，心跳要让"该发生却没发生"成为可检测事件，降级要诚实（向量腿坏了就降 BM25，不要假装还在语义检索）。

## 判断变化（相对本周起点）
1. **Mem0 从"抽取式代表"变为"可本地跑但回执不可信"**：能力边界清楚了（单遍 ADDITIVE、无图、TTL 可用），但写入确认必须绕开 `add()` 返回值。
2. **Zep 从"A− 新开源"降为"B 观察"**：CE 已 deprecated，开源线只剩 Graphiti（Neo4j 5.26+/FalkorDB + Redis 自建成本未实测）。
3. **"存储≠会用"从单证据变双证据**：合成基准 + 真实工作流独立指向同一结论，可信度上升。
4. **新增一条工程约束**：记忆系统的可靠性可被确定性检测（健康门/心跳/覆盖率/回执一致性），不需要 LLM 参与——这直接可给 silver-shield 当检测项。

## 未回灌 / 挂账
- Letta 三级记忆 API 实测（时间不足）——**未执行**。
- Graphiti 本地部署成本实测——**未执行**（CE 前提消失后改为评估 Graphiti）。
- EvolveLab 行为验证（需 API keys + GAIA/WebWalkerQA/xBench）——**仅结构验证**。
- SIx Harness / MemEvolve 源码级核对——**未做**；SIx 为 N=1 自报，作者自陈无对照组。

## 结论
**Changed**
