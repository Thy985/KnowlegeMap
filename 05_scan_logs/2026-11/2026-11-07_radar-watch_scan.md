# Personal Tech Radar 深耕扫描日志 · 2026-11-07（Runtime 周第二周 · 周六回灌日）

> 领域：Runtime，第二周（11-02~11-08）。当天分工：**把 11-06 验证日结论回灌 index / connections / 能力树**。不新增扫描，不引入新候选。

## 回灌输入（11-06 已验证结论）
1. **Agent Substrate → validated**（`agent-substrate/substrate`；`go build ./cmd/...` 通过；15 二进制；gRPC `SuspendActor`/`ResumeActor`；gVisor/microVM；短时 SPIFFE X.509 + per-actor JWT；actor 零凭据 + credential provider 外注；request parking 5s/1024；官方口径 10x 密度/<500ms resume/>500 activations/s，集群未实测）。
2. **`[val]sandbox-lifecycle-suspend-resume-2026-11.md` → validated**（OpenKruise Agents v0.6.0：CheckpointControl/CheckpointRestore/PersistentContents（含 gpuMemory）/PauseStrategy=Stop|Hibernate/Commit CRD/SandboxUpdateOps 两阶段/Security Identity Provider 恢复重签/SecurityProfile 含 MCP 工具管控）。

## 回灌动作
### graph.md（新增 4 条跨域边）
| 边 | 落点 | 含义 |
|---|---|---|
| `lifecycle-control-plane` | agent-runtime（F1/F2）/ governance / observability | suspend-resume 从「内部行为」升级为**显式控制面 API**；每次生命周期操作即审计事件与容量信号 |
| `identity-egress-fusion` | agent-runtime（D/E）/ governance（C3）/ web-security | 身份（SPIFFE SVID/per-actor JWT）与出站策略在同一策略点裁决，替代「先给凭据再靠网络策略兜」 |
| `zero-credential-execution` | governance / agent-runtime（D）/ developer-tools | 凭据外注的可执行形态：agent 只持 placeholder，真实 secret 在沙箱外替换 |
| `load-shedding-parking` | agent-runtime（F3）/ observability / agent-evaluation | 池饱和时的过载语义（park budget 5s、1024 槽、指数退避、已提交 restore 不取消） |

### 04_connections（2 条新增 + 1 条补充）
- **Agent Substrate**：TeamMind（生命周期控制面设计基线 + warm worker 与 K8s 调度解耦）、silver-shield（零凭据降低被攻陷后的外泄面；egress PEP 可挂 DLP/注入检测）、Tafcm（反面参照：K8s 依赖重，不适用离线优先）→ ✅ validated。
- **OpenKruise Agents v0.6.0**：TeamMind（若走 K8s 路线，CheckpointRestore/PauseStrategy/Commit CRD 即现成原语）、silver-shield（恢复/克隆/CSI 重挂时重签 token，防旧身份复用）→ ✅ validated。
- **durable 品类卡**：补「控制面 vs 数据面」维度（生命周期 API 应与 sandbox 实现解耦），维持 🟡 观察，不升格。

### 能力树 agent-runtime.md
- 新增 **§七 第二周回灌**（与 §五 10-31 回灌分开记账，防止两周证据混成一条时间线）；§五 标题加指针。
- 明确记录未回灌项：缺口④ 未执行、集群实测受限、缺口⑤ 维持 🟡（MXC Entra 托管侧仍缺）。

## 结论与遗留
- Runtime 第二周闭环状态：**主体闭环完成**（候选→验证→回灌三环在本周内闭合：11-05 建卡 → 11-06 验证 → 11-07 回灌）。
- 未闭合项（不掩盖）：缺口④ TeamMind 权限模型 vs dsh/MXC 对照（B 级）顺延；集群级实测环境不可行，维持「未实测」。
- 11-08（周日）待办：第二周小结 + 换域判断（候选 Memory；若缺口④ 仍不执行，需在换域记录中显式挂账，避免「闭环完成」口号化）。
