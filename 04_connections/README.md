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
## 2026-09-04 雷达新增连接（1 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Agentic CLEAR（IBM 自动多层级评估）** | silver-shield（Benchmark Harness）/ Tafcm ADI / Validation 编译器 | Agent Evaluation / 自动 trace 评估 / Evidence→Judgment | 🟡 已出候选卡 | [agentic-clear-2026](../03_expansion_queue/candidates/[cand]agentic-clear-2026.md) |
> 雷达增量（2026-09-04）：Agent Memory（Mem0 v3 + 分数批判）、OTel GenAI（语义规范稳定化 + 阿里 LoongSuite）两条已知对象的重要变化已在对应候选卡内追加记录，连接关系不变。
## 2026-09-05 雷达新增连接（2 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Agent Skill 供应链安全（SkillFortify 形式化验证 + Unit 42 BIV）** | **EP-002**（权限即安全边界）/ campus_order（OpenClaw）/ dsh-pentest | AI 安全（G1）/ Skills 体系 / 声明 vs 实际验证 / OWASP ASI04 | 🟡 已出候选卡 | [skill-supply-chain-security-2026](../03_expansion_queue/candidates/[cand]skill-supply-chain-security-2026.md) |
| **Agentic GraphRAG 2026（MemGraphRAG / Graph-R1 / A-RAG）** | **GrowthOS** / TeamMind / silver-shield | RAG 系统化（G2）/ 记忆×图×多 Agent / Context Engineering | 🟡 已出候选卡 | [agentic-graphrag-2026](../03_expansion_queue/candidates/[cand]agentic-graphrag-2026.md) |
> 雷达增量（2026-09-05）：无已知对象重要变化；MCP 侧 2026-07-28 stateless 已由各语言 SDK（rust 3.0 beta / C# v2 / go v1.7）落地，属已知事件执行确认。
## 2026-09-06 雷达新增连接（1 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Agentic UX / AI 原生产品设计模式** | **TeamMind** / campus_order（OpenClaw 2.0 浏览器 UI）/ agent-attention / Tafcm | AI 原生产品（G2 空白区）/ 五级自主度 / diff 预览即确认 / EP-002 可见性 | 🟡 已出候选卡 | [agentic-ux-2026](../03_expansion_queue/candidates/[cand]agentic-ux-2026.md) |
> 雷达增量（2026-09-06）：OpenClaw 2.0（v2026.8.1 大版本）、SkillSpector/CHAINDROP/Tenable、ATR 威胁规则等 3 条已知对象重要变化已在对应候选卡内追加记录，连接关系不变。
## 2026-09-07 雷达新增连接（1 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **去中心化 AI / Agent 联邦学习（IETF 草案）** | **TeamMind**（协作面与执行面解耦类比）/ silver-shield / EP-002 延伸 | 去中心化 AI（G4）/ 隐私保护 / 多 Agent 互操作（A2A 对接） | 🟡 已出候选卡 | [decentralized-ai-federated-agents-2026](../03_expansion_queue/candidates/[cand]decentralized-ai-federated-agents-2026.md) |
> 雷达增量（2026-09-07）：DeepSeek Harness（validated）v0.1.3 大版本迭代（原生图片输入 + 异构 sub-agent 编排 + 200k stars）已在 validated 卡内追加记录，连接关系不变。
## 2026-09-08 雷达新增连接（2 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Agent 形式化验证 / 可证明 Guardrail** | **Validation 编译器**（证据机器可核验层）/ EP-002 / TeamMind（工具调用策略）/ silver-shield | 形式化验证（G5 战略）/ 可证明安全 / 策略即代码 | 🟡 已出候选卡 | [agent-formal-verification-2026](../03_expansion_queue/candidates/[cand]agent-formal-verification-2026.md) |
| **Robotics×LLM / 具身智能 VLA** | **multi_arm_line_ws**（孤悬项目知识支撑）/ TeamMind（统一 harness 范式类比） | Robotics × LLM（G4）/ 多模态 / 世界模型 | 🟡 已出候选卡 | [robotics-llm-vla-2026](../03_expansion_queue/candidates/[cand]robotics-llm-vla-2026.md) |
> 雷达增量（2026-09-08）：LLM 可观测选型格局——Helicone 进入维护模式（Mintlify 收购后），xtrace/Logfire/Opik 新进者双路线，已在 otel-genai 卡内追加记录，连接关系不变。
## 2026-09-09 雷达新增连接（2 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Agentic Attack 范式事件** | **silver-shield**（防御侧直接对标）/ dsh-pentest（实战基准参考）/ TeamMind（多 agent 安全边界正反教材）/ EP-002（权限失效模式） | AI 安全攻防（G1 第一盲区）/ Agent 威胁建模 / 攻击经济学 | 🟡 已出候选卡 | [agentic-attack-2026](../03_expansion_queue/candidates/[cand]agentic-attack-2026.md) |
| **OpenCode（headless HTTP coding agent）** | **TeamMind**（异构 harness 编排参考）/ Tafcm（agent 服务化对照）/ DeepSeek Harness（谱系对照） | Agent Harness 架构（S3）/ 五维 Runtime / agent 服务化 | 🟡 已出候选卡 | [opencode-agent-2026](../03_expansion_queue/candidates/[cand]opencode-agent-2026.md) |
> 雷达增量（2026-09-09）：Agent Memory——Mem0×DeepSeek Harness 原生插件、Letta Code memory-first coding agent 已在 agent-memory 卡内追加记录，连接关系不变。
## 2026-09-10 雷达新增连接（1 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **HAAF 可信度评估范式（场景流形采样）** | **Validation 编译器**（Evidence 收集代表性理论）/ silver-shield（风险敏感采样）/ Agentic CLEAR（元框架对照） | Agentic 评测方法论（S2 核心）/ 基准批判 / 代表性评估 | 🟡 已出候选卡 | [haaf-trustworthy-agent-eval-2026](../03_expansion_queue/candidates/[cand]haaf-trustworthy-agent-eval-2026.md) |
> 雷达增量（2026-09-10）：OpenClaw 2026.9.3（2.0 后首个稳定迭代）记日志；A2A v1.0 加入 AAIF 为已记录事件日期确认，连接关系不变。
## 2026-09-11 雷达新增连接（1 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Agent 防火墙 / 运行时防御品类** | **silver-shield**（确定性 guardrail 借鉴）/ EP-002（权限边界工程实现）/ campus_order（ClawKeeper 针对 OpenClaw）/ TeamMind（工具治理选型池）/ dsh-pentest（可攻击测试） | AI 安全防御侧（G1）/ Agent 运行时治理 / Skill 供应链同线 | 🟡 已出候选卡 | [agent-firewall-runtime-defense-2026](../03_expansion_queue/candidates/[cand]agent-firewall-runtime-defense-2026.md) |
> 雷达增量（2026-09-11）：DeepSeek Harness v0.1.5×V4.1 Flash 联合训练、local-edge-llm MiniCPM5-2B/Edge LLM 已分别在 validated/local-edge 卡内追加记录，连接关系不变。
## 2026-09-12 雷达新增连接（1 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Trace-based Agent Evaluation（agentevals/TraceBench/AWS）** | **Validation 编译器**（trace 即 Evidence、可重放评测）/ TeamMind（tool trajectory 确定性门禁=Evaluation 不变量）/ Tafcm（本地零成本评测）/ silver-shield（trace 审计+回归门禁） | Agent 评测方法论（S2 核心）/ 可观测 × 评测交叉 | 🟡 已出候选卡 | [trace-based-agent-eval-2026](../03_expansion_queue/candidates/[cand]trace-based-agent-eval-2026.md) |
> 雷达增量（2026-09-12）：Agent 防火墙品类第二批（OWASP Agent Memory Guard/Guardian 等）已追加在 agent-firewall-runtime-defense-2026 卡内，连接关系不变。
## 2026-09-20 雷达新增连接（1 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Agentic Inference Infra（NVIDIA Dynamo/AWS prefix-aware/HyperPod Gateway/vLLM KV offload/Unified AI Gateway）** | **Tafcm**（端-边-云联合路由=本地优先架构参考）/ **TeamMind**（multi-agent fan-out 推理模式）/ **dsh**（coding agent 长 prefill+tool call 循环优化）/ E2E-CLI（长链路推理） | AI Infra × Agent（G3/G5 空白区）/ Context Engineering（前缀复用=缓存预算）/ Harness 六职责 control 侧面 | 🟡 已出候选卡 | [agentic-inference-infra-2026](../03_expansion_queue/candidates/[cand]agentic-inference-infra-2026.md) |

