# Personal Tech Radar 兜底扫描 · 2026-11-19（06:00）

> 定位：全领域轻量安全网，只捕当前深耕（Memory）之外的 S/A 级重大突发事件。

## 一、检索（2 路 + 3 次定向核对）
1. MCP security vulnerability CVE November 2026
2. AI agent framework major breaking release November 2026
3. 定向：EUVD-2026-117801 全文、CVE-2026-41902 一手核对、servers #5491 / Windows-MCP 核对

## 二、判定表

| # | 对象 | 事实 | 判定 |
|---|---|---|---|
| 1 | **CVE-2026-111771（MCP TS SDK audience）** | sdk 1.6.0–1.32.0 / server 2.0.0–2.3.0 / express 2.0–2.0.2 / server-legacy 2.0–2.3.1；bearer 不校验 aud；CVSS 6.8；修复 1.32.0/2.3.0/2.0.2/2.3.1；**升级后需显式开 audience** | **A｜事件日 22** |
| 2 | **CVE-2026-48989（Windows-MCP）** | HTTP 无认证 + 通配 CORS + PowerShell 工具 = 本地任意命令执行，浏览器可跨域触发 | **A｜事件日 22** |
| 3 | **CVE-2026-41901（mcp-server-sqlite）+ 同批 7 CVE** | write_query 只读 allowlist 被 VACUUM INTO 绕过；含 Desktop Commander | A−｜并入 |
| 4 | CVE-2026-41902 | 一手核实为 FreeScout 邀请哈希（9.1），**非** mcp-server-git | 纠错不采信 |
| 5 | GPT-6.2 Astra/Sol（11-17） | 仅二手聚合稿（头条转述），UK AISI "85% 轨迹考虑被对齐测试" 未取一手 | B｜不写 |
| 6 | LangGraph 1.2.22、MAF 1.24.0、OpenAI Agent Builder 11-30 下线 | 已知或普通增量 | 不写 |
| 7 | 116684 / 125926 / 104850 / 110279 | 事件日 20/21 已收 | 去重命中 |

## 三、核心判断
1. **参考实现不是安全实现**：MCP 官方 servers 与常见本地方案自身批量中招，"官方即可信"的装机假设失效。
2. **本地 agent 控制面是独立高危面**：无认证 + 通配 CORS + 高危工具三者叠加，等于浏览器可触发的本地 RCE。
3. **"升级即修复"第三次失效**：111771 升级后仍须开配置；与 104850（只能只连可信 server）同构。
4. **二手博客的 CVE 编号不可信**：41902 张冠李戴；事件必须回一手 advisory/NVD。

## 四、限制
- 111771 为 EUVD 全文（GHSA/release note 未读）；48989 仅 PyPA advisory YAML（NVD/CVSS 未取）；41901 与"7 CVE"仅二手汇总。
- 三件均未复现，无在野利用证据；本批为补捕（11-08~11-11 披露，11-08 兜底当时 No Action）。

## 结论
**Changed**（S 卡事件日 22 + 一处编号纠错；无新卡）
