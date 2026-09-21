# 候选证据卡 · [cand] Agent 防火墙 / 运行时防御品类（Aigis + ClawKeeper + AgentGuard + Pipelock）
> 状态：`[cand]` ｜ 分类：AI 安全防御侧 / Agent 运行时治理（G1） ｜ 发现：2026-09-11（雷达 #10） ｜ 等级：**A**
## 一句话定位
2026-09 一周内"Agent 防火墙/运行时防御"品类密集涌现：**Aigis**（确定性零依赖 Python 防火墙：MCP rug-pull/memory poisoning/indirect injection/exfil 检测 + 44 合规模板）、智源 **ClawKeeper v1.0**（Skill/Plugin/Watcher 三位一体，面向 OpenClaw 全生命周期）、**AgentGuard**（Prompt/Tool/Command 三层运行时防火墙）、**Pipelock v3.5**（扫描 HTTP/MCP/A2A/WebSocket 流量 + 可验证签名 receipts）——Agent 安全从"检测工具"走向"运行时治理层"。
## 1. 它是什么 / 解决什么问题
- 痛点：Agent 工具调用/文件写入/代码执行/agent 互信缺运行时监管——一次 prompt injection 即数据外泄；chatbot 时代的"文本过滤"已不够["https://github.com/gaebalai/aigis-kr"]
- **Aigis（pyaigis v1.1.11，Apache-2.0，零运行时依赖）**：每次工具调用的确定性 guardrail + 防篡改审计日志 + 生成的 IT 审批包；覆盖 MCP rug-pull、记忆投毒、间接注入、外泄通道；内置**事件生命周期管理**（威胁自动建 incident + 全时间线）；44 合规模板（US/CN/JP/EU）["https://github.com/gaebalai/aigis-kr"]["https://pypi.org/project/pyaigis/"]
- **ClawKeeper v1.0（智源 + 北邮 + 信通院，2026-09）**：面向 OpenClaw 的实时安全框架，**Skill/Plugin/Watcher 三位一体**防御架构，覆盖 agent 全生命周期，适配局域网 agent 集群监控["https://blog.csdn.net/FENGQIYUNRAN/article/details/161616195"]
- **AgentGuard（0xrem）**：桌面/开发机 AI Agent 运行时防火墙——Prompt Guard（输入/检索/工具参数：warn/mask/block/ask）+ Tool Guard（文件/浏览器/HTTP/DB/邮件：allow/deny/ask/sandbox）+ Command Guard（shell：suspend/block/confirm/kill）["https://github.com/0xrem/agentguard"]
- **Pipelock v3.5.0（2026-09-01）**：开源 AI agent 防火墙，扫描 HTTP/MCP/A2A/WebSocket 流量防外泄/SSRF/prompt injection，**可验证签名 action receipts** 供审计["https://kitploit.com/en/posts/github-luckypipewrench-pipelock-v350"]
- 同线：Agent Guard（Avveerayy，运行时治理层）、NeuralGuard（FastAPI 中间件）、LlamaFirewall（arXiv 2505.03574，open source guardrail 框架）["https://github.com/Aveerayy/agent-guard"]["https://arxiv.org/pdf/2505.03574"]
> **雷达增量（2026-09-12，品类持续爆炸）**：
> - **OWASP Agent Memory Guard（OWASP 官方 Incubator，2026-08-30 页面）**：**ASI06 Memory Poisoning 的参考实现**（OWASP Top 10 for Agentic Applications 该风险项此前缺实现）——SHA-256 密码学基线验证记忆完整性、检测注入/敏感泄漏/关键键修改/突变/大小异常、YAML 声明式安全策略、快照取证 + 回滚到已知良好态、drop-in 中间件（LangChain/LlamaIndex/CrewAI）；被 MITRE ATLAS "Memory Hardening" 缓解项引用——**与已覆盖的 OWASP Agentic Security（S）+ Agent Memory（S）形成官方项目级闭环**["https://owasp.org/www-project-agent-memory-guard/"]
> - **Guardian（LegionForge，2026-09-10）**：FastAPI sidecar，工具调用前 7 项**确定性检查**（Task token ACL / 模式匹配 / 哈希校验 / 密码学验证）——"No LLM. No heuristics. decisions that cannot be prompt-injected"["https://github.com/LegionForge/guardian"]
> - **AI Protector（szesnasty，09-02）**：确定性安全运行时（~50ms 全本地），"provable"——Benchmark Hub 度量 + runtime 执行 + 证明
> - **Agent Shield（cdayAI，09-03）**：npm SDK（agentshield-sdk），40+ 威胁类别零依赖本地检测
> - **InjectShield（09-04）/ llm-injection-guard（09-02）**：启发式规则库 REST API / Python 实时注入检测库
> - **含义**：① 品类从"4 个代表项目"扩张为"10+ 项目生态"，确定性（无 LLM 判定）、密码学验证、可证明（provable）成为共同主线——**Aigis/Guardian/AI Protector 三选一实测**应尽快排期；② OWASP 官方下场做 Memory Poisoning 参考实现，说明 Agent 安全正式进入标准治理层；③ silver-shield 的"记忆/状态完整性"防线可直接采用 SHA-256 基线 + 回滚模式["https://github.com/szesnasty/ai-protector"]["https://github.com/cdayAI/Agent-Shield"]["https://github.com/maheshmakvana/llm-injection-guard"]
> **雷达增量（2026-09-14，品类商业化）**：**天融信获国内首批《人工智能防火墙产品测评》证书（09-13）**——提示词注入防护覆盖 DAN 越狱/模型劫持/角色扮演等数十种手法（直接+间接注入）、OCR 识别图片/文档隐藏指令、敏感数据双向检测脱敏、Token 消耗阈值风控——Agent 防火墙品类进入**商用合规产品化**阶段["http://m.toutiao.com/group/7684990768863363593/"]
> **雷达增量（2026-09-15，重量级方案 + 可证明路线）**：
> - **Microsoft Agent Governance Toolkit（2026-04-02 开源，MIT，7 包 monorepo，Python/TS/Rust/Go/.NET）**：**"Agent OS"无状态策略引擎**（拦截每个 agent 动作，<0.1ms p99，支持 YAML/OPA Rego/Cedar 三种策略语言）+ Agent Mesh（DID+Ed25519 密码学身份、Inter-Agent Trust Protocol、0-1000 动态信任评分）+ Agent Runtime（CPU 特权级启发的执行环 + saga 编排 + kill switch）+ Agent SRE（SLO/熔断/混沌工程）+ Agent Compliance（EU AI Act/HIPAA/SOC2 映射 + OWASP 10 证据收集）+ Agent Marketplace（插件 Ed25519 签名 + 供应链）+ Agent Lightning（RL 训练治理）；**覆盖全部 10 项 OWASP Agentic AI 风险**（Memory poisoning→Cross-Model Verification Kernel 多数投票；Goal hijacking→语义意图分类器）；框架无关（LangChain/CrewAI/ADK/Dify/LlamaIndex/OpenAI Agents SDK/Haystack/LangGraph/PydanticAI 集成）；9500+ 测试/SLSA/Scorecard；**配套 Agent Control Specification（ACS）开放规范**——在 agent 工作流 checkpoints 放置确定性安全控制的便携标准["https://opensource.microsoft.com/blog/2026/04/02/introducing-the-agent-governance-toolkit-open-source-runtime-security-for-ai-agents/"]["https://devblogs.microsoft.com/foundry/build-2026-open-trust-stack-ai-agents/"]
> - **Proof-of-Guardrail（arXiv 2603.05786，ICML'26 AI4GOOD Workshop，v2 2026-06-26）**：解决"开发者谎称有安全措施"的信任问题——agent+guardrail 在 **TEE 中运行**，产生 TEE 签名的 attestation 证明 guardrail 确实执行过（用户离线可验证）；**已实现于 OpenClaw agents**；同时揭示信任边界（恶意开发者可主动 jailbreak guardrail）["https://arxiv.org/abs/2603.05786"]
> - **含义**：① 微软把"OS 内核/服务网格/SRE"成熟模式整体移植到 agent 治理（Agent OS/Mesh/SRE 命名即意图），是品类中的**重量级完整方案**（对比 Aigis 等轻量单包）——**Aigis/Guardian/AI Protector/Agent Governance Toolkit 四选实测**需重新评估权重；② **ACS 开放规范**与 OWASP/Skills Top10 同属标准层，是"确定性控制 checkpoint"的行业标准候选；③ **Proof-of-Guardrail 的 TEE attestation**把"provable"从软件承诺升级为**硬件可信根证明**，且**直接落地 OpenClaw**（campus_order 栈）——silver-shield 若做"安全声明可验证"可作为路线；④ 微软官方下场 + 框架无关集成，说明"运行时治理层"正式成为大厂主航道
> **雷达增量（2026-09-22，端点 AIDR 新品类——主流 EDR 入场）**：
> - **CrowdStrike Falcon Guardian（09-01 Fal.Con 发布，GA + 09-03 OpenAI Codex 集成）**：**AI Detection and Response（AIDR）平台**——在**端点运行时**检测对 agent 的攻击与恶意 agent 行为、执行强制；典型场景：coding agent 用你的凭据调 API/发 Slack/查数据库时被监控拦截——**主流 EDR 厂商首次把 agent 运行时安全做成端点产品**["https://byteiota.com/crowdstrike-falcon-guardian-ai-agent-runtime-security-arrives/"]["https://www.barchart.com/story/news/4381249/crowdstrike-unveils-falcon-guardian-to-secure-ai-agents-where-they-execute-on-the-endpoint-at-runtime"]
> - **Microsoft Defender for Endpoint AI Agent Runtime Protection（preview，09-16）**：本地 AI agent（coding 助手/CLI/桌面 AI/自主 agent 平台）端点运行时保护——agent 以用户权限运行、处理不可信文本即风险面["https://learn.microsoft.com/ko-kr/defender-endpoint/ai-agent-runtime-protection-overview"]
> - **Arcjet Runtime Security for AI Agents（09-17/18）**：agent 行为监控/控制 + **执行记录**（供安全合规审查）；策略决策先于受保护动作（block 或转人工批准）；usage limits/自动化检测/prompt injection 筛查["https://securitytoday.com/articles/2026/09/18/arcjet-launches-runtime-security-product-for-ai-agents.aspx?admgarea=ht.government"]
> - **F5 AI Guardrails × MuleSoft Agent Fabric（09-02 GA）**：Salesforce Agentforce 栈内联安全层（prompt/模型响应/agentic workflow 运行时拦截）["https://www.martechnotes.com/f5-brings-ai-guardrails-to-mulesoft-agent-fabric-for-salesforce-agent-security/"]
> - **含义**：① **"端点 AIDR"成为新品类**——EDR 厂商把"agent 以用户权限运行"识别为主风险面（对照 MS AGT 的服务端治理），**运行时强制从 API 网关层延伸到端点执行层**——与 PaperCut/Glasswing 的"agent 自主行动"威胁叙事直接对位；② CrowdStrike Codex 集成 = coding agent 主战场（dsh 同类栈可直接参照其检测项设计）；③ silver-shield 的防线设计获得"端点执行监控"这一新参照层（行为基线 + 凭据使用审计）
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-11）**：Aigis GitHub/PyPI ✅、ClawKeeper 多源报道 ✅、AgentGuard GitHub ✅、Pipelock release ✅
- 时间密集：09-01 Pipelock → 09-02 AgentGuard → 09-04 ClawKeeper/Aigis PyPI → 09-05 Aigis 更新——一周内至少 4 个独立项目发布，品类成形信号
- 与 Agentic Attack（09-09 S 级）同一安全叙事的两面：攻击链 agent 化 → 防御必须运行时化
## 3. 与我的连接
- **连接的项目**：**silver-shield**（防诈骗/风险检测——Aigis 的确定性 guardrail + 事件生命周期可直接借鉴）；**EP-002**（Permission Is Security Boundary——AgentGuard 的 Tool/Command Guard 正是"权限边界"的工程实现）；**campus_order**（OpenClaw——ClawKeeper 直接针对 OpenClaw）；**TeamMind**（工具调用治理层参考）；dsh-pentest（可攻击测试这些防火墙）
- **连接的知识点**：AI 安全攻防（G1）、Agent 运行时治理、Skill 供应链安全（S 级卡同线）
- **潜在收益**：silver-shield 可评估引入 Aigis 类确定性 guardrail 作为防线；为 TeamMind 提供"运行时防火墙"选型池
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/gaebalai/aigis-kr ｜ https://blog.csdn.net/FENGQIYUNRAN/article/details/161616195 ｜ https://github.com/0xrem/agentguard ｜ https://kitploit.com/en/posts/github-luckypipewrench-pipelock-v350 |
| 证据等级 | **FACT（GitHub/PyPI + 多源报道核验通过）** |
| 验证方式 | 装 Aigis 对一个 agent 工具调用链跑确定性 guardrail → 对照 silver-shield 防线设计 → 评估 AgentGuard 三层模型是否入 TeamMind 工具治理 |
| 预期完成时间 | 2026-09/10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
