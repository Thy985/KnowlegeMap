# 2026-11-23 Personal Tech Radar 深耕扫描（Computer Use / Browser 第一周 Day1）

- 领域：Computer Use / Browser（周起始 11-23）｜当日分工：**周一 = 建能力树/基线**
- 产出：`08_agent_centric/domains/agent-computer-use.md`（新建，八层 A~H / 44 节点）

## 扫描动作
1. 读 `07_radar_watch/README.md` + `current_focus.md`（确认领域与七条待办）
2. 读三张在队卡（computer-browser-use / browser-harness / webwright）+ 06 index 去重
3. 定向 6 次检索：OSWorld/WebArena 现状、browser-use release、Playwright MCP 表示路线、CUA 安全研究、OSWorld 2.0
4. 去重：OSWorld / BioShocking / Invisible Ink / II-Bench / WebTrap / CaMeLs 在 06 index、候选卡、08 领域树中**均 0 命中**（首次入账）

## 关键事实（新增）
- **browser-use 1.0 推翻重写**（1.0.0 11-10、1.0.6 11-16）：持久 Python REPL 直连 CDP，"no DOM serializer, no action schema"；同模型自报 +33 分 / 便宜 2.7–5.2x / 快 2–3x；默认云浏览器 + 网关 key；`max_steps=100`/`timeout=1700s`；1.0.5 增逐次 judge（含 `prompt_injection_detected` / `bot_block_or_captcha_detected`）。
- **OSWorld 2.0**（2606.29537）：108 长时任务、人工中位 1.6h、平均 318 次调用（1.0 约 30）；Opus 4.8 二值 20.6% / 部分 54.8%；失败画像＝丢约束 / 漏中途信息 / 猜而不问 / 跳过验证。
- **基准口径分裂**：OSWorld-Verified 人类 72.36%（前沿 82–86%）vs WebArena 58.1% vs WebVoyager 自报 89–94% vs OSWorld 2.0 20.6%——测的不是同一件事；同模型 verified 与自报差 6–11pt。
- **安全基线**：CSA（弹窗 ASR 86%、任务 −47%、隐藏通道、planner-executor 分离）；BioShocking（6/6 agentic 浏览器被虚构框架击穿，Anthropic 修复仍可绕过）；UW（同源策略差异 + 记忆跨 origin 混流）；Invisible Ink（低害目标与人机确认不可区分）；WebTrap（中途劫持后回归原任务）。

## 判定与处置
- 建树：八层 A~H（含 A1.1/A2.1/A2.2/A3.1/A3.2/B2.1/B2.2/C2.1–C2.3 六个密切分）
- 锚点 12 行；基准批判 5 条；判断 7 条；缺口 6 项（① S 本地控制面裸露 / ② A 回执可核验 / ③ A 表示覆盖率 / ④⑤⑥ B）
- browser-use 1.0 作为**对象级 Changed** 并入既有 S 卡（不新建卡）
- OSWorld 2.0 / 安全研究记 baseline，不建碎片卡（域内且为基线材料）
- 未做：任何实跑（本机无 GUI），缺口①②③ 排周五

## 结论
**Changed**：browser-use 从"action schema + DOM serializer"退到"REPL + CDP"，与 Webwright 独立收敛 → "代码即动作"是本周第一个方向判断。
**New**：Computer Use / Browser 周能力树基线建立。
