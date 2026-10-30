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
