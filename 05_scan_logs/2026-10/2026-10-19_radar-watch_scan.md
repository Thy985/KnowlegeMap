# 深耕扫描日志 · 2026-10-19（Personal Tech Radar · Harness/治理 周 Day1 · 建能力树/基线）

> 周一分工：建该领域能力树/基线，对照 Tech Map 标注已知 / 缺口 / 相邻未覆盖；更新 current_focus.md。

## 本次动作
1. **Re-ground**：读取 01_personal_tech_map.md（Agent Systems ★★★★★ / Control 维度 / G1 安全缺口）、02_knowledge_gap_map.md、03_project_landscape.md（TeamMind 需 MCP/A2A、dsh-pentest 空壳）、06_expansion_index/README.md 去重基准。
2. **核对既有锚点**（不重复收集）：[val]deepseek-harness（S，源码级）、[cand]agent-harness-control-plane（S，Omnigent/MS AGT/六职责/HarnessDev/AgentCore GA/NVIDIA Open Shell）、[cand]microsoft-execution-containers（A，MXC GA）、[cand]agent-firewall-runtime-defense（A，Aigis/ClawKeeper/MS AGT/Proof-of-Guardrail/Falcon Guardian）、[cand]browser-harness（A，留 Computer Use 周）、Evaluation 周评测隔离 C1/C4 回灌。
3. **建能力树**：`08_agent_centric/domains/agent-harness-governance.md`（A-F 六层）：
   - A. Harness 架构与范式（A1 插件化 dsh / A2 Meta-Harness / A3 六职责 / A4 托管 harness / A5 自我演化）
   - B. 执行隔离与沙箱（B1 MXC OS 级 / B2 云沙箱 / B3 双层策略 / B4 三模式渐进）
   - C. 权限与策略治理（C1 能力 seam 权限集 / C2 无状态策略引擎 / C3 身份信任 / C4 最小权限）
   - D. 运行时防御（D1 确定性 guardrail / D2 运行时防火墙 / D3 端点 AIDR / D4 可证明治理 / D5 MS AGT）
   - E. 安全事件与威胁模型（E1 argv 注入 / E2 网关凭据 / E3 MCP 信任边界 / E4 事件生命周期 / E5 合规映射）
   - F. 评测 × 治理闭环（F1 评测隔离 / F2 HarnessDev 基准 / F3 治理回灌 / F4 Agent SRE）
4. **更新 current_focus.md**：状态 scheduled → active，勾选周一，补已知锚点（含 10-18 兜底移交线索 CVE-2026-96620 / MS Agent Framework 1.0），记录周五验证计划。

## 本周缺口（Harness 周重点，来自基线 §二）
- A 级：MXC 实测（Linux Bubblewrap 后端/JSON 策略 schema）、无状态策略引擎/确定性 guardrail 对比实测、评测隔离落地核查（引擎 eval fail-closed）
- A/B 级：Agent Mesh 认证身份层（TeamMind 互信）、argv 注入防御清单、TeamMind 权限模型 vs dsh/MXC 对照

## 周五验证计划（10-23）
1. MXC 实测/对照（候选卡 44 验证项）
2. 确定性 Guardrail / 策略引擎对比（Aigis 或 MS AGT）
3. 评测隔离落地核查（承接 Evaluation 周 6.2/6.3-5）

## 结论
**Important**（Harness/治理 周 Day1：能力树/基线已建，领域正式 active，周五验证计划就绪）。
