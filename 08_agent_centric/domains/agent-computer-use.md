# Domain Tree · Computer Use / Browser（真实环境操作层）

> 建立：2026-11-23（周一，Computer Use / Browser 周第一天）｜ 类型：领域能力树/基线
> 定位：Tafcm / campus_order / E2E-CLI / OpenClaw 的真实环境操作共性底座；也是 silver-shield 的"动作侧"防御面（相对 Memory 周的"存储侧"）。
> 树与图分工：本文件是 Tree；跨域复用见 `08_agent_centric/capabilities/graph.md`。
> 上游交接前提（Memory 周 §十 10.5）：三条判据迁移到真实执行——**执行通道是否唯一 / 成功判据来自哪里 / 动作回执能否核验**。本周所有判断都以这三问为骨架。
> 与 Runtime 周的分界：Runtime 管"agent 自己跑在哪"（进程/沙箱/身份/网络）；本周管"agent 通过什么界面碰外部世界"（浏览器/桌面），二者的隔离结论可互相引用但**不互相替代**。

## 一、领域树

```
Computer Use / Browser
├── A. 环境表示（Environment Representation）：agent 到底"看见"什么
│   ├── A1. 原始 DOM / HTML（CSS selector / XPath / 数字索引）
│   │   └── A1.1 过滤与裁剪（可交互元素提取、可见性判定、iframe/shadow DOM 穿透）
│   ├── A2. 无障碍树（role + accessible name + state + ref id）
│   │   ├── A2.1 稳定引用（ref 生命周期：重渲染即失效）
│   │   └── A2.2 语义定位（getByRole/getByLabel/getByText 的可迁移性）
│   ├── A3. 像素 / 坐标（screenshot + grounding）
│   │   ├── A3.1 分辨率与 DPR / 缩放 / 多显示器
│   │   └── A3.2 视觉定位（元素检测 → 坐标映射；坐标漂移）
│   ├── A4. 混合表示（a11y 为主 + 截图按需；vision 三档 always/on-demand/never）
│   ├── A5. 非浏览器表示（桌面窗口树 / UI Automation / AT-SPI / 终端文本 / 画布状态）
│   └── A6. 表示覆盖率（canvas / 自绘控件 / 无 label 图标 / 跨域 iframe 的漏检）
├── B. 动作空间与 grounding
│   ├── B1. 抽象动作（click(ref) / type / select / navigate / scroll）
│   ├── B2. 代码即动作（模型直接写脚本或 Python 在 REPL 里跑；Playwright 脚本、CDP 直连）
│   │   ├── B2.1 脚本产物（可复用/可审查的 artifact）vs 一次性会话
│   │   └── B2.2 代码生成的执行边界（在哪跑、能 import 什么、能碰哪些文件）
│   ├── B3. 坐标动作（click(x,y) / drag / 键鼠事件序列）
│   ├── B4. 动作原子性与批处理（单动作 turn vs 多动作 batch；失败回滚粒度）
│   ├── B5. 可执行性判定（元素可见/可点/未被遮挡/未 disabled；等待策略）
│   └── B6. 幂等与可重放（同一目标重放是否等价；脚本 vs 会话录制）
├── C. 感知与自验证（Perception & Self-Verification）
│   ├── C1. 观察-动作循环（observe → act → observe；每步观察成本）
│   ├── C2. 成功判据来源（执行外部事实 > 页面文案 > 模型自评）
│   │   ├── C2.1 外部事实（DOM 终态 / 网络响应 / 落库记录 / 文件校验和）
│   │   ├── C2.2 页面文案（"操作成功" toast —— 可伪造、可延迟）
│   │   └── C2.3 模型自评（judge LLM：success / failure_reason；无独立证据）
│   ├── C3. 进度判定（partial completion、step budget、超时预算）
│   ├── C4. 环境异常检测（登录墙 / CAPTCHA / bot 拦截 / 弹窗 / 会话过期）
│   ├── C5. 不确定性表达（何时该停下问人，何时可以猜；"guess rather than ask" 反模式）
│   └── C6. 静默假成功（页面说成功、实际未落库；重试导致重复副作用）
├── D. 会话与状态
│   ├── D1. 会话生命周期（persistent session / 临时 profile / 冷启动成本）
│   ├── D2. 登录态与凭据继承（cookie / localStorage / 已登录账号 = 权限放大器）
│   ├── D3. 状态恢复（崩溃/超时后 resume；checkpoint 粒度）
│   ├── D4. 多标签 / 多窗口 / 同源策略边界（跨 tab 数据流）
│   ├── D5. 会话与任务解耦（一个会话服务多任务 vs 一任务一会话）
│   └── D6. 环境漂移（live web 改版、A/B 实验、地区/语言差异、时间相关状态）
├── E. 隔离与凭据
│   ├── E1. Profile 隔离（每任务新 profile / 一次性 profile / 目录权限）
│   ├── E2. 本地控制面暴露（CDP 端口、MCP server 绑定地址、通配 CORS、调试端口）
│   ├── E3. 桌面会话隔离（VM / 容器 / 独立用户 / 虚拟显示）
│   ├── E4. 凭据外注（短时令牌 / vault 代理 / 不落 profile / 不落环境变量）
│   ├── E5. 文件系统与剪贴板边界（下载目录、上传路径、复制粘贴通道）
│   ├── E6. 出网控制（egress allowlist、代理、DNS）
│   └── E7. 资源与并发（多 agent 共享浏览器、profile 串用、端口争用）
├── F. 信任边界（Trust Boundary）
│   ├── F1. 页面内容 = 不可信输入（整屏皆上下文；间接注入的第一入口）
│   ├── F2. 隐藏通道（Unicode tag 字符 U+E0000–E007F、零字号、白底白字、离屏、注释、alt、aria-label）
│   ├── F3. 低害目标注入（"star 仓库 / 装个包 / 多看两页"——与正常动作不可区分）
│   ├── F4. 中途劫持（把攻击目标绑成用户任务的前置条件，完成后回归原任务）
│   ├── F5. 会话继承放大（已登录态 × 虚构框架 → 护栏失效 → 凭据外送）
│   ├── F6. 同源与跨源混流（agent 把不同 origin 的信息混进一份上下文/记忆）
│   ├── F7. 人类确认点设计（确认粒度、确认疲劳、低害动作不确认）
│   └── F8. 页面 ↔ 记忆的混合边界（读到的东西进 memory，下次跨站复用）
├── G. 人机交接（Human Handoff）
│   ├── G1. 接管与交还（human takeover / pause / resume 的上下文传递）
│   ├── G2. 确认点挂载（不可逆动作：支付/发送/删除/授权/安装）
│   ├── G3. 中断理由说明（为什么停、当前假设、已完成的步骤）
│   ├── G4. 权限降级（只读模式、受限动作集、单站点白名单）
│   └── G5. 批准审计（谁批的、批了什么、依据哪一帧）
└── H. 可观测与回放
    ├── H1. 轨迹（动作序列 / 截图 / DOM 快照 / 网络 / 控制台）
    ├── H2. 动作回执（动作 id + 目标标识 + 前后状态 + 结果 + 覆盖范围）
    ├── H3. 回放确定性（脚本重跑 vs 会话回放；时间/随机/网络/登录态的影响）
    ├── H4. 失败归因分类（表示错 / grounding 错 / 判据错 / 策略错 / 环境漂移）
    ├── H5. 成本可观测（token / 步数 / 时长 / 云浏览器小时）
    └── H6. 静默失败防护（"success=True" 不构成证据；需外部断言）
```

