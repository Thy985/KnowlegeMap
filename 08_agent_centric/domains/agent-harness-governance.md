# Domain Tree · Agent Harness / 治理（Agent 执行环境与治理）

> 建立：2026-10-19（周一，Harness/治理 周第一天）｜ 类型：领域能力树/基线
> 定位：命中"高效、可信、可控"的 **Control 维度**；承接 Evaluation 周评测隔离设计；直接对应 TeamMind（多 Agent 运行时）、Tafcm（本地执行）、campus_order（OpenClaw 智能体）、silver-shield（反诈骗判定）。
> 树与图分工：本文件是 **Tree**（层级组织与任务分解）；跨域复用/依赖见 `08_agent_centric/capabilities/graph.md`（Capability Graph）。
> JIT 原则：不建百科，只展开与任务相关、且当前缺失的分支。

## 一、领域树（Agent Harness / 治理）

```
Agent Harness / 治理
├── A. Harness 架构与范式（Harness Architecture）
│   ├── A1. 插件化 Harness（Everything is a plugin：DeepSeek Harness / Cordis 内核，能力 seam 三角色）
│   ├── A2. Meta-Harness / Control Plane（Omnigent：组合多 harness + 控制面策略 + 共享会话）
│   ├── A3. Harness 六职责分解（observation / context / control / action / state / verification）
│   ├── A4. 托管 Harness 即服务（Bedrock AgentCore GA、MS Agent Framework 1.0）
│   └── A5. Harness 自我演化（JIT-Agent / HarnessDev / Ecdysis：harness 生成·训练·演化）
├── B. 执行隔离与沙箱（Containment）
│   ├── B1. OS 级执行隔离（MXC：五策略域 × 四后端——AppContainer/Seatbelt/Bubblewrap/MicroVM）
│   ├── B2. 云沙箱（E2B 类，与本地 MXC 互补）
│   ├── B3. 双层策略（workload 声明 + 组织 Intune 策略叠加）
│   └── B4. 三运行模式渐进（Learning → Permissive → Enforcement，最小权限起草流程）
├── C. 权限与策略治理（Permission & Policy）
│   ├── C1. 能力 Seam 权限集（sandbox / approval / permission-presets / credentials seam）
│   ├── C2. 无状态策略引擎（YAML / OPA Rego / Cedar；MS AGT <0.1ms p99；控制外置）
│   ├── C3. 身份与信任（Agent Mesh：DID + Ed25519、Inter-Agent Trust Protocol、动态信任评分）
│   └── C4. 最小权限落地（EP-002 Permission Is Security Boundary 的工程化）
├── D. 运行时防御（Runtime Defense）
│   ├── D1. 确定性 Guardrail（无 LLM 判定：Aigis / Guardian / AI Protector）
│   ├── D2. 运行时防火墙（AgentGuard 三层 Prompt/Tool/Command；Pipelock 流量扫描 + 签名 receipts）
│   ├── D3. 端点 AIDR（CrowdStrike Falcon Guardian、MS Defender endpoint agent runtime）
│   ├── D4. 可证明治理（Proof-of-Guardrail TEE attestation；硬件可信根）
│   └── D5. 治理工具箱（MS Agent Governance Toolkit：Agent OS / Mesh / SRE / Compliance / Marketplace）
├── E. 安全事件与威胁模型（Threat & Incident）
│   ├── E1. 参数注入类（CVE-2026-96620 argv→--mcp-config；CVE-2026-14540 Protocol Pivoting）
│   ├── E2. 网关 / 凭据层（10-11 七平台 gateway 凭据批量披露；CVE-2026-108586 tag-scope 绕过）
│   ├── E3. MCP 信任边界（ToFu：schema-valid 参数必须视为不可信）
│   ├── E4. 事件生命周期管理（Aigis：威胁自动建 incident + 全时间线）
│   └── E5. 合规映射（EU AI Act / HIPAA / SOC2 / OWASP 10 证据收集）
└── F. 评测 × 治理闭环（Eval × Governance）
    ├── F1. 评测隔离（eval 层 fail-closed 网络策略 + 凭据注入白名单——承接 Evaluation 周 C1/C4）
    ├── F2. Harness 评测基准（HarnessDev：LLM 能否创建/演化自己的 harness）
    ├── F3. 治理回灌（audit trails → 策略调整 → 最小权限收敛）
    └── F4. Agent SRE（SLO / 熔断 / 混沌工程；kill switch）
```

## 二、基线：已知 vs 缺口 vs 相邻未覆盖

