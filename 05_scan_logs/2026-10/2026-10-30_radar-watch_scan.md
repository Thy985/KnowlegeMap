# 深耕扫描日志 · 2026-10-30（Personal Tech Radar Runtime 周 Day5·验证日）

> 定位：周五对 2-3 个高价值候选做实际验证/对比（非增量扫描）。当前领域：Runtime（10-26 周起）。

## 验证执行

### 1. Dapr Agents（A 卡头号锚点）→ 晋升 validated ✅
- **官方文档全文精读**：Getting Started（docs.dapr.io，10-25 更新，6728 tokens 全读）+ Core Concepts（12040 tokens）
  - **`Agent` 类 deprecated（v1.0.0-rc.1），`DurableAgent` 唯一推荐**（新状态，补入卡）
  - 中断恢复官方步骤：POST /agent/run 拿 WORKFLOW_ID → slow_weather_func 5 秒延迟期间 Ctrl+C → 重启 → GET /agent/instances/{WORKFLOW_ID} → 从最后持久化步骤继续、不重放已完成 LLM/工具调用
  - 双 state store 核对：agent-memory（会话历史，state.redis）+ agent-workflow（durable state，`actorStateStore: "true"` 必需）；LLM 走 Conversation API（conversation.openai 组件，Ollama 本地默认，YAML 换 provider）
  - 新增机制：event sourcing 重放 + `ContextAwareLogger` 抑制重放日志；AgentRunner 三模式 run/subscribe/serve
- **包级实测**：`pip install dapr-agents` → 1.1.0；DurableAgent/AgentRunner/AgentMemoryConfig/AgentStateConfig/ConversationDaprStateMemory 全部可导入
- **环境限制（如实记录）**：无 Docker/Dapr CLI/Redis/Ollama，未真实跑中断 demo；以文档精读+包实测+公开可复现步骤三级验证替代（按 Harness 周先例判定）

### 2. durable 品类卡（B）→ 9 向横向对照产出，维持观察
- 对照表见卡 §5：**四层位**（基础设施运行时 Dapr/DBOS/Restate；harness 包装 Vercel/Notion/Mastra；serverless 平台 AWS Lambda；并发挂起 Infinity）
- **恢复语义两派**：步骤持久化恢复（Dapr/Restate/DBOS/MS，重放不重执行）vs 挂起恢复（Infinity/Lambda，等待零资源）
- **TeamMind 启示**：自研以 Dapr 双 store+actor+pub-sub 为设计基线；评估现成 Java 首选 Restate；轻量路径 Diagrid wrapper

### 3. AWS Infinity（B 卡）→ 对照完成，维持观察
- 三路线设计对照产出（步骤持久化 vs 挂起恢复互补）；research early release，仓库级复现未做（GitHub robots 限制+无容器环境）

## 文件变更
- **修改** `03_expansion_queue/candidates/[cand]dapr-agents-distributed-runtime-2026.md`（§5 验证结果回填 + §6 决策晋升 validated）
- **修改** `03_expansion_queue/candidates/[cand]durable-execution-category-mainstreaming-2026-10.md`（§5 9 向对照表 + §6 维持观察）
- **修改** `03_expansion_queue/candidates/[cand]aws-infinity-agent-runtime-2026-10.md`（§5 对照结论 + §6 维持观察）
- **修改** `07_radar_watch/current_focus.md`（状态→active；周五 ✅；Runtime 历史行补 Day2-5）
- **新建** `05_scan_logs/2026-10/2026-10-30_radar-watch_scan.md`（本日志）

## 结论
**Changed**（Dapr Agents 候选→validated；durable 品类 9 向横向完成；Infinity 对照完成维持观察）
