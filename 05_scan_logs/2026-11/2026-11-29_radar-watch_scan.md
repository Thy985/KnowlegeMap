# 2026-11-29 深耕（Computer Use / Browser 第一周 Day7 · 周小结 + 换域判定）

- 领域：Computer Use / Browser（11-23~11-29，一周驻留）
- 任务类型：周日小结 + 换域判断（按 README 每日分工）。本轮**不新扫描**，只审计已有产出并做交接。

## 三环审计

| 环 | 状态 | 证据 |
|---|---|---|
| 候选 | ✅ 完整 | 能力树 A~H 44 节点 / 锚点 21 行 / 判断 11 条 / 缺口 6 项；新卡 3 张（agent-desktop A、GUI 回放与效果核验品类 A、本地控制面暴露 A），WebMCP A 入 Day2；既有 S/A 卡补 §3.9 |
| 验证 | ✅ **源码级** | browser-use 1.0.8（无 DOM serializer / judge 与 actor 共享前缀 / `state/cells` 第二级证据）；@playwright/mcp 0.0.86（并入 playwright-core / ref 无 stale 语义 / P8 非 loopback 时 Host 检查关闭）；本地控制面 9 模式（本机 9222 `/json/version`、`/json/list` 只读）。**无一项实跑** |
| 回灌 | ✅ 完整 | 能力树 §十一（锚点 4 行 / 缺口 3 行 / 判断增补 / 挂账）；connections 4 条；graph 4 边；06 index 置顶段；`_INDEX` 行；11-28 日志 |

## 结案口径

1. **结案口径＝源码级**，与判断 11 一致：跨周引用必须带「源码级」限定语，不得与实跑级 validated 混排。
2. **不宣称闭环完整**：7 项执行级验证未做——profile 目录权限、browser-use 最小 demo（需独立 profile）、`@playwright/mcp` 端到端 call、Webwright CLI 实跑、DNS rebinding PoC、P8 真实 `--host 0.0.0.0` 启动、agent-desktop 包级核对。①②③ 转 silver-shield / E2E-CLI / Tafcm 施工项；④⑤⑥⑦ 留域内挂账。
3. 域内未解决：表示与动作空间缺选择函数（ComponentBench 只有相关性）；回放确定性只有品类级证据（OpenAdapt 54/90→9/90→0/90），重放度未实测。

## 换域判定

**Computer Use / Browser → AI Infra / 本地边缘（11-30 起，第一周）**。依据：三环在声明深度上闭合；剩余项依赖真实 GUI / 独立 profile，属项目施工而非雷达周；下一域有真实施工需求（Tafcm 本地推理 6GB 显存、campus_order 本地部署），且是顺序表末段。

携带判据：判断 9（入口 × 绑定/传输形态）、判断 11（证据深度分级）→ 分别落到「本地推理服务 bind/认证」与「厂商 bench 默认按包级」。

## 写入清单

1. `08_agent_centric/domains/agent-computer-use.md`：新增 **§十二 第一周小结与结案口径**（12.1 三环 / 12.2 结案口径与不宣称部分 / 12.3 四条可复用结论 / 12.4 留在域内的理论问题）。
2. `07_radar_watch/current_focus.md`：换域为 AI Infra / 本地边缘（目标 A~H 八层、已知锚点、七日分工）；换域记录新增 11-29 条目；换域规则改为顺序表末段；历史聚焦记录 Computer Use 行改结案 + 新增 AI Infra 行。
3. `04_connections/README.md`：新增「2026-11-29 周小结」3 条交接（入口×形态 → 本地推理；bench 包级 → Tafcm/E2E-CLI；默认值只在默认硬件成立 → 6GB 显存）。
4. `08_agent_centric/capabilities/graph.md`：新增 3 边（guard-coverage-scope / noise-vs-signal-bench / local-edge-viability → ai-infra、tafcm-local）。
5. `06_expansion_index/README.md`：置顶 11-29 周小结段（无新增对象）。
6. `_INDEX.md`：新增 11-29 行（🟡）。

## 未做 / 限制

- 未做增量扫描（周日分工只做小结）。
- 下一域能力树未建，按分工留给 11-30 周一。
- AI Infra 锚点仅登记、未核（SGLang v1.0 / vLLM 0.34.0 的版本与默认值需周一回一手源确认，ROCm 10.2 捆的 vLLM 0.32.0 与 11-16 的 0.34.0 存在版本落差，需分辨「主线版本 vs 发行版捆绑」）。
