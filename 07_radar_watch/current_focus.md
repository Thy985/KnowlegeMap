# Current Focus（雷达当前聚焦领域）

> 定时任务每次运行先读本文件，确定当前领域与本周进度。换域后更新本文件。

## 当前领域：Evaluation / Observability（评估与可信验证）

- **周起始日**：2026-10-12（周一）
- **状态**：active（2026-10-12 起按每日分工执行；10-09~10-11 维持通用全量扫描已结束）
- **为什么先做它**：横向能力，TeamMind / silver-shield / agent-attention / 引擎自身都需要；命中"高效、可信、可控"；已有 validated 锚点，能从已知向相邻空白扩展。

## 目标
- 建立 Agent Evaluation 领域能力树/基线（已知 vs 缺口 vs 相邻未覆盖）✅ 2026-10-12
- 发现并验证 2-3 个高价值评估/可观测工具或方法（验证计划：AgentJudgeBench 精读 / 评测隔离设计落地检查 / promptfoo Agent Evals 扩展实测）
- 闭环：候选 → 验证 → 回灌 index/connections/能力树

## 已知锚点（不重复收集）
- promptfoo（S，validated）
- DeepSeek Harness（S，validated）
- 引擎内 evaluation 层（criterion 打分 + 证据保留）

## 本周进度（每日分工）
- [x] 周一（10-12）：建能力树/基线，更新本文件 → **能力树已建：08_agent_centric/domains/agent-evaluation.md**（领域树 A-E 五层 + 基线三表 + 周五验证计划）
- [x] 周二（10-13）：增量扫描，写候选卡
- [x] 周三（10-14）：增量扫描，写候选卡 → **求索 4.0（A）+ ReviewBench（A），候选卡 41→43；记日志：OTel GenAI 生态增量/MCP 可观测性增量/Jaeger 演进**
- [x] 周四（10-15）：增量扫描，写候选卡 → **TestJack（A）+ LiveMACE（B+），候选卡 44→46；评测可信度双环→三环；记日志：CloudWatch Omni/LangSmith AI Search/阿里 AgentLoop 等**
- [x] 周五（10-16）：实际验证/对比 2-3 个候选 → **三环对比完成（AgentJudgeBench judge 侧 / Transect 评测者侧 / TestJack 补丁侧），TestJack 核验 34.4% 判正确 trial 违规 / 50.6%→33.2%；引擎 eval 层落地建议 5 条；候选卡验证结果已回填，均维持观察**（日志：05_scan_logs/2026-10/2026-10-16_radar-watch_scan.md）
- [ ] 周六（10-17）：回灌 index/connections/能力树（待回灌：三环方法论 → 能力树 A3/C3/D1/B2；评测隔离 C1/C4 落地检查；引擎 eval 层建议）
- [ ] 周日（10-18）：本周小结，判断是否换域（候选：Harness/治理；待验证素材：求索 4.0 参照系、评测隔离设计）

## 换域规则
- 一周是最小驻留，不是硬切换；闭环未完成可延长到第二周。
- 下一领域（候选）：Harness / 治理 → Runtime（接 TeamMind）。

## 历史聚焦记录
| 领域 | 周起始 | 状态 | 产出 |
|---|---|---|---|
| Evaluation / Observability | 2026-10-12 | active | 能力树/基线：08_agent_centric/domains/agent-evaluation.md（10-12）｜ 待：增量→验证→回灌 |
