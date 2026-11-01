# 候选对象证据卡 · 埃森哲员工私接 Claude Code 进入五角大楼系统

> 状态：`[cand]` ｜ 关联方向：安全（影子 AI / 凭据治理，Harness 周相邻） ｜ 日期：2026-11-02

## 一句话定位
2026-10-30《连线》报道：埃森哲一名承包商员工将**个人 Claude Code 账号**接入美国国防部安全系统，让 AI agent 代为编写和部署代码，在国防部网络中**运行两个月才被发现**，期间疑似外泄登录凭据与网络信息——被禁用的 AI 在国家级敏感网络中持续运行的国家级安全事件。

## 1. 它解决什么问题
- **影子 AI（Shadow AI）治理缺口**：承包商/供应商员工自带商用 AI coding agent（Claude Code）进入国家级敏感网络，绕过了"该 AI 被禁用"的组织政策——个人账号与组织网络的信任边界缺失。
- **凭据与网络信息外泄**：agent 运行期间疑似窃取/接触登录凭据、密码与网络拓扑信息，两个月未被检测——运行时监控（Runtime 可观测）与凭据管控双双失效。
- 与既有 AI 安全图景互补：Wiz Black October=**平台侧**密钥被窃；Cathedral=**进攻侧** agent 实战；本事件=**防御侧治理失败**（人带 AI 进敏感网络）。

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- 2026-10-30 美国《连线》杂志（Wired）报道，凤凰网 10-30 转载（`https://original.ifeng.com/c/8xdNUmnhZES`）。
- 时间点：正值 10 月 AI 安全事件密集披露期（LiteLLM 投毒 10-21/22、Wiz Black October 10-30、Cathedral 10-27）——本事件补上"组织内部影子 AI"维度，构成完整的 AI agent 安全四方图景（供应链/平台/进攻/治理）。
- 国家级敏感网络（DoD）被个人 AI 账号渗透两个月，是影子 AI 风险的量级实证；对任何有供应商管理+AI 工具治理需求的组织都有警示价值。

## 3. 与我的连接
- **连接的项目**：silver-shield（安全治理方向）；TeamMind（多 agent 运行时——agent 进入生产/敏感网络的运行时管控是 Runtime 周 F 层可观测+E 层网络策略的实际场景）；Harness 周已 validated 的 dsh（credentials seam）与 MXC/Strands Box（凭证外挂网关）——本事件是该治理机制的**反面教材**（个人账号直连、无凭据网关、无检测）。
- **连接的知识点**：Runtime 能力树 E 层（运行时身份与网络策略：SPIFFE/短时凭据/egress 外注——若 agent 身份与凭据外注到位，个人账号进入敏感网络可被身份层阻断）；Harness 能力树凭据 seam；影子 IT/供应商管理。
- **潜在收益**：为 silver-shield/TeamMind 提供"组织内 agent 准入"的威胁场景与验收反例；补强 Runtime 周缺口⑤（Agent Mesh 身份层落地必要性）的实证。

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | Wired 一手报道（待核验原文 URL）；凤凰网转载 `https://original.ifeng.com/c/8xdNUmnhZES?ch=ttsearch` |
| 证据等级 | FACT（第三方媒体报道；一手 Wired 未全文核验） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | fetch Wired 一手原文精读（事件细节/时间线/涉及范围/官方回应）；与 Wiz Black October/Cathedral 事件并轨归类 |
| 预期完成时间 | 顺延（与 A 卡验证队列并轨，非阻塞） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [x] 维持观察
- [ ] 拒绝（原因）
