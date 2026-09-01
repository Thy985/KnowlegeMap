# 候选证据卡 · [cand] OWASP Agentic Security 体系（Top10 2026 + Skills Top10 + Secure MCP）

> 状态：`[cand]` ｜ 分类：AI 安全治理（S3）/ G1 声明未覆盖 ｜ 发现：2026-09-01 ｜ 等级：**S**

## 一句话定位
OWASP 为"自主 AI Agent"发布的整套权威安全框架：`ASI01-ASI10`（Agent 应用 Top10）+ `AST01-AST10`（Skills/工具 Top10）+ 官方《Secure MCP Server 开发指南》——这是我 G1 缺口（AI 安全攻防）最权威的入口，也直接给 MCP 扫锚定安全基线。

## 1. 它是什么 / 解决什么问题
- **OWASP Top 10 for Agentic Applications 2026**（ASI01–ASI10，2026 年初发布、全球同行评审）：Agent Goal Hijack、Tool Misuse、Identity/Privilege Abuse、Excessive Autonomy、Resource Exhaustion、Rogue Agent Generation、Sensitive Data Exposure、Model Theft 等——专门针对"多步自主行动、替用户做决策"的 Agent 风险["https://genai.owasp.org/initiatives/agentic-security-initiative/"]
- **OWASP Agentic Skills Top 10**（AST01–AST10，v1.0 目标 2026 Q3）：Over-Privileged Skills、Insecure Metadata、Untrusted External Instructions、Weak Isolation、Update Drift——专门针对"工具/Skills 供应链"["https://github.com/OWASP/www-project-agentic-skills-top-10"]
- **《Practical Guide for Secure MCP Server Development》+ 第三方 MCP server 使用 CheatSheet**：MCP 是 agent-tool 连接点，官方出安全指南["https://genai.owasp.org/initiatives/agentic-security-initiative/"]
- 微软已发布 **Agent Governance Toolkit（AGT）参考架构**，把 ASI01–10 逐一映射到缓解模式["http://microsoft.github.io/agent-governance-toolkit/compliance/owasp-agentic-top10-architecture/"]

## 2. 为什么与我的知识/项目有关
- **EP-002「Permission Is Security Boundary」** 的直接理论化落地：ASI02 Tool Misuse、ASI03 Privilege Abuse 就是我 EP 原则要解决的事
- 直接服务 **dsh-pentest**（空壳项目，G1 缺口）与 **silver-shield**（防诈骗=Agent 安全应用）
- **Skills Top10** 与我的 OpenClaw Skills / 工具档案知识体系直接同域
- **Secure MCP 指南** 与首轮 MCP 扫描形成闭环：协议安全基线

## 3. 证据与活跃度
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（OWASP 官方 + 一手来源核验） |
| 来源 | https://genai.owasp.org/initiatives/agentic-security-initiative/ ｜ https://github.com/OWASP/www-project-agentic-skills-top-10 ｜ Microsoft AGT 架构 |
| 活跃度 | 高（2026-08 仍在更新 Skills Top10；OWASP 旗舰项目评审中） |

## 4. 验证计划
- [ ] 精读 ASI01–10 与 AST01–10，映射到我的 EP 原则（新增/修订）
- [ ] 用 OWASP 清单给 silver-shield / agent-attention 做一次安全自评
- [ ] 按 Secure MCP 指南校验 agent-attention 改造为 MCP server 的安全设计

## 5. 决策
- [ ] 晋升 validated
- [x] 维持观察（待完成 EP 映射 + 项目自评）
- [ ] 拒绝
