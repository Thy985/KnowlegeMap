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
| 一手来源（官方文档/源码/论文/Release URL） | MS Durable Extension ["https://learn.microsoft.com/en-au/agent-framework/hosting/durable-extension"]；AWS Lambda Durable Go SDK ["https://aws.amazon.com/about-aws/whats-new/2026/10/aws-lambda-durable-go-sdk-support/"]；Restate ["https://restate.dev/"]["https://docs.restate.dev/ai"]；Mastra 1.73/1.78 ["https://openorchestrators.org/news/mastra-1-73-durable-recovery/"]；Temporal llm-info ["https://temporal.io/llm-info"]；Obelisk 0.42 ["https://obeli.sk/blog/announcing-obelisk-0-42/"]；品类汇总 ["https://insights.reinventing.ai/articles/ai-agents-open-source-tooling-wave-2026-10-20"] |
| 证据等级 | FACT（官方文档/官方公告/官方仓库 release 多源交叉） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① 周五（10-30）durable 品类 7 向横向对照表（步骤持久化粒度/恢复语义/部署形态/语言栈/适用场景）；② 精读 MS durable extension 文档核对 checkpoint 语义；③ Restate quickstart 可行性评估（Java 栈是否可接入 TeamMind 思路） |
| 预期完成时间 | 2026-10-30（周五验证日）；本卡先占位 |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [ ] 维持观察
- [ ] 拒绝（原因）
