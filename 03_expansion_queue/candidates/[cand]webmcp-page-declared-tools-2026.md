# 候选证据卡 · [cand] WebMCP（页面声明工具，Give agents tools, not DOM）

> 状态：`[cand]` ｜ 分类：Computer Use / Browser · 动作空间与信任边界 ｜ 发现：2026-11-24 ｜ 等级：**A**

## 一句话定位
WebMCP 让网页把自身功能**声明为结构化工具**供浏览器内 agent 直接调用——把 agent 的动作空间从"操作 UI"改成"调用页面给的契约"，同时把**工具清单本身变成不可信输入通道**。

## 1. 它解决什么问题
- 现状：浏览器 agent 靠抓 DOM / 无障碍树 / 截图去"猜"页面语义（约 40 个 DOM 节点才能推出一件事），慢、token 贵、易点错，且页面里的文字天然是注入通道。
- WebMCP：页面用 `document.modelContext.registerTool({name, description, inputSchema, execute})`（命令式）或注解 HTML 表单（声明式）把能力暴露成工具，agent 直接按 schema 调用，由页面自己执行。
- 官方叙事："Give agents tools, not DOM"；同一 booking widget，左侧抓 DOM、右侧调工具，声称"更快、更安全、更少 token"。**"更安全"是厂商主张，不是证据**——它只是把注入面从页面内容挪到了工具清单。

## 2. 为什么现在值得关注（一手证据）
- **规范状态**（Chrome 官方）：Draft Community Group 规范，非 standards-track；Early Preview 需 Chromium `146.0.7672.0+` 与 `#enable-webmcp-testing` 旗标；Chrome 149 起有 origin trial。页面于 2026-05-18 发布、2026-10-07 更新。
- **Playwright MCP 已把它接进真实工具面（2026-11-18 release）**：页面注册的工具直接出现在工具列表里，名为 `webmcp_<tool>`，带页面自己的 input schema 与 annotations；列表跟随当前 tab；变化时向客户端发 `tools/list_changed`。取代了 v0.0.81 的 `browser_webmcp_list` / `browser_webmcp_call`（已不再经 MCP 暴露）。
  - 官方原话："**Tool names, descriptions, schemas and results come from the page, so treat them as untrusted input.**"
  - 可关：`--no-webmcp`（config `webmcp: false`、env `PLAYWRIGHT_MCP_WEBMCP=false`）；标注为 experimental。
- **Chrome 自己的 agent 安全指引（2026-06-09）**已列出确定性护栏：token 上限、在系统指令中承认 `untrustedContentHint`、限制跨源交互、向用户确认动作；概率性护栏：在任何工具调用前扫描页面上下文与工具说明、扫描工具输出、用不接触不可信内容的 critic 校验计划。
- **暴露范围（二手待核）**：默认 page + 同源 frame + 浏览器内置 agent；`exposedTo: [origins]` 可放宽到指定安全源；可用 Permissions Policy 关闭（来源为社区 PR 对规范的转述，未见一手 spec 原文）。

## 3. 与我的连接
- **连接的项目**：
  - **E2E-CLI**：对启用了 WebMCP 的站点，测试可直接调工具而不是点 UI；但这等于**把断言建立在被测方自己的契约上**——对外部验证是负资产，只适合作为"被测方自证"的补充通道。
  - **campus_order（OpenClaw）**：若站点声明工具，跨站任务的动作数会显著下降；代价是页面掌握语义解释权，agent 更难发现"页面在骗我"。
  - **silver-shield**：新增检测项——工具清单漂移（`tools/list_changed` 中途改写）、恶意 manifest（工具名/描述/参数里夹指令）、输出污染、`untrustedContentHint` 是否被下游承认。
- **连接的知识点**：
  - A 环境表示：参与站点上，表示层从"观察"退化为"读契约"，覆盖率问题变成**opt-in 不对称**（没启用的站点仍要退回 DOM/a11y）。
  - B 动作空间：tool call 与 UI 动作是两种动作语义；前者可被页面重定义，后者受 UI 约束。
  - C2 成功判据：`execute` 返回的字符串（示例 "Performed..."）是**页面声明**，不是外部事实——与本周缺口②同构。
  - F 信任边界：注入从"页面内容"前移到"工具清单"，且发生在**执行之前**（读 description 时即生效）。
- **潜在收益**：给"动作侧"防御一个明确的新面：不只查页面藏了什么字，还要查**agent 的工具清单是谁改的**。

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://developer.chrome.com/docs/ai/webmcp ｜ https://developer.chrome.com/docs/modern-web-guidance/guides/webmcp/webmcp ｜ https://developer.chrome.com/docs/agents/security ｜ https://developer.chrome.com/docs/ai/webmcp/imperative-api/ ｜ Playwright MCP 2026-11-18 release notes |
| 证据等级 | FACT（Chrome 官方文档 + MCP server release notes）；暴露范围一条 DESIGN/二手待核 |
| 验证方式 | 周五可做"结构验证"：读 `@playwright/mcp` 包内 webmcp 相关实现，确认 (a) 是否对页面 schema 做任何校验，(b) `tools/list_changed` 是否触发重新授权，(c) `--no-webmcp` 是否为默认关闭；(d) 无 GUI 时用 `webmcp` 单测/示例页做只读核对 |
| 预期完成时间 | 2026-11-27（周五验证日，作为第 3 个候选；若 browser-use 与 Playwright 源码核对占满则顺延到周六回灌时补） |

## 5. 验证结果
（待回填）

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察（early preview + 旗标 + 规范未定稿；方向重要但当前不可作为生产依赖）
- [ ] 拒绝（原因）
