# Personal Tech Radar 深耕扫描日志 · 2026-11-08（Runtime 周第二周 · 周日小结 / 换域判断）

> 领域：Runtime，第二周（11-02~11-08）。当天分工：**本周小结 + 判断是否换域**。不新增扫描。

## 1. 两周闭环审计
| 缺口 | 状态 | 依据 |
|---|---|---|
| ① Dapr Agents 实测 | ✅ 闭环（10-30） | 官方文档全文 + pip `dapr-agents 1.1.0`；环境无 Docker，未实跑中断 demo（按先例判定 validated） |
| ② Agent Substrate 复现 | ✅ 闭环（11-06） | `agent-substrate/substrate` clone；`go build ./cmd/...` exit 0；gRPC Suspend/Resume、SPIFFE、egress 外注、request parking 全部文档+代码核对 |
| ③ durable 品类横向 | ✅ 闭环（10-30） | 9 向对照表（11-03 再补 2 向观察） |
| ④ TeamMind 权限 vs dsh/MXC | ❌ 未执行（B） | 显式挂账，随 Memory 周携带 |
| ⑤ Agent Mesh 身份层 | 🟡 部分 | 开源侧（Substrate SPIFFE/per-actor JWT/恢复重签）确认；托管侧 MXC Entra 仍缺 |

## 2. 净产出（两周）
- validated 锚点 2 个：**Dapr Agents**（10-30）、**Agent Substrate**（11-06，代码级）。
- validated 品类卡 1 张：`[val]sandbox-lifecycle-suspend-resume-2026-11.md`（OpenKruise v0.6.0 源码核对）。
- 观察中：durable 品类卡（9+2 向，🟡）、AWS Infinity（B，🟡）。
- 知识结构：graph 新增 7 条跨域边（第一周 3 + 第二周 4）；connections 新增/升级 4 行。
- 事实修正：`cmd/` 实为 **14** 个二进制（此前多处 15，已全库修正）；Titanium IPU 属 ACE 托管侧。

## 3. 未完成与限制（如实记录）
- **集群实测未做**：无 Docker/kubectl/K8s；Substrate 的 10x 密度 / <500ms resume / >500 activations/s 与 OpenKruise freeze-resume 均为官方口径或代码推断。仓库内 `benchmarking/locust`、`nighthawk-*` 为有环境后的第一动作。
- **缺口④ 未执行**：不因换域而视为消失，已转挂 Memory 周（记忆作用域与权限同源）。
- 缺口⑤ 托管侧超出当前可验证范围（无 MXC 账号/环境），继续观察、不设期限。

## 4. 换域判定：Runtime → Memory（2026-11-09 周一起）
判定标准（README：唯一标准是三环闭环）：
1. **三环闭合**：候选 → 验证 → 回灌两周内完成，无「只收集不验证」的悬挂候选。
2. **双锚点落地**：Dapr（步骤持久化/event sourcing）与 Substrate（挂起恢复/snapshot）构成 durable 两派的可对照基线，且均为公开可复现。
3. **剩余缺口不阻塞**：④ 为 B 级且已挂账、⑤ 托管侧环境不可达，继续留在 Runtime 周无法推进。
> 结论：**换域 Memory**。携带输入：① Runtime 的「执行状态 ≠ 会话记忆」分层结论；② 11-07 兜底事件日 13 的跨会话记忆注入威胁，作为 Memory 周首要威胁素材。

## 5. 落位动作
- `08_agent_centric/domains/agent-runtime.md` 新增 **§八 第二周小结 + 换域判定**（8.1 产出 / 8.2 缺口审计 / 8.3 限制 / 8.4 判定 / 8.5 遗留清单）。
- `07_radar_watch/current_focus.md`：当前领域改为 **Memory（周起始 2026-11-09）**，写入目标/已知锚点/本周每日分工/换域记录；Runtime 历史行状态改 ✅ 并补第二周收尾。
- 全库事实修正：`15 个二进制` → `14 个二进制`（6 个文件 9 处）。
- 06 index 与 _INDEX 追加本段/行。
