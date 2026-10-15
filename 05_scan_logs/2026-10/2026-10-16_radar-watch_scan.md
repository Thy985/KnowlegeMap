# 验证日志 · 2026-10-16（Personal Tech Radar · Evaluation 周 Day5 · 周五验证）

> 周五分工：对 2-3 个高价值候选做实际验证/对比。本次验证 3 张候选卡：AgentJudgeBench / Transect / TestJack（三环对比）。

## 验证方式
- arXiv 一手摘要精读核验（TestJack 2610.10619、Transect 2610.08364 v2），确认作者/版本/量化证据/方法细节
- 与引擎 evaluation 层（criterion 打分 + 证据保留）做落地对照
- 与 DeepSeek Harness validated 卡（沙箱/凭据/可观测 seam）对照评测隔离设计

## 验证结论：评测可信度三环

| 环 | 对象 | 审计对象 | 核心量化证据 | 能力树层 |
|---|---|---|---|---|
| judge 侧 | AgentJudgeBench（A） | LLM-as-judge 对齐度 | 对齐度随难度单调下降；无 GT 退化快 1.5x；喂 GT 反损 | D1/D3 |
| 评测者/transcript 侧 | Transect（A） | 评测者推断的可复现/可审计性 | 1300 万 token AI R&D 案例；回合时间线+标签溯源 | B2/B4 |
| 补丁/测试侧 | TestJack（A） | 固定测试是否真测到任务要求 | **34.4% 判正确 trial 违反要求；resolution 50.6%→33.2%** | C3/A3 |

## 关键核验增量
- **TestJack**：作者含 UC Berkeley（Koushik Sen / Dawn Song）+ Columbia（Baishakhi Ray）；6 frontier backends × 5 benchmarks（DeepSWE/SWE Marathon）；"evaluator 必须更自适应"主张；未见公开代码仓库 → 方法论可迁移、未达 validated
- **Transect**：v2（10-08）；Inspect Scout 生态（UK AISI，MIT）确认；evaluation-family configuration + judge 分离 + 可导航报告；未见公开仓库 URL → 数据模型可借鉴、工具复现留待后续
- **AgentJudgeBench**：三环对比中其结论（judge 不可靠）与其他两环（评测者不可审计、测试可 hack）互相印证——三个失真源独立量化

## 对引擎 evaluation 层的落地结论（周五产出，周六回灌）
1. **judge 校准约束**：关键结论不依赖单一 LLM 打分；程序化断言优先，LLM-judge 仅作次级信号；难度分层时 judge 可靠性预期下降，hard 任务配程序化验证
2. **证据注入受控**：喂 judge 更多信息（GT）可能反损对齐——评测设计不是"信息越多越好"
3. **可回放测试概念**：自建基准/评测引入"动态测试生成 → 只保留 GT 通过的 → 失败可回放"环节，避免固定测试被 hack（34.4% 系统性偏差）
4. **证据链数据模型**：回合时间线 + 标签可追溯（Transect 模型），与 Validation 编译器 Claim→Evidence→Judgment 同构
5. **评测隔离设计**：DeepSeek Harness 的 sandbox/approval/credentials seam 是运行时隔离，eval 层还需 fail-closed 网络策略（对照 10-11 事件：网络/凭据/外部目标三隔离）——周六回灌时补入能力树 C1/C4

## 去重确认
- 三环对象均已建卡，本次只做验证回填，无新卡
- 未大规模扩展搜索（仅 2 篇 arXiv 精读 + 本地对照）

## 结论
**Important**（周五验证闭环：三环对比完成，引擎落地建议 5 条产出；候选卡维持观察，周六回灌）。
