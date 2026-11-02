# Personal Tech Radar 深耕扫描日志 · 2026-11-03（Runtime 周第二周 Day2 · 只追增量）

> 领域：Runtime（Agent 执行运行时），第二周（11-02~11-08）Day2 周二。分工：只追增量（durable/编排运行时新 release、Infinity 后续、Restate/DBOS 新动态）。

## 扫描结果
3 路 general_search（durable execution 新动态 / AWS Infinity 后续 / suspend-resume-checkpoint 增量）。

### 增量并入（B 级，并入 durable 品类卡，不建新卡）
1. **durare v0.5.0（crates.io，~10-09 更新）**——DBOS 兼容 Rust durable execution SDK：普通 async 代码每步 checkpoint 到 Postgres/SQLite，崩溃后精确恢复；**品类第 10 向**，Rust 语言栈补齐（DBOS 生态 Rust 扩展）。来源：crates.io orchestration 关键词页。
2. **semarun（PyPI 2026-10-21 更新）**——"Semantic checkpointing runtime"：Python 长运行 agent 语义检查点，暂停数小时/跨崩溃部署存活，换模型/工具结果继续不重做已完成工作；恢复语义**第三派候选（语义状态恢复）**，观察位（生态未明）。来源：PyPI。

### 普通增量记日志（不写卡）
- AWS Bedrock AgentCore Runtime 实例：最长 **14 天持久性会话**+GPU 加速实例+容量提供者（release notes 10-21 更新）——平台托管运行时能力扩展。
- 其余命中全部去重：revisit.tech durable 对比长文（10-12，DBOS 第 8 向来源已覆盖）、dbos/restate/temporal llm-info 首页（品类卡已覆盖）、Infinity 多篇转载（10-24~26，已覆盖）、AgentCore quota 提升（7 月旧闻）、Genkit Go 1.13 resumable loops（9-14，普通增量）、LangChain runtime 文（4-20 旧闻）、MS Agent Framework checkpoints 文档（9-16，已覆盖）、PulseHive multi-agent runtime（不知名小工具）。

## 产出
- durable 品类卡 §5 追加「第二周 Day2 增量（2026-11-03）」：durare=第 10 向；semarun=恢复语义第三派观察；AgentCore 14 天持久会话记日志。
- 无新候选卡（增量并入既有品类卡）。

## 后续
- 周三~周四继续只追增量；**周五 11-07 Agent Substrate 复现验证**（头号任务：clone+文档精读+K8s 零信任核对，满足 validated 门槛则晋升）；缺口④⑤ 视进度。
