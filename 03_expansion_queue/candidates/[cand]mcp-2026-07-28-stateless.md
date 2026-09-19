# 候选证据卡 · [cand] MCP 2026-07-28 无状态协议

> 状态：`[cand]` ｜ 关联方向：Top20 #1（MCP 生态） ｜ 日期：2026-09-01

## 一句话定位
MCP 协议发布史上最大版本 `2026-07-28`：从有状态双向协议转型为**无状态 request/response 协议**，成为可水平扩展的企业级 Agent 基础设施。

## 1. 它解决什么问题
- 旧版有状态会话（initialize/session）导致服务器无法放在普通负载均衡后，扩容与可靠性受限；
- 授权接入成本高（DCR 动态注册、redirect_uri 兼容问题）；
- 服务端主动调用（sampling/elicitation/roots）依赖常开双向流，不利于基础设施部署。

## 2. 为什么现在值得关注（活跃度证据）
- 官方发布：2026-07-28 正式发布（发布距今仅 1 个月）["https://blog.modelcontextprotocol.io/posts/2026-07-28/"]
- **雷达增量（2026-09-02）**：2026-08-22 官方发布 final 后新 Roadmap，宣告 2026-07-28 已落地 transport 演进等核心目标，转向"agent 通信 / 治理成熟 / 企业就绪"下一阶段["https://blog.modelcontextprotocol.io/posts/mcp-roadmap/"]；go-sdk 已按 Stateless 新规发布（2026-09-01）["https://github.com/modelcontextprotocol/go-sdk/releases"]
> **雷达增量（2026-09-20，扩展框架与统一传输）**：
> - **MCP Roadmap 统一传输方向（08-22）**：本地 server 用 **Streamable HTTP over stdio**——全部部署模式统一到一种传输，简化 server/client 实现["https://blog.modelcontextprotocol.io/posts/mcp-roadmap/?ref=upstract.com"]
> - **SEP-2663 Tasks 扩展正式化（08-28）**：长运行任务的协议级扩展（tasks/get、tasks/cancel），与 2025-11-25 Tasks 规范兼容路径——"长任务"成为一等协议能力["https://modelcontextprotocol.io/seps/2663-tasks-extension"]
> - **MCP Apps（UI 扩展）落地（09-14 extensions overview 更新）**：server-rendered UI 扩展（io.modelcontextprotocol/ui）+ 扩展框架（settings schema + 优雅降级）——**MCP server 从"工具"扩展到"界面"**["https://modelcontextprotocol.io/extensions/overview"]
> - **AWS 企业部署指引（09-01）**："MCP went stateless: Is your AWS MCP server deployment well-architected?"——协议声明缓存（ttlMs/cacheScope）成为企业架构规范输入["https://aws.amazon.com/blogs/architecture/mcp-went-stateless-is-your-aws-mcp-server-deployment-well-architected/"]
> - **含义**：① MCP 生态进入"**扩展框架成熟 + 传输统一**"阶段——Tafcm/TeamMind 按 2026-07-28 做 server 时可同步采用 Tasks 扩展（长任务）与 Streamable HTTP over stdio；② MCP Apps 的"server 渲染 UI"与 agentic-ux 卡的 MCP Apps 模式互证——界面标准化继续推进
- Tier1 SDK（TS/Python/Go/C#）月下载合计近 5 亿，TS 与 Python SDK 各自累计下载已破 10 亿["https://blog.modelcontextprotocol.io/posts/2026-07-28/"]
- AWS（Bedrock AgentCore）、Cloudflare（Agents SDK 首发支持）、Google Cloud、Figma、Sentry/Linear、honeycomb（20% 交互查询来自 Agent）等企业级背书["https://aws.amazon.com/jp/blogs/machine-learning/how-agentcore-gateway-supports-the-mcp-2026-07-28-spec/"]["https://blog.modelcontextprotocol.io/posts/2026-07-28/"]
- 官方 Registry 已收录数千 server（Anthropic/GitHub/PulseMCP/Microsoft 背书），Registry 仍 Preview["https://registry.modelcontextprotocol.io/"]

## 3. 与我的连接
- **连接的项目**：Tafcm（ADI 诊断接口）、agent-attention（通知基础设施）、TeamMind（多 CLI 编排）、OpenClaw（Skills/ClawHub）
- **连接的知识点**：Agent 五维模型之 Tool System、EP 原则、工具档案（OpenClaw Skills 即 MCP 兼容体系）
- **潜在收益**：把"我怎么做 Tool System"升级为"行业标准怎么做"；Tafcm/agent-attention 可直接按新规做 MCP server/client

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | 官方博客 https://blog.modelcontextprotocol.io/posts/2026-07-28/ ｜ Spec https://modelcontextprotocol.io/specification/2026-07-28 |
| 证据等级 | FACT（官方发布 + 生态伙伴联名背书） |
| 验证方式 | 精读迁移说明（breaking changes）→ 用我的五维模型对照评估 → 写一个最小 stateless MCP server probe |
| 预期完成时间 | 2026-09 内 |

## 5. 关键变化速记（供后续精读）
- 取消 `initialize/initialized` 与 `Mcp-Session-Id`；请求自带 `_meta`（协议版本/客户端身份/能力）
- 新增 `server/discover` RPC（可选）；MRTR 取代服务端发起的 elicitation/sampling/roots
- 头路由：`Mcp-Method` / `Mcp-Name`；list 结果可缓存（ttlMs/cacheScope）
- 授权：RFC 9207 iss 校验；DCR 向 CIMD 迁移；凭证绑定 issuer
- Tasks 移入 `io.modelcontextprotocol/tasks` 扩展；Roots/Sampling/Logging 废弃（12 个月窗口）；HTTP+SSE 旧传输废弃

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据，含一次真机验证）
- [x] 维持观察（待完成 stateless probe）
- [ ] 拒绝
