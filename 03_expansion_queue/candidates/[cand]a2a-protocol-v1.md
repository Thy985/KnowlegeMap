# 候选证据卡 · [cand] A2A 协议 v1.0 + Agentic AI Foundation

> 状态：`[cand]` ｜ 分类：多 Agent 编排 / 互操作协议（S5） ｜ 发现：2026-09-01 ｜ 等级：**S**

## 一句话定位
A2A（Agent2Agent）v1.0 于 2026-03-12 冻结，是"Agent↔Agent"的事实标准，与 MCP（Agent↔Tool）互补，共同构成 Agent 互操作地基；2026-08-17 与 MCP 同入 **Agentic AI Foundation（AAIF）**（250+ 成员，含 Google/MS/AWS/Anthropic/OpenAI）。

## 1. 它是什么 / 解决什么问题
- 解决"异构 Agent 之间如何发现、通信、协调、交易"——跨框架（LangGraph/CrewAI 等）、跨厂商、跨组织["https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year"]
- **v1.0 关键特性**：Signed Agent Cards（加密身份校验）、多租户、多协议绑定（含 gRPC）、版本协商、迁移路径["https://dailyaiworld.com/blogs/a2a-10-joins-agentic-ai-foundation-internet-agents"]
- **Agent Payments Protocol (AP2)**：Agent 驱动的安全交易，60+ 组织支持——A2A 从通信延伸到经济协调
- 心智模型：**MCP = agent-to-tool，A2A = agent-to-agent**（"Internet of Agents"）

## 2. 活跃度证据（2026）
- 150+ 组织支持（AWS/Cisco/Google/IBM/Microsoft/Salesforce/SAP/ServiceNow）；22K+ GitHub stars["https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year"]
- 已进 Azure AI Foundry/Copilot Studio、Amazon Bedrock AgentCore Runtime、Google 平台["https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year"]
- SDK 已扩展至 Python/JavaScript/Java/Go/.NET 五种语言
- IBM Research 的 ACP 已并入 A2A 路线图；ANP（W3C DID）作为开放互联网补充["https://zylos.ai/research/2026-04-18-agent-to-agent-interoperability-protocols/"]
- AAIF 成员从 <40 增至 250+（含 Anthropic、OpenAI、Bloomberg、Cloudflare、Shopify、Block）["https://bigaiagent.tech/ai-agent-interoperability-2026-a2a-joins-mcp/"]
- **雷达增量（2026-09-02）**：2026-08-17/18 Google 正式将 A2A 移交 AAIF（250+ 成员共同治理，与 MCP 同基金会）["https://dailyaiworld.com/blogs/a2a-10-joins-agentic-ai-foundation-internet-agents"]；Microsoft Agent Framework .NET 已同步更新 A2A v1 SDK（client 发现/托管）["https://devblogs.microsoft.com/agent-framework/a2a-v1-is-here-cross-platform-agent-communication-in-microsoft-agent-framework-for-net/"]
> **雷达增量（2026-09-16，实现成熟期）**：
> - **A2A Java SDK 1.3.0.Final（2026-08-27）**：多租户支持 + **授权模型默认 fail-closed** + 一批安全加固 + 全传输协议合规；含 breaking changes——官方 Java SDK 首个"安全默认"版本["https://a2aproject.github.io/a2a-java/posts/a2a-java-sdk-1-3-0-final-released/"]
> - **A2A Jakarta 1.0.0.Final（2026-09-10，WildFly）**：Jakarta 集成，支持 v1.0 协议的 JSON-RPC/gRPC/HTTP+JSON/REST 三传输 + v0.3 兼容层（同部署可服务两版客户端）["https://www.wildfly.org/news/2026/09/10/A2A-Jakarta-1-0-0-Final-is-released/"]
> - **Azure Foundry A2A 工具 GA（2026-09-15 更新）**：`a2a` 工具类型正式 GA（替代 a2a_preview）；incoming A2A 要求 responses protocol（不支持 SSE streaming）["https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/agent-to-agent"]["https://learn.microsoft.com/en-gb/AZURE/foundry/agents/how-to/enable-agent-to-agent-endpoint"]
> - **Fetch.ai A2A Outbound Adapter（09-13）**：uAgents 仓库集成 A2A 出站适配器["https://www.coindesk.cc/fetch-ai-releases-a2a-outbound-adapter-for-seamless-agent-integration-113112.html"]
> - **含义**：① A2A 从"规范冻结（v1.0/AAIF）"进入**实现成熟期**——企业级 Java SDK 落定 + Azure GA + Jakarta EE 生态；② **fail-closed 默认授权**是工程层安全信号（与 agent-firewall 品类"确定性"主线呼应）；③ TeamMind（Java）的 A2A 接入可直接基于 **Java SDK 1.3.0**（Agent Card/任务模型/多租户）落地，无需从零实现协议
> **雷达增量（2026-09-23，生态清单成型 + v1.1 路线）**：
> - **A2A Community Hub（09-02 更新）**：**13 个框架内置 A2A 集成**——ADK/Agno/AG2/BeeAI/CrewAI/Hector/LangGraph/LiteLLM/Microsoft Agent Framework/Noorle/Pydantic AI/Slide/Strands + 多社区 SDK——**跨框架互操作从"可能"变"默认"**["https://a2a-protocol.org/latest/community/"]
> - **A2A Roadmap v1.1（09-15 更新）**：**v1.1 协议增强**——细化 task timeline 规范、标准化事件过滤机制（向后兼容）、核心健壮性加固["https://a2a-protocol.org/latest/roadmap/"]
> - **AG2 A2A 模块（09-02）**：transport-agnostic——同一 agent 可经 JSON-RPC/HTTP+JSON(REST)/gRPC 三种传输服务，客户端按发布绑定选择["https://docs.ag2.ai/latest/docs/beta/a2a/overview/"]
> - **Microsoft Foundry A2A 双向打通（09-15）**：A2A 工具 GA（出站连远程 A2A 端点）+ **入站 A2A 端点启用**（Foundry agent 可被外部 agent 调用）——平台级双向互操作["https://learn.microsoft.com/en-us/azure/foundry/agents/how-to/tools/agent-to-agent"]
> - **含义**：① A2A 生态进入"**13 框架默认集成 + 平台双向打通 + v1.1 演进**"——TeamMind 接入成本进一步下降（Java SDK 1.3.0 + AG2 传输无关可作参考实现）；② v1.1 的 task timeline/事件过滤标准化 = 可观测性规范化（与 otel-genai 卡同向）；③ A2A 从"协议标准"变成"生态默认"，与 MCP 一起构成完整的 Agent 互操作地基

## 3. 与我的知识/项目关系
- **TeamMind（Java 多 Agent 团队运行时）** 直接受益：A2A 提供标准化的 Agent 发现/协作/任务模型，可与 MCP 一起成为 TeamMind 的协议层
- 补上 Project Landscape 结论「Agent 基础设施链缺协议标准层（MCP/A2A）」的另一半
- 与首轮 MCP 扫描形成完整互操作图景

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（Linux Foundation 官方 + 一手来源核验） |
| 来源 | https://a2a-protocol.org/latest/specification/ ｜ https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year |
| 验证方式 | 读 v1.0 spec → 设计 TeamMind 的 A2A 接入方案（Agent Card / 任务模型）→ 评估与现有 CLI 编排的取舍 |

## 5. 决策
- [ ] 晋升 validated（需 TeamMind 接入设计）
- [x] 维持观察
- [ ] 拒绝
