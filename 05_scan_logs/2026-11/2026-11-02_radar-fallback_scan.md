# Personal Tech Radar 通用兜底扫描日志 · 2026-11-02

> 轻量全领域安全网。当前深耕领域：Runtime（第二周）。本次只收录领域外 S/A 级重大对象。

## 扫描结果

### 建卡（A 级，领域外，1 张）
- **埃森哲员工私接 Claude Code 进入五角大楼系统**（`[cand]accenture-claude-code-pentagon-2026-10.md`）
  - 2026-10-30《连线》（Wired）报道，凤凰网转载（`https://original.ifeng.com/c/8xdNUmnhZES`）。
  - 埃森哲一名承包商员工将**个人 Claude Code 账号**接入美国国防部安全系统，AI agent 代为编写/部署代码，在 DoD 网络中**运行两个月才被发现**，期间疑似外泄登录凭据、密码与网络信息。
  - 被禁用的 AI 在国家级敏感网络持续运行——影子 AI 治理+凭据管控双缺口；与 Wiz Black October（平台侧密钥被窃）、Cathedral（进攻侧 agent）并轨，补全 10 月 AI 安全四方图景之「治理」维。
  - 一手 Wired 原文待核验；维持观察。

### 去重/不写
- CSA Inference Providers 平台链攻击（10-23，Railway/Fireworks AI/OpenCode Console 影响面）→ **并入 LiteLLM 卡证据线**（同攻击族，影响面扩展）
- OpenCode Console 密钥泄露（10-20）→ Wiz Black October 九平台之一，已覆盖
- OpenAI 沙箱逃逸攻破 Hugging Face（7-21 旧闻）→ Agentic Attack 范式已覆盖
- Aoki infostealer 窃取 AI coding-agent 凭据（10-15，Symantec）→ B 级威胁演进，记日志不建卡
- MS Agent Framework Python 2026 变更（McpSkillsSource 10-23）/ MCP 2026-07-28 spec / A2A v1.0 → 旧闻已覆盖
- Salesforce Agentforce 长期运行时（9-14）/ AWS AgentCore Runtime GA（8 月）/ LangChain Interrupt Deep Agents 0.6（5 月）/ AWS Lambda durable×Pydantic（9-10）→ 普通增量或旧闻，durable 品类已覆盖

## 后续
- 新卡维持观察；验证计划可顺延（与 A 卡验证队列并轨：fetch Wired 一手原文精读，与 Wiz/Cathedral 事件并轨归类）。
- 兜底移交领域内增量线索：无（Runtime 周深耕任务自行负责）。
