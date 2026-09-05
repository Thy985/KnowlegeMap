# 06 · Expansion Index（外部知识扩展索引）

> 本索引维护每一次"外部世界新发现"的完整记录，回答：**第一次发现时间 / 来源 / 分类 / 与我的项目关系 / 当前状态 / 优先级 / 是否已深入研究 / 是否已实际验证**。
> 用途：全仓去重（避免重复收集同一对象）、追踪每条线索的生命周期、为后续自动探索提供去重基准。

## 状态定义
- `[cand]` 候选卡已建，未完成真机验证
- `[validated]` 已晋升（≥2 条独立证据 + 一次真机验证）
- `[dropped]` 已评估并放弃
- `[observe]` 仅观察，暂不投入

## 2026-09-01 首轮定向扫描（MCP + Evals）
| 对象 | 首次发现 | 来源 | 分类 | 项目关系 | 状态 | 优先级 | 已深入 | 已验证 |
|---|---|---|---|---|---|---|---|---|
| MCP 2026-07-28 无状态协议 | 2026-09-01 | 官方博客/Spec | MCP 生态 | Tafcm/agent-attention/TeamMind/OpenClaw | [cand] | S | 部分 | 未 |
| MCP 通知类 Server | 2026-09-01 | GitHub | MCP 生态 | agent-attention（同域） | [cand] | S | 部分 | 未 |
| promptfoo | 2026-09-01 | 官方文档+实测 | Agent Evals | Tafcm ADI / silver-shield | [cand] | S | 是 | ✅ 本机 eval 2/2 PASS |
| Evals 框架格局 | 2026-09-01 | 2026 横向评测 | Agent Evals | Tafcm/silver-shield/dsh-pentest | [cand] | A | 是 | 未 |

