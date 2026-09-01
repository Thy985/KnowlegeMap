# 扫描日志 · 2026-09-01 首轮定向扫描（MCP 生态 + Agent Evals）

- **日期**：2026-09-01
- **扫描主线**：Top20 S 档前二 —— MCP 生态（#1） + Agent Evals（#2）
- **来源**：MCP 官方博客/Spec、MCP Registry、GitHub、promptfoo 官方文档、2026 横向评测、本机实测

## 1. 扫描范围
- MCP：官方 2026-07-28 发布说明 + Spec；Registry 现状；通知类 server 盘点
- Evals：promptfoo / DeepEval / OpenAI Evals / Inspect / Ragas / Langfuse 选型格局；promptfoo 本机最小试跑

## 2. 信号与收线（6 条）

| # | 线索 | 一句话价值 | 来源 | 处理 |
|---|---|---|---|---|
| 1 | MCP 2026-07-28 无状态协议 | 协议史上最大版本，秒级相关（发布仅 1 个月），直接关系 Tool System 知识升级 | 官方博客/Spec | ✅ → candidates |
| 2 | MCP Registry 数千 server | 生态规模化证据；Registry 仍 Preview | registry.modelcontextprotocol.io | 并入 #1 证据 |
| 3 | MCP 通知类 server 生态 | 与 agent-attention 直接同域，现成参考实现 | GitHub（mcp-win-toast 等） | ✅ → candidates |
| 4 | promptfoo 本机可跑通 | Evals 最小试跑成功（v0.122.2，2/2 PASS） | 官方文档 + 实测 | ✅ → candidates |
| 5 | Evals 框架选型格局 | promptfoo/DeepEval/OpenAI Evals/Inspect/Ragas/Langfuse 分层清晰 | 2026 多份横向评测 | ✅ → candidates |
| 6 | OpenAI 官方迁移 cookbook | 官方推动 OpenAI Evals → promptfoo，趋势信号 | developers.openai.com | 并入 #4/#5 |

## 3. 筛选结果
- 进入 candidates：4 张（mcp-2026-07-28-stateless / mcp-notification-servers / promptfoo-agent-evals / evals-framework-landscape）
- 已覆盖/重复：无（MCP 与 Evals 均为知识库空白区）
- 与主线无关丢弃：0 条

## 4. 连接更新
- 04_connections：MCP（#1 协议、#通知 server）与 Evals（promptfoo、框架格局）4 行从"待验证"升为"🟡 已出候选卡"

## 5. 本机实测（promptfoo）
- 环境 Node v22.23.2 / npm 10.9.8；`npx -y promptfoo@latest eval`（echo provider，2 用例）
- 结果 `✓ 2 passed (100%)` —— CLI/YAML/CI 化评估管线可用，接真实 provider 仅需 API key

## 6. 下一步
- [ ] MCP：精读迁移说明，产出"stateless MCP server 最小 probe"（对 Tafcm/agent-attention 的改造评估）
- [ ] MCP：对照 agent-attention 与 mcp-win-toast/mcp-notifications，产出"改造为 MCP 通知 server"设计方案
- [ ] Evals：promptfoo 接入真实 provider + Tafcm ADI 回归用例（升级 validated 候选）
- [ ] Evals：DeepEval / Inspect 各跑一次最小 demo（为 silver-shield / dsh-pentest 选型）
