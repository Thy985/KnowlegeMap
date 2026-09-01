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
