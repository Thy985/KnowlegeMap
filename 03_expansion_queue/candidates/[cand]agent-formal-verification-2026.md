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
> **雷达增量（2026-09-17，工程实践 + 能力缺口量化）**：
> - **NVIDIA OpenShell（2026-09-10）**：用 **Z3 SMT 对 agent 策略做形式化**——ports 映射整数、hosts/paths 映射字符串、globs 映射正则、策略组合映射布尔逻辑，再交给 Z3 证明——与 Google CEL/AWS Cedar 同线的工程化实践["https://nvidia.github.io/OpenShell-Research/dev-notes/posts/2026-09-10-learning-formal-methods-agent-policy-prover/"]
> - **Vero benchmark（2026-08-13 发布，09-16 深度分析）**：**首个系统性衡量"frontier coding agents 能否在仓库规模同时产出实现 + 机器检查证明"**的基准（43 实例）——最强配置仅解 27 个、最具挑战代码库上完成 0 规格——"agent 驱动可验证软件合成"能力缺口被量化（与 agentic-benchmarks 卡交叉）["https://codex.danielvaughan.com/2026/08/14/vero-benchmark-formally-verified-software-repositories-coding-agents-codex-cli-proof-synthesis-posttooluse-verification/"]
> - **NabaOS（arXiv 2603.10060，09-16 更新）**：轻量验证框架——**HMAC 签名的工具执行 receipts（LLM 无法伪造）** + 认识论来源分类（pramāṇa：直接工具输出/推理/外部证言/缺失/无根据观点），逐句判定幻觉归属——与 trace-based eval 的"行为证据"范式呼应["https://arxiv.org/html/2603.10060"]
> - **Verus 路线（PAgE 2026 keynote，09-08）**：LLM agent 随代码发形式证明、由 **Verus（SMT-based Rust verifier）** 验证——仓库级系统代码上"frontier-model-gated yes"；但**规格仍是可信头（TCB）**，agent 只提供证明不提供规格["https://wal.sh/events/pldi-2026/page-2026/keynote-shan-lu/"]
> - **含义**：① 形式化验证从"语言/框架"进入"策略验证工程"（NVIDIA Z3 实践）——TeamMind 工具策略可先做 Z3 可解建模；② **Vero 量化缺口**说明 agent 自动证明仍是开放问题，但"验证钩子（verification hooks）"已成 codex 等 CLI 标配；③ **NabaOS 的不可伪造 receipts**是"机器可核验证据"的轻量形态——Validation 编译器证据层可参考（成本远低于 Lean 内核证明）
> **雷达增量（2026-09-26，验证方法论扩展 + 评测基础设施形式化）**：
> - **Harnessing Code Agents for Automatic Software Verification（arXiv 2607.06341）**：**"脚手架不必要"**——Claude Code/Codex 等通用代码 agent 直接整条 lemma 级证明，优于窄角色（predict a tactic/fill a slot）系统——"agent 自由规划证明路径"比限定角色更有效["https://arxiv.org/html/2607.06341"]
> - **Event-B Agent（arXiv 2605.17475）**：**LLM agent 综合+修复 Event-B 形式化模型**——自然语言需求→初始模型→用形式验证反馈迭代修复/精化（refinement 简化证明、修复保证每一步健全）["https://arxiv.org/html/2605.17475"]
> - **BenchShield（2026-09-10）**：**formal model-backed instrumentation 保护 LLM-agent 评测基础设施的奖励完整性**——把形式化模型引入 agent 评测，防 reward hacking（与 SWE-Bench Pro Verified 反 reward hacking 同线的形式化解法）["https://www.semanticscholar.org/paper/BenchShield:-Formal-Model-Backed-Instrumentation-in-Zheng-Di/aa6f64210fa8817ed5925f21a96d6daf0e3b2e3f"]
> - **Toward Safe LLM Agents Survey（arXiv 2608.14590）**：**specification/verification/enforcement 三阶段综述**——GRADE 表系统盘点 AgentProof/DafnyPro/VeriGuard 等"pre-action verified generation"路线的成熟度（多数 Very Low——领域仍早期）["https://arxiv.org/html/2608.14590v1"]
> - **含义**：① 方法论翻转——**"通用 agent 自由规划证明 > 窄角色脚手架"**（2607.06341）直接验证 dsh"通用 harness 驱动"路线的正确性；② **评测基础设施本身成为形式化对象**（BenchShield）——与 agentic-benchmarks 卡互证，Vero 缺口 + Survey 的"Very Low"成熟度 = 领域早期但方向确立；③ Event-B 的"验证反馈驱动模型修复"循环与 Validation 编译器"Evidence→Judgment→修正"闭环同构——形式化侧的实现参考再添一个
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
