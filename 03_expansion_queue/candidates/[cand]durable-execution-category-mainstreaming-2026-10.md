# 候选对象证据卡 · Durable Execution 品类主流化（2026-10 密集成熟）

> 状态：`[cand]` ｜ 关联方向：**Agent Runtime（当前深耕领域）** / Durable Execution 品类 / 多 Agent 编排 ｜ 日期：2026-10-27（Runtime 周 Day2 增量扫描捕获）

## 一句话定位
2026-10 中下旬，durable execution 从"基建 niche"密集主流化：**微软 MS Agent Framework 官方 Durable Extension**（10-17）、**AWS Lambda Durable Execution Go SDK GA**（10-15）、**Restate 强化 agent 原生定位**（Replit 采用为证）、**Mastra durable/AgentController GA**（10-06~15）、**Temporal 出 agent 适配页**（10-15）——五大信号同周出现，是 Dapr Agents（10-16 头号锚点）之外"步骤持久化+崩溃恢复"范式的品类级收敛证据线。

## 1. 它解决什么问题
- 长时程 agent 任务跨进程崩溃/重启会从头重跑、重复已完成的 LLM/工具调用——durable execution 通过**每步持久化 + 从最后完成步骤恢复**解决（同 Dapr Agents 问题域）
- 不同厂商路线：**平台侧**（AWS Lambda Durable Execution：serverless 函数级 checkpoint，暂停等待外部事件最长一年）、**编排框架侧**（MS Agent Framework durable extension、Mastra harness 层）、**独立运行时侧**（Restate/Temporal：通用 durable runtime 反哺 agent）
- 单机/单人场景的"长驻 agent"原语化：schedules/goals/typed signal queues/durable resume 从自拼代码变成框架原语（Mastra 1.78）

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（MS Agent Framework Durable Extension，2026-10-17 官方文档）**：为 agents/multi-agent orchestrations/workflows 提供 durable execution——persist agent sessions、checkpoint orchestration/workflow progress、recover ["https://learn.microsoft.com/en-au/agent-framework/hosting/durable-extension"]。MS Agent Framework 1.0 GA（10-13，已覆盖）后一周即上 durable 扩展——主流编排框架官方背书。
- **FACT（AWS Lambda Durable Execution SDK for Go GA，2026-10-15 官方公告）**：Go 原生体验构建 Lambda durable functions；checkpoint 自动 + 等待外部事件暂停最长一年 ["https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/"]——serverless 平台级 GA。
- **FACT（Restate agent 原生定位 + Replit 采用，10 月上旬更新）**：Restate 定位"the Durable Runtime for your Agents and Backends"；Replit quote"Restate now handles all durable orchestration at Replit"；AI 文档明确 durable execution/多轮会话/并发控制/agent 间任务路由 ["https://restate.dev/"]["https://docs.restate.dev/ai"]——成熟开源运行时（非本周新项目）agent 化采用案例。
- **FACT（Mastra 1.78，2026-10-15）**：agent scopes（typed `<type>:<value>` 身份，冲突 HTTP 400）+ `queueSignal()` typed signal queue + resume 保留 suspendData + `AGENT_RESUME_INVALID_DATA`；此前 1.45 durable agents / 1.43 goals / 1.50 schedules / AgentController GA（10-06）；10-01~17 共 15 个 minor release；durable 仍标 beta ["https://openorchestrators.org/news/mastra-1-73-durable-recovery/"]["https://insights.reinventing.ai/articles/ai-agents-open-source-tooling-wave-2026-10-20"]
- **FACT（Temporal agent 适配页，2026-10-15）**：Temporal llm-info 页面向 AI crawlers/assistants ["https://temporal.io/llm-info"]——durable execution 鼻祖开始 agent 化。
- **FACT（Obelisk 0.42，2026-10-04）**：durable agents + layered sandboxes；引用 Kelsey Hightower PlatformCon 2026 "zero token architecture"（模型构建应用，执行期不耗 token）["https://obeli.sk/blog/announcing-obelisk-0-42/"]
- **FACT（Day3 增量：Dapr v1.19，2026-10-22 官方公告）**：Scheduler 服务 actor placement + Binary Store building block + alpha search/vector APIs + workflow workers 只收每轮新增 history 事件——Dapr Agents 底层平台 release，actor 放置/向量存储直接增强 Dapr Agents 编排与检索能力 ["https://blog.dapr.io/posts/2026/10/22/dapr-v1.19-is-now-available/"]
- **FACT（Day3 增量：Diagrid agent-integrations，docs 2026-10-24）**：开源 drop-in 包装库——把既有 agent 代码包进 Dapr Workflows，每个 LLM 调用/工具执行变 checkpointed durable activity（自动故障检测+恢复）；**"durable 化既有 agent 框架"而非从零构建**，TeamMind 直接候选 ["https://docs.dapr.io/developing-ai/agent-integrations/"]
- **FACT（Day3 增量：DBOS 第 8 向候选）**：Temporal/Restate/DBOS 三强格局确认（2026-10-12 对比文；Temporal Server 1.32.1 于 10-09）——PostgreSQL 原生 durable execution 开源实现，补入品类横向 ["https://revisit.tech/blog/durable-execution-in-2026-revisit-temporal-restate-and-dbos-before-you-hand-roll-retries-sagas-and-cron-jobs/"]
- **FACT（Day3 增量：Mastra core 1.79.0，2026-10-21）**：durable agent snapshot 尺寸减半（工具结果不再每步双存），`stopWhen` 条件仍收完整 step——长时程 durable agent 存储成本优化 ["https://newreleases.io/project/github/mastra-ai/mastra/release/@mastra/core@1.79.0"]
- **与已有知识不重复**：Dapr Agents（已建 A 卡，单对象锚点）互补——本卡是**品类全景**；Vercel durable-harness/Notion Gen-6（10-20~22，B 级记日志）互补；MCP 2026-07-28 spec/AG2 MCP 2.0 移植（MCP 卡已覆盖）不重复。

