# 候选证据卡 · [cand] Computer/Browser Use 工具集 GA + browser-use 生态

> 状态：`[cand]` ｜ 分类：Browser/Computer Use / Agent Harness ｜ 发现：2026-09-01 ｜ 等级：**A**

## 一句话定位
2026 年"Agent 操作真实环境"能力集中 GA：Claude browser use / computer use 工具集去掉 beta、browser-use 成为开源事实标准、Playwright MCP 服务化——Agent 从"对话"走向"动手"。

## 1. 它是什么 / 解决什么问题
- **Claude browser use tool**（`browser_toolset_20260801`，2026-05-27 上线，GA）：运行在你应用托管的浏览器里，读 accessibility tree/元素/表单/标签页，27 个内置成员工具 + 4 个可选（文件上传/JS 执行等），不依赖整机桌面["https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool"][https://platform.claude.com/docs/en/release-notes/overview#may-27-2026]
- **Claude computer use tool**（`computer_toolset_20260801`）：整桌面操作，GA，无需 beta header["https://platform.claude.com/docs/en/agents-and-tools/tool-use/computer-use-tool?product_id=1010787"]
- **browser-use**（Python/Playwright）：开源事实标准，MCP-native，Claude Code/Codex/Cursor/Hermes/OpenClaw 直接可用["https://github.com/browser-use/browser-use/"]
- 生态选择：嵌入式产品→Claude Computer Use；自托管开源→browser-use；MCP 生态→Playwright MCP servers["https://ztabs.co/blog/ai-browser-automation-2026"]

## 2. 与我的知识/项目关系
- **campus_order（OpenClaw 接入）**：OpenClaw 已兼容 browser-use 生态，可直接给校园场景加"Agent 代操作"
- **E2E-CLI（遗留测试项目）**：Playwright MCP + browser-use 让 E2E 测试从"脚本"变"Agent 自主修复"
- **agent-attention**：browser use 的"可见性/反馈"与通知基础设施可联动
- 与我的 Tool System 知识直接碰撞：真实环境操作的工具边界/权限问题

## 3. 证据与活跃度
| 项 | 内容 |
|---|---|
| 证据等级 | FACT（Claude 官方文档 + 生态多源） |
| 来源 | https://platform.claude.com/docs/en/agents-and-tools/tool-use/browser-use-tool ｜ https://github.com/browser-use/browser-use/ |
| 活跃度 | 极高（2026-08 持续更新；Claude 平台 release notes 密集） |

## 4. 验证计划
- [ ] 跑一次 browser-use 最小 demo（任务：抓取并导出结构化数据）
- [ ] 评估给 campus_order/OpenClaw 加 browser-use 的可行性
- [ ] 与 Claude browser use 对比"托管浏览器 vs 自托管"取舍

## 5. 决策
- [ ] 晋升 validated
- [x] 维持观察
- [ ] 拒绝