## 二、基线（锚点 / 基准口径 / 批判 / 缺口）

### 2.1 锚点表

| 对象 | 对应层 | 关键事实 | 证据等级 | 状态 |
|---|---|---|---|---|
| **browser-use 1.0.8**（2026-11-22；1.0.6 于 11-16，1.0.0 于 11-10） | A4 / B2 / C2.3 / H2 | **推翻重写**：agent 在**一个持久 Python REPL 里直接写代码、跑在原始 CDP 上**，"no DOM serializer, no action schema"；同模型对比 0.x 自报 **+33 分 / 便宜 2.7–5.2x / 快 2–3x**；默认云浏览器 + 网关 key；默认 `max_steps=100`、`timeout=1700s`；1.0.5（11-14）新增**每次运行由自选 judge 模型判**（`success` / `failure_reason` / `prompt_injection_detected` / `bot_block_or_captcha_detected`）；**1.0.8 增 `gotchas` + `judge_context`**（可注入外部判据，判定者仍是同一模型）；官方自述 `Browser('chrome')`/`profile=` 会开 **127.0.0.1 无认证调试端口**，同机用户可接管登录态；`sensitive_data` 明写 **"Not a sandbox: model-written Python can read the value, and screenshots"** | FACT（PyPI + GitHub Release）+ 自报数字 | `[cand]` → 本周五验证（1.0.8） |
| **Playwright MCP**（MS 官方，70+ 工具） | A2 / B1 / D1 / H1 | 默认**无障碍快照**而非像素；每元素给 `ref`（如 `e5`），动作按 ref 而非坐标；跨 Chromium/Firefox/WebKit/Edge；**默认持久会话**（登录态与 cookie 跨会话保留）；官方定位"no vision models required"；**2026-11-18 起把 WebMCP 页面注册工具直接暴露为 `webmcp_<tool>`**（名称/描述/schema/结果均视为不可信，`--no-webmcp` 可关）；**`browser_take_screenshot` 文档已改为不再排除"据截图动作"**（推翻 Day1 基线） | FACT（playwright.dev/mcp + release notes） | `[cand]` |
| **Webwright**（MS Research，`microsoft/Webwright`） | B2.1 / H3 | 终端原生：agent 写 Playwright 脚本、跑 bash、看日志、迭代；**持久产物是脚本**（可复用/可审查/可回放），会话只是进程；Online-Mind2Web **86.7%**、Odysseys **60.1%**（基线 GPT-5.4 33.5%） | FACT（官方仓库/页/论文）+ 自报基准 | `[cand]` |
| **Browser Harness**（browser-use 团队） | B2 / F1 / EP-002 | 极简自愈 harness：一根 CDP WebSocket 连 Chrome，agent 在 `agent-workspace/` 里边跑边写缺失代码；无框架、无 recipes；15.7k stars、PyPI 0.1.6 | FACT（仓库/包） | `[cand]` |
| **Claude browser/computer use toolsets**（`browser_toolset_20260801` / `computer_toolset_20260801`，均 GA） | A2/A3 / B1 / G2 | browser 侧读 accessibility tree + 元素引用（非坐标猜测），27 个内置成员工具 + 4 可选；computer 侧整桌面操作；支持单次调用内**连续多动作**；09-12 起 Pro/Max 可直接授权使用电脑 | FACT（官方文档/Release Notes） | 锚点（不建卡） |
| **OSWorld-Verified**（369→360 任务，执行式评测） | C2.1 / C3 | 人类基线 **72.36%**；2024 年 SOTA 12.24% → 2026 年多模型越过人类线（Claude Fable 5 自报 85.0%、开源 Holo3-35B-A3B 82.6%、Qwen-CUA 论文 86.2）；**verified 与自报差距 6–11pt**（Sonnet 4.6 72.5 vs 78.5、Opus 4.8 72.7 vs 83.4） | 第三方汇总 + 论文 | 评测口径 |
| **OSWorld 2.0**（arXiv 2606.29537，2026-06-28；v2 07-13） | C3 / C5 / C6 / H4 | **108 个长时任务**，人工中位 1.6 小时，平均 **318 次工具调用**（1.0 约 30 次）；500 步内二值完成率 Claude Opus 4.8 **20.6%** / 部分分 54.8%，GPT-5.5 约 13%；10 月榜 Opus 5 34.72%/70.19%；**失败画像**：丢约束、漏中途到达的信息、**猜而不问**、**跳过验证**、隐藏状态恢复差 | FACT（论文 + 官方站 + 榜） | 关键证据 |
| **agent-desktop**（Vercel Labs，npm 1.2.0，Apache-2.0） | A2 / A6 / B1 / C2 / D3 / G | 桌面侧无障碍树 + ref：`snapshot --app Finder -i` → `@s8f3k2p9:e8`（ref 携带快照 id，裸 `@e8` 报 `INVALID_ARGS`）；UI 变了动作返回 `STALE_REF` / `AMBIGUOUS_TARGET`；**错误自带 `disposition.retry` 是否安全**；默认 headless（不动真实指针/焦点），`--headed` 才物理输入；60 命令（56 可用，`key-down/up`、`mouse-down/up` 需 daemon 能释放按住键才执行）；1.2.0 起 `agent-desktop mcp` 把每条命令暴露为 `desktop_*` stdio 工具；`--stdin` 让密钥不进 argv；跨 macOS AX / Windows UIA / Linux AT-SPI；官方自警「snapshot/clipboard/截图可能含隐私桌面内容」 | FACT（npm 1.2.0 README）+ 第三方（per-agent cursor） | `[cand]` → 周五/周六包级核对 |
| **ComponentBench**（arXiv 2608.18307） | A1 / A6 / B1 / C3 | 同任务、同 harness，只换观察/动作空间（AX-tree / Set-of-Marks / Pixel / Browser-Use）：GPT-5 mini **AX 83.1 → Pixel 48.9（−34.2pt）**，GPT-5.4 反而 **Pixel 83.8 > AX 81.5 > SoM 77.0**；clutter 使 Pixel **−14.3%** 而 AX 仅 **−0.2%**，紧凑间距 Pixel −13.6% / AX −4.5%；任务级不对称：**123 个任务 AX 稳过而 Pixel 稳挂，反向仅 52**；Drag/Drop AX **72.1** / Pixel 57.4 / SoM 31.8 / Browser-Use **29.7**（DOM 动作面做不了真空间拖拽）；聚合稳定（跑间 ≤1.4pt）但 GPT-5 mini Pixel 有 **17.3% 任务逐条翻转** | FACT（论文表格） | 关键证据（缺口③ 部分闭环） |
| **GUI 回放 / 效果核验族**（OpenAdapt / EchoPath / Activity Frames / AgentRR / agrepl） | B2.1 / C2 / H2 / H3 | **OpenAdapt**：一次演示编译为确定性程序，健康路径零模型调用；故障注入 90 例中「只看屏幕」静默接受 **54/90** → 带外效果校验 **9/90** → 完整 system-of-record 读路径 **0/90**（第二域 24/36→3/36）；**EchoPath**（2609.16635）轨迹→参数化可调用记忆 + 图像目标重瞄（IBTR），中位 token **−90%** / 时间 **−60%**；**Activity Frames**（2608.05784）零模型编译、字节可复现，**但确定性只对存储后的 OCR 文本向前成立、不回溯像素**；**agrepl**（2607.16200）传输层 MITM 重放 F=1.0（只重放外部交互） | 论文（OpenAdapt 为 draft 2026-07） | `[cand]` 品类卡 |
| **CSA《CUA Safety Blind Spots》**（2026-04-15） | F1 / F2 / F7 | 对抗弹窗在 OSWorld + VisualWebArena 上**平均 ASR 86%**，同时任务完成率 **−47%**；"ignore pop-ups" 类系统提示**无效**；隐藏通道（Unicode tag、零字号、白底白字、离屏）通用可打；Promptware Kill Chain 七阶段，36 起真实事件中 **21 起跨 ≥4 阶段**；结构性防御建议 **planner-executor 分离**（特权 planner 不碰不可信内容） | 二手研究摘要（一手待核） | 风险基线 |
| **BioShocking**（LayerX，2026-07） | F3 / F5 / F7 | 纯自然语言"虚构框架"绕护栏 → 窃取已登录凭据；**6/6 被测 agentic 浏览器全部中招**（ChatGPT Atlas / Comet / Claude Chrome 扩展 / Fellou / Genspark / Sigma）；无代码执行、无漏洞利用；修复不一致：OpenAI 已补、Anthropic 修复**仍可绕过**、Perplexity 关单不处理、3 家无回应 | 二手（CSA 研究 note 引 LayerX） | 风险基线 |
| **UW agentic browser 研究**（2026-06-30） | D4 / F6 | 7 款 agentic 浏览器对同源策略处理各异；"像人类用户一样的权限"反而能被骗过人不会中招的招；**不同 origin 的信息在记忆里混流**（压缩/改写导致来源丢失） | 二手（校方新闻） | 风险基线 |
| **Invisible Ink Threats / II-Bench**（arXiv 2608.02018v2） | F3 / F7 / G2 | 低害目标（star 仓库、装包、多看两页）**与正常动作行为上不可区分**，因此同时躲过模型安全机制与人类复核；人机确认范式对此**基本无效** | 论文摘要 | 关键证据 |
| **WebTrap**（arXiv 2605.08310） | F4 | 中途中途劫持：仅 3 条注入指令就让 agent 把攻击目标当作"用户任务的前置条件"，完成后**回归原任务**；在扩展 WASP / InjecAgent 环境上高成功率且保持原任务可用性 | 论文摘要 | 关键证据 |
| **Keil 2025（OSWorld 受控实验）** | F1 / C4 | Anthropic Computer Use 在经典注入与诱导下载恶意软件场景 **100% 失败**（未抵抗），凭据钓鱼场景 80%；措辞微小变化显著改变脆弱率 → 现有防护高度依赖上下文 | 论文 | 历史基线 |
| **CVE-2026-48989**（Windows-MCP） | E2 / E3 | HTTP 传输**无认证 + 通配 CORS + PowerShell 工具** = 浏览器可触发的本地 RCE（PYSEC-2026-3425 / GHSA-vrxg-gm77-7q5g） | FACT（已入安全 S 卡事件日 22） | 复用 |
| **CVE-2026-112136**（Mendix Studio Pro MCP） | E2 | 监听未限 loopback，CVSS 4.0 **9.2**（SSA-710379；NVD 待评估） | FACT（已入事件日 24） | 复用 |
| **Memory 周交接三判据** | B / C2 / H2 | 动作门控位置 > 强度；判定依据必须外部；回执可核验 | 本仓结论 | 验收框架 |

