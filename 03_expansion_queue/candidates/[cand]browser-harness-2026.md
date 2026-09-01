# 候选证据卡 · [cand] Browser Harness（browser-use 生态的 Self-Healing CDP Harness）
> 状态：`[cand]` ｜ 分类：Computer Use / Browser Automation（S5） ｜ 发现：2026-09-02（雷达） ｜ 等级：**A**
## 一句话定位
browser-use 团队推出的 `browser-harness`（MIT，2026-04 起，15.7k+ stars）：极简、自愈的浏览器 harness——直接基于 CDP 一根 WebSocket 连 Chrome，让 LLM 在 `agent-workspace/` 内"边跑边写缺失代码"，无框架、无 recipes、无 rails，harness 每次运行自我改进。
## 1. 它是什么 / 解决什么问题
- 解决"浏览器自动化 agent 的脆弱性"：传统框架（Playwright 封装）预设行为边界，复杂任务易卡壳；browser-harness 让 agent 在执行中动态补写 helpers/工具，自愈式完成任意浏览器任务["https://github.com/browser-use/browser-harness"]["https://github.com/femto/browser-harness"]
- 技术栈：直接 CDP + agent-workspace 内代码生成，persistent browser / cloud browser 等 tag 全覆盖["https://github.com/DavidWells/stars/blob/master/stars/browser-use/browser-harness.md"]
## 2. 为什么现在值得关注（活跃度证据）
- 15.7k stars（2026-07 快照），PyPI browser-harness 0.1.6（2026-07-17）["https://pypi.org/project/browser-harness/0.1.6/"]
- browser-use 生态（computer use GA 相关）的官方延伸，社区活跃["https://github.com/DavidWells/stars/blob/master/stars/browser-use/browser-harness.md"]
- 与 2026 年"agent 自改代码/自愈 harness"趋势一致（同 Webwright、DeepSeek Harness 的理念）
## 3. 与我的连接
- **连接的项目**：**campus_order（OpenClaw 智能体）**——浏览器操作场景；**E2E-CLI（E2E 测试）**——自动化验证；**agent-attention**——可与 browser agent 协作通知；Computer Use 方向（computer-browser-use-2026.md）
- **连接的知识点**：Harness/Control Plane（S5）、EP-002 权限边界（自愈写代码 = 高风险权限需边界）、五维模型 Tool 维度
- **潜在收益**：一套可跑通的"让 agent 自己写代码完成浏览器任务"的最小参考，用于评估 E2E-CLI 升级路线；与 OpenClaw/browser-use 已有知识形成对照
## 4. 证据与验证计划
| 项 | 内容 |
|---|---|
| 一手来源 | https://github.com/browser-use/browser-harness ｜ https://pypi.org/project/browser-harness/ |
| 证据等级 | FACT（仓库/包信息） |
| 验证方式 | 本地 pip 安装 + 一个真实浏览器任务 demo；评估 agent-workspace 自愈机制的安全边界（EP-002 视角） |
| 预期完成时间 | 2026-09 内 |
## 5. 验证结果
<!-- 待回填 -->
## 6. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
