# 候选对象证据卡 · AWS Infinity：极端并发 Agent Runtime（Hydro 项目）

> 状态：`[cand]` ｜ 关联方向：**Agent Runtime（当前深耕领域）** / 并发挂起恢复 Runtime / Serverless Agent ｜ 日期：2026-10-29（Runtime 周 Day4 增量扫描捕获）

## 一句话定位
**AWS Infinity**（2026-10-23 开源，Apache 2.0，AWS×UC Berkeley 合作 Hydro 项目）是研究定位的 agent runtime：把编程语言 **stackless coroutine 挂起/恢复**机制搬到 agent 执行上——每个 tool call 是 await 点，runtime 保存会话后挂起 agent（slice 语义），tool 结果到达时从持久化状态恢复；挂起 agent 只占会话历史内存（Raspberry Pi 5 的 8GB 可容 75,000 并发 agent），并原生支持 serverless step 模式（等待期间零计算）。

## 1. 它解决什么问题
- 传统 agent harness 的 agent loop 是阻塞步骤序列：调模型→调工具→等返回→循环；agent 等待工具时**持有进程与内存**，无法处理期间到达的事件
- 长时程 agent（20 分钟 build、数小时等 PR、隔夜等审批）浪费进程资源；serverless 平台被迫在工具运行期间保持 invocation 打开
- Infinity 用 **bounded slice** 替代阻塞步骤：一次 slice = 加载 history→一次模型补全→持久化→至多一个工具调用→slice 结束；工具调用成为 await 点，agent 永不在 slice 内阻塞
- 事件驱动：一切可恢复 agent 的消息（用户输入、tool 结果、父子 agent 消息）走共享 input queue；挂起 agent 不占内存，消息到达即启新 slice

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（AWS 官方开源博客，2026-10-23）**：Apache 2.0 发布，Hydro 项目（AWS + UC Berkeley）["https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/"]
- **FACT（性能基准，官方博客）**：模拟模型 20-turn 往返基准，挂起 agent 内存≈其 history 大小；75,000 并发 agent 于 8GB（Raspberry Pi 5）
- **FACT（serverless step mode）**：step 模式无常驻 task，平台按消息批次调 `step`；slice 有界执行、无进程亲和、at-least-once 投递+状态记录消息 ID（幂等去重）、FIFO 组串行化线程（无需分布式锁）——等待三天 CI 的 agent 在结果到达前零计算
- **FACT（synthetic tool calls 机制）**：异步事件以 `receive_event__injected` 合成工具调用呈现给模型（模型不可主动调用该名，runtime 拒绝）；订阅式事件按默认走临时子线程（不污染父线程 context），associative 事件才并入主线程 history；父子 agent 通过 `spawn_thread`/`report_to_parent` 普通工具调用通信，无需独立消息系统
- **与已有知识不重复**：与 durable 品类卡互补——**不是步骤持久化 checkpoint（Dapr Agents/Restate/MS/Lambda durable 路线），而是极低内存并发挂起（slice + serverless 卸载）**，第三条 runtime 设计路线；Dapr v1.19/AWS Lambda Durable（已并入品类卡）不重复；Cloudflare Agents SDK（10-28 增量，普通 release）不重复

## 3. 与我的连接
- **连接的项目**：
  - **TeamMind（Java 多 Agent 运行时）——最强连接**：Infinity 的 actor-style 线程模型（每会话独立 input queue、线程间仅消息、FIFO 串行化免锁）+ 子线程事件处理，是 TeamMind 并发模型设计的直接对照；slice 语义可为 TeamMind 的长时间任务提供"有界执行单元"思路
  - **Tafcm（本地优先）**：8GB/75k 并发证据线——本地边缘设备上的高密度 agent 可行性参照
  - silver-shield：serverless step 模式"等待零计算"= 资源控制新维度（成本/占用可预期）
- **连接的知识点**：能力树 agent-runtime.md **A 层（Durable Execution 与失败恢复）**——A4 durable-harness 品类的"并发挂起"旁支；**C 层（资源隔离与密度）**——75k 并发/8GB 密度基准补强；**D 层（生命周期 suspend-resume）**——slice/step 语义直接素材
- **潜在收益**：周五（10-30）验证日对照池 +1（与 Dapr Agents 的步骤持久化对照）；TeamMind 并发/事件模型设计参考

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | 官方博客 ["https://aws.amazon.com/blogs/opensource/introducing-infinity-a-runtime-for-extreme-agent-concurrency/"]；仓库待确认（Hydro 项目，博客正文含链接） |
| 证据等级 | FACT（AWS 官方开源博客 + 性能基准数据）；research early release（非 GA 生产工具） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① 精读官方博客全文明细（slice 生命周期/step 模式/synthetic events 机制已精读）；② 若仓库可及：跑通最小 demo 验证挂起-恢复与 step 模式；③ 对照表：Infinity（并发挂起）vs Dapr Agents（步骤持久化）vs Restate（通用 durable）三路线设计对比 |
| 预期完成时间 | 2026-10-30（周五验证日）或延后至第二周；本卡先占位 |

## 5. 验证结果
**2026-10-30（Runtime 周 Day5 验证日）对照回填**：
- ✅ 官方博客全文精读完成（Day4 建卡时）：slice 生命周期、serverless step 模式、synthetic tool calls（`receive_event__injected`）、spawn_thread/report_to_parent 机制均已确认
- ✅ **三路线设计对照产出**（详见 `[cand]durable-execution-category-mainstreaming-2026-10.md` §5 9 向表）：Infinity 与 Dapr Agents/Restate 属**不同恢复语义派**——Infinity 是**挂起恢复**（slice 有界执行+serverless 卸载，等待零计算，挂起 agent 只占 history 内存）vs Dapr/Restate/DBOS 是**步骤持久化恢复**（重放不重执行）；二者互补：步骤持久化保证失败后不重复已完成调用，挂起模型保证等待期间零资源占用
- ⚠️ 仓库 clone/demo 未跑（GitHub 网页 robots 限制 + 本环境无容器运行时；research early release 非生产 GA 工具，判定维持观察合理）
- **对 TeamMind 的启示**：Infinity 的 actor-style 线程模型（每会话独立 input queue、线程间仅消息、FIFO 串行化免锁）与 slice 有界执行单元是 TeamMind 并发/长时间任务设计的直接参考；但 research 阶段不宜直接选型

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察（research early release；博客一手精读+对照完成，缺仓库级复现）
- [ ] 拒绝（原因）
