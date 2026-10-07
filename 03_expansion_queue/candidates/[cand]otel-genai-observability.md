# 候选证据卡 · [cand] OpenTelemetry GenAI 可观测标准 + LLM 平台格局

> 状态：`[cand]` ｜ 分类：LLM 可观测性（B12）/ G2 已启动未深化 ｜ 发现：2026-09-01 ｜ 等级：**A**

## 一句话定位
OpenTelemetry **GenAI 语义约定**已从实验态走向核心可移植标准（Datadog/Google/AWS/Azure/Langfuse/Phoenix 原生接入），Langfuse v3 直接构建于 OTel 之上——LLM/Agent 可观测性从"各写各的"走向"标准协议"。

## 1. 它是什么 / 解决什么问题
- **OTel GenAI SIG**（2024-04 成立）标准化了描述 LLM 调用/agent 步骤/工具调用/向量库查询的 span 属性、指标名、事件 schema；2026 核心属性已出实验态，trace 可移植["https://pythondatabench.com/article/llm-observability-python-langfuse-langsmith-arize-phoenix-2026"][https://aiworkflowlab.dev/it/article/osservabilita-llm-2026-tracing-valutazione-langsmith-langfuse]
- **Langfuse v3**：基于 OpenTelemetry 重建；自托管；trace/评估/prompt 管理一体["https://langfuse.com/docs/observability/sdk/upgrade-path/python-v2-to-v3"]
- **平台格局**：LangSmith（LangChain/LangGraph 原生）、Arize Phoenix（eval 严谨/RAG 漂移）、Braintrust（eval-first）、OpenLIT（自动插桩）["https://www.marktechpost.com/2026/08/09/top-llm-observability-and-evaluation-platforms-in-2026-langfuse-langsmith-braintrust-arize-and-more-compared/amp/"]
- 选型：LangGraph 栈→LangSmith；自托管→Langfuse；eval 严谨→Phoenix["https://www.marktechpost.com/2026/08/09/top-llm-observability-and-evaluation-platforms-in-2026-langfuse-langsmith-braintrust-arize-and-more-compared/amp/"]
> **雷达增量（2026-09-04，Changed）**：
> - **OTel GenAI 语义约定已稳定**（2025 末正式 stabilized）：`gen_ai.*` 属性标准化 prompt/model/token 用量/tool 与 agent 调用，已成 CNCF 生态厂商中立基线；2026-04-21 OTel 官方博客（MS James Newton-King）详解"LLM 调用内部：GenAI 可观测性"["https://github.com/open-telemetry/opentelemetry.io/blob/0c1d9634144d434ac1604c1611ffd6b24bdf24ed/content/en/blog/2026/genai-observability/index.md"]["https://signoz.io/comparisons/llm-observability-tools/"]
> - **可观测覆盖 6 层已成形**：LLM 调用 / agent 编排 / MCP 工具调用 / content capture / 质量评估，多数工具已原生接入 OTel["https://www.greptime.com/blogs/2026-05-09-opentelemetry-genai-semantic-conventions"]
> - **新玩家**：阿里云 **LoongSuite**（OTel 之上推出 GenAI 可观测语义规范 + 零代码 Python Agent 采集）、Iris（OTel-native 自托管 trace+eval+回归检测，但同名项目混乱待甄别）["https://www.alibabacloud.com/blog/loongsuite-python-agent-launches-observability-into-every-ai-agent-action-zero-code-integration_603016"]["https://github.com/saishettar/iris"]
> - **含义**：Tafcm ADI 接 OTel GenAI 现在有稳定规范可依；阿里 LoongSuite 的零代码采集与 MCP 工具调用观测值得对照
> **雷达增量（2026-09-08，Changed）**：
> - **Helicone 进入维护模式**：2026-03 被 Mintlify 收购后仅安全补丁与 bugfix，不再功能迭代——可观测选型格局出现一个"事实出局"样本，选型清单需更新["https://www.kosmoy.com/resources/blog/best-ai-observability-platforms-2026/"]
> - 新进者：**xtrace**（自托管 OTLP collector/UI/业务报告层，独立于 Xrouter，2026-09-03 活跃）、pydantic **Logfire**（生产 LLM/agent 可观测，AI 工具链深度绑定）、Comet **Opik**（trace+自动评估+仪表盘）["https://github.com/EeroEternal/xtrace"]["https://github.com/topics/agent-observability?l=python"]
> - **含义**：自托管 OTLP 栈（Langfuse/xtrace）与 eval 一体化（Opik/Logfire）双路线并行；Tafcm ADI 选型时需把 Helicone 从候选剔除
> **雷达增量（2026-09-16，agent span 语义正式化）**：
> - **OTel GenAI semconv v1.41.0（09-15 更新）**：`invoke_agent` span kind 规则正式化——**provider-managed agents**（OpenAI Assistants、Bedrock Agents，agent 跑在服务端）= **CLIENT** span；**framework-managed agents**（LangChain、CrewAI、Vercel AI SDK ToolLoopAgent）= **INTERNAL** span——不再由框架任意选择，agent span 语义可跨框架互操作["https://hivebook.wiki/wiki/opentelemetry-genai-semantic-conventions-gen-ai-span-attributes"]
> - **genai-otel-instrument 1.19.0（09-06）**：TraceVerde 生产 gap 反哺 spec 已成机制（PR #142：BlobPart/FilePart/UriPart 增加 modality 枚举，PDF/DOCX 不再落入 free-form 字符串分支，2026-05-16 merged）["https://pypi.org/project/genai-otel-instrument/"]
> - **OpenSearch LLM traces（09-01）**：OpenSearch 可观测性直接消费 GenAI semconv（model/token 用量/tool/agent step 标准化 span），GenAI SDK 支持 Strands Agents 等自动插桩["https://dev.to/jon_handler_9bb3e6b4a2fd0/read-your-ai-agents-mind-opensearch-observability-for-llm-traces-2ll"]
> - **TrueFoundry LLM 网关插桩实践（09-11）**：span kind 约定落地——外部 provider 调用=CLIENT、网关内 guardrail（PII 脱敏/schema 校验）=INTERNAL、根=SERVER["https://www.truefoundry.com/ar/blog/opentelemetry-llm-gateway-instrumentation"]
> - **含义**：① agent span kind 规则解决"同一 agent 在不同框架 trace 语义不一致"的互操作问题——**Tafcm ADI 接 OTel 时 span kind 决策有标准可依**；② 生产实践（OpenSearch/TrueFoundry/genai-otel-instrument）与 spec 双向往返，标准进入稳定演进期
> **雷达增量（2026-09-27，大厂 agent 观测环境入场 + 自托管 GA）**：
> - **AWS CloudWatch Omni（09-23）**：**首个大厂级 AI agent 观测/测试环境**——支持主流 AI 框架、IDE 集成、open inference、OpenTelemetry——**agent 观测从"工具层"升到"云平台原生能力"**["https://awsinsider.net/blogs/awsinsider-release-radar/2026/09/aws-launches-cloudwatch-omni.aspx"]
> - **OpenObserve v1.0 GA（09-22）**：自托管 AI observability 正式 GA（LLM traces/成本/评测）——自托管路线继 Langfuse/xtrace 后再添成熟选项["https://www.apmdigest.com/openobserve-v10-released"]
> - **Agentreplay（PyPI 0.1.4，09-24）**：agent 追踪平台（语义搜索 + RAGAS/G-Eval/toxicity evals + **Git-like prompt/response 版本化**）——"trace+eval+版本化"一体化小工具["https://pypi.org/project/agentreplay/"]
> - **Azure Foundry 外部 agent 观测注册 preview（09-01）**：LangChain 等外部 agent 通过 exporter 接入 Foundry 观测/评测——**跨框架 agent 注册进统一观测面**["https://learn.microsoft.com/en-gb/Azure/foundry/agents/how-to/register-external-agent"]
> - **含义**：① **AWS 入场 = agent 可观测成为云平台标准能力**（对照 OTel semconv 1.41 的标准化）——Tafcm/TeamMind 选型时"云原生观测（CloudWatch Omni 类）vs 自托管（OpenObserve/Langfuse 类）"成为顶层路线选择；② Agentreplay 的"Git-like 版本化"与 KnowlegeMap/记忆卡的"证据保留"同构——trace 即版本化证据；③ 观测、评测、版本化三者持续一体化——与 trace-based-eval 卡"行为数据层"收敛方向一致
> **雷达增量（2026-10-03，平台入局 + 标准进 IETF）**：
> - **Cloudflare Agents Tracing（10-01 转标准定价）**：agent tracing 免费 beta 结束——Workers Free 200k 日事件/3 天保留，Paid 20M 月事件/7 天保留（$0.60/百万事件增量）——**边缘云厂商把 agent 观测做成计费产品**（agent 观测从"工具"走向"云基础设施计费面"）["https://wasifahmed.dev/cloudflare-agents-tracing-observability/"]
> - **IETF draft-wnd-opsawg-icon-ps（07-09）**：**GenAI 语义约定进入 IETF 标准化流程**——四域语义（System Context/Token Economics/Vector Retrieval/Agent Reasoning）+ Protocol/Decision/System Events——**agent 观测从 OpenTelemetry 社区约定升级为国际标准流程对象**["https://www.ietf.org/archive/id/draft-wnd-opsawg-icon-ps-00.txt"]
> - **工具全景（Rework 09-29：13 工具 / AY 09-26 定价对比）**：LLM 专用 span 免费计费（仅 LLM 调用计费）+ Logfire 10M 条/月免费等定价分层——自托管（Langfuse/Phoenix/Opik/OpenLIT）vs 托管（Logfire/AgentOps）格局清晰["https://resources.rework.com/tools/ai-agents/best-ai-agent-observability-tools-2026"]["https://www.ayautomate.com/blog/best-ai-agent-observability-tools"]
> - **含义**：① **Cloudflare 把 agent 观测纳入 Workers 计费 = "观测即平台默认能力"再确认**（AWS 之后第二家云厂）——Tafcm/TeamMind 的观测选型已无"要不要"只有"选哪家/自托管哪种"；② **IETF draft = 标准从 OTel 社区走向国际标准**——agent 观测语义将成为网络运维标准的一部分（ICON），长期降低多厂商锁定；③ OTel semconv 1.41 + IETF + 双云厂 = **agent 观测标准化三层结构成型**（社区约定→云产品→国际标准）
> **雷达增量（2026-10-08，云厂观测面继续扩 + 语义约定 2.0 + 国内云厂）**：
> - **Google Cloud Agent Observability（10-07 文档更新）**：logs/metrics/traces 统一覆盖 **Gemini Enterprise Agent Platform、Agent Gateway、Model Armor** 的 agent——**第三家云厂（AWS/Cloudflare 后）把 agent 观测做成平台能力**["https://docs.cloud.google.com/stackdriver/docs/observability/agent-observability"]
> - **阿里云 OpenTelemetry GenAI Utils（09-21）**：**手动 instrumentation 方案**——自定义框架/多语言架构下生成符合 GenAI SemConv 的标准 Span，上报 ARMS——**国内云厂进 GenAI 观测**（四域语义落地产品）["https://help.aliyun.com/en/cms/cloudmonitor-2-0/integrating-llm-applications-with-opentelemetry-genai-utils"]
> - **OTel GenAI 2.0 Run Tree 语义（10-02）**：span 层级严格映射认知系统**执行树（Run Tree）**——"语义运行树"替代泛化 span 名——**约定 2.0 从"事件打点"升级为"结构建模"**["https://dev.to/ricardofriba/observabilidade-de-trajetorias-agenticas-com-opentelemetry-genai-hla"]
> - **Microsoft Foundry server-side tracing（09-30）**：接 Application Insights 即自动启用、无需改码——**托管 agent 观测零配置化**["https://learn.microsoft.com/en-gb/azure/foundry/observability/how-to/trace-agent-setup"]
> - **含义**：① **云厂观测面四方会齐**（AWS Omni/Cloudflare/Google/阿里 + Microsoft Foundry）——"agent 观测是云平台默认件"成定局，Tafcm/TeamMind 观测选型锁定托管 vs 自托管后直接对接云厂；② **OTel GenAI 2.0 Run Tree**——观测从"调用链"升级为"执行树结构"——与 Trace-Based Eval 卡"轨迹即评测依据"互证，轨迹语义化是 agent 评测的前提；③ 阿里 GenAI Utils 说明 GenAI 观测规范已成**中国云厂商基础设施**——国内部署（Tafcm 若上云）合规观测基线可循

## 2. 与我的知识/项目关系
- **Tafcm ADI 诊断接口**：OTel GenAI 约定可直接作为 ADI 的标准化底座
- **silver-shield CI/可观测体系**：从自建走向标准协议
- **G2 缺口"LLM 可观测性"** 从"1 篇散文"走向体系
- 与首轮 Evals 扫描的 Langfuse 交叉：可观测+评估一体

## 3. 证据与验证计划
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（OTel/Langfuse 官方 + 2026 评测） |
| 来源 | https://langfuse.com/integrations/native/opentelemetry ｜ https://www.marktechpost.com/2026/08/09/top-llm-observability-and-evaluation-platforms-in-2026-langfuse-langsmith-braintrust-arize-and-more-compared/amp/ |
| 验证方式 | 给 Tafcm ADI 或一个最小 agent 接 OTel GenAI trace，发往本地 Langfuse |
| 预期 | 2026-09/10 |

## 4. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
