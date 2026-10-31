# 候选对象证据卡

> 状态：`[cand]` ｜ 关联方向：Agent 平台 / Runtime（托管执行） ｜ 日期：2026-11-01

## 一句话定位
OpenAI DevDay 2026（9-29）重大平台路线发布：GPT-6.1 Sol（1/5 价格）、**Agents API public beta**（hosted execution+memory+tools+multi-agent+computer use）、**Dots always-on agents**（7×24 运行的个人 agent+独立云电脑）、Decisions API（Luna 分类路由，limited preview）。

## 1. 它解决什么问题
Agent 从"每请求一次推理"走向**持续运行的托管执行**——平台侧托管运行时（执行环境、记忆、工具、多 agent 编排、GUI 操作）成为主流交付形态；Decisions API 解决 agent 决策的路由/分类基座。对自研运行时（TeamMind）是"平台化替代 vs 自建"的路线参考系。

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- OpenAI DevDay 2026-09-29 官方发布，Agents API 进入 public beta（hosted execution/memory/tools/multi-agent/computer use）；
- Dots：always-on 个人 agent（Astra 驱动、独立云电脑、全天候运行）——"持续 agent"产品化拐点信号；
- Decisions API（Luna）limited preview——agent 决策层平台化；
- DevDay 官方社区公告（10-02）+ 多篇独立分析（Nathan Mzumara 10-05 "always-on agents arrived"）共振；与 GPT-6.1 Sol（价格 1/5）构成 Q4 最大产品簇。

## 3. 与我的连接
- **连接的项目**：TeamMind（多 Agent 运行时——平台托管执行是重要对照系）、Tafcm（可能用 Agents API 托管执行）、个人 Agent 体系
- **连接的知识点**：Runtime 周能力树（托管执行/生命周期/状态持久化）、durable 品类（always-on 需要 durable 支撑）、Dapr validated（自建基线与平台托管对照）
- **潜在收益**：判断"平台托管 vs 自建运行时"的边界；always-on agent 的 suspend-resume/记忆/成本模型参考

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | OpenAI 开发者社区 DevDay 公告（10-02）：`https://community.openai.com/t/devday-2026-announcements-and-developer-resources/`（经搜索片段核验，未 verbatim 全文）；OpenAI release notes：`https://openai.com/zh-Hans-CN/products/release-notes/` |
| 证据等级 | FACT（官方公告，待 verbatim 全文核验） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | 精读 DevDay 公告全文确认 Agents API 能力边界；对照 Runtime 周 9 向 durable 表定位"托管平台层位" |
| 预期完成时间 | 可顺延非阻塞（与 Runtime 周第二周并轨） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察
- [ ] 拒绝（原因）
