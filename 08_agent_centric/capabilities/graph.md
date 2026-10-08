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
