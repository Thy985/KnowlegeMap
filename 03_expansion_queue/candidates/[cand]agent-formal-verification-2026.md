# 候选证据卡 · [cand] Agent 形式化验证 / 可证明 Guardrail（AWS Dogwood + Lean4Agent + ePCA + AProver）
> 状态：`[cand]` ｜ 分类：形式化验证 × Agent（G5 战略级） ｜ 发现：2026-09-08（雷达 #7） ｜ 等级：**A**
## 一句话定位
2026 年"给 Agent 加数学保证"从学术设想变为可运行工具：**AWS Dogwood**（2026-08-06 开源的 agent 运行时验证治理语言，接替 AgentCore Policy 的 Cedar）、**Lean4Agent**（Lean 4 依赖类型验证 agent 工作流与执行轨迹）、**ePCA**（中科大"可证明安全 Agent Guardrail"，arXiv 2605.29251，用执行证明约束动作）、**AProver/BMC-Agent**（LLM agent + bounded model checking 验证 AI 生成代码）——"验证编译器"路线在形式化侧出现工业级落点。
## 1. 它是什么 / 解决什么问题
- 痛点：现有 agent guardrail 是语义级启发式（prompt 检查），无法给出"动作必然合规"的保证；形式化验证过去只用于专家手工写的协议["https://www.llm-hacking.com/hacks/provably-secure-agent-guardrail-epca.md/"]
- **AWS Dogwood**：为 agent 和工具设计的开源治理语言——每次工具调用前判定动作是否允许，替代/演进 AgentCore Policy 的 Cedar 策略层；运行时验证（runtime verification）定位["https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/"]
- **Lean4Agent**（Wang et al., 2026-06）：首个用 Lean 4 依赖类型系统形式化建模并验证 agent 工作流/执行轨迹的框架；验证通过的工作流显著优于失败对照["https://codex.danielvaughan.com/2026/07/11/lean4agent-formal-verification-agent-workflows-codex-cli-pre-post-conditions-typed-guardrails/"]
- **ePCA（Executable Proof-Constrained Action）**：每个待执行动作视为数学猜想，仅当 Lean 4 内核证明其满足预编译法规公理才放行（金融场景已映射 SEC 15c3-5/FINRA 3110）["https://arxiv.org/html/2604.01483"]
- **AProver BMC-Agent**：LLM agent（生成 spec/分类反例/精化 spec）+ 可靠的 bounded model checking 后端——agent 处理语义推理、solver 提供界内形式保证["https://github.com/agentic-prover/aprover"]
- 同线：Google CEL 形式化验证框架（Z3 定理证明防 policy 代码缺陷，2026-08-18）、VCG（Dafny 证书的 Python 生成）、QWED（Z3/SMT 确定性验证层）["https://www.opensourceforu.com/2026/08/google-open-source-framework-cel/"]["https://www.emergence.ai/blog/vcg-a-high-performance-verified-coding-agent-for-python"]
## 2. 为什么现在值得关注（活跃度证据）
- **一手核验（2026-09-08）**：AWS 官方博客 Dogwood ✅、AProver GitHub ✅（2026-09-03 活跃）、arXiv 2604.01483 ✅（Lean-Agent Protocol）
- 工业界三巨头同月动作：AWS（Dogwood 开源）、Google（CEL 形式化框架）、MS/OpenAI（Lean 生态）——形式化验证进入 agent 安全主流叙事
- 2026 已形成"声明侧（SkillFortify 静态）+ 运行时侧（Dogwood/ePCA）+ 代码侧（AProver/VCG）"三段式可证明安全雏形
## 3. 与我的连接
- **连接的项目**：**Validation 编译器**（Claim→Operationalization→Evidence→Judgment 的"形式化侧补全"——Lean 类型/证明内核就是 Evidence 的机器可核验形态）；**EP-002**（Permission Is Security Boundary——Dogwood 正是"策略即代码、调用前判定"的工程化）；**TeamMind**（agent 行为门控）；**silver-shield**（防诈骗 guardrail 可证明化）
- **连接的知识点**：形式化验证（G5 战略）、验证编译器体系、AI 安全（G1）
- **潜在收益**：给 Validation 编译器补上"机器可核验证据"层级；Dogwood 可作为 TeamMind 工具调用策略层的开源参考实现
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://aws.amazon.com/blogs/opensource/introducing-dogwood-runtime-verification-for-ai-agents/ ｜ https://codex.danielvaughan.com/2026/07/11/lean4agent-formal-verification-agent-workflows-codex-cli-pre-post-conditions-typed-guardrails/ ｜ https://arxiv.org/html/2604.01483 ｜ https://github.com/agentic-prover/aprover |
| 证据等级 | **FACT（AWS 官方 + arXiv + GitHub 核验通过）** |
| 验证方式 | 读 Dogwood 规范 → 对 TeamMind 的一个高风险工具调用写策略 → 对照 ePCA 证明约束思路 → 评估并入 Validation 编译器的证据层 |
| 预期完成时间 | 2026-09/10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
