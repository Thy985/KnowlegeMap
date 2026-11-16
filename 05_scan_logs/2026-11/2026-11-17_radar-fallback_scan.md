# Personal Tech Radar 兜底扫描 · 2026-11-17（周二 06:00）

> 定位：安全网。当前深耕领域 = **Memory 第二周**（F/E 层）；本任务只抓领域之外的 S/A 级重大突发事件，领域内与普通增量不写。

## 一、检索（3 路，轻量）
1. MCP 协议安全事件 / 漏洞（recency 窗口）
2. Agent 框架重大版本 / 破坏性变更
3. MCP 网关与注册表类基础设施

## 二、判定表

| # | 对象 | 事实 | 判定 |
|---|---|---|---|
| 1 | **CVE-2026-116684**（MCP Python SDK） | `AuthSettings` + `token_verifier` 不校验 `aud`，多资源授权服务器下接受"别人的 token"，可认证到错误 MCP server 并行使其权限；受影响 `>=1.10.0,<1.30.0` / `>=2.0.0,<2.2.0`，修复 1.30.0 / 2.2.0；CWE-863；CNA CVSS 3.1 **6.8**，NVD 未评估 | **A｜并入 S 卡（事件日 20）** |
| 2 | **CVE-2026-125926**（AWS mcp-gateway-registry） | 注册/更新 API 的 upstream 地址校验存在 SSRF：有注册权限的已认证用户可指向内网，网关可能回传内网响应；受影响 `>=1.0.3,<=1.34.0`，修复 1.35.0；升级**不回洗历史配置**，需人工复核 upstream、审计日志、必要时轮换云角色凭据 | **A｜并入 S 卡（事件日 20）** |
| 3 | 11-08 `modelcontextprotocol/servers` 两份通告（ShieldPi） | 仅个人博客转述，称"部分技术成立、当时无补丁"；未取得 advisory 原文 | 未采信（观察项，不写） |
| 4 | MAF `Migrate to MCP 2.x`（11-11） | MCP SDK 2.x 生命周期、`unsafe_extra_run_args`、AG-UI 授权模式、A2A allowlist | 已知对象执行确认（B，11-16 已记） |
| 5 | LangChain changelog（11-11） | `create_deep_agent` 不再默认挂 TodoListMiddleware；其余为常规迭代 | B（普通增量，不写） |
| 6 | Microsoft Agent 365 SDK 2.0 / Foundry hosted agents 迁移 | 11-06 / 11-10，破坏性变更集中于已弃用包或协议库替换 | 已于 11-16 兜底记为 B，去重命中 |
| 7 | CVE-2026-111770 | 事件日 19，11-16 已写 | 去重命中 |

## 三、为什么不新建卡
两条均为 MCP 生态安全事件，按既有纪律「安全域事件合并、不建碎片卡」并入 `[cand]agentic-attack-2026.md` 作**事件日 20**，卡状态仍 S。

## 四、核心判断
1. **认证只证明"你是谁"，不证明"这张 token 是给谁的"**：缺少 audience 校验时，多资源授权服务器会把合法 token 变成跨服务通行证。与事件日 19 的 request-id 碰撞、MemLeak 的 filter≠gate 同构——**身份/上下文没有绑定到资源边界**。
2. **MCP 网关是新的信任汇聚点**：注册表 + 代理 + 凭据三合一，SSRF 可直接升级为云角色凭据滥用；"有注册权限"成了新的高危权限位。
3. **修复不是升级即完**：116684 需要改 `TokenVerifier`（校验 aud）或确认单资源；125926 的 1.35.0 只校验新写入，历史脏配置必须人工回查。
4. 对 silver-shield 的可落地检查项：多资源授权服务器是否校验 aud、MCP server 是否单实例复用、网关 upstream 白名单、组件出网目的域收敛、云角色最小权限。

## 五、限制
- 116684 仅 NVD 描述 + CNA 评分，GHSA 全文与两个 release note 未取；125926 为 AWS 官方公告但未核对 GHSA 与 1.35.0 diff。
- 均未复现；受影响部署量与在野利用未知。11-08 两例未采信。

## 结论
**Changed**（既有 S 卡新增事件日 20；无新卡）
