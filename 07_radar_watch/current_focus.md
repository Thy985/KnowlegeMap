# Current Focus（雷达当前聚焦领域）

> 定时任务每次运行先读本文件，确定当前领域与本周进度。换域后更新本文件。

## 当前领域：Harness / 治理（Agent 执行环境与治理）

- **周起始日**：2026-10-19（周一）
- **状态**：active（10-19 Day1 能力树/基线已建；上一领域 Evaluation/Observability 已闭环换域）
- **为什么先做它**：领域顺序建议的下一站；评测隔离设计（eval 层 fail-closed 网络策略）是治理的一部分，与上周 Evaluation 周天然衔接；命中"高效、可信、可控"的 Control 维度；与用户项目 TeamMind（多 Agent 运行时）、Tafcm（本地执行）、campus_order（OpenClaw 智能体）、silver-shield（反诈骗判定）直接相关。

## 目标
- 建立 Agent Harness / 治理能力树/基线（已知 vs 缺口 vs 相邻未覆盖）
- 发现并验证 2-3 个高价值 harness/治理工具或方法（候选方向：评测隔离落地、DeepSeek Harness 已 validated 对照、MXC 治理策略验证、MCP 安全/治理周素材）
- 闭环：候选 → 验证 → 回灌 index/connections/能力树

## 已知锚点（不重复收集）
- DeepSeek Harness（S，validated——sandbox/approval/permission-presets/credentials seam/session-telemetry）
- Microsoft Execution Containers / MXC（A 候选卡，2026-10-07 GA——OS 级 agent 策略隔离层，候选卡 44）
- Harness/Control Plane 范式（S 候选卡——Omnigent/MS Agent Framework/六职责/HarnessDev/AgentCore GA/NVIDIA Open Shell）
- Agent 防火墙/运行时防御品类（A 候选卡——Aigis/ClawKeeper/AgentGuard/Pipelock/MS AGT/Proof-of-Guardrail/Falcon Guardian）
- 引擎内 evaluation 层 + security-assessment 能力树模板（已有）
- 评测隔离设计（C1/C4 落地检查结论：eval 层需 fail-closed 网络策略+凭据注入白名单）
- 10-18 兜底移交线索：CVE-2026-96620（argv→--mcp-config 注入，补丁 7 月已发）、MS Agent Framework 1.0 GA

## 本周进度（每日分工）
- [x] 周一（10-19）：建能力树/基线（agent-harness-governance.md，A-F 六层），更新本文件 ✅
- [ ] 周二~周四（10-20~10-22）：增量扫描，写候选卡（S/A/B）
- [ ] 周五（10-23）：实际验证/对比 2-3 个高价值候选（计划：MXC 对照 / 确定性 guardrail-策略引擎对比 / 评测隔离落地核查）
- [ ] 周六（10-24）：验证结果回灌 index/connections/能力树
- [ ] 周日（10-25）：本周小结，判断是否换域（候选：Runtime，接 TeamMind）

## 换域规则
- 一周是最小驻留，不是硬切换；闭环未完成可延长到第二周。
- 下一领域（候选）：Runtime（接 TeamMind）→ Memory → Computer Use / Browser → AI Infra / 本地边缘（接 Tafcm）。

## 历史聚焦记录
| 领域 | 周起始 | 状态 | 产出 |
|---|---|---|---|
| Evaluation / Observability | 2026-10-12 | ✅ 已闭环（10-18 换域） | 能力树 agent-evaluation.md（A-E 五层+§六回灌）｜候选卡：AgentJudgeBench/Transect/求索 4.0/ReviewBench/TestJack/LiveMACE｜三环方法论+评测隔离 C1/C4+引擎 eval 建议 5 条｜graph 5 边+connections 6 条 |
| Harness / 治理 | 2026-10-19 | active（Day1 已建基线） | 能力树 agent-harness-governance.md（A-F 六层：Harness 架构/执行隔离/权限策略/运行时防御/威胁模型/评测闭环）｜已知锚点：dsh validated + Harness-ControlPlane S 卡 + MXC A 卡 + Agent 防火墙 A 卡｜周五验证计划：MXC 对照/guardrail-策略引擎对比/评测隔离落地 |
