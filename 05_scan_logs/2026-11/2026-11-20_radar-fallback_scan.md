# Personal Tech Radar 兜底 · 2026-11-20（06:00）

> 当前深耕：Memory（第二周）。本任务只捕获领域外 S/A 级重大事件。

## 扫描
2 路 search（MCP security CVE / agent framework 重大版本）+ 3 次一手核（NVD 116686、NVD 63118、EUVD 126629）+ 定向 grep 去重（116686 / 63118 / 115563 / MAF 1.28 / A2A Java 均无命中）。

## 判定 7 行
| 对象 | 级别 | 处理 |
|---|---|---|
| CVE-2026-115563（MCP Python SDK OAuth 凭据外送，7.5） | A | 写事件日 23 |
| CVE-2026-116686（Python SDK `$ref` SSRF，6.5） | B | 记日志 |
| CVE-2026-63118（Ruby SDK DNS rebinding，6.9，7-29 发布） | B | 记日志（旧洞补录） |
| MAF .NET 1.28.0（A2A 托管只返 message） | B | 不写 |
| A2A Java SDK 1.5.0.Final（破坏性变更） | B | 不写 |
| CVE-2026-111770 / 116684 / 104850 | 去重 | 已在事件日 19/20/21 |
| MCP 规范 | 无变更 | — |

## 判断
1. "服务器指定授权服务器"不是 TS SDK 单点 bug，Python SDK 自 1.9.1 起同样存在 → MCP OAuth 客户端模型级假设问题。
2. 第四次"升级不修复"：必须显式 issuer，存储的 registration 也要清空重注册。
3. 事件日 21~23 连成同一族：token 的 audience、凭据的 issuer 都没有绑定。

## 结论
Changed（1 条 A 并入既有安全卡；无新建卡）
