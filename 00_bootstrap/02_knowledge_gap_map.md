# 02 · Knowledge Gap Map

> 生成时间：2026-09-01（Bootstrap 第三阶段产物）。
> 原则：缺口 = "边界之外且值得进入"的东西；每个缺口给出证据（为什么判定为缺口）与连接点。

---

## 缺口分类框架

| 类型 | 定义 | 处理策略 |
|---|---|---|
| **G1 · 声明未覆盖** | 用户自我定位/兴趣承诺了，但知识库基本空白 | 最高优先级，先补 |
| **G2 · 已启动未深化** | 知识库有零星条目，但未成体系 | 中等优先级，做连接 |
| **G3 · 项目需要而 KB 无** | 活跃项目明确依赖，知识库无支撑 | 高优先级，随项目拉通 |
| **G4 · 兴趣未接入** | 对话历史有关注，但从未进入知识体系 | 视相关性决定 |
| **G5 · 方法论可外推** | 我的方法论体系可自然外推到的新领域 | 战略性，看时机 |

---

## G1 · 声明未覆盖（最高优先）

### 1. AI 安全与攻防（Red Teaming / Adversarial ML / Agent 安全）
- **证据**：GitHub bio 明确写"专注AI安全、网络攻防"；内库有 `dsh`、`dsh-pentest` 两个项目 Hub（均为空骨架）；但知识库仅有 `安全审查_AI生成代码安全`、`安全审查_OWASP_Top10_2025` 两篇，无任何 AI 安全/攻防体系。
- **连接点**：EP-002 Permission Is Security Boundary、silver-shield（防诈骗=AI 安全应用）、工具档案中的 Sandbox 知识。
- **缺口范围**：对抗样本、Prompt Injection 防御、Agent 越权/沙箱逃逸、红队评测（AISI 类）、AI 漏洞挖掘工具链。

## G2 · 已启动未深化

### 2. 商业领域（Business）
- **证据**：商业空间按 Protocol 接入，已有 30+ 概念卡、10 条原则、6 个框架、13 个案例——但仅 Phase 0/1，且**未与 AI 原生产品、AI 公司经营闭环**相连。
- **深化方向**：AI×商业（AI-native 产品单元经济）、AI 公司经营（承接 AI Company OOS）。

### 3. LLM 可观测性与追踪
- **证据**：KB 仅 1 篇《可观测性_LLM应用追踪》；但 Tafcm 已建 ADI 诊断接口、silver-shield 有完整 CI/可观测体系。
- **深化方向**：OpenTelemetry GenAI / Langfuse / LangSmith / AgentOps 等主流方案对比。

### 4. RAG / 检索系统化
- **证据**：KB 仅 1 篇《混合检索避免单一策略盲区》；Context Engineering 有上下文编排篇。
- **深化方向**：chunking/rerank/GraphRAG/Agentic RAG，与 Context Engineering 打通。

### 5. 评估体系（Evals / Benchmarks）
- **证据**：五维模型有 Evaluation 维度；silver-shield 有 Benchmark Harness 实践；但无主流 Agent 基准（SWE-bench/GAIA/MLE-bench）实证。
- **深化方向**：Agent eval 框架对比、自建评估基准方法论。

## G3 · 项目需要而 KB 无

### 6. MCP 与 Agent 互操作协议
- **证据**：Tafcm(ADI) / TeamMind(多 CLI 编排) / agent-attention(跨 Agent 通知) / campus_order(OpenClaw) 都涉及 Agent 间通信与工具协议；KB 有完整 Tool System 理论但无 MCP/A2A/AGENTS.md 标准实证。
- **深化方向**：MCP 规范、A2A、AGENTS.md/AG-UI 标准化运动。

### 7. 本地 / 边缘 / 移动端 AI
- **证据**：Tafcm 定位"手机优先+离线可用"；silver-shield 需摄像头端感知；但 KB 无任何 on-device ML / 移动工程知识。
- **深化方向**：TFLite/ONNX Runtime/llama.cpp/Ollama/WebGPU、移动端 Dart/Flutter 工程体系。

### 8. 后端 / 基础设施工程深度
- **证据**：campus_order（SpringBoot）、myBlog（Java）等项目需要后端能力；KB 偏"AI 放大软件工程"，缺 SpringBoot/数据库/消息队列/云部署体系。
- **深化方向**：后端工程化、可观测后端、部署可靠性。

### 9. Agent Memory 实现层
- **证据**：五维模型有 Memory 维度 + Validation 有记忆验证章；但无 Mem0/Letta/Zep/A-MEM 等实现层对比。
- **深化方向**：主流记忆框架实证、长期记忆评测。

## G4 · 兴趣未接入

### 10. 去中心化 AI / 联邦学习 / 加密技术
- **证据**：对话历史高频关注区块链、去中心化 AI、联邦学习、Mag7；知识库完全空白。
- **连接点**：与 AI Company 分布式协作、数据主权、隐私计算相邻。

### 11. 机器人 / 具身智能 / 多机械臂
- **证据**：GitHub 有 `multi_arm_line_ws` 项目但孤悬无知识支撑；知识库无 robotics 条目。
- **连接点**：Robotics×LLM（VLA）、感知-决策-执行链路（与 silver-shield 感知链路同构）。

## G5 · 方法论可外推

### 12. 形式化验证 / Agent 可证明性
- **证据**：Validation 空间已经走向"可验证的系统属性"（验证编译器概念）；自然外推到形式化方法（TLA+/Lean/模型检测）。
- **连接点**：把"主观体验"变"可验证属性"的下一步就是形式化。

### 13. 组织科学 × AI 团队
- **证据**：AI Company OOS 已在定义组织形态；缺外部理论支撑（组织理论、团队认知、分布式决策）。
- **连接点**：把 Agent 组织视为真实组织研究，接《团队协作方式》空间。

---

## 缺口热力排序（按"与项目相关 × 与知识相关 × 新颖度 × 影响"）

| 排名 | 缺口 | 类型 | 优先级 |
|---|---|---|---|
| 1 | AI 安全与攻防 | G1 | 🔴 最高 |
| 2 | MCP / Agent 协议 | G3 | 🔴 高 |
| 3 | Agent Evaluation / Evals | G2/G3 | 🔴 高 |
| 4 | 本地/边缘/移动 AI | G3 | 🟠 高 |
| 5 | Agent Memory 实现层 | G3 | 🟠 高 |
| 6 | LLM 可观测性 | G2 | 🟠 中高 |
| 7 | RAG 系统化 | G2 | 🟠 中高 |
| 8 | AI 原生产品 / Agentic UX | G2 | 🟡 中 |
| 9 | 商业×AI 经营闭环 | G2 | 🟡 中 |
| 10 | 去中心化 AI / 联邦学习 | G4 | 🟡 中 |
| 11 | 形式化验证 | G5 | 🟢 战略 |
| 12 | 组织科学 × AI 团队 | G5 | 🟢 战略 |
| 13 | Robotics × LLM | G4 | 🟢 战略 |