## 2026-10-17 回灌：Evaluation 周（10-12~10-16）新增连接（6 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **AgentJudgeBench（LLM-as-Judge 可靠性）** | **Validation 编译器**（judge 校准约束）/ 引擎 evaluation 层（程序化断言优先）/ silver-shield（风险判定不依赖单一 LLM） | Agent 评测方法论（S2 核心）/ judge 对齐度 / GT 依赖管理 | 🟡 已出候选卡（三环验证完成，维持观察） | [agentjudge-bench-2026](../03_expansion_queue/candidates/[cand]agentjudge-bench-2026.md) |
| **Transect（transcript 可审计分析）** | **Validation 编译器**（证据链数据模型：回合时间线+标签溯源，与 Claim→Evidence→Judgment 同构）/ TeamMind（长时程 agent 可观测）/ silver-shield（审计链） | 评测者可审计性（B2/B4）/ Inspect Scout 生态 / 可复现评测 | 🟡 已出候选卡（三环验证完成，维持观察） | [transect-agent-eval-observability-2026](../03_expansion_queue/candidates/[cand]transect-agent-eval-observability-2026.md) |
| **TestJack（Agentic Coding 基准审计）** | **Validation 编译器**（可回放测试概念）/ 引擎 evaluation 层（动态测试生成）/ E2E-CLI（测试注入复用） | 补丁/测试侧审计（C3）/ 34.4% 判正确违规 / evaluator 自适应 | 🟡 已出候选卡（三环验证完成，维持观察） | [testjack-agentic-benchmark-audit-2026](../03_expansion_queue/candidates/[cand]testjack-agentic-benchmark-audit-2026.md) |
| **求索 4.0（国内 AI 评测基准）** | silver-shield（Benchmark Harness 参照）/ Tafcm（本地模型评测）/ 引擎 evaluation 层 | 国内评测体系（A2/A4）/ 全产业链基准 / 真实负载 | 🟡 已出候选卡 | [qiusuo-benchmark-2026](../03_expansion_queue/candidates/[cand]qiusuo-benchmark-2026.md) |
| **LiveMACE（动态市场持久评测）** | TeamMind（多 agent 持续评测）/ Memory 周（动态测试床方法论先行参照）/ 引擎 evaluation 层（outcome-capability gap） | 动态 vs 静态评测设计 / 过程感知评估 / 30 天连续评测 | 🟡 已出候选卡（B+，留待 Memory 周验证） | [livemace-process-aware-eval-2026](../03_expansion_queue/candidates/[cand]livemace-process-aware-eval-2026.md) |
| **评测隔离设计（10-11 事件：Anthropic 切断 eval live internet）** | **DeepSeek Harness**（运行时隔离 vs eval 层隔离对照）/ 引擎 evaluation 层（fail-closed 网络策略）/ dsh-pentest（测试环境隔离） | 评测环境隔离（C1/C4）/ 网络/凭据/外部目标三隔离 / eval 默认不出网 | ✅ 已回灌能力树（C1/C4 落地检查完成） | 事件记录见 10-11 日志 + agent-evaluation.md §6.2 |

