# 扫描日志
> 日期：2026-09-19 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 18 次运行） ｜ 来源：general_search ×3 批次 + 已有 Expansion Index 去重
## 1. 扫描范围
- Re-ground：git 状态（9aa2eea 已推送，干净）+ 06_expansion_index/README.md 去重基准（36 对象）
- 今日聚焦（事件驱动 + 未跟进领域）：
  1. **Agent 安全新事件**（agentic-attack S 卡）——09-17 大事件日后 2 天
  2. **Agentic 基准/Eval**（agentic-benchmarks A 卡）——09-14 后首次跟进
  3. **Edge/本地 LLM**（local-edge-llm A 卡，Tafcm 直接相关）——09-13 后首次跟进
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **Hugging Face 官方技术时间线（09-17）**：Stage 1 eval 沙箱→rooted launchpad、Stage 2 两 injection vectors | 一手权威复盘（此前二手） | huggingsface.co 官方博客 | → agentic-attack 卡增量（重大事件日 3） |
| 2 | **Hacktron 三人组 + Claude 攻进 OpenAI Monorepo（09-17 WSJ）** | 攻防不对称压缩到"人力规模级" | 华尔街见闻转引 WSJ | → agentic-attack 卡增量 |
| 3 | **Plugin4Shell 零点击 RCE（09-18）** + **BragJack 浏览器 agent 劫持（09-17）** | 插件/扩展供应链=零点击入口 | cybersecuritynews / gridthegrey | → agentic-attack 卡增量 |
| 4 | 西班牙首例自主 AI agent 数据泄露 + **Anthropic Glasswing**（自主找 FFmpeg 16 年漏洞） | 监管首例 + 攻防双刃剑 | gridthegrey / anthropic.com | → agentic-attack 卡增量 |
| 5 | **Sierra Hyper-τ-Bench（09-08）** + **GitTaskBench（09-13）** + **MTAC-IFBench（09-14）** | "agent 建 agent"+多轮约束保持新评测维度 | bobweb / ai-damn / arXiv | → agentic-benchmarks 卡增量 |
| 6 | **AA Coding Agent Index v1.5（09-18）**：TB4.0/DeepSWE v1.1 | 权威榜单口径持续收紧 | artificialanalysis | → agentic-benchmarks 卡增量 |
| 7 | **MiniCPM-V 4.6**（官方 iOS/Android/HarmonyOS）+ **Gemma 4 E2B/E4B** + LFM2.5-2.6B + **Desert Ant 18 模型** + **PrismML 三元权重** | 端侧从文本 SLM 扩到多模态全家桶 | evermx / Google / mer.vin | → local-edge-llm 卡增量 |
| 8 | MiniCPM5-2B / Falcon-Edge / Edge0 / GLM-5.3-Flash / Qwen3.8 | **已覆盖**（09-11/09-13 轮） | — | 去重 |
## 3. 筛选结果
- 无 S/A/B 级新对象需建卡（全部落入已有 S/A/B 卡增量）
- 增量更新 3 条（不新建卡）：agentic-attack（重大事件日 3，6 事件）、agentic-benchmarks（4 对象）、local-edge-llm（5 对象）
- 无新范式丢弃：RuBench（俄语仓库基准）、Kotlin Benchmark（JetBrains 语言专用）、Next.js evals（厂商自营，参考价值低）
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-09-19 雷达扫描段（0 新对象 + 3 条 Changed 增量）
- `04_connections/README.md`：无新连接对象，连接地图保持 36 行
- `_INDEX.md`：candidates 保持 36 张，日志索引补 09-19
## 5. 下一步
- 验证优先级更新：**campus_order OpenClaw 升级评估** ＞ **Plugin4Shell/BragJack 对 dsh/TeamMind 插件加载的威胁建模**（新零点击入口）＞ Tafcm 端侧多模态选型（Gemma 4 E2B/E4B 官方链优先）
- 下次扫描聚焦：computer use 新变化、eval 新基准、OpenClaw 生态
