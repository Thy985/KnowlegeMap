# 候选证据卡 · [cand] Agent Harness / Control Plane 新范式（Omnigent + MS Agent Framework + Harness 调查）

> 状态：`[cand]` ｜ 分类：Agent Runtime / Harness / 编排（S3/S5） ｜ 发现：2026-09-01 ｜ 等级：**S**

## 一句话定位
2026 年 Agent 工程的重心正从"单一 harness"上移到 **meta-harness / control plane 层**（组合、治理、协作）；Databricks Omnigent 与 Microsoft Agent Framework 1.0 是代表，arXiv 已有以 model-harness 视角拆解 runtime 六职责的综述论文。

## 1. 它是什么 / 解决什么问题
- **Databricks Omnigent**（2026-06-16 开源，Apache 2.0，alpha）：meta-harness，位于你已有的 Claude Code/Codex/Pi/自研 agent 之上，把多 harness 变成可互换部件。三支柱：Composition（组合多模型/harness）、Control（**在 meta-harness 层做有状态上下文策略**，如成本预算/权限，而非 prompt 层）、Collaboration（共享会话 URL 实时协作）。架构 = runner 包裹任何 agent 为统一 API 的沙箱会话 + server 提供策略/共享["https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents"]
- **Microsoft Agent Framework 1.0**（2025-10 GA；Build 2026 发布 Agent Harness、Hosted Agents、CodeAct、多代理编排模式稳定）["https://devblogs.microsoft.com/agent-framework/microsoft-agent-framework-at-build-2026-announce/"]["https://www.infoq.cn/article/aDEJegvNSKwvue2JZ0yI"]
- **Harness 调查论文**《From Question Answering to Task Completion: A Survey on Agent System and Harness Design》（arXiv 2606.20683）：把执行 harness 拆成 **observation / context / control / action / state / verification 六项耦合职责**，映射任务属性→harness 选择["https://arxiv.org/abs/2606.20683v1"]

## 2. 为什么与我的知识/项目关系密切
- **六职责分解（尤其 verification 是独立职责）与我的"验证编译器 / 五维模型"几乎同构**——我的理论在 2026 年获得学术侧独立印证，可交叉验证
- **TeamMind** 本质就是"项目级 meta-harness"：Omnigent 的控制面/共享会话模式可直接借鉴
- **EP-002 / Permission**：Omnigent 的"策略在 harness 层而非 prompt 层"正是我 EP 原则的工程化表述
- **agent-attention**：Omnigent 的实时共享会话 = 通知/协作的另一种形态

