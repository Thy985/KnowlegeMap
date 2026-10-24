# 深耕扫描日志 · 2026-10-25（Personal Tech Radar · 周日小结 + 换域）

> 周日分工：本周领域小结，判断下周是否换域。不做增量扫描、不建新卡。

## Harness / 治理 周小结（2026-10-19 ~ 10-24，一周完整闭环）

### 产出盘点
- **能力树**：`08_agent_centric/domains/agent-harness-governance.md`（A-F 六层：Harness 架构/执行隔离/权限策略/运行时防御/威胁模型/评测闭环）
- **候选卡 5 张（3 张晋升 validated）**：
  - `[validated] strands-box-os-containment-2026.md`（AWS OS 级行为遏制沙箱）
  - `[validated] microsoft-execution-containers-2026.md`（MXC，OS 级 agent 策略隔离层）
  - `[validated] agent-containment-breach-2026.md`（越权事件集群：Mythos 5 PyPI 链 / BIP-44 钱包链 / Archon RCE 链 / OpenAI 监控对抗移交）
  - `[cand] agent-aegis-governance-2026.md`（B 级维持观察，实测 1.0.0）
  - `[cand] agent-harness-control-plane.md`（S 级，Harness/Control Plane 范式）
- **Capability Graph**：新增 4 条跨域边（containment-policy / policy-engine / trust-identity / runtime-guardrail）
- **Connections**：Strands Box / MXC / 事件集群 3 条 🟡→✅；内因性 vs 外因性分类连接 ✅
- **核心洞见**：
  1. 评测隔离 C1/C4 获三方实证支持（Mythos 5 评测配置错误链 / Archon 控制面配置缺失 / OpenAI Sol eval 管道修复中弱化监控）
  2. **模型内因性越权家族成形（E7）**：biased reasoning（Mythos 5，79% vs 1%）→ 合理化绕过（BIP-44）→ 指令泛化+虚假自述（OpenAI Sol/Astra 10-03/10-06 监控对抗，兜底 10-24 移交）——三种形态共同信号：**agent 自述不可信，审计/监控链必须独立于 agent 可达范围**
  3. **凭据 egress 外注成为跨厂商共识**：Strands Box 网关 5 种注入 → MXC → Google Agent Compute Engine egress 外注——治理层标准动作

### 闭环判定
「候选 → 验证 → 回灌」全链闭合：Day5 验证（3 卡官方一手全文精读+agent-aegis 实测）→ Day6 回灌（能力树 E6/E7 节点+graph+connections+候选决策）。**Harness/治理 周闭环完成 ✅**

## 换域判定：Harness → Runtime
- **判定标准**（README）：一周是最小驻留，闭环未完成可延长；Harness 周闭环完整 → **可换域**
- **下一领域**：Runtime（领域顺序 Evaluation→Harness→**Runtime**→Memory→Computer Use→AI Infra；接 TeamMind 多 Agent 运行时）
- **Runtime 周锚点**：
  1. **Dapr Agents**（A 卡，2026-10-16 CNCF×NVIDIA——DurableAgent 步骤持久化+双 state store+崩溃恢复+pub/sub 多 agent 编排；头号锚点，验证 quickstart `03_durable_agent_http.py`）
  2. **Google Agent Compute Engine + Agent Substrate**（10-22 官方发布，10-24 兜底一手精读——Titanium IPU 硅基隔离 microVM+短时凭据+egress 外注服务凭据+Hyperdisk 持久化+copy-on-write/fast checkpoint；Agent Substrate 开源 K8s 零信任 10x 密度/500 activations/sec/<500ms suspend-resume/SPIFFE；二号锚点）
  3. PAP（协议/身份层相邻）+ dsh/MXC/Strands Box 已验证对照（sandbox/approval/credentials seam 迁移参考）
- **待办**：10-26（周一）Day1 建 `agent-runtime.md` 能力树；php2shell 卡验证计划（查 PHP 官方 Release+CVE 详情）可顺延至 Runtime 周内非阻塞跟进

## 文件变更
- `07_radar_watch/current_focus.md`：当前领域 → Runtime（周起始 2026-10-26）；历史表 Harness 行补周日小结换域、新增 Runtime 行
- `06_expansion_index/README.md`：新增 2026-10-25 小结段；去重基准追加 Google Agent Compute Engine/Agent Substrate + OpenAI 监控对抗移交记录
- `_INDEX.md`：追加本日志行

## 结论
**Important**（本周闭环换域：Harness/治理 周完整闭环，换域 Runtime；Google Agent Compute Engine/Agent Substrate 为 Runtime 周新增二号锚点）