## 2026-09-01 External Knowledge Expansion 扫描
| 对象 | 首次发现 | 来源 | 分类 | 项目关系 | 状态 | 优先级 | 已深入 | 已验证 |
|---|---|---|---|---|---|---|---|---|
| OWASP Agentic Security 体系 | 2026-09-01 | OWASP 官方 | AI 安全治理（G1） | dsh-pentest/silver-shield/EP-002 | [cand] | **S** | 否 | 未 |
| A2A 协议 v1.0 + AAIF | 2026-09-01 | Linux Foundation/A2A 官网 | 多 Agent/互操作 | TeamMind（协议层） | [cand] | **S** | 否 | 未 |
| Agent Harness/Control Plane 范式 | 2026-09-01 | Databricks/MS/arXiv | Runtime/Harness | TeamMind/五维模型/验证编译器 | [cand] | **S** | 否 | 未 |
| Agent Memory 2026 实现层 | 2026-09-01 | Mem0/Zep/Letta/MemEval | Agent Memory | GrowthOS/TeamMind/Validation | [cand] | **S** | 部分 | 未 |
| AI 攻防工具链 | 2026-09-01 | 官方仓库+评测 | AI 攻防（G1） | dsh-pentest/silver-shield | [cand] | A | 否 | 未 |
| Computer/Browser Use GA | 2026-09-01 | Claude 官方/browser-use | Computer Use | campus_order/E2E-CLI/agent-attention | [cand] | A | 否 | 未 |
| E2B 沙箱 + APP | 2026-09-01 | E2B 官方 | 代码沙箱 | TeamMind/EP-002/dsh-pentest | [cand] | A | 否 | 未 |
| OTel GenAI 可观测标准 | 2026-09-01 | OTel/Langfuse 官方 | LLM 可观测 | Tafcm ADI/silver-shield | [cand] | A | 否 | 未 |
| Agentic 基准 2026 批判 | 2026-09-01 | 2026 评测/OpenAI | Agent 基准 | Validation/silver-shield | [cand] | A | 否 | 未 |
| 本地/边缘 LLM 推理 | 2026-09-01 | arXiv/官方文档 | 本地/边缘 AI | Tafcm/silver-shield | [cand] | A | 否 | 未 |
| 开源 Agentic CI | 2026-09-01 | InfoQ/评测 | Agentic CI | AI Code Review 资产族/Tafcm | [cand] | B | 否 | 未 |
| Fine-tuning 对齐新范式 | 2026-09-01 | arXiv/GitHub | Fine-tuning | ML 方法论/silver-shield | [cand] | B | 否 | 未 |
| Multi-Agent 框架终局 | 2026-09-01 | 2026 对比 | 多 Agent 编排 | TeamMind | [cand] | B | 否 | 未 |
## 2026-09-02 Personal Tech Radar 首次扫描（每日 External Knowledge Watch）
| 对象 | 首次发现 | 来源 | 分类 | 项目关系 | 状态 | 优先级 | 已深入 | 已验证 |
|---|---|---|---|---|---|---|---|---|
| DeepSeek Harness v0.1 | 2026-09-02 | DeepSeek 开源 | Harness/Runtime（S5） | TeamMind（同构对照） | **[validated]** | **S** | **是（架构精读）** | ✅ clone+对照 2026-09-02 |
| Flutter 本地 LLM 工具链（ai_edge/flutter_gemma/Llamafu） | 2026-09-02 | pub.dev/GitHub | 本地/边缘 AI（G3） | **Tafcm**（离线能力） | [cand] | A | 否 | 未 |
| Browser Harness（browser-use 生态） | 2026-09-02 | GitHub/PyPI | Computer Use（S5） | campus_order/E2E-CLI/agent-attention | [cand] | A | 否 | 未 |
| MS Research Webwright | 2026-09-02 | MS Research | Computer Use / Web Agent | E2E-CLI/campus_order | [cand] | B | 否 | 未（一手来源已核验 FACT） |
| hermes-agent（Nous Research） | 2026-09-02 | GitHub/ClawBench | Agent Framework | OpenClaw 对照 | [cand] | B | 否 | 未（一手来源已核验 FACT，★修正 ~57k→~217k） |
> **雷达增量（Changed，2026-09-02）**：MCP（final 后新 Roadmap 2026-08-22 + go-sdk Stateless 发布）、A2A（08-17/18 正式移交 AAIF + MS .NET 接 A2A v1）、OWASP（新增 Red Teaming Solutions Landscape + Red Teaming Taxonomy + Skills B1-B4 Trust Boundary Model）、Agent Memory（Mem0 SDK 2.0 + Platform v3 时间感知 + Letta Agents SDK/Mods）。以上 4 条已在原候选卡内追加雷达增量记录，不新建卡。
## 2026-09-03 Personal Tech Radar 第 2 次扫描（每日 External Knowledge Watch）
| 对象 | 首次发现 | 来源 | 分类 | 项目关系 | 状态 | 优先级 | 已深入 | 已验证 |
|---|---|---|---|---|---|---|---|---|
| Microsoft RAMPART + Clarity | 2026-09-03 | MS Security Blog/GitHub | AI 安全攻防（G1） | dsh-pentest/silver-shield/E2E-CLI | [cand] | **S** | 否 | 未（一手来源已核验 FACT） |
| PI-Hunter 注入审计线（+ARGUS/PISmith/SoK） | 2026-09-03 | arXiv | AI 安全攻防 / 注入审计（G1） | dsh-pentest/TeamMind/Validation | [cand] | A | 否 | 未（arXiv 全文可读 FACT） |
> **雷达增量（Changed，2026-09-03）**：hermes-agent（v0.20.x 系列：The Herald 08-03 + v0.20.3 08-16 稳定 rollup ~125 PRs + 新增 Native Windows/DeepSeek V4/AI 视频生成）、Flutter 本地 LLM（**flutter_litert_lm**：Android 端 LiteRT-LM 已取代 MediaPipe LLM Inference + llx_flutter/flutter_native_ai/Flutter Local AI 新插件）。已在原候选卡内追加增量记录，不新建卡。
## 2026-09-04 Personal Tech Radar 第 3 次扫描（每日 External Knowledge Watch）
| 对象 | 首次发现 | 来源 | 分类 | 项目关系 | 状态 | 优先级 | 已深入 | 已验证 |
|---|---|---|---|---|---|---|---|---|
| Agentic CLEAR（IBM，arXiv 2605.22608） | 2026-09-04 | arXiv / ibm.github.io | Agent Evaluation / 评估方法论（G2） | silver-shield Benchmark / Tafcm ADI / Validation | [cand] | A | 否 | 未（arXiv+官方页核验 FACT） |
> **雷达增量（Changed，2026-09-04）**：Agent Memory（**Mem0 v3.0 新记忆算法** LoCoMo +20/LongMemEval +26、3-4x 低成本；**分数可信度批判** Zep LoCoMo 84%→58% 更正、Mem0 平台分 vs SDK 分；Letta Context Constitution + Context Repositories；Zep DMR 94.8% 自报；Supermemory MCP 原生）、LLM 可观测（**OTel GenAI 语义约定已稳定** 2025 末 + 阿里 LoongSuite 零代码采集 + Iris 观察不建卡）。已在原候选卡内追加增量记录，不新建卡。
## 2026-09-05 Personal Tech Radar 第 4 次扫描（每日 External Knowledge Watch）
| 对象 | 首次发现 | 来源 | 分类 | 项目关系 | 状态 | 优先级 | 已深入 | 已验证 |
|---|---|---|---|---|---|---|---|---|
| Agent Skill 供应链安全（SkillFortify 形式化验证 + Unit 42 BIV 实证） | 2026-09-05 | arXiv 2603.00195 / unit42.paloaltonetworks.com | AI 安全攻防 / Agent 供应链（G1） | **EP-002** / campus_order（OpenClaw）/ dsh-pentest | [cand] | **S** | 否 | 未（arXiv+官方报告核验 FACT） |
| Agentic GraphRAG 2026（MemGraphRAG / Graph-R1 / A-RAG） | 2026-09-05 | GitHub / arXiv 2606.00610 / OpenReview | RAG 系统化（G2） | GrowthOS / TeamMind / silver-shield | [cand] | A | 否 | 未（GitHub+arXiv 核验 FACT） |
> 说明：MCP 侧 2026-09-05 仅确认 SDK 落地执行（rust 3.0 beta / C# v2 / go v1.7 / Cloudflare 采用 2026-07-28 stateless），属已知对象执行确认，无新范式，不记录为新条目。
## 2026-09-06 Personal Tech Radar 第 5 次扫描（每日 External Knowledge Watch）
| 对象 | 首次发现 | 来源 | 分类 | 项目关系 | 状态 | 优先级 | 已深入 | 已验证 |
|---|---|---|---|---|---|---|---|---|
| Agentic UX / AI 原生产品设计模式（Agentic Design / 五级自主度 / Smashing 六模式 / zylos 四层栈） | 2026-09-06 | agentic-design.ai / aiuxplayground / smashingmagazine / zylos | AI 原生产品 / Agentic UX（G2 空白区） | TeamMind / campus_order / agent-attention / Tafcm | [cand] | B | 否 | 未（设计社区一手来源多站交叉 FACT） |
> **雷达增量（Changed，2026-09-06）**：Agent Framework（**OpenClaw 2.0** v2026.8.1 史上最大更新：933 贡献者/16k+ PR、简化安装、重建浏览器 App、multiplayer sessions、新安全控制，社区对比"用户转投 Hermes"）、Agent Skill 供应链（**NVIDIA SkillSpector** 同域扫描器 + **CHAINDROP** 后门 400+ npm 包 13 亿月下载 + **Tenable AI Inspector** + **AI Agent Firewall 品类**/LLM 防火墙批判）、AI 攻防（**Agent Threat Rules** 威胁规则库 + **OpenAI 智能体劫持德国网站事件** + awesome-agent-skills-security 清单）。已在原候选卡内追加增量记录，不新建卡。

