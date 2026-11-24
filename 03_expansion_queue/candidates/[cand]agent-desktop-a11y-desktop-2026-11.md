# 候选对象证据卡

> 状态：`[cand]` ｜ 关联方向：Computer Use / Browser（A 表示层 / B 动作空间 / C 自验证） ｜ 日期：2026-11-25

## 一句话定位
Vercel Labs 的 `agent-desktop` 把桌面 computer use 的表示固定为**操作系统无障碍树 + 带快照 id 的 ref**，并把"这次失败能不能重试"写成命令契约（`STALE_REF` / `AMBIGUOUS_TARGET` / `disposition.retry`）——首个把"动作回执"做成结构化错误而非布尔成功的通用桌面执行面。

## 1. 它解决什么问题
桌面自动化此前只有两条路：截图 + 视觉模型猜坐标（分辨率/DPI/主题一变就漂，且整屏外发），或 app-specific RPA（选择器一改就碎）。`agent-desktop` 选了第三条：让 agent 读 OS 自己的结构化 UI（macOS AX / Windows UIA / Linux AT-SPI），返回 JSON 树，每个可操作元素带 `ref`；动作按 `ref` 而不是坐标，做完再 `snapshot` 一次核对。它自己**不含模型**——只是一个 CLI + C 库（Rust），循环留在 agent 里，因此可接 Claude Code / Codex / 任意能跑 shell 的 agent。

真正有工程价值的不是"a11y 比像素好"，而是三处把不确定性显式化：
1. **ref 绑定快照身份**：`@s8f3k2p9:e8` 里的 `s8f3k2p9` 是快照 id，裸 `@e8` 直接 `INVALID_ARGS`。UI 变了则返回 `STALE_REF` 或 `AMBIGUOUS_TARGET`——"目标已失效"是明确状态，而不是静默点到隔壁按钮。
2. **重试安全性是数据不是建议**：错误里带 `disposition.retry`（`safe` / 非 safe），agent 只在 safe 时重试。这直接对上 Memory 周"回执可核验"的判据：**不重试到成功为止，而是先判断这次失败是否可重放**。
3. **headless 默认**：默认不动真实指针、不改焦点，`--headed` 才走物理输入；多 agent 时各自有 overlay 光标（第三方描述），需要单一物理指针的动作串行。这让"多个 agent 并行用一台机器"从概念变成有明确争用规则的设计。

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **版本与体量**：npm `agent-desktop` **1.2.0**（页面显示 last publish 约 11-20，48 个版本；第三方 changelog 记 1.2.0 为 11-05——**两处时间不一致，标待核**），周下载约 **5.0 万**；10-28 发 1.0（加 Linux）、10-30 发 1.0.2、11-03 发 1.1.0（Windows overlay 与文本输入修复）；11-03 时第三方记 11.6k stars。Apache-2.0。
- **命令面**：60 个命令名，**56 个可用**；`key-down` / `key-up` / `mouse-down` / `mouse-up` 四个**在 daemon 能释放被按住键之前拒绝执行**（这是对"agent 中途崩了但键还按着"的显式处理）。分组覆盖 observe / act-on-ref / 键鼠 / 应用与窗口 / 通知 / 剪贴板 / wait / 会话 / trace / cursor-overlay。
- **MCP 面（1.2.0）**：`agent-desktop mcp` 以 stdio 把每条命令暴露为工具（`desktop_snapshot` / `desktop_click` / `desktop_session_start`），返回同一 JSON envelope；`--session` / `--headed` / `--trace` 对全部调用生效。
- **凭据卫生**：`type` / `set-value` / `clipboard-set` 支持 `--stdin`，让密钥不进 argv（README 明确"batch JSON text 会出现在进程参数里"，要求 secret 步骤单独走 stdin）。
- **平台**：macOS 13+（AX API）、Windows 10 1809+（UIA）、Linux Ubuntu 24.04+（AT-SPI）。npm 页写 X11 **或 Wayland**，第三方文章写"Linux 鼠标与窗口控制依赖 X11"——**冲突待核**。
- **官方自警（重要）**：snapshot、剪贴板读取、截图、命令输出、debug 产物都可能含隐私桌面内容，要求不要进公共日志/上传；第三方评论补了一句更关键的：**a11y 树暴露的可能比单窗口截图更多**——它不是"更安全的表示"，只是"不同形状的暴露"。

## 3. 与我的连接
- **E2E-CLI**：桌面 E2E 的产物应是"脚本 + 外部断言"，而 `ref` 携带快照 id 给了断言一个新锚点——断言可以绑到"某一版 UI 快照"而不是"某个像素位置"；`STALE_REF` 可以直接映射为 H4 失败类（目标失效），不必靠截图 diff 猜。
- **Tafcm**：本地桌面场景下，a11y 路径能保持"零像素外发"，同时 CLI 无模型、不驻留服务；但 macOS 需要 Accessibility 授权、Linux 需要 AT-SPI 会话——这与判断 7"隔离最小单位是 profile/会话"同构：**授权范围就是权限范围**。
- **silver-shield**：新增两个检测/暴露面——① a11y 快照是明文结构化数据，含窗口标题、控件名、剪贴板内容，比截图更易被日志化；② `agent-desktop mcp` 又是一个本地 stdio 工具面（与 Windows-MCP 的 HTTP 无认证不同，stdio 不可远程直连，但会被任何能起进程的 agent 继承）。
- **能力树**：A2（结构化表示的具体形态）、A6（覆盖率与漏检）、B1（ref grounding vs 坐标）、C2（读回核对 vs 声明成功）、D3（会话/trace/cursor overlay 的并发争用）、G（`--headed` 与确认点的物理边界）。

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | npm `agent-desktop` README（1.2.0，含 JSON envelope、ref 规则、错误码、命令表、MCP 配置、平台表）；GitHub `vercel-labs/agent-desktop`（**直接抓取被 robots.txt 拒，未直取**）；第三方：indiekings 11-03（1.1.0 / 60 命令 / retry 规则 / 隐私提示）、shiftdelete 11-01（1.0 Linux / per-agent cursor / headless）、dev.to 11-07（1.2.0 changelog 与 MCP） |
| 证据等级 | **FACT**（npm 一手 README）；per-agent cursor、11.6k stars、1.2.0 日期为**二手/待核** |
| 验证方式 | 本机无 GUI，只做**包级 + 文档级**：`npm view agent-desktop versions` 核对版本线；`npm pack` 后检查是否携带 native 二进制与 skills 文档；读取 `skills get desktop` 的 retry/ref 语义；核对 `mcp` 工具命名与 `--stdin` 行为。**不做真机点击**（无桌面会话） |
| 预期完成时间 | 周五（11-27）验证日或周六回灌，视 browser-use/Playwright MCP 两项进度 |

## 5. 验证结果
<!-- 待回填 -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察（A 级；桌面 a11y 路线的代表实现，等包级核对后再定）
- [ ] 拒绝（原因）
