# Capability Registry（Agent-Centric 能力注册表）

> 由引擎从种子知识库导出（09_agent_engine/engine/knowledge.py）。
> 能力是发现单位：先发现'需要什么能力'，再找实现工具。

| capability_id | 名称 | 前置能力 | 工具候选 | 相关项目 | 证据锚点 |
|---|---|---|---|---|---|
| agent-evaluation | Agent 评测 | evidence-collection | promptfoo, agentevals, deepseek-harness | Validation 编译器, silver-shield | 03_expansion_queue/candidates/[cand]agentic-benchmarks-2026.md, [cand]trace-based-agent-eval-2026.md |
| agent-memory | Agent 记忆 | - | mem0, dsh-memory-evolve | GrowthOS, TeamMind, dsh | 03_expansion_queue/candidates/[cand]agent-memory-2026.md, [cand]dsh-memory-evolve.md |
| assertion | 断言验证 | result-aggregation | promptfoo, agentevals, playwright | Validation 编译器, E2E-CLI | 03_expansion_queue/candidates/[cand]promptfoo-agent-evals.md |
| browser-interaction | 浏览器交互 | - | playwright, browser-use, webwright, hermes-agent | campus_order, E2E-CLI, agent-attention | 03_expansion_queue/candidates/[cand]browser-harness-2026.md, [cand]computer-browser-use-2026.md |
| embedding | 本地嵌入 | local-inference | glm-edge, ollama | Tafcm | 03_expansion_queue/candidates/[cand]local-edge-llm-2026.md |
| endpoint-discovery | 端点发现 | reconnaissance | browser-use, webwright, playwright | dsh-pentest | 03_expansion_queue/candidates/[cand]browser-harness-2026.md |
| evidence-collection | 证据收集 | result-aggregation | otel-genai, langfuse, promptfoo | Validation 编译器, silver-shield | 03_expansion_queue/candidates/[cand]otel-genai-observability.md, [cand]trace-based-agent-eval-2026.md |
| failure-recovery | 失败恢复 | state-persistence | openclaw, deepseek-harness | TeamMind, E2E-CLI | 03_expansion_queue/candidates/[cand]agent-harness-control-plane.md |
| http-interaction | HTTP 交互 | endpoint-discovery | mcp, browser-use, playwright | dsh-pentest, E2E-CLI | 03_expansion_queue/candidates/[cand]mcp-2026-07-28-stateless.md |
| local-inference | 本地推理 | - | ollama, glm-edge, llamafile | Tafcm, silver-shield | 03_expansion_queue/candidates/[cand]local-edge-llm-2026.md |
| long-term-memory | 长期记忆 | agent-memory | mem0, dsh-memory-evolve | GrowthOS, dsh | 03_expansion_queue/candidates/[cand]agent-memory-2026.md |
| monitoring | 运行监控 | observability | otel-genai, langfuse | Tafcm, TeamMind | 03_expansion_queue/candidates/[cand]otel-genai-observability.md |
| multi-agent-orchestration | 多 Agent 编排 | - | openclaw, langgraph, a2a, mcp | TeamMind, campus_order | 03_expansion_queue/candidates/[cand]multiagent-framework-2026.md, [cand]a2a-protocol-v1.md |
| observability | 可观测性 | - | otel-genai, langfuse | Tafcm, silver-shield, TeamMind | 03_expansion_queue/candidates/[cand]otel-genai-observability.md |
| privacy-guard | 隐私防护 | local-inference | ollama, glm-edge | Tafcm, silver-shield | 03_expansion_queue/candidates/[cand]local-edge-llm-2026.md |
| protocol-interop | 协议互操作 | - | mcp, a2a | TeamMind, agent-attention | 03_expansion_queue/candidates/[cand]mcp-2026-07-28-stateless.md, [cand]a2a-protocol-v1.md |
| reconnaissance | 侦察与目标测绘 | - | garak, pyrit, browser-use, webwright | dsh-pentest | 03_expansion_queue/candidates/[cand]ai-offensive-toolchain.md, [cand]agentic-attack-2026.md |
| reporting | 报告生成 | evidence-collection | promptfoo, langfuse | silver-shield | 03_expansion_queue/candidates/[cand]promptfoo-agent-evals.md |
| request-replay | 请求重放 | http-interaction | playwright, browser-use, webwright | E2E-CLI | 03_expansion_queue/candidates/[cand]webwright-2026.md |
| result-aggregation | 结果聚合 | vulnerability-detection | promptfoo, langfuse, agentevals | silver-shield, Validation 编译器 | 03_expansion_queue/candidates/[cand]promptfoo-agent-evals.md, [cand]otel-genai-observability.md |
| runtime-defense | 运行时防御 | security-governance | agent-firewall | silver-shield, campus_order | 03_expansion_queue/candidates/[cand]agent-firewall-runtime-defense-2026.md |
| sandbox-execution | 沙箱执行 | - | e2b, opencode | TeamMind, dsh-pentest, EP-002 | 03_expansion_queue/candidates/[cand]e2b-sandbox.md |
| scheduling | 任务调度 | - | openclaw, langgraph | agent-attention, TeamMind | 03_expansion_queue/candidates/[cand]multiagent-framework-2026.md |
| security-governance | 安全治理 | - | owasp-agentic-security, agent-firewall | EP-002, silver-shield, campus_order | 03_expansion_queue/candidates/[cand]owasp-agentic-security.md, [cand]agent-firewall-runtime-defense-2026.md |
| self-improvement | 自我改进 | agent-evaluation | promptfoo, agentevals | Validation 编译器, dsh | 03_expansion_queue/candidates/[cand]trace-based-agent-eval-2026.md |
| state-persistence | 状态持久化 | - | deepseek-harness, openclaw, langgraph | TeamMind, dsh | 03_expansion_queue/candidates/[cand]agent-harness-control-plane.md |
| vulnerability-detection | 漏洞检测 | http-interaction | garak, pyrit, owasp-agentic-security | dsh-pentest, silver-shield | 03_expansion_queue/candidates/[cand]ai-offensive-toolchain.md, [cand]owasp-agentic-security.md |
