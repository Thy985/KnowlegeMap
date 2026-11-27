# 2026-11-28 深耕扫描（Computer Use / Browser · 第一周 Day6 · 周六回灌）

- 当前领域：Computer Use / Browser（第一周，11-23~11-29）。今日分工＝**验证结果回灌**，不做新扫描、不追增量（按 README「周六：更新 index / connections / 能力树」）。
- 输入：Day5（11-27）三次源码级核对 + 本机只读实测 + 11-27 兜底捕获的 jupyter CVE-2026-77359。

## 回灌判定（不涉及新对象，全部为状态与结论落位）

| 对象 | 变化 | 落点 |
|---|---|---|
| browser-use 1.0.8 | `[cand]` → **validated（源码级）** | 能力树 2.1 锚点行 + §十一 11.1 |
| @playwright/mcp 0.0.86 | `[cand]` → **validated（源码级）**，含新缺陷 P8 | 同上 |
| 本地控制面清单 | 7 模式 → **9 模式 validated** | 锚点行 + 缺口① |
| Webwright 0.0.7 | 等级统一 **B**，维持观察 | 锚点行 |
| jupyter CVE-2026-77359 | 不入候选卡，作**判断 9 第三例**入锚点表 | 锚点表新增 1 行 |

## 写入清单

1. `08_agent_centric/domains/agent-computer-use.md`：2.1 锚点 4 行状态改写 + 新增 jupyter 行；2.4 缺口 ①②④ 回填；判断 9 强化（三例同构 → 入口×形态逐格清点）；新增判断 11（证据深度分级）；新增 **§十一 Day6 回灌**（11.1 锚点变更 / 11.2 缺口回填 / 11.3 判断增补 / 11.4 落到别处 / 11.5 未做挂账）。
2. `04_connections/README.md`：新增「2026-11-28 回灌」4 条（校验二维清点 → silver-shield；判分独立性 → E2E-CLI/Tafcm；持久等级 → E2E-CLI；部署形态显式登记 → Tafcm/campus_order）。
3. `08_agent_centric/capabilities/graph.md`：新增 4 边（guard-coverage-scope / judge-independence / artifact-persistence-tier / deployment-shape-validity）。
4. `06_expansion_index/README.md`：置顶 11-28 回灌段（状态变更，无新增对象）。
5. `_INDEX.md`：新增 11-28 回灌行（🔁）。
6. `07_radar_watch/current_focus.md`：状态行加 Day6；周六行勾选并写摘要。

## 未做 / 限制

- 未新扫描（周六按分工只回灌）；无新增候选卡、无 S/A 新对象。
- agent-desktop 包级核对顺延（周五时间用满三候选）。
- profile 目录权限、browser-use 最小 demo、`@playwright/mcp` 端到端 call、Webwright CLI、DNS rebinding PoC、P8 真实 `--host 0.0.0.0` 启动验证：均未执行，交周日小结时决定是否随「最小驻留」延长。