### 2.2 基准口径（三个数字测的不是同一件事）

| 基准 | 测什么 | 现在的数字 | 怎么读 |
|---|---|---|---|
| OSWorld-Verified | 单机短任务、执行式判定 | 人类 72.36%，前沿模型 82–86% | 已过人类线，但只是"单应用短任务"的人类线；**必须区分 verified 与自报** |
| WebArena | 多站点真实 web 任务 | OpenAI CUA 58.1%，最佳企业脚手架约 61.7% | 目前最诚实的公开 web 数字；58% 意味着不能无人值守跑工作流 |
| WebVoyager | 活网导航、自报 | Magnitude 93.9% / browser-use 89.1% / OpenAI 87% | **不要用来做容量规划**：活网在变、全是自报 |
| OSWorld 2.0 | 长时真实工作流（318 次调用/任务） | 20.6% 完成 / 54.8% 部分分 | 这才是"职业级 computer use"的真实距离 |
| ST-WebAgentBench | 安全策略合规（CuP + 风险比） | SOTA 策略遵守差 | 能力 ≠ 合规；本周 F 层的评测参照 |

### 2.3 基准批判（沿用 Memory 周的六条体例，本周新增五条）

1. **自报与 verified 不可比**：同一模型差 6–11pt；引用 OSWorld 数字必须说明 harness 与是否为 Verified，否则等于引用营销材料。
2. **只测 happy path**：所有主流基准都无对抗、无中途状态变化、无确认点，因此"成功率"与"能不能安全地跑"是两个正交量。
3. **短任务成绩不能外推**：30 步到 318 步，完成率从 82% 级掉到 20% 级；把 OSWorld-Verified 当"能力已成熟"是口径错误。
4. **失败画像缺失**：只报成功率不报失败类型，掩盖了"点错"与"没验证"的区别——后者才是长时任务的主因（OSWorld 2.0 明说：skip verification / guess rather than ask）。
5. **活网基准不可复现**：WebVoyager 的数字随时间/地区/A-B 漂移，不能用于回归；回归要用可固定环境的 WebArena/OSWorld 或自建任务集。

