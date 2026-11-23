# 2026-11-24 Personal Tech Radar 深耕扫描（Computer Use / Browser · 第一周 Day2）

- 当天分工：周二 = **只追增量**（browser-use / Playwright MCP / Webwright / Browser Harness 新 release 与活跃变化），不做全量重建。
- 检索：4 组 general_search + 2 次一手核对（PyPI 包页、npm 包页/Chrome 官方文档）+ 全仓 `grep -a` 去重（关键词 WebMCP / BrowserSkill / 1.0.8 / 1.0.7 / gotchas / sensitive_data）。

## 发现

| 对象 | 结论 | 处置 |
|---|---|---|
| **browser-use 1.0.8**（1.0.7 11-20/21 → 1.0.8 2026-11-22） | Changed（对象级增量） | 并入 S 卡 `[cand]computer-browser-use-2026.md`；能力树锚点行改 1.0.8 |
| ├ judge 增 `gotchas` + `judge_context`（可注入自有判据），成本计入 `result.usage`/`cost_usd` | 判定主体仍是同一模型 → 缺口② 口径微调 | 同上 |
| ├ `sensitive_data` + `type_secret()` 全链路替换为 `<secret:name>`，但官方明写 **"Not a sandbox: model-written Python can read the value, and screenshots"** | 凭据遮罩＝显示层脱敏，不是隔离 | 同上（E4） |
| ├ `Browser('chrome')` / `profile=` 开 **127.0.0.1 无认证调试端口**，"other local users can attach to that browser and its logins" | **判断 7 由"待验证"升为厂商自述** | 同上（E1/E2 + 缺口①） |
| **Playwright MCP 11-18**：页面注册工具直接成为 MCP 工具 `webmcp_<tool>`（页面 schema/annotations/结果；`tools/list_changed`；`--no-webmcp` 可关；取代 v0.0.81 的 list/call） | Changed（新能力面 + 新信任面） | 并入能力树 Playwright MCP 锚点行；抽出 WebMCP 单独立卡 |
| **`browser_take_screenshot` 文档已改为"不再排除据截图动作"** | **Day1 基线事实作废**（原记"文档明写不能据此动作"） | 能力树该行改写；周五核执行层是否真放宽 |
| **WebMCP**（Chrome 提案；Chromium 146+ 旗标；Chrome 149 origin trial；Draft CG 规范） | **New（A）** | 新建 `[cand]webmcp-page-declared-tools-2026.md` |
| Playwright MCP README 新增"coding agent 更适合 CLI-as-SKILL，比 MCP 省 token" | 旁证，不改判断 | 记入能力树 §七（与判断 2"代码即动作"同向） |
| Webwright | 未检索到 11-23/24 新 release；GitHub releases 页被 robots 拒取 → **未核** | 不写卡 |
| Browser Harness | 最新 0.1.10（2026-08-26，piwheels），无新版本 | 不写卡 |
| Tencent BrowserSkill | 已在 09-29 增量与 S 卡覆盖；今日二手资料补充"borrow gate 不 fail-open / 借用 tab 不归还给别的会话 Agent Window" | 不重复建卡，记日志 |

## WebMCP 一手事实（进卡）
- Chrome 官方：Draft Community Group 规范，非 standards-track；Early Preview 需 Chromium `146.0.7672.0+` + `#enable-webmcp-testing`；Chrome 149 起 origin trial；页面 2026-05-18 发布、2026-10-07 更新。
- API：`document.modelContext.registerTool({name, description, inputSchema, execute})`；也有声明式（注解 HTML 表单）。
- Playwright MCP 原文："Tool names, descriptions, schemas and results come from the page, so treat them as untrusted input"。
- Chrome agent 安全指引（2026-06-09）：token 上限 / 承认 `untrustedContentHint` / 限制跨源 / 动作需用户确认；概率侧：调用前扫描页面上下文与工具说明、扫描输出、用不接触不可信内容的 critic 校验计划。
- 暴露范围 `exposedTo: [origins]` 一条来自社区 PR 转述，**二手待核**。
- 版本号：npm 页显示 0.0.80、第三方目录显示 v0.0.85（11-09）、release notes 页更新于 11-18 → **WebMCP 变更所属版本号未定，记为"11-18 release，v0.0.8x 待核"**，不在仓内写死。

## 判定
- 该对象是否在既有索引命中：WebMCP 0 命中 → 新；browser-use/Playwright MCP 已命中 → 增量并入，不新建碎片卡。
- 价值阈值：WebMCP **A**（方向结构性重要，但 early preview + 旗标 + 规范未定稿，不能作生产依赖）；两条 changed 为 S/A 对象的实质变化。
- 未做：任何实跑（本机无 GUI）；Playwright `@playwright/mcp` 包内 webmcp 实现未读（周五）。
