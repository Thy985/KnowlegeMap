# 候选对象证据卡 · Strands Box（AWS OS 级 Agent 行为遏制沙箱，Dogwood 驱动）

> 状态：`[cand]` ｜ 关联方向：Agent Harness / 执行隔离（B 层）/ 权限策略（C 层）｜ 日期：2026-10-20（Harness 周 Day2 增量扫描）

## 一句话定位
AWS 2026-10-07 发布的**开源（Apache 2.0）OS 级 Agent 行为遏制沙箱**：以 OS 隔离（当前 macOS Seatbelt）建立硬边界，内嵌 Dogwood 策略引擎在网络出口/Python/Shell/MCP 多个拦截点对 agent 行为做细粒度放行/拒绝，支持**依赖历史行为的时间性策略**（频次/冷却/顺序约束）与**出站凭证外挂**（真实密钥不进 agent 环境）。

## 1. 它解决什么问题
- "YOLO mode"：coding assistant/自建 harness/成品 agent 普遍全批准执行，可游走出工作目录、执行危险命令、触达不该看的凭据
- 沙箱只能限"能触达什么"，不能限"能对触达之物做什么"——容器/microVM 强隔离不执行**上下文规则**（如：可读生产日志，但不可改）
- harness 自带权限运行在 agent 自身进程内、judge 的是工具调用而非其**效果**（看不到命令会碰哪些文件/哪些主机），且各 harness 规则格式不互通
- 策略需跨工具关联：`fs:read` 事件不论来自 shell 还是 Python 统一上报，可写"读了 customer-data 目录后禁止出站 HTTP"

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（官方博客）**：AWS Open Source Blog 2026-10-07 发布，developer preview，GitHub `strands-agents/box`，Apache 2.0 ["https://aws.amazon.com/blogs/opensource/introducing-strands-box-ai-agent-sandboxes-powered-by-dogwood/"]
- **FACT（机制）**：双层架构——containment（macOS Seatbelt 等 OS 级隔离）+ policy（Dogwood 语言，Cedar 语法 permit/forbid + when/temporal 子句）；enforcement points：egress gateway / Python interpreter / Shell interpreter / MCP broker；`box.toml` + `policy.dw` 双文件配置；harness agnostic（配 Strands Harness/LangChain/Claude Agent SDK）
- **FACT（差异化能力）**：
  - **时间性策略**：Dogwood temporal 算子（`formerly within 10m` + count），权限依赖 agent 已做之事（示例：Slack 发帖 10 分钟限 3 条，403 回执带 rule @id 与 @description 供 agent 自适应调整）
  - **凭证外挂网关**：agent 只见 placeholder token，网关出站时替换真实密钥（Bearer/custom header/Basic/query param/AWS SigV4），真实凭据永不进入 agent 环境——**与引擎 eval 层"凭据注入白名单"设计同构**
  - **拒绝可观测**：每个拦截点拒绝均返回 403 + 规则标识 + 描述，支持 agent 自纠（等待而非重试）
- **FACT（路线图）**：扩 OS（当前 macOS，目标多 OS 保留隔离保证）、CLI 自动探测已装 harness 生成 box.toml+基线策略、部署到 Bedrock AgentCore/ECS/K8s（策略随部署携带）、Dogwood 扩展 liveness（"必须最终发生"的义务检测）
- 与已覆盖对象**不重复**：MXC（Microsoft 侧策略驱动 OS 隔离，Bubblewrap/AppContainer 等后端，JSON 策略）vs Box（AWS 侧，Dogwood 策略语言 + 时间性 + 凭证网关）——**同一问题域的两大云厂商官方方案，天然适合周五对照验证**；NVIDIA OpenShell 已入 Harness-ControlPlane S 卡（沙箱+服务访问+凭据管理+形式化策略），Box 与其同向但属 AWS 开源线

## 3. 与我的连接
- **连接的项目**：
  - TeamMind（Java 多 Agent 运行时）：Box 的"OS 级策略强制 + 时间性约束 + harness agnostic"可作为 TeamMind 多 agent 信任边界的参照实现；`policy.dw`/`box.toml` 双文件模型可对照 TeamMind 权限模型设计
  - Tafcm（Dart 本地 LLM）：本地执行场景的 OS 级遏制边界设计（Seatbelt 类比）与 Dogwood 策略语言轻量子集可借鉴
  - silver-shield（反诈骗判定）：Box 网关"出站凭证外挂 + 目的地 permit"模式 = 反诈骗判定所需的确定性出站管控
  - campus_order（OpenClaw 智能体）：Box 对 OpenClaw 类 agent 的遏制（ClawKeeper 已覆盖 OpenClaw 侧，Box 是 harness 无关的 OS 侧补充）
