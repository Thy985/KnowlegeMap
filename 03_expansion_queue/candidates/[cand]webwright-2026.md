# 候选证据卡 · [cand] MS Research Webwright（Terminal-Native Web Agent 框架）
> 状态：`[cand]` ｜ 分类：Computer Use / Web Agent（S5） ｜ 发现：2026-09-02（雷达） ｜ 等级：**B**
## 一句话定位
Microsoft Research 2026 发布的 Webwright：终端原生的 Web Agent 框架——让 agent 用 Playwright 写代码控制浏览器、跑 bash、查日志、迭代脚本，把"浏览器会话"当作可启动/检查/丢弃的进程，持久产物是脚本而非会话。
## 1. 它是什么 / 解决什么问题
- 解决"web agent 会话状态难复现"：把浏览器当成 agent 可编程的进程，agent 产出的是可维护的 Playwright 脚本（不是一次性会话），任务可回放、可审查["https://aifuturefront.com/microsoft-research-releases-webwright-a-terminal-native-web-agent-framework-that-scores-60-1-on-odysseys-up-from-base-gpt-5-4s-33-5/"]
- 效果：Odysseys 基准 60.1%（基线 GPT-5.4 33.5%），接近翻倍
## 2. 为什么现在值得关注（活跃度证据）
- Microsoft Research 出品 + 基准显著提升 + 与"agent 写代码而非点 UI"的 2026 范式一致["https://aifuturefront.com/microsoft-research-releases-webwright-a-terminal-native-web-agent-framework-that-scores-60-1-on-odysseys-up-from-base-gpt-5-4s-33-5/"]
- 与 Browser Harness / DeepSeek Harness 的"自愈、可编程、轻框架"理念同源，说明方向已成熟
## 3. 与我的连接
- **连接的项目**：E2E-CLI（E2E 测试与修复）——脚本化浏览器 = E2E 的自然升级；campus_order（OpenClaw web 操作）
- **连接的知识点**：Computer Use（computer-browser-use-2026.md）、AI 放大软件工程（测试/CI 方法论）
- **潜在收益**：为 E2E-CLI 提供"脚本而非会话"的设计参考，符合可复现/可审查的验证纪律
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | Microsoft Research 发布页 / 论文（需核验 GitHub 与论文 URL） |
| 证据等级 | FACT（发布事实）待核验；基准数字来自第三方报道需交叉核对 |
| 验证方式 | 读论文/源码 → 对比 browser-use 路线 → 评估 E2E-CLI 升级可行性 |
| 预期完成时间 | 观察期（2026-09 内决定是否深入） |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
