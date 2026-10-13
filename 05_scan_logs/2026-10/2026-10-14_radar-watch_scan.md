# 扫描日志 · 2026-10-14（Personal Tech Radar 第 42 次扫描 · Evaluation 周 Day3 · 增量）

> 周三分工：只追增量（新 release/新工具/相邻项目），不做全量。

## 扫描范围
general_search 两路：① agent evaluation framework / LLM evals / observability 新 release；② OTel GenAI 语义约定 / agent tracing 新变化。

## 结果

### 新候选卡（+2，候选卡 41→43）
- **求索 4.0**（A 级）——`03_expansion_queue/candidates/[cand]qiusuo-benchmark-2026.md`
  - 2026-10-13 央视发布，国内首个 AI **全产业链评测基准**（国家标准评测基准体系）：四大板块（基础软硬件 / 模型与智能系统 / 安全治理 / 行业落地）、16 项测评工具，覆盖算力→大模型→智能体→具身智能→AI 安全→行业场景
  - 配套电力/医疗/钢铁真实业务测试负载；算力/大模型/智能体轻量版代码工具开源可复现；国标院（中国电子技术标准化研究院）主导
  - 命中能力树 A 层（评估设计与标准）与"自建基准方法论"缺口，提供国内参照系；证据 FACT（央视）
- **ReviewBench**（A 级）——`03_expansion_queue/candidates/[cand]reviewbench-2026.md`
  - GitHub 官方（Blog 10-05）开源 AI 代码审查离线基准：按 1 亿+ 真实 PR 的语言/仓库规模/PR 规模分布建模，多源 golden set + 统一 rubric + 资深工程师独立验证
  - 与 Pullfrog/OpenCodeReview（代码审查工具）不同——这是评测基准本身；"分布建模→golden set→rubric→独立验证"方法论直接可迁移到自建基准
  - 证据 FACT（GitHub 官方）

### 记日志不建卡（增量/格局内/时效已过）
- **OTel GenAI 生态增量**：语义约定已迁至独立仓库 `semantic-conventions-genai`（生产需固定版本）；v1.41.0 增加 streaming、reasoning token、time-to-first-chunk、更新 tool 定义；OpenInference 捐赠提案（Arize → OTel）——OTel GenAI 已在基准，增量记录
- **MCP 可观测性增量**：2026-07-28 MCP spec 弃用 protocol-level Logging/Roots/Sampling/HTTP+SSE（12 个月时钟）；OTel GenAI 语义约定新增 MCP 专用 spans/attributes/metrics——与 10-13 Protocol Pivoting 卡不同角度，记录待 MCP 周深化
- **Jaeger 向 AI agent tracing 演进**（CNCF 05-26）：采纳 MCP/ACP/AG-UI 三标准，成为交互式 agent 观测工作区——主流 APM 转型信号，Changed 类；5 月事件时效已过，B 级观察项记日志
- **TruLens 博客（09-01）**：judge scores→evidence 对齐方法论——与 10-10 AgentJudgeBench 卡主题同构，增量记录
- **GPA 框架（arXiv 2510.08847）**：Goal-Plan-Action 对齐三维评估——2025 年论文、单篇未验证活跃度，B- 观察，记日志

### 去重确认
- Transect（arXiv 2610.08364）已建卡（10-13）→ 命中，不重复
- OTel GenAI、MCP、Pullfrog/OpenCodeReview、LangSmith/DeepEval/Arize Phoenix/OpenAI Evals 均在基准 → 只做增量

## 结论
**New**（领域内 2 张 A 级卡，候选卡 41→43）。周三增量有实质捕获，按规范建卡并推送。
