# 兜底扫描日志 · 2026-10-15（Personal Tech Radar 通用兜底扫描 06:00 安全网）

> 定位：不漏掉当前深耕领域（Evaluation/Observability）之外的重大突发事件。轻量，刻意只看重大。

## 扫描范围
general_search 两路：① MCP/agent 安全突发与重大事件；② runtime/harness/协议重大版本与新方向。

## 结果

### 新候选卡（+1，候选卡 46→47）
- **ToFu**（A 级，领域外·安全）——`03_expansion_queue/candidates/[cand]tofu-mcp-tool-fuzzing-2026.md`
  - arXiv 2610.13651（10-09，Penn State / Montpellier / Dartmouth）：工具感知 fuzzing 框架，从 tool metadata + CWE 指导 sanitizer（74 个）自动推导语义安全检查；实测 273 MCP servers / 3,405 tools / **253 已验证漏洞（343 工具 / 118 server）**
  - "Repeat-After-Me" 攻击跨 6 编排框架复现（LangGraph/MS MAF/Google ADK 2.0/AutoGen/AWS Strands/CrewAI）；核心结论：schema-valid 参数必须视为不可信，执行层强制
  - 与 10-13 卡 Protocol Pivoting 互补（攻击范式 vs 审计框架），构成"隔离+信任+审计"三角；连接 dsh-pentest/silver-shield/引擎 security-assessment
  - 证据 FACT（arXiv 一手 + GBHackers 10-13）

### 记日志不建卡
- **Anthropic MCP SDK 登录劫持漏洞**（SecurityBrief 10-12，Cycode 经 Anthropic 安全流程报告，补丁已发布）：官方 MCP SDK 单点漏洞（已修），B 级，并入 MCP 安全趋势观察，不单独建卡
- **253 漏洞/343 工具的中文媒体扩散**（至顶网 10-12 等）：即 ToFu 研究的媒体报道，已建卡
- **Protocol Pivoting 媒体扩散**（neoteo/techbeat/cyber-ivy）：10-13 已建卡事件，不重复
- **IETF agentproto 工作组新草案**（10-10~13）：draft-bu-agentproto-security-principal-binding-08（安全主体/验证者绑定，迭代到 08 版）、draft-stephan-agentproto-6g-usecases-00（6G 用例）——标准化持续推进，B 级观察
- **同谱系 fuzzing**：ChainFuzzer（arXiv 2603.12614，工作流级多工具漏洞，3 月）、OrchJail（2605.07414，5 月）——作为 ToFu 背景记入卡片
- **Zhivex Harness / A3S-Lab Code changelog**：小项目普通 release，不追
- **Microsoft Foundry hosted agent 迁移**（8-6 文档）：旧内容，不追

## 结论
**New**（领域外 1 张 A 级卡，候选卡 46→47）。ToFu 满足"领域外 + S/A 级 + 重大（大规模实证+开源框架+跨框架复现）"三条件；其余均低于阈值或已去重。
