# 2026-11-23 Personal Tech Radar 通用兜底扫描

- 当前深耕领域：Computer Use / Browser（11-23~11-29 第一周，Day1 已完成）——本任务不重复其细节。
- 扫描范围：MCP / A2A / Harness / Runtime / Memory / Evals / AI Infra / 安全 / 本地边缘；只取重大、突发、高影响。
- 广度：4 组检索（MCP 变更、Agent 框架路线变更、Agent 安全 CVE、本地推理发布）+ 2 次一手核验（NVD、PyPI）。

## 发现与去重
| 对象 | 判定 | 处置 |
|---|---|---|
| **Langflow CVE-2026-93680 / 110186**（1.0.0–1.12.8，CVSS 9.8，认证绕过 + 代码生成 RCE，1.13.0 修复） | **A 级、领域外、此前 0 命中** | 新建 A 卡 `[cand]langflow-unauth-rce-2026.md` |
| OpenClaw CNNVD 82 漏洞聚合页（11-23） | 已有对象增量、非新事件 | 不建卡（campus_order 安全清单施工项） |
| fast-agent CVE-2026-102610 / Agenta CVE-2026-123786 | 06 index 已覆盖 | 不重复 |
| Edge0-145B / local-edge | 已在 `[cand]local-edge-llm-2026` 与 index | 不重复 |
| MCP 11-11 六个月发布节奏（SEP-3398）+ Ruby SDK Tier 1 | B 级治理增量 | 不写（非实践变更） |
| MS Agent Framework 11-13 破坏性变更（A2A options / Hyperlight 30s） | B 级框架增量 | 不写 |
| ggml v1.0.0 / Inkling 2 Mini（11-20，26.4B looped MoE 本地可跑） | 下一域（AI Infra/本地边缘）候选，非本日突发 | 不写，留待 11-30 起首周建树 |
| pandas-ai CVE-2026-51898（默认 sandbox=None） | 与 Langflow 同构，作为品类证据引用 | 不单独立卡 |

## 一手核验记录（防二手误引）
- NVD：CVE-2026-93680 发布 2026-10-29，CWE-287，CVSS 3.1 9.8，`PR:N/AC:L`，配置 `<1.13.0`；SSVC `exploitation=none`（10-30）。
- NVD：CVE-2026-110186 同日，CWE-94，CVSS 9.8，同区间。
- Rapid7（10-23）：6 个 Metasploit 模块覆盖 Langflow；其中 93680 模块为 `auxiliary/gather`，**只做 MCP 端点无凭据工具枚举，不执行代码**（Rescana 11-02 复核）——故"一键 RCE"不成立。
- PyPI：1.13.0 于 10-23 发布；1.13.3 于 11-18 为当前最新。
- 未核：乌干达 CERT 称 KEV 中 6 条 Langflow CVE（我只核到 3 条）；Aviatrix 称第三个漏洞可经 Agentic Assistant 执行 OS 命令；两条新 CVE 的在野利用未见一手。

## 结论
**New（A）**：Langflow 双 9.8 未授权漏洞补漏入账，立"AI 编排平台功能即执行面"判据。
其余 No Action（已覆盖 / B 级 / 下一域留待）。
