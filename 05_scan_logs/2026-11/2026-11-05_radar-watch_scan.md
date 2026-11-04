# Personal Tech Radar 深耕扫描日志 · 2026-11-05（Runtime 周第二周 Day4 · 只追增量）

> 领域：Runtime（Agent 执行运行时），第二周（11-02~11-08）Day4 周四。分工：只追增量（durable/编排运行时新 release、Infinity 后续、生命周期 suspend-resume 相邻）。

## 扫描结果
3 路 general_search（durable 运行时新动态 / Infinity 后续 / suspend-resume-checkpoint 与 serverless 沙箱相邻）。

### 新候选卡（B 级，1 张）
- **`[cand]sandbox-lifecycle-suspend-resume-2026-11.md`——沙箱生命周期管理（suspend/resume/checkpoint）品类**：
  - 主体：**OpenKruise Agents v0.6.0**（CNCF 官方 blog 11-03）——SandboxUpdateOps 支持 CheckpointRestore（休眠 fleet 批量升级不唤醒、不丢文件系统）+ PoolAutoscaler（warm pool 容量管理）+ 自动 pause/resume（probe 空闲检测/定时唤醒/wake-on-traffic，空闲沙箱零 CPU）；
  - 对照 1：**Genspark SB-Box**（10 月底 beta）——每 agent 一个 VM，0.35s 中位启动，Freeze 保持内存/进程/磁盘只计磁盘费、0.8s 恢复、每次 freeze 可 fork 回滚（商业实现，第三方单源）；
  - 对照 2：**AWS AgentCore maxLifetime checkpoint**（re:Post 10-31 操作文）——watchdog 在期限前 checkpoint 内存态，重启/部署后新 microVM 恢复续跑。
  - 意义：正对能力树 **F 层（生命周期 suspend-resume-checkpoint）**；三侧实现（K8s 生态/商业 VM/平台 microVM）为 **11-07 Agent Substrate 验证日**（<500ms suspend-resume 基准）提供对照素材。

### 品类卡增量并入（durable 品类卡 §5「第二周 Day4 增量」）
- **DBOS 官方 10-29 blog**：Postgres-backed durable workflows 横向扩展至 **100 万 workflows/秒**（DBOS 行扩展性数据点）。
- **Dapr docs 首页 10-31 更新**：宣传语升级为 "durable, verifiable execution"——执行历史加密签名可审计（tamper-evident），Dapr 已验证卡事实更新。

### 其余命中全部去重/旧闻
- Dapr v1.19（10-22 已并入）、Infinity 官方博客（10-23 已建卡）、AgentCore release notes（Python 3.14/span destination，9 月旧闻；14 天持久会话 11-03 已记）、AgentCore new runtime（9-18 旧闻）、Lambda MicroVMs（7-10 旧闻）、Lambda durable functions 多 agent（6-29 旧闻）、MS Agent Framework checkpoints（11-01 文档更新）、亚马逊云中国区新闻（无关）。

## 产出
- 新候选卡 1 张（B 级 sandbox-lifecycle）；品类卡并入 2 项 B 级增量。

## 后续
- **周五（11-07）Agent Substrate 复现验证**（头号任务）：本卡与 11-04 IEEE SPIFFE 论文入对照素材；缺口④⑤ 视进度。
