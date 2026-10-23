# 深耕扫描日志 · 2026-10-24（Personal Tech Radar · Harness/治理 周 Day6 · 周六回灌日）

> 任务类型：周六 = 验证结果回灌（index / connections / 能力树）。本日不做增量扫描，只做回灌与落盘。

## Re-ground
- 当前领域：Harness / 治理（10-19 起）；Day1~Day5 均已完成（能力树/基线→增量→周五验证）
- 周五（10-23）验证产出：Strands Box / MXC / 事件集群 3 卡晋升 validated；agent-aegis 实测 1.0.0 维持观察；Archon CVSS 修正 4.0 9.3
- 兜底（10-23）移交 3 项领域内事件（AWS AgentCore 区域级劫持 / CERT-In 印度逃逸 / ARTEX 韩国银行）→ 作为 E6 事件基准的后续证据线参考，未单独建卡

## 回灌执行

### 1. 能力树 `08_agent_centric/domains/agent-harness-governance.md`
- **B 层**：B1 MXC 标注 **validated**（官方 GA 公告全文精读）；新增 **B5 Strands Box**（AWS 开源行为遏制沙箱，validated）
- **C 层**：C2 补 Dogwood = Cedar 语法 + 时间算子扩展（与 MXC JSON schema 对照）；C3 注明 MXC Entra agent 身份归因 coming soon 未落地
- **D 层**：D1 补 agent-aegis 1.0.0 实测状态（init/patch 可用，AGEF/AGP 厂商自述）
- **E 层**：E1 强化（Archon CVSS 4.0 9.3 + 控制面默认 fail-closed）；**新增 E6 生产越权事件基准**（10-19 事件集群，validated）+ **新增 E7 模型内因性越权**（Mythos 5 biased reasoning 79% vs 1% 量化 + BIP-44 钱包派生，机制=模型自身推理替代授权）
- 已知表：MXC / Strands Box / 事件集群 3 项 [cand] → **validated**
- 缺口节：3 项验证候选全部标记「已回灌 10-23」；保留未闭合缺口（Agent Mesh 身份层 / argv 防御清单 / TeamMind 权限模型对照）转 Runtime 周或后续
- 验证计划/回灌目标节：全部勾选完成

### 2. Capability Graph `08_agent_centric/capabilities/graph.md`
- 新增 4 条跨域边：**containment-policy**（governance↔runtime-defense↔developer-tools）、**policy-engine**（governance↔agent-evaluation↔agent-runtime）、**trust-identity**（governance↔agent-runtime↔web-security）、**runtime-guardrail**（governance↔agent-evaluation↔agent-runtime）

### 3. Connections `04_connections/README.md`
- 10-20 Day2 三条连接升级：Strands Box / 事件集群 🟡 → ✅ 已验证；agent-aegis 维持 🟡（B 级观察）
- 新增 10-24 回灌段：MXC 连接升 ✅；内因性 vs 外因性分类连接 ✅ 已回灌能力树

### 4. 候选卡决策
- **晋升 validated（3）**：strands-box-os-containment-2026 / microsoft-execution-containers-2026 / agent-containment-breach-2026（均已 ≥2 独立一手来源）
- **维持观察（1）**：agent-aegis-governance-2026（1.0.0 实测可用，但 AGEF/AGP 无独立证据）

### 5. 兜底移交事件处理
- AWS AgentCore 区域级劫持 / CERT-In 印度逃逸 / ARTEX 韩国银行：与事件集群卡同线（E6 越权事件基准），已在 10-23 兜底日志存档，本次作为证据线参考不再重复收集

## 结论
**Important**（Harness/治理 周「候选→验证→回灌」闭环完成：4 卡验证、3 卡 validated、能力树 E6/E7 节点落地、graph 4 边、connections 3 条升级）
