# Personal Tech Radar 兜底扫描 · 2026-11-18（06:00）

> 深耕领域：**Memory 第二周**（细节不重复）。本任务只找**领域外 S/A 级重大突发事件**。

## 一、检索（2 路 + 1 次定向核对）
1. MCP / Model Context Protocol security advisory CVE（近一周）
2. Agent 框架重大版本 / 路线变更（LangGraph / OpenAI Agents SDK / A2A / MAF）

## 二、判定表

| # | 对象 | 事实 | 判定 |
|---|---|---|---|
| 1 | **CVE-2026-104850**（MCP TS SDK OAuth 客户端，CWE-345/522） | >=1.12.0,<1.31.0 与 >=2.0.0,<2.2.0；server 决定授权服务器，无交互外送 refresh_token/client_secret；修复 1.31.0 / 2.2.0；CNA CVSS **7.5**；SSVC automatable=yes | **A｜并入 S 卡（事件日 21）** |
| 2 | **CVE-2026-110279**（IBM ContextForge MCP Gateway，CWE-287） | v1.0.0–v1.1.0；`X-Upstream-Authorization` → `Authorization` 恒改名，已认证用户可覆盖网关上游凭据、绕过权限与审计；修复 v1.1.1（PR #7341）；CVSS **8.1**；公告 11-12 | **A｜并入 S 卡（事件日 21）** |
| 3 | CVE-2026-104120（mcp_server_fetch SSRF） | 公开可利用、修复 PR 未合 | B，记日志不立项 |
| 4 | EUVD-2026-117801 | = CVE-2026-116684（事件日 20） | 去重 |
| 5 | LangGraph v1.2.0（DeltaChannel / 节点超时 / 流式 v3） | 11-11，已记 B | 已知 |
| 6 | MAF Python 2026 显著变更 / A2A SDK v1.0 迁移 | 已知对象（MCP 2.x / A2A run-context allowlist） | 已知 |
| 7 | OpenAI Agents SDK 0.24.0（10-15） | 普通版本增量 | 不写 |

## 三、核心判断
1. **MCP 信任根正从"工具"转向"授权服务器 + 网关"**：客户端把 refresh_token 交给哪个 AS，由 server 的 metadata 决定；网关把上游凭据交给谁，由请求头决定。
2. **事件日 19/20/21 三日连续同一缺陷族**：request-id 未绑连接、token 未绑 audience、凭据未绑 issuer/资源。**身份 → 资源边界缺一层强制绑定**。
3. 网关成为凭据代理单点：能转发 + 能持有凭据 + 能改写头，三者叠加即高危；打穿的不只是权限还有审计归因。
4. 修复均非"升级即完"：104850 的 1.x 无 `expectedIssuer`，只能只连可信 server；110279 需确认前置代理不再透传该头。

## 四、限制
- 104850：NVD 全文（版本/评分/SSVC 完整），GHSA 与 release note 未读，未复现。
- 110279：IBM 公告全文，NVD 记录与 PR diff 未核。
- 104120：仅 NVD 片段。

## 结论
**Changed**（事件日 21 两条 A，并入既有 S 卡；无新建卡）
