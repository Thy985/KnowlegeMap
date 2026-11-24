# 2026-11-25 Personal Tech Radar 深耕扫描（Computer Use / Browser 第一周 Day3）

- 今日分工：周三＝只追增量（desktop CUA / a11y vs 像素 grounding / 动作重放与确定性）。
- 检索：general_search 4 组 + web_fetch 2 次（ComponentBench 正文、npm agent-desktop README；GitHub 仓库被 robots 拒，未直取）。
- 去重：`grep -a` 关键词 UI-TARS / ScreenSpot / grounding / 回放 / determinis / agent-desktop / OpenAdapt / EchoPath。

## 发现与判定

| 对象 | 判定 | 处置 |
|---|---|---|
| **agent-desktop**（Vercel Labs，npm 1.2.0） | **New（A）** | 新建 `[cand]agent-desktop-a11y-desktop-2026-11.md` |
| **GUI 回放 / 效果核验族**（OpenAdapt / EchoPath / Activity Frames / AgentRR / agrepl） | **New（A，品类）** | 新建 `[cand]gui-action-replay-effect-verification-2026-11.md` |
| **ComponentBench**（arXiv 2608.18307） | **A 级评测证据（不建卡）** | 进能力树 2.1 锚点；缺口③ 部分闭环 |
| Gemini computer use on macOS（11-19） | B（消费级产品铺开，市场信号） | 记日志 |
| n8n Nod（11-10） | B（自托管个人 agent，产品级） | 记日志 |
| UI-TARS-desktop 新版本 | 无（仓库最后 commit 10-09；腾讯云 11-24 页为转载） | 不写 |
| browser-use / Playwright MCP / Webwright / Browser Harness | 无 11-24/25 新 release | 不写 |

## 关键一手事实

**agent-desktop（npm README 1.2.0）**
- ref 形如 `@s8f3k2p9:e8`，携带快照 id；裸 `@e8` → `INVALID_ARGS`；UI 变化 → `STALE_REF` / `AMBIGUOUS_TARGET`。
- 错误 envelope 含 `error.disposition.retry`；只在 `safe` 时重试。
- 默认 headless（不动指针/焦点），`--headed` 才物理输入；60 命令名 / 56 可用，`key-down`/`key-up`/`mouse-down`/`mouse-up` 需 daemon 能释放按住键。
- `agent-desktop mcp`（1.2.0）把每条命令暴露为 `desktop_*` stdio 工具；`--stdin` 让密钥不进 argv。
- 平台：macOS 13+ AX / Windows 10 1809+ UIA / Linux Ubuntu 24.04+ AT-SPI；npm 写 X11 或 Wayland，第三方写 Linux 鼠标/窗口控制依赖 X11——**冲突待核**。
- 隐私：官方明示 snapshot/clipboard/截图/debug 产物可能含隐私内容；第三方补"a11y 树暴露面可能大于单窗口截图"。
- 体量：48 版本、约 5.0 万下载/周；1.2.0 的 npm last publish 约 11-20，第三方 changelog 记 11-05——**日期不一致待核**。

**ComponentBench（24 项表 1 / 表 2 / 表 15）**
- GPT-5 mini：AX 83.1 / SoM 78.5 / Pixel 48.9 / Browser-Use 87.0（−34.2pt 同 harness 同任务）。
- GPT-5.4：Pixel 83.8 > AX 81.5 > SoM 77.0（强模型上结构化辅助反损）；GPT-5.4 mini：Pixel 77.1 > AX 79.1 > SoM 74.7。
- clutter：Pixel −14.3% / AX −0.2%；紧凑间距 Pixel −13.6% / AX −4.5%。GPT-5.4 在 clutter=none 时 Pixel 领先 AX 4.5%，clutter=medium 时反转 AX 领先 9.7%。
- 任务级：123 任务 AX 稳过 Pixel 稳挂，反向 52。Drag/Drop：AX 72.1 / Pixel 57.4 / SoM 31.8 / BU 29.7。
- 稳定性：聚合跑间 ≤1.4pt，但 GPT-5 mini Pixel 两轮同为 52.5% 而 17.3% 任务翻转。
- 效率：BU 95.2 pass 但仅 56.1% 在人类步数内；AX/SoM 中位步数比 1.0×。

**回放族**
- OpenAdapt：screen-only 静默接受 54/90；带外 effect check 9/90；完整 SoR 0/90；第二域 24/36→3/36。
- EchoPath：token −90% / 时间 −60%（中位）；重放拒绝模糊步骤 → 有界修复或重新规划。
- Activity Frames：一天捕获 → 86× 小、68ms；问答 98.4% vs LLM 摘要 66–80%；确定性只对存储 OCR 文本向前，不回溯像素。
- agrepl：MITM 全外部交互重放，F=1.0，每步 −98.3%，零出网；不含 UI 状态。

## 未做
- 未实跑任何桌面动作（本机无 GUI）；agent-desktop 未做包级核对（排周五/周六）。
- ComponentBench 未跑；OpenAdapt 为 draft，未独立复现。
