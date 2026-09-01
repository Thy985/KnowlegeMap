# 04 · Top 20 Expansion Directions

> 生成时间：2026-09-01（Bootstrap 第四阶段产物）。
> 评分维度（1–5）：**PR** 与项目相关度（权重0.25）｜**KR** 与知识体系相关度（0.20）｜**N** 新颖度（0.10）｜**PI** 潜在影响（0.20）｜**CA** 当前活跃度（0.10）｜**V** 值得实际验证度（0.15）。
> 综合分 = Σ(维度×权重)。**只列出能回答"为什么值得进入视野"的方向，不为凑数。**

---

## 综合排名总表

| # | 方向 | PR | KR | N | PI | CA | V | **综合** | 档位 |
|---|---|---|---|---|---|---|---|---|---|
| 1 | **MCP 生态与 Agent 互操作协议** | 5 | 5 | 3 | 5 | 5 | 5 | **4.80** | 🔴 S |
| 2 | **Agent Evaluation / Evals 框架** | 5 | 5 | 3 | 4 | 4 | 5 | **4.50** | 🔴 S |
| 3 | **Agent 安全治理（沙箱/权限/策略引擎）** | 4 | 5 | 4 | 5 | 4 | 4 | **4.40** | 🔴 S |
| 4 | **Agent Memory 实现前沿（Mem0/Letta/Zep/A-MEM）** | 4 | 5 | 3 | 4 | 5 | 5 | **4.35** | 🔴 S |
| 5 | **多 Agent 编排框架实证（LangGraph/CrewAI/AutoGen/Agents SDK）** | 4 | 5 | 2 | 4 | 5 | 5 | **4.25** | 🟠 A |
| 6 | **AI Red Teaming / Adversarial ML** | 4 | 4 | 4 | 5 | 4 | 4 | **4.20** | 🟠 A |
| 7 | **Agentic CI 工业化（CodeRabbit/Greptile 等）** | 5 | 4 | 3 | 3 | 4 | 5 | **4.10** | 🟠 A |
| 8 | **Agent 基准与排行榜（SWE-bench/GAIA/MLE-bench）** | 4 | 4 | 3 | 4 | 4 | 5 | **4.05** | 🟠 A |
| 9 | **AI 驱动的攻防工具链（AI pentest/漏洞挖掘）** | 4 | 3 | 4 | 5 | 4 | 4 | **4.00** | 🟠 A |
| 10 | **数据为中心 AI 工具（Cleanlab/Snorkel/Argilla）** | 4 | 5 | 2 | 3 | 3 | 5 | **3.85** | 🟡 B |
| 11 | **代码沙箱/解释器（E2B/Daytona/microVM）** | 3 | 4 | 3 | 4 | 4 | 5 | **3.80** | 🟡 B |
| 12 | **LLM 可观测性（OpenTelemetry GenAI/Langfuse/LangSmith）** | 4 | 3 | 2 | 4 | 4 | 5 | **3.75** | 🟡 B |
| 13 | **本地/边缘 AI（ONNX/TFLite/llama.cpp/WebGPU）** | 4 | 3 | 3 | 4 | 4 | 4 | **3.70** | 🟡 B |
| 14 | **LLM Fine-tuning 与对齐（LoRA/DPO/RLAIF/合成数据）** | 2 | 4 | 3 | 5 | 5 | 4 | **3.70** | 🟡 B |
| 15 | **AI 原生产品与 Agentic UX** | 3 | 3 | 4 | 5 | 4 | 3 | **3.60** | 🟡 B |
| 16 | **组织科学 × AI 团队** | 3 | 4 | 5 | 4 | 3 | 3 | **3.60** | 🟡 B |
| 17 | **RAG 系统化（GraphRAG/Agentic RAG）** | 2 | 4 | 2 | 4 | 5 | 5 | **3.55** | 🟡 B |
| 18 | **形式化验证 × Agent（TLA+/Lean/模型检测）** | 2 | 4 | 5 | 5 | 3 | 3 | **3.55** | 🟡 B |
| 19 | **Robotics × LLM（VLA/具身智能）** | 3 | 2 | 5 | 4 | 4 | 3 | **3.30** | 🟢 C |
| 20 | **去中心化 AI / 联邦学习** | 2 | 2 | 5 | 4 | 3 | 3 | **2.95** | 🟢 C |

---

