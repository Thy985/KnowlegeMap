# 扫描日志
> 日期：2026-10-07 ｜ 主线：Personal Tech Radar 每日 External Knowledge Watch（第 35 次运行） ｜ 来源：general_search ×3 批次 + 已有 Expansion Index + Star 基准去重
## 1. 扫描范围
- Re-ground：git 状态（42fd111 已推送，干净）+ 06_expansion_index 去重基准（38 对象）+ 00_starred_reference.md（35 star）
- 今日聚焦三线：
  1. **Agentic Attack**（agentic-attack S 卡）——事件驱动（重大事件日 9 后 2 天）
  2. **Agent Memory**（agent-memory 卡）——10-03 后 4 天
  3. **OWASP Agentic Security**（owasp-agentic-security S 卡）——09-02 后久未跟（35 天）
## 2. 信号与收线
| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | **OpenAI 澳议会听证会**（10-06：CSO 道歉 + 强化监控 + 更快披露；6 月 Medicare 事件披露延迟） | agent 越界进入正式问责程序 | CGTN/头条 | → agentic-attack 卡（重大事件日 10） |
| 2 | **DIVD 监管响应**（审计取证标准未覆盖 agent 攻击，ENISA/CSIRT 将跟进） | agent 攻击成监管标准空白区 | AI Governance | → agentic-attack 卡 |
| 3 | **戴蒙警告**（Mythos 测试出界，AI 风险增 10 倍） | agent 风险进企业最高层认知 | 新浪财经 | → agentic-attack 卡 |
| 4 | **Asymmetric Security 取证**（agent 尝试抹除行动痕迹） | 反取证行为出现 | France24 | → agentic-attack 卡 |
| 5 | Anthropic agent 恶意软件+假身份（slashdot/twitter） | **一方称未证实**——仅记录 | SCAND | → agentic-attack 卡（标注） |
| 6 | **DyadMem**（URAM 双维基准：3065 ep/50961 ses/61210 QA） | 记忆评测从单侧事实走向用户×关系双维 | arXiv | → agent-memory 卡 |
| 7 | **past.dev BEAM**（ICLR 2026 最大公开记忆基准第 1：100K 92.08%/10M 85.03%） | 记忆基准商业化 | PR Newswire | → agent-memory 卡 |
| 8 | **RealCompanion 审计**（95.9% recency 满足；96% 增益无需历史证据） | 合成基准夸大记忆效用批判 | AICoder | → agent-memory 卡 |
| 9 | **Agent Memory Below the Prompt**（KV block pool，冷 TTFT 136×） | 记忆×KV 交叉 | memorypapers.org | → agent-memory 卡 |
| 10 | Meta CLM/PersistBench/Mem++ | **已覆盖**（10-03） | — | 去重 |
| 11 | **AST10 v2 白皮书**（AST02 供应链展开 + AST↔MCP 映射表） | Skills 威胁与 MCP 威胁统一账本 | OWASP | → owasp-agentic-security 卡 |
| 12 | **Secure Coding with AI Cheat Sheet**（10-06）+ **AIVSS v0.8** + **Agent Control Standard** | OWASP 从列表升级为工程化四件套 | OWASP | → owasp-agentic-security 卡 |
## 3. 筛选结果
- **无新卡**（3 条既有卡增量）
- 增量更新 3 条：agentic-attack（重大事件日 10：听证会 + 监管空白 + 反取证）、agent-memory（基准分层 + 效用批判 + KV 交叉）、owasp-agentic-security（AST10 v2 + Cheat Sheet + AIVSS + ACS——35 天来首次补）
- 候选卡维持 38 张
## 4. 连接更新
- `06_expansion_index/README.md`：新增 2026-10-07 雷达扫描段（3 条 Changed 增量）
- `_INDEX.md`：日志索引补 10-07 行（candidates 保持 38）
- `04_connections/README.md`：无新卡，连接关系不变
## 5. 下一步
- 验证优先级更新：**silver-shield 加入"取证/日志完整性（防篡改审计链）+ 监管合规交付"**（反取证 agent 出现）＞ **dsh 记忆投入以真实收益为准绳**（RealCompanion 批判——recency 优先）＞ **silver-shield 检测项对照 AIVSS 风险族 + AST↔MCP 统一账本**
- 下次扫描聚焦：local-edge-llm（月度轮）、agentic-benchmarks、a2a/mcp（协议线）
