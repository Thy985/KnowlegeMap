# 2026-11-21 Personal Tech Radar 兜底扫描（全领域）

- 聚焦领域：Memory（第二周 Day6 回灌完成，细节由深耕任务负责，本任务不重复收集）
- 扫描方式：2 路 search（MCP security CVE / agent framework 重大版本）+ 3 次一手 fetch（AWS 2026-179 全文、NVD 112136、NVD 125271）+ 定向 grep 去重
- 判定 6 行，写 3 条 A（A−1 条），合并入 `[cand]agentic-attack-2026.md` 事件日 24；另做 1 处订正

## 入库
1. CVE-2026-100307（AWS mcp-gateway-registry，A）：`>=1.0.9,<=1.24.7` → 1.25.0；外部管理 API 只认证不判权，`groups/import` 自映射到 `mcp-registry-admin`；升级不回改历史映射/不失效旧凭据。
2. CVE-2026-112136（Mendix Studio Pro 11 MCP Server，A）：CWE-1327 未限 loopback；CVSS 4.0 9.2 CRITICAL（CNA Siemens）。
3. CVE-2026-125271（aws-api-mcp-server，A−）：`>=0.2.13,<1.5.1` → 1.5.1；操作名归一化错误 → denyList/elicitList 静默不匹配；CVSS 4.0 8.5（CNA AMZN）。

## 订正
- CVE-2026-111770（事件日 19）：NVD 现由 CNA GitHub 给出 CVSS 3.1 7.7 HIGH，NVD 自身未评估；影响面与修复不变。06 index 原「CVSS 未评估」已改。

## 不写
- CVE-2026-116635（AWS Serverless MCP Server 路径穿越，<v0.2.1）— B
- CVE-2026-117567（esp-mcp 命令注入，8.5）— B（单人项目、无生态影响）
- MAF .NET `A2AAgentOptions` 破坏性重构（#10113）、A2A 包 1.0.0-preview4（#9995）— 已知 A2A v1 迁移线，普通增量

## 结论
**Changed**（事件日 24，3 条 A 合并入既有 S 卡，无新建卡）。核心判断：策略存在 ≠ 策略生效；网关管理员是持凭据的单点；本地 MCP listener 仍被误当成本地。
