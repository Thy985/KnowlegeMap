# Capability Graph（跨域复用视图）

## 跨域复用能力（≥2 领域）
- **agent-memory** → agent-memory, agent-runtime
- **assertion** → agent-evaluation, e2e-testing
- **browser-interaction** → browser-agents, e2e-testing, web-automation, web-security
- **endpoint-discovery** → api-testing, web-security
- **evidence-collection** → agent-evaluation, web-security
- **http-interaction** → api-testing, browser-agents, web-automation, web-security
- **monitoring** → observability, runtime-defense
- **protocol-interop** → agent-runtime, developer-tools
- **reconnaissance** → red-teaming, web-security
- **reporting** → agent-evaluation, web-security
- **result-aggregation** → agent-evaluation, web-automation
- **runtime-defense** → governance, runtime-defense
- **sandbox-execution** → developer-tools, web-automation
- **self-improvement** → agent-evaluation, agent-runtime
- **vulnerability-detection** → red-teaming, web-security

## 领域 → 能力
- agent-evaluation: agent-evaluation, assertion, evidence-collection, reporting, result-aggregation, self-improvement
- agent-memory: agent-memory, embedding, long-term-memory
- agent-runtime: agent-memory, failure-recovery, multi-agent-orchestration, protocol-interop, scheduling, self-improvement, state-persistence
- api-testing: endpoint-discovery, http-interaction
- browser-agents: browser-interaction, http-interaction
- developer-tools: protocol-interop, sandbox-execution
- e2e-testing: assertion, browser-interaction
- governance: privacy-guard, runtime-defense, security-governance
- observability: monitoring, observability
- red-teaming: reconnaissance, vulnerability-detection
- runtime: local-inference
- runtime-defense: monitoring, runtime-defense
- web-automation: browser-interaction, http-interaction, result-aggregation, sandbox-execution
- web-security: browser-interaction, endpoint-discovery, evidence-collection, http-interaction, reconnaissance, reporting, request-replay, vulnerability-detection

## 2026-10-17 回灌：Evaluation 周新增跨域边
> 来源：评测可信度三环（AgentJudgeBench / Transect / TestJack）验证结论 → 引擎 evaluation 层落地建议。

- **judge-calibration** → agent-evaluation（D1/D3），e2e-testing（assertion 校准参照）
- **replayable-tests** → agent-evaluation（C3），e2e-testing（动态测试生成），web-security（测试注入复用）
- **eval-isolation** → agent-evaluation（C1/C4），runtime-defense（sandbox 复用），developer-tools（fail-closed 网络策略）
- **evidence-chain** → agent-evaluation（B2/B4），web-security（evidence-collection 同构），agent-memory（标签溯源复用）
- **eval-feedback** → agent-evaluation（E1/E2），agent-runtime（self-improvement 回灌），observability（drift 监测）

## 2026-10-24 回灌：Harness/治理 周新增跨域边
> 来源：周五验证日结论（Strands Box×MXC 双对照 / 事件集群三链精读 / agent-aegis 实测）回灌。

- **containment-policy** → governance（B 层 B1/B5），runtime-defense（执行隔离复用），developer-tools（sandbox-execution 升级）
- **policy-engine** → governance（C2 无状态策略引擎），agent-evaluation（F1 评测隔离策略），agent-runtime（multi-agent-orchestration 权限层）
- **trust-identity** → governance（C3 身份与信任），agent-runtime（multi-agent 互信），web-security（认证边界同构）
- **runtime-guardrail** → governance（D1 确定性 guardrail），agent-evaluation（eval 层 fail-closed 落地），agent-runtime（self-improvement 安全回灌）

## 2026-10-31 回灌：Runtime 周验证结论回灌（Dapr validated / durable 品类 / 挂起恢复线）
> 来源：周五验证日结论（Dapr Agents 官方文档全文+包实测晋升 validated / durable 品类 9 向横向对照 / Infinity 对照维持观察）回灌。

- **durable-state** → agent-runtime（A 层 Durable Execution：步骤持久化+双 store+恢复语义），agent-memory（agent-workflow 执行状态 vs agent-memory 会话记忆分层），developer-tools（Diagrid wrapper：durable 化既有 agent 框架）
- **checkpoint-recovery** → agent-runtime（F 层生命周期：suspend-resume/crash recovery），governance（durable checkpoint=可审计执行链，E 层证据），observability（每步持久化=Diagrid 可视化/审计基础设施）
- **suspend-resume** → agent-runtime（F1/F3：<500ms 挂起/恢复、slice 有界执行），agent-evaluation（长时程 agent 过程感知评测——LiveMACE 跨域），web-automation（挂起等待零计算=serverless step 模式）

## 2026-11-07 回灌：Runtime 第二周验证结论（Substrate validated / sandbox-lifecycle validated）
> 来源：11-06 验证日（Agent Substrate 代码级验证晋升 validated / OpenKruise Agents v0.6.0 源码核对晋升 validated）回灌。区分于 10-31「Dapr + durable 品类」线，本轮补的是**生命周期控制面**与**身份-出口一体化**两类边。

- **lifecycle-control-plane** → agent-runtime（F1/F2：SuspendActor/ResumeActor 作为显式控制面，checkpoint 到新 snapshot/from latest snapshot），governance（每次 suspend/resume=可审计生命周期事件），observability（状态迁移点与 park 队列=容量/健康信号）
- **identity-egress-fusion** → agent-runtime（D/E 层：每 actor 短时 SPIFFE X.509 + egress gateway per-actor JWT，身份与出站策略在同一策略点裁决），governance（C3 身份与信任：MXC Entra 托管侧缺口的开源参照），web-security（egress PEP 与认证边界同构）
- **zero-credential-execution** → governance（凭据外注=最小权限的可执行形态：actor 仅持 placeholder header），agent-runtime（D 层隔离：被攻陷 agent 无可外泄 secret），developer-tools（credential-provider 作为可插拔组件）
- **load-shedding-parking** → agent-runtime（F3 伸缩/过载：park budget 5s、parking lot 1024、指数退避，已提交 restore 不取消），observability（park 深度/等待时长=调度容量指标），agent-evaluation（长时程评测的过载语义基线）

## 2026-11-14 回灌：Memory 周验证结论（可靠性三条边）
> 来源：11-12 SIx Harness 增量 + 11-13 验证日（Mem0 本地实跑 / EvolveLab 结构核对 / Zep CE 作废）回灌。补的是**记忆子系统的失败可检测性**，与 durable-state / checkpoint-recovery 那组「执行状态」边区分开。

- **memory-reliability** → agent-memory（H1~H5：健康门/心跳/降级诚实/静默腐化防护/告警预算；SIx 11 项自检 + 85 次失败零静默），observability（健康门单行状态 `MEMORY-HEALTH: 11/11 GREEN`、hook 心跳把"该发生却没发生"变成事件=可观测原语），governance（"静默失败必须可检测"作为可靠性证据要求，与 E 层审计同构），runtime-defense（记忆被静默腐化=防御面整体失效，且不会出现在任何 benchmark 上）
- **honest-degradation** → agent-memory（向量腿坏自动降 BM25-only、永不阻塞主流程、失败写 log-once），agent-runtime（降级语义与 fail-open/fail-closed 同构：可降级但必须显式），developer-tools（降级记录=排障证据，避免"看起来正常"）
- **write-receipt-verification** → agent-memory（Mem0 `add()` 返回 `{"results": []}` 而数据已落库：回执≠状态），governance（F4 审计要求"回执与状态不一致必须可查"），agent-evaluation（写入确认是评测前置条件，否则评测对象本身不明）
