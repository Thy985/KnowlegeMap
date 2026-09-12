# 扫描日志
> 日期：2026-09-13 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 12 次运行） ｜ 来源：general_search ×3 批次 + 已有 Expansion Index 去重
## 1. 扫描范围
- Re-ground：git 状态（cc91341 已推送，干净）+ 06_expansion_index/README.md 去重基准（36 对象）
- 今日聚焦（按雷达规范"按当天聚焦、不全量"）：
  1. **Agent Memory / Context Engineering 新进展**（agent-memory S 卡 Changed 检测）
  2. **Agent Harness / Coding Agent 新动态**（TeamMind/agent-attention 相关）
  3. **本地/边缘 LLM 新路线**（Tafcm 直接相关）
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **Mem0 新算法架构细节确认**：两遍 extraction（extract→diff→ADD/UPDATE/DELETE）→ 单遍 ADD-only，**移除图存储**；Pi Agent Plugin v0.3.0 + Strands 集成 | S 级卡核心对象架构变化确认（向量+关系简化路线） | Habr / GitHub releases | → agent-memory 卡增量（Changed） |
| 2 | **Letta Trajectory（2026-07）**：把 Claude Code/Codex/Letta Code 会话规范化为 token 高效标准格式供 agent 学习 | 与 09-12 trace-based eval 卡同属"行为数据标准化"范式，面向学习/复用 | Letta Research | → agent-memory 卡增量（Changed） |
| 3 | **OpenCode v1.18.28-30（09-04/09-09）**：GPT-6 Astra/Copilot session ID；**Cline SDK**（runtime 化重构 + headless，67.9k★） | coding agent "runtime 化"共同演进方向 | opencode.ai changelog / Cline | → opencode 卡增量（Changed，小） |
| 4 | **Edge0-35B-A3B（09-12）**：35B MoE <3GiB 内存磁盘流式运行；**Falcon-Edge**（1.58-bit 三元）；Qwen3.8-Flash-Next 手机 CPU | 边缘 LLM 进入"磁盘流式 MoE + 超低位量化"新路线 | MindStudio / TII 报道 | → local-edge-llm 卡增量（Changed） |
| 5 | agentmemory（hansonkim）/ agents-memory（Lolaplex） | 编码 agent 记忆新项目，同线观察级 | GitHub | → 并入 agent-memory 增量 |
| 6 | ECC（Everything Claude Code）2.0 / 各 fork | Claude Code 配置/插件管理类项目，"Harness OS"概念与 control-plane 同线但价值中等 | GitHub | 观察级，不写卡 |
## 3. 筛选结果
- 今日无 S/A/B 级新对象需建卡（增量消化日：连续两日安全侧大发现后收敛）
- 增量更新 3 条（不新建卡）：agent-memory（Mem0 架构/Letta trajectory/编码 agent 记忆新项目）、opencode（v1.18.28-30 + Cline SDK 竞品）、local-edge-llm（Edge0/Falcon-Edge/Qwen3.8-Flash-Next 手机 CPU）
- 无新范式丢弃：Cline SDK 发布信息（05 月新闻，仅记录竞品动态）、腾讯混元 1bit 量化（07 月旧闻）、Edge inference cookbook（教程级）
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-09-13 雷达扫描段（0 新对象 + 3 条 Changed 增量）
- `04_connections/README.md`：无新连接对象（均为已有卡增量），连接地图保持 36 行
- `_INDEX.md`：candidates 保持 36 张，日志索引补 09-13
## 5. 下一步
- 验证优先级：Aigis/Guardian/AI Protector 三选一实测（防火墙品类）＞ agentevals 本地跑样本 trace（trace-based eval）＞ Edge0-35B 磁盘流式 MoE 可用性核验（Tafcm 混合架构）
- 下次扫描聚焦：RAMPART 实测进度、SkillFortify 本机验证、dsh-pentest 对防火墙品类攻击测试
