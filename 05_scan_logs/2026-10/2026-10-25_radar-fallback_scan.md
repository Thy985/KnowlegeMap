# 兜底扫描日志 · 2026-10-25（Personal Tech Radar · 全领域轻量安全网）

> 当前聚焦领域：Runtime（10-26 周一 Day1 建能力树，进行中周序：Harness 已闭环 → Runtime 开始前夜）。

## 结论：No Action（无领域外 S/A 级重大新对象）

扫描范围：安全 / MCP / A2A / 框架 / Memory / Computer Use / AI Infra / durable execution。所有重大事件均命中去重基准：
- OpenAI 监控对抗事件（Sol/Astra）→ 已移交 10-24 兜底、10-25 深耕小结并入 E7 证据线 ✅
- ARTEX 韩国银行 / php2shell → 已建卡/已移交 ✅
- MCP spec 2026-07-28 无状态核心 → 09-01 已覆盖 ✅
- LangChain / OpenAI Agents SDK / LangSmith Engine v2 → 普通增量，不写

## B 级信号（记日志，不建卡）

### 1. OpenCode 泄露事件（安全，B+）
- **事件**：开源 AI 编程工具 OpenCode（headless HTTP coding agent，已在去重基准）10-17 披露泄露——**蒸馏攻击始于 9 月末，波及 OpenCode Console 约 1.4% 用户**，用户存储的外部 AI 提供商 API keys（OpenAI/Anthropic/Google 等）暴露
- **影响**：多名开发者报告未经授权 API 扣费（数百~$1,700+/晚）、Google Cloud 项目被暂停；联合创始人 Dax Raas 称 10-16 起遭遇"不间断的 AI 驱动攻击"
- **信号**：AI 编程工具供应链凭证存储成攻击面——"凭证外挂/集中存储"另一侧教训（对照 Strands Box 网关外注 vs OpenCode 集中存 key）；与 10-19 Reuters 单人黑客 100+ 公司事件同属 agentic-attack 主线
- **来源**：BleepingComputer 10-19 / eSecurityPlanet 10-19 / 财联社 10-24
- **处置**：B+ 级记日志；凭证管理教训并入 Runtime 周（凭证外注模式对照素材）

### 2. ACP 并入 A2A（协议生态收敛，B）
- 10-15 ClawdBytes：**ACP（Agent Client Protocol）deprecated，merge 进 A2A**；A2A 获 150+ 组织支持、嵌入 Azure AI Foundry 与 Amazon Bedrock；"A2A-compliant" 只认证连接语言、不认证安全/身份
- **信号**：agent 互操作标准收敛到 A2A（A2A 已在去重基准 [cand] S）；ACP 阵营（Sourcegraph/Cody 生态）面临 re-architecture；与 MCP（工具）/A2A（agent 间）/PAP（agent-to-business）三协议格局对照
- **处置**：B 级记日志，并入既有 A2A 卡增量认知，不单独建卡

### 3. durable execution 领域信号（Runtime 周预置，领域内移交不建卡）
- **Vercel durable-harness 开源**（10-21）：包装 Pi/OpenCode/Claude Code/Codex 的 crash-proof harness——session 存 durable log，dead function 不丢工作；**10-20 Vercel durable agent state stack 参考应用开源**（AI Gateway 上运行，agent logic / execution environment / persistence 三层分离）
- **Notion Gen-6 Agent Harness**（10-22）：durable execution 商用落地——queue-backed worker loop，agent 可跨系统重启存活、无人值守跑 24h
- **信号**：durable execution 从 Dapr Agents（10-16 CNCF×NVIDIA）扩展为 2026-10 下旬主流趋势（Vercel/Notion 跟进）；**正是 Runtime 周（10-26 起）核心主题**，与 Dapr Agents 头号锚点直接对照
- **处置**：领域内信号 → 移交深耕，Runtime 周 Day1 建能力树与周五验证可并入对照池（Dapr Agents vs Vercel durable-harness vs Notion）

## 文件变更
- 本日志新建（No Action，无候选卡、无去重基准变更）
- `_INDEX.md`：追加本日志行

## 结论
**No Action**（无领域外 S/A 级重大新对象；B 级 3 项记日志：OpenCode 泄露 / ACP 并入 A2A / durable execution 领域信号移交 Runtime 周）
