# 候选对象证据卡 · Microsoft Execution Containers (MXC)（OS 级 Agent 策略隔离层，GA）

> 状态：`[cand]` ｜ 关联方向：Agent Runtime / 安全治理 / 沙箱（兜底捕获，非当前深耕领域）｜ 日期：2026-10-14（兜底扫描）

## 一句话定位
微软 2026-10-07 宣布 **GA** 的策略驱动 Agent 执行隔离层：**agent 不能成为自身的安全权威**——边界由开发者/组织在 agent 之外声明、由 OS 独立强制执行，agent 或其生成代码无法自我授权。统一 JSON 策略 + 多语言 SDK，映射到 Windows/macOS/Linux 容器后端。

## 1. 它解决什么问题
- 二选一困境：给 agent 无限制访问（赌不出事）vs 全部封锁（失去生产力）
- 核心命题：**"An agent cannot be its own security authority. It must run within a boundary defined by the developer or organization and enforced independently of the agent itself."**
- 典型场景：coding agent 可读写仓库、可读生产配置理解部署，但**不能改生产配置**——即使模型认为改配置是完成任务最快路径，隔离层也阻止该操作
- 策略在 agent 工作负载控制之外，agent/generated code/plugin/tool 无法自我提权

## 2. 关键机制（FACT，官方文档）
- **隔离后端谱系**：
  - Process container（Win11/macOS/Linux；AppContainer / Seatbelt / Bubblewrap）——轻量，模型生成代码与工具执行
  - Session container（Win11 独占；独立 Windows 账户/会话，隔离桌面/剪贴板/UI/输入）——长时程 agent
  - WSLc（Win11；Linux 工具链）
  - MicroVM（Win11/Linux，**实验性**；硬件支撑隔离）
- **五类策略域**：Containment / Process / File system（可写/只读/不可见）/ Network（含 loopback 出入站）/ UI（桌面交互）
- **三运行模式**（先观察后强制）：Enforcement（阻断）/ Learning（阻断+记录 JSON 活动报告）/ Permissive（允许+记录，用于起草最小权限策略）
- **双层策略**：开发者声明 workload 需求 + 组织 Intune 管理策略叠加，同一 agent 可在不同企业边界内运行
- **Identity 归因**：Microsoft Entra 将区分 agent 活动 vs 人类活动（coming soon），安全控制可单独针对 agent 而不影响员工
- **生态**：已接入 GitHub Copilot、**OpenClaw**、OpenAI Codex、Replit、LM Studio、Unsloth；NVIDIA OpenShell 集成（文件/推理服务访问控制、网络控制、凭据管理、OCSF 审计）；即将支持 Claude Code、Manus、Perplexity、Raycast 等；Windows 365 Cloud PC 支持

## 3. 为什么现在值得关注（新颖度/活跃度证据）
- **一手证据（FACT）**：Windows Developer Blog 2026-10-07《Microsoft Execution Containers: Policy-driven containment for AI agents》（GA 公告）+ Microsoft news 同日官方稿；MXC SDK 最初在 Build 2026（06-02）公布，10-07 GA
- **新颖点**：不是又一个 agent 框架，而是**平台级（OS）执行边界原语**——把"agent 权限边界"从应用层约定提升为 OS 强制；与 E2B（云沙箱）互补，这是本地/桌面侧的答案
- **活跃度**：GA 即有 Copilot/Codex/Replit/OpenClaw 等首批接入，生态信号强

## 4. 与我的连接
- **连接的知识点**：架构原则 20（安全边界：Task Risk / Permission / Environment / Approval / Sandbox，fail-closed）——MXC 是该原则的官方范式与可落地参考；三模式（Learning/Permissive/Enforcement）与 Evaluation 周的"执行观测"交叉
- **连接的项目**：
  - **Tafcm**：本地/桌面 agent 运行，Linux 后端即 Bubblewrap——JSON 策略 schema 与进程沙箱可直接借鉴
  - **TeamMind**：多 Agent runtime 的策略层（workload 声明 + 组织策略双层）
  - **campus_order（OpenClaw）**：OpenClaw 已为首批支持 MXC 的 agent，可直接观察其集成方式
