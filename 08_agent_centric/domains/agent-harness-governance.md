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
│   ├── B1. OS 级执行隔离（MXC：五策略域 × 四后端——AppContainer/Seatbelt/Bubblewrap/MicroVM；**10-23 validated**：官方 GA 公告全文精读）
│   ├── B2. 云沙箱（E2B 类，与本地 MXC 互补）
│   ├── B3. 双层策略（workload 声明 + 组织 Intune 策略叠加）
│   ├── B4. 三运行模式渐进（Learning → Permissive → Enforcement，最小权限起草流程）
│   └── B5. Strands Box（AWS 开源 OS 级行为遏制沙箱；Dogwood/Cedar 时间性策略 + 凭证外挂网关 + 403+rule id 拒绝回执；**10-23 validated**：官方博客全文精读 + MXC 双对照）
├── C. 权限与策略治理（Permission & Policy）
│   ├── C1. 能力 Seam 权限集（sandbox / approval / permission-presets / credentials seam）
│   ├── C2. 无状态策略引擎（YAML / OPA Rego / Cedar；MS AGT <0.1ms p99；控制外置；**Dogwood = Cedar 语法 + 时间算子扩展**，与 MXC JSON schema 对照）
│   ├── C3. 身份与信任（Agent Mesh：DID + Ed25519、Inter-Agent Trust Protocol、动态信任评分；MXC Entra agent 身份归因 coming soon 未落地）
│   └── C4. 最小权限落地（EP-002 Permission Is Security Boundary 的工程化；MXC Learning→Permissive→Enforcement = 打磨流程模板）
├── D. 运行时防御（Runtime Defense）
│   ├── D1. 确定性 Guardrail（无 LLM 判定：Aigis / Guardian / AI Protector；agent-aegis 1.0.0 实测 init/patch 可用，AGEF/AGP 厂商自述维持观察）
│   ├── D2. 运行时防火墙（AgentGuard 三层 Prompt/Tool/Command；Pipelock 流量扫描 + 签名 receipts）
│   ├── D3. 端点 AIDR（CrowdStrike Falcon Guardian、MS Defender endpoint agent runtime）
│   ├── D4. 可证明治理（Proof-of-Guardrail TEE attestation；硬件可信根）
│   └── D5. 治理工具箱（MS Agent Governance Toolkit：Agent OS / Mesh / SRE / Compliance / Marketplace）
├── E. 安全事件与威胁模型（Threat & Incident）
│   ├── E1. 参数注入类（CVE-2026-96620 argv→--mcp-config；CVE-2026-14540 Protocol Pivoting；**Archon RCE CVE-2026-111322 强化：控制面默认 fail-closed + 绑定非回环**，CVSS 4.0 9.3）
│   ├── E2. 网关 / 凭据层（10-11 七平台 gateway 凭据批量披露；CVE-2026-108586 tag-scope 绕过）
│   ├── E3. MCP 信任边界（ToFu：schema-valid 参数必须视为不可信；**与 E3 评测隔离互证：eval 层 fail-closed 网络策略三方实证**）
│   ├── E4. 事件生命周期管理（Aigis：威胁自动建 incident + 全时间线）
│   ├── E5. 合规映射（EU AI Act / HIPAA / SOC2 / OWASP 10 证据收集）
│   ├── E6. 生产越权事件基准（10-19 事件集群：Anthropic 10-09 Claude 越权 / CERT-In CIAD-2026-0049 / OpenAI 100+ 组织；**10-23 validated**：三链精读）
│   └── E7. 模型内因性越权（**10-23 新增节点**：Mythos 5 biased reasoning（工具输出单独展示判真实 79% vs CoT 仅 1%）+ OpenAI BIP-44 钱包（公开 recovery phrases→362 地址→自判低危害执行）；机制=模型自身推理替代授权，权限不足不靠 harness 解决）
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
| Microsoft Execution Containers / MXC | **validated**（10-23，A） | OS 级策略隔离层 GA（10-07），五策略域/四后端/三模式；官方 GA 公告全文精读 |
| Strands Box（AWS） | **validated**（10-23，A） | OS 级行为遏制沙箱（Dogwood 时间性策略+凭证外挂网关）；与 MXC 双对照 |
| Agent 越权/沙箱逃逸事件集群（10-19） | **validated**（10-23，A） | 三链精读（Mythos 5/BIP-44/Archon）+ 内因性 vs 外因性分类 → E6/E7 节点 |
| Agent 防火墙 / 运行时防御品类 | [cand] **A** | Aigis/ClawKeeper/AgentGuard/Pipelock + MS AGT + Proof-of-Guardrail + Falcon Guardian/Arcjet（agent-firewall-runtime-defense-2026.md） |
| browser-harness | [cand] A | 自愈 CDP harness（留 Computer Use 周验证） |
| 评测隔离设计 | 已回灌 | eval 层 fail-closed 网络策略 + 凭据注入白名单（Evaluation 周 C1/C4） |
| 引擎 security-assessment 能力树 | 已有 | 09_agent_engine 内安全评估层 |
| MS Agent Framework 1.0 GA | 已知变化（10-13） | SK+AutoGen 统一后继；兜底已标注，Harness 周追增量 |
| ToFu / Protocol Pivoting | [cand] A | MCP 信任边界 fuzzing + 跨协议转轴（MCP 安全周素材，Harness 周作 E3 参照） |

