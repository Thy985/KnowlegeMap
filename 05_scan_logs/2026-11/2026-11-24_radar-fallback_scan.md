# 2026-11-24 Personal Tech Radar 兜底扫描

- 定位：一周一域（Computer Use / Browser 第一周 Day2）之外的安全网，只抓重大突发事件；4 组检索（MCP / A2A / Agent 框架安全 / 本地推理），未做扩展搜索。
- 去重基准：`06_expansion_index/README.md`（`grep -a`，关键词 agent-framework / GHSA-764m / PYSEC-2026-4388 / Cairn / PyPI 投毒 / supply chain）。

## 结论

| 对象 | 判定 | 处置 |
|---|---|---|
| **Microsoft agent-framework PyPI 投毒（1.26.1 / 1.26.2）** | **New（A，领域外）** | 新建 `[cand]maf-pypi-supply-chain-2026-11.md` |
| A2A v1.0 / ADK 2.14 A2A 转正 / IBM ContextForge ADR-048 | B（已在库：A2A 仍 v1.0，2026-03 GA；v1.0.1 仅规范修正） | 不写 |
| AG2 SandboxShellTool 命令注入 CVE-2026-113663（换行/回车绕过前缀过滤，`sh -c` 追加语句，默认 LocalEnvironment 宿主执行；1.1.1 修复；NVD 11-06） | B+（单框架沙箱过滤缺陷，已发布补丁十日以上） | 记日志，不建卡（与 Runtime 周"沙箱边界"同族，留作证据） |
| 三个 MCP server 越界 CVE（11-18）：Gortex 7.8 / yt-mcp 7.5 / DOMShell 4.8（DOMShell = Chrome 自动化 server，属当前深耕域） | 领域内 + B/C | 不写（交由深耕周四安全增量） |
| llama.cpp / ggml 1.0.0（11-13）、Inkling 2 Mini（11-20，vLLM day-0）、Kimi K3.1 Pro（11-04） | 已在"下一域候选"记录（AI Infra / 本地边缘） | 不写 |
| fast-agent CVE-2026-102610、Langflow 双 9.8 | 已覆盖（11-23 兜底） | 不写 |

## MAF 事件一手事实（进卡）
- 时间线：1.26.0（11-12）→ 1.26.1（11-17 20:35 UTC）→ 1.26.2（21:08 UTC，33 分钟后）→ 约 21:30 两版被 PyPI 移除；窗口约 41–45 分钟。
- 形态：wheel-only（正常发布含 sdist）；`.pth` 在解释器启动时执行（`pip` 启动也触发）；1.26.1 文件名 `agent_framework_meta.pth` / `_telemetry.py`，1.26.2 改为 `af_runtime_diag.pth` / `af_runtime_diag.py`。
- 载荷：env（OPENAI / HF_ / FOUNDRY 等）、`/proc` 他进程 environ、`.npmrc`、`.git-credentials`、Azure CLI 会话、HF token；申请 Azure MI / Azure DevOps OIDC（1.26.2 加 GitHub Actions OIDC）新令牌；单一 `webhook.site` 外发。
- 定性：GHSA-764m-3ppc-5m73 malware，CWE-506/829/522，critical，**无 CVE**；PYSEC-2026-4388 称"未经授权上传"并已移除；1.26.0 为最后干净版。
- 根因（Wiz 单源）：疑似微软内部发布流水线**客户端证书被窃**，绕过源码仓库直接发布 → 标"待核"。
- 影响面：约 41k 下载/周、190k/月；Wiz 可见请求中 3 次成功外发。11-20 `microsoft/agent-framework` 等三仓库 GitHub API 仍 404（与本次攻击关联未确认）。

## 未做
- 未取 wheel 做静态 diff、未做隔离行为复现（兜底任务不排期；写入卡 §4 验证计划）。
