# 候选对象证据卡

> 状态：`[cand]` ｜ 关联方向：Top20 #07（Agent Runtime）｜ 日期：2026-11-05

## 一句话定位
K8s 生态的 Agent 沙箱生命周期管理（suspend/resume/checkpoint）开始成品类：OpenKruise Agents v0.6.0 提供 CheckpointRestore + 自动暂停/恢复，Genspark SB-Box 提供商业 freeze/resume，平台侧 AgentCore 提供 maxLifetime checkpoint 操作——正对 Runtime 能力树 F 层（生命周期 suspend-resume-checkpoint），与 11-07 Agent Substrate 验证的 <500ms suspend-resume 基准直接对照。

## 1. 它解决什么问题
- 长运行 agent 的沙箱资源长期占用问题：空闲 agent 实例持续耗 CPU/内存，但「休眠-唤醒」需要不丢文件系统/内存/进程状态。
- K8s 上批量运维沙箱 fleet（升级/扩容/回收）需要不唤醒实例即可操作（checkpoint-restore）。
- 平台托管 agent 的长任务在重启/部署后需从 checkpoint 干净恢复（AgentCore maxLifetime 场景）。

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（OpenKruise Agents v0.6.0，CNCF 官方 blog 2026-11-03）**：SandboxUpdateOps 支持 **CheckpointRestore**（批量升级休眠 fleet 不唤醒、不丢文件系统）；**PoolAutoscaler**（declarative warm pool 容量+水位线+cron）；**自动 pause/resume**（probe 驱动空闲检测、定时唤醒、wake-on-traffic，空闲沙箱零 CPU）["https://www.cncf.io/blog/2026/11/03/openkruise-agents-v0-6-0-leaping-ahead-in-agent-sandbox-security-and-automation/"]
- **FACT（Genspark SB-Box，2026-10 底 beta，11-01 第三方报道）**：每 agent 一个完整 VM；0.35s 中位启动（4GB 机器）；Freeze 保持内存/进程/磁盘但只计磁盘费；0.8s 中位恢复；每个 freeze 是版本可 fork/回滚——商业侧 freeze/resume 实现 ["https://aitoolsreview.co.uk/insights/genspark-sb-box"]
- **FACT（AWS re:Post 2026-10-31 操作文）**：AgentCore Runtime 长运行 agent 通过 watch dog 在 maxLifetime 前 checkpoint 内存态，重启/部署后新 microVM 恢复续跑；版本变更时需把跨部署状态放入 durable store ["https://repost.aws/articles/ARr12gviwcQYStNRlawgMmTA/amazon-bedrock-agentcore-runtime-pre-monitor-maxlifetime-so-long-running-agents-checkpoint-before-the-restart-resume-cleanly-on-v2-and-after-deploys-and-plan-cold-starts-per-region"]

## 3. 与我的连接
- **连接的项目**：TeamMind（多 Agent 运行时——若自建沙箱/agent 实例，生命周期管理是其运行时的天然组件）；dsh（若未来加沙箱层）。
- **连接的知识点**：Runtime 能力树 F 层（生命周期 suspend-resume-checkpoint）；Agent Substrate（二号锚点，<500ms suspend-resume/20 万 agent 基准）——本卡提供 K8s 生态/商业/平台三侧实现对照。
- **潜在收益**：11-07 验证日 Substrate 精读时用本卡对照「第三方如何实现 suspend-resume」（K8s checkpoint-restore vs 商业 VM freeze vs 平台 microVM checkpoint），评估生命周期层的工程成熟度；为 TeamMind 沙箱休眠设计提供现成参考。

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | OpenKruise Agents ["https://www.cncf.io/blog/2026/11/03/openkruise-agents-v0-6-0-leaping-ahead-in-agent-sandbox-security-and-automation/"]；Genspark SB-Box ["https://aitoolsreview.co.uk/insights/genspark-sb-box"]（第三方报道，官方 beta 待核）；AWS re:Post ["https://repost.aws/articles/ARr12gviwcQYStNRlawgMmTA/amazon-bedrock-agentcore-runtime-pre-monitor-maxlifetime-so-long-running-agents-checkpoint-before-the-restart-resume-cleanly-on-v2-and-after-deploys-and-plan-cold-starts-per-region"] |
| 证据等级 | FACT（CNCF 官方）+ DESIGN（Genspark 商业设计，第三方单源） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | 11-07 周五验证日并入 Agent Substrate 对照：精读 Substrate 的 suspend-resume 机制 vs 本卡三侧实现；OpenKruise 文档精读核对 CheckpointRestore 语义 |
| 预期完成时间 | 11-07 周五验证日 |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察（三侧实现均为早期/beta/操作文，等待周五 Substrate 对照后定级）
- [ ] 拒绝（原因）