## 分档说明与行动建议

### 🔴 S 档（4.3+）—— 立即进入探索队列，优先验证
| 方向 | 为什么值得进入 | 连接锚点 | 首个验证动作 |
|---|---|---|---|
| **MCP 生态** | Agent 工具协议的"事实标准"，我的 Tool System 理论缺标准实证；TeamMind/agent-attention/Tafcm 全部可直接受益 | TeamMind 编排、Tafcm ADI、OpenClaw Skills | 读 MCP 规范 → 给 agent-attention 写一个 MCP server 做概念验证 |
| **Agent Evals** | Validation 空间是"验证编译器"，缺主流 eval 框架实证；silver-shield 有 Benchmark Harness 可对照 | Validation 空间、五维模型 Evaluation、Tafcm ADI | 跑通一个 eval 框架（如 promptfoo/DeepEval）用于 Tafcm 的 ADI 回归 |
| **Agent 安全治理** | EP-002 原则的直接延伸；AI 安全是声明方向；silver-shield 的权限边界同构 | EP-002、Sandbox 知识、AI Company 权限矩阵 | 调研 Agent 安全框架（如 OWASP Agentic Security、安全 agent 沙箱方案） |
| **Agent Memory 前沿** | 五维模型 Memory 维度缺实现层；长期记忆是 Validation 未覆盖的实证区 | Memory 维度、Validation 记忆验证章 | 对比 Mem0/Letta 的记忆持久化与检索，写一张证据卡 |

### 🟠 A 档（4.0–4.3）—— 高优先级，与正在做的事直接对接
| 方向 | 为什么值得进入 | 连接锚点 |
|---|---|---|
| **多 Agent 编排框架** | TeamMind 需要框架级对比支撑"选型与拓扑" | 多Agent_框架选型与拓扑、TeamMind |
| **AI Red Teaming** | 补齐"AI 安全"声明缺口的第一块；对抗思维可反哺 silver-shield | dsh-pentest、安全审查、silver-shield |
| **Agentic CI 工业化** | 我有自研 AgenticCI 资产，外部产品化方向可对照验证 | AI Code Review 资产族 |
| **Agent 基准** | 让"验证"有标尺；评估自己项目的 agent 能力 | Validation、Benchmarks 占位 |
| **AI 攻防工具链** | 承接 dsh-pentest 空壳；AI 时代安全能力 | dsh-pentest、AI 安全方向 |

### 🟡 B 档（3.5–4.0）—— 有选择地跟进，先出证据卡再决定
| 方向 | 跟进理由 |
|---|---|
| **数据为中心 AI 工具** | weather-recognition 方法论可直接复用 |
| **代码沙箱/解释器** | 承接权限/沙箱知识，支撑 Agent 执行域 |
| **LLM 可观测性** | 连接 Tafcm ADI，体系化现有单篇 |
| **本地/边缘 AI** | Tafcm 离线、silver-shield 边缘都依赖 |
| **Fine-tuning/对齐** | 从 ML 方法论走向 LLM 层，影响大但工程重 |
| **AI 原生产品/Agentic UX** | 承接 AI Company + Business 的产品化闭环 |
| **组织科学×AI 团队** | 给 AI Company OOS 提供理论支撑 |
| **RAG 系统化** | 补 Context Engineering 的实现面 |
| **形式化验证** | 战略级，把 Validation 推向可证明性 |

### 🟢 C 档（<3.5）—— 保持观察，非当前重点
| 方向 | 观察理由 |
|---|---|
| **Robotics×LLM** | 有 multi_arm_line_ws 但知识断层大，等具身生态成熟 |
| **去中心化 AI/联邦学习** | 兴趣向，与主线弱连接，低优先 |

---

## 三条主线（合并后的探索纲领）

1. **协议与标准线**（S1/S2/S3/S5/S7/S8）—— 把"我怎么做 Agent"变成"行业标准怎么做"：MCP → Evals → 安全治理 → Memory 实现。
2. **安全与攻防线**（S3/A6/A9）—— 兑现 GitHub 定位：Red Teaming → Agent 安全治理 → AI 攻防工具链，反哺 silver-shield 与 dsh-pentest。
3. **验证与评测线**（S2/A8/B10/B12/B18）—— 让"可验证性"成为跨项目方法论护城河：Evals → 基准 → 可观测性 → 形式化。