### 2.4 缺口表

| # | 缺口 | 层级 | 等级 | 计划 |
|---|---|---|---|---|
| ① | **本地控制面裸露清单**：CDP/调试端口、MCP server 绑定地址、CORS、profile 目录权限、剪贴板/下载目录 | E2/E5 | **S** | 周四扫描 + 周五本机 `ss -ltnp` / profile 权限结构核查（无 GUI，包级+源码级） |
| ② | **动作回执的可核验性**：现框架几乎都只有 `success=True`；browser-use 1.0.8 的 judgement 仍是模型自评（新增 `judge_context` 可注入外部判据，但判定主体未变） | C2 / H2 | **A** | 周五读 browser-use 1.0.8 源码，确认 judgement 字段来源、`judge_context` 是否入 trace、是否有状态断言 |
| ③ | **表示覆盖率**：a11y 树对 canvas/自绘/无 label 控件的漏检率无公开数据 | A6 | A | **部分闭环（11-25）**：ComponentBench 给出受控对照（Drag/Drop、Advanced Editors 上 a11y 与 Pixel 排序相反；clutter 下 Pixel 掉 14pt 而 AX 只掉 0.2pt）；剩余：自建任务集上的漏检率 |
| ④ | **回放确定性**：脚本化（Webwright）vs 会话录制在登录态/时间/网络下的可重放度无实测 | B6 / H3 | B | **升级为 A-（11-25）**：已有 5 个对象可对照（传输 / 编译 / 执行三层确定性），周五做降级验证（SoR 断言两臂） |
| ⑤ | **确认疲劳的量化**：Invisible Ink 只有定性结论，无 field 数据；确认点阈值缺经验值 | F7 / G2 | B | 观察，不投入 |
| ⑥ | **本地/边缘协同**：浏览器 agent 与本地模型（Tafcm）的延迟与上下文预算 | H5 / 边缘 | B | 转 AI Infra 周 |

