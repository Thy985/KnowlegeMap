# 候选对象证据卡 · AAIF 四项目托管：Agent 协议/标准 vendor-neutral 治理收敛

> 状态：`[cand]` ｜ 关联方向：**Agent 标准治理 / 协议层（领域外兜底）** ｜ 日期：2026-10-29（兜底扫描捕获）

## 一句话定位
**Linux Foundation 的 Agentic AI Foundation（AAIF）2026-10-22 在 AGNTCon + MCPCon North America（San Jose）新增四个托管项目**：Anthropic **Agent Skills**（SKILL.md folder 格式）、OpenAI **Open Responses**（Responses API 派生多提供商 API 规范）、Hugging Face **OpenEnv**（RL 环境框架，MCP+Gym）、Alibaba **OpenSandbox**（agent 沙箱执行平台，Docker/K8s）——托管项目 3→10（既有 MCP/goose/AGENTS.md/A2A/Agent Router/agentgateway）。核心变化是 **vendor-neutral 治理**：四大竞争厂商的标准资产由单一基金会共治（Platinum 成员含 AWS/Google/Microsoft/Anthropic/OpenAI/Cloudflare/Block/Bloomberg）。

## 1. 它解决什么问题
- agent 工程实践的**协议/标准碎片化**：每家厂商有自己的 skills 格式、API 规范、执行沙箱——锁定风险高
- AAIF 治理把资产从"某厂商文档"变为"基金会规范"：Agent Skills 格式（SKILL.md 目录）stewardship 移入基金会（70+ 平台支持、skills.sh 注册表 7 个月 1M+ skills、~2.8 亿安装——AAIF/Vercel 数据非独立审计）；Open Responses 使多模型 API 层的 endpoint/model 配置化（Databricks Model Serving 已暴露 Open Responses 端点服务 Claude/Gemini/开放模型，Vercel AI Gateway 提供 OpenResponses API）；OpenSandbox 提供统一沙箱 API（Python/Java-Kotlin/TS-JS/C#/Go SDK + osb CLI + MCP server）
- **注意边界**：治理不是供应链安全——skills 可携带脚本与链接（上月的 placeholder-domain 攻击）；AAIF 明确 skill 提供指令而非权限

## 2. 为什么现在值得关注（新颖度/活跃度证据）
- **FACT（Linux Foundation 官方新闻稿 + AAIF 公告，2026-10-22）**：四项目托管，AAIF 3→10 ["https://technologypulse.app/2026-10-24-aaif-agent-skills-open-responses-openenv-opensandbox/"]
- **FACT（项目与实现现状）**：Agent Skills 仓库 agentskills/agentskills（Apache 2.0 code/CC BY 4.0 docs）；Open Responses 仓库 openresponses/openresponses（Apache 2.0 + compliance tester，spec 公开，Databricks/Vercel 两家实现）；OpenEnv huggingface/OpenEnv（reset/step/state 客户端对容器化环境服务器，可发布到 HF Spaces，TRL 集成）；OpenSandbox opensandbox-group/OpenSandbox（Apache 2.0）
- **FACT（成员格局）**：Platinum 层含 AWS、Google、Microsoft、Anthropic、OpenAI、Cloudflare、Block、Bloomberg——**两大闭源巨头（OpenAI+Anthropic）与三大云（AWS/Google/MS）同基金共治**
- **未确认（保守标注）**：无 SKILL.md/Open Responses schema 变更公告；无官方认证/SLA 计划；无 Anthropic API 原生支持 Open Responses 的承诺——"基金会标志 ≠ 行业采纳"
- **与既有知识去重**：AAIF 本体/MCP/A2A/AGENTS.md/Agent Router/agentgateway 已在覆盖（各卡/日志）；**Agent Skills / Open Responses / OpenEnv / OpenSandbox 四资产为新增对象**——AAIF 10 项目收敛是跨厂商标准治理的结构性变化

## 3. 与我的连接
- **连接的项目**：
  - **agent-attention / Tafcm（本地 agent 栈）**：Agent Skills 是 SKILL.md folder 规范（与 doubao skills 体系同构参照）——本地 agent 若兼容 skills 格式，可对接 70+ 平台生态；Open Responses 为多模型 API 层提供中立 schema（本地多 provider 网关参考）
  - **silver-shield（运行时防御）**：OpenSandbox 的统一沙箱 API 是"沙箱执行层标准"候选；AAIF 明确"skill 不携带权限"——与 silver-shield 权限模型互补
  - TeamMind：A2A/Agent Router 同基金治理 → 多 agent 互操作标准基线
- **连接的知识点**：能力树 agent-runtime.md **E 层（运行时身份与网络策略）** 与 **F 层（生命周期）** 相邻——标准治理收敛影响 runtime 的协议接口选择；Harness 周 agent 防火墙品类（skill 供应链风险）与"治理非安全"边界直接呼应
- **潜在收益**：选型决策依据（协议标准走向）；多 provider API 适配策略（Open Responses compliance tester 可测现有 gateway）；skill 生态对接窗口

## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源（官方文档/源码/论文/Release URL） | Linux Foundation 新闻稿（10-22）["https://www.linuxfoundation.org/press/agentic-ai-foundation-announces-four-new-projects"]；AAIF 博客四篇（Agent Skills/Open Responses/OpenEnv/OpenSandbox）；仓库 agentskills/agentskills、openresponses/openresponses、huggingface/OpenEnv、opensandbox-group/OpenSandbox；分析 ["https://technologypulse.app/2026-10-24-aaif-agent-skills-open-responses-openenv-opensandbox/"] |
| 证据等级 | FACT（基金会官方公告 + 公开仓库）；采纳度数字为 AAIF/Vercel 自述非独立审计 |
| 验证方式（跑通 demo / 精读源码 / 对照实验） | ① 精读四篇 AAIF 公告与各仓库 README/spec；② Open Responses compliance tester 跑本地 gateway 对照；③ 评估 Agent Skills 格式与本地 skills 体系的互操作性 |
| 预期完成时间 | 待安排（可顺延至标准治理相关周） |

## 5. 验证结果
<!-- 验证后回填：实际结果、遗留问题、是否进入 validated -->

## 6. 决策
- [ ] 晋升 validated（≥2 条独立证据）
- [ ] 维持观察
- [ ] 拒绝（原因）