- **连接的知识点**：Harness 能力树 B 层（执行隔离）B1 MXC → 新增 **B5 Strands Box**（AWS 对照线）；C 层权限策略（C2 无状态策略引擎 YAML/OPA/Cedar<0.1ms → Dogwood/Cedar 时间性扩展）；E 层威胁模型（10-19 事件集群 → Box 即其防御侧答案）
- **潜在收益**：周五验证计划①从"MXC 单卡对照"升级为 **MXC × Strands Box 双对照**（同域两大厂方案差异：JSON 策略 vs Cedar 语法、OS 后端谱系 vs 单 OS+扩展、凭据处理方式）；为引擎 eval 层 fail-closed 网络策略+凭据注入白名单提供**可运行的参考实现**（Box 网关模式）

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | AWS Open Source Blog ["https://aws.amazon.com/blogs/opensource/introducing-strands-box-ai-agent-sandboxes-powered-by-dogwood/"]；GitHub ["https://github.com/strands-agents/box"]；Dogwood 语言指南 ["https://dogwood-policy.github.io/dogwood/"]；Marc Brooker 配套文 ["https://aigovernance.com/news/aws-strands-box-raises-the-bar-for-agent-behavioral-containment"] |
| 证据等级 | FACT（官方博客+开源仓库） |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① 精读 GitHub README/box.toml/policy.dw 示例，核 OS 后端与 enforcement points；② 与 MXC 候选卡做差异对照（隔离后端/策略语言/凭证处理/时间性能力）——**并入周五验证计划①**；③ 评估 TeamMind/Tafcm 权限模型适配点 |
| 预期完成时间 | 2026-10-23（周五验证日） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->
**2026-10-23（周五验证日）——AWS 官方博客全文精读 + 与 MXC 官方博客双对照完成**：

### ✅ 一手证据核验（FACT 确认，独立来源×2）
- AWS Open Source Blog《Introducing Strands Box: AI agent sandboxes powered by Dogwood》全文精读，机制全部落实：
  - **双层架构**确认：containment（macOS Seatbelt 起步）+ policy（Dogwood Local Engine 内嵌）；"OS-level containment 建立硬边界 + 拦截点策略强制"为 AWS 明确设计立场
  - **enforcement points 确认**：egress gateway（全部出站流量代理）+ Python interpreter + Shell interpreter + MCP broker（运行在 Box 自身进程外，agent 以普通 bash/python3/MCP 命令经本地 socket 触达）
  - **统一事件语义确认**：跨工具归一（shell 读与 python 读同报 `fs:read`；curl 与 python HTTP 同报 `http:request`）——支持"读了 customer-data 后禁出站 HTTP"式跨工具规则
  - **时间性策略确认**：Dogwood temporal 算子（`formerly within 10m` + `count for (t: Timepoint)`），Slack 10 分钟限 3 帖示例完整；拒绝回执 = HTTP 403 + rule `@id` + `@description`（agent 自纠而非静默失败）
  - **凭证外挂网关确认**：5 种注入方式（Bearer token / Custom header / HTTP Basic / Query parameter / AWS SigV4）；agent 只见 placeholder，真实密钥永不进入 agent 环境；`secret.inject = "always"` 模式确认
  - **配置形态确认**：`box.toml`（环境/命令/工作目录/直接文件访问/工具/MCP 服务器/凭证绑定）+ `policy.dw`（Dogwood 规则，Cedar 语法 `permit`/`forbid` + `when`）；`box run --config box.toml` 启动
- 路线图确认：扩 OS（当前 macOS）、CLI 自动探测已装 harness 生成 box.toml+基线策略、部署至 Bedrock AgentCore/ECS/K8s、Dogwood 扩展 liveness（"必须最终发生"义务检测）

### 📊 MXC × Strands Box 双对照（周五验证计划①产出）
| 维度 | Strands Box（AWS，dev preview，Apache 2.0） | MXC（Microsoft，GA 10-07） |
|---|---|---|
| 定位 | 开源 OS 级行为遏制沙箱（开发者侧） | 平台级（OS）执行边界原语（平台/企业侧） |
| 策略语言 | Dogwood（**Cedar 语法** permit/forbid+when） | **统一 JSON schema** + 多语言 SDK |
| 时间性策略 | ✅ 原生支持（count/cooldown/ordering + history） | ❌ 未见（三模式 Learning/Permissive 记录活动，非策略时间算子） |
| 凭证处理 | ✅ 出站凭证外挂网关（placeholder→真实密钥，SigV4） | ⚠️ 部分（经 OpenShell 集成补凭据管理；自身未见同构网关） |
| 模式 | 逐点放行/拒绝（403+rule id） | Enforcement/Learning/Permissive 三运行模式（先观察后强制） |
| 策略双层 | 单层（box.toml+policy.dw） | 双层（workload 声明 + 组织 Intune 管理策略） |
| 隔离后端 | 当前 macOS Seatbelt（多 OS 计划中） | 多后端谱系（AppContainer/Seatbelt/Bubblewrap/Session/WSLc/MicroVM） |
| 生态 | harness agnostic（Strands/LangChain/Claude Agent SDK） | Copilot/Codex/Replit/OpenClaw/LM Studio/Unsloth 已接入；Claude Code 等排队 |
| 归属 | AWS 开源线（同 NVIDIA OpenShell 同向） | Microsoft 平台能力（含 Entra agent 身份归因 coming soon） |

**对照结论**：两者是同一问题域（"agent 不能是自身安全权威"）的两大云厂商官方答案，且能力互补——**Box 胜在细粒度策略语言+时间性约束+凭证网关**（更贴近引擎 eval 层"凭据注入白名单+fail-closed"的设计同构），**MXC 胜在平台级多后端+组织策略+三模式渐进打磨**（更贴近生产治理落地）。对引擎 eval 层的参考：Box 网关模式 = 凭据注入白名单的可运行实现；MXC Learning→Permissive→Enforcement = 最小权限策略打磨流程模板。

### 遗留问题
- 未跑通本机 demo（Linux 环境，Box 当前仅 macOS）；验证为源码/文档级（官方博客全文+机制逐项核对）
- Agent Mesh 身份层（MXC Entra agent attribution）为 coming soon，未落地可验证

## 6. 决策
- [x] 晋升 validated（≥2 条独立证据：AWS 官方博客 + MXC 官方博客双来源互证，机制逐项核对通过）
- [ ] 维持观察
- [ ] 拒绝（原因）
