# 周日小结日志 · 2026-10-18（Personal Tech Radar · Evaluation 周 Day7 · 小结+换域）

> 周日分工：本周领域小结，判断是否换域（换不换标准 = "候选→验证→回灌"闭环是否完成）。

## 本周小结（Evaluation / Observability，2026-10-12 ~ 10-18）
### 产出清单
- **能力树/基线**：`08_agent_centric/domains/agent-evaluation.md`（A-E 五层 + 基线三表 + §六回灌）
- **候选卡 8 张（领域内/相邻）**：AgentJudgeBench（A，10-10 过渡期建）、Transect（A，10-13）、求索 4.0（A，10-14）、ReviewBench（A，10-14）、TestJack（A，10-15）、LiveMACE（B+，10-15）；领域外兜底另建 Protocol Pivoting（10-13）、MXC（10-14）、ToFu（10-15）
- **验证（10-16）**：评测可信度三环对比闭环——judge 侧（AgentJudgeBench：对齐度随难度下降/无 GT 退化 1.5x/喂 GT 反损）｜评测者侧（Transect：1300 万 token 案例/回合时间线+标签溯源）｜补丁测试侧（TestJack：34.4% 判正确违规/50.6%→33.2%）
- **回灌（10-17）**：三环→能力树 A3/C3/D1/B2；评测隔离 C1/C4 落地检查（运行时隔离已有，eval 层需 fail-closed 网络策略+凭据注入白名单）；引擎 eval 层建议 5 条；graph 补 5 边；connections 增 6 条

### 核心结论（可复用）
1. **评测可信度三环**：LLM-judge 可靠性、评测者/transcript 可审计性、补丁/测试侧审计，三者缺一不可——单一 LLM 打分不可作为关键结论唯一依据
2. **eval 层隔离**：agent 运行时隔离（sandbox/credentials seam）≠ 评测隔离；eval harness 默认 fail-closed（不出网）
3. **引擎落地 5 条**：judge 校准约束 / 难度分层 / 证据注入受控 / 可回放测试 / 评测隔离——待引擎实现阶段执行

### 闭环判断
- 候选 ✅ → 验证 ✅（实际对比取证）→ 回灌 ✅（index/connections/能力树全落）
- **核心方法论闭环完成**；3 卡维持观察（缺公开代码仓库复现）属正常生命周期，跨周跟进；求索 4.0 参照系、LiveMACE 动态评测 → 后续周

## 换域判断：**换域 → Harness / 治理**
- 理由：闭环已完成；领域顺序建议下一站 = Harness/治理；待验证素材（求索 4.0 参照系、评测隔离设计）与 Harness/治理周天然衔接（评测隔离即治理的一部分）
- **下周（2026-10-19 周一起）：Harness / 治理**——周一建能力树/基线
- 历史记录：见 current_focus.md 历史聚焦记录表

## 结论
**Important**（Evaluation 周闭环收官，换域 Harness/治理；下周一起进入新领域）。