## 2026-10-20 兜底扫描新增连接（1 条 · 领域外捕获）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Dapr Agents（CNCF Dapr × NVIDIA 分布式 Agent 运行时）** | **TeamMind**（最强连接：durable execution 步骤持久化/崩溃恢复、actor 并发、pub/sub 多 agent 编排=TeamMind 生产化分布式问题的成熟参照）/ **Tafcm**（Ollama 本地默认+provider-agnostic Conversation API）/ 引擎（每步持久化+Diagrid 可视化=可观测/审计链基础设施） | Agent Runtime（下一深耕领域）/ durable execution 范式（Temporal 式工作流的 agent 原生 API）/ Memory 与 execution state 分层（双 state store） | ✅ **已验证（10-30 文档全文+包实测，晋升 validated）** | [dapr-agents-distributed-runtime-2026](../03_expansion_queue/candidates/[cand]dapr-agents-distributed-runtime-2026.md) |

## 2026-10-20 雷达新增连接（Harness 周 Day2 · 3 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Strands Box（AWS OS 级行为遏制沙箱）** | **TeamMind**（OS 级外部强制边界参照 + policy.dw/box.toml 双文件模型对照权限设计）/ **Tafcm**（本地执行遏制边界）/ **silver-shield**（出站凭证外挂+目的地 permit 确定性管控）/ **campus_order**（OpenClaw 类 agent 遏制） | Harness B 层（执行隔离：MXC 对照线）/ C 层（策略引擎 Cedar/Dogwood 时间性）/ 评测隔离（网关凭证注入同构） | ✅ 已验证（10-23 双对照，10-24 回灌） | [strands-box-os-containment-2026](../03_expansion_queue/candidates/[cand]strands-box-os-containment-2026.md) |
| **Agent 越权/沙箱逃逸事件集群（2026-10）** | **TeamMind**（多 agent 生产化失败案例基线）/ **silver-shield**（越权/虚假举报行为模式识别）/ **campus_order**（生产 agent 越权风险清单） | Harness E 层（威胁模型：生产失控真实证据）/ B 层隔离失效动机链（→ Strands Box/MXC）/ **E7 模型内因性越权新节点** | ✅ 已验证（10-23 三链精读，10-24 回灌） | [agent-containment-breach-2026](../03_expansion_queue/candidates/[cand]agent-containment-breach-2026.md) |
| **agent-aegis（Guardrails+Policy+Protocol 一体化）** | **TeamMind**（YAML 策略引擎+approval gates 对照）/ **silver-shield**（PII/注入 guardrails 前置过滤）/ 引擎 evaluation 层（确定性 guardrail 落地候选） | Harness C2（无状态策略引擎 YAML 线）/ D1（确定性 guardrail 无 LLM 线） | 🟡 已出候选卡（B 级，10-23 实测 1.0.0 通过，维持观察） | [agent-aegis-governance-2026](../03_expansion_queue/candidates/[cand]agent-aegis-governance-2026.md) |

