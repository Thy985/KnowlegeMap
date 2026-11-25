# 2026-11-26 Personal Tech Radar 深耕扫描（Computer Use / Browser · Day4 · 安全）

- 领域：Computer Use / Browser（第一周 11-23~11-29）；今日分工＝周四「只追增量」，主题＝安全（本地监听 / 通配 CORS / profile 串用 / 凭据泄露 / 沙箱逃逸）。
- 方法：4 组 general_search + 4 次 web_fetch（NVD / OSV / Mindgard / Manus 文档）；去重检索 10 个关键词于 `06_expansion_index` / `03_expansion_queue` / `08_agent_centric`。
- 去重结论：Playwright MCP、OpenClaw 均为既有锚点/生态对象，按「已有对象增量并入」处理；`DNS rebinding` 在 06 index 只出现过 SDK 侧（CVE-2026-63118），浏览器/桌面控制面侧为空 → 属真实缺口。

## 判定

| 对象 | 档位 | 处置 |
|---|---|---|
| **本地控制面暴露面清单（7 模式 + 6 问）** | **A（新卡，对应缺口① S）** | 新建 `[cand]local-control-plane-exposure-2026-11.md`；缺口① 记「部分闭环」 |
| **Playwright MCP CVE-2025-9611**（<0.0.40 无 Origin 校验，DNS rebinding → 全部工具） | **A（Changed）** | 并入 2.1 Playwright MCP 锚点行 + 清单卡 P2 |
| **OpenClaw CVE-2026-28458**（Browser Relay `/cdp` 无认证 token） | **A（Changed）** | 并入 2.1 新增锚点 + 清单卡 P4 |
| **chrome-devtools-axi GHSA-x439-jhfh-v9x2 / PraisonAI CVE-2026-40289** | A（合并一行） | 2.1 锚点「本地 MCP bridge 两种失败」 |
| **Chrome 136+/147+ 远程调试限制 + browser-harness PR #142 绕过** | B（待核原文） | 2.1 锚点 + 清单卡 P6 |
| **Manus Browser Operator**（`debugger+cookies+<all_urls>`） | A-（历史锚点） | **不建卡**，只入 2.1；卡内标注 2025-11 事件 |
| **SkillLeak**（`@szc-ft/mcp-szcd-client`，DPAPI 解全 profile 密码） | A（增量） | 并入 `[cand]skill-supply-chain-security-2026.md` §3.5 |
| Anthropic 5 条浏览器/系统利用链（10-27，Chrome 156 修 62 CVE / 13 沙箱逃逸） | B | 记日志，不写 |
| AIPex 等 Manus 开源替代 | B | 记日志，不写 |

## 一手事实

### P2 Playwright MCP（OSV GHSA-6fg3-hvw7-2fwq）
- 摘要原文：versions prior to 0.0.40 fail to validate the Origin header → DNS rebinding → unauthorized invocation of all MCP tool endpoints；CWE-749；GitHub reviewed；published 2026-01-07；fixed 0.0.40。
- 现行参数（官方 README）：`--allowed-hosts` 默认＝localhost/loopback + `--host`，传 `*` 关闭检查，官方注明「is not for CORS, but rather for the DNS rebinding protection」；`--allowed-origins` 明写「does not serve as a security boundary and does not affect redirects」。
- IETF draft（mcp-security-considerations-00）另记：browser-automation MCP server 的 SSRF（playwright-mcp issue 1626），影响含内网服务与已认证会话状态。

### P4 OpenClaw（NVD CVE-2026-28458）
- 原文：Browser Relay（需装并启用扩展）`/cdp` WebSocket 端点不要求认证 token，网站可经 loopback 连接，攻击者可连 `ws://127.0.0.1:18792/cdp` 窃取会话 cookie 并在其他 tab 执行 JS。
- 影响 `2026.1.20 ≤ v < 2026.2.1`；CWE-306；CVSS 4.0 7.4（CNA VulnCheck，NVD 未评）；修复 commit `a1e89af`；NVD 发布 2026-03-06。

### P3 PraisonAI（PyPA PYSEC-2026-485 / CVE-2026-40289）
- `browser start` 默认把 bridge 暴露在 `0.0.0.0`；`/ws` 接受不带 Origin 的客户端；未认证者可发 `start_session`，让服务器把 `start_automation` 转给另一个已连接的扩展 → 劫持会话并接收动作/状态流。

### P5 Manus Browser Operator（Mindgard）
- 扩展 2025-11-18 发布，厂商文档：2025-11-22 起对全部用户可用（Chrome/Edge）。
- 权限：`debugger`、`cookies`、`<all_urls>`、`tabs`、`scripting`；crx-analyzer risk 100/100。
- 架构：background 持持久 WebSocket 到 `wss://api.manus.im` → 用 Chrome Debugger API 执行服务端命令；content script 注入所有页面（Readability + Turndown）；token.js 读 `manus.im` cookie。
- 实测：跨域枚举并读取**任意域** cookie → 暂存本地临服 → 上传远端；Chrome 仅提示「Manus Browser Operator started debugging this browser」；授权为整段会话 open-ended，无法按域名/动作收窄。
- 厂商文案：「the activity is viewed as legitimate, it reliably clears standard access barriers」。

### P6 Chrome 护栏
- Chrome 136+：默认 user-data-dir 不允许 `--remote-debugging-port`（日志 "DevTools remote debugging requires a non-default data directory"）。
- Chrome 147+（Google 品牌版）：静默阻塞、每次重启弹 Allow、`DevToolsActivePort` 可能不写。
- browser-harness PR #142（2026-04）：用 `CHROME_CONFIG_HOME` 指向持久伪路径，使 Chrome 计算的「默认目录」不再是真实默认目录，从而在 Linux 上绕过 Allow 步骤。

### P7 SkillLeak（Xygeni）
- `@szc-ft/mcp-szcd-client` 的 `local-browser-test` skill：`connect()` → `_decryptCredentials()` → DPAPI + AES-256-GCM 解全 profile 已存密码 → `~/.szcd-mcp/deps/decrypted-creds.json` → 作为 MCP tool result 流向 `mcp.szcd-mcp.top`。
- 命名要点：能力藏在 **skill 运行时**，不在 install hook。

## 写入

1. `03_expansion_queue/candidates/[cand]local-control-plane-exposure-2026-11.md`（新建 A 卡，7 模式表 + 6 问 + 证据限制）
2. `08_agent_centric/domains/agent-computer-use.md`：2.1 新增 5 行、Playwright MCP 行加安全侧；2.4 缺口① 改「部分闭环（11-26）」；§四 新增判断 8（置于判断 7 后）；§九 Day4 记录
3. `06_expansion_index/README.md`：置顶 11-26 段（6 行）
4. `04_connections/README.md`：3 条（silver-shield 四元组 / TeamMind 能力组合授信 / 审查点前移）
5. `03_expansion_queue/candidates/[cand]skill-supply-chain-security-2026.md`：§3.5 SkillLeak
6. `_INDEX.md`：11-26 深耕行
7. `07_radar_watch/current_focus.md`：状态行 + 周四勾选

## 未做

- 本机 `ss -ltnp` 监听面、profile 目录权限核查（周五）；DNS rebinding 只设计未实跑；chrome-devtools-axi 原 advisory 被 robots 拒（只取镜像，CVSS 分数未取）；Chrome 官方 release note 原文未取；SkillLeak 单源未核 npm advisory。
