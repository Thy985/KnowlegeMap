# Personal Tech Radar 深耕日志 · 2026-11-15（周日，Memory 周 Day7）

> 分工：本周领域小结 + 换域判断。不追新资讯，只做审计与判定。

## 一、本周范围与产出

| 项 | 实数 |
|---|---|
| 能力树 | `agent-memory.md` **A~H 八层**（A 分层 / B 写入 / C 检索压缩 / D 生命周期 / E 作用域 / F 信任边界 / G 与执行状态分界 / H 可靠性），§一~§七 |
| 锚点 | 13 行（Mem0 / Zep→Graphiti / Hy-Memory 2.0 / Letta / A-MEM / MemEval / 平台内置 / 文件-Git / 学术新线 / SIx A / MemEvolve A− / 基准批判六条 等） |
| 判断 | 4 条 → **5 条**（新增"双向失败 / 可靠性是一等公民"） |
| 批判 | 2 条 → **6 条**（命题错位 / 存储≠会用 / 回执层） |
| 缺口 | 6 行 → **8 行**（"基准口径核验""写入策略实证"标完成；新增"可靠性落地" A、"写入/删除回执语义" B） |
| 增量 | 4 天 **8 组**，无新建碎片卡，S 卡 `[cand]agent-memory-2026.md` 持续增量 |
| 验证 | 3 项（Mem0 行为级 / EvolveLab 结构级 / Zep CE 否定结论） |
| 回灌 | 11-14 五项落点 + graph 3 边 + connections 2 行 1 注 |
| 日志 | 深耕 7（11-09~11-15）+ 兜底 7（11-09~11-14） |

## 二、三环闭合审计

| 环 | 结论 | 依据 |
|---|---|---|
| 候选环 | **完整** | 4 天增量覆盖开源框架（Hy-Memory/Mem0/Zep）、基准（StreamMemBench/MEMTIER）、工程记录（SIx）、架构搜索（MemEvolve/EvolveLab）、自报产品（OpenViking） |
| 验证环 | **不完整** | 仅 Mem0 为行为级（本地实跑，无云）；EvolveLab 为结构级（13 providers/统一接口，未跑行为）；Zep CE 为文档级否定结论；**Letta API、Graphiti 部署成本未执行** |
| 回灌环 | **完整** | H 层进树、批判 ⑤ 双证据、批判 ⑥ 回执、Zep 行修正、锚点 2 新增、缺口回填、connections/graph 落地；11-14 两次提交 `1ae9003` + `6eb4227` |

**不宣称"闭环完成"。** 严格口径：候选→验证→回灌 中，验证环只有 1/3 达标（1 行为 + 1 结构 + 1 否定）。

## 三、未闭合挂账

1. **F 层注入/污染防御（S）**——本周唯一完全未触碰的 S 级缺口，仅有事件侧证据（事件日 13 跨会话注入持久存活 / PersistBench / OWASP Agent Memory Guard），无本地复现。
2. **E 层作用域与租户隔离（A）**——承接 Runtime 缺口④（TeamMind 权限模型 vs dsh/MXC），连续两周挂账。
3. **H 层可靠性落地（A）**——设计进树，原型零代码。
4. **写入/删除回执语义（B）**——已观测 Mem0 `add()` 空回执，未系统化为写入确认协议。
5. **证据等级**：Hy-Memory 全自报、StreamMemBench 仅摘要、SIx N=1、OpenViking 自报、MEMTIER 仅摘要、EvolveLab 未跑行为。
6. **未执行验证**：Letta 三级记忆 API；Graphiti 本地部署成本（CE 前提消失）。

## 四、换域判定

**延长第二周（11-16~11-22），不换 Computer Use / Browser。**

1. 风险优先级压过覆盖率：最危险的判断（"写入即植入后门"）恰好落在唯一未验证的 S 缺口上，换域不解决它。
2. E 层连续两周挂账，制度上不能允许第三次。
3. 第二周可用确定性命中检查（非 LLM 判断）产出可复现证据——Mem0 本地栈已跑通，性质不同于第一周的采集。

## 五、第二周计划（写入 `agent-memory.md` §7.5 与 `current_focus.md`）

| 日 | 任务 |
|---|---|
| 11-16 周一 | F 层建子树 + E 层威胁模型（§八） |
| 11-17~19 | 只追增量（memory guard / PersistBench 复现件 / Graphiti×Mem0） |
| 11-20 周五 | **三项实测**：注入复现 / delete 回执一致性 / 作用域串读 |
| 11-21 周六 | 回灌 §八 + connections/graph |
| 11-22 周日 | 小结；达标换 Computer Use，未达标再议 |

> 约束：无外部 API 时按先例降级为"代码级 + 结构级"，如实标注，不得推断冒充实测。

## 六、落位动作

1. `08_agent_centric/domains/agent-memory.md` 新增 **§七**（净产出 / 三环审计 / 挂账 / 换域判定 / 第二周计划）。
2. `07_radar_watch/current_focus.md`：周日勾选 ✅；状态改"第二周延长"；新增第二周五条待办；换域记录新增 11-15 条目；历史表新增 Memory 行。
3. `06_expansion_index/README.md` 新增本日小结段（无新对象，仅判定与落点）。
4. `_INDEX.md` 新增本日志行。

## 结论

**Changed（周小结 + 判定延长第二周；0 新建卡 / 0 新对象）**
