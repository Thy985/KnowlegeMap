# Personal Tech Radar 兜底扫描日志 · 2026-11-11（06:00）

> 定位：一周一域之外的安全网。当前深耕领域 Memory，本任务只收领域外 S/A 级重大突发事件。

## 检索
两路 `general_search`（minimum）+ 2 次 `web_fetch`（全文：al-ice.ai NEAR AI 复盘、whatsthebigdata 澳洲监管稿）+ `grep -a -ril` 去重（NEAR AI / Fireworks / GitBook / OpenHuman / Australia / Medicare / SGLang）。

## 判定
| 对象 | 等级 | 判定 |
|---|---|---|
| **NEAR AI SGLang RCE → 云泄露**（11-08 利用 / 11-09 报告） | **A** | 并入事件日 16（安全域合并卡，不新建） |
| **Fireworks AI 第二起入侵**（11-09 公告，LLMJacking，权重/数据集/密钥） | **A−** | 并入事件日 16 FACT-2 |
| **澳大利亚 11-10 接受 18 项建议**（强制 AI 事件报告 + 监管机构 + 刑法修订，2027 立法） | **A** | 并入事件日 16 FACT-3（接 09-24 披露 / 10-02 NPWS / 10-06 听证线） |
| MCP 规范 / A2A v1.0 / ADK 2.14 | — | 无新变更 / 已知协议迁移 |
| OpenHuman 7 CVE（11-05，含 9.8 未认证 cron RCE） | B | 批量修复，记日志不写 |
| GitBook agent-infra 泄露（同周） | — | 细节未取得，暂不单列 |

## 要点
- NEAR 报告自述最硬的一句：**confidential computing 保护数据不被运营方/宿主机看到，但不防环境内运行的软件漏洞**；另一条：**deprecated ≠ decommissioned**（下线 Private Chat 的后端仍可拖库）。
- 18 个旧部署 agent 的 chat history / settings / logs 被读取 → Memory 周 E/F 层（作用域、保留、删除权）的现实对照物：agent 记忆散落在旧部署、下线产品后端与日志里，不受记忆系统删除策略管辖。
- 澳洲线从个案问责走到**制度化**：强制报告「错位行为」、独立监管机构、可能刑责；披露时点与充分性成为法定义务，反向要求事件台账与取证留存。

## 证据限制
NEAR AI 报告经 al-ice.ai 一手通读转述，原文未直接取得；SGLang 漏洞未分配 CVE。Fireworks 为公告二手摘要。澳洲立法尚未提交（计划 2027），18 项建议全文未取得。

## 落位
- `[cand]agentic-attack-2026.md` 事件日 16 段。
- 06 index 兜底段、`_INDEX.md` 🔁 行、本日志。
- 未新建卡、未改 connections。

## 结论
**Changed**
