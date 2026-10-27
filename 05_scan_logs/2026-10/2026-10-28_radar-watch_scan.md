# 深耕扫描日志 · 2026-10-28（Personal Tech Radar · Runtime 周 Day3 增量扫描）

> 定位：周二~周四只追增量（新 release/新工具/相邻项目）；S/A/B 写卡、C 级记日志、普通 release 一律不写。

## 扫描范围
Runtime 领域两路增量检索（Dapr/Agent Substrate 锚点动态 + durable execution 品类新 release），去重基准比对后判定。

## 发现与判定

### 建卡 0 张；既有卡并入增量 2 处（durable 品类卡）
本日无新对象达写卡阈值（S/A/B 新对象）；4 个增量信号全部并入既有 durable 品类卡，不新建卡（避免碎片化）：
- **Dapr v1.19（10-22 官方 release，B 级锚点平台增量）**：Scheduler 服务 actor placement + Binary Store building block + alpha search/vector APIs + workflow workers 只收每轮新增 history 事件——Dapr Agents 底层平台能力增强（actor 放置/向量存储），并入品类卡证据线 ["https://blog.dapr.io/posts/2026/10/22/dapr-v1.19-is-now-available/"]
- **Diagrid agent-integrations（docs 10-24，B 级领域内新工具）**：开源 drop-in 包装库把既有 agent 代码包进 Dapr Workflows，每个 LLM 调用/工具执行→checkpointed durable activity（自动故障检测+恢复）；"durable 化既有框架"而非从零构建——**TeamMind 直接候选**，并入品类卡 ["https://docs.dapr.io/developing-ai/agent-integrations/"]
- **DBOS（10-12 对比文确认，B 级品类第 8 向候选）**：Temporal/Restate/DBOS 三强格局（PostgreSQL 原生 durable execution）；Temporal Server 1.32.1（10-09）——补入品类横向 ["https://revisit.tech/blog/durable-execution-in-2026-revisit-temporal-restate-and-dbos-before-you-hand-roll-retries-sagas-and-cron-jobs/"]
- **Mastra core 1.79.0（10-21，B- 普通增量）**：durable snapshot 减半（工具结果不再双存）；`stopWhen` 保留完整 step——长时程 agent 存储成本优化，并入品类卡 ["https://newreleases.io/project/github/mastra-ai/mastra/release/@mastra/core@1.79.0"]

### 去重命中（不重复收集）
- Restate $20M A 轮（9-30）+ Replit 采用（10-15）——10-27 品类卡已覆盖
- Mastra 1.73/1.78、Temporal llm-info、Obelisk 0.42——品类卡已覆盖
- Agent Substrate：**无新变化**（10-22 发布后静默，符合预期）

## 文件变更
- **修改** `03_expansion_queue/candidates/[cand]durable-execution-category-mainstreaming-2026-10.md`（§2 追加 4 条 Day3 证据 + §4 追加 URL）
- **修改** `06_expansion_index/README.md`（新增 2026-10-28 深耕段）
- **修改** `_INDEX.md`（追加本日志行）
- **新建** `05_scan_logs/2026-10/2026-10-28_radar-watch_scan.md`（本日志）

## 结论
**Potentially Relevant**（无新对象写卡；durable 品类卡并入 4 条 B 级增量——Dapr v1.19/Diagrid wrapper/DBOS 第 8 向/Mastra 1.79，为周五验证日扩充横向素材）
