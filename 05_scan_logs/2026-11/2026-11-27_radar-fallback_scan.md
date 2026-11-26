# 2026-11-27 通用兜底扫描

- 当前深耕领域：Computer Use / Browser（第 1 周 Day5 已完成，`e351ae1`）——本任务不重复收集该领域。
- 扫描方式：3 次 `general_search`（MCP/Agent 框架安全、A2A/Agent 框架重大变更、AI Infra 推理框架）+ 1 次一手 `web_fetch`（NVD）。只看重大，未扩展。

## 判定

| 对象 | 是否新 | 是否领域外 | 档位 | 处置 |
|---|---|---|---|---|
| **jupyter-mcp-server CVE-2026-77359**（NVD 11-20，`<1.0.3`，CWE-350） | 是（仓内零命中） | 是（MCP 层） | **A** | 并入 `[cand]agentic-attack-2026.md` 事件日 27 |
| CVE-2026-114090 trigger.dev `--mcp` 绑全网卡、`/sse`+`/messages` 无认证（7.6，10-21） | 是 | 是 | B | 记日志，不写（事件日 22/24 同族第 4 例） |
| CSA《MCP's Transport Trust Gap》（11-09） | 是 | 是 | B（框架综述） | 记日志，作为事件日 27 的分析背景引用 |
| SGLang v1.0（11-12/13 Summit 宣布）+ vLLM 0.34.0（11-16，移除 Model Runner V1、block-size 默认 64） | 是 | 是（AI Infra，**下一域**） | A- | **不写**：下一域 11-30 建基线时统一收，避免重复与提前占位 |
| A2A Java SDK 1.5.0.Final（11-03 breaking）、MAF A2A SDK v1 迁移（11-18）、Google ADK 2.14（11-07，A2A/评测/执行环境转正 + `RunSkillScriptTool` 去掉裸 shell 字符串） | 否 | 是 | — | 已在 09-01 A2A 卡与 11 月 index 明确标记「已知协议迁移」 |

## 一手证据

1. NVD CVE-2026-77359：`jupyter-mcp-server < 1.0.3`；原文「standalone streamable-http mode validates Host and Origin values for **/mcp** but does not apply the same browser-origin controls to the state-changing **/api/connect** and **/api/stop**」；「the vulnerability is the missing management-route origin boundary, not a lack of Host validation on /mcp」；修复 `1.0.3`（commit `c2e98fca`，PR #262）；CWE-350；NVD 未评 CVSS。
2. GHSA-9x8x-crjq-g64h 侧（经 Beam 转述）：CVSS 4.0 **9.3**，11-20 入库 —— **第三方分数，未取 GHSA 原文，标待核**。
3. 机制：DNS rebinding → `/api/connect` 接受浏览器形态请求 → 替换 `runtime_url`/`document_url` → 对攻击者基础设施建 kernel client；`/api/stop` 可掐 kernel。

## 写入

- `03_expansion_queue/candidates/[cand]agentic-attack-2026.md`：新增「事件日 27」块（含「不写」说明）。
- `06_expansion_index/README.md`：置顶 11-27 兜底段（1 行 + 不写说明），位于同日深耕段之前。
- `_INDEX.md`：新增 11-27 兜底行（🟡），位于 11-27 深耕行之前。

## 未做 / 限制

- 未复现 DNS rebinding；未取 GHSA 原文核对 9.3 与受影响版本区间（NVD 与 Beam 一致指向 `<1.0.3`）。
- 未扫 CISA KEV（昨日已发现其 JSON 为 2026.05.22 陈旧快照，无判定价值）。
