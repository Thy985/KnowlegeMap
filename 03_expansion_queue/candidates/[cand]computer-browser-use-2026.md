# 候选证据卡 · [cand] Computer/Browser Use 工具集 GA + browser-use 生态

> 状态：`[cand]` ｜ 分类：Browser/Computer Use / Agent Harness ｜ 发现：2026-09-01 ｜ 等级：**A**

## 一句话定位
2026 年"Agent 操作真实环境"能力集中 GA：Claude browser use / computer use 工具集去掉 beta、browser-use 成为开源事实标准、Playwright MCP 服务化——Agent 从"对话"走向"动手"。

## 1. 它是什么 / 解决什么问题
- **Claude browser use tool**（`browser_toolset_20260801`，2026-05-27 上线，GA）：运行在你应用托管的浏览器里，读 accessibility tree/元素/表单/标签页，27 个内置成员工具 + 4 个可选（文件上传/JS 执行等），不依赖整机桌面["https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool"][https://platform.claude.com/docs/en/release-notes/overview#may-27-2026]
- **Claude computer use tool**（`computer_toolset_20260801`）：整桌面操作，GA，无需 beta header["https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool?product_id=1010787"]
- **browser-use**（Python/Playwright）：开源事实标准，MCP-native，Claude Code/Codex/Cursor/Hermes/OpenClaw 直接可用["https://github.com/browser-use/browser-use/"]
- 生态选择：嵌入式产品→Claude Computer Use；自托管开源→browser-use；MCP 生态→Playwright MCP servers["https://ztabs.co/blog/ai-browser-automation-2026"]

## 2. 与我的知识/项目关系
- **campus_order（OpenClaw 接入）**：OpenClaw 已兼容 browser-use 生态，可直接给校园场景加"Agent 代操作"
- **E2E-CLI（遗留测试项目）**：Playwright MCP + browser-use 让 E2E 测试从"脚本"变"Agent 自主修复"
- **agent-attention**：browser use 的"可见性/反馈"与通知基础设施可联动
- 与我的 Tool System 知识直接碰撞：真实环境操作的工具边界/权限问题

## 3. 证据与活跃度
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（Claude 官方文档 + 生态多源） |
| 来源 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool ｜ https://github.com/browser-use/browser-use/ |
| 活跃度 | 极高（2026-08 持续更新；Claude 平台 release notes 密集） |
> **雷达增量（2026-09-14，Changed）**：
> - **GPT-6 Astra（2026-09-03/04 发布）**：OpenAI 旗舰，"为 **Computer use、Browser Use、软件工程、网络安全**树立新标杆"；105 万 token 上下文 + 12.8 万输出 + Low~Max 五档推理强度["https://pdf.dfcfw.com/pdf/H3_AP202609061829071760_1.pdf"]["http://m.toutiao.com/group/7681426829210665518/"]
> - **Claude computer use 产品化（09-12 release notes）**：Cowork + Claude Code + Dispatch 中 **Pro/Max 用户可直接授权 Claude 使用电脑**（打开文件/运行工具/点击导航，零配置）——computer use 从 API 工具走向消费级产品["https://support.claude.com/en/articles/12138966-release-notes?35444d06_page=16"]
> - **frontier 四模型三日齐发（09-01~03）**：Anthropic Claude Fable 5.1、OpenAI GPT-6 Astra、Google Gemini 3.8 Flash、Meta Muse Spark 1.3——computer use 能力是各旗舰标配卖点["https://yorozuipsc.com/uploads/1/3/2/5/132566344/be586a8853d9417591f0.pdf"]
> - **Gemini CLI v0.61 nightly（09-09/10）**：NTFS 路径修复 + **沙箱安全加固**——CLI agent 沙箱化继续推进["https://releases.sh/google/gemini"]
> - **含义**：① computer use 从"小众 API"进入**消费级产品与旗舰标配**阶段，campus_order/E2E-CLI 的"Agent 代操作"路径成熟度显著上升；② SIR 攻击（见 agentic-attack 卡 09-14 增量）专门劫持 computer-use agent——能力普及与攻击面扩大同步，安全约束必须前置
> **雷达增量（2026-09-20，GA 产品化 + 生态入场）**：
> - **Anthropic Computer Use/Skills/Files API 正式 GA（09-18）**：三大核心 agent API 企业级 GA（含完整 SLA），同时发布**新 Browser Use 工具**（agent 自主导航操作浏览器）；**Computer Use 支持单模型调用内连续多动作**——任务更快、往返更少["https://aicoder.com/news/news-20260918-anthropic-computer-use-skills-files-api-ga"]["https://ai-damn.com/anthropic-s-big-update-computer-use-skills-and-files-apis-now-live-1787526310076"]
> - **Vercel Agent Browser（09-15）**：免装浏览器驱动的 LLM 网页交互（点击/滚动/交互）——Vercel 以基础设施商身份入场["https://ai-damn.com/vercel-s-new-tool-lets-ai-actually-use-websites-like-humans-1768345535936"]
> - **Browserbase 重建 Stagehand（09-09）**：更快更 token 高效的浏览器 agent + **MCP 工具面** + Playwright→Stagehand 转译——"code your way through the web"["https://releasebot.io/updates/browserbase/browserbase"]
> - **Skyvern 3.0 Engine beta（08 月）**：持久工具循环 + 标记截图回退 + **原生 hCaptcha/TOTP/邮件一次性码处理**——验证码/2FA 自动化突破["https://agenticindex.io/vendors/skyvern"]
> - **Gemini Spark 降价普及（07-30 Chrome 集成，09-14 报道）**：操作真实桌面浏览器 + 使用登录账户/密码，敏感操作（支付）强制人工批准；价格从 $249/月 Ultra 独占降至 $19 套餐捆绑["https://www.toolbit.ai/blog/inside-gemini-spark-googles-new"]
> - **含义**：① computer use 进入"**GA 标准化 + 基础设施商入场 + 验证码能力突破**"三线并进——E2E-CLI/campus_order 的"Agent 代操作"已无技术壁垒；② Gemini Spark 的"敏感动作人工批准"与 BragJack 攻击（09-19 轮）同帧——浏览器 agent 权限边界是产品层一等问题
> **雷达增量（2026-09-25，浏览器内置 agent 再添厂商）**：
> - **Claude for Chrome（09-24 发布）**：Anthropic **浏览器扩展 AI agent**（research preview，首批 1,000 Max 订阅者 + waitlist）——sidebar 内保持上下文、对话并**代执行浏览器任务（点击/填表）**["https://www.techshotsapp.com/technology/anthropic-introduces-claude-for-chrome--ai-agent-inside-your-browser"]
> - **含义**：① 浏览器内置 AI agent 从 Google（Gemini Spark）/Perplexity（Comet）扩展到 **Anthropic**——"浏览器=agent 主战场"三巨头齐集，E2E-CLI/campus_order 的"Agent 代操作"可跟随任一生态；② **BragJack 攻击面（09-19）随 Claude for Chrome 扩大**——内置 agent 常驻浏览器 = 默认攻击入口（劫持/数据窃取面），silver-shield 浏览器侧风险检测与 campus_order 部署需把"浏览器 agent 权限边界"前置为设计约束
> **雷达增量（2026-09-29，browser use 企业 GA + 零配置新入口）**：
> - **Anthropic Computer Use / Skills / Files APIs 全面 GA（09-18）**：三核心 agent API 升企业级 GA（full SLA）+ **原生 Browser Use 工具发布**（终端编码与实时浏览器执行打通）——"browser use"成为 API 层一等公民["https://aicoder.com/news/news-20260918-anthropic-computer-use-skills-files-api-ga"]
> - **computer/browser toolsets 上 Google Cloud（09-28）**：computer_toolset_20260801/browser_toolset_20260801 在 GCP 对 Claude 全系可用——**跨云可用性确认**["https://platform.claude.com/docs/en/release-notes/overview"]
> - **Vercel Agent Browser（09-24）**：LLM **点击/滚动/交互网页**零配置（免 driver/依赖）——"用起来像人"的浏览器交互产品化["https://ai-damn.com/vercel-s-new-tool-lets-ai-actually-use-websites-like-humans-1768345535936"]
> - **Tencent BrowserSkill（06-2026 开源，MIT）**：DOM 观察+截图混合感知，跑在用户自己浏览器（CLI + Chrome/Edge 扩展）——**国内大厂开源浏览器 agent 桥**["https://aiwiki.ai/wiki/ai_browser_agent"]
> - **含义**：① **"browser use"完成从实验能力到企业 GA 的跃迁**（Anthropic full SLA + GCP 跨云）——E2E-CLI/campus_order 的浏览器自动化基线可直接对齐官方 API 而非自研；② **Vercel 零配置 + Tencent 开源**提供两条低成本替代（Agent Browser/ BrowserSkill）——Tafcm 若做"用户可见浏览器操作"可先复用；③ browser use 全面产品化 = **攻击面同步扩大**（Vercel/Tencent 工具均可被劫持）——silver-shield 需覆盖"agent 浏览器操作"监测
> **雷达增量（2026-10-05，开发者工具链 computer use + AI 浏览器新玩家）**：
> - **GitHub Copilot computer use（10-01 上线）**：Copilot 可**交互桌面应用**（/computer 命令 + 描述期望结果）——computer use 进入主流开发者工具链（VS Code 生态）["https://github.blog/changelog/2026-10-01-github-copilot-can-now-interact-with-desktop-apps/"]
> - **Perplexity Comet（09-27 收录）**：**AI-native Chromium 浏览器**——助手跨 tab 读取 + agent 点击/填表完成任务（预订/购物/邮件），**企业版带 admin 控制/审计日志/MDM 部署**——"浏览器即 agent 平台"再添搜索系玩家["https://agenticindex.io/vendors/perplexity-comet"]
> - **Claude Browser Use GA 技术细节（08-20）**：browser use 读取**页面 accessibility tree、按元素引用点击**（而非猜测屏幕坐标）+ computer use **批量化多动作 turns**——技术路线分化：a11y-tree 引用 vs 像素坐标["https://aitoolsreview.co.uk/insights/claude-computer-use-skills-files-ga"]
> - **含义**：① **computer use 从"AI 产品功能"进入"开发者工具链"**（GitHub Copilot 桌面应用交互）——E2E-CLI 的"端到端诊断"可借鉴"agent 直接操作被测桌面应用"模式；② **Perplexity Comet 证明"AI 浏览器"品类从消费级走向企业级治理**（admin/audit/MDM）——与 campus_order/OpenClaw 的浏览器操作管理同向；③ **a11y-tree 引用 vs 坐标猜测的技术分化**影响自动化稳定性——自研/选型 browser agent 时优先 a11y-tree 方案（Claude 路线）以规避坐标漂移

> **雷达增量（2026-11-23，Changed — 对象级重写）**：**browser-use 1.0 推翻重写**（1.0.0 于 2026-11-10，1.0.6 于 11-16）。官方原文「We started over. The agent now writes Python in one persistent REPL, straight on Chrome DevTools Protocol. **No DOM serializer, no action schema, nothing in between**.」同模型对比 0.x 自报 **+33 分 / 便宜 2.7–5.2x / 快 2–3x**（BU Bench v2，60 任务 ×3 次，云浏览器，11-09）；默认改为**云浏览器 + Browser Use 网关 key**（本地须显式 `Browser('chromium')`），默认 `max_steps=100` / `timeout=1700s`（0.x 为 500）；1.0.5（11-14）新增**逐次运行的 judge**（`success` / `failure_reason` / `prompt_injection_detected` / `bot_block_or_captcha_detected`）；1.0.6 默认模型换 BU 4.0（token 单价为 bu-fast 的 15 倍）。["https://pypi.org/project/browser-use/"]["https://followagents.com/en/agents/browser-use"]
> **含义**：① 这是**架构级路线变更**而非普通 release——删掉中间抽象层说明维护成本已高于模型能力缺口，与 Webwright「脚本即产物」同一方向；② 官方建议 `pin ==1.0.6`（releases move fast and can break APIs）；③ 本项目此前「browser-use 作为开源事实标准」的定位需改写为「已转向 REPL+CDP 的自有云网关产品」，自托管选型要重新评估（默认路径依赖其云与 key）。

**雷达增量（2026-11-24，Changed — 1.0.7 → 1.0.8，含官方自述的控制面风险）**：
> - **版本**：1.0.7（GitHub 11-20 20:01 / PyPI 11-21）、**1.0.8（PyPI 2026-11-22，当前最新）**；官方改为建议 `pin ==1.0.8`（此前 1.0.6）。仍在高频迭代。
> - **judge 扩面**：`result.judgement` 增 `gotchas`（站点经验：限流、页面顺序、字段格式），新增 `judge_context` 可传自有评判标准、`judge=False` 可关；judge 的 token/成本计入 `result.usage` / `result.cost_usd`。仍是"同一模型自评"，但**外部判据可注入** → 缺口② 从"纯自评"变成"自评 + 可给外部标准"，判定主体没变。
> - **凭据遮罩 ≠ 隔离**（官方原文）：`sensitive_data` + `type_secret()` 会在 cell output / checkpoints / tool results / task / result 中把值替换为 `<secret:name>`，但明写 **"Not a sandbox: model-written Python can read the value, and screenshots"** → E4 只是显示层脱敏，不是执行面隔离。
> - **官方自述本地控制面风险**（原文）：`Browser('chrome')` 与 `profile=` 打开的是 **127.0.0.1 上无认证的调试端口**，"on a shared machine, other local users can attach to that browser and its logins" → 直接证实判断 7（隔离最小单位是 profile 而非进程）与缺口①；也意味着"借用真实登录态"在多用户机器上等于把登录态暴露给同机任意用户。
> - **profile 三档（E1 光谱）**：`Browser('chromium')` 全新临时 profile、结束后删除；`Browser('chrome', profile='Work')` 在用户 profile 的临时副本上开新 Chrome（关同步、Windows 除外用户 Chrome 可继续开）；`Browser('chrome')` 直接挂用户已开 Chrome（需开 remote debugging）。
> - **含义**：① browser-use 亲手拆掉了"自托管==可信"的假设，安全边界必须由部署方提供（一次性 profile / 专用系统用户 / 端口绑定 loopback）；② E2E-CLI / Tafcm 若采用，默认应 `Browser('chromium')` 而非 `Browser('chrome')`；③ `judge_context` 是把外部判据接进判定的唯一官方入口，周五应核对它是否写进 trace 可复核。

## 3.9 源码级验证（2026-11-27，周五 Day5｜未实跑）

取包 `browser_use-1.0.8-py3-none-any.whl`（300,909 B / 47 py / 976 KB）。四个验证问题全部有代码答案：

- **无 DOM serializer 是代码事实**：`grep -rln "serialize_dom|DOMSerializer|markdownify|dom_tree|bs4"` 零命中。执行面是 `browser/`（`browser.py` 65 KB + `local.py` 27 KB）+ `ax.py` + `repl/`（`worker.py` 58 KB / `session.py` 28 KB）。**「one persistent Python REPL on raw CDP」成立。**
- **judge 是模型，不是确定性核验**：`agent/judge.py` 单次 `model_request` + Pydantic `Judgement`。`judge_cached` **把 judge 当作 run 的再一轮**，复用 run 的 messages/instructions/tool definitions 吃 prompt cache → **judge 与 actor 共享上下文，不独立**；`judge_run` 另发新 prompt（全额计费）。trace 预算 `120_000` 字符（超限保头 1/5 + 尾）、单 part `5_000`、截图 `4` 张（Cloud 20）、超时 180s。`judge_context` 拼成 `<judge_context>` 置于 prompt 前部、上限 `20_000` 字符、明写「user's own criteria and comes first」。
  → 结论：**「判据可注入」≠「判定依据外部」**。它做到了前者，未做到后者。
- **本地执行必须显式**：`browser/local.py:333` 自建 `--user-data-dir=… --remote-debugging-port=0`（随机端口）；用户自开 Chrome 需 `BU_CDP_URL`；**9222/9223 永不猜测**（原文 `Ports 9222/9223 are never guessed`）。
- **`max_steps` 两处默认**：`Agent.run(max_steps=100)` 入口默认（最后一步是 delivery-only turn），内部 `Session.max_steps=1000`。此前记录的「100」对入口成立，但**不能推断 100 步必断**——内部上限是 1000。

**安全侧新增（并入 P1 证据链）**：`require_debug_port()` 的 docstring 明写 browser-harness 0.1.13 会 attach 到 `127.0.0.1:9222/9223` 上**任何应答者**（「another user's Chrome, a fake one」），后果是「the agent then typed your secrets into their browser」；并实现 `_left_over()` 在 `DevToolsActivePort` 残留且端口被他人占用时**直接抛错**。→ 厂商是在防**自己的 attach 行为**被劫持，不是防外部攻击。

## 4. 验证计划
- [x] **源码级核对 1.0.8（2026-11-27）**：无 DOM serializer / judge 机制 / 本地显式 / max_steps 双默认，四项完成（见 §3.9）
- [ ] 跑一次 browser-use 最小 demo（本机 9222 上是活动 Chrome，为不打断会话未接管；需独立 profile 后再跑）
- [ ] 评估给 campus_order/OpenClaw 加 browser-use 的可行性
- [ ] 与 Claude browser use 对比"托管浏览器 vs 自托管"取舍

## 5. 决策
- [x] 晋升 validated（源码级，2026-11-27；**未实跑**，环境限制已在 §3.9 标注）
- [ ] 维持观察
- [ ] 拒绝
