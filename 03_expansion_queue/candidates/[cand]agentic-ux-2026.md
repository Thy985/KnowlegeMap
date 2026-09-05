# 候选证据卡 · [cand] Agentic UX / AI 原生产品设计模式（2026）
> 状态：`[cand]` ｜ 分类：AI 原生产品 / Agentic UX（G2 空白区） ｜ 发现：2026-09-06（雷达 #5） ｜ 等级：**B**
## 一句话定位
2026 年 Agentic UX 已从口号沉淀为可复用设计模式体系：Agentic Design（模式库）、AI UX Playground 五级自主度框架（L1 Suggest→L5）、Smashing Magazine 六模式（Pre-Action/Confirm/Consent）、zylos 四层前端栈（Approval orchestration/组件库/Activity panel/Error surface）——"copilot UX ≠ agentic UX"，交互模型从"建议-用户执行"转向"计划-审查-委托"。
## 1. 它是什么 / 解决什么问题
- 痛点：agent 自主规划执行多步任务后，用户失去掌控感与信任；对话界面本身不足以承载"自主性边界、不确定性、任务交接、数据使用、恢复操作"["https://agentic-design.ai/zh/patterns/ui-ux-patterns"]
- **Agentic Design**（模式库）：人在环内/环上控制、渐进式披露、置信度可视化、混合主动工作流；MCP Apps 在 Claude/ChatGPT/VS Code 的出现加速 UI 层标准化["https://agentic-design.ai/zh/patterns/ui-ux-patterns"]
- **AI UX Playground 五级自主度**：L1 Suggest / L2 Draft / L3 Confirm / L4 Bounded / L5（Monitor）——滑动条式自主度设计["https://www.aiuxplayground.com/frameworks/agentic/"]
- **Smashing Magazine 六模式**：Pre-Action → Confirm → Consent…，遵循 agentic 交互功能生命周期["https://www.smashingmagazine.com/2026/02/designing-agentic-ai-practical-ux-patterns/"]
- **zylos 四层前端栈**：Approval orchestration（LangGraph interrupts 等框架原生门控）、组件库（预审 UI 目录）、Activity panel（独立审计层）、Error surface（结构化三段错误消息）["https://zylos.ai/research/2026-05-28-agentic-ux-frontend-design-patterns-ai-agents/"]
- 高频模式：diff 预览即确认（inline diff approvals）、背景模式异步任务+完成通知、plan-as-code 可见可编辑、manager surface（agent 专属操作空间）["https://github.com/bitcomplete/agentic-craft/blob/main/docs/research.md"]
## 2. 为什么现在值得关注（活跃度证据）
- 2026 上半年密集产出：Smashing Magazine（02-11）、p0stman 时间线（08-05）、AI UX Playground（08-07）、agentic-design.ai（08-03 更新）——设计社区已形成共识而非孤例["https://www.p0stman.com/agent-ux"]
- 工业界落地：MS 发布明确 agent UX 指南（actions must be visible and controllable）、MCP Apps 进入主流 agent 客户端["https://www.p0stman.com/agent-ux"]
- 信任与成本成为新 UX 需求：token/成本透明化为"felt UX requirement"["https://www.p0stman.com/agent-ux"]
## 3. 与我的连接
- **连接的项目**：**TeamMind**（多 Agent 运行时需要产品化交互面）、**campus_order**（OpenClaw 生态的浏览器 UI 重建可直接借鉴）、agent-attention（通知/背景任务模式）、Tafcm（移动端 agent UI）
- **连接的知识点**：EP 原则（可见性/可控性）、五维模型 Orchestration、Human-Agent Collaboration、Context Engineering 的"计划可见性"
- **潜在收益**：补 G2"AI 原生产品"空白；"diff 预览即确认"与我的 Validation 编译器"Evidence→Judgment"在产品层同构；五级自主度框架可反哺权限边界设计（EP-002）
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://agentic-design.ai/zh/patterns/ui-ux-patterns ｜ https://www.aiuxplayground.com/frameworks/agentic/ ｜ https://www.smashingmagazine.com/2026/02/designing-agentic-ai-practical-ux-patterns/ ｜ https://zylos.ai/research/2026-05-28-agentic-ux-frontend-design-patterns-ai-agents/ ｜ https://github.com/bitcomplete/agentic-craft/blob/main/docs/research.md |
| 证据等级 | **FACT（设计社区一手来源，多站点交叉）** |
| 验证方式 | 抽取五级自主度 + 六模式 → 映射到 TeamMind 的 UI 需求 → 产出"agent 交互模式 checklist"供 campus_order 参考 |
| 预期完成时间 | 2026-09/10 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
