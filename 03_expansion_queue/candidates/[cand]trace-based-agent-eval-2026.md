# 候选证据卡 · [cand] Trace-based Agent Evaluation（agentevals + Agent TraceBench + AWS Agent Health）
> 状态：`[cand]` ｜ 分类：Agent 评测 × 可观测（G2 主动研究 / S2 核心） ｜ 发现：2026-09-12（雷达 #11） ｜ 等级：**A**
## 一句话定位
**Trace-based Evaluation 新范式**：以 OpenTelemetry trace 为 Agent 行为的原始证据，**记录一次、可反复评测、不重新执行**——agentevals 是代表实现（框架无关、本地优先、golden eval sets、CI/CD 门禁），Agent TraceBench / AWS Agent Health / Bedrock AgentCore 佐证范式正在被开源与云厂商共同确认。
## 1. 它是什么 / 解决什么问题
- 痛点：传统评测=对数据集重新执行 agent（烧 token、非确定性、框架绑定）；Agent 行为轨迹（工具选择/参数/顺序/失败重试）无法用"输出评分"覆盖["https://github.com/agentevals-dev/agentevals"]
- **agentevals（agentevals-dev，Apache-2.0，2026-09-04 活跃更新）**：从预记录 OTel traces 直接评分——**no re-execution**（不重放昂贵 LLM 调用）；golden eval sets（预期行为→确定性 pass/fail 门禁）；tool trajectory 匹配（EXACT/IN_ORDER/ANY_ORDER）+ response match + LLM judges + 自定义 evaluator（Python/JS/任意语言/OpenAI Eval API）；CLI/Web UI/**MCP server**/Helm chart；支持 LangChain/Strands/Google ADK/OpenAI Agents SDK，Jaeger JSON + OTLP 输入
- **Agent TraceBench（MDPI Software 论文）**：JSONL trace 步骤 + 确定性延迟/token/失败摘要 + 因果顺序重放 + OTel span 导出 + **CI 回归检查**（聚合阈值门 + 分布感知置换检验），离线零依赖["https://zenodo.org/records/21194993/files/AgentTraceBench_MDPI_Software.pdf?download=1"]
- **AWS 系（2026-08/09）**：OpenSearch Agent Health（分析 traces + 跑评测）、Bedrock AgentCore Evaluations（OTel 解耦评测——"telemetry 流经 OTel 即可评分，与底层 SDK 无关"）["https://aws.amazon.com/blogs/big-data/observing-and-evaluating-production-agents-using-opensearch-agent-health/"]["https://aws.amazon.com/blogs/machine-learning/evaluate-any-agent-framework-with-amazon-bedrock-agentcore-evaluations/"]
- 同线：AEMA（arXiv 2601.11903，可验证多 Agent 评测框架）、TruLens（09-03 更新：OTel GenAI semconv 双发射 + conversation_id 线程分组）、llmmas-otel（arXiv 2608.24271，MAS 观测+故障注入）
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-12）**：agentevals README 全量精读 ✅（含明确的能力边界声明）、Agent TraceBench 论文 ✅、AWS 官方博客 ×2 ✅
- **agentevals 的边界声明本身就是重要信息**：Claude Code/Codex/OpenCode **不发射 GenAI semconv 格式的 OTel**——"对每个 harness 的专有遥测做胶水适配需数千行代码，且主导信号是'最终输出感觉对不对'而非'工具轨迹对不对'"——印证 harness 可观测性缺口（连接 DeepSeek Harness 的 session-telemetry-otel、OpenCode 卡）
- 范式确认度：开源实现（agentevals/TraceBench）+ 云厂商（AWS 双产品）+ 学术（AEMA）三线独立出现
## 3. 与我的连接
- **连接的项目**：**Validation 编译器**（trace 即 Evidence 收集的工程化——"记录一次、可反复评估"正是证据可重放需求）；**TeamMind**（五维模型 Evaluation=invariants——tool trajectory 确定性门禁可作运行时不变量）；**Tafcm**（本地评测零成本路径）；**silver-shield**（trace 审计 + 回归门禁）
- **连接的知识点**：Agentic CLEAR（trace 作为证据）、OTel GenAI 可观测（A）、agentic-benchmarks（A）、HAAF（A）、Agent Harness/Control Plane（S）
- **潜在收益**：为 TeamMind/Validation 提供"不重新执行的 trace 评测"方法论与工具链；dsh 的 session-telemetry-otel 若对齐 GenAI semconv，可直接接入 agentevals 生态
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/agentevals-dev/agentevals ｜ https://zenodo.org/records/21194993/files/AgentTraceBench_MDPI_Software.pdf?download=1 ｜ https://aws.amazon.com/blogs/big-data/observing-and-evaluating-production-agents-using-opensearch-agent-health/ ｜ https://aws.amazon.com/blogs/machine-learning/evaluate-any-agent-framework-with-amazon-bedrock-agentcore-evaluations/ |
| 证据等级 | **FACT（README 精读 + 论文 + AWS 官方博客）** |
| 验证方式 | 本地装 agentevals，用样本 trace（helm/k8s）跑 tool_trajectory_avg_score → 对照 TeamMind 不变量设计 → 评估 TraceBench CI 门禁入 Validation 编译器 |
| 预期完成时间 | 2026-09/10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