### 已知（系统已覆盖，不重复收集）
| 锚点 | 状态 | 说明 |
|---|---|---|
| DeepSeek Harness (dsh) | **validated**（源码级，S） | 插件化 harness + 能力 seam 三角色 + sandbox/approval/credentials/session-telemetry-otel；v0.2.1-alpha.1（10-03） |
| Harness / Control Plane 范式 | [cand] **S** | Omnigent + MS Agent Framework + 六职责论文 + HarnessDev/AgentAO + AgentCore GA + NVIDIA Open Shell + Tokenomics（agent-harness-control-plane.md） |
| Microsoft Execution Containers / MXC | [cand] **A** | OS 级策略隔离层 GA（10-07），五策略域/四后端/三模式；候选卡 44 |
| Agent 防火墙 / 运行时防御品类 | [cand] **A** | Aigis/ClawKeeper/AgentGuard/Pipelock + MS AGT + Proof-of-Guardrail + Falcon Guardian/Arcjet（agent-firewall-runtime-defense-2026.md） |
| browser-harness | [cand] A | 自愈 CDP harness（留 Computer Use 周验证） |
| 评测隔离设计 | 已回灌 | eval 层 fail-closed 网络策略 + 凭据注入白名单（Evaluation 周 C1/C4） |
| 引擎 security-assessment 能力树 | 已有 | 09_agent_engine 内安全评估层 |
| MS Agent Framework 1.0 GA | 已知变化（10-13） | SK+AutoGen 统一后继；兜底已标注，Harness 周追增量 |
| ToFu / Protocol Pivoting | [cand] A | MCP 信任边界 fuzzing + 跨协议转轴（MCP 安全周素材，Harness 周作 E3 参照） |

### 缺口（本领域内未覆盖，Harness 周重点）
| 缺口 | 证据 | 优先级 |
|---|---|---|
| **OS 级执行隔离实测**（MXC Linux Bubblewrap 后端 / JSON 策略 schema / 跨平台映射） | MXC A 卡"留待 Harness 周验证" | **A（本周验证候选）** |
| **无状态策略引擎实测**（MS AGT 或 Aigis/Guardian 确定性 guardrail 对比） | agent-firewall 卡"四选实测需重新评估权重" | **A（本周验证候选）** |
| 评测隔离落地核查（引擎 eval 层 fail-closed 网络策略是否落地） | Evaluation 周 6.2 结论待实现 | A（本周验证候选） |
| 认证/身份层（Agent Mesh DID/信任评分——TeamMind 多 Agent 互信） | G1/G3；TeamMind 需要 | A |
| argv 注入类防御清单（resume/session_id 等 untrusted→CLI flag） | CVE-2026-96620（10-18 兜底移交） | B |
| Harness 自研治理层（TeamMind 权限模型 vs dsh/MXC 对照） | 03_project_landscape | B |

### 相邻未覆盖（本领域外、可外推）
| 相邻方向 | 与 Harness 的连接 | 归属周 |
|---|---|---|
| Agent Runtime 状态持久化/失败恢复 | harness 的下层执行内核 | 下一域（Runtime，接 TeamMind） |
| Memory 实现层 | 治理需覆盖记忆读写边界（OWASP ASI06） | Memory 周 |
| Computer Use / Browser | browser-harness / 浏览器权限治理 | Computer Use/Browser 周 |
| 本地 / 边缘 AI | MXC Bubblewrap / Tafcm 本地执行 | AI Infra/本地边缘（接 Tafcm） |

## 三、本周验证计划（周五 10-23 用，2-3 个高价值候选）
1. **MXC 实测/对照**：拉取 MXC 文档与 SDK，检查 JSON 策略 schema + Linux Bubblewrap 后端形态；对照 Tafcm/TeamMind 权限模型写差异分析（承接候选卡 44 验证项）
2. **确定性 Guardrail / 策略引擎对比**：Aigis（pyaigis）或 MS Agent Governance Toolkit 任一跑通，评估"无 LLM 判定"防线对 silver-shield/TeamMind 的可用性
3. **评测隔离落地核查**：对照引擎 evaluation 层，检查 eval 默认不出网 / 凭据注入白名单是否可落地（承接 Evaluation 周 6.2/6.3-5）

## 四、任务视图（Capability Tree 动态实例化锚点）
- 任务类型 `agent-harness-governance-task` → 实例化本领域树，JIT 只展开缺失分支
- 引擎映射：leaf `maps_to` 扁平能力（sandbox-execution / runtime-defense / security-governance / privacy-guard / monitoring），见 `08_agent_centric/capabilities/README.md`（governance 域已存在：privacy-guard, runtime-defense, security-governance）

## 五、回灌目标（周六 10-24）
- 更新 `08_agent_centric/capabilities/graph.md`（补 harness-governance 相关跨域边，如 containment-policy / policy-engine / trust-identity / runtime-guardrail）
- 更新 `04_connections/README.md`
- 候选 → validated / dropped 决策
