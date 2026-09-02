# 04 · Connections（外部技术 ↔ 现有项目/知识连接地图）

> 记录"外部世界值得关注的对象"与"我的项目/知识体系"之间的连接。
> 这是从"发现"到"对我有意义"的关键一跳——没有连接的对象不值得进入视野。

## 连接卡模板字段

每条连接卡包含：`外部对象` → `连接的项目` → `连接的知识点` → `潜在收益` → `验证方式` → `状态`。

## 已识别的连接（截至 2026-09-02：首轮 4 + Expansion 13 + 雷达 5，共 22 条）

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
## 2026-09-02 雷达新增连接（5 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **DeepSeek Harness v0.1** | TeamMind（同构对照）/ agent-attention | Harness/Control Plane / 五维模型 Runtime | ✅ 已验证（源码级） | [deepseek-harness-2026 → [val]](../03_expansion_queue/validated/[val]deepseek-harness-2026.md) |
| **Flutter 本地 LLM 工具链** | **Tafcm**（离线 AI）/ silver-shield | 本地/边缘 AI（G3）/ 移动工程 | 🟡 已出候选卡 | [flutter-local-llm-2026](../03_expansion_queue/candidates/[cand]flutter-local-llm-2026.md) |
| **Browser Harness** | campus_order / E2E-CLI / agent-attention | Computer Use / EP-002 权限边界 | 🟡 已出候选卡 | [browser-harness-2026](../03_expansion_queue/candidates/[cand]browser-harness-2026.md) |
| **MS Research Webwright** | E2E-CLI（脚本化浏览器）/ campus_order | Computer Use / 可复现验证 | 🟡 已出候选卡 | [webwright-2026](../03_expansion_queue/candidates/[cand]webwright-2026.md) |
| **hermes-agent** | OpenClaw 生态对照 / campus_order | Agent Framework 格局 / 开源生态 | 🟡 已出候选卡 | [hermes-agent-2026](../03_expansion_queue/candidates/[cand]hermes-agent-2026.md) |
> 雷达增量（2026-09-02）：MCP / A2A / OWASP / Agent Memory 四条已知对象的重要变化已在对应候选卡内追加记录，连接关系不变。
## 2026-09-03 雷达新增连接（2 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Microsoft RAMPART + Clarity** | dsh-pentest（AI 攻防 CI）/ silver-shield / E2E-CLI | AI 安全（G1）/ EP-002 / Validation | 🟡 已出候选卡 | [rampart-clarity-2026](../03_expansion_queue/candidates/[cand]rampart-clarity-2026.md) |
| **PI-Hunter 注入审计线** | dsh-pentest / TeamMind / Validation 编译器 | AI 安全（G1）/ 注入路径定位 / 证据链思维 | 🟡 已出候选卡 | [pi-hunter-injection-audit-2026](../03_expansion_queue/candidates/[cand]pi-hunter-injection-audit-2026.md) |
> 雷达增量（2026-09-03）：hermes-agent（v0.20.x 系列 + Native Windows/DeepSeek V4）、Flutter 本地 LLM（flutter_litert_lm / LiteRT-LM 取代 MediaPipe）两条已知对象的重要变化已在对应候选卡内追加记录，连接关系不变。

## 规则

- 只有进入 `03_expansion_queue/validated` 的对象才能把状态改为 ✅（绿）。
- 🟡 = 已有候选证据卡、证据充足但尚未完成真机验证。
- ⬜ = 尚未扫描，仍为 Bootstrap 期的连接假设。
- 连接卡不重复写对象的基础介绍，只写连接关系。
- 全量对象清单、生命周期与去重基准见 `06_expansion_index/README.md`。
