# 05 · 未来自动探索策略

> 生成时间：2026-09-01（Bootstrap 第五阶段产物）。
> 目标：让本仓库成为未来 3 个月持续运转的 **External Knowledge Expansion Layer**——有节奏、有证据、不贪多。

---

## 1. 探索节奏

| 周期 | 动作 | 产物 |
|---|---|---|
| **每周** | 1 次定向扫描（按当周主线选 1 个 S/A 档方向） | `05_scan_logs/` 新增扫描日志 |
| **每两周** | 从 inbox 筛选 → 生成候选卡（进入 candidates） | 1–3 张候选证据卡 |
| **每月** | 月度评审：validated 中已充分验证的对象 → 晋升内库；清点覆盖变化 | 更新 Known Territory + Connections |
| **每季度** | 重跑一次 Top 20 评分（权重不变，更新活跃度/影响） | 更新 04_top20_expansion.md |

> 每次扫描上限：**收 5–8 条原始线索 → 筛选到 1–3 个候选 → 0–1 个进入 validated**。宁可少而精。

## 2. 信息源清单（按主线）

### 协议与标准线（MCP/Evals/Agent 安全）
- MCP 官方 Spec 与 registry（modelcontextprotocol.io）
- OpenAI / Anthropic / Google 官方博客与 Release Notes
- arXiv：cs.AI、cs.SE、cs.CR、cs.LG
- OWASP Agentic Security / Top 10 for LLM Applications

### 安全与攻防线
- AI Safety 机构（AISI、Anthropic Safety、OpenAI Preparedness）
- 攻防社区（HackTheBox AI、LLM 安全论坛、对抗样本综述）
- 安全工具 Release（Vulnhuntr、prompt injection 防御库）

### 验证与评测线
- 评测框架 Release（promptfoo / DeepEval / LangSmith / OpenAI Evals）
- 新基准发布（SWE-bench 更新、GAIA、MLE-bench、AgentBench）
- 可观测性标准（OpenTelemetry GenAI semantic conventions）

### 通用
- GitHub Trending（按语言/话题：agent、mcp、ai-security）
- Hacker News / Reddit r/LocalLLaMA（信号，非事实源）
- Product Hunt 的 AI 开发工具类

## 3. 流水线：inbox → candidates → validated

```
信号捕捉（周扫描）
   ↓
inbox/        原始线索（URL + 一句话"为什么值得看"）
   ↓ 筛选：① 是否重复已知领域？→ 丢弃  ② 是否与主线/项目相关？→ 保留
   ↓ ③ 证据是否可获取（官方文档/源码/论文/Release）？
candidates/   候选证据卡（candidate_card.md：What/Why/Evidence/Connection/Verification plan）
   ↓ 实际验证（跑通 demo / 精读源码 / 对照实验）
validated/    已验证对象（进入 04_connections 连接图 → 晋升飞书内库）
```

## 4. 证据标准（沿用内库 FACT/DESIGN 纪律）

- **FACT**：官方文档、GitHub 源码、Release、arXiv 论文、实测结果。
- **DESIGN**：博客观点、社区讨论、趋势判断——只作为"待验证假设"，不当作事实。
- 每条候选卡必须回答 4 个问题：*它解决什么问题？为什么现在值得关注？与我哪个项目/知识连接？我怎么验证它？*
- **禁止**：只看 README 就推荐；只凭 star 数下结论；重复收集已知领域基础资料。

## 5. 与内库的晋升协议

| 触发条件 | 动作 | 落点 |
|---|---|---|
| 候选对象完成一次真实验证（跑通/精读） | 写入 `04_connections/` 连接卡 | 仓库层 |
| 同一对象积累 ≥2 条独立验证证据 | 晋升飞书内库对应空间 | 内库层 |
| 形成跨项目稳定结论 | 提议成为 Engineering Principle（走内库 EP 流程） | 原则层 |
| 仅"听说过/看人推荐" | 留在 inbox，不升级 | 仓库层 |

## 6. 反模式（避免）

1. **重复已知**：MCP 已确认后，不再收集"什么是 MCP"的基础资料，只追新进展。
2. **数量幻觉**：单次扫描不追求"收了很多"。
3. **无证据推荐**：不看一手源就写进 candidates。
4. **越权入内库**：未经验证不写进飞书正式知识体系（遵守用户"探索≠定结构"原则）。
5. **脱离项目**：收了一堆与本仓库项目、知识体系都无关的方向。

## 7. 首轮扫描计划（下次执行）

> 按用户指令，**Bootstrap 本次不做大规模扩展**。首轮扫描建议从以下 2 个 S 档方向切入：

1. **MCP 生态**：读 MCP 最新 Spec → 盘点 registry 中与"通知/文档/记忆"相关的 server → 评估给 agent-attention 加 MCP 支持的可行性。
2. **Agent Evals**：对比 promptfoo / DeepEval / OpenAI Evals 的最小可用路径 → 用 Tafcm 的 ADI 或 silver-shield 的 benchmark 做一次小规模试跑。

每轮扫描后按 `99_templates/scan_log.md` 记录，并更新 `03_expansion_queue/` 状态。
