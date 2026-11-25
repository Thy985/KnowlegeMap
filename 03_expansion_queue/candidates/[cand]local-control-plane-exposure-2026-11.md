# 候选对象证据卡

> 状态：`[cand]` ｜ 关联方向：Computer Use / Browser · E 隔离与凭据（缺口①，S） ｜ 日期：2026-11-26

## 一句话定位
把「agent 的本地控制面」按**谁能触发**拆成 7 种已发生的失效模式，并给出 6 问可执行核查清单——它不是新工具，是 silver-shield / TeamMind / campus_order 可直接用的暴露面基线。

## 1. 它解决什么问题

「绑 127.0.0.1 就安全」是这一层最贵的错觉。浏览器/桌面 agent 的控制面不止一个入口：同机任意进程（无认证 CDP）、**浏览器里的任意网页**（DNS rebinding / 通配 Origin / 扩展中继）、局域网或公网（默认绑 `0.0.0.0`）。三者需要三套不同校验，只做 loopback 绑定只挡住第三类。

同时，「凭据泄露」也不是单一动作：profile 目录可读、cookie store 可枚举、系统密码库可解密、剪贴板/下载目录可捞——每一种的**触发条件与检测点**都不同，混成一句「agent 会偷密码」就无法施工。

## 2. 为什么现在值得关注（7 种失效模式，全部有已发生证据）

| # | 失效模式 | 对象与事实 | 谁能触发 | 证据 |
|---|---|---|---|---|
| P1 | **无认证 CDP 调试端口** | browser-use 1.0.8 官方自述：`Browser('chrome')` / `profile=` 会开 `127.0.0.1` 无认证调试端口，同机其他本地用户可 attach 到该浏览器及其登录态 | 同机任意进程/用户 | FACT（PyPI 文档） |
| P2 | **本地 HTTP bridge 无 Host/Origin/认证 + DNS rebinding** | `chrome-devtools-axi` ≤0.1.26：`http://127.0.0.1:9224` 只按 method/path 分发，`POST /call` 直接执行任意 CDP → 完全接管 Chrome 会话；0.1.27 修复（GHSA-x439-jhfh-v9x2，2026-07-22，High）。同类：**Playwright MCP <0.0.40** 不校验 Origin，网页 rebind 到 127.0.0.1 即可调用**全部** server 工具；0.0.40 修复（CVE-2025-9611 / GHSA-6fg3-hvw7-2fwq，2026-01-07，GitHub 评级 High） | 浏览器内任意网页 | FACT（NVD/OSV/官方 advisory） |
| P3 | **默认绑 0.0.0.0 + Origin 可选校验** | PraisonAI `browser start` 默认把 browser bridge 暴露在 `0.0.0.0`；`/ws` 接受**完全不带 Origin** 的客户端，未认证者可伪装 controller、劫持已连接的扩展会话（CVE-2026-40289 / PYSEC-2026-485，CWE-306） | 同网段/公网任意客户端 | FACT（PyPA advisory DB） |
| P4 | **扩展中继端点无令牌** | OpenClaw Browser Relay（需装并启用扩展）`ws://127.0.0.1:18792/cdp` 不要求认证 token，**网站可经 loopback 连上**，窃取会话 cookie 并在其他 tab 执行 JS；影响 `2026.1.20 ≤ v < 2026.2.1`，CWE-306，CVSS 4.0 **7.4**（CNA: VulnCheck；NVD 未评） | 浏览器内任意网页 | FACT（NVD CVE-2026-28458） |
| P5 | **扩展权限组合本身即后门** | Manus Browser Operator（扩展 2025-11-18 发布、11-22 起全量；非本轮新增，补为历史锚点）：`debugger` + `cookies` + `<all_urls>`，持久 WebSocket 连 `wss://api.manus.im`，服务端实时下发导航/点击/输入，跨域枚举 cookie 并经预签名 URL 外传；Chrome 只给「某扩展正在调试此浏览器」的小提示；授权是**整段会话 open-ended**，不能按域名/动作收窄 | 远端厂商后端（经本地扩展代理） | FACT（Mindgard 实测）+ 厂商文档（「clears standard access barriers」） |
| P6 | **profile 指针与浏览器护栏被拆** | Chrome 136+ 起，默认 user-data-dir 不允许开 `--remote-debugging-port`（防「让 Chrome 以调试模式启动→读全部 cookie」）；Chrome 147+ 品牌版改为**静默阻塞 + 每次重启弹 Allow**，`DevToolsActivePort` 可能不写。而 browser-harness PR #142（2026-04）用 `CHROME_CONFIG_HOME` 指向伪「非默认」路径绕过该检查，让默认 profile 继续可调试 | 本地自动化工具（自拆护栏） | FACT（Chrome 策略，二手转述待核具体版本）+ PR 描述（一手） |
| P7 | **凭据解密器藏在 skill 运行时** | SkillLeak（2026-09）：`@szc-ft/mcp-szcd-client` 的 `local-browser-test` skill 在 `connect()` 调 `_decryptCredentials()`，用 Windows DPAPI + AES-256-GCM 解出**整个 Chrome/Edge profile 的全部已存密码**，明文写 `~/.szcd-mcp/deps/decrypted-creds.json` 并作为 MCP tool result 返回，流向默认远端 `mcp.szcd-mcp.top` | 装了该包、且按正常用法指向自己浏览器的人 | FACT（Xygeni 分析） |

