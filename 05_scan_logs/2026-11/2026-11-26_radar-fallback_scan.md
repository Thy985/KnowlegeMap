# 2026-11-26 Personal Tech Radar 兜底扫描

- 聚焦领域：Computer Use / Browser（第 1 周 Day4，安全主题）——由深耕任务负责，本任务不重复收集。
- 扫视范围：MCP / A2A 协议、主流 Agent 框架、AI Infra、Memory、本地边缘、Agent 安全；3 次 general_search + 2 次 web_fetch（NVD、CISA KEV）。
- 去重：`06_expansion_index` / `03_expansion_queue` / `08_agent_centric` 检索 `120779` / `ClawHavoc` / `Capsule` / `hackerbot` / `SGLang` / `CISA` / `KEV`。

## 判定

| 对象 | 档位 | 处置 |
|---|---|---|
| **VS Code MCP elicitation 通知注入 CVE-2026-120779**（1.0.0<1.145.3，CWE-94，CVSS 3.1 **9.6**，UI:R） | **A（领域外，补记）** | 并入 `[cand]agentic-attack-2026.md` 事件日 26；06 index 新段；_INDEX 行 |
| Capsule《The Agentic AI Threat Landscape Has Crossed a Threshold》（11 月） | B（综述） | 不写；为 2026 上半年战役综述，非新事件 |
| ClawHavoc（约 12% marketplace skill 感染）/ hackerbot-claw（MS/DataDog/CNCF CI/CD，Aqua Trivy 全仓接管） | 历史（2026 Q1） | 不写；已有 skill-supply-chain 卡覆盖 Unit 42 ClawHub 审计 |
| NEAR AI × SGLang RCE（11-08/09） | 已有 | 已事件日 16 |
| Cairn × MONAI Label（CVE-2026-133968） | 已有 | 已事件日 25；仅记 KEV 状态待核 |
| MCP 2026-07-28 规范 / MAF / Mastra / LangChain breaking changes | 普通增量 | 不写；均属已知对象版本线 |

## 一手事实（CVE-2026-120779）

- NVD：`CVE-2026-120779`，CWE-94，**受影响 Visual Studio Code 1.0.0 < 1.145.3**，CNA = Microsoft，CNA 评分 **CVSS 3.1 9.6**（`AV:N/AC:L/PR:N/UI:R/S:C/C:H/I:H/A:H`）；NVD 状态 "Awaiting Enrichment"，未独立评估；NVD 发布 2026-11-11。
- 机制（mallory.ai 摘要，MSRC 原文未取）：远端 MCP server 在无活跃 chat session 时发 `elicitation` → `McpElicitationService` 退化为 workbench notification → 渲染器把 server 字符串当 linked text，命令链接触发 workbench 命令；非字符串 message 可伪装内部结构。
- 缓解：无专门 workaround；`ChatMCP` 策略关闭 MCP，或 `registryOnly`；本地 stdio server 沙箱化**不覆盖**此路径（远端 server 触发的客户端渲染）。
- 影响：用户权限任意代码执行，不提权到管理员/SYSTEM。

## 未做 / 限制

- MSRC 公告原文未取；Capsule 报告"9.6 核心 MCP 基础设施"未点名 CVE，**未作同一性断言**。
- CISA KEV JSON 抓取只得到 `catalogVersion 2026.05.22`（count 1602）的陈旧快照，无法判定 CVE-2026-133968 是否入 KEV；NotebookCheck（11-24）称已列入，仍标待核。
- 未追普通 release：MCP 2026-07-28 后续、MAF 1.26/1.27、Mastra breaking changes、LangChain deepagents v0.7 均已知对象线。
