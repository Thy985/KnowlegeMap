# 兜底扫描日志 · 2026-10-17（Personal Tech Radar · 06:00 安全网）

> 定位：一周一域深耕（当前 Evaluation/Observability）之外的轻量安全网，只抓领域外重大突发事件。
> 扫视范围：MCP / A2A / Harness / Runtime / Memory / Computer Use / Evals / AI Infra / 安全 / 本地边缘。

## 扫视结果（3 路）
| 方向 | 命中 | 判定 |
|---|---|---|
| 安全事件 | Protocol Pivoting（techbeat/unite.ai/techtimes 媒体扩散，10-05~06）、Anthropic MCP SDK 登录劫持（SecurityBrief 10-12）、GHOSTJACKING（forkast 10-06）、ToFu 253 漏洞（gbhackers 10-13） | **全部已去重**：Protocol Pivoting（10-13 兜底建卡）、ToFu（10-15 兜底建卡）、GHOSTJACKING（10-16 兜底记日志）、MCP SDK 登录劫持（10-15 兜底记日志 B 级） |
| 框架/协议重大版本 | LangChain changelog（10-14 更新）、Managed Deep Agents v0.9（10-07，schedules/per-run config/Slack）、MS Agent Framework 迁移 a2a-sdk v1.0 | 普通增量（B 级以下）；a2a-sdk 迁移 10-16 兜底已去重 |
| Runtime/Memory/Computer Use/Infra | **Anchor Action Index**（10-15 发布）、Claude Memory（产品增量 10-10）、联想 YOGA Pro 15 RTX Spark AIPC（10-16）、Google TPU 8（4 月旧闻）、Claude Managed Agents Memory（4 月旧闻） | 见下 |

## 新见但记日志不建卡
- **Anchor Action Index**（2026-10-15 发布，tsnmedia.org / webdesignernews 转载）：Anchor（browser infra 公司）发布 computer-use agent 的"共享工作流记忆"——agent 把已成功完成的 web workflow 存为确定性代码回放，页面变化时模型才介入；宣称 token 成本降 100x。
  - **判定 B 级，不建卡**：商业产品发布（非开源、非标准、非框架路线变更），单一来源均为新闻稿转载，无第三方验证；概念（workflow replay = deterministic code + model fallback）与已有 Browser Harness/Webwright 候选卡谱系相邻。
  - 留待 **Computer Use/Browser 周**（领域顺序第 5 周）与 Browser Harness 候选卡合并验证。

## 结论
**No Action**（无新卡）：领域外无 S/A 级重大突发事件；安全线全部为已覆盖对象的媒体扩散，框架线为普通增量，Anchor Action Index 按 B 级记日志留待 Computer Use 周。