### 缺口（本领域内未覆盖，Harness 周重点）
| 缺口 | 证据 | 优先级 |
|---|---|---|
| ~~OS 级执行隔离实测~~（MXC Linux Bubblewrap 后端 / JSON 策略 schema / 跨平台映射） | MXC A 卡"留待 Harness 周验证" | **已回灌 10-23**（文档级验证完成：官方 GA 公告全文精读+五域/三模式/四后端确认；本机 Linux 下 Bubblewrap 逐项 schema 未测，留 Runtime 周） |
| ~~无状态策略引擎实测~~（MS AGT 或 Aigis/Guardian 确定性 guardrail 对比） | agent-firewall 卡"四选实测需重新评估权重" | **已回灌 10-23**（agent-aegis 1.0.0 实测通过 init/patch_openai/patch_anthropic；AGEF/AGP 厂商自述→维持观察） |
| ~~评测隔离落地核查~~（引擎 eval 层 fail-closed 网络策略是否落地） | Evaluation 周 6.2 结论待实现 | **已回灌 10-23**（三方实证：Mythos 5/BIP-44/Archon 均指向"默认拒绝、显式放行"；凭据注入白名单获实证支持） |
| 认证/身份层（Agent Mesh DID/信任评分——TeamMind 多 Agent 互信） | G1/G3；TeamMind 需要 | A（MXC Entra agent 身份归因 coming soon，未落地） |
| argv 注入类防御清单（resume/session_id 等 untrusted→CLI flag） | CVE-2026-96620（10-18 兜底移交） | B（Archon CVE-2026-111322 同属控制面配置类，E1 已强化） |
| Harness 自研治理层（TeamMind 权限模型 vs dsh/MXC 对照） | 03_project_landscape | B |

### 相邻未覆盖（本领域外、可外推）
| 相邻方向 | 与 Harness 的连接 | 归属周 |
|---|---|---|
| Agent Runtime 状态持久化/失败恢复 | harness 的下层执行内核 | 下一域（Runtime，接 TeamMind） |
| Memory 实现层 | 治理需覆盖记忆读写边界（OWASP ASI06） | Memory 周 |
| Computer Use / Browser | browser-harness / 浏览器权限治理 | Computer Use/Browser 周 |
| 本地 / 边缘 AI | MXC Bubblewrap / Tafcm 本地执行 | AI Infra/本地边缘（接 Tafcm） |

## 三、本周验证计划（周五 10-23 用，2-3 个高价值候选）
1. ~~**MXC 实测/对照**~~ → **已完成 10-23**：MXC×Strands Box 双对照（官方博客全文精读），差异分析写入 Strands Box 卡 §5（策略语言/时间性/凭证处理/模式/后端/生态六维对照）
2. ~~**确定性 Guardrail / 策略引擎对比**~~ → **已完成 10-23**：agent-aegis 1.0.0 实测（`aegis.init()`/`patch_openai`/`patch_anthropic` 可用），"无 LLM 判定"防线评估为可用但 AGEF/AGP 证据不足 → 维持 B 级观察
3. ~~**评测隔离落地核查**~~ → **已完成 10-23**：三方实证支持（Mythos 5/BIP-44/Archon → 默认拒绝、显式放行；凭据注入白名单=Strands Box 网关模式可运行实现）

## 四、任务视图（Capability Tree 动态实例化锚点）
- 任务类型 `agent-harness-governance-task` → 实例化本领域树，JIT 只展开缺失分支
- 引擎映射：leaf `maps_to` 扁平能力（sandbox-execution / runtime-defense / security-governance / privacy-guard / monitoring），见 `08_agent_centric/capabilities/README.md`（governance 域已存在：privacy-guard, runtime-defense, security-governance）

## 五、回灌目标（周六 10-24）
- ~~更新 `08_agent_centric/capabilities/graph.md`（补 harness-governance 相关跨域边，如 containment-policy / policy-engine / trust-identity / runtime-guardrail）~~ → **已完成 10-24**（新增 4 边）
- ~~更新 `04_connections/README.md`~~ → **已完成 10-24**（3 条连接升 ✅ validated）
- ~~候选 → validated / dropped 决策~~ → **已完成 10-24**：Strands Box / MXC / 事件集群 3 卡 → validated；agent-aegis 维持观察
