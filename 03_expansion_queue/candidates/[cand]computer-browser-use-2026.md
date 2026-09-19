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

## 4. 验证计划
- [ ] 跑一次 browser-use 最小 demo（任务：抓取并导出结构化数据）
- [ ] 评估给 campus_order/OpenClaw 加 browser-use 的可行性
- [ ] 与 Claude browser use 对比"托管浏览器 vs 自托管"取舍

## 5. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