## 三、验证计划（周五 11-27，2–3 个候选）

1. **browser-use 1.0.8（首选，包级 + 源码级）**：本机无 GUI，按先例降级——`pip download`/装包核对 API 表面是否真的只剩"REPL + CDP"；读源码确认：(a) 是否有 DOM serializer 残留，(b) `judgement` 的 `prompt_injection_detected` 是模型判断还是确定性检查、`judge_context` 落在何处，(c) 默认云浏览器是否意味着本地执行必须显式传 `Browser('chromium')`，(d) `max_steps=100` 对长任务的截断行为。
2. **Playwright MCP（源码级）**：核对 a11y 快照的 ref 生命周期与持久会话默认值；确认 11-18 文档改动后 `browser_take_screenshot` 与 `browser_snapshot` 的分工（是否只是措辞放宽，执行层未变），并核对 `webmcp_*` 工具是否对页面 schema 做校验。
3. **Webwright（只读对比）**：以"脚本产物 vs 会话"作为 B2.1 的对照轴，与 browser-use 1.0 的"REPL 即产物"比较——两者都把持久物从会话挪到了代码，这是本周最值得确认的方向判断。

## 四、判断（Day1 基线，待验证）

1. **表示决定失败模式，不存在通用最优**：a11y 树把"点偏"换成"看不见"（canvas/自绘/无 label 缺失）；像素把"看不见"换成"点偏"。所以选型不是"哪个更先进"，而是"我的任务分布里哪类失败更贵"——E2E-CLI 的回归场景该用 a11y（稳定、便宜），campus_order 的跨站任务该保留视觉通道（真实用户界面有大量非语义控件）。
2. **2026 的收敛点是"代码即动作"**：browser-use 1.0 把 action schema 与 DOM serializer 全部删掉、直接让模型写 Python 跑在 CDP 上；Webwright 早就在做同一件事（脚本为产物）。两家独立收敛说明**中间抽象层的维护成本已高于模型能力缺口**。这对我的直接含义：E2E-CLI 的产物应该是脚本而不是会话回放。
3. **瓶颈已从"会不会点"转到"知不知道自己成没成"**：OSWorld 2.0 的失败画像（跳过验证、猜而不问、丢约束）与 Memory 周判断 7 同构——判据必须来自执行外部事实。`success=True` 是声明，不是证据。
4. **人机确认不是安全边界**：Invisible Ink（低害目标与正常动作不可区分）+ BioShocking（虚构框架让护栏失效，6/6）+ 弹窗 ASR 86% → 确认只在"人类能判读为危险"时有效。确认点必须绑**不可逆 / 跨信任域**动作（支付、发送、删除、授权、安装、外发文件），而不是"敏感"这个模糊标签。
5. **会话继承是权限放大器，风险不在"能读到密码"**：agentic browser 继承全部已登录态，同时又与攻击者可控的文本共享同一上下文——真正的危险是"凭据与指令同处一个可被改写的窗口"，而不是凭据本身被读。UW 研究补了另一半：跨 origin 的信息在记忆里混流后连来源都丢了。
6. **基准只测 happy path，能力数字与安全数字必须分开报**：82% 的 OSWorld 与 86% 的弹窗 ASR 可以同时成立，因为测的不是同一件事。任何"agent 可无人值守"的结论都必须同时给出完成率、合规率（ST-WebAgentBench 式 CuP）与静默失败率。
7. **隔离的最小单位是 profile 而非进程（待验证）**：CDP 端口 + 持久 profile = 同机任意进程可取用登录态；"一任务一 profile + 一次性凭据"比"套一层容器"更贴近实际威胁面。这条要在周五用本机端口/目录核查证实或推翻。

