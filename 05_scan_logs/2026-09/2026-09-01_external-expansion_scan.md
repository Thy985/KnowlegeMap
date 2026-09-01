# 扫描日志 · 2026-09-01 External Knowledge Expansion 全领域扫描

- **日期**：2026-09-01
- **扫描主线**：从项目与知识缺口出发的 External Knowledge Expansion（七批次，7 个领域带）
- **来源**：GitHub / 官方博客 / Linux Foundation / OWASP / arXiv / 2026 横向评测 / 多份行业报告

## 1. 扫描范围（从 Project Landscape + Knowledge Gap Map 出发）
| 批次 | 领域 | 覆盖方向 |
|---|---|---|
| A | AI 安全治理 + AI 攻防（G1/S3/A6/A9） | OWASP Agentic Top10/Skills Top10、Garak/PyRIT、PentestGPT/PentAGI、MITRE ATLAS |
| B | Agent Memory（S4） | Mem0/Zep/Letta/A-MEM、MemEval、记忆基准批判 |
| C | 多 Agent 编排 + 互操作协议（S5） | A2A v1.0/AAIF、LangGraph/CrewAI/AG2/MS |
| D | Computer Use + Agent Harness/Runtime | Claude browser/computer use、browser-use、Omnigent、MS Agent Framework、harness 调查 |
| E | Developer Tools / AI Infra | 开源 Agentic CI、E2B 沙箱、OTel GenAI 可观测 |
| F | Model Ecosystem / 本地边缘 / 微调（B13/B14） | LlamaWeb/MLC-LLM/BitNet 边缘微调/TinyLLM、DPO/ORPO/KTO |
| G | 新框架 + 论文/报告 | 2026 新框架、Agentic 基准批判、企业 Agent 市场报告 |

## 2. 信号与收线（40+ 原始信号 → 13 张候选卡）
- 首轮已覆盖（去重不重复收集）：MCP 2026-07-28、MCP 通知 server、promptfoo、Evals 框架格局。
- 本轮按 S/A/B 分级写入：**S×4 / A×6 / B×3**（详见 03_expansion_queue/candidates/）。

## 3. 分级结果
### 🔴 S 级（可能显著改变项目或认知）
| # | 对象 | 为什么 S |
|---|---|---|
| 1 | OWASP Agentic Security 体系（Top10 2026 + Skills Top10 + Secure MCP 指南） | 直接填 G1 最大缺口；EP-002 理论化；微软 AGT 映射 |
| 2 | A2A 协议 v1.0 + Agentic AI Foundation | 与 MCP 互补构成互操作地基；TeamMind 协议层 |
| 3 | Agent Harness/Control Plane 范式（Omnigent/MS + harness 调查） | "meta-harness" 层兴起；六职责分解与我的五维模型同构；TeamMind 直接对照 |
| 4 | Agent Memory 2026 实现层 + 基准批判 | Memory 维度实现层实证 + "基准不可信"活教材 |

### 🟠 A 级（高价值，值得深入研究）
AI 攻防工具链、Computer/Browser Use GA、E2B 沙箱、OTel GenAI 可观测、Agentic 基准批判、本地/边缘 LLM。

### 🟡 B 级（保留观察）
开源 Agentic CI、Fine-tuning 对齐新范式、Multi-Agent 框架终局。

### 未收录
- MemPalace（记忆宫殿，2026-04 演员名人项目）：新奇但证据薄弱、噱头成分高 → 仅观察，不入库。
- 各类商业/市场报告（$47B/$7.5B 等）：口径差异大、与我的项目连接弱 → 仅作背景，不入候选。
- 抖音/微博等低证据密度内容：全部过滤。

## 4. 证据核验
- 三个 S 档锚点（Omnigent / A2A / OWASP）已用一手来源 web_fetch 复核，非二手转述。
- 记忆基准批判（LoCoMo 污染、长上下文碾压）保留为"第三方批判"与"厂商自报"区分标注。

## 5. 仓库更新
- `06_expansion_index/README.md`：**新增 Expansion Index**（17 条对象，含生命周期与去重基准）
- `03_expansion_queue/candidates/`：+13 张候选卡
- `04_connections/README.md`：17 条连接全部升 🟡
- `05_scan_logs/`：本日志

## 6. 下一步（按优先级）
- [ ] **S1 优先**：OWASP ASI01-10 映射到 EP 原则；给 agent-attention 做安全自评
- [ ] **S2**：精读 harness 六职责论文，与五维模型产出对照卡
- [ ] **S3**：A2A v1.0 spec → TeamMind 接入设计
- [ ] **S4**：MemEval 口径下对比 Mem0/Zep 最小实证
- [ ] A：Garak/PyRIT 本地红队最小实测（填 dsh-pentest 第一步）
- [ ] A：browser-use / E2B / OTel 各跑一次最小 demo