## 去重基准（扫描前先查这里）
已覆盖对象清单：MCP（2026-07-28/通知 server/Registry）、promptfoo/DeepEval/OpenAI Evals/Inspect/Ragas/Langfuse（选型）、OWASP Agentic Top10/Skills Top10、A2A、Omnigent/MS Agent Framework、Mem0/Zep/Letta/A-MEM/MemEval、Garak/PyRIT/PentestGPT/PentAGI/ATLAS/HarmBench、Claude browser/computer use/browser-use、E2B、OTel GenAI、Agentic 基准族、LlamaWeb/MLC-LLM/BitNet/TinyLLM、Pullfrog/OpenCodeReview、DPO/ORPO/KTO、LangGraph/CrewAI/AG2/Mastra、Agentic CLEAR/AgentEval、Mem0 v3/Letta Context Constitution/Zep DMR、RAMPART/Clarity、PI-Hunter/ARGUS/PISmith、SkillFortify/BIV/MalSkills/SkillSafetyBench、MemGraphRAG/Graph-R1/A-RAG、Agentic UX 模式体系（Agentic Design/AI UX Playground/Smashing/zylos）、OpenClaw 2.0、SkillSpector、CHAINDROP、Agent Threat Rules。

> 新扫描前：先 grep 本表对象名，命中即不重复收集，只做增量更新。
