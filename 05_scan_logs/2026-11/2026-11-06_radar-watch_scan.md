# Personal Tech Radar 深耕扫描日志 · 2026-11-06（Runtime 周第二周周五 · 验证日）

> 领域：Runtime（Agent 执行运行时），第二周（11-02~11-08）**周五验证日**。任务：对 2 个高价值候选做实际验证/对比（头号：Agent Substrate 复现；对照：OpenKruise Agents v0.6.0 沙箱生命周期品类）。

## 环境前置
- 可用：git、go 1.27.3（按仓库要求自动下载）、python 3.12.11；**无 Docker / kubectl / K8s 集群**。
- 因此采用「仓库 clone + 编译 + API/CRD/文档核对」级复现（与 10-30 Dapr、10-31 Strands Box 先例同级），集群运行时行为如实标注未验证。

## 验证 1：Google Agent Substrate（二号锚点，头号任务）
- **仓库地址修正**：官方仓库为 `https://github.com/agent-substrate/substrate`（不在 google org；`google/ax` 是构建其上的上层编排器 AX/Agent Executor）。首轮 clone `google/agent-substrate` 失败（Repository not found），已按官方 README 交叉链接纠正。
- **构建验证**：`go build ./cmd/...` **通过（exit 0）**，go 1.27.3 linux/amd64。
- **产物核对**：`cmd/` 下 **14 个二进制**——`ateapi`（控制面 gRPC）、`atecontroller`、`atelet`（节点代理）、`atenet`（网络/路由）、`ate-idp-server`（身份提供方）、`ateworker-gvisor` / `ateworker-microvm`（双沙箱实现）、`ate-setup`、`credential-provider`、`objectstore-plugin`、`podcertcontroller`、`kubectl-ate`、`dataplane`、`benchmarking`。
- **生命周期语义（代码级）**：`api/ateapi/v1/ateapi.proto` 暴露 `SuspendActor`（"A running actor is checkpointed to a new snapshot"）与 `ResumeActor`（"Resume an actor from its latest snapshot"）——与能力树 F1 suspend-resume 直接对应。
- **隔离/身份/网络（文档级 + 组件级）**：
  - 沙箱必须是 gVisor（runsc）或 Cloud Hypervisor microVM，**不支持普通 Linux 容器**；
  - 每 active actor 默认获**短时 SPIFFE X.509**，egress gateway 可按策略铸造 **per-actor JWT**，二者携带 actor identity + atespace，支持外部 IdP 联邦；
  - **actor 零凭据**：只发 placeholder header，gateway 在沙箱外向 credential provider 取真实 secret 并替换，注入的 prompt/被攻陷 agent 无可外泄对象；
  - 默认拒绝网络：无入站路径（除 atenet-router）、无横向 actor-to-actor、无控制面访问，出站由 egress gateway 管控（可替换 PEP，挂 DLP/注入扫描/云 IAM）。
- **过载语义（实现细节，强于宣传语）**：request parking——`ResumeActor` 遇 `ResourceExhausted/Unavailable` 时按指数退避重试，park budget 默认 5s、parking lot 上限 1024；预算耗尽也不取消已提交 restore（晚到即晚服务，而非失败）。
- **指标口径**：README/架构文档原文为 **10x 密度、<500ms resume、>500 activations/s**；"20 万 agent" 是 Google 发布时的验证规模（10-22 报道），非仓库 README 承诺值——已区分标注。
- **限制**：`benchmarking/`（locust + nighthawk ingress/egress + telemetry）套件在仓库内可复现，但本地无 K8s 未跑；密度/延迟数据为官方口径，非本次实测。
- **决策：晋升 validated**（代码可编译 + gRPC/组件/文档可核验 + Apache-2.0 公开仓库）。
- **事实修正**：Titanium IPU 硅基隔离属于 **Google Cloud Agent Compute Engine（ACE）托管服务**；开源 Substrate 侧是 gVisor / Cloud Hypervisor microVM。此前能力树与卡把它写作 Substrate 特性，已更正。

## 验证 2：OpenKruise Agents v0.6.0（沙箱生命周期品类卡）
- clone `github.com/openkruise/agents`（最新 commit 11-05），核对 CHANGELOG v0.6.0 与 `api/v1alpha1/`：
  - `CheckpointControl`（#508）、`CheckpointRestore` 升级策略（#670）、`PersistentContents`（#674；代码枚举 podInfo/memory/filesystem/**gpuMemory**）；
  - `PauseStrategy` 代码枚举 **Stop / Hibernate**（blog 的 Snapshot/CloudDisk 为转述偏差，以代码为准）；
  - `SandboxUpdateOps` 两阶段升级（#710/#750）+ 成功后清除策略（#785）；
  - `Commit` CRD + nerdctl commit/push；resume 原子性（#435）、恢复后重新初始化/CSI 重挂（#416）；
  - Security Identity Provider：token 签发、**resume/clone/CSI re-mount 重签**（#633/#637/#638/#639/#671）、主动轮换（#475/#742）；
  - `SecurityProfile` 含 MCP 工具访问控制（#614）等——安全面扩展。
- **决策：`[cand]sandbox-lifecycle-suspend-resume-2026-11.md` 晋升 validated**（CNCF blog + 源码两条独立证据）；限制=未跑集群。
- 与 Substrate 的对照结论：两者在「actor 暂停→快照→按需恢复到 warm worker」上是同一设计范式，差异在实现层——Substrate 用统一控制面（gRPC + idp + egress PEP）管异构 sandbox；OpenKruise 用 K8s CRD/控制器嵌入现有集群运维（SandboxSet/SandboxUpdateOps/Commit）。对 TeamMind 的启示：自研优先「控制面与沙箱技术解耦 + 生命周期 API 独立」，避免把 checkpoint 绑死在某一 sandbox 实现。

## 落位
- 能力树 `08_agent_centric/domains/agent-runtime.md`：锚点表 Substrate → **validated ✅**（含实现细节与事实修正）；缺口② → **已闭环**；缺口⑤ → **部分闭环**（SPIFFE/per-actor JWT/ate-idp-server/恢复重签，与 11-04 IEEE 论文对照）；§六 任务表与日期校正（11-06=周五）。
- 候选卡 `[cand]sandbox-lifecycle-suspend-resume-2026-11.md`：§5 验证结果回填 + §6 勾 validated + 状态改 `[val]`。

## 遗留（顺延）
- 缺口④ TeamMind 权限模型 vs dsh/MXC 对照（B 级）未执行 → 周六回灌日或第三周。
- 集群级实测（Substrate 密度/延迟、OpenKruise freeze/resume）环境不可行，已如实标注，不伪造实测结论。
- 周六（11-07）：graph.md / 04_connections 回灌（新增「生命周期控制面」「身份-egress 一体化」两条边）；周日（11-08）第二周小结并判换域。
