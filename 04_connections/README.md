# 04 · Connections（外部技术 ↔ 现有项目/知识连接地图）

> 记录"外部世界值得关注的对象"与"我的项目/知识体系"之间的连接。
> 这是从"发现"到"对我有意义"的关键一跳——没有连接的对象不值得进入视野。

## 连接卡模板字段

每条连接卡包含：`外部对象` → `连接的项目` → `连接的知识点` → `潜在收益` → `验证方式` → `状态`。

## 已识别的连接（2026-09-01：首轮扫描 4 张 + Expansion 扫描 13 张候选卡，共 17 条）

| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| MCP 2026-07-28 无状态协议 | TeamMind / agent-attention / Tafcm / OpenClaw | Tool System / 五维模型 / 工具档案 | 🟡 已出候选卡 | [mcp-2026-07-28-stateless](../03_expansion_queue/candidates/[cand]mcp-2026-07-28-stateless.md) |
| MCP 通知类 Server | agent-attention | Tool System / Agent 对外可见性 | 🟡 已出候选卡 | [mcp-notification-servers](../03_expansion_queue/candidates/[cand]mcp-notification-servers.md) |
| promptfoo（Evals） | Tafcm ADI / silver-shield Benchmark | Validation / Evaluation 维度 | 🟡 已出候选卡 + 本机实测 | [promptfoo-agent-evals](../03_expansion_queue/candidates/[cand]promptfoo-agent-evals.md) |
| Evals 框架格局（DeepEval/OpenAI Evals/Inspect/Ragas/Langfuse） | Tafcm / silver-shield / dsh-pentest | Validation / Evaluation / AI 安全 | 🟡 已出候选卡 | [evals-framework-landscape](../03_expansion_queue/candidates/[cand]evals-framework-landscape.md) |
| **OWASP Agentic Security 体系** | dsh-pentest / silver-shield | EP-002 / AI 安全（G1）/ 工具供应链 | 🟡 已出候选卡 | [owasp-agentic-security](../03_expansion_queue/candidates/[cand]owasp-agentic-security.md) |
| **A2A 协议 v1.0 + AAIF** | TeamMind | 多 Agent 编排 / 互操作协议 | 🟡 已出候选卡 | [a2a-protocol-v1](../03_expansion_queue/candidates/[cand]a2a-protocol-v1.md) |
| **Agent Harness / Control Plane（Omnigent/MS）** | TeamMind / 五维模型 | Runtime / 验证编译器 / EP 治理 | 🟡 已出候选卡 | [agent-harness-control-plane](../03_expansion_queue/candidates/[cand]agent-harness-control-plane.md) |
| **Agent Memory 2026（Mem0/Zep/Letta/A-MEM）** | GrowthOS / TeamMind / Validation | Memory 维度 / 记忆验证 / 基准批判 | 🟡 已出候选卡 | [agent-memory-2026](../03_expansion_queue/candidates/[cand]agent-memory-2026.md) |
| **AI 攻防工具链（Garak/PyRIT/PentestGPT）** | dsh-pentest / silver-shield | AI 安全（G1）/ 红队 / 对抗 | 🟡 已出候选卡 | [ai-offensive-toolchain](../03_expansion_queue/candidates/[cand]ai-offensive-toolchain.md) |
| **Computer/Browser Use GA + browser-use** | campus_order / E2E-CLI / agent-attention | Tool System / 真实环境操作 | 🟡 已出候选卡 | [computer-browser-use-2026](../03_expansion_queue/candidates/[cand]computer-browser-use-2026.md) |
| **E2B 沙箱 + Agentic Provisioning** | TeamMind / dsh-pentest | EP-002 / 执行域隔离 | 🟡 已出候选卡 | [e2b-sandbox](../03_expansion_queue/candidates/[cand]e2b-sandbox.md) |
| **OTel GenAI 可观测标准** | Tafcm ADI / silver-shield | 可观测性_LLM应用追踪 | 🟡 已出候选卡 | [otel-genai-observability](../03_expansion_queue/candidates/[cand]otel-genai-observability.md) |
| **Agentic 基准 2026 批判视角** | Validation / silver-shield Benchmark | 验证编译器 / 基准可信度 | 🟡 已出候选卡 | [agentic-benchmarks-2026](../03_expansion_queue/candidates/[cand]agentic-benchmarks-2026.md) |
| **本地/边缘 LLM 推理** | Tafcm / silver-shield | 本地/边缘 AI（G3） | 🟡 已出候选卡 | [local-edge-llm-2026](../03_expansion_queue/candidates/[cand]local-edge-llm-2026.md) |
| **开源 Agentic CI** | AI Code Review 资产族 / Tafcm | Agentic CI / 代码审查 | 🟡 已出候选卡 | [open-source-agentic-ci](../03_expansion_queue/candidates/[cand]open-source-agentic-ci.md) |
| **Fine-tuning 对齐新范式** | ML 方法论 / silver-shield | Fine-tuning / 对齐 | 🟡 已出候选卡 | [llm-finetuning-alignment-2026](../03_expansion_queue/candidates/[cand]llm-finetuning-alignment-2026.md) |
| **Multi-Agent 框架终局（LangGraph/CrewAI/AG2/MS）** | TeamMind | 多Agent_框架选型与拓扑 | 🟡 已出候选卡 | [multiagent-framework-2026](../03_expansion_queue/candidates/[cand]multiagent-framework-2026.md) |

## 规则

- 只有进入 `03_expansion_queue/validated` 的对象才能把状态改为 ✅（绿）。
- 🟡 = 已有候选证据卡、证据充足但尚未完成真机验证。
- ⬜ = 尚未扫描，仍为 Bootstrap 期的连接假设。
- 连接卡不重复写对象的基础介绍，只写连接关系。
- 全量对象清单、生命周期与去重基准见 `06_expansion_index/README.md`。