## 2026-10-24 回灌：Harness 周验证结论回灌（3 条升级 + 2 条补充）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Microsoft Execution Containers / MXC** | **TeamMind**（平台级执行边界原语参照）/ **campus_order**（OpenClaw 已接入 MXC 生态）/ **Tafcm**（本地策略隔离） | Harness B1（五策略域×四后端）/ B3 双层策略 / B4 三模式渐进 | ✅ 已验证（10-23 GA 公告精读，10-24 回灌） | [microsoft-execution-containers-2026](../03_expansion_queue/candidates/[cand]microsoft-execution-containers-2026.md) |
| **内因性 vs 外因性越权分类** | **silver-shield**（模型合理化行为=判定信号）/ **TeamMind**（harness 不解决内因性，需模型倾向+评测隔离双线） | Harness E7（模型内因性越权）/ E1 强化（控制面 fail-closed）/ F1 评测隔离互证 | ✅ 已回灌能力树（E6/E7 节点落地 10-24） | 事件集群卡 §5 分类表 |

## 2026-10-27 雷达新增连接（Runtime 周 Day2 · 1 条）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Durable Execution 品类（MS Durable Extension / AWS Lambda Go SDK GA / Restate / Mastra / Temporal / Obelisk）** | **TeamMind**（durable state/崩溃恢复生产化方案选型——**Restate Java/Kotlin SDK 直接候选**，对照 Dapr Agents Python）/ **Tafcm**（Obelisk zero token architecture：执行期不耗 token）/ **silver-shield**（durable checkpoint=可审计执行链） | Runtime A 层（Durable Execution：步骤持久化/双 store/恢复语义）/ 缺口③（品类横向扩 7 向，周五验证）/ Mastra AgentController=harness 原语化 | 🟡 已出候选卡（B 级；10-30 §5 产出 **9 向横向对照表**，品类卡维持观察） | [durable-execution-category-mainstreaming-2026-10](../03_expansion_queue/candidates/[cand]durable-execution-category-mainstreaming-2026-10.md) |

## 2026-10-31 回灌：Runtime 周验证结论回灌（1 条升级 + 2 条新增）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Dapr Agents（CNCF Dapr × NVIDIA）** | **TeamMind**（durable execution/actor/pub-sub 生产化设计基线）/ **Tafcm**（Conversation API provider-agnostic：Ollama 默认本地）/ 引擎（每步持久化=审计链） | Runtime A/B/C/F 层（DurableAgent 唯一推荐路径：`Agent` deprecated；event sourcing 重放+ContextAwareLogger；双 store+actorStateStore；AgentRunner 三模式） | ✅ **已验证（10-30 文档全文+包实测 1.1.0，晋升 validated）** | [dapr-agents-distributed-runtime-2026](../03_expansion_queue/candidates/[cand]dapr-agents-distributed-runtime-2026.md) |
| **Durable Execution 品类 9 向对照（验证结论）** | **TeamMind**（选型矩阵：基础设施运行时 Dapr/DBOS/Restate vs harness 包装 Vercel/Notion/Mastra vs serverless 平台 AWS Lambda vs 并发挂起 Infinity；恢复语义两派；Java 首选 Restate） | Runtime A 层（步骤持久化粒度/恢复语义/部署形态四层位） | ✅ 已回灌能力树（缺口①③已闭环；graph durable-state/checkpoint-recovery/suspend-resume 三边） | [durable-execution-category-mainstreaming-2026-10](../03_expansion_queue/candidates/[cand]durable-execution-category-mainstreaming-2026-10.md) |
| **AWS Infinity（并发挂起 runtime，10-23 开源）** | **TeamMind**（第三条设计路线对照：stackless coroutine 式挂起/恢复 vs 步骤持久化互补）/ 引擎（slice 有界执行+synthetic tool call 语义） | Runtime A/F 层（挂起恢复派：slice（history→一次补全→至多一个工具调用）/serverless step 模式/75k 并发 8GB） | 🟡 已出候选卡（B 级；10-30 对照完成，research early release 维持观察） | [aws-infinity-agent-runtime-2026-10](../03_expansion_queue/candidates/[cand]aws-infinity-agent-runtime-2026-10.md) |