## 3. 证据与活跃度
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（Databricks/MS 官方 + arXiv 一手来源核验） |
| 来源 | https://github.com/omnigent-ai/omnigent ｜ https://www.databricks.com/blog/introducing-omnigent-meta-harness-combine-control-and-share-your-agents ｜ https://arxiv.org/abs/2606.20683v1 |
| 活跃度 | 极高（Omnigent 2026-06 开源、路线图含 GEPA/MemEx/RLM/Omnigent Server MCP；MS 2026-06 Build GA） |
> **雷达增量（2026-09-18，harness 内 context 工程机制）**：
> - **"Context Engineering Inside the Harness"（MarkTechPost 09-12）**：harness 层四机制击败上下文溢出/目标丢失——**compaction（压缩）、memory strategy（记忆策略）、context budgeting（上下文预算）、todo-state（任务状态跟踪）**，逐一对比 LangChain Deep Agents/Claude Code/Manus/OpenAI Codex/Bedrock AgentCore 的实现与**实际阈值**——context 工程从"prompt 层技巧"下沉为 harness 机制["https://www.marktechpost.com/2026/09/12/context-engineering-inside-the-harness-4-mechanisms-that-beat-context-overflow-and-goal-loss-on-long-horizon-tasks/"]
> - **TrueFoundry 网关层 context 工程（09-11）**：`X-TFY-CONVERSATION-ID` 会话管理把 30 轮运行变成一条可查询时间线（而非 30 条孤立请求）——context 编排下沉到网关层["https://www.truefoundry.com/es/blog/context-engineering-gateway-session-management"]
> - **含义**：① 与 Harness 调查论文"六职责"（observation/context/control…）互证——**context 职责的工程细节（四机制阈值）已在生产 harness 中收敛**；② Omnigent"控制面在 harness 层而非 prompt 层"获得实现级印证；③ TeamMind/自研 harness 可直接对照四机制与阈值做差距分析（compaction 触发阈值/budget 分配）
> **雷达增量（2026-09-24，Harness 自我演化/生成新主线）**：
> - **JIT-Agent（arXiv 2608.25593，09-03）**：**首个专为 just-in-time harness 生成打造的模型**——把 harness 智能确立为"可训练、可迁移、可复合"的 agent 能力维度["https://arxiv.org/html/2608.25593"]
> - **HarnessDev（arXiv 2609.01437，ByteDance Seed + SUTD + Georgia Tech + M-A-P + TokenWave）**：**LLM 能否创建并演化自己的 agent harness 的基准**——直接命中我 09-18"Context Engineering Inside the Harness"与 dsh 的 DeepSeek harness 主线（harness 从"手写"走向"模型自演化"）["https://arxiv.org/pdf/2609.01437"]
> - **Ecdysis（arXiv 2609.11677，09-10）**：运行时 harness 的高效/有效训练——harness 本身成为可训练对象["https://arxiv.org/abs/2609.11677"]
> - **StarHarness（arXiv 2608.24804，08-25，ServiceNow + Mila + Montréal，GitHub 开源）**：企业环境的**分层搜索演化 harness**（替换/演化 harness 组件）["https://arxiv.org/html/2608.24804v1"]
> - **AgentAO（arXiv 2608.13574v2）**：**策略治理的嵌入式工具使用 agent 运行时 harness**——威胁模型/治理模型/执行管线/结构化事件接口（不提供形式安全保证，但治理显式化）["https://arxiv.org/pdf/2608.13574v2"]
> - **Harness Engineering via Reusable Tool Primitives（arXiv 2609.01736，09-01）**：agent 原生**可复用工具原语**降低 harness 工程成本["https://arxiv.org/abs/2609.01736"]
> - **含义**：① **"harness 自我演化"成为 harness 领域研究新前沿**（生成/训练/演化三维）——与 DeepSeek harness（dsh）、HarnessDev（字节）直接同线，我的"自研 harness + 验证编译器"路线获得学术侧强印证；② **HarnessDev 作为基准**可用来评估"我的 harness 能否被模型重写"——dsh-pentest 可把 JIT-Agent/HarnessDev 作为验证对象；③ AgentAO 的"策略治理 + 事件接口"与 agent-firewall 卡"策略→执行"主线互证——harness 层治理显式化成为共识
> **雷达增量（2026-09-30，托管 harness GA + agent 生命周期治理）**：
> - **AWS Bedrock AgentCore Harness 全面 GA（09-17 release notes）**：托管 harness——**CreateHarness/InvokeHarness 无编排代码无容器**；GA 默认内置记忆（可自带）、更多模型提供方（LiteLLM/Bedrock Mantle，解锁 GPT-5.5）；**09-29 再更新：MCP 工具结果元数据流式返回**["https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/release-notes.html"]
> - **Harness（公司）Agent DLC + Autonomous Worker Agents（06-30/07-31 shipped）**：agent **全生命周期平台**（build/test/store/deploy/operate/govern + AIBOM 物料清单）——pipeline 每步可跑 reasoning agent（scoped credentials + OPA policy + approval gates + audit trails，与人工部署同级治理）["https://www.harness.io/blog?sck=1778014584698_17780141792434"]["https://www.harness.io/blog/shipped-in-june-2026"]
> - **Tencent Cloud"从 Harness 到自进化 Agent"（09-20 方法论文）**：Phase 3 自进化 Harness 时代——代表 Hermes Agent（自动复盘/自动沉淀经验/自动改进，"你纠正一次它永远记住"）——与 09-24 卡内 HarnessDev/自演化线互证["https://cloud.tencent.com/developer/article/2747237"]
> - **含义**：① **"托管 harness 即服务"主流化**（AgentCore GA = 无编排代码跑 agent）——自研 harness（dsh/DeepSeek）与托管路线的竞争/互补格局成形，silver-shield 评测 harness 可对照 AgentCore 的"内置记忆+多模型"设计；② **agent 生命周期治理产品化**（Agent DLC/Worker Agents + AIBOM）——"agent 安全"从运行时防护扩展到**全生命周期治理管道**（与 skill-supply-chain 卡的 AIBOM/物料清单互证、EP-002 权限边界获得企业级参考实现）；③ 自进化 harness 从研究（JIT-Agent/HarnessDev）走向方法论共识（Tencent Phase 3）——dsh 的 harness 迭代路线再获外部印证
> **雷达增量（2026-10-05，GPU 厂商进安全基础设施 + 控制平面×成本路由）**：
> - **NVIDIA Open Agent Safety Platform（09-28 发布）**：**open shell** 提供**模型与 agent harness 之外的强制安全运行时边界**——定位"agent 不应自我监管，控制必须外置"；打包进 AI factory（sandbox/DPU/attestation/audit logs/runtime permissions 成"工业安全护栏"）——**GPU 硬件厂商把 agent 安全做成基础设施层**["https://nvidianews.nvidia.com/news/open-agent-safety-platform"]["https://technology.siften.com/nvidia-pitches-agent-safety-as-infrastructure-not-just-model-behavior-1790644471297"]
> - **Harness Tokenomics（arXiv 2609.28919）**：**企业 agentic control plane 路由器**——Jev 分类器给每个 prompt 打标（自带 taxonomy）+ **定价驱动路由**（session start/side lanes/subagent launch 三处路由，按价格表计算 mid-task 切换回报）——控制平面加入"成本路由"维度["https://arxiv.org/pdf/2609.28919.pdf"]
> - **Harness（公司）AI Worker Agents 身份权限（07-16）**：agent 即 pipeline step——**RBAC/OPA 治理继承**（who 可建 + policy 允许什么，控制台/API/agent 同一决策，服务端强制非 UI 假设）["https://www.harness.io/blog/identity-and-permissions-for-ai-worker-agents-in-harness"]
> - **含义**：① **"控制外置"成硬件级共识**——NVIDIA open shell 与 OWASP agentic/RAMPART"harness 外边界"完全同构，但下沉到 GPU/DPU 层——silver-shield 若做硬件侧 agent 防护可跟踪 NVIDIA 实现；② **控制平面从"策略/审计"扩到"成本路由"**（Tokenomics）——"agent 每步调用都计费+可路由"与 AP2/A2A 经济层呼应，"agent 经济学"成型；③ **权限"服务端强制 + 单一决策源"**（Harness）是 EP-002 的企业级参考——自研权限系统应避免"UI 层校验"，把决策收敛到统一策略引擎

## 4. 验证计划
- [ ] 精读六职责分解论文，与我五维模型做逐项对照（产出对照卡）
- [ ] 跑 Omnigent quickstart，评估"组合 Claude Code + Codex"对我的实际工作流价值
- [ ] 评估 TeamMind 架构迁移到 meta-harness 模式的成本/收益

## 5. 决策
- [ ] 晋升 validated
- [x] 维持观察（待六职责对照卡）
- [ ] 拒绝
