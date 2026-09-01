# 03 · Project Landscape

> 数据来源：GitHub（Thy985，14 公开仓库，2026-09-01 抓取）+ 飞书知识库项目 Hub。
> 用途：回答"我在做什么项目、每个项目缺什么、外部技术怎么接进来"。

---

## 一、公开仓库全景（按活跃度排序）

| # | 项目 | 语言 | 一句话定位 | 阶段 | 活跃度 |
|---|---|---|---|---|---|
| 1 | **Tafcm** | Dart | 移动端 Typora 级 Markdown/公式写作工具（WYSIWYG、LaTeX→SVG、Mermaid、ADI 诊断接口、ffx-cli 工具链） | Phase 3.12 Info Architecture | 🔴 极高（当日更新） |
| 2 | **silver-shield** | Python | 老年人诈骗风险数字孪生与协同预警（萤石摄像头感知→事件→规则→决策→预警→家属/社区协同） | MVP RC v0.1.0 + v2 设计 | 🔴 极高（当日更新） |
| 3 | **weather-recognition** | Jupyter | 证据追踪式天气图像分类实证研究（小样本+隐藏分布偏移；最终 Platform F1 0.9137） | ✅ 完成（方法论母矿） | 🟢 稳定 |
| 4 | **agent-attention** | TypeScript | Windows Agent 通知基础设施（agent-notify CLI → daemon → Toast/托盘/Center；支持 Claude/Codex/Aider 集成） | v0.3 | 🟠 高 |
| 5 | **huaBan-pro** | C++ | 像素画软件 | 早期 | 🟡 中 |
| 6 | **TeamMind** | Java | 项目级 AI 团队运行时：给每个项目配多 Agent（Codex/Claude/Aider）团队，共享状态、角色分工、自动进化 | 概念→MVP | 🟡 中 |
| 7 | **multi_arm_line_ws** | Python | 多机械臂探索（ROS workspace） | 探索期 | 🟡 中 |
| 8 | **GrowthOS** | TypeScript | 个人经验管理系统（经历→反思→抽象→迁移→能力；AI 成长教练） | 概念/早期 | 🟡 中 |
| 9 | **Blog** | - | 个人博客 | 维护中 | 🟢 |
| 10 | **KnowlegeMap** | Markdown | 本仓库：个人技术世界边界模型 | 🟢 Bootstrap 完成 | 🟢 本次 |
| 11 | **E2E-CLI** | TypeScript | E2E 测试与修复 | 遗留 | ⚪ 低 |
| 12 | **myBlog** | Java | 接入 OpenClaw 的博客 | 遗留 | ⚪ 低 |
| 13 | **AI-blog** | - | AI 驱动博客 | 遗留 | ⚪ 低 |
| 14 | **campus_order** | HTML/全栈 | 高校订餐平台（三角色 + OpenClaw 智能体 + 飞书接入） | 早期/演示 | ⚪ 低 |

## 二、内库项目 Hub（飞书 · 05 项目）

| Hub | 状态 | 说明 |
|---|---|---|
| Weather Recognition | ✅ 完整（55 篇知识资产） | 已完成项目 + 方法论提取范例 |
| FormulaFix | 骨架 | 用户历史项目（前端/LaTeX 渲染修复），待填充 |
| TeamMind | 骨架 | 与 GitHub 同名项目对应 |
| DSH | 骨架 | 疑与 silver-shield 同源（Digital Safety/Shield 系列） |
| dsh-pentest | 骨架 | 攻防向项目，**对应 AI 安全方向，知识库完全未填充** |

## 三、项目间关系图

```
                 ┌─────────────────────────────────────────────┐
                 │           AI Agent 基础设施生态              │
                 │   TeamMind(编排) → agent-attention(通知)     │
                 │   Tafcm(ADI诊断) → AI Company OOS(组织治理)  │
                 └─────────────────────────────────────────────┘
                                        │ 共享"证据/验证"纪律
                 ┌─────────────────────────────────────────────┐
                 │         证据驱动工程纪律（方法论层）           │
                 │   weather-recognition → ML 实验方法论        │
                 │   silver-shield → Validation/ADR/CI 体系     │
                 └─────────────────────────────────────────────┘
                                        │
                 ┌─────────────────────────────────────────────┐
                 │           AI 安全应用（G1 缺口方向）          │
                 │   silver-shield(防诈骗) → dsh-pentest(攻防)  │
                 └─────────────────────────────────────────────┘
                 ┌─────────────────────────────────────────────┐
                 │           个人生产力（外圈）                 │
                 │   Tafcm(写作) → GrowthOS(经验) → Blog(输出)  │
                 └─────────────────────────────────────────────┘
```

## 四、每个项目的缺口与外部连接候选

| 项目 | 当前缺什么 | 外部技术连接候选 |
|---|---|---|
| **Tafcm** | 移动端发布、Agent 自主修复闭环、公式渲染性能 | ONNX/WebGPU 本地渲染、MCP server（暴露文档操作）、Evals 化 ADI |
| **silver-shield** | 实时风险流未接通、音频链路待集成、真实部署、风险模型精度 | 边缘 AI（TFLite/YAMNet）、可解释 AI 工具、隐私计算、对抗鲁棒性测试 |
| **weather-recognition** | 方法论已提取，可复用为模板 | Data-Centric 工具（Cleanlab/Snorkel）、自动化实验框架 |
| **TeamMind** | 进化证据不足、真实项目实证、多 Agent 状态同步 | MCP/A2A 协议、LangGraph/CrewAI 对比、Agent 评测（SWE-bench 类） |
| **agent-attention** | 跨平台（macOS/Linux）、Agent 生态覆盖 | MCP 通知扩展、桌面通知标准、daemon 可观测性 |
| **GrowthOS** | 数据模型落地、AI 教练接入 | 向量记忆（Mem0/Zep）、LLM eval、反思框架（Reflexion） |
| **huaBan-pro** | 产品化 | 图形学算法、跨平台渲染 |
| **campus_order** | 真实运营 | Agentic 客服、支付合规 |
| **dsh-pentest**（内库） | **整个攻防知识 + 项目本体都缺** | AI 漏洞挖掘、红队框架、对抗样本、安全评测基准 |

## 五、跨项目共性结论

1. **所有活跃项目共享同一条"证据纪律"**（ADR/契约测试/CI 门禁/证据分级）——这是最强的方法论资产，可以外推到任何新领域。
2. **Agent 基础设施链是主线**（TeamMind→agent-attention→Tafcm ADI→AI Company OOS），但**缺协议标准层（MCP/A2A）与评测层（Evals）**。
3. **AI 安全应用已有一个产品（silver-shield），但攻防方向（dsh-pentest）是空壳**——与 GitHub 定位一致地形成了最大缺口。
4. 遗留项目（E2E-CLI/myBlog/AI-blog/campus_order）是早期探索，不建议再投入，只保留经验。