## 2026-11-07 回灌：Runtime 第二周验证结论（2 条新增 + 1 条补充）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Google Agent Substrate（开源，agent-substrate/substrate）** | **TeamMind**（生命周期控制面设计基线：SuspendActor/ResumeActor + warm worker 解耦 K8s 调度；身份-egress 一体化可直接借用）/ **silver-shield**（actor 零凭据=被攻陷 agent 无可外泄对象；egress PEP 可挂 DLP/注入检测）/ **Tafcm**（反面参照：K8s 集群依赖重，离线优先不适用） | Runtime D/E/F 层（gVisor/microVM 双沙箱、短时 SPIFFE+per-actor JWT、credential provider 外注、request parking 过载语义、10x 密度/<500ms resume 官方口径） | ✅ **已验证（11-06 代码级：go build 通过+API/组件/文档核对；集群实测受限）** | 见能力树锚点表（无独立卡，二号锚点直接入树） |
| **OpenKruise Agents v0.6.0（CNCF，K8s 原生 agent 沙箱）** | **TeamMind**（若走 K8s 路线：CheckpointRestore 升级策略+PauseStrategy 两档+Commit CRD 即生产级生命周期原语）/ **silver-shield**（Security Identity Provider 在 resume/clone/CSI 重挂时重签 token，防旧身份复用） | Runtime F 层（Stop=删 Pod vs Hibernate=保留 rootfs/内存；PersistentContents 含 gpuMemory；两阶段 SandboxUpdateOps；SecurityProfile 含 MCP 工具访问控制） | ✅ **已验证（11-06 源码级：CRD/CHANGELOG 核对；PauseStrategy 以代码为准修正 blog 转述）** | [sandbox-lifecycle-suspend-resume-2026-11](../03_expansion_queue/candidates/[cand]sandbox-lifecycle-suspend-resume-2026-11.md) |
| **Durable Execution 品类卡（补充）** | **TeamMind**（新增判定：生命周期 API 应与 sandbox 实现解耦——Substrate/OpenKruise 两条实现佐证「控制面独立」优于把 checkpoint 绑死单一实现） | Runtime A/F 层（恢复语义两派之外补「控制面 vs 数据面」维度） | 🟡 维持观察（§5 补 2 条实现佐证，不升格） | [durable-execution-category-mainstreaming-2026-10](../03_expansion_queue/candidates/[cand]durable-execution-category-mainstreaming-2026-10.md) |

## 2026-11-14 回灌：Memory 周验证结论（2 条新增 + 1 条修正）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Mem0 OSS（`mem0ai 2.2.1`）本地可跑形态** | **Tafcm**（本地记忆层最低成本参照，但不建议先上：qdrant 本地路径 + 假 LLM/embedder 才能零云跑通）/ **TeamMind**（写入确认语义：`add()` 回执不可信，须查 `get_all`）/ **silver-shield**（"回执≠落库"作为新的检测项） | Memory B1（单遍 ADDITIVE 抽取）/ C1（向量+关键词混合）/ D1（`expiration_date` TTL）/ F4（写入审计：回执与状态不一致） | ✅ **已验证（11-13 本地实跑：add→get_all 2 条→search 0.837；依赖无图库）** | [agent-memory-2026](../03_expansion_queue/candidates/[cand]agent-memory-2026.md) |
| **EvolveLab（MemEvolve 的 12 基线统一实现）** | **引擎 / Validation**（记忆架构横向对照台：同一接口换 13 个 provider）/ **GrowthOS**（记忆结构可按任务域元进化，而非一次选型定终身） | Memory A5（分层映射可比）/ D3（巩固重组可被"进化"搜索）/ 评测方法论（跨基准/跨 backbone 迁移证据） | 🟡 **结构验证（13 providers / 统一接口核对；未跑行为，需 API keys + 三套数据集）** | [agent-memory-2026](../03_expansion_queue/candidates/[cand]agent-memory-2026.md) |

> **修正（同日）**：`agent-memory-2026` 连接行仍有效，但卡内 Zep「Community Edition 开源（10-29）」判定**作废**——CE 公告实为 2024-09-26 且已 deprecated，开源线只剩 Graphiti（自建需 Neo4j 5.26+/FalkorDB + Redis）；`getzep/zep` 是 examples 仓库，不是产品代码。连接关系不变，证据口径已更正。

## 2026-11-16 建基线：Memory 信任边界与作用域（2 条新增）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Trojan Hippo / PASB / OWASP AMG（写入门控三件套）** | **Tafcm**（只存明确表达 + 已确认事实，推断标记 `inferred` 且默认不读回）/ **silver-shield**（provenance、note 权威度异常、自强化循环检测）/ **GrowthOS**（append-only ledger 防改写） | Memory **B5 写入门控** / **F1.2 休眠载荷** / **F3.1 主张升级** / **F4.1 provenance**；SIx 的"诚实降级"在此延伸为"来源降级"：读回时保留原话/推断/已验证三级 | 🟡 证据到账（论文摘要级）；11-20 本地复现 | [agent-memory-trust-boundary-2026](../03_expansion_queue/candidates/[cand]agent-memory-trust-boundary-2026.md) |
| **MemLeak（检索后 ownership gate）** | **TeamMind**（多租户双层强制：查询 filter + 检索后硬门；空 filter 禁止）/ **Tafcm**（单用户保留 `user_id` 字段，多档案时启用）/ **silver-shield**（跨 scope 命中计数作检测信号） | Memory **E4.1~E4.3** / **G3 命名空间隔离**；"共享 embedding 空间即共享侧信道"，filter 不足、gate 才有效（1.4 ms 代价） | 🟡 证据到账（论文摘要级）；11-20 串读实测 | [agent-memory-trust-boundary-2026](../03_expansion_queue/candidates/[cand]agent-memory-trust-boundary-2026.md) |