- **潜在收益**：① 统一 JSON 策略 schema 设计（五域）可作为引擎/TeamMind 权限模型的外部参照；② Learning→Permissive→Enforcement 渐进式策略打磨流程，可迁移到任何最小权限落地；③ 跨平台后端映射表（AppContainer/Seatbelt/Bubblewrap/MicroVM）是本地沙箱选型的现成清单

## 5. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://blogs.windows.com/windowsdeveloper/2026/10/07/microsoft-execution-containers-policy-driven-containment-for-ai-agents/ ；https://developer.microsoft.com/en-us/windows/agentic |
| 证据等级 | **FACT**（微软官方，多页面互证） |
| 验证方式 | ① 拉取 MXC SDK/文档，检查 JSON schema 与 Linux Bubblewrap 后端实际形态；② 对照 Tafcm/TeamMind 权限模型写一份差异分析；③ 观察 OpenClaw 的 MXC 集成 commit |
| 预期完成时间 | 留待 Harness/治理周或 Runtime 周（接 TeamMind）验证 |

## 6. 验证结果
<!-- 验证后回填 -->
**2026-10-23（周五验证日）——Windows Developer Blog 官方 GA 公告全文精读，机制全部落实（FACT 确认）**：

### ✅ 一手证据核验
- **GA 状态确认**：10-07 GA 公告（Logan Iyer），"agent 不能是自身安全权威"核心命题原文确认
- **五类策略域确认**：Containment / Process / File system（可写/只读/不可见）/ Network（含 loopback 出入站）/ UI（桌面交互）
- **三运行模式确认**：Enforcement（阻断无报告）/ Learning（阻断+JSON 活动报告）/ Permissive（放行+记录，供最小权限起草）——活动报告仅 Windows process container 产出
- **后端谱系确认**：Process container（Win11/macOS/Linux：AppContainer/Seatbelt/Bubblewrap）/ Session container（Win11 独有：独立账户+会话+隔离桌面/剪贴板/UI/输入）/ WSLc（Win11）/ MicroVM（Win11/Linux 实验性，硬件支撑）
- **双层策略确认**：workload 声明 + Intune 组织管理策略（soon），同一 agent 可运行在不同企业边界
- **生态确认（官方伙伴矩阵）**：已接入 GitHub Copilot、OpenClaw、OpenAI Codex、Replit、LM Studio、Unsloth AI；即将支持 Anthropic Claude Code、Box、Egnyte、Heidi Health、Hermes（Nous）、Manus、Perplexity、Raycast、Simular；**NVIDIA OpenShell 已集成**（文件/推理服务访问控制+网络控制+凭据管理+OCSF 审计）；Windows 365 Cloud PC GA
- **Identity 归因确认**：Entra agent 身份区分（coming soon），安全控制可只针对 agent 不影响员工

### 📊 MXC × Strands Box 双对照（见 Strands Box 卡 §5）
**MXC 侧结论**：平台级治理强（多后端谱系/组织策略/三模式/身份归因），细粒度策略表达弱于 Box（JSON 无时间算子，凭证处理依赖 OpenShell 集成补位）；"Learning→Permissive→Enforcement"渐进打磨流程是生产落地最小权限的最佳实践模板。

### 遗留问题
- 本机为 Linux，Session/WSLc 后端不可测；Bubblewrap 后端具体 schema 未逐项对照
- Entra agent 身份归因为 coming soon，未落地可验证

## 7. 决策
- [x] 晋升 validated（≥2 条独立证据：微软官方 GA 公告全文 + 生态矩阵/后端谱系逐项核对）
- [ ] 维持观察
- [ ] 拒绝（原因）
