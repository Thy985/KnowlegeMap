# 回灌日志 · 2026-10-17（Personal Tech Radar · Evaluation 周 Day6 · 周六回灌）

> 周六分工：把周五验证结果回灌 index / connections / 能力树。素材源：2026-10-16 验证日志（评测可信度三环 + 引擎 eval 层建议 5 条 + 评测隔离检查）。

## 回灌动作
1. **能力树（agent-evaluation.md）**：补「评测可信度三环」到 A3/C3/D1/B2 节点证据；评测隔离 C1/C4 落地检查结论写入 C1/C4；引擎 eval 层落地建议映射到对应层
2. **Capability Graph（capabilities/graph.md）**：补 evaluation 跨域边（judge-calibration / replayable-tests / eval-isolation / evidence-chain）
3. **Connections（04_connections/README.md）**：新增 Evaluation 周连接 6 条（AgentJudgeBench / Transect / TestJack / 求索 4.0 / LiveMACE / 评测隔离事件）
4. **候选 → validated / dropped 决策**：三环候选（AgentJudgeBench / Transect / TestJack）均维持观察（缺公开代码仓库复现，未达 validated 门槛）；本周新增 8 张候选卡全部保留，无 dropped
5. **去重基准（06_expansion_index/README.md）**：追加本轮回灌段，无新对象

## 三环方法论 → 能力树映射
| 环 | 对象 | 量化证据 | 能力树节点 | 引擎落地 |
|---|---|---|---|---|
| judge 侧 | AgentJudgeBench | 对齐度随难度下降；无 GT 退化 1.5x；喂 GT 反损 | A3 / D1 / D3 | judge 校准约束：程序化断言优先，LLM-judge 次级信号；hard 任务配程序化验证 |
| 评测者/transcript 侧 | Transect | 1300 万 token 案例；回合时间线+标签溯源 | B2 / B4 | 证据链数据模型：回合时间线+标签可追溯（与 Validation 编译器同构） |
| 补丁/测试侧 | TestJack | 34.4% 判正确 trial 违规；resolution 50.6%→33.2% | A3 / C3 | 可回放测试：动态测试生成→只保留 GT 通过的→失败可回放 |

## 评测隔离 C1/C4 落地检查（对照 DeepSeek Harness validated 卡）
- DeepSeek Harness 提供 **sandbox / approval / permission-presets / credentials seam / session-telemetry-otel**——属**运行时隔离**（agent 执行期）
- Evaluation 层缺口：**eval harness 需 fail-closed 网络策略**（eval 默认不出网，测试目标与外部网络隔离），对照 10-11 Anthropic 事件三隔离（网络/凭据/外部目标）
- 结论：引擎 eval 层落地时，评测执行与 agent 执行共用 sandbox 能力，但 eval 场景需追加"评测专用网络策略 + 凭据注入白名单"，不能复用运行时默认策略

## 引擎 eval 层落地建议（5 条，待实现）
1. judge 校准约束：关键结论不依赖单一 LLM 打分，程序化断言优先，LLM-judge 仅次级信号
2. 难度分层：hard 任务 judge 可靠性预期下降，配程序化验证
3. 证据注入受控：喂 GT 可能反损对齐，评测设计非"信息越多越好"
4. 可回放测试：动态测试生成替代固定测试，失败可回放（避免 34.4% 系统性偏差）
5. 评测隔离：eval 层 fail-closed 网络策略 + 凭据注入白名单

## 决策汇总
- 维持观察（3）：AgentJudgeBench / Transect / TestJack —— 方法论已闭环，代码/复现待后续
- 保留待后续周验证（5）：求索 4.0（国内参照系，本周素材已并入能力树 A2/A4）、LiveMACE（B+，动态/持久评测方法论留待 Memory 周）、ReviewBench（Harness/治理周参照）、MXC / Protocol Pivoting / ToFu / GHOSTJACKING（领域外，MCP 安全/治理周验证）
- dropped：0

## 结论
**Important**（周六回灌完成：三环方法论/评测隔离/引擎建议已落入能力树、graph、connections；候选决策明确；周小结与换域判断待周日 10-18）。