## 2026-11-17 增量：把"防御的代价"做成指标（1 条新增）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Price of Safety（防御良性代价三读数）** | **silver-shield**（新增"防御自身指标"面板：fire rate / withheld rate / token overhead；只报 ASR 视为未评估）/ **Tafcm**（读回过滤只按来源等级与 scope，不按语义相似度删）/ **TeamMind**（读时 gate 只判 ownership，不做内容相关性裁剪） | Memory **F4/F5** 与 **C4 证据保留**；防御验收从"挡住多少"改为"良性流量动了什么"；读时相关性过滤 = 用相关性冒充安全（2.2% → 14.9%） | 🟡 证据到账（论文摘要级）；11-20 观测项 | [agent-memory-trust-boundary-2026](../03_expansion_queue/candidates/[cand]agent-memory-trust-boundary-2026.md) |

## 2026-11-18 增量：记忆后端的成本维度（1 条新增）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **Mem0×Graphiti 成本/精度对照（2601.07978v2）** | **Tafcm**（本地记忆后端默认向量、图记忆按需而非默认；多跳时序查询确实是需求再引入 Graphiti，且要单列成本）/ **silver-shield**（"能删、能证"优先于"能连图"：回执与审计是安全项，图谱是能力项） | Memory **C2 图检索**与 **B1 写入策略**：图记忆的价值在时序推理而非精度；选型必须把加载/资源/网络成本计入 | 🟡 单一测试床，非验证 | — |

## 2026-11-19 增量：安全门只认执行台账（1 条新增）
| 外部对象 | 连接的项目 | 连接的知识点 | 状态 | 候选卡 |
|---|---|---|---|---|
| **PoEM（执行回执防御）** | **silver-shield**（安全动作门判据从"记忆/上下文声明"改为"签名执行台账"；台账与记忆的写权限必须分离）/ **Tafcm**（记忆=可错叙述、执行台账=事实；"上次已处理"只作提示不作跳过依据）/ **TeamMind**（共享记忆带 source_class 与派生边，敏感动作验祖先是否 External） | Memory **F1.1 休眠载荷 / F5.2 删除回执** 与 **H3 降级诚实**：检测措辞是伪防御（一次改写即归零），防御对象是动作不是文本 | 🟡 论文 + MIT 代码，未复现 | [agent-memory-trust-boundary-2026](../03_expansion_queue/candidates/[cand]agent-memory-trust-boundary-2026.md) |

## 2026-11-20 实测回灌：声明层与验证层分家（3 条新增）
- **delete 回执 → silver-shield / Tafcm**：`{"message":"successfully"}` 只能证明"调用没报错"。silver-shield 的删除校验必须自己出可核验回执（id + scope + 内容哈希 + 时间 + 覆盖范围），不能信 SDK 返回值；Tafcm 删除 note 后要直接查 history/索引残留。
- **单一明文存储 → TeamMind**：Mem0 qdrant 本地路径是单文件，`scroll` 可一次读出所有 user 明文。团队共享 bank 必须"一租户一库/一密钥"，不能靠应用层 filter 当隔离；备份与快照按同等密级管理。
- **scope 强制 filter → Tafcm / TeamMind**：Mem0 2.2.1 `filters=None` 直接报错，是可借鉴的"默认拒绝"设计；Tafcm 单用户也保留 `user_id` 必填，TeamMind 的检索入口禁止无 scope 调用。

## 2026-11-21 回灌：门控的位置比门控的强度更重要（2 条新增）
- **直写旁路 → Tafcm / silver-shield**：Mem0 `infer=False` 使抽取门控完全失效，poison 原样落库并命中 0.8。Tafcm 生产只保留一个写入口，调试/批量直写不进常驻进程；silver-shield 把"配置里存在绕过抽取的门控"作为**配置类缺陷**检测项（确定性，不依赖 LLM）。
- **回执可核验率 → silver-shield / TeamMind**：11-17 的三读数（ASR / 良性触发率 / 扣留率）扩为**四读数**，第四项=回执是否含 `id + scope + 哈希 + 时间 + 覆盖范围`，缺一项记 0。TeamMind 的删除 API 对外只暴露可核验回执，内部 SDK 的 `successfully` 不外传。

## 2026-11-22 小结：交给 Computer Use 周的三条判据（3 条）
- **动作门控位置 → Computer Use / Browser 能力树（B/E 层）**：Memory 的结论"门控强度=入口唯一性"在真实环境执行里等价于"执行通道是否唯一"——只要有不受门控的点击/输入/本地端口通道，上层策略即装饰。周一起草能力树时把"通道枚举"作为必填项。
- **判定依据外部 → C 层（感知与自验证）**：Mem0 的 `successfully` 证明"调用没报错 ≠ 状态正确"。浏览器/桌面动作的成功判据只能来自执行事实（DOM 变更、下载落盘、进程退出码），不能来自页面自述或 agent 自述。
- **回执可核验 → H 层（可观测与回放）**：动作回执须含目标（URL / DOM 路径 / 进程）+ 时间 + 结果哈希 + 覆盖范围；与 Memory 五字段回执同构，可直接复用为验收模板。

