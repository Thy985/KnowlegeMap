# 候选证据卡 · [cand] MS Research Webwright（Terminal-Native Web Agent 框架）
> 状态：`[cand]` ｜ 分类：Computer Use / Web Agent（S5） ｜ 发现：2026-09-02（雷达） ｜ 等级：**B**
## 一句话定位
Microsoft Research 开源的终端原生 Web Agent 框架（`microsoft/Webwright`，2026）：让 agent 用 Playwright 写代码控制浏览器、跑 bash、查日志、迭代脚本，把"浏览器会话"当作可启动/检查/丢弃的进程——持久产物是**可复用脚本**而非一次性会话。
## 1. 它是什么 / 解决什么问题
- 解决"web agent 会话状态难复现"：agent 产出可维护、可回放、可审查的 Playwright 脚本（而非一次性浏览器会话）["http://microsoft.github.io/Webwright/"]
- Agent Loop：Runner 送上下文 → 模型返回 thinking + shell command → Environment 返回终端输出/日志/截图/报错 → 循环直到完成
- **一手核验（2026-09-02）**：GitHub `microsoft/Webwright` ✅（含 skill_factory 模块、Web Skill Factory：可复用/可验证的 code-native skills）、官方页 microsoft.github.io/Webwright ✅、MSR writeup ✅、arXiv/论文《Webwright: A terminal is all you need for web agents》(Lu, Xu, Huang, Awadallah, 2026) ✅
- 脚本可复用在 Claude Code / Codex / OpenClaw（host 驱动，无需额外 LLM key）["https://github.com/microsoft/Webwright/blob/main/README.md"]
## 2. 为什么现在值得关注（活跃度证据）
- 基准：Online-Mind2Web 86.7% / Odysseys 60.1%（基线 GPT-5.4 33.5%），接近翻倍
- 安装路径清晰：clone → venv → pip install -e . → playwright install chromium → 配 model["https://github.com/microsoft/Webwright/tree/main/src/webwright/skill_factory"]
- 与 Browser Harness / DeepSeek Harness 的"自愈、可编程、轻框架"理念同源，说明方向已成熟
## 3. 与我的连接
- **连接的项目**：E2E-CLI（E2E 测试与修复）——脚本化浏览器 = E2E 的自然升级；campus_order（OpenClaw web 操作）
- **连接的知识点**：Computer Use（computer-browser-use-2026.md）、AI 放大软件工程（测试/CI 方法论）、Skills 资产（Web Skill Factory 与我的 Skills 体系同构）
- **潜在收益**：为 E2E-CLI 提供"脚本而非会话"的设计参考 + Skill Factory 思路；符合可复现/可审查的验证纪律
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/microsoft/Webwright ｜ http://microsoft.github.io/Webwright/ ｜ MSR writeup ｜ arXiv 论文 |
| 证据等级 | **FACT（官方 GitHub + 官方页 + MSR writeup + 论文四重核验通过）** |
| 验证方式 | 读论文/源码（skill_factory）→ 对比 browser-use 路线 → 评估 E2E-CLI 升级可行性 |
| 预期完成时间 | 观察期（2026-09 内决定是否深入） |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