## 五、项目映射

| 项目 | 落点 | 具体约束 |
|---|---|---|
| **E2E-CLI** | B2.1 / C2 / H2 | 产物改为"可复用脚本 + 外部断言"，不接受 `success` 布尔；失败必须能归到 H4 五类之一 |
| **campus_order（OpenClaw）** | A4 / D2 / F7 | 跨站任务保留视觉通道；登录态按任务隔离；支付/提交类动作强制确认且确认粒度为"具体动作 + 目标 + 金额" |
| **Tafcm** | E1 / H5 | 本地桌面场景优先一次性 profile；不把用户真实浏览器 profile 借给 agent |
| **silver-shield** | E2 / F1–F6 | 新增"动作侧"检测项：本地控制面端口扫描、页面隐藏通道、跨 origin 混流、确认点缺失；与 Memory 周 F 层形成"读进来 / 点下去"两侧 |

## 六、Day1 记录（2026-11-23）

- 建立八层树 A~H（A 环境表示 / B 动作空间与 grounding / C 感知与自验证 / D 会话与状态 / E 隔离与凭据 / F 信任边界 / G 人机交接 / H 可观测与回放），含 6 个二级密切分（A1.1/A2.1/A2.2/A3.1/A3.2/B2.1/B2.2/C2.1–C2.3），共 44 个节点。
- 锚点 12 行（3 张在队卡 + Playwright MCP / Claude toolsets / OSWorld 1.0+2.0 / CSA / BioShocking / UW / II-Bench / WebTrap / Keil / 两条本地控制面 CVE + Memory 交接）。
- **Day1 意外收获（Changed）**：browser-use 在 11-10~11-16 完成 **1.0 推翻重写**（删掉 DOM serializer 与 action schema，改持久 Python REPL 直连 CDP），已作为增量写入 `[cand]computer-browser-use-2026.md`。
- 基准批判 5 条、判断 7 条、缺口 6 项（S 1 / A 2 / B 3）。
- 未做：任何实跑（本机无 GUI）；缺口①②③ 排到周五。

