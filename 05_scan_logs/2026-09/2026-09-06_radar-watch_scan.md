# 扫描日志
> 日期：2026-09-06 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 5 次运行） ｜ 来源：general_search ×3 批次 + 已有 Expansion Index 去重
## 1. 扫描范围
- Re-ground：07_radar_watch/README.md、06_expansion_index/README.md（27 对象去重基准）、00_bootstrap 技术地图/缺口地图
- 今日聚焦（按雷达规范"按当天聚焦、不全量"）：
  1. **G1 AI 安全新增量**（agent 安全工具/事件，区别于已覆盖的 OWASP/RAMPART/PI-Hunter/SkillFortify）
  2. **重点开源项目新 Release**（OpenClaw / hermes-agent / browser-use）
  3. **G2 空白区：AI 原生产品 / Agentic UX**
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **OpenClaw 2.0（v2026.8.1，2026-08-31，史上最大更新）** | 933 贡献者/16k+ PR：简化安装 + 重建浏览器 App + multiplayer sessions + 新安全控制；社区对比"用户转投 Hermes" | InfoQ / 36kr / Aetos.AI | → hermes-agent 卡增量（Changed） |
| 2 | **NVIDIA SkillSpector**（agent skills 扫描器，Claude Code/Codex/MCP） | 与 SkillFortify 互补的启发式生态扫描工具 | GitHub topics/agent-security | → 供应链安全卡增量（Changed） |
| 3 | **CHAINDROP（2026-08-04）** | 后门 400+ npm 包（13 亿月下载）、4h 内 2,212 恶意版本——供应链攻击规模化 | vibe-eval.com | → 供应链安全卡增量（Changed） |
| 4 | **Tenable AI Inspector（09-05）+ AI Agent Firewall 品类** | 商业工具进入 agent 供应链验证；LLM 防火墙范式批判（stateless 不适配 agent） | aitools / forkast / habr | → 供应链安全卡增量（Changed） |
| 5 | **Agent Threat Rules（ATR）+《The Collapse of Trust》** | 开源 agent 威胁规则库，数据流点×攻击类×真实事件映射 | GitHub ATR-Paper | → 攻防工具链卡增量（Changed） |
| 6 | **OpenAI 智能体劫持德国网站事件（09-04 新华社）** | 多 agent 互操作即攻击面的实证事件 | 新京报/新华社 | → 攻防工具链卡增量（Changed） |
| 7 | **Agentic UX 设计模式体系（Agentic Design / AI UX Playground 五级自主度 / Smashing 六模式 / zylos 四层栈）** | G2"AI 原生产品"空白区 2026 已成型，与 TeamMind/campus_order 产品化直接相关 | agentic-design.ai / aiuxplayground / smashingmagazine / zylos | → **新建 [cand]agentic-ux-2026.md（B）** |
| 8 | awesome-agent-skills-security 清单 | 快速索引，价值并入攻防卡 | GitHub | → 并入攻防卡增量 |
## 3. 筛选结果
- 进入 candidates（新 1 张）：`[cand]agentic-ux-2026`（B）
- 增量更新（不新建卡，3 条）：hermes-agent（OpenClaw 2.0 竞争格局）｜ skill-supply-chain-security（SkillSpector/CHAINDROP/Tenable/Firewall 品类）｜ ai-offensive-toolchain（ATR/OpenAI 劫持事件/awesome 清单）
- 无新范式丢弃：browser-use 无独立新变化信号（已并入 browser-harness 卡覆盖）
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-09-06 雷达扫描段（1 新对象 + 3 条 Changed 增量）
- `04_connections/README.md`：新增 1 行连接卡（Agentic UX），共 27 → 28 行
- `_INDEX.md`：candidates 27 → 28 张，B 级 5 → 6，连接地图 27 → 28 行，日志索引补 09-06
## 5. 下一步
- 验证优先级：OpenClaw 2.0（campus_order 直接相关，实测对照）＞ SkillSpector vs SkillFortify 对比验证 ＞ Agentic UX 模式清单产出
- 下次扫描聚焦：OpenClaw 2.0 生态实测、Agentic CLEAR 实证进度、DeepSeek Harness 新版本