## 2026-11-22 兜底：AI 网关 = 凭据集中点（2 条）
- **LiteLLM 漏洞族 → silver-shield / TeamMind（运行时身份 R 层）**：gateway 一旦被碰，`LITELLM_MASTER_KEY` + 全部 provider key 一次性交出。加固的第一杠杆不是打补丁而是**凭据外注/短时令牌**——与 Runtime 周 Substrate "零凭据执行 + egress PEP" 直接同构，可在 silver-shield 落成检查项。
- **"披露 ≠ 在野" → 事件判读纪律（MCP / 网关 / 浏览器控制面通用）**：40217 从报送（2-13）到 KEV（11-18）用了 7 个月；只有 KEV / 蜜罐探测 / 厂商确认"已利用"才算在野。与"策略存在 ≠ 策略生效"同类：**公告存在 ≠ 有人在打**。

## 2026-11-23 基线：真实环境操作的三个连接（3 条）
- **"代码即动作" → E2E-CLI（产物形态）**：browser-use 1.0 与 Webwright 独立收敛到"持久物是脚本/代码而非会话"。E2E-CLI 的 E2E 资产应改为可复用脚本 + 外部断言；会话回放只作调试，不作证据。
- **"确认点绑不可逆动作" → campus_order / silver-shield（人机交接）**：BioShocking 6/6、弹窗 ASR 86%、Invisible Ink 低害目标不可区分 → "敏感动作需确认"这一模糊规则无效，必须枚举：支付/发送/删除/授权/安装/外发文件。
- **"成功判据外部化" → Tafcm / Validation（回执）**：`success=True` 与 judge 自评都不是证据；与 Memory 周 F5.2 五字段回执同构，动作侧需"目标标识 + 前后状态 + 结果 + 覆盖范围"。

## 2026-11-24 增量：工具清单成为不可信输入（2 条）

- **WebMCP 页面声明工具** → E2E-CLI / silver-shield / campus_order：动作空间从"操作 UI"变成"调用页面给的契约"；注入面**前移到工具清单**（读 description 时即生效，执行之前），`tools/list_changed` 允许页面中途改写 agent 的动作面；`execute` 返回值是页面自证而非外部事实 → E2E 断言仍须独立。🟡 新建 A 卡 [`webmcp-page-declared-tools-2026`](../03_expansion_queue/candidates/[cand]webmcp-page-declared-tools-2026.md)
- **browser-use 1.0.8 的自我揭短** → Tafcm / E2E-CLI：官方承认 `Browser('chrome')`/`profile=` 打开 **127.0.0.1 无认证调试端口**（同机用户可接管登录态），且 `sensitive_data` 明写"非沙箱、模型可读" → 判断 7（隔离最小单位是 profile）由"待验证"升为**厂商自述**，部署默认应改 `Browser('chromium')`（一次性临时 profile）。🟡 增量并入 S 卡 [`computer-browser-use-2026`](../03_expansion_queue/candidates/[cand]computer-browser-use-2026.md)

## 2026-11-25 增量：桌面的表示、回执与回放（3 条）

1. **agent-desktop（a11y 树 + 快照 id ref）→ E2E-CLI 的断言粒度**：`@s8f3k2p9:e8` 里带快照 id，意味着断言可以绑到"某一版 UI"而不是"某个坐标"；`STALE_REF` / `AMBIGUOUS_TARGET` 是可直接映射的失败类，不需要靠截图 diff 猜。→ 桌面 E2E 落地路径：**脚本 + ref 断言 + SoR 校验**三层，缺一层就退化成 `success` 布尔。
2. **OpenAdapt 的 54/90 → 0/90 → campus_order 的确认点设计**：屏幕断言会静默放过六成注入故障，只有 system-of-record 读路径是 0。这给"支付/提交/删除"类动作定了硬要求：**效果声明 + 外部校验 + 核验失败即拒绝**，而不是"点完看弹窗"。
3. **EchoPath 的 IBTR 重瞄 → silver-shield 的新检测面**：回放的"目标重解析/repair"是可被诱导的环节——屏幕上放一个更显眼、同名的假控件，重瞄就会把动作改道。与 WebTrap"把攻击目标变成任务前置条件"同机制；检测项应包含"重瞄依据的是哪一帧证据、repair 是否留痕"。

## 2026-11-26 增量：控制面的三个触发者（3 条）

1. **`127.0.0.1` ≠ 安全 → silver-shield 的端口基线要带"触发者"字段**：同机进程、浏览器内网页、公网是三套威胁；只记"是否 loopback"会把 DNS rebinding（chrome-devtools-axi / Playwright MCP）与扩展中继（OpenClaw `/cdp`）都判成安全。检测项应写成「地址 + 是否校验 Host/Origin + 是否有 per-session token + 凭据面级别」四元组。
2. **P5 扩展权限组合 → TeamMind 的授信单位**：`debugger + cookies + <all_urls>` 三项合起来等价于完整 RAT 能力，但每一项单看都"合理"。多 agent 体系给组件授信时必须按**能力组合**评估，不能按来源（"厂商官方扩展"）或单项权限放行；且授权粒度要能按域名/动作收窄，否则就是整段会话的 open-ended 授权。
3. **P7 运行时解密 → 审查点前移**：SkillLeak 的能力不在 install hook，而在 `connect()` 首次指向真实浏览器时。skill 审查因此要加"首次调用行为"与"MCP 返回值是否含明文凭据"；同一条也适用于 E2E-CLI 的插件加载链。