**关键分布**：7 种里 4 种（P2/P4/P5/P7）的触发者是「正常使用就会发生」的角色——浏览一个网页、装一个扩展、跑一次 skill；只有 P1/P3 是「别人要主动来打」。这解释了为什么这类问题在 review 里总被低估：**默认路径即暴露**。

## 3. 6 问核查清单（每个控制面都要答）

1. **绑在哪**：`127.0.0.1` / `::1` / `0.0.0.0` / Unix socket？绑定地址是否可配、默认值是什么？
2. **校验什么**：Host 头？Origin 头？还是「只要 method/path 对就执行」？注意 `--allowed-origins` 这类参数官方常注明「**不是安全边界、不影响重定向**」。
3. **认不认证**：有没有 per-session token / 一次性凭据？token 是否可能进 argv（`ps` 可见）？
4. **谁能到达**：同机进程 / 浏览器内网页 / 局域网 / 公网——四者分别做过什么？
5. **凭据面多大**：profile 目录、cookie store、系统密码库、剪贴板、下载目录、`/proc/*/environ`、`.git-credentials`——哪些是「全 profile」级而不是「单站点」级？
6. **失败是否 fail-closed**：校验缺失时是拒绝，还是「宽松放行 + 日志」？

## 4. 与我的连接

- **连接的项目**：
  - **silver-shield**：清单直接变成检测项——端口/绑定地址基线、Host/Origin 校验缺失、扩展中继端点、skill 运行时的凭据解密调用（不是只看 install hook）。
  - **TeamMind**（多 agent 运行时）：P5/P7 说明「扩展/技能」是多 agent 体系里最容易被当成可信组件的一层；信任授予应按「能力组合」而不是「来源」。
  - **campus_order（OpenClaw）**：OpenClaw 自身有 Browser Relay 无认证历史（P4），接入时必须核版本 ≥2026.2.1，并禁止把用户真实 profile 交给 agent。
  - **Tafcm / E2E-CLI**：本机自动化一律一次性 profile + 非默认 user-data-dir；E2E 用例应包含「DNS rebinding 打本机 bridge」这一负例。
- **连接的知识点**：能力树 E2（绑定地址）/ E4（凭据面）/ E5（profile 与目录）/ F1（不可信输入）/ 判断 7、8；MAF 卡的 `.pth` 与 Cairn 的 `sitecustomize.py` 同属「启动即执行」，与 P7 的「运行时才解密」构成凭据获取的两条时间线。
- **潜在收益**：把「本地控制面安全」从一句原则变成**可勾选的 6 问 + 7 个已知形态**，review 时能直接对照，不需要每次重新想。

## 5. 证据与验证计划

| 项 | 内容 |
|---|---|
| 一手来源 | NVD CVE-2026-28458｜OSV GHSA-6fg3-hvw7-2fwq｜GitLab advisory CVE-2025-9611｜PyPA PYSEC-2026-485｜Mindgard（Manus）｜browser-harness PR #142｜Chrome 136+ 策略（二手转述）｜Xygeni（SkillLeak） |
| 证据等级 | FACT（CVE/advisory/厂商文档）+ DESIGN（6 问清单为本仓归纳） |
| 验证方式 | 周五：本机 `ss -ltnp` 取监听面基线；`ls -ld` 核 profile 目录权限；对 Playwright MCP 核 `--allowed-hosts` 默认值与 `*` 语义；对 DNS rebinding 做一次最小 PoC 设计（不实跑攻击） |
| 预期完成时间 | 2026-11-27（周五，与 browser-use / Playwright MCP 验证合并） |

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察（清单本身已可用；待周五本机核查补「我这台机器」的事实）
- [ ] 拒绝（原因）

## 7. 证据限制
- P6 的 Chrome 版本分界（136 起 / 147+ 品牌版）来自二手技术博客与 PR 描述，**未取 Chrome 官方 release note 原文**；「147+ 静默阻塞」待核。
- P5 是 2025-11 事件（Mindgard 正文「Tuesday, November 18」对应 2025-11-18，厂商文档写 2025-11-22 全量），**不是本周新增**；检索元数据给出的 2026-10-30 为再索引日期，勿当发布时间。
- P7 的包名/版本区间来自 Xygeni 单源，未取 npm 侧 advisory 原文。
- P2 的 chrome-devtools-axi 只取到镜像文本（原 GitHub advisory 被 robots 拒），CVSS 分数未取。
