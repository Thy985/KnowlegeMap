# Personal Tech Radar 兜底扫描 · 2026-11-16（周一 06:00）

> 定位：安全网。当前深耕领域 = **Memory 第二周**（F/E 层），本任务只抓该领域之外的 S/A 级重大突发事件，领域内与普通增量不写。

## 一、检索（3 路，轻量）
1. MCP 规范重大变更 / 安全事件
2. Agent 框架重大版本 / 破坏性变更
3. AI Infra / runtime / computer-use 重大事故

## 二、判定表

| # | 对象 | 事实 | 判定 |
|---|---|---|---|
| 1 | **CVE-2026-111770**（MCP 官方 TS SDK） | `@modelcontextprotocol/server` 2.0.0–2.3.0：多客户端共用一个 stateless HTTP transport / Server 实例时，响应与通知**投给错误客户端**；JSON-RPC id 从 0 起导致正常并发即碰撞；2.3.0 修复但**需改代码**；stdio 与 per-call 工厂不受影响；NVD **CVSS 未评估** | **A｜写入既有 S 卡（事件日 19）** |
| 2 | MCP 规范版本 | 仍为 **2026-07-28**（无状态核心 + Extensions + Tasks + MCP Apps），无新版本/路线变更 | 无新增 |
| 3 | MAF `Migrate to MCP 2.x`（11-11） | SDK 2.x 生命周期、`unsafe_extra_run_args`、AG-UI endpoint、A2A run-context allowlist | 已知对象执行确认（B，不写） |
| 4 | **Microsoft Agent 365 SDK 2.0**（11-06） | 破坏性变更集中在已弃用的 observability 包，均有迁移路径 | B（仅记日志） |
| 5 | Foundry hosted agents 迁移（11-10） | 框架适配包（agentframework/langgraph）被协议库（responses/invocations）替代 | B（仅记日志） |
| 6 | LangGraph changelog（11-11） | DeltaChannel beta、节点超时/恢复、流式 v3 | **已于 11-09 兜底记为 B**，去重命中 |
| 7 | OpenAI × Hugging Face 沙箱逃逸 / Fireworks 第二起入侵 | 已被事件日 13/14/16 覆盖，含官方复盘与 HF 时间线 | 去重命中，不重复写 |

## 三、为什么不新建卡
CVE 属既有安全 S 卡 `[cand]agentic-attack-2026.md` 的事件流；按既有纪律「安全域事件合并，不建碎片卡」，追加为**事件日 19**，不改卡状态（仍 S，验证计划不变）。

## 四、核心判断
1. **无状态化 ≠ 隔离**：MCP 2026-07-28 去掉了会话状态，但「单实例复用 + request-id 从 0 起」成了新的跨租户边界；响应投错人比会话劫持更隐蔽。
2. 修复粒度为**构造粒度**（per-request/per-session），网关鉴权救不了；这与 Memory E 层「filter 不等于 gate」同构。
3. 影响面被低估的常见部署：单容器网关、低代码平台、把 MCP server 当全局单例的宿主。

## 五、限制
- NVD 为唯一一手来源；CVSS 未评估、厂商公告/SDK release note 未取得、在野利用未知。
- 未做代码级复现（需 TypeScript 环境与多客户端 HTTP 场景），本轮只做记录。

## 结论
**Changed**（既有 S 卡新增事件日 19；无新卡）
