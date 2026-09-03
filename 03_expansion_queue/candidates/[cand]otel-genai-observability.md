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