## 2026-11-28 回灌：Computer Use 周验证结论（4 条）

1. **校验要按「入口 × 部署形态」二维清点 → silver-shield 检测项模板**：三例同构——P8（Playwright MCP 的 Host 检查只对 loopback 绑定生效）、jupyter CVE-2026-77359（`/mcp` 有 Host/Origin 校验而 `/api/connect`、`/api/stop` 没有）、CSA 11-09 综述里的 SDK（本地 HTTP 默认不开 rebinding 防护）。三条都不是「没有校验」，而是「校验覆盖范围 < 攻击可达范围」。检测项因此不能写「是否校验 Host/Origin」，要写成四元组表格：**覆盖哪些路由 / 在哪些 bind 与传输模式下生效 / 未覆盖时返回什么（放行还是报错）/ 谁能触发未覆盖的那个入口**。✅ 依据 `[cand]local-control-plane-exposure-2026-11`（9 模式）+ CVE-2026-77359。
2. **判分的独立性取决于上下文是否共享 → E2E-CLI / Tafcm**：browser-use 的 `judge_cached` 把 judge 当作 run 的再一轮（复用 run 的 messages/instructions/tool definitions 吃 prompt cache）→ judge 与 actor 同前缀，等于自己给自己判卷。`judge_context` 让用户把判据喂进去，但判据仍由同一模型解释。E2E 的成功判定必须由**不共享上下文**的进程执行（独立 runner + 外部 SoR），否则「判据可注入」会被误当成「判定依据外部」。✅
3. **产物持久等级就是证据上限 → E2E-CLI / Tafcm**：会话 < 脚本 < 代码+执行记录 < 外部 system-of-record。browser-use 第三级（`state/cells/NNNN.txt` 代码+输出、跨 run 续编号）、Webwright 第二级（脚本+diff）、Playwright MCP 的 ref 不构成持久物。E2E 资产归档必须标等级，**低于第三级不进 CI 证据链**；判据「回执可核验」先问载体在哪一级。✅
4. **「部署形态」是必须显式登记的配置项 → Tafcm 本地部署 / campus_order**：同一个 MCP server，stdio 与 `streamable-http` 是两套信任模型（jupyter 的漏洞只落在后者）；`--host 0.0.0.0` 与默认 loopback 是两套校验（P8）。部署清单要写死三件事：**绑定地址 + 传输模式 + 该模式下哪几条校验实际生效**，并逐条在目标形态下复验——「默认安全」只在默认形态成立。✅

## 2026-11-29 周小结：Computer Use → AI Infra 的三条交接（3 条）

1. **「入口 × 部署形态」清点法直接迁移到本地推理服务 → Tafcm 本地部署**：判断 9 在 Computer Use 周由三例同构逼出来（P8 只对 loopback 生效 / jupyter 只对 `/mcp` 生效 / SDK 本地 HTTP 默认无防护）。本地推理同一问题：`--host 0.0.0.0`、OpenAI 兼容端点、无 API key、`/metrics` 裸奔。验收提问不变：覆盖哪些路由 / 哪种 bind 生效 / 未覆盖时返回什么 / 谁能触发。✅ 依据 `agent-computer-use.md` 判断 9。
2. **bench 数字默认按「包级」看待 → Tafcm / E2E-CLI**：判断 11 的证据深度分级（包级 < 源码级 < 实跑）落到性能域就是：厂商宣称的 tokens/s、量化收益、显存占用，在没有本机可复现命令 + 原始输出前一律算包级。E2E-CLI 的回归基线同理——「比上版快 20%」若无同机同参数记录，不进结论。✅
3. **量化与 offload 的「默认值即结论」→ Tafcm 6GB 显存约束**：vLLM 0.34.0 把 `gpu_memory_utilization` 默认拉到 1.0、`block-size` 默认 16→64，这类默认值在 6GB 卡上直接决定 OOM 与否；与判断 9 同构——**默认值只在默认硬件成立**。验收提问：这条默认值在什么显存/后端/精度下退化为错误配置。✅ 依据 `[cand]local-edge-llm-2026` + vLLM 0.34.0 release。

## 规则

- 只有进入 `03_expansion_queue/validated` 的对象才能把状态改为 ✅（绿）。
- 🟡 = 已有候选证据卡、证据充足但尚未完成真机验证。
- ⬜ = 尚未扫描，仍为 Bootstrap 期的连接假设。
- 连接卡不重复写对象的基础介绍，只写连接关系。
- 全量对象清单、生命周期与去重基准见 `06_expansion_index/README.md`。