## 七、Day2 增量记录（2026-11-24，周二）

- **Changed · browser-use**：1.0.7（11-20/21）→ **1.0.8（11-22）**；judge 增 `gotchas` / `judge_context`；官方自述 `Browser('chrome')` / `profile=` 开 127.0.0.1 无认证调试端口；`sensitive_data` 明写"非沙箱"。已并入 `[cand]computer-browser-use-2026.md`。
- **Changed · Playwright MCP**：11-18 release 把 **WebMCP 页面工具**直接暴露为 `webmcp_<tool>`（页面提供的名称/描述/schema/结果均不可信，`tools/list_changed` 可中途改工具面，`--no-webmcp` 可关）；同时 `browser_take_screenshot` 文档**不再排除"据截图动作"**——Day1 基线里"文档明写不能据此动作"这一条作废，改记为"措辞已放宽，执行层是否强制待周五核"。
- **New · WebMCP**：新建 A 卡 `[cand]webmcp-page-declared-tools-2026.md`。核心不是"更快"，而是**动作空间从 UI 操作变成页面给的契约**：注入面前移到工具清单（执行之前），成功判据变成页面 `execute` 的返回值（自证）。
- **No Action**：Webwright 未检索到 11-23/24 新 release（GitHub 页面 robots 限制，未直取，标注未核）；Browser Harness 最新仍 0.1.10（2026-08-26，piwheels），无新版本。
- **旁证（不改判断、记一笔）**：Playwright MCP 自己的 README 现写明"coding agent 更适合 CLI-as-SKILL，比 MCP 省 token"——**连 MCP 服务方都建议编码 agent 走 CLI**，与判断 2"代码即动作"同向。

