# 候选对象证据卡 · CoreBreak：三大主流 Agent 栈共有结构性安全缺陷（Black Hat 2026）

> 状态：`[cand]` ｜ 关联方向：**Agent 安全 / Harness 治理（领域外兜底）** ｜ 日期：2026-10-29（兜底扫描捕获）

## 一句话定位
**CoreBreak**（Black Hat 2026，研究者 Aviyam Ivgi & Hedi Ingber）揭示**贯穿三大主流 agent 栈的同一种结构性缺陷**——AWS Bedrock AgentCore（Strands SDK）、Google Agent Development Kit（ADK）、Vercel AI SDK harness 都把安全强制放在 agent 能触及的地方（模型周围：system prompt/内容过滤/拒绝训练）；绕过模型即绕过全部护栏。三厂商均已打补丁（AWS CVE-2026-18830 CVSS 8.6 / Google CVE-2026-18236 CVSS 9.3 critical / Vercel CVE-2026-64650+CVE-2026-64651），修复方向收敛为 **out-of-band policy enforcement（OBPE）**：强制放在 agent 触及不到的边界。

## 1. 它解决什么问题
- 行业护栏全部包在模型外（system prompt、内容过滤器、拒绝训练）——**绕过模型 = 绕过全部护栏**。CoreBreak 给出两条路径：
  1. 喂给 harness 一段"最新消息已含 tool call"的伪造 history → 工具以攻击者选定参数执行，模型与其周围所有 guardrail 一次都不触发（**caller-authored tool calls**）
  2. 在同一 history 中伪造"approved"确认事件 → human-in-the-loop 审批批准了**没有人看到过**的动作——审批机制本身成为攻击向量（**forged approval events**）
- 凭据窃取路径：注入指令驱使 managed browser / code-interpreter 工具读取 execution role 的云凭据并外泄——一般计算环境里环境云凭据让注入指令一步可及；typed, mediated tool grant 才把凭据留在边界后
- 三家大厂各自 patch 的同一动作：**把工具执行绑定到攻击者不能 author 的状态，拒绝外部提供的 tool call 与审批**

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（Black Hat 2026 + 3 厂商官方 CVE 修补，10 月中下旬披露）**：AWS CVE-2026-18830（CVSS 8.6）、Google CVE-2026-18236（CVSS 9.3 critical）、Vercel CVE-2026-64650/64651 ["https://urbangeekz.com/2026/10/corebreak-ai-agent-security-flaws/"]
- **FACT（独立实证，Redpanda research）**：3,621 trials × 4 模型（Claude Sonnet 4.6 / Haiku 4.5 / GPT-5 / GPT-5 mini）——仅 prompt 规则护栏失败 **57.6%**；OBPE 边界同批失败 **0.2%**；in-band reviewer 模型（读输出阻断）失败 58.6%（"能拒绝答案，但不能撤销已读取的记录/已落地的写入"）；OBPE 0.0% 失败、任务完成 66.2% vs reviewer 58.7%、安全有用完成 63.0% vs 19.7%、reviewer 多花 930 次模型调用
- **FACT（修复共识）**：研究者加固清单=拒绝 caller-authored tool calls + 执行时授权 + 减少继承权限 + 绑定工具调用到产生它的确切模型事件与授权状态；Redpanda 独立研究达同一结论——OBPE（确定性策略评估，微秒级零 token）vs 模型护栏（每步一次推理调用，成本延迟随能力增长）
- **与既有知识不重复**：与 Harness 周已验证的 dsh 凭据外注 / MXC & Strands Box 凭证外挂网关 / Google egress 外注服务凭据（同一设计原理线的第三方大厂确认）**互补强化**而非重复——CoreBreak 提供"护栏放错位置"的正向攻击证据 + 三厂商 CVEs；Archon（CVE-2026-111322，已并入事件集群卡）是控制面认证问题，不同缺陷类；Strands Box 是沙箱产品本体（已 validated），CoreBreak 涉及其 SDK 宿主栈 Bedrock AgentCore 的缺陷

## 3. 与我的连接
- **连接的项目**：
  - **silver-shield（运行时防御）——最强连接**：OBPE 直接是 silver-shield 的架构原则（策略在 agent 触及不到的边界）；CoreBreak 的"伪造审批事件"攻击为 silver-shield 的审批/授权模块提供真实攻击面清单
  - **TeamMind（多 Agent 运行时）**：tool call 作者验证 + 执行时授权 + 拒绝 caller-authored calls = TeamMind 工具调用的安全基线要求
  - Tafcm / agent-attention：本地 agent 栈若采用 harness 式工具执行，需防 caller-authored history 注入
- **连接的知识点**：能力树 agent-harness-governance.md **B 层（执行隔离）** 与 **E 层（威胁模型）**——CoreBreak 是"模型外护栏可整体绕过"的教科书级证据，与越权事件集群卡（内因性/外因性）并列；Harness 周已验证的 OBPE 原理线（dsh/MXC/Strands Box 凭据外注）获得独立大厂背书
- **潜在收益**：OBPE 决策原则可直接并入 silver-shield 架构文档；攻击模式清单（caller-authored tool call / forged approval event / credential exfiltration via managed tools）作为内部 agent 安全 checklist

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | Black Hat 2026 披露；三厂商 CVE（AWS CVE-2026-18830 / Google CVE-2026-18236 / Vercel CVE-2026-64650+64651）；Redpanda 研究 ["https://urbangeekz.com/2026/10/corebreak-ai-agent-security-flaws/"] |
| 证据等级 | FACT（Black Hat 会议披露 + 官方 CVE + 独立基准 3,621 trials） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① 精读 Black Hat 演讲材料/研究论文（若公开）；② 对照 silver-shield 架构：逐项映射 CoreBreak 两条攻击路径→现有防御缺口；③ 复核三家 CVE 描述与补丁说明（NVD/CVE 详情） |
| 预期完成时间 | 待安排（可顺延；Harness 周已验证 OBPE 线，本卡补强证据） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [ ] 维持观察
- [ ] 拒绝（原因）
