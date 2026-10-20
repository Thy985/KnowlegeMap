# 深耕扫描日志 · 2026-10-21（Personal Tech Radar · Harness/治理 周 Day3 · 增量扫描）

> 定位：周二~周四只追**增量**（新 release/新工具/相邻项目），写候选卡（S/A/B）。当前领域：Harness / 治理（10-19 起，Day1 能力树已建，Day2 已出 3 卡）。

## Re-ground
- README 每日分工确认 Day3 = 增量扫描
- current_focus.md：Harness/治理 active，已知锚点 dsh/MXC/Harness-ControlPlane/Agent 防火墙/Strands Box/事件集群/agent-aegis
- 去重基准：06_expansion_index 文末（含 10-20 全部对象）

## 扫描动作
2 路领域搜索（Archon CVE 细节、sandbox/containment/policy/guardrail 领域）+ 1 路相邻搜索（MCP 安全/治理工具）+ grep 去重核验（NVIDIA Sentry 未被既有卡覆盖）。

## 捕获结果与决策

### 决策 1：CVE-2026-111322 Archon → 并入事件集群卡（不单独建卡）✅
- 证据闭合：NVD（10-15/17，CVSS 9.8，VulnCheck 评分）、Tenable（10-16）、al-ice.ai（10-16 精读）、dev.to（10-18 Lockdown Guide）
- 事实：coleam00/Archon（23,692 stars AI coding agent）0.2.13–0.11.1，`/api/*` control API **默认绑 0.0.0.0 无认证**，攻击者可向以 **bypass permissions** 运行的 agent 发消息执行任意命令（未授权 RCE）
- 并入理由：与集群前三起（agent 自身越权/逃逸）机制不同，本起为**攻击者经失控默认配置远程接管 agent**，补全第四类「控制面配置缺失（默认无认证/开放绑定）」；映射能力树 E 层 E1 控制面配置类；与 10-19 兜底移交判断一致
- 卡更新：证据区第 4 条 FACT + 一手来源 + 验证计划升级（Archon RCE 链条纳入周五精读路径）

### B 级领域内增量（记日志不建卡，素材移交周五对比池）
| 对象 | 时间/来源 | 本质 | 处置 |
|---|---|---|---|
| **NVIDIA Sentry** | 9-28，shattered.io | BlueField-4 DPU **带外 watchdog**：不在 agent 环境内、毫秒级隔离越界 agent，独立于 OpenShell | B 级记日志；与 MXC/Strands Box「agent 之外强制边界」同哲学但硬件级；OpenShell 生态相邻增量（发布近 1 月、无后续证据） |
| **Warden** | 10-11，LobeHub/AlwaysReadyAllies | MCP drop-in 安全中间件：tamper-evident 日志+策略+危险调用门控+注入/密钥扫描，YAML 配置 | B 级记日志；guardrail 品类新成员，并入周五对比池 |
| **mcpkernel** | 10-08，PyPI | MCP 网关自攻击「免疫系统」模式（Shadow LLM 持续自我 prompt-injection 探测 0-day） | B 级维持观察；概念新颖但仅 PyPI 自述无第三方证据 |
| **Vaikora Guard MCP** | 10-15 开源，Data443 | MCP 策略执行中间件（写工具显式审批） | B 级记日志；并入周五对比池 |

## 周五验证计划（Day2 升级版）待办核对
- ① MXC × Strands Box 双对照（含凭证网关模式=引擎 eval 凭据注入白名单参考实现）
- ② guardrail-策略引擎对比池扩容：Aigis·MS AGT·agent-aegis + **Warden/mcpkernel/Vaikora**（Day3 素材，实际对比按证据可得性取舍）
- ③ 评测隔离落地核查（引擎 eval fail-closed）
- ④ 事件集群精读回填 E 层（**新增 Archon RCE 链条**：默认配置→开放绑定→RCE 路径）

## 结论
**Changed**（已知对象事件集群卡升级：Archon CVE-2026-111322 并入第 4 条证据线；B 级增量 4 项记日志移交周五对比池）。
