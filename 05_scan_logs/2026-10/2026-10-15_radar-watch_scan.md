# 扫描日志 · 2026-10-15（Personal Tech Radar 第 43 次扫描 · Evaluation 周 Day4 · 增量）

> 周三分工：只追增量（新 release/新工具/相邻项目），不做全量。

## 扫描范围
general_search 两路：① agent evaluation 基准/框架新论文与新 release；② agent 可观测/tracing 平台新变化。

## 结果

### 新候选卡（+2，候选卡 44→46）
- **TestJack**（A 级）——`03_expansion_queue/candidates/[cand]testjack-agentic-benchmark-audit-2026.md`
  - arXiv 2610.10619（10-07）：Agentic Coding 基准**审计框架**——为每个 trial 动态生成针对 prompt 要求的测试、只保留 ground-truth patch 通过的测试、复查失败，每个确认失败有**可回放测试**支撑；含轻量采样变体
  - 不是新基准而是"审计基准的框架"；与 AgentJudgeBench（judge 侧）+ Transect（评测者审计侧）互补成评测可信度**三环**（+补丁/测试侧审计），命中能力树 B 层与"主流基准实证"缺口
  - 证据 FACT（arXiv）
- **LiveMACE**（B+ 级）——`03_expansion_queue/candidates/[cand]livemace-process-aware-eval-2026.md`
  - arXiv 2610.09872（10-07）：真实金融市场演化作为持久 LLM Agent 测试床，30 天连续评测发现 **outcome-capability gap**（实现结果 vs 机制能力分离）
  - 方法论增量：动态演化测试床 + 过程感知诊断 + 持久 agent 评测，填补能力树 A 层"静态 vs 动态评测设计"缺口
  - 论文级证据（未见工具）；TeamMind（多 agent）/Memory 周（持久记忆）先行参照

### 记日志不建卡
- **Amazon CloudWatch Omni**（AWS 官方，09-22）：下一代 CloudWatch，应用+AI agent 统一可观测（自动拓扑/自然语言+SQL/AI 引导调查）——平台级 agent 观测增量，归入已建卡的 Trace-based Agent Evaluation 主线（AWS Agent Health/Bedrock AgentCore 的平台化延伸）
- **LangSmith AI Search**（10-14）：自然语言描述检索 agent traces——LangSmith 商业增量，与 Transect 可导航报告方向相关
- **阿里云 AgentLoop**（09-15）：Agent Ontology 全栈拓扑 + STAROps 诊断——国内云 agent 观测平台，商业增量
- **Traccia**（Product Hunt 10-11）：vendor-neutral agent Control Plane（OTel 基础）——新品证据单一，观察
- **HoneyHive**（官网更新）：agent 可观测+评估平台——商业增量
- **Argo-Bench**（TextQL Labs 10-01）/ **EnterpriseBench**（arXiv 2609.37658）/ **AgentWorld**（09-26）：场景型基准堆积，后果驱动评分方法论已被 LiveMACE/TestJack 覆盖，不建卡
- **LoCoBench-Agent**（arXiv 2511.13998）：2025 年 11 月论文，时效已过

### 去重确认
- AgentJudgeBench / Transect / 求索 4.0 / ReviewBench / MXC / Protocol Pivoting 均已建卡 → 命中不重复
- Trace-based Agent Evaluation（含 AWS 系）在基准 → CloudWatch Omni 只做增量记录
- LangSmith 在基准 → AI Search 只做增量记录

## 结论
**New**（领域内 2 张卡：TestJack A + LiveMACE B+，候选卡 44→46）。周四增量有实质捕获，按规范建卡并推送。
