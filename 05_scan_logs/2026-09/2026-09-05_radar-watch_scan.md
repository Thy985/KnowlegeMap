# 扫描日志
> 日期：2026-09-05 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 4 次运行） ｜ 来源：general_search ×6 批次 + 已有 Expansion Index 去重
## 1. 扫描范围
- Re-ground：07_radar_watch/README.md、06_expansion_index/README.md（25 对象去重基准）
- 今日聚焦（按雷达规范"按当天聚焦、不全量"）：
  1. **G2 RAG 系统化**（Agentic GraphRAG / 记忆增强检索——KB 仅 1 篇的最薄弱缺口）
  2. **MCP / Agent 互操作增量**（已知对象，查新 Release）
  3. **Agent 供应链安全**（G1 相邻新前线：skill/插件/依赖攻击，与 EP-002 直接相关）
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **SkillFortify（arXiv 2603.00195，形式化 skill 供应链验证）** | 首个"静态分析保证"（DY-Skill 模型 + 五定理）而非启发式扫描，540-skill benchmark F1 96.95% | arXiv / SkillFortifyBench | → 新建 [cand]skill-supply-chain-security-2026.md（S） |
| 2 | **Unit 42 BIV（49943 个 OpenClaw skill 审计，80% 偏离声明、5% 恶意）** | 技能层供应链实证失守，直接对应 OWASP ASI04；ClawHub 已 takedown | unit42.paloaltonetworks.com | → 并入供应链安全卡（S） |
| 3 | MalSkills（神经符号恶意 skill 检测）/ SkillSafetyBench / Agent Skill Security 威胁模型 | 同线工具与分类学，生态完整 | arXiv | → 并入供应链安全卡 |
| 4 | **MemGraphRAG（KDD'26，三层记忆 + 多 Agent 图构建）** | 记忆×图×多 Agent 合流，直接命中 RAG 缺口 + GrowthOS 可接 | GitHub / arXiv 2606.00610 | → 新建 [cand]agentic-graphrag-2026.md（A） |
| 5 | Graph-R1（端到端 RL agentic GraphRAG，F1 57.82 vs 32.05）+ A-RAG（分层检索接口） | RAG 走向 agent 主动遍历的收敛证据 | OpenReview / arXiv | → 并入 GraphRAG 卡 |
| 6 | MCP 2026-07-28 stateless + SDK 落地（rust 3.0 beta / C# v2 / go v1.7 / Cloudflare 采用） | 已知对象，仅 SDK 执行确认无新范式 | MCP 官方博客 | → 无动作（已在 09-01/09-02 覆盖） |
| 7 | Slopsquatting（幻觉包名供应链武器）+ WorkOS MCP 供应链清单固定 | 供应链攻击新模式与防御实践 | Codex KB / WorkOS | → 并入供应链安全卡（防御侧） |
## 3. 筛选结果
- 进入 candidates（新 2 张）：`[cand]skill-supply-chain-security-2026`（**S**）｜ `[cand]agentic-graphrag-2026`（A）
- 增量更新：无（MCP 已覆盖；OWASP ASI04 已在其卡内）
- 与主线无关/已覆盖丢弃：MCP SDK 落地确认、GraphRAG 企业案例二手报告
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-09-05 雷达扫描段（2 新对象）
- `04_connections/README.md`：新增 2 行连接卡（Skill 供应链安全、Agentic GraphRAG），共 25 → 27 行
- `_INDEX.md`：candidates 25 → 27 张，S 级/A 级更新
## 5. 下一步
- 验证优先级：SkillFortify（S，对 Claude Code skills 跑能力验证，直接进 dsh-pentest）＞ MemGraphRAG（A，小语料多跳问答对照）
- 下次扫描聚焦：AI 安全工具实测（RAMPART/SkillFortify 落地）、Agentic CLEAR 实证、DeepSeek Harness 新版本