## 3. 与我的连接
- **连接的项目**：
  - **TeamMind（Java 多 Agent 运行时）——最强连接**：Restate 提供 **Java/Kotlin SDK**，是 TeamMind 可直接评估的 durable execution 候选（对照 Dapr Agents 的 Python 实现）；MS durable extension 提供编排框架侧参照
  - **Tafcm（本地优先）**：Obelisk zero token architecture（执行期不耗 token）+ 本地持久化——端侧长时程任务参照
  - silver-shield / 引擎：durable checkpoint = 可审计执行链（每步持久化即证据）
- **连接的知识点**：能力树 agent-runtime.md **A 层（Durable Execution 与失败恢复）**——A4 durable-harness 品类节点扩容；**缺口③**（durable 品类横向 Dapr vs Vercel vs Notion）扩为 7 向（+MS/Lambda/Restate/Mastra）；Memory 周架构参照（agent-workflow vs agent-memory 双 store 语义被多厂商复用）
- **潜在收益**：周五（10-30）验证日的品类横向素材库；TeamMind 生产化的 durable state/恢复方案选型输入（Restate Java vs 自研）

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | MS Durable Extension ["https://learn.microsoft.com/en-au/agent-framework/hosting/durable-extension"]；AWS Lambda Durable Go SDK ["https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/"]；Restate ["https://restate.dev/"]["https://docs.restate.dev/ai"]；Mastra 1.73/1.78 ["https://openorchestrators.org/news/mastra-1-73-durable-recovery/"]；Temporal llm-info ["https://temporal.io/llm-info"]；Obelisk 0.42 ["https://obeli.sk/blog/announcing-obelisk-0-42/"]；品类汇总 ["https://insights.reinventing.ai/articles/ai-agents-open-source-tooling-wave-2026-10-20"]；Dapr v1.19 ["https://blog.dapr.io/posts/2026/10/22/dapr-v1.19-is-now-available/"]；Diagrid agent-integrations ["https://docs.dapr.io/developing-ai/agent-integrations/"]；DBOS/三强对比 ["https://revisit.tech/blog/durable-execution-in-2026-revisit-temporal-restate-and-dbos-before-you-hand-roll-retries-sagas-and-cron-jobs/"]；Mastra 1.79 ["https://newreleases.io/project/github/mastra-ai/mastra/release/@mastra/core@1.79.0"] |
| 证据等级 | FACT（官方文档/官方公告/官方仓库 release 多源交叉） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① 周五（10-30）durable 品类 7 向横向对照表（步骤持久化粒度/恢复语义/部署形态/语言栈/适用场景）；② 精读 MS durable extension 文档核对 checkpoint 语义；③ Restate quickstart 可行性评估（Java 栈是否可接入 TeamMind 思路） |
| 预期完成时间 | 2026-10-30（周五验证日）；本卡先占位 |

