# 深耕扫描日志 · 2026-10-27（Personal Tech Radar · Runtime 周 Day2 · 增量扫描）

> 周二分工：只追增量（新 release/新工具/相邻项目），写候选卡（S/A/B），与去重基准比对。

## 扫描范围（Runtime 领域增量）
durable execution 品类（MS/AWS/Restate/Mastra/Temporal/Obelisk）｜分布式多 agent 编排（MCP 2.0 落地）｜锚点活跃度（Agent Substrate/ACE 无新变化，保持二号锚点）

## 发现与判定

### 建卡 1 张（B 级）：`[cand]durable-execution-category-mainstreaming-2026-10.md`
**durable execution 品类主流化（2026-10 密集成熟）**——5 大官方信号同周出现：
1. **MS Agent Framework Durable Extension**（10-17 官方文档）——主流编排框架官方 durable 扩展（persist sessions/checkpoint orchestration/recover）
2. **AWS Lambda Durable Execution SDK for Go GA**（10-15 官方公告）——serverless 平台级 GA，暂停等待外部事件最长一年
3. **Restate agent 原生定位**（10 月上旬 docs 更新 + Replit 采用）——成熟开源运行时 agent 化；**Java/Kotlin SDK 对 TeamMind 是直接候选**
4. **Mastra 1.78**（10-15 agent scopes/queueSignal/resume 语义；durable agents 1.45/AgentController GA 10-06/goals 1.43/schedules 1.50）——自托管框架 durable 原语化
5. **Temporal llm-info agent 适配页**（10-15）+ **Obelisk 0.42 durable agents + zero token architecture**（10-04，Kelsey Hightower PlatformCon 概念）

**服务缺口③**：durable 品类横向（Dapr vs Vercel vs Notion）扩为 7 向（+MS/Lambda/Restate/Mastra），周五（10-30）验证日素材库就绪。
**不重复**：Dapr Agents（A 卡，单对象）互补；Vercel/Notion（10-20~22 B 级已记）；MCP spec（已覆盖）。

### 记日志不建卡（B 级增量，已有对象）
- **MCP 2.0 成为共同地板**：Mastra `@mastra/mcp` 2.0（09-22）+ AG2 全量移植 MCP 2.0（breaking，1.1.2 10-03 含 ACP 0.12 serving/A2A AgentCard 签名）+ OpenAI SDK 64 页 discovery cap——2026-07-28 spec 落地动态，并入 MCP 卡认知，不新卡
- **编排框架普通增量**：OpenAI Agents SDK 0.24.0 Py/0.20.0 TS（hardening：checkpoint 校验/approval 计入 maxTurns）、CrewAI 1.15.28（agent-invocable eval）、Pydantic AI 2.53-2.57（no-breaking 政策）、AutoGen 进入维护模式（安全修复）→ 普通增量不写
- **Agent Substrate/ACE**：本周无新变化（阿里云 09-28 解读文为旧闻）→ 二号锚点维持

## 文件变更
- **新建** `03_expansion_queue/candidates/[cand]durable-execution-category-mainstreaming-2026-10.md`（B 级）
- **修改** `06_expansion_index/README.md`（新增 2026-10-27 段 + 去重基准追加对象）
- **修改** `04_connections/README.md`（追加 Restate→TeamMind durable execution 连接）
- **修改** `_INDEX.md`（追加本日志行）
- **新建** `05_scan_logs/2026-10/2026-10-27_radar-watch_scan.md`（本日志）

## 结论
**New**（durable execution 品类主流化 5 信号收敛为 B 级新卡，直接服务周五 7 向横向；领域内普通增量记日志不写卡）
