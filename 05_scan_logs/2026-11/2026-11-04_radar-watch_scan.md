# Personal Tech Radar 深耕扫描日志 · 2026-11-04（Runtime 周第二周 Day3 · 只追增量）

> 领域：Runtime（Agent 执行运行时），第二周（11-02~11-08）Day3 周三。分工：只追增量（durable/编排运行时新 release、Infinity 后续、Restate/DBOS 新动态；缺口⑤身份层相邻）。

## 扫描结果
3 路 general_search（Restate/DBOS/Temporal 新动态 / AWS Infinity 后续 / agent 身份 SPIFFE 零信任）+ 1 次 web_fetch（Restate blog 核验 BYOC）。

### B 级记日志（不并入品类卡，避免卡膨胀）
1. **Restate BYOC**（blog 置顶近期公告，日期未明）——fully managed Restate 部署进用户自有云账号/VPC（private+secure，性能提升表述）；Restate 托管部署形态的商业扩展，对 TeamMind 评估（自托管 Java SDK）无实质影响。
2. **IEEE「SPIFFE-Based Zero-Trust Authentication for AI Agent Ecosystems」**（IEEE Xplore 11431026，索引 2026-07）——SPIRE 为 K8s 上 5 agent 集群签发短时 X.509 SVID（1h TTL、50% 生命周期轮换）实现零信任 agent 互认证、消除静态 API key；**缺口⑤（Agent Mesh 身份层 SPIFFE）直接学术素材**，供 11-07 周五 Agent Substrate 验证日 SPIFFE 对照。

### 其余命中全部去重
- revisit.tech durable 对比文（10-12，DBOS 第 8 向来源已覆盖）、maketocreate Temporal vs Restate vs Inngest 对比（10-12，品类格局已覆盖）、eCorpIT DBOS（8-02 旧闻）、Restate Series A $20M（9-30 旧闻）、Restate 1.7/1.6（7-07/2 月旧闻）、Restate+Langfuse/Pydantic AI 集成文（4-09/4-02 旧闻）
- Infinity 官方博客（10-23，已建卡）、AgentCore release notes（Python 3.14/span destination/Step Functions，9-17 及更早旧闻；14 天持久会话 11-03 已记）
- SPIFFE 10 周年 Community Day（10-27 活动）、OpenShift 4.20 SPIRE Agent（9-02 旧闻）、Istio Ambient SPIFFE（6-20 旧闻）、arXiv 2504.14760 CI/CD SPIFFE（2025-04 旧闻）

## 产出
- 无新候选卡、无品类卡增量并入（2 项 B 级记日志）。

## 后续
- 周四（11-05）继续只追增量；**周五（11-07）Agent Substrate 复现验证**（头号任务：clone+文档精读+K8s 零信任模型核对 SPIFFE/egress 代理/密度基准；本日志第 2 项 IEEE 论文作 SPIFFE 对照素材）；缺口④⑤ 视进度。