## 八、Day3 增量记录（2026-11-25，周三）

- **New · agent-desktop**（A）：Vercel Labs 的桌面 a11y 执行面，npm **1.2.0**（约 5 万下载/周、48 个版本）。核心不是"a11y 一定更好"，而是把不确定性显式化：ref **绑快照 id**（裸 ref 报错）、UI 变了返回 `STALE_REF` / `AMBIGUOUS_TARGET`、错误自带 **`disposition.retry`**、默认 **headless**（`--headed` 才动物理指针）、1.2.0 起 `agent-desktop mcp` 暴露 `desktop_*` 工具、`--stdin` 让密钥不进 argv。官方自警"快照/剪贴板/截图可含隐私"，第三方补一句更关键：**a11y 树暴露面可能大于单窗口截图**。卡见 `[cand]agent-desktop-a11y-desktop-2026-11.md`。
- **New · GUI 回放 / 效果核验品类**（A）：5 个对象合起来给出本周最硬的一条数字——**OpenAdapt 故障注入 90 例，只看屏幕的验证静默接受 54/90；加带外效果校验 9/90；完整 system-of-record 读路径 0/90**（第二域 24/36→3/36）。EchoPath 用 IBTR 重瞄把回放成本打到 token −90% / 时间 −60%；Activity Frames 明确"确定性只对存储后的 OCR 文本向前成立，不回溯像素"。卡见 `[cand]gui-action-replay-effect-verification-2026-11.md`。
- **判断 1 从"设计推断"升级为"受控证据"**：ComponentBench 在同一 harness 上只换表示，GPT-5 mini AX 83.1 → Pixel 48.9（−34.2pt）；但 GPT-5.4 的排序**反过来**（Pixel 83.8 > AX 81.5 > SoM 77.0）——所以不是"结构化一律更好"，而是**表示 × 模型能力 × 场景密度三者交互**：clutter 下 Pixel −14.3%、AX −0.2%，GPT-5.4 在 clutter=none 时 Pixel 领先 4.5%、到 clutter=medium 反转成 AX 领先 9.7%。"选哪种表示"必须先测自己的任务分布与场景密度，不能抄结论。
- **判断 3 获得量化支撑**：OpenAdapt 的 54/90 正是"屏幕成功 ≠ 已写入"的比例化版本；加上 EchoPath 的"拒绝模糊步骤"、agent-desktop 的 `STALE_REF`，三者指向同一件事——**回执要来自执行外部状态，且失败要能"拒绝继续"而不是重试到成功**。
- **Changed · 缺口③ 部分闭环、缺口④ 升级 A-**（见 2.4 表）。
- **No Action / 记日志**：Gemini computer use 上 macOS（11-19，US 英文，AI Plus/Pro/Ultra）——消费级产品铺开，属市场信号不属工程对象，记 B；n8n Nod（11-10，自托管个人 agent，自带沙箱电脑与"发送/支付/删除前询问"）——B，产品级；UI-TARS-desktop 仓库最后 commit 仍 10-09（腾讯云镜像页 11-24 为转载），无新版本。
