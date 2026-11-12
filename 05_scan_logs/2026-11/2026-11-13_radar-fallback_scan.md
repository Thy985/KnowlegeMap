# Personal Tech Radar 兜底扫描日志 · 2026-11-13（06:00）

> 定位：一周一域之外的安全网，只看 S/A 级重大突发事件。当前深耕域 = Memory（11-09 起），本任务不重复收集该域细节。

## 检索
- 两路 `general_search`（minimum）：① AI agent security breach / MCP · A2A 重大变更；② AI agent 事件与披露（11-10~11-12）。
- `grep -a -ril` 去重（Notion / Fireworks / fast-agent / Agenta / 事件日 18）。
- `web_fetch` 全文：`https://smartcr.org/cloud-security/notion-s-fireworks-breach-disclosure-puts-ai-chat-privacy-in-focus/`（2026-11-12）。

## 判定
| 对象 | 等级 | 判定 |
|---|---|---|
| Notion × Fireworks：客户 AI 对话被泄露 + ZDR 缺口（11-10/11-11） | **A** | 并入 `[cand]agentic-attack-2026.md` 事件日 18（沿用安全域合并卡纪律） |
| fast-agent CVE-2026-102610（CVSS 6.4，`serve` 绑 0.0.0.0 暴露 MCP over HTTP）+ Agenta CVE-2026-123786（未认证 SSRF），11-06 入 NVD | B | 仅记日志，不写卡 |
| MCP 规范 / A2A 协议 | — | 无重大变更：MCP 仍 2026-07-28（stateless core + extensions），A2A 稳定线仍 v1 |
| 亚阈值事件 | — | MCP rug-pull / Agent Card poisoning（11-10 分析文，非新事件）；NEAR AI（事件日 16 已记）；OpenAI 澳洲案（事件日 16 已记） |

## 要点
- **FACT-1**：Notion 11-10/11-11 更新公告，Fireworks 泄露中被访问的数据集含 **Notion AI Insights 的 chat transcripts**；受影响 workspace **<1%**；多数 transcript 无法归属作者/workspace，但内容可能含用户输入的任何敏感信息；11-11 已吊销受影响消息中暴露的 Notion API key。
- **FACT-2（最关键）**：Notion 的 ZDR 承诺**只覆盖实时请求**，不覆盖 Insights 这类**存储后批处理分析**的数据；Fireworks 有合同性 ZDR 承诺，但 Notion 调查发现数据确从其使用的端点被保留 → **合同承诺 ≠ 技术不落盘**。
- **FACT-3**：11-02 通知（初判合成测试数据）→ 11-03 断开/删除/中止训练 → 11-08 收到数据集 → 11-10/11 定性并吊销 key；Fireworks 公告（11-09）称 Inference/Training SDK/Nexus 默认 ZDR 未受影响，但未解释是哪个系统保留了数据。
- **含义**：ZDR 要按端点/路径逐条验证；供应链事件按「数据类别 + 端点」清算；聊天里粘贴的 key 是二级泄露源，需出站 secret 扫描与自动吊销；记忆删除权必须覆盖「功能副本 / 分析数据集 / 供应商侧留存」；事件响应 SLA 应进采购合同。

## 证据限制
- 一手为 SmartCR（11-12）对 Notion 公告的转述（原文指向 ThorstenMeyerAI.com）；**未取得 Notion 公告原文与 Fireworks 11-09 公告全文**。
- 受影响人数、保留时长、具体保留系统均未公开；「<1% workspace」为 Notion 自述。

## 落位
- `[cand]agentic-attack-2026.md` 新增事件日 18 段（4 FACT + 5 含义 + 证据限制）。
- 06 index 新增本日兜底段；`_INDEX.md` 新增 🔁 行；本日志。
- 未新建卡；未改 connections / 能力树（属深耕域周六动作）。

## 结论
**Changed**