## 5. 验证结果
**2026-10-30（Runtime 周 Day5 验证日）品类 9 向横向对照（产出）**：

| 方案 | 层位 | 步骤持久化粒度 | 恢复语义 | 部署形态 | 语言栈 | 并发/规模信号 |
|---|---|---|---|---|---|---|
| **Dapr Agents** | 基础设施运行时（workflow+actor+state） | 每步 reasoning+tool call（双 store：agent-memory/agent-workflow，actorStateStore 必需） | 从最后完成步骤恢复，不重放已完成 LLM/工具调用（v1.1.0 文档+包实测确认） | K8s/本地 sidecar | Python | 400 分布式 multi-agent 工作流生产评估；Diagrid Dev Dashboard 可视化 |
| **Vercel durable-harness** | harness 包装层（10-20/21 开源） | agent logic 每步 session 存 durable log | 从 durable log 恢复 | 无服务器/本地 | TS/JS | 包装 Pi/OpenCode/Claude Code/Codex |
| **Notion Gen-6** | queue-backed worker loop（10-22） | worker loop 步骤 | queue 语义（未详） | 服务器 | 未详 | 24h 无人值守 |
| **MS Durable Extension** | 编排框架扩展（10-17 文档） | agent session + orchestration/workflow checkpoint | checkpoint 恢复 | Azure Functions | C#/.NET | MS Agent Framework 1.0 GA（10-13）后一周推出 |
| **AWS Lambda Durable Go SDK** | serverless 平台级（10-15 GA） | 函数级 checkpoint 自动 | 暂停等待外部事件最长一年 | AWS Lambda | Go | 平台原生 GA |
| **Restate** | 通用 durable runtime（agent 定位） | 每步（virtual objects） | 从最后完成步骤恢复 | 自托管/K8s/托管 | Java/Kotlin/TS/Python 等 | Replit 采用（全量 durable orchestration） |
| **Mastra** | JS 编排框架（1.78/1.79，10-15/21） | agent step snapshot（1.79 尺寸减半） | resume 保留 suspendData | 服务器 | TS/JS | agent scopes+queueSignal typed signal |
| **DBOS** | Postgres 原生 durable runtime（第 8 向） | 每步（PostgreSQL 事务） | 从最后完成步骤恢复 | Postgres+服务器 | TS/Python | Temporal/Restate/DBOS 三强格局（10-12 对比文） |
| **AWS Infinity** | 研究型并发 runtime（10-23 开源，Hydro） | slice（history→一次补全→持久化→至多一个工具调用） | 从持久化 history 恢复（挂起不占内存） | serverless step 模式（等待零计算） | 待定（研究） | 75k 并发/8GB（RPi 5 基准）；第三条设计路线 |

**横向结论**：①层位分明——基础设施运行时（Dapr/DBOS/Restate）vs harness 包装（Vercel/Notion/Mastra）vs serverless 平台（AWS Lambda）vs 并发挂起（Infinity）；②恢复语义两派——**步骤持久化恢复**（Dapr/Restate/DBOS/MS，重放不重执行）vs **挂起恢复**（Infinity/Lambda 暂停，不占资源）；③对 TeamMind 的启示——若走自研：Dapr 双 store+actor+pub-sub 是完整设计基线（本卡 Dapr 已 validated）；若评估现成：Java 栈首选 **Restate**（Java/Kotlin SDK，durable 化既有 agent），其次 Dapr Java SDK 路线；Diagrid agent-integrations wrapper（3 行代码 durable 化既有 agent）为轻量路径候选。

## 6. 决策
- [ ] 晋升 validated（品类全景卡，非单点验证对象；各成员已有独立证据）
- [x] 维持观察（品类 9 向横向完成；成员级验证随 Dapr validated + 未来周次）
- [ ] 拒绝（原因）
