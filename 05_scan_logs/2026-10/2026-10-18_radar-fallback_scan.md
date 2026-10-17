# 兜底扫描日志 · 2026-10-18（Personal Tech Radar · 06:00 安全网）

> 定位：一周一域深耕（Evaluation 周已于 10-18 凌晨收官；Harness/治理 10-19 周一起）之外的轻量安全网。
> 扫视范围：MCP / A2A / Harness / Runtime / Memory / Computer Use / Evals / AI Infra / 安全 / 本地边缘。

## 扫视结果（2 路）
| 方向 | 命中 | 判定 |
|---|---|---|
| 安全事件 | **CVE-2026-96620 Claude Agent SDK argv 注入**（NVD 10-16 发布，al-ice 10-17 分析）、CVE-2026-108586（@1mcp/agent OAuth tag-scope 绕过，10-14）、10-11 七 agent 平台 gateway 凭据批量披露（BotSharp/UNLA/Plano 等，hieuPenguinnn）、MCP Rug Pulls/Agent Card Poisoning 综述（dev.to 10-17，引用 CVE-2025-6514/6515 旧 CVE） | 见下，全部不建卡 |
| 框架/协议 | **Microsoft Agent Framework 1.0**（Semantic Kernel + AutoGen 统一后继，10-13 GA，hivebook 10-17 更新）、a2a-sdk v1.0 迁移（10-15，已去重）、Google ADK 2.11 / OpenAI Agents SDK 0.23（10-01，旧闻）、DeepSeek V4.1-Flash-1017（10-17，模型小版本） | 见下，全部不建卡 |

## 新见但记日志不建卡（移交 Harness/治理周，10-19 起深耕）
1. **CVE-2026-96620（claude-agent-sdk Python < 0.2.121，CVSS 4.0 9.2 Critical）**
   - 机制：`resume`/`session_id` 以两 token 形式传给 Claude CLI，dash 开头值被解析为独立 flag → 注入 `--mcp-config` 定义 stdio MCP server → CLI 启动时任意命令执行（绕过 SDK 权限控制）。
   - **关键事实：补丁 0.2.121 早在 2026-07-17 发布（当前 0.2.168），TS SDK v0.3.208 更早修复；NVD 滞后 91 天发布**。前提受限：应用须把不受信任输入路由到 resume/session_id（AT:P）。
   - 不建卡理由：① 已修复 3 个月的滞后披露，非突发未修复事件；② 属已知 argv injection（CWE-88）实例，非新范式；③ 属 Harness/治理领域（明天起深耕），与已建卡 ToFu（schema-valid 参数不可信）、Protocol Pivoting 同源，深耕周合并处理。
   - 参考：https://al-ice.ai/posts/2026/10/claude-agent-sdk-cve-2026-96620-resume-argv-flag-injection-mcp-config/
2. **CVE-2026-108586（@1mcp/agent 0.20.0–0.39.0，OAuth tag-scope 否定表达式绕过）**：第三方 MCP 网关单产品授权缺陷，B 级。
3. **10-11 七平台 gateway 凭据披露批量**（VulnCheck 批量分配，单一研究者 hieuPenguinnn）：B 级非主流平台，无范式新意。
4. **Microsoft Agent Framework 1.0 GA（10-13）**：SK + AutoGen 合并后继正式版；去重基准已含 Omnigent/MS Agent Framework（已知对象重要变化），属 Harness 领域，深耕周追增量。
5. **DeepSeek V4.1-Flash-1017（10-17）**：模型小版本更新，非框架/协议级；dsh 项目用到 V4.1 Flash，留意即可，B 级。

## 结论
**No Action**（无新卡）：无 S/A 级且领域外的重大突发事件。最显眼的 CVE-2026-96620 属已修复 3 个月的滞后披露且落入明天开始的 Harness/治理领域，连同 MS Agent Framework 1.0 一并作为 Harness 周线索移交深耕任务。
