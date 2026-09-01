# 候选证据卡 · [cand] DeepSeek Harness v0.1（开源 Agent Harness）
> 状态：`[cand]` ｜ 分类：Agent Runtime / Harness（S5） ｜ 发现：2026-09-02（雷达） ｜ 等级：**S**
## 一句话定位
DeepSeek 于 2026-08-13 发布的 Agent Harness 开发者预览版 v0.1，MIT 协议开源，主打"一切皆插件"（模型/工具/技能/会话/沙箱/存储/循环/调度/UI 全部基于 Cordis 元框架可替换），并提供标准/PTC/极简/创造四种运行模式——是 2026 年开源的又一 agent harness 落地样本。
## 1. 它是什么 / 解决什么问题
- 解决"如何把 LLM 能力组织成可插拔、可复用的 Agent 运行时"——从单点工具走向 harness 层统一抽象["https://deepseek.csdn.net/6a7e851810ee7a33f29ace99.html"]
- 与 Omnigent（meta-harness）、MS Agent Framework 同属 2026 Harness/Control Plane 范式收敛的一部分，但路线不同：**Cordis 元框架 + 全组件可替换插件**，近似"Agent 版 Spring"
- 四种运行模式（标准/PTC/极简/创造）说明它在探索不同使用场景的 harness 配置化
## 2. 为什么现在值得关注（活跃度证据）
- 2026-08-13 开源（DevPreview v0.1），MIT 许可，首个 DeepSeek Agent 产品，发布即引发社区盘点["https://deepseek.csdn.net/6a7e851810ee7a33f29ace99.html"]
- 与"Model + Harness 时代"叙事直接呼应（Claude Code/Codex/OpenClaw 并列的国产竞品）["https://deepseek.csdn.net/6a7e851810ee7a33f29ace99.html"]
## 3. 与我的连接
- **连接的项目**：TeamMind（Java 多 Agent 运行时）——同为"项目级 harness"，可借鉴其插件化架构与运行模式设计；agent-attention（可作 harness 的协作/通知插件）
- **连接的知识点**：Harness/Control Plane 候选方向（agent-harness-control-plane.md）、五维模型（本质/架构/Runtime/Orchestration）、EP-002 权限边界（沙箱作为可替换插件）
- **潜在收益**：一个可本地跑通的开源 harness 参考实现，用于 TeamMind 架构对照与"如何模块化 agent 运行时"的实证；PTC/极简等运行模式可映射到我的不同项目需求
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | GitHub 官方仓库（deepseek-ai 系）+ 官方发布说明（需定位仓库 URL） |
| 证据等级 | FACT（发布事实）待核验仓库存在性；架构主张为 DESIGN |
| 验证方式 | clone 源码 → 通读插件机制（Cordis）→ 对照 TeamMind 模块划分 → 评估是否可跑 quickstart |
| 预期完成时间 | 2026-09 内 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
