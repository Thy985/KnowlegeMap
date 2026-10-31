# Personal Tech Radar 通用兜底扫描日志 · 2026-11-01

> 轻量全领域安全网。当前深耕领域：Runtime（延长第二周）。本次只收录领域外 S/A 级重大对象。

## 扫描结果

### 建卡（A 级，领域外，2 张）
1. **Wiz Black October**（`[cand]wiz-black-october-ai-platform-keys-2026-10.md`）
   - 10-30 Wiz 研究发布：2026 年 10 月至少 **9 个 AI 开发平台遭入侵**，共同主线=攻击者针对存储的环境变量（AI 模型密钥）；窃取密钥约 **30 分钟内被测试并转售**（凭证市场成熟化）。
   - LLMJacking 规模化：单案 **13 小时 170 万次 Amazon Bedrock 调用、超 10 万美元欺诈费用**。
   - 与 LiteLLM 供应链投毒（10-21/22，已建卡）同月共振，构成「AI 凭证安全」系统性图景。
   - 一手来源：Wiz 研究（经 dev.to 转载片段核验，一手报告待 verbatim 核验）；维持观察。

2. **OpenAI DevDay 2026 / Agents API public beta / Dots**（`[cand]openai-devday-agents-api-dots-2026-10.md`）
   - 9-29 DevDay：GPT-6.1 Sol（1/5 价格）、**Agents API public beta**（hosted execution+memory+tools+multi-agent+computer use）、**Dots always-on 个人 agent**（独立云电脑 7×24 运行）、**Decisions API**（Luna，limited preview）。
   - Agent 平台重大路线变更——「持续 agent」产品化拐点，托管执行成为主流交付形态；与 Runtime 周 durable 品类对照（平台托管 vs 自建）。
   - 一手来源：OpenAI 开发者社区 DevDay 公告（10-02，片段核验）+ release notes；维持观察。

### 去重/不写
- MCP 2026-07-28 spec / A2A v1.0 / IBM ADR-048 → 旧闻已覆盖
- Google ADK 2.11 × OpenAI Agents SDK 0.23（10-01）→ 普通 release（cancellation/approvals/redaction），兜底不追
- GPT-6.1 Terra（10-27）→ 模型发布，非 agent 工程对象
- Anthropic × Google/Broadcom 算力合作 → AI Infra 非 agent 实践
- Swarmcha.se 高德 3.5 万次访问事件（10-14 披露）→ 单云 agent 失控+密钥泄露运营事故，**B 级**，不建卡

## 后续
- 两张 A 卡维持观察，验证计划可顺延（Wiz 与 LiteLLM 卡验证并轨；OpenAI DevDay 与 Runtime 第二周并轨对照）。
